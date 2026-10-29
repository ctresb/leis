"""Baixa diários oficiais de Salvador (portal CMS Dioly) e extrai atos promulgados.

O índice vem de `GET https://portal-api.dioly.com.br/api/diarios/?page=N` (≤2 req/s). A busca
`q=` do próprio CMS localiza edições cujo PDF menciona a frase. PDFs são retomáveis em
`municipais/_fonte/dioly/`. O texto sai de `pdftotext -raw` (histórias InDesign).

`--modo emendas` (padrão) lê o DOL e fica só com emendas à LOM promulgadas pela Mesa.
`--modo leis-complementares` lê o DOM e fica só com leis complementares sancionadas
(epígrafe `LEI COMPLEMENTAR Nº`, Art. 1º, sanção, gabinete). Projetos ficam de fora.
Citações a LC em portaria, contrato ou balanço não entram.
`--modo leis-ordinarias` lê o DOM e fica só com leis ordinárias sancionadas (epígrafe
`LEI Nº 9.829/2025` em caixa alta, sem COMPLEMENTAR; Art. 1º, sanção e gabinete do prefeito
datado até 1 ano antes da edição). Leis antigas reproduzidas em edital/anexo ficam de fora.
`--modo resolucoes` e `--modo decretos-legislativos` leem o DOL e ficam só com atos promulgados
pela Mesa (epígrafe em linha própria, Art. 1º, promulga/faz saber, Sala das Sessões no ano).
`--modo decretos` lê o DOM e fica só com decretos numerados do Prefeito (`DECRETO Nº N de …`
em linha própria, DECRETA:, Art. 1º, GABINETE DO PREFEITO + Prefeito). Decretos legislativos,
decretos simples sem número e retificações ficam de fora. Todos os modos somam aos md já
gravados: (número, ano) presente de outra edição fica com o md antigo.
"""
import argparse
import collections
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote, urlsplit, urlunsplit

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import (  # noqa: E402
    CANONICO, Rede, normalizar_chave, pdf_escaneado, slugify, texto_pdf_para_md, yaml_str,
)
from datas import MESES, POR_EXTENSO  # noqa: E402
from extrair_diario_municipal import SHA_EXTRATOR as SHA_GEOMETRIA  # noqa: E402
from extrair_diario_municipal import VERSAO as EXTRATOR_GEOMETRIA  # noqa: E402
from extrair_diario_municipal import linhas_palavras  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
API = "https://portal-api.dioly.com.br/api/diarios/"
IBGE_SALVADOR = "2927408"
MUNICIPIO = "Salvador"
UF = "BA"
EXTRATOR = "dioly-raw-v2"
CONSULTAS_PADRAO = (
    "EMENDA À LEI ORGÂNICA",
    "EMENDA A LEI ORGANICA",
    "Emenda à Lei Orgânica do Município",
    "PROMULGA A SEGUINTE EMENDA",
)
CONSULTAS_LC = (
    "LEIS COMPLEMENTARES",
    "a seguinte Lei Complementar:",
    "sanciono a seguinte Lei Complementar",
    "sanciono a seguinte Lei:",
    "Altera dispositivos da Lei Complementar",
)
CONSULTAS_LO = (
    "sanciono a seguinte Lei:",
    "Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei",
    "a seguinte Lei:",
)

EPIGRAFE = re.compile(
    r"EMENDA\s+N[ºo°.]?\s*(?P<num>\d{1,3})\s+[ÀA]\s+LEI\s+ORG[ÂA]NICA"
    r"|EMENDA\s+[ÀA]\s+LEI\s+ORG[ÂA]NICA(?:\s+DO\s+MUNIC[ÍI]PIO)?\s+N[ºo°.]\s*(?P<num2>\d{1,3})"
    r"|EMENDA\s+[ÀA]\s+LOM\s+N[ºo°.]\s*(?P<num3>\d{1,3})",
    re.I,
)
INICIO_ATO = re.compile(
    r"^(?:EMENDA\s+(?:N[ºo°.]?\s*)?\d{1,3}\s+[ÀA]\s+LEI\s+ORG[ÂA]NICA"
    r"|EMENDA\s+[ÀA]\s+LEI\s+ORG[ÂA]NICA"
    r"|EMENDA\s+[ÀA]\s+LOM\s+N"
    r"|PROJETO\s+DE\s+EMENDA"
    r"|LEI\s+(?:COMPLEMENTAR\s+)?N[ºo°.]"
    r"|RESOLU[ÇC][ÃA]O\s+N[ºo°.]"
    r"|DECRETO\s+(?:LEGISLATIVO\s+)?N[ºo°.])",
    re.I | re.M,
)
PROXIMO_ATO = re.compile(
    r"^(?:PROJETO\s+DE\s+EMENDA"
    r"|RESOLU[ÇC][ÃA]O\s+N[ºo°.]"
    r"|DECRETO\s+(?:LEGISLATIVO\s+)?N[ºo°.]"
    r"|LEI\s+(?:COMPLEMENTAR\s+)?N[ºo°.]"
    r"|EMENDA\s+N[ºo°.]\s*\d{1,3}\s+[ÀA]\s+LEI\s+ORG)",
    re.I | re.M,
)
PROMULGA = re.compile(
    r"promulg\w*.{0,160}a\s+seguinte\s+emenda\s+[àa]\s+(?:lei\s+org|lom)"
    r"|a\s+seguinte\s+emenda\s+[àa]\s+lei\s+org[aâ]nica"
    r"|a\s+mesa\s+da\s+c[aâ]mara.{0,240}emenda\s+[àa]\s+lei\s+org",
    re.I | re.S,
)
FIM_JORNAL = re.compile(
    r"^(?:DOLM?\s|Ano\s+[IVXLC]+\b|Criado pela Lei|Quinta-feira|Sexta-feira|"
    r"Segunda-feira|Ter[cç]a-feira|Quarta-feira|S[aá]bado|Domingo|"
    r"Assessoria de|www\.cms\.ba\.gov\.br|Câmara vai aos|"
    r"F-PL-|DI[AÁ]RIO OFICIAL DO LEGISLATIVO)",
    re.I | re.M,
)
PROMULGA_FRACO = re.compile(r"promulga e manda publicar", re.I)
NEWS = re.compile(
    r"coronav[ií]rus|cestas b[aá]sicas|LOG[IÍ]STICA FALHOU|Câmara vai aos|"
    r"vereadora Marta|quer substituir\s+por dinheiro",
    re.I,
)
CHROME = re.compile(
    r"^(?:F-PL-|DI[AÁ]RIO OFICIAL|P[AÁ]GINA\b|DOLM?\b|Camara_Template|Layout 1)",
    re.I,
)
CARGO = re.compile(
    r"^(?:Presidente|1[ºo°]?\s*Secretári[oa]|2[ºo°]?\s*Secretári[oa]|"
    r"3[ºo°]?\s*Secretári[oa])\b",
    re.I,
)
SESSAO = re.compile(
    r"vereador|expediente|ordem do dia|projeto de (?:lei|indica|resolu)|mo[cç][oõ]es?\b",
    re.I,
)
ARTIGO_LINHA = re.compile(r"^(?:Art\.|§|Parágrafo único|prevista neste artigo)", re.I)
EPIGRAFE_ORIGINAL = re.compile(
    r"^EMENDA\s+N[ºo°.]?\s*\d{1,3}\s+[ÀA]\s+LEI\s+ORG[ÂA]NICA", re.I)
PROJETO = re.compile(r"projeto\s+de\s+emenda\s+[àa]\s+lei\s+org|projeto\s+de\s+emenda\s+[àa]\s+lom", re.I)
ESTATISTICA = re.compile(
    r"emenda\s+[àa]\s+lei\s+org[aâ]nica\s+do\s+munic[ií]pio\s+promulgada\s+\d+\s*$", re.I | re.M)
ARTIGO = re.compile(r"\bArt\.?\s*1[º°o]?\b", re.I)
SALA = re.compile(r"Sala das Sess[oõ]es,?\s+em\s+[oO]?\s*" + POR_EXTENSO.pattern, re.I)
CABECALHO_PAGINA = re.compile(
    r"^(?:DOLM?\s+\d|Ano\s+[IVXLC]+\s*[-–—]|P[aá]gina\s+\d+|Sexta-feira,|Segunda-feira,"
    r"|Ter[cç]a-feira,|Quarta-feira,|Quinta-feira,|S[aá]bado,|Domingo,"
    r"|Terça, Quarta e Quinta-feira)\b", re.I)

EPIGRAFE_LC = re.compile(
    r"LEI\s+COMPLEMENTAR\s+N[ºo°.]?\s*(?P<num>\d{1,3})\s*/\s*(?P<ano>\d{4})",
    re.I,
)
INICIO_LC = re.compile(
    r"^(?:PROJETO\s+DE\s+LEI\s+COMPLEMENTAR"
    r"|LEI\s+COMPLEMENTAR\s+N[ºo°.]?\s*\d{1,3}\s*/\s*\d{4}"
    r"|LEI\s+N[ºo°.]?\s*[\d.]+\s*/\s*\d{4}"
    r"|DECRETO\s+N[ºo°.]"
    r"|DECRETOS?\s+FINANCEIROS"
    r"|PORTARIA\s+N[ºo°.]"
    r"|PORTARIAS?\b"
    r"|RESOLU[ÇC][ÃA]O\s+N[ºo°.])",
    re.I | re.M,
)
SANCIONO_LC = re.compile(
    r"sanciono a(?:\s+seguinte)?\s+Lei(?:\s+Complementar)?\s*:"
    r"|decreta e eu sanciono",
    re.I,
)
PROJETO_LC = re.compile(r"projeto\s+de\s+lei\s+complementar", re.I)
GABINETE_LC = re.compile(
    r"GABINETE DO PREFEITO.{0,80},\s*em\s+"
    r"(?P<dia>\d{1,2})\s+(?:de\s+)?(?P<mes>\w+)\s+de\s+(?P<ano>\d{4})",  # "em 28 março de 2025" (DOM 9001)
    re.I,
)
REPUBLICADA = re.compile(r"Republicada por ter sa[ií]do com incorre", re.I)
CHROME_LC = re.compile(
    r"^(?:DI[AÁ]RIO OFICIAL DO(?:\s+MUNIC[IÍ]PIO(?:\s+DO\s+SALVADOR)?)?|"
    r"SALVADOR[-–—• ]+BAHIA|SALVADOR-BAHIA|"
    r"ANO\s+[IVXLC]+\s*\|?\s*N\s*[ºo°.]?\s*[\d.]+(?:\s+\d{1,3})?|"
    r"(?:Segunda|Ter[cç]a|Quarta|Quinta|Sexta)-feira|S[aá]bado|Domingo|"
    r"[0-3]?\d DE (?:JANEIRO|FEVEREIRO|MAR[CÇ]O|ABRIL|MAIO|JUNHO|JULHO|"
    r"AGOSTO|SETEMBRO|OUTUBRO|NOVEMBRO|DEZEMBRO) DE 20\d{2}|"
    r"Ouvidoria Geral do Munic[ií]pio|Disque Salvador|"
    r"Di[aá]rio Oficial do Munic[ií]pio - Edi[cç][oõ]es Anteriores|"
    r"CEP:\s*40\.020-000|Coordenador de Tecnologia|"
    r"www\.(?:ouvidoria|disquesalvador|dom)\.|atendimento 24h\.?"
    r")\s*$", re.I)
COLOFON_LC = re.compile(r"Criado pelo art\.\s*82 da Lei n", re.I)
CARGO_LC = re.compile(
    r"^(?:Prefeito|Chefe de Gabinete|Chefe da Casa Civil|Secretári[oa]\b|"
    r"Procurador|em exerc[ií]cio)\b",
    re.I)
LETRA_VERTICAL_LC = re.compile(r"^[EDIÇÃOEXTRAÇÃOedicaoextra]{1}$")


def indice_itens(bruto):
    if isinstance(bruto, list):
        return bruto
    if isinstance(bruto, dict) and isinstance(bruto.get("items"), list):
        return bruto["items"]
    raise ValueError("índice Dioly: esperado lista de edições ou objeto com items")


def carregar_indice(caminho):
    return indice_itens(json.loads(Path(caminho).read_text()))


def gravar_json(caminho, dados):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    tmp = caminho.with_suffix(caminho.suffix + ".tmp")
    tmp.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(caminho)


