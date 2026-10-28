"""Baixa diários oficiais de Salvador (portal CMS Dioly) e extrai atos promulgados.

O índice vem de `GET https://portal-api.dioly.com.br/api/diarios/?page=N` (≤2 req/s). A busca
`q=` do próprio CMS localiza edições cujo PDF menciona a frase. PDFs são retomáveis em
`municipais/_fonte/dioly/`. O texto sai de `pdftotext -raw` (histórias InDesign).

`--modo emendas` (padrão) lê o DOL e fica só com emendas à LOM promulgadas pela Mesa.
`--modo leis-complementares` lê o DOM e fica só com leis complementares sancionadas
(epígrafe `LEI COMPLEMENTAR Nº`, Art. 1º, sanção, gabinete). Projetos ficam de fora.
Citações a LC em portaria, contrato ou balanço não entram.
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
    r"(?P<dia>\d{1,2})\s+de\s+(?P<mes>\w+)\s+de\s+(?P<ano>\d{4})",
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


def data_do_gabinete(bloco, data_edicao):
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
            if d > limite + dt.timedelta(days=3):
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--indice", type=Path, help="JSON local (lista de edições). Sem isso, consulta a API.")
    ap.add_argument("--atualizar-indice", action="store_true",
                    help="varre todas as páginas da API e grava --indice")
    ap.add_argument("--tipo", default="DOL")
    ap.add_argument("--de", default="2010-01-01")
    ap.add_argument("--ate", default="2026-12-31")
    ap.add_argument("--rps", type=float, default=2)
    ap.add_argument("--modo", choices=("emendas", "leis-complementares"), default="emendas")
    ap.add_argument("--completo", action="store_true",
                    help="baixa todo DOL no intervalo, sem filtro q= (milhares de PDFs)")
    ap.add_argument("--so-cache", action="store_true",
                    help="não consulta a API; processa só PDFs já gravados em municipais/_fonte/dioly/")
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args(argv)
    if not 0 < a.rps <= 2:
        ap.error("--rps máximo 2")
    conferir_ibge(RAIZ)
    rede = Rede(rps=a.rps)
    pasta_fonte = RAIZ / "municipais/_fonte/dioly/salvador"
    consultas = CONSULTAS_LC if a.modo == "leis-complementares" else CONSULTAS_PADRAO
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