def baixar_indice(rede, tipo=None, consulta=None, per_page=100):
    itens, pagina = [], 1
    while True:
        q = [("page", str(pagina)), ("per_page", str(per_page))]
        if tipo:
            q.append(("tipo", tipo))
        if consulta:
            q.append(("q", consulta))
        from urllib.parse import urlencode
        st, bruto, _ = rede.get(API + "?" + urlencode(q), tentativas=4, timeout=90)
        if st != 200:
            raise RuntimeError("API Dioly HTTP %s na página %s" % (st, pagina))
        corpo = json.loads(bruto.decode("utf-8"))
        lote = corpo.get("items") or []
        itens.extend(lote)
        total_paginas = int(corpo.get("total_pages") or 1)
        if pagina >= total_paginas or not lote:
            break
        pagina += 1
    return itens


def candidatos(rede, tipo="DOL", consultas=None):
    por_id = {}
    for consulta in (consultas or CONSULTAS_PADRAO):
        for item in baixar_indice(rede, tipo=tipo, consulta=consulta):
            por_id[item["id"]] = item
    return [por_id[k] for k in sorted(por_id)]


def filtrar_edicoes(itens, tipo="DOL", inicio=None, fim=None):
    saida = []
    for item in itens:
        if tipo and item.get("tipo") != tipo:
            continue
        data = item.get("data_publicacao") or ""
        if inicio and data < inicio:
            continue
        if fim and data > fim:
            continue
        if not item.get("pdf_url"):
            continue
        saida.append(item)
    return sorted(saida, key=lambda x: (x.get("data_publicacao") or "", x.get("numero") or 0, x["id"]))


def url_segura(url):
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, quote(p.path, safe="/-._~()"), p.query, p.fragment))


def caminho_pdf(pasta, item):
    data = item.get("data_publicacao") or "sem-data"
    tipo = item.get("tipo") or "DOL"
    numero = item.get("numero") or item["id"]
    return Path(pasta) / ("%s-%s-%s.pdf" % (data, tipo, numero))


def baixar_pdf(rede, item, destino):
    destino = Path(destino)
    if destino.exists() and destino.stat().st_size > 100 and destino.read_bytes()[:4] == b"%PDF":
        return destino.read_bytes(), True
    st, bruto, tipo = rede.get(url_segura(item["pdf_url"]), tentativas=4, timeout=180)
    if st != 200 or not bruto.startswith(b"%PDF"):
        raise RuntimeError("PDF indisponível HTTP %s tipo=%s" % (st, tipo))
    destino.parent.mkdir(parents=True, exist_ok=True)
    tmp = destino.with_suffix(".pdf.tmp")
    tmp.write_bytes(bruto)
    tmp.replace(destino)
    return bruto, False


def palavras_pagina(page):
    ns = "{http://www.w3.org/1999/xhtml}"
    out = []
    for linha in page.iter(ns + "line"):
        for w in linha.iter(ns + "word"):
            t = "".join(w.itertext())
            if t.strip():
                out.append((float(w.attrib["xMin"]), float(w.attrib["yMin"]),
                            float(w.attrib["xMax"]), float(w.attrib["yMax"]), t))
    return out


def cortes_y(words, passo=3, vazio=4):
    y0 = min(w[1] for w in words)
    y1 = max(w[3] for w in words)
    n = int((y1 - y0) / passo) + 1
    occ = [0] * n
    for w in words:
        a = int((w[1] - y0) / passo)
        b = int((w[3] - y0) / passo)
        for i in range(max(0, a), min(n, b + 1)):
            occ[i] += 1
    cortes = [y0]
    i = 0
    while i < n:
        if occ[i] == 0:
            j = i
            while j < n and occ[j] == 0:
                j += 1
            if j - i >= vazio:
                cortes.append(y0 + (i + j) / 2 * passo)
            i = j
        else:
            i += 1
    cortes.append(y1 + 1)
    return cortes


def gutters(words, width):
    """Vales de cobertura vertical perto do centro: 1 vale → 2 colunas; 2 vales → 3."""
    bins = 80
    cov = [0] * bins
    for w in words:
        a = int(w[0] / width * bins)
        b = int(w[2] / width * bins)
        for i in range(max(0, a), min(bins, b + 1)):
            cov[i] += 1
    ini, fim = int(bins * 0.28), int(bins * 0.72)
    limiar = max(2, int(max(cov[ini:fim] or [0]) * 0.12))
    vales, i = [], ini
    while i < fim:
        if cov[i] <= limiar:
            j = i
            while j < fim and cov[j] <= limiar:
                j += 1
            if j - i >= 2:
                vales.append((i + j) / 2 / bins * width)
            i = j
        else:
            i += 1
    # funde vales vizinhos
    unidos = []
    for x in vales:
        if unidos and abs(x - unidos[-1]) < width * 0.08:
            unidos[-1] = (unidos[-1] + x) / 2
        else:
            unidos.append(x)
    return unidos[:2]


def texto_faixa(words, width):
    if len(words) < 8:
        return linhas_palavras(words)
    cortes = gutters(words, width)
    if not cortes:
        meio = width / 2
        esq = sum(1 for w in words if (w[0] + w[2]) / 2 < meio)
        dir_ = len(words) - esq
        if min(esq, dir_) >= 8 and min(esq, dir_) / max(esq, dir_) > 0.25:
            cortes = [meio]
        else:
            return linhas_palavras(words)
    limites = [0.0] + cortes + [width]
    colunas = []
    for a, b in zip(limites, limites[1:]):
        col = [w for w in words if a <= (w[0] + w[2]) / 2 < b]
        if col:
            colunas.append(linhas_palavras(col))
    return "\n\n".join(colunas)


def texto_bbox(pdf):
    with tempfile.TemporaryDirectory() as pasta:
        xml = Path(pasta) / "paginas.html"
        subprocess.run(["pdftotext", "-bbox-layout", "-enc", "UTF-8", str(pdf), str(xml)],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=300)
        paginas = []
        for _, el in ET.iterparse(xml, events=("end",)):
            if el.tag.endswith("}page"):
                paginas.append((float(el.attrib["width"]), float(el.attrib["height"]), palavras_pagina(el)))
                el.clear()
    blocos = []
    for width, _altura, words in paginas:
        if not words:
            continue
        cortes = cortes_y(words)
        for a, b in zip(cortes, cortes[1:]):
            faixa = [w for w in words if a <= (w[1] + w[3]) / 2 < b]
            if faixa:
                txt = texto_faixa(faixa, width)
                if txt.strip():
                    blocos.append(txt)
        blocos.append("\f")
    return "\n".join(blocos)


def texto_layout(pdf):
    r = subprocess.run(["pdftotext", "-q", "-layout", "-enc", "UTF-8", str(pdf), "-"],
                       capture_output=True, timeout=300)
    return r.stdout.decode("utf-8", "replace")


def texto_raw(pdf):
    """Ordem dos text frames do InDesign: no DOL de Salvador, isso preserva a emenda inteira."""
    r = subprocess.run(["pdftotext", "-q", "-raw", "-enc", "UTF-8", str(pdf), "-"],
                       capture_output=True, timeout=300)
    return r.stdout.decode("utf-8", "replace")


def juntar_hifen(texto):
    return re.sub(r"(\w)-\n(\s*)(\w)", r"\1\3", texto or "")


def extrair_texto(pdf):
    """Prefere -raw (histórias InDesign); cai para bbox/layout se o raw vier vazio."""
    try:
        texto = texto_raw(pdf)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError):
        texto = ""
    if len(re.sub(r"\W", "", texto)) < 80:
        try:
            texto = texto_bbox(pdf)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, ET.ParseError, RuntimeError):
            texto = ""
    if len(re.sub(r"\W", "", texto)) < 80:
        texto = texto_layout(pdf)
    return texto


def _nota_bloco(b):
    news = 1 if NEWS.search(b) else 0
    sala = 1 if SALA.search(b) else 0
    prom = 1 if (PROMULGA.search(b) or PROMULGA_FRACO.search(b)) else 0
    tam = -len(b) if sala else len(b)
    return (-news, sala, prom, tam)


def escolher_blocos(pdf):
    """Compara raw/bbox/layout e fica o recorte promulgada mais limpo (Sala, sem notícia)."""
    por_num = {}

    def incorporar(texto):
        if len(re.sub(r"\W", "", texto or "")) < 80:
            return
        for num, bloco in blocos_emenda(juntar_hifen(texto)):
            atual = por_num.get(num)
            if atual is None or _nota_bloco(bloco) > _nota_bloco(atual):
                por_num[num] = bloco

    try:
        incorporar(texto_raw(pdf))
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError):
        pass
    if por_num and all(SALA.search(b) and not NEWS.search(b) for b in por_num.values()):
        return [(n, por_num[n]) for n in sorted(por_num, key=lambda x: int(x or 0))]
    try:
        incorporar(texto_bbox(pdf))
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, ET.ParseError, RuntimeError):
        pass
    try:
        incorporar(texto_layout(pdf))
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError):
        pass
    return [(n, por_num[n]) for n in sorted(por_num, key=lambda x: int(x or 0))]


def numero_epigrafe(m):
    for k in ("num", "num2", "num3"):
        if m.group(k):
            return str(int(m.group(k)))
    return ""


def eh_promulgada(bloco):
    if ESTATISTICA.search(bloco):
        # balanço anual: a linha existe, mas o bloco não é o texto da emenda
        if len(re.sub(r"\W", "", bloco)) < 400:
            return False
    if PROJETO.search(bloco.split("\n")[0] if bloco.strip() else ""):
        return False
    # projeto cujo primeiro parágrafo já se declara proposição
    cabeca = "\n".join(bloco.splitlines()[:8])
    if PROJETO.search(cabeca) and not PROMULGA.search(bloco):
        return False
    if not EPIGRAFE.search(bloco):
        return False
    if not ARTIGO.search(bloco):
        return False
    if not PROMULGA.search(bloco):
        # layout de jornal às vezes parte "a seguinte Emenda"; a epígrafe original
        # + Mesa/promulga + Sala das Sessões ainda identificam a promulgação.
        if not (EPIGRAFE_ORIGINAL.search(bloco.lstrip()) and PROMULGA_FRACO.search(bloco) and SALA.search(bloco)):
            return False
    # emenda parlamentar / orçamentária
    if re.search(r"emendas?\s+parlamentar", bloco, re.I) and not re.search(r"lei\s+org", bloco, re.I):
        return False
    return True


def proximos_inicios(texto):
    achados = []
    for m in INICIO_ATO.finditer(texto):
        achados.append(m.start())
    return achados


def blocos_emenda(texto):
    """Recorta cada emenda promulgada a partir da epígrafe até o próximo ato ou o fim."""
    saida = []
    for m in EPIGRAFE.finditer(texto):
        # recua para o início da linha
        ini = texto.rfind("\n", 0, m.start()) + 1
        prefixo = texto[max(0, ini - 40):ini]
        if PROJETO.search(prefixo) or PROJETO.search(texto[ini:ini + 80]):
            continue
        fim = len(texto)
        for n in PROXIMO_ATO.finditer(texto, m.end()):
            if n.start() < m.end() + 10:
                continue
            trecho = texto[n.start():n.start() + 80]
            em = EPIGRAFE.search(trecho)
            if em and numero_epigrafe(em) == numero_epigrafe(m):
                continue
            fim = n.start()
            break
        bloco = texto[ini:fim]
        bloco = recortar_ato(bloco)
        bloco = limpar_bloco(bloco)
        if eh_promulgada(bloco):
            saida.append((numero_epigrafe(m), bloco))
    # dedup por número: fica o maior bloco (texto mais completo)
    por_num = {}
    for num, bloco in saida:
        # a promulgação original usa "EMENDA Nº N À LEI ORGÂNICA"; a forma
        # "Emenda à LOM nº N" aparece em tramitação, citação e compilação.
        if not re.search(r"EMENDA\s+N[ºo°.]?\s*" + re.escape(num) + r"\s+[ÀA]\s+LEI\s+ORG", bloco, re.I):
            continue
        if num not in por_num or len(bloco) > len(por_num[num]):
            por_num[num] = bloco
    return [(n, por_num[n]) for n in sorted(por_num, key=lambda x: int(x or 0))]


def recortar_ato(bloco):
    """Corta o jornal que segue a promulgação: Sala das Sessões + cargos, nada do expediente."""
    m = SALA.search(bloco)
    if not m:
        return bloco.strip()
    linhas, n = [bloco[:m.end()].rstrip()], 0
    for ln in bloco[m.end():].splitlines():
        s = ln.strip()
        if not s or s == ".":
            continue
        if (FIM_JORNAL.match(s) or INICIO_ATO.match(s) or CABECALHO_PAGINA.match(s)
                or CHROME.match(s) or ARTIGO_LINHA.match(s) or SESSAO.search(s)):
            break
        if len(s) > 80 and not CARGO.search(s):
            break
        n += 1
        if n > 14:
            break
        linhas.append(s)
    return "\n".join(linhas).strip()


def limpar_bloco(bloco):
    linhas = []
    for ln in bloco.splitlines():
        s = ln.strip()
        if not s:
            if linhas and linhas[-1] != "":
                linhas.append("")
            continue
        if CABECALHO_PAGINA.match(s) or CHROME.match(s) or FIM_JORNAL.match(s):
            continue
        if re.fullmatch(r"\d{1,3}", s) or re.fullmatch(r"N[°ºo]\s*[\d.]+", s, re.I):
            continue
        if s in {"LEGISLATIVO", "PODER LEGISLATIVO", "ATOS DO", "ATOS DO PODER",
                 "ATOS DO PODER LEGISLATIVO"}:
            continue
        linhas.append(s)
    texto = re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()
    return texto


def data_do_bloco(bloco, numero, data_edicao):
    m = SALA.search(bloco)
    if m:
        mes = MESES.get(m.group(2).lower())
        if mes:
            try:
                d = dt.date(int(m.group(3)), mes, int(m.group(1)))
                if d <= dt.date.fromisoformat(data_edicao):
                    return d.isoformat()
            except ValueError:
                pass
    # epígrafe com data por extenso nas primeiras linhas
    from datas import data_do_texto
    achada = data_do_texto("# x\n\n" + bloco, numero, linhas=10)
    if achada and achada <= data_edicao:
        return achada
    return ""


def titulo_do_bloco(bloco, numero, data):
    primeira = next((ln.strip() for ln in bloco.splitlines() if ln.strip()), "")
    primeira = re.sub(r"\s+", " ", primeira)
    if data:
        partes = data.split("-")
        meses = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()
        extenso = "%d de %s de %s" % (int(partes[2]), meses[int(partes[1]) - 1], partes[0])
        return "Emenda à Lei Orgânica nº %s, de %s" % (numero, extenso)
    if EPIGRAFE.search(primeira) and len(primeira) <= 160:
        return primeira
    return "Emenda à Lei Orgânica nº %s" % numero


def corpo_markdown(bloco):
    md = texto_pdf_para_md(bloco)
    return md.strip() + "\n"


def gravar_emenda(destino, meta, corpo):
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    ordem = [
        "titulo", "tipo", "tipo_na_fonte", "numero", "data", "ano", "municipio", "uf",
        "codigo_ibge", "revogada", "versao_texto", "extrator", "sha256_classificador",
        "sha256_extrator_geometria", "sha256_pdf", "sha256_texto", "publicacao",
        "data_publicacao", "codigo_identificador", "fonte", "baixado_em",
    ]
    linhas = ["---"]
    for k in ordem:
        if k not in meta:
            continue
        v = meta[k]
        if k == "revogada" and v is None:
            linhas.append("revogada: null")
        elif k in ("data", "data_publicacao", "baixado_em") and re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(v or "")):
            linhas.append("%s: %s" % (k, v))
        else:
            linhas.append("%s: %s" % (k, yaml_str(v)))
    linhas += ["---", "", "# " + meta["titulo"], "", corpo]
    if not corpo.endswith("\n"):
        linhas.append("")
    texto = "\n".join(linhas)
    if not texto.endswith("\n"):
        texto += "\n"
    tmp = destino.with_suffix(".md.tmp")
    tmp.write_text(texto)
    tmp.replace(destino)
    return texto


def processar_edicao(item, pdf_path, bruto, pasta_md, classificador_sha, hoje, vistos=None):
    texto = extrair_texto(pdf_path)
    if pdf_escaneado(texto) and len(re.sub(r"\W", "", texto)) < 80:
        return [], {"status": "sem_texto", "motivo": "PDF sem texto legível", "edicao": item["id"]}
    emendas = escolher_blocos(pdf_path)
    if vistos is not None:
        emendas = [(num, bloco) for num, bloco in emendas if num not in vistos]
    contaminados = [num for num, bloco in emendas if NEWS.search(bloco)]
    emendas = [(num, bloco) for num, bloco in emendas if not NEWS.search(bloco)]
    if not emendas:
        if contaminados:
            return [], {"status": "texto_misturado",
                        "motivo": "corpo misturado com notícia do jornal; PDF conservado para reprocessar",
                        "edicao": item["id"], "numeros": contaminados}
        return [], None
    sha_pdf = hashlib.sha256(bruto).hexdigest()
    data_edicao = item["data_publicacao"]
    gravadas = []
    for numero, bloco in emendas:
        data = data_do_bloco(bloco, numero, data_edicao)
        ano = (data or data_edicao)[:4]
        titulo = titulo_do_bloco(bloco, numero, data)
        corpo = corpo_markdown(bloco)
        if len(re.sub(r"\W", "", corpo)) < 80:
            continue
        codigo = "DOL-%s-ELO-%s" % (item.get("numero") or item["id"], numero)
        slug = slugify("emenda-a-lei-organica-%s-%s-%s" % (numero, ano, codigo.lower()))[:110]
        destino = Path(pasta_md) / ano / (slug + ".md")
        meta = {
            "titulo": titulo,
            "tipo": CANONICO["emenda a lei organica"][1],
            "tipo_na_fonte": "Emenda à Lei Orgânica",
            "numero": numero,
            "data": data,
            "ano": ano,
            "municipio": MUNICIPIO,
            "uf": UF,
            "codigo_ibge": IBGE_SALVADOR,
            "revogada": None,
            "versao_texto": "publicação original no Diário Oficial do Legislativo (CMS/Dioly)",
            "extrator": EXTRATOR,
            "sha256_classificador": classificador_sha,
            "sha256_extrator_geometria": SHA_GEOMETRIA,
            "sha256_pdf": sha_pdf,
            "sha256_texto": hashlib.sha256(corpo.encode()).hexdigest(),
            "publicacao": "DOL nº %s de %s" % (item.get("numero") or item["id"],
                                               dt.date.fromisoformat(data_edicao).strftime("%d/%m/%Y")),
            "data_publicacao": data_edicao,
            "codigo_identificador": codigo,
            "fonte": item["pdf_url"],
            "baixado_em": hoje,
        }
        if destino.exists():
            anterior = destino.read_text()
            mesma = ('codigo_identificador: %s' % yaml_str(codigo)) in anterior
            if mesma and ('sha256_classificador: %s' % yaml_str(classificador_sha)) in anterior:
                gravadas.append(str(destino))
                if vistos is not None:
                    vistos.add(numero)
                continue
            if not mesma:
                raise RuntimeError("documento existente exige reconciliação: " + str(destino))
            destino.unlink()
        gravar_emenda(destino, meta, corpo)
        gravadas.append(str(destino))
        if vistos is not None:
            vistos.add(numero)
    return gravadas, None


def numero_lc(m):
    return str(int(m.group("num"))), m.group("ano")


def eh_epigrafe_ato_lc(texto, ini, m):
    """Epígrafe de ato em caixa alta; citações em minúsculas ou no meio da frase saem."""
    linha = texto[ini:texto.find("\n", ini) if texto.find("\n", ini) >= 0 else len(texto)]
    if not re.match(r"LEI\s+COMPLEMENTAR\s+N", linha):
        return False
    if PROJETO_LC.search(texto[max(0, ini - 40):ini + 80]):
        return False
    depois = texto[m.end():m.end() + 48].lstrip()
    if depois.startswith(",") or depois.startswith(".") or (depois[:1].islower()):
        return False
    return True


def eh_lc_promulgada(bloco):
    cabeca = "\n".join(bloco.splitlines()[:10])
    if PROJETO_LC.search(cabeca) and not SANCIONO_LC.search(bloco):
        return False
    if not EPIGRAFE_LC.search(bloco):
        return False
    if not ARTIGO.search(bloco):
        return False
    if not (SANCIONO_LC.search(bloco) or GABINETE_LC.search(bloco)):
        return False
    if not GABINETE_LC.search(bloco):
        return False
    return True


def recortar_lc(bloco):
    """Mantém anexos da lei; corta o ato seguinte (decreto, portaria, outra lei)."""
    m = GABINETE_LC.search(bloco)
    if not m:
        return bloco.strip()
    resto = bloco[m.end():]
    corte = COLOFON_LC.search(resto)
    if corte and not re.search(r"Art\.|ANEXO|QUADRO", resto[corte.end():], re.I):
        bloco = bloco[:m.end() + corte.start()]
        resto = bloco[m.end():]
    linhas = [bloco[:m.end()].rstrip()]
    n = 0
    for ln in resto.splitlines():
        s = ln.strip()
        if not s:
            linhas.append("")
            continue
        if INICIO_LC.match(s) and not EPIGRAFE_LC.match(s):
            break
        if COLOFON_LC.search(s):
            break
        n += 1
        if n > 40 and not CARGO_LC.search(s) and not re.search(r"ANEXO|QUADRO", s, re.I):
            if len(s) > 80 and not CARGO_LC.search(s):
                # tabelas de anexo continuam; só para se parecer outro expediente
                if re.match(r"^(?:O PREFEITO|Faço saber)", s, re.I):
                    break
        linhas.append(s)
    return "\n".join(linhas).strip()


def limpar_bloco_lc(bloco):
    linhas = []
    for ln in bloco.splitlines():
        s = ln.strip()
        if not s:
            if linhas and linhas[-1] != "":
                linhas.append("")
            continue
        if LETRA_VERTICAL_LC.match(s):
            continue
        if CHROME_LC.match(s) or CABECALHO_PAGINA.match(s) or CHROME.match(s):
            continue
        if re.fullmatch(r"\d{1,3}", s):
            continue
        linhas.append(s)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()


def blocos_lc(texto):
    """Recorta cada LC sancionada a partir da epígrafe em caixa alta até o próximo ato."""
    saida = []
    for m in EPIGRAFE_LC.finditer(texto):
        ini = texto.rfind("\n", 0, m.start()) + 1
        if not eh_epigrafe_ato_lc(texto, ini, m):
            continue
        num, ano = numero_lc(m)
        fim = len(texto)
        for n in INICIO_LC.finditer(texto, m.end()):
            if n.start() < m.end() + 10:
                continue
            trecho = texto[n.start():n.start() + 90]
            em = EPIGRAFE_LC.search(trecho)
            if em and numero_lc(em) == (num, ano):
                continue
            fim = n.start()
            break
        bloco = limpar_bloco_lc(recortar_lc(texto[ini:fim]))
        if eh_lc_promulgada(bloco):
            saida.append((num, ano, bloco))
    por = {}
    for num, ano, bloco in saida:
        chave = (num, ano)
        if chave not in por or len(bloco) > len(por[chave][2]):
            por[chave] = (num, ano, bloco)
    return [por[k] for k in sorted(por, key=lambda x: (x[1], int(x[0])))]


def nota_lc(bloco):
    return (1 if REPUBLICADA.search(bloco) else 0, len(bloco))


def data_do_gabinete(bloco, data_edicao, folga=3):
    achadas = []
    for m in GABINETE_LC.finditer(bloco):
        mes = MESES.get(m.group("mes").lower())
        if not mes:
            continue
        try:
            d = dt.date(int(m.group("ano")), mes, int(m.group("dia")))
        except ValueError:
            continue
        if data_edicao:
            try:
                limite = dt.date.fromisoformat(data_edicao)
            except ValueError:
                limite = d
            if d > limite + dt.timedelta(days=folga):
                continue
        achadas.append(d)
    return achadas[0].isoformat() if achadas else ""


def titulo_lc(numero, data):
    if data:
        partes = data.split("-")
        meses = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()
        extenso = "%d de %s de %s" % (int(partes[2]), meses[int(partes[1]) - 1], partes[0])
        return "Lei Complementar nº %s, de %s" % (numero, extenso)
    return "Lei Complementar nº %s" % numero


def extrair_lc(pdf):
    for fn in (texto_raw, texto_layout):
        try:
            texto = juntar_hifen(fn(pdf))
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError):
            continue
        achados = blocos_lc(texto)
        if achados:
            return achados
    return []


def processar_edicao_lc(item, pdf_path, bruto):
    try:
        amostra = texto_raw(pdf_path)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError):
        amostra = ""
    if pdf_escaneado(amostra) and len(re.sub(r"\W", "", amostra)) < 80:
        return [], {"status": "sem_texto", "motivo": "PDF sem texto legível", "edicao": item["id"]}
    achados = extrair_lc(pdf_path)
    if not achados:
        return [], None
    return achados, None


def gravar_lc(destino, meta, corpo):
    return gravar_emenda(destino, meta, corpo)


# --- leis ordinárias (DOM) ---------------------------------------------------------------
EPIGRAFE_LO = re.compile(
    r"^LEI\s+N\s*[ºo°]?\s*\.?\s*(?P<num>\d{1,2}\.?\d{3})\s*"
    r"(?:/\s*(?P<ano>\d{4})|,?\s+DE\s+\d{1,2}\s+DE\s+[A-ZÇ]+\s+DE\s+(?P<ano2>\d{4}))[ \t]*$",
    re.M,
)
PROJETO_LO = re.compile(r"projeto\s+de\s+lei", re.I)
SANCIONO_LO = re.compile(r"sanciono a(?:\s+seguinte)?\s+Lei\s*:|decreta e eu sanciono a seguinte Lei", re.I)
ATO_MAIUSCULO = re.compile(r"^[A-ZÇÃÕÉÍÓÚÂÊ]{3,}")
GLIFO_QUEBRADO = re.compile(r"[\u0180-\u03ff\ufffd\x01-\x08\x0e-\x1f]")
ILEGIVEL = "[trecho ilegível no PDF: fonte sem mapa Unicode]"


def marcar_ilegivel(bloco):
    """Troca linhas com glifos sem ToUnicode (ex. `ŶĞǆŽ`) por um marcador; não reconstrói texto."""
    linhas = []
    for ln in bloco.splitlines():
        s = ln.strip()
        ruins = len(GLIFO_QUEBRADO.findall(s))
        if ruins and (ruins == len(s) or (ruins >= 2 and ruins >= 0.1 * len(s))):
            if linhas and linhas[-1] == ILEGIVEL:
                continue
            linhas.append(ILEGIVEL)
            continue
        linhas.append(ln)
    return "\n".join(linhas)


def numero_lo(m):
    return str(int(m.group("num").replace(".", ""))), m.group("ano") or m.group("ano2")


def eh_epigrafe_ato_lo(texto, ini, m):
    """Linha inteira `LEI Nº N/AAAA` em caixa alta; nunca COMPLEMENTAR, nunca projeto."""
    linha = m.group(0)
    if "COMPLEMENTAR" in linha.upper():
        return False
    if PROJETO_LO.search(texto[max(0, ini - 40):ini]):
        return False
    return True


def eh_lo_promulgada(bloco):
    cabeca = "\n".join(bloco.splitlines()[:3])
    if re.search(r"COMPLEMENTAR", cabeca, re.I) and EPIGRAFE_LC.search(cabeca):
        return False
    if PROJETO_LO.search(cabeca):
        return False
    if not EPIGRAFE_LO.search(bloco):
        return False
    if not ARTIGO.search(bloco):
        return False
    gab = GABINETE_LC.search(bloco)
    if not gab:
        return False
    # Algumas leis saem no DOM sem a fórmula de sanção (DOM 9007, 9181, 9185); vale então
    # o fecho do gabinete assinado pelo Prefeito logo abaixo.
    if not SANCIONO_LO.search(bloco) and not re.search(
            r"^\s*Prefeito\s*$", bloco[gab.end():gab.end() + 160], re.I | re.M):
        return False
    return True


def blocos_lo(texto):
    """Recorta cada lei ordinária sancionada da epígrafe em caixa alta até o próximo ato."""
    saida = []
    for m in EPIGRAFE_LO.finditer(texto):
        ini = m.start()
        if not eh_epigrafe_ato_lo(texto, ini, m):
            continue
        num, ano = numero_lo(m)
        fim = len(texto)
        for n in INICIO_LC.finditer(texto, m.end()):
            if n.start() < m.end() + 10 or not ATO_MAIUSCULO.match(texto[n.start():n.start() + 8]):
                continue
            em = EPIGRAFE_LO.match(texto, n.start())
            if em and numero_lo(em) == (num, ano):
                continue
            fim = n.start()
            break
        bloco = marcar_ilegivel(limpar_bloco_lc(recortar_lc(texto[ini:fim])))
        if eh_lo_promulgada(bloco):
            saida.append((num, ano, bloco))
    por = {}
    for num, ano, bloco in saida:
        chave = (num, ano)
        if chave not in por or len(bloco) > len(por[chave][2]):
            por[chave] = (num, ano, bloco)
    return [por[k] for k in sorted(por, key=lambda x: (x[1], int(x[0])))]


def lo_contemporanea(bloco, ano, data_edicao, folga_dias=366):
    """Gabinete datado no ano da lei e até `folga_dias` antes da edição (barra lei antiga em edital).

    Edições de feriado cobrem vários dias ("02 Á 06 DE ABRIL"); a API dá só o primeiro, então o
    gabinete pode cair até 10 dias depois de `data_publicacao`.
    """
    data = data_do_gabinete(bloco, data_edicao, folga=10)
    if not data or data[:4] != ano:
        return ""
    if data_edicao:
        try:
            if dt.date.fromisoformat(data) < dt.date.fromisoformat(data_edicao) - dt.timedelta(days=folga_dias):
                return ""
        except ValueError:
            return ""
    return data


def titulo_lo(numero, data):
    return titulo_lc(numero, data).replace("Lei Complementar", "Lei", 1)


def extrair_lo(pdf):
    for fn in (texto_raw, texto_layout):
        try:
            texto = juntar_hifen(fn(pdf))
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError):
            continue
        achados = blocos_lo(texto)
        if achados:
            return achados
    return []


# --- decretos do Executivo (DOM) --------------------------------------------------------
CONSULTAS_DEC = (
    "DECRETO Nº",
    "DECRETO N°",
    "DECRETOS NUMERADOS",
    "DECRETOS FINANCEIROS",
)
# Epígrafe = linha inteira em caixa alta: "DECRETO Nº 41.680 de 30 de abril de 2026",
# "DECRETO Nº 38.212/2024", "DECRETO Nº 37.001/2023, DE 05/01/2023". Nunca LEGISLATIVO,
# MUNICIPAL (citação em parecer) nem "DECRETOS de …" (decretos simples, não numerados).
EPIGRAFE_DEC = re.compile(
    r"^[ \t]*DECRETO[ \t]+N[ \t]*[ºo°]?[ \t]*\.?[ \t]*(?P<num>\d{1,2}\.\d{3}|\d{1,5})[ \t]*"
    r"(?:/[ \t]*(?P<ano>\d{4})(?:[ \t]*,?[ \t]*(?:DE|de)[ \t]+\d{1,2}/\d{1,2}/\d{4})?"
    r"|,?[ \t]+(?:DE|de)[ \t]+\d{1,2}[º°]?[ \t]+(?:DE|de)[ \t]+[A-Za-zÇç]+[ \t]+(?:DE|de)[ \t]+(?P<ano2>\d{4}))"
    r"[ \t.]*$", re.M)
DECRETA = re.compile(r"\bDECRETA\s*:", re.I)
PREFEITO_DEC = re.compile(r"O\s+PREFEITO\s+(?:MUNICIPAL\s+)?D[OA]\s+MUNIC[IÍ]PIO|PREFEIT[OA]\s+(?:MUNICIPAL\s+)?"
                          r"(?:EM\s+EXERC[IÍ]CIO\s+)?D[OA]\s+(?:(?:MUNIC[IÍ]PIO|CIDADE)\s+D[OE]\s+)?SALVADOR", re.I)
# Cabeçalho de página do DOM que pdftotext intercala no meio do ato ("SÁBADO A SEGUNDA-FEIRA",
# "24 A 26 DE JANEIRO DE 2026", "DIÁRIO OFICIAL DO SALVADOR-BAHIA").
_DIA_DOM = r"(?:SEGUNDA|TER[ÇC]A|QUARTA|QUINTA|SEXTA|S[ÁA]BADO|DOMINGO)(?:-FEIRA)?"
_MES_DOM = r"(?:JANEIRO|FEVEREIRO|MAR[ÇC]O|ABRIL|MAIO|JUNHO|JULHO|AGOSTO|SETEMBRO|OUTUBRO|NOVEMBRO|DEZEMBRO)"
CHROME_DOM = re.compile(
    r"^(?:" + _DIA_DOM + r"(?:\s*(?:,|A|E|À)\s*" + _DIA_DOM + r")*"
    r"|\d{1,2}(?:\s*(?:,|A|E|À)\s*\d{1,2})*\s+(?:DE\s+)?" + _MES_DOM + r"(?:\s*(?:A|E|À)\s*\d{1,2}\s+DE\s+"
    + _MES_DOM + r")?\s+DE\s+20\d{2}"
    r"|DI[ÁA]RIO\s+OFICIAL\s+DO\s+SALVADOR[-–— ]+BAHIA"
    r"|ANO\s+[IVXLC]+\s*\|?\s*N\s*[ºo°.]?\s*[\d.]+(?:\s+\d{1,3})?)\s*$")
# Linha que encerra o recorte de um decreto (próximo ato ou seção do DOM).
FIM_DEC = re.compile(
    r"^(?:DECRETOS?\b|LEI\s+(?:COMPLEMENTAR\s+)?N|PORTARIAS?\b|RESOLU[ÇC][ÃA]O\b|INSTRU[ÇC][ÃA]O\s+NORMATIVA"
    r"|EXTRATOS?\b|AVISOS?\b|EDITA(?:L|IS)\b|ERRATA\b|RETIFICA[ÇC][ÃA]O\b|COMUNICADO\b|ATOS?\s+D[OA]\b"
    r"|ATA\b|PROJETO\s+DE\b|AVISO\b|SECRETARIA\s+MUNICIPAL\b|CASA\s+CIVIL$|GABINETE\s+DO\s+PREFEITO$"
    r"|EXECUTIVO$|LEGISLATIVO$|SUM[ÁA]RIO$)")
# "GABINETEDO PREFEITO" (DOM 9301, 9315) sai colado no PDF.
GABINETE_DEC = re.compile(
    r"GABINETE\s*DO\s+PREFEITO.{0,80}?,\s*(?:em|de)?\s*"
    r"(?P<dia>\d{1,2})[º°]?\s*(?:de\s*)?(?P<mes>[A-Za-zçÇ]+?)\s*(?:de\s*)?(?P<ano>\d{4})",
    re.I,
)
# Cabeçalho de órgão: dentro de anexo só encerra se um ato começa logo abaixo.
ORGAO_DEC = re.compile(r"^(?:SECRETARIA\s+MUNICIPAL\b|CASA\s+CIVIL$|GABINETE\s+DO\s+PREFEITO$)")
ATO_DEC = re.compile(
    r"^(?:DECRETOS?\b|LEI\s+(?:COMPLEMENTAR\s+)?N|PORTARIAS?\b|RESOLU[ÇC][ÃA]O\b|INSTRU[ÇC][ÃA]O\s+NORMATIVA"
    r"|EXTRATOS?\b|AVISOS?\b|EDITA(?:L|IS)\b|ERRATA\b|RETIFICA[ÇC][ÃA]O\b|COMUNICADO\b|ATOS?\b|ATA\b)")
ASSINA_DEC = re.compile(
    r"^(?:Prefeit[oa]|Vice-Prefeit|Secret[áa]ri[oa]|Chefe|Procurador|Controlador|Diretor|Presidente"
    r"|Ouvidor|Subsecret|em\s+exerc[ií]cio)", re.I)


def limpar_dom(bloco):
    return "\n".join(ln for ln in bloco.splitlines() if not CHROME_DOM.match(ln.strip()))


def numero_dec(m):
    return str(int(m.group("num").replace(".", ""))), m.group("ano") or m.group("ano2")


def _linha_nome(s):
    return (len(s) <= 80 and not re.search(r"\d", s) and s.upper() == s
            and re.search(r"[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{3,}", s) and not FIM_DEC.match(s) and not CHROME_LC.match(s))


def recortar_dec(bloco):
    """Decreto até o gabinete + assinaturas; anexo próprio (`ANEXO …`) entra até o próximo ato."""
    m = GABINETE_DEC.search(bloco)
    if not m:
        return bloco.strip()
    fim_linha = bloco.find("\n", m.end())
    fim_linha = len(bloco) if fim_linha < 0 else fim_linha
    linhas = [bloco[:fim_linha].rstrip()]
    anexo = False
    resto = [ln.strip() for ln in bloco[fim_linha:].splitlines() if ln.strip()]
    for i, s in enumerate(resto):
        if (CHROME_LC.match(s) or CHROME_DOM.match(s) or CABECALHO_PAGINA.match(s)
                or LETRA_VERTICAL_LC.match(s) or re.fullmatch(r"\d{1,3}", s)):
            linhas.append(s)
            continue
        if anexo:
            if EPIGRAFE_DEC.match(s) or COLOFON_LC.search(s):
                break
            if ORGAO_DEC.match(s):
                if any(ATO_DEC.match(x) for x in resto[i + 1:i + 5]):
                    break
            elif FIM_DEC.match(s):
                break
            linhas.append(s)
            continue
        if re.match(r"^ANEXO\b", s, re.I):
            anexo = True
            linhas.append(s)
            continue
        if ASSINA_DEC.match(s) or _linha_nome(s):
            linhas.append(s)
            continue
        break
    return "\n".join(linhas).strip()


def eh_dec_sancionado(bloco):
    linhas = [ln for ln in bloco.splitlines() if ln.strip()]
    if not linhas or not EPIGRAFE_DEC.match(linhas[0]):
        return False
    art = ARTIGO.search(bloco)
    if not art:
        return False
    antes = bloco[:art.start()]
    if not DECRETA.search(antes) or not PREFEITO_DEC.search(antes):
        return False
    gab = GABINETE_DEC.search(bloco)
    if not gab or gab.start() < art.start():
        return False
    return bool(re.search(r"^\s*Prefeit[oa](?:\s+em\s+exerc[ií]cio)?\s*$",
                          bloco[gab.end():gab.end() + 400], re.I | re.M))


def blocos_dec(texto):
    """Recorta cada decreto numerado do Prefeito (epígrafe em linha própria) até o próximo ato."""
    saida, descartes = [], []
    for m in EPIGRAFE_DEC.finditer(texto):
        ini = m.start()
        num, ano = numero_dec(m)
        if PROJETO_LO.search(texto[max(0, ini - 40):ini]):
            continue
        fim = len(texto)
        for n in EPIGRAFE_DEC.finditer(texto, m.end()):
            fim = n.start()
            break
        bloco = marcar_ilegivel(limpar_bloco_lc(limpar_dom(recortar_dec(texto[ini:fim]))))
        if eh_dec_sancionado(bloco):
            saida.append((num, ano, bloco))
        elif ARTIGO.search(bloco):
            descartes.append((num, ano, "sem DECRETA + Art. 1º + gabinete/Prefeito no recorte"))
    por = {}
    for num, ano, bloco in saida:
        chave = (num, ano)
        if chave not in por or len(bloco) > len(por[chave][2]):
            por[chave] = (num, ano, bloco)
    return [por[k] for k in sorted(por, key=lambda x: (x[1], int(x[0])))], descartes


def data_dec(bloco, ano, data_edicao, folga_dias=366):
    """Data do gabinete no ano da epígrafe, até 10 dias depois e 1 ano antes da edição."""
    for m in GABINETE_DEC.finditer(bloco):
        mes = MESES.get(m.group("mes").lower())
        if not mes:
            continue
        try:
            d = dt.date(int(m.group("ano")), mes, int(m.group("dia")))
        except ValueError:
            continue
        if str(d.year) != ano:
            continue
        if data_edicao:
            e = dt.date.fromisoformat(data_edicao)
            if d > e + dt.timedelta(days=10) or d < e - dt.timedelta(days=folga_dias):
                continue
        return d.isoformat()
    return ""


def titulo_dec(numero, data):
    return titulo_lc(numero, data).replace("Lei Complementar", "Decreto", 1)


def extrair_dec(pdf):
    descartes = []
    for fn in (texto_raw, texto_layout):
        try:
            texto = juntar_hifen(fn(pdf))
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError):
            continue
        achados, desc = blocos_dec(texto)
        if achados:
            return achados, desc
        descartes = descartes or desc
    return [], descartes


# --- resoluções e decretos legislativos (DOL) ---------------------------------------------
CONSULTAS_RES = (
    "RESOLUÇÃO Nº",
    "promulga a seguinte Resolução",
)
CONSULTAS_DL = (
    "DECRETO LEGISLATIVO",
    "DECRETO LEGISLATIVO Nº",
)
_NUM_ATO = r"N\s*\.?\s*[ºo°]?\s*\.?\s*(?P<num>\d{1,2}\.\d{3}|\d{1,4})"
_NUM_ATO_MIN = r"[Nn]\s*\.?\s*[ºo°]?\s*\.?\s*(?P<num>\d{1,2}\.\d{3}|\d{1,4})"
_ANO_ATO = (r"\s*(?:/\s*(?P<ano>\d{4}|\d{2})"
            r"|,?\s+(?:DE|de)\s+\d{1,2}[º°]?\s+(?:DE|de)\s+[A-Za-zÇç]+\s+(?:DE|de)\s+(?P<ano2>\d{4}))"
            r"[ \t.]*$")
# Epígrafe = linha inteira. CMS usa caixa alta (2017+) e "Resolução nº 1.971/2010" em 2010–2016;
# citações no meio da frase nunca ocupam a linha sozinhas.
EPIGRAFE_RES = re.compile(
    r"^[ \t]*(?:RESOLU[ÇC][ÃA]O[ \t]+" + _NUM_ATO + "|Resolu[çc][ãa]o[ \t]+"
    + _NUM_ATO_MIN.replace("num", "numm") + ")" + _ANO_ATO, re.M)
EPIGRAFE_DL = re.compile(
    r"^[ \t]*(?:DECRETO[ \t]+LEGISLATIVO[ \t]+" + _NUM_ATO + "|Decreto[ \t]+Legislativo[ \t]+"
    + _NUM_ATO_MIN.replace("num", "numm") + ")" + _ANO_ATO, re.M)
PROXIMO_ATO_MESA = re.compile(
    r"^[ \t]*(?:RESOLU[ÇC][ÃA]O\s+N|Resolu[çc][ãa]o\s+[Nn]\s*\.?\s*[ºo°]\s*\.?\s*[\d.]+\s*/"
    r"|DECRETO\s+LEGISLATIVO\s+N|Decreto\s+Legislativo\s+[Nn]\s*\.?\s*[ºo°]\s*\.?\s*[\d.]+\s*/"
    r"|LEI\s+(?:COMPLEMENTAR\s+)?N|EMENDA\s+(?:N|[ÀA]\s+LEI)|PROJETO\s+DE\b"
    r"|ATOS?\s+D[OA]\s+(?:PRESIDENTE|MESA)|ATO\s+(?:DA\s+MESA\s+)?N|PORTARIA\b|INDICA[ÇC][ÃA]O\b"
    r"|MO[ÇC][ÃA]O\b|EDITAL\b|AVISO\b|EXTRATO\b|ERRATA\b|RETIFICA[ÇC][ÃA]O\b|REQUERIMENTO\b"
    r"|PARECER\b|ATAS?\b|EXPEDIENTE\b)", re.M)
_MES_CAP = r"(?:Janeiro|Fevereiro|Mar[çc]o|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)"
# cabeçalho de página do DOL: "8 de Outubro de 2026", "Quinta e Sexta-feira, 8 e 9 de Dezembro de 2022",
# "CÂMARA MUNICIPAL"; o corpo do ato escreve o mês em minúsculas.
CHROME_MESA = re.compile(
    r"^(?:(?:(?:Segunda|Ter[çc]a|Quarta|Quinta|Sexta|S[áa]bado|Domingo)(?:-feira)?[, e]*)+"
    r"(?:\s*[\d, ea]+\s+de\s+" + _MES_CAP + r"\s+de\s+\d{4})?"
    r"|\d{1,2}(?:\s*(?:,|e|a|à)\s*\d{1,2})*\s+de\s+" + _MES_CAP + r"\s+de\s+\d{4}"
    r"|C[ÂA]MARA\s+MUNICIPAL|Ano\s+[IVXLC]+|N\s*[°º]\s*[\d.]+|ATOS\s+DO\s+PODER\s+LEGISLATIVO)\s*$")
ULTIMO_ARTIGO_SALA = 1500
# 2013–2015 a CMS publica "A CÂMARA MUNICIPAL DE SALVADOR / RESOLVE:" (ou DECRETA:) no lugar
# de "promulga e manda publicar" (DOL 4237).
PROMULGA_MESA = re.compile(
    r"promulg\w*|faz\s+saber|fa[çc]o\s+saber"
    r"|A\s+C[ÂA]MARA\s+MUNICIPAL\s+D[OE]\s+SALVADOR\s*,?\s*(?:RESOLVE|DECRETA)\s*:", re.I)
SALA_ATO = re.compile(r"Sala\s+das\s+Sess[oõ]es,?\s+(?:em\s+)?[oO]?\s*" + POR_EXTENSO.pattern, re.I)
PROJETO_MESA = re.compile(r"projeto\s+de\s*$", re.I)
PARA_ASSINATURA = re.compile(
    r"^(?:ATOS?\b|ATO\s|O\s+PRESIDENTE|A\s+PRESIDENTE|A\s+MESA|C[ÂA]MARA\b|PORTARIA|RESOLU|DECRETO"
    r"|LEI\b|EMENDA|PROJETO|INDICA|MO[ÇC]|EDITAL|AVISO|EXTRATO|ERRATA|RETIFICA|SECRETARIA"
    r"|DIRETORIA|SUPERINTEND|TERMO|CONTRATO|PREG[ÃA]O|LICITA|HOMOLOGA|PAUTA|ORDEM\s+DO|Fotos?:)", re.I)
SERIES_MESA = {
    "resolucoes": {
        "chave": "resolucao", "sigla": "RES", "tipo_na_fonte": "Resolução", "rotulo": "Resolução",
        "epigrafe": EPIGRAFE_RES, "consultas": CONSULTAS_RES,
    },
    "decretos-legislativos": {
        "chave": "decreto legislativo", "sigla": "DL", "tipo_na_fonte": "Decreto Legislativo",
        "rotulo": "Decreto Legislativo", "epigrafe": EPIGRAFE_DL, "consultas": CONSULTAS_DL,
    },
}


def edicao_dol(item):
    """Número da edição DOL pela API: o nome do PDF no DOL é `DOL-AAAA-MM-DD-NNNN` (com erros
    de digitação como `66951`), então não serve para o número."""
    return item.get("numero") or item["id"]


def numero_mesa(m):
    num = m.group("num") or m.group("numm")
    ano = m.group("ano") or m.group("ano2")
    if len(ano) == 2:
        ano = "20" + ano
    return str(int(num.replace(".", ""))), ano


def _linha_assinatura(s):
    """Nome de vereador ou cargo da Mesa; para no próximo expediente, legenda ou frase."""
    if CARGO.search(s):
        return True
    if len(s) > 70 or PARA_ASSINATURA.match(s) or FIM_JORNAL.match(s) or CHROME.match(s):
        return False
    if CABECALHO_PAGINA.match(s) or SESSAO.search(s) or re.search(r"\d|[:;]$|\.$", s):
        return False
    palavras = [p for p in re.split(r"\s+", s) if len(p) > 3]
    if not palavras:
        return False
    return sum(1 for p in palavras if p[:1].isupper()) / len(palavras) >= 0.7


def recortar_mesa(bloco):
    """Ato até Sala das Sessões + assinaturas da Mesa; nada do expediente seguinte."""
    m = SALA_ATO.search(bloco)
    if not m:
        return bloco.strip()
    fim_linha = bloco.find("\n", m.end())
    fim_linha = len(bloco) if fim_linha < 0 else fim_linha
    linhas, n = [bloco[:fim_linha].rstrip()], 0
    for ln in bloco[fim_linha:].splitlines():
        s = ln.strip()
        if not s or s == ".":
            continue
        if not _linha_assinatura(s):
            break
        n += 1
        if n > 8:
            break
        linhas.append(s)
    return "\n".join(linhas).strip()


def limpar_mesa(bloco):
    linhas = [ln for ln in bloco.splitlines() if not CHROME_MESA.match(ln.strip())]
    return limpar_bloco("\n".join(linhas))


def sala_longe_do_artigo(bloco):
    """Sala das Sessões muito depois do último artigo = recorte atravessou outro texto (ata, notícia)."""
    sala = SALA_ATO.search(bloco)
    arts = [m.start() for m in re.finditer(
        r"^(?:Art\b|§|Parágrafo único|[IVXLC]+\s*[-–—)]|[a-z]\))", bloco[:sala.start()], re.M)]
    return not arts or sala.start() - arts[-1] > ULTIMO_ARTIGO_SALA


def eh_ato_mesa(bloco, epigrafe):
    linhas = [ln for ln in bloco.splitlines() if ln.strip()]
    if not linhas or not epigrafe.match(linhas[0]):
        return False
    m = ARTIGO.search(bloco)
    if not m:
        return False
    if not PROMULGA_MESA.search(bloco[:m.start()]):
        return False
    if not SALA_ATO.search(bloco):
        return False
    return True


def blocos_mesa(texto, serie):
    """Recorta cada resolução/decreto legislativo promulgado da epígrafe até o próximo ato.

    Devolve (achados, descartes): achados = [(num, ano, bloco)]; descartes = [(num, ano, motivo)].
    """
    epigrafe = SERIES_MESA[serie]["epigrafe"]
    saida, descartes = [], []
    for m in epigrafe.finditer(texto):
        ini = m.start()
        num, ano = numero_mesa(m)
        if PROJETO_MESA.search(texto[max(0, ini - 40):ini].rstrip()):
            continue
        fim = len(texto)
        for n in PROXIMO_ATO_MESA.finditer(texto, m.end()):
            if n.start() < m.end() + 2:
                continue
            fim = n.start()
            break
        bloco = limpar_mesa(recortar_mesa(texto[ini:fim]))
        if NEWS.search(bloco):
            descartes.append((num, ano, "texto misturado com notícia do jornal"))
            continue
        if eh_ato_mesa(bloco, epigrafe):
            if sala_longe_do_artigo(bloco):
                descartes.append((num, ano, "Sala das Sessões longe do último artigo (recorte misturado)"))
                continue
            saida.append((num, ano, bloco))
        elif ARTIGO.search(bloco) or SALA_ATO.search(bloco):
            # epígrafe isolada com corpo, mas sem a forma promulgada completa
            descartes.append((num, ano, "sem Art. 1º + promulgação + Sala das Sessões no recorte"))
    por = {}
    for num, ano, bloco in saida:
        chave = (num, ano)
        if chave not in por or len(bloco) > len(por[chave][2]):
            por[chave] = (num, ano, bloco)
    return [por[k] for k in sorted(por, key=lambda x: (x[1], int(x[0])))], descartes


def data_sala(bloco, ano, data_edicao, folga_dias=366):
    """Data da Sala das Sessões no ano da epígrafe, até 10 dias depois e 1 ano antes da edição."""
    for m in SALA_ATO.finditer(bloco):
        mes = MESES.get(m.group(2).lower())
        if not mes:
            continue
        try:
            d = dt.date(int(m.group(3)), mes, int(m.group(1)))
        except ValueError:
            continue
        if str(d.year) != ano:
            continue
        if data_edicao:
            e = dt.date.fromisoformat(data_edicao)
            if d > e + dt.timedelta(days=10) or d < e - dt.timedelta(days=folga_dias):
                continue
        return d.isoformat()
    return ""


def titulo_mesa(rotulo, numero, data):
    return titulo_lc(numero, data).replace("Lei Complementar", rotulo, 1)


def extrair_mesa(pdf, serie):
    descartes = []
    for fn in (texto_raw, texto_layout):
        try:
            texto = juntar_hifen(fn(pdf))
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError):
            continue
        achados, desc = blocos_mesa(texto, serie)
        if achados:
            return achados, desc
        descartes = descartes or desc
    return [], descartes


def persistir_mesa(pasta_md, serie, item, num, ano_ep, bloco, data, sha_pdf, classificador_sha, hoje):
    cfg = SERIES_MESA[serie]
    data_edicao = item.get("data_publicacao") or ""
    ano = (data or ano_ep)[:4]
    corpo = corpo_markdown(bloco)
    if len(re.sub(r"\W", "", corpo)) < 80:
        return None
    edicao = edicao_dol(item)
    codigo = "%s-%s-%s-%s" % (item.get("tipo") or "DOL", edicao, cfg["sigla"], num)
    slug = slugify("%s-%s-%s-%s" % (serie, num, ano, codigo.lower()))[:110]
    destino = pasta_md / ano / (slug + ".md")
    meta = {
        "titulo": titulo_mesa(cfg["rotulo"], num, data),
        "tipo": CANONICO[cfg["chave"]][1],
        "tipo_na_fonte": cfg["tipo_na_fonte"],
        "numero": num,
        "data": data,
        "ano": ano,
        "municipio": MUNICIPIO,
        "uf": UF,
        "codigo_ibge": IBGE_SALVADOR,
        "revogada": None,
        "versao_texto": "publicação original no Diário Oficial do Legislativo (CMS/Dioly)"
        + ("; republicada por incorreção" if REPUBLICADA.search(bloco) else ""),
        "extrator": EXTRATOR,
        "sha256_classificador": classificador_sha,
        "sha256_extrator_geometria": SHA_GEOMETRIA,
        "sha256_pdf": sha_pdf,
        "sha256_texto": hashlib.sha256(corpo.encode()).hexdigest(),
        "publicacao": "%s nº %s de %s" % (
            item.get("tipo") or "DOL", edicao,
            dt.date.fromisoformat(data_edicao).strftime("%d/%m/%Y") if data_edicao else ""),
        "data_publicacao": data_edicao,
        "codigo_identificador": codigo,
        "fonte": item["pdf_url"],
        "baixado_em": hoje,
    }
    if destino.exists():
        destino.unlink()
    gravar_emenda(destino, meta, corpo)
    return destino


def chaves_existentes(pasta_md):
    """(numero, ano) → md já gravado na pasta da série (rodadas anteriores q=/completo).

    Uma rodada nova soma: chave já presente vinda de outra edição fica com o md antigo."""
    saida = {}
    for md in sorted(Path(pasta_md).glob("*/*.md")):
        cab = md.read_text(encoding="utf-8", errors="replace")[:3000]
        num = re.search(r'^numero:\s*"?([^"\n]+)"?\s*$', cab, re.M)
        ano = re.search(r'^ano:\s*"?(\d{4})"?\s*$', cab, re.M)
        cod = re.search(r'^codigo_identificador:\s*"?([^"\n]+)"?\s*$', cab, re.M)
        if num and ano:
            saida.setdefault((num.group(1).strip(), ano.group(1)), (md, cod.group(1) if cod else ""))
    return saida


def coletar_mesa(a, rede, edicoes, pasta_fonte, classificador_sha, hoje):
    serie = a.modo
    cfg = SERIES_MESA[serie]
    pasta_md = RAIZ / "municipais" / UF / "salvador" / CANONICO[cfg["chave"]][0]
    existentes = chaves_existentes(pasta_md)
    ja_existiam = collections.Counter()
    nome_lote = a.lote or "%s-salvador-%s-%s-%s" % (hoje.replace("-", ""), serie, a.de[:4], a.ate[:4])
    lote = RAIZ / "municipais/_lotes" / nome_lote
    lote.mkdir(parents=True, exist_ok=True)
    gravar_json(lote / "edicoes.json", edicoes)
    falhas_path = lote / "falhas.jsonl"
    falhas_path.write_text("")
    cont = collections.Counter()
    por_chave = {}
    descartes = []
    with falhas_path.open("a", encoding="utf-8") as falhas:
        for n, item in enumerate(edicoes, 1):
            pdf = caminho_pdf(pasta_fonte, item)
            try:
                bruto, _cache = baixar_pdf(rede, item, pdf)
                achados, desc, falha = [], [], None
                amostra = texto_raw(pdf)
                if pdf_escaneado(amostra) and len(re.sub(r"\W", "", amostra)) < 80:
                    falha = {"status": "sem_texto", "motivo": "PDF sem texto legível", "edicao": item["id"]}
                else:
                    achados, desc = extrair_mesa(pdf, serie)
            except Exception as e:
                falha = {"status": "erro", "edicao": item.get("id"), "data": item.get("data_publicacao"),
                         "fonte": item.get("pdf_url"), "erro": str(e)[:400]}
                achados, desc = [], []
            if falha:
                falhas.write(json.dumps(falha, ensure_ascii=False) + "\n")
                falhas.flush()
                cont[falha.get("status", "erro")] += 1
                continue
            data_edicao = item.get("data_publicacao") or ""
            for num, ano, motivo in desc:
                descartes.append({"numero": num, "ano": ano, "edicao": edicao_dol(item), "motivo": motivo})
            validos = []
            for num, ano, bloco in achados:
                data = data_sala(bloco, ano, data_edicao)
                if not data:
                    descartes.append({"numero": num, "ano": ano, "edicao": edicao_dol(item),
                                      "motivo": "Sala das Sessões fora do ano/da edição (reprodução ou citação)"})
                    continue
                validos.append((num, ano, bloco, data))
            if not validos:
                cont["sem_ato_promulgado"] += 1
            else:
                cont["ok"] += 1
                sha_pdf = hashlib.sha256(bruto).hexdigest()
                for num, ano, bloco, data in validos:
                    chave = (num, ano)
                    velho = existentes.get(chave)
                    codigo = "%s-%s-%s-%s" % (item.get("tipo") or "DOL", edicao_dol(item), cfg["sigla"], num)
                    if velho is not None and velho[1] != codigo:
                        ja_existiam[chave] += 1
                        continue
                    nota = nota_lc(bloco) + (data_edicao,)
                    atual = por_chave.get(chave)
                    if atual is not None and nota <= atual[0]:
                        continue
                    destino = persistir_mesa(pasta_md, serie, item, num, ano, bloco, data, sha_pdf,
                                             classificador_sha, hoje)
                    if destino is None:
                        continue
                    if atual is not None:
                        antigo = atual[1]
                        if antigo != destino and Path(antigo).exists():
                            Path(antigo).unlink()
                    por_chave[chave] = (nota, destino)
                    print("  %s %s/%s → %s" % (cfg["sigla"], num, ano, destino.relative_to(RAIZ)), flush=True)
            if n % 10 == 0 or n == len(edicoes):
                print("[%s/%s] %s chaves=%s" % (n, len(edicoes), dict(cont), len(por_chave)), flush=True)
    ordem = sorted(por_chave, key=lambda x: (x[1], int(x[0])))
    gravados = [str(por_chave[k][1]) for k in ordem]
    manifesto = {
        "municipio": MUNICIPIO, "uf": UF, "codigo_ibge": IBGE_SALVADOR,
        "fonte_api": API, "rps": a.rps, "consultas": [] if a.completo else list(cfg["consultas"]),
        "completo": bool(a.completo),
        "intervalo": [a.de, a.ate], "tipo": a.tipo, "extrator": EXTRATOR,
        "extrator_geometria": EXTRATOR_GEOMETRIA, "sha256_geometria": SHA_GEOMETRIA,
        "sha256_classificador": classificador_sha, "edicoes": len(edicoes),
        "so_cache": bool(a.so_cache), "rps_max": 2, "modo": serie,
        "contagens": dict(cont), "arquivos": [str(Path(p).relative_to(RAIZ)) for p in gravados],
        "numeros": ["%s/%s" % k for k in ordem],
        "ja_existiam": len(ja_existiam),
        "novos": ["%s/%s" % k for k in ordem if k not in existentes],
        "descartes": descartes,
        "observacao": (
            "Só atos promulgados pela Mesa da CMS (epígrafe em linha própria, Art. 1º, fórmula "
            "promulga/faz saber, Sala das Sessões datada no ano da epígrafe e até 1 ano antes da "
            "edição). Projetos, indicações, citações em ata/expediente e reproduções antigas não entram. "
            "Recorte termina nas assinaturas da Mesa."
        ),
        "baixado_em": hoje,
    }
    gravar_json(lote / "manifesto.json", manifesto)
    (lote / "lista.txt").write_text("\n".join(manifesto["arquivos"]) + ("\n" if gravados else ""))
    print("gravadas", len(gravados), "em", pasta_md, flush=True)
    return 0


def conferir_ibge(raiz):
    ibge = json.loads((Path(raiz) / "municipais/_indice/ibge-municipios.json").read_text())
    item = next(x for x in ibge if str(x["id"]) == IBGE_SALVADOR)
    uf = item["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]
    if item["nome"] != MUNICIPIO or uf != UF:
        raise RuntimeError("IBGE Salvador diverge")
    if slugify(normalizar_chave(item["nome"])) != "salvador":
        raise RuntimeError("slug Salvador diverge")
    return hashlib.sha256((Path(raiz) / "municipais/_indice/ibge-municipios.json").read_bytes()).hexdigest()


EDICAO_PDF = re.compile(r"(?:dom|dol)-(\d{3,5})[-_.]", re.I)


def numero_edicao(item):
    """Prefere o número gravado no nome do PDF; o campo `numero` da API às vezes diverge."""
    m = EDICAO_PDF.search(item.get("pdf_url") or "")
    if m:
        return int(m.group(1))
    return item.get("numero") or item["id"]


def persistir_lc(pasta_md, item, num, ano_ep, bloco, sha_pdf, classificador_sha, hoje):
    data_edicao = item.get("data_publicacao") or ""
    data = data_do_gabinete(bloco, data_edicao) or data_edicao
    ano = (data or ano_ep)[:4]
    corpo = corpo_markdown(bloco)
    if len(re.sub(r"\W", "", corpo)) < 80:
        return None
    edicao = numero_edicao(item)
    codigo = "%s-%s-LC-%s" % (item.get("tipo") or "DOM", edicao, num)
    slug = slugify("leis-complementares-%s-%s-%s" % (num, ano, codigo.lower()))[:110]
    destino = pasta_md / ano / (slug + ".md")
    meta = {
        "titulo": titulo_lc(num, data),
        "tipo": CANONICO["lei complementar"][1],
        "tipo_na_fonte": "Lei Complementar",
        "numero": num,
        "data": data,
        "ano": ano,
        "municipio": MUNICIPIO,
        "uf": UF,
        "codigo_ibge": IBGE_SALVADOR,
        "revogada": None,
        "versao_texto": "publicação original no Diário Oficial do Município (CMS/Dioly)"
        + ("; republicada por incorreção" if REPUBLICADA.search(bloco) else ""),
        "extrator": EXTRATOR,
        "sha256_classificador": classificador_sha,
        "sha256_extrator_geometria": SHA_GEOMETRIA,
        "sha256_pdf": sha_pdf,
        "sha256_texto": hashlib.sha256(corpo.encode()).hexdigest(),
        "publicacao": "%s nº %s de %s" % (
            item.get("tipo") or "DOM", edicao,
            dt.date.fromisoformat(data_edicao).strftime("%d/%m/%Y") if data_edicao else ""),
        "data_publicacao": data_edicao,
        "codigo_identificador": codigo,
        "fonte": item["pdf_url"],
        "baixado_em": hoje,
    }
    if destino.exists():
        destino.unlink()
    gravar_lc(destino, meta, corpo)
    return destino


def coletar_lc(a, rede, edicoes, pasta_fonte, classificador_sha, hoje):
    pasta_md = RAIZ / "municipais" / UF / "salvador" / "leis-complementares"
    lote = RAIZ / "municipais/_lotes/20261028-salvador-leis-complementares"
    lote.mkdir(parents=True, exist_ok=True)
    gravar_json(lote / "edicoes.json", edicoes)
    falhas_path = lote / "falhas.jsonl"
    falhas_path.write_text("")
    cont = collections.Counter()
    por_chave = {}
    with falhas_path.open("a", encoding="utf-8") as falhas:
        for n, item in enumerate(edicoes, 1):
            pdf = caminho_pdf(pasta_fonte, item)
            try:
                bruto, _cache = baixar_pdf(rede, item, pdf)
                achados, falha = processar_edicao_lc(item, pdf, bruto)
            except Exception as e:
                falha = {"status": "erro", "edicao": item.get("id"), "data": item.get("data_publicacao"),
                         "fonte": item.get("pdf_url"), "erro": str(e)[:400]}
                achados = []
            if falha:
                falhas.write(json.dumps(falha, ensure_ascii=False) + "\n")
                falhas.flush()
                cont[falha.get("status", "erro")] += 1
            elif achados:
                cont["ok"] += 1
                sha_pdf = hashlib.sha256(bruto).hexdigest()
                for num, ano, bloco in achados:
                    chave = (num, ano)
                    nota = nota_lc(bloco) + (item.get("data_publicacao") or "",)
                    atual = por_chave.get(chave)
                    if atual is not None and nota <= atual[0]:
                        continue
                    destino = persistir_lc(pasta_md, item, num, ano, bloco, sha_pdf,
                                           classificador_sha, hoje)
                    if destino is None:
                        continue
                    if atual is not None:
                        antigo = atual[4]
                        if antigo != destino and Path(antigo).exists():
                            Path(antigo).unlink()
                    por_chave[chave] = (nota, item, bloco, sha_pdf, destino)
                    print("  LC %s/%s → %s" % (num, ano, destino.relative_to(RAIZ)), flush=True)
            else:
                cont["sem_lc_promulgada"] += 1
            if n % 10 == 0 or n == len(edicoes):
                print("[%s/%s] %s chaves=%s" % (n, len(edicoes), dict(cont), len(por_chave)), flush=True)
    gravados = [str(por_chave[k][4]) for k in sorted(por_chave, key=lambda x: (x[1], int(x[0])))]
    resto = {
        "janela_entregue": [a.de, a.ate],
        "janela_restante": ["2011-01-01", "2015-12-31"] if a.de >= "2016-01-01" else [],
        "observacao": (
            "Citações a LC no DOM (portaria, contrato, LRF, LC 140/2011 federal) não entram. "
            "Projetos de lei complementar ficam de fora. "
            "A janela 2011–2015 (~50 edições q=LEIS COMPLEMENTARES) fica para leva seguinte; "
            "lá já foram vistas LC 053, 054, 056–058, 060–062."
        ),
    }
    manifesto = {
        "municipio": MUNICIPIO, "uf": UF, "codigo_ibge": IBGE_SALVADOR,
        "fonte_api": API, "rps": a.rps, "consultas": list(CONSULTAS_LC),
        "intervalo": [a.de, a.ate], "tipo": a.tipo, "extrator": EXTRATOR,
        "extrator_geometria": EXTRATOR_GEOMETRIA, "sha256_geometria": SHA_GEOMETRIA,
        "sha256_classificador": classificador_sha, "edicoes": len(edicoes),
        "so_cache": bool(a.so_cache), "rps_max": 2, "modo": "leis-complementares",
        "contagens": dict(cont), "arquivos": [str(Path(p).relative_to(RAIZ)) for p in gravados],
        "numeros": [k[0] for k in sorted(por_chave, key=lambda x: (x[1], int(x[0])))],
        "resto": resto, "baixado_em": hoje,
    }
    gravar_json(lote / "manifesto.json", manifesto)
    (lote / "lista.txt").write_text("\n".join(manifesto["arquivos"]) + ("\n" if gravados else ""))
    print("gravadas", len(gravados), "em", pasta_md, flush=True)
    return 0


def persistir_lo(pasta_md, item, num, ano_ep, bloco, data, sha_pdf, classificador_sha, hoje):
    data_edicao = item.get("data_publicacao") or ""
    ano = (data or ano_ep)[:4]
    corpo = corpo_markdown(bloco)
    if len(re.sub(r"\W", "", corpo)) < 80:
        return None
    edicao = numero_edicao(item)
    codigo = "%s-%s-LO-%s" % (item.get("tipo") or "DOM", edicao, num)
    slug = slugify("leis-ordinarias-%s-%s-%s" % (num, ano, codigo.lower()))[:110]
    destino = pasta_md / ano / (slug + ".md")
    meta = {
        "titulo": titulo_lo(num, data),
        "tipo": CANONICO["lei ordinaria"][1],
        "tipo_na_fonte": "Lei Ordinária",
        "numero": num,
        "data": data,
        "ano": ano,
        "municipio": MUNICIPIO,
        "uf": UF,
        "codigo_ibge": IBGE_SALVADOR,
        "revogada": None,
        "versao_texto": "publicação original no Diário Oficial do Município (CMS/Dioly)"
        + ("; republicada por incorreção" if REPUBLICADA.search(bloco) else ""),
        "extrator": EXTRATOR,
        "sha256_classificador": classificador_sha,
        "sha256_extrator_geometria": SHA_GEOMETRIA,
        "sha256_pdf": sha_pdf,
        "sha256_texto": hashlib.sha256(corpo.encode()).hexdigest(),
        "publicacao": "%s nº %s de %s" % (
            item.get("tipo") or "DOM", edicao,
            dt.date.fromisoformat(data_edicao).strftime("%d/%m/%Y") if data_edicao else ""),
        "data_publicacao": data_edicao,
        "codigo_identificador": codigo,
        "fonte": item["pdf_url"],
        "baixado_em": hoje,
    }
    if destino.exists():
        destino.unlink()
    gravar_emenda(destino, meta, corpo)
    return destino


def coletar_lo(a, rede, edicoes, pasta_fonte, classificador_sha, hoje):
    pasta_md = RAIZ / "municipais" / UF / "salvador" / "leis-ordinarias"
    lote = RAIZ / ("municipais/_lotes/%s-salvador-leis-ordinarias" % hoje.replace("-", ""))
    lote.mkdir(parents=True, exist_ok=True)
    gravar_json(lote / "edicoes.json", edicoes)
    falhas_path = lote / "falhas.jsonl"
    falhas_path.write_text("")
    cont = collections.Counter()
    por_chave = {}
    descartes = []
    with falhas_path.open("a", encoding="utf-8") as falhas:
        for n, item in enumerate(edicoes, 1):
            pdf = caminho_pdf(pasta_fonte, item)
            try:
                bruto, _cache = baixar_pdf(rede, item, pdf)
                achados, falha = [], None
                amostra = texto_raw(pdf)
                if pdf_escaneado(amostra) and len(re.sub(r"\W", "", amostra)) < 80:
                    falha = {"status": "sem_texto", "motivo": "PDF sem texto legível", "edicao": item["id"]}
                else:
                    achados = extrair_lo(pdf)
            except Exception as e:
                falha = {"status": "erro", "edicao": item.get("id"), "data": item.get("data_publicacao"),
                         "fonte": item.get("pdf_url"), "erro": str(e)[:400]}
                achados = []
            if falha:
                falhas.write(json.dumps(falha, ensure_ascii=False) + "\n")
                falhas.flush()
                cont[falha.get("status", "erro")] += 1
                continue
            data_edicao = item.get("data_publicacao") or ""
            validos = []
            for num, ano, bloco in achados:
                data = lo_contemporanea(bloco, ano, data_edicao)
                if not data:
                    descartes.append({"numero": num, "ano": ano, "edicao": numero_edicao(item),
                                      "motivo": "gabinete ausente/fora do ano ou antigo (edital/anexo)"})
                    continue
                validos.append((num, ano, bloco, data))
            if not validos:
                cont["sem_lo_sancionada"] += 1
            else:
                cont["ok"] += 1
                sha_pdf = hashlib.sha256(bruto).hexdigest()
                for num, ano, bloco, data in validos:
                    chave = (num, ano)
                    nota = nota_lc(bloco) + (data_edicao,)
                    atual = por_chave.get(chave)
                    if atual is not None and nota <= atual[0]:
                        continue
                    destino = persistir_lo(pasta_md, item, num, ano, bloco, data, sha_pdf,
                                           classificador_sha, hoje)
                    if destino is None:
                        continue
                    if atual is not None:
                        antigo = atual[1]
                        if antigo != destino and Path(antigo).exists():
                            Path(antigo).unlink()
                    por_chave[chave] = (nota, destino)
                    print("  LO %s/%s → %s" % (num, ano, destino.relative_to(RAIZ)), flush=True)
            if n % 10 == 0 or n == len(edicoes):
                print("[%s/%s] %s chaves=%s" % (n, len(edicoes), dict(cont), len(por_chave)), flush=True)
    ordem = sorted(por_chave, key=lambda x: (x[1], int(x[0])))
    gravados = [str(por_chave[k][1]) for k in ordem]
    manifesto = {
        "municipio": MUNICIPIO, "uf": UF, "codigo_ibge": IBGE_SALVADOR,
        "fonte_api": API, "rps": a.rps, "consultas": [] if a.completo else list(CONSULTAS_LO),
        "completo": bool(a.completo),
        "intervalo": [a.de, a.ate], "tipo": a.tipo, "extrator": EXTRATOR,
        "extrator_geometria": EXTRATOR_GEOMETRIA, "sha256_geometria": SHA_GEOMETRIA,
        "sha256_classificador": classificador_sha, "edicoes": len(edicoes),
        "so_cache": bool(a.so_cache), "rps_max": 2, "modo": "leis-ordinarias",
        "contagens": dict(cont), "arquivos": [str(Path(p).relative_to(RAIZ)) for p in gravados],
        "numeros": ["%s/%s" % k for k in ordem],
        "descartes": descartes,
        "observacao": (
            "Só leis sancionadas pelo prefeito (epígrafe LEI Nº em caixa alta, Art. 1º, sanção, "
            "gabinete). Leis promulgadas pela Câmara (veto derrubado), projetos, citações e leis "
            "antigas reproduzidas em edital/anexo não entram."
        ),
        "baixado_em": hoje,
    }
    gravar_json(lote / "manifesto.json", manifesto)
    (lote / "lista.txt").write_text("\n".join(manifesto["arquivos"]) + ("\n" if gravados else ""))
    print("gravadas", len(gravados), "em", pasta_md, flush=True)
    return 0


def persistir_dec(pasta_md, item, num, ano_ep, bloco, data, sha_pdf, classificador_sha, hoje):
    data_edicao = item.get("data_publicacao") or ""
    ano = (data or ano_ep)[:4]
    corpo = corpo_markdown(bloco)
    if len(re.sub(r"\W", "", corpo)) < 80:
        return None
    edicao = numero_edicao(item)
    codigo = "%s-%s-DEC-%s" % (item.get("tipo") or "DOM", edicao, num)
    slug = slugify("decretos-%s-%s-%s" % (num, ano, codigo.lower()))[:110]
    destino = pasta_md / ano / (slug + ".md")
    meta = {
        "titulo": titulo_dec(num, data),
        "tipo": CANONICO["decreto"][1],
        "tipo_na_fonte": "Decreto",
        "numero": num,
        "data": data,
        "ano": ano,
        "municipio": MUNICIPIO,
        "uf": UF,
        "codigo_ibge": IBGE_SALVADOR,
        "revogada": None,
        "versao_texto": "publicação original no Diário Oficial do Município (Dioly)"
        + ("; republicada por incorreção" if REPUBLICADA.search(bloco) else ""),
        "extrator": EXTRATOR,
        "sha256_classificador": classificador_sha,
        "sha256_extrator_geometria": SHA_GEOMETRIA,
        "sha256_pdf": sha_pdf,
        "sha256_texto": hashlib.sha256(corpo.encode()).hexdigest(),
        "publicacao": "%s nº %s de %s" % (
            item.get("tipo") or "DOM", edicao,
            dt.date.fromisoformat(data_edicao).strftime("%d/%m/%Y") if data_edicao else ""),
        "data_publicacao": data_edicao,
        "codigo_identificador": codigo,
        "fonte": item["pdf_url"],
        "baixado_em": hoje,
    }
    if destino.exists():
        destino.unlink()
    gravar_emenda(destino, meta, corpo)
    return destino


def coletar_dec(a, rede, edicoes, pasta_fonte, classificador_sha, hoje):
    """Decretos numerados do Prefeito no DOM; soma aos md já gravados (dedup por número/ano)."""
    pasta_md = RAIZ / "municipais" / UF / "salvador" / CANONICO["decreto"][0]
    existentes = chaves_existentes(pasta_md)
    ja_existiam = collections.Counter()
    nome_lote = a.lote or "%s-salvador-decretos-%s-%s" % (hoje.replace("-", ""), a.de[:4], a.ate[:4])
    lote = RAIZ / "municipais/_lotes" / nome_lote
    lote.mkdir(parents=True, exist_ok=True)
    gravar_json(lote / "edicoes.json", edicoes)
    falhas_path = lote / "falhas.jsonl"
    falhas_path.write_text("")
    cont = collections.Counter()
    por_chave = {}
    descartes = []
    with falhas_path.open("a", encoding="utf-8") as falhas:
        for n, item in enumerate(edicoes, 1):
            pdf = caminho_pdf(pasta_fonte, item)
            try:
                bruto, _cache = baixar_pdf(rede, item, pdf)
                achados, desc, falha = [], [], None
                amostra = texto_raw(pdf)
                if pdf_escaneado(amostra) and len(re.sub(r"\W", "", amostra)) < 80:
                    falha = {"status": "sem_texto", "motivo": "PDF sem texto legível", "edicao": item["id"]}
                else:
                    achados, desc = extrair_dec(pdf)
            except Exception as e:
                falha = {"status": "erro", "edicao": item.get("id"), "data": item.get("data_publicacao"),
                         "fonte": item.get("pdf_url"), "erro": str(e)[:400]}
                achados, desc = [], []
            if falha:
                falhas.write(json.dumps(falha, ensure_ascii=False) + "\n")
                falhas.flush()
                cont[falha.get("status", "erro")] += 1
                continue
            data_edicao = item.get("data_publicacao") or ""
            for num, ano, motivo in desc:
                descartes.append({"numero": num, "ano": ano, "edicao": numero_edicao(item), "motivo": motivo})
            validos = []
            for num, ano, bloco in achados:
                data = data_dec(bloco, ano, data_edicao)
                if not data:
                    descartes.append({"numero": num, "ano": ano, "edicao": numero_edicao(item),
                                      "motivo": "gabinete fora do ano/da edição (reprodução ou citação)"})
                    continue
                validos.append((num, ano, bloco, data))
            if not validos:
                cont["sem_decreto"] += 1
            else:
                cont["ok"] += 1
                sha_pdf = hashlib.sha256(bruto).hexdigest()
                for num, ano, bloco, data in validos:
                    chave = (num, ano)
                    velho = existentes.get(chave)
                    codigo = "%s-%s-DEC-%s" % (item.get("tipo") or "DOM", numero_edicao(item), num)
                    if velho is not None and velho[1] != codigo:
                        ja_existiam[chave] += 1
                        continue
                    nota = nota_lc(bloco) + (data_edicao,)
                    atual = por_chave.get(chave)
                    if atual is not None and nota <= atual[0]:
                        continue
                    destino = persistir_dec(pasta_md, item, num, ano, bloco, data, sha_pdf,
                                            classificador_sha, hoje)
                    if destino is None:
                        continue
                    if atual is not None:
                        antigo = atual[1]
                        if antigo != destino and Path(antigo).exists():
                            Path(antigo).unlink()
                    por_chave[chave] = (nota, destino)
            if n % 10 == 0 or n == len(edicoes):
                print("[%s/%s] %s chaves=%s" % (n, len(edicoes), dict(cont), len(por_chave)), flush=True)
    ordem = sorted(por_chave, key=lambda x: (x[1], int(x[0])))
    gravados = [str(por_chave[k][1]) for k in ordem]
    manifesto = {
        "municipio": MUNICIPIO, "uf": UF, "codigo_ibge": IBGE_SALVADOR,
        "fonte_api": API, "rps": a.rps, "consultas": [] if a.completo else list(CONSULTAS_DEC),
        "completo": bool(a.completo),
        "intervalo": [a.de, a.ate], "tipo": a.tipo, "extrator": EXTRATOR,
        "extrator_geometria": EXTRATOR_GEOMETRIA, "sha256_geometria": SHA_GEOMETRIA,
        "sha256_classificador": classificador_sha, "edicoes": len(edicoes),
        "so_cache": bool(a.so_cache), "rps_max": 2, "modo": "decretos",
        "contagens": dict(cont), "arquivos": [str(Path(p).relative_to(RAIZ)) for p in gravados],
        "numeros": ["%s/%s" % k for k in ordem],
        "ja_existiam": len(ja_existiam),
        "novos": ["%s/%s" % k for k in ordem if k not in existentes],
        "descartes": descartes,
        "observacao": (
            "Só decretos numerados do Prefeito (epígrafe DECRETO Nº em linha própria, O PREFEITO … "
            "DECRETA:, Art. 1º, GABINETE DO PREFEITO datado no ano da epígrafe e até 1 ano antes da "
            "edição, assinatura do Prefeito). Decretos legislativos, decretos simples sem número, "
            "retificações, citações em parecer e projetos não entram. Anexo próprio (ANEXO …) entra."
        ),
        "baixado_em": hoje,
    }
    gravar_json(lote / "manifesto.json", manifesto)
    (lote / "lista.txt").write_text("\n".join(manifesto["arquivos"]) + ("\n" if gravados else ""))
    print("gravados", len(gravados), "em", pasta_md, flush=True)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--indice", type=Path, help="JSON local (lista de edições). Sem isso, consulta a API.")
    ap.add_argument("--atualizar-indice", action="store_true",
                    help="varre todas as páginas da API e grava --indice")
    ap.add_argument("--tipo", default=None, help="DOL (emendas) ou DOM (LC/LO); padrão conforme --modo")
    ap.add_argument("--de", default="2010-01-01")
    ap.add_argument("--ate", default="2026-12-31")
    ap.add_argument("--rps", type=float, default=2)
    ap.add_argument("--modo", choices=("emendas", "leis-complementares", "leis-ordinarias",
                                       "resolucoes", "decretos-legislativos", "decretos"),
                    default="emendas")
    ap.add_argument("--lote", default=None,
                    help="nome da pasta em municipais/_lotes/ (resoluções/DL; padrão por série+janela)")
    ap.add_argument("--completo", action="store_true",
                    help="baixa todo DOL no intervalo, sem filtro q= (milhares de PDFs)")
    ap.add_argument("--so-cache", action="store_true",
                    help="não consulta a API; processa só PDFs já gravados em municipais/_fonte/dioly/")
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args(argv)
    if a.tipo is None:
        a.tipo = "DOL" if a.modo in ("emendas", "resolucoes", "decretos-legislativos") else "DOM"
    if not 0 < a.rps <= 2:
        ap.error("--rps máximo 2")
    conferir_ibge(RAIZ)
    rede = Rede(rps=a.rps)
    pasta_fonte = RAIZ / "municipais/_fonte/dioly/salvador"
    consultas = {"leis-complementares": CONSULTAS_LC,
                 "leis-ordinarias": CONSULTAS_LO,
                 "resolucoes": CONSULTAS_RES,
                 "decretos-legislativos": CONSULTAS_DL,
                 "decretos": CONSULTAS_DEC}.get(a.modo, CONSULTAS_PADRAO)
    if a.atualizar_indice:
        if not a.indice:
            ap.error("--atualizar-indice exige --indice")
        itens = baixar_indice(rede)
        gravar_json(a.indice, itens)
        print("índice", len(itens), "edições →", a.indice, flush=True)
    if a.so_cache:
        if not a.indice or not a.indice.exists():
            ap.error("--so-cache exige --indice com o JSON local")
        edicoes = filtrar_edicoes(carregar_indice(a.indice), tipo=a.tipo, inicio=a.de, fim=a.ate)
        edicoes = [it for it in edicoes if caminho_pdf(pasta_fonte, it).exists()]
    elif a.completo:
        if a.indice and a.indice.exists():
            itens = carregar_indice(a.indice)
        else:
            itens = baixar_indice(rede, tipo=a.tipo)
        edicoes = filtrar_edicoes(itens, tipo=a.tipo, inicio=a.de, fim=a.ate)
    else:
        edicoes = filtrar_edicoes(candidatos(rede, tipo=a.tipo, consultas=consultas),
                                 tipo=a.tipo, inicio=a.de, fim=a.ate)
        if a.indice and a.indice.exists():
            por_id = {x["id"]: x for x in carregar_indice(a.indice)}
            edicoes = [por_id.get(x["id"], x) for x in edicoes]
    if a.limite:
        edicoes = edicoes[:a.limite]
    print("%s edições %s %s–%s modo=%s" % (len(edicoes), a.tipo, a.de, a.ate, a.modo), flush=True)
    if a.listar:
        for it in edicoes:
            print(it.get("data_publicacao"), it.get("numero"), it.get("pdf_url"))
        return 0

    classificador_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    hoje = dt.date.today().isoformat()
    if a.modo == "leis-complementares":
        return coletar_lc(a, rede, edicoes, pasta_fonte, classificador_sha, hoje)
    if a.modo == "leis-ordinarias":
        return coletar_lo(a, rede, edicoes, pasta_fonte, classificador_sha, hoje)
    if a.modo == "decretos":
        return coletar_dec(a, rede, edicoes, pasta_fonte, classificador_sha, hoje)
    if a.modo in SERIES_MESA:
        return coletar_mesa(a, rede, edicoes, pasta_fonte, classificador_sha, hoje)

    pasta_md = RAIZ / "municipais" / UF / "salvador" / "emendas-lei-organica"
    falhas_path = RAIZ / "municipais/BA/salvador/_falhas.jsonl"
    falhas_path.parent.mkdir(parents=True, exist_ok=True)
    falhas_path.write_text("")
    cont = collections.Counter()
    gravados = []
    vistos = set()
    with falhas_path.open("a", encoding="utf-8") as falhas:
        for n, item in enumerate(edicoes, 1):
            pdf = caminho_pdf(pasta_fonte, item)
            try:
                bruto, cache = baixar_pdf(rede, item, pdf)
                arquivos, falha = processar_edicao(item, pdf, bruto, pasta_md, classificador_sha, hoje,
                                                   vistos=vistos)
            except Exception as e:
                falha = {"status": "erro", "edicao": item.get("id"), "data": item.get("data_publicacao"),
                         "fonte": item.get("pdf_url"), "erro": str(e)[:400]}
                arquivos = []
            if falha:
                falhas.write(json.dumps(falha, ensure_ascii=False) + "\n")
                falhas.flush()
                cont[falha.get("status", "erro")] += 1
            elif arquivos:
                cont["ok"] += 1
                gravados.extend(arquivos)
            else:
                cont["sem_emenda_promulgada"] += 1
            if n % 10 == 0 or n == len(edicoes):
                print("[%s/%s] %s" % (n, len(edicoes), dict(cont)), flush=True)
    manifesto = {
        "municipio": MUNICIPIO, "uf": UF, "codigo_ibge": IBGE_SALVADOR,
        "fonte_api": API, "rps": a.rps, "consultas": list(CONSULTAS_PADRAO),
        "intervalo": [a.de, a.ate], "tipo": a.tipo, "extrator": EXTRATOR,
        "extrator_geometria": EXTRATOR_GEOMETRIA, "sha256_geometria": SHA_GEOMETRIA,
        "sha256_classificador": classificador_sha, "edicoes": len(edicoes),
        "so_cache": bool(a.so_cache), "rps_max": 2,
        "contagens": dict(cont), "arquivos": [str(Path(p).relative_to(RAIZ)) for p in gravados],
        "baixado_em": hoje,
    }
    lote = RAIZ / "municipais/_lotes/20261028-salvador-emendas-elo"
    gravar_json(lote / "manifesto.json", manifesto)
    print("gravadas", len(gravados), "em", pasta_md, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
