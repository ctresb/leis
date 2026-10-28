"""Captura documentos estruturantes das capitais em publicações oficiais identificadas.

Catálogo explícito de fontes: não adivinha URLs, datas ou números. Preserva os
binários, o corte da compilação e anexos, sem contar cada anexo como nova norma.

Itens `extrator=dioly-raw` saem de `pdftotext -raw` no DOM/Dioly (histórias InDesign),
com recorte da lei e limpeza do chrome do jornal; rps ≤ 2.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import Rede, documento_para_md, normalizar_chave, texto_pdf_para_md, yaml_str
from baixar_dioly import juntar_hifen, texto_raw, url_segura

RAIZ = Path(__file__).resolve().parent.parent
API_DIOLY = "https://portal-api.dioly.com.br/api/diarios/"
EPIGRAFE_LEI = re.compile(
    r"LEI\s+N[ºo°. ]?\s*(?P<num>\d{1,3}(?:\.\d{3})*)/(?P<ano>\d{4})", re.I)
COLOFON = re.compile(r"Criado pelo art\.\s*82 da Lei n", re.I)
COLOFON_BLOCO = re.compile(
    r"Criado pelo art\.\s*82 da Lei n[ºo°.].{0,120}\n(?:.*\n){0,22}?"
    r"(?:Chefe de Gabinete do Prefeito, em exercício|CEP:\s*40\.020-000)[^\n]*\n?",
    re.I)
CHROME_DOM = re.compile(
    r"^(?:DI[AÁ]RIO OFICIAL DO(?:\s+MUNIC[IÍ]PIO(?:\s+DO\s+SALVADOR)?)?|"
    r"SALVADOR[-–—• ]+BAHIA|SALVADOR-BAHIA|"
    r"ANO\s+[IVXLC]+\s*\|?\s*N\s*[ºo°.]?\s*[\d.]+(?:\s+\d{1,3})?|"
    r"(?:Segunda|Ter[cç]a|Quarta|Quinta|Sexta)-feira|S[aá]bado|Domingo|"
    r"[0-3]?\d DE (?:JANEIRO|FEVEREIRO|MAR[CÇ]O|ABRIL|MAIO|JUNHO|JULHO|"
    r"AGOSTO|SETEMBRO|OUTUBRO|NOVEMBRO|DEZEMBRO) DE 20\d{2}|"
    r"Ouvidoria Geral do Munic[ií]pio|"
    r"Disque Salvador|"
    r"Di[aá]rio Oficial do Munic[ií]pio - Edi[cç][oõ]es Anteriores|"
    r"CEP:\s*40\.020-000|"
    r"Coordenador de Tecnologia|"
    r"www\.(?:ouvidoria|disquesalvador|dom)\.|"
    r"atendimento 24h\.?|"
    r"E\s*D\s*I[CÇ]\s*[AÃ]\s*O\s*E\s*X\s*T\s*R\s*A"
    r")\s*$", re.I)
LETRA_VERTICAL = re.compile(r"^[EDIÇÃOEXTRAÇÃOedicaoextra]{1}$")
ASSINATURA_GABINETE = re.compile(
    r"GABINETE DO PREFEITO MUNICIPAL DO SALVADOR,\s*em\s+"
    r"(?P<dia>\d{1,2})\s+de\s+(?P<mes>\w+)\s+de\s+(?P<ano>\d{4})", re.I)

CATALOGO = [{
    'municipio': 'Recife', 'uf': 'PE', 'codigo_ibge': '2611606',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-04-04',
    'titulo': 'Lei Orgânica do Município do Recife, de 4 de abril de 1990',
    'slug': 'lei-organica-recife-1990', 'cache': 'recife-organica.pdf',
    'fonte': 'https://transparencia.recife.pe.leg.br/institucional/competencias/lei-organica_atualizada-em-08-04-2024.pdf',
    'fonte_texto': 'https://transparencia.recife.pe.leg.br/institucional/competencias/lei-organica_atualizada-em-08-04-2024.pdf/@@download/file',
    'versao_texto': 'compilação oficial atualizada em 08/04/2024, com emendas anexas; não certifica atualização posterior',
    'marcas_obrigatorias': ['LEI ORGÂNICA DO MUNICÍPIO DO RECIFE', 'Promulgada em 4 de abril de 1990',
                           'Atualizada em 08 de abril de 2024'],
}, {
    'municipio': 'São Paulo', 'uf': 'SP', 'codigo_ibge': '3550308',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-04-04',
    'titulo': 'Lei Orgânica do Município de São Paulo, de 4 de abril de 1990',
    'slug': 'lei-organica-sao-paulo-1990', 'cache': 'sao-paulo-organica.pdf',
    'fonte': 'https://www.saopaulo.sp.leg.br/lei-organica/',
    'fonte_texto': 'https://www.saopaulo.sp.leg.br/wp-content/uploads/2022/09/LOMC.pdf',
    'versao_texto': 'compilação oficial, edição 2026 atualizada até a Emenda 44/25; índice remissivo preservado',
    'marcas_obrigatorias': ['LEI ORGÂNICA DO MUNICÍPIO DE SÃO PAULO', 'Atualizada até a Emenda 44/25',
                           'São Paulo, 4 de abril de 1990'],
}, {
    'municipio': 'Salvador', 'uf': 'BA', 'codigo_ibge': '2927408',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-04-05',
    'titulo': 'Lei Orgânica do Município de Salvador, de 5 de abril de 1990',
    'slug': 'lei-organica-salvador-1990', 'cache': 'salvador-organica.pdf',
    'fonte': 'https://www.cms.ba.gov.br/lei-organica',
    'fonte_texto': 'https://www.cms.ba.gov.br/uploads/3bdae368d1a3e255c81b7f262ba1bbf6_1709038424.pdf',
    'versao_texto': 'compilação oficial da Câmara Municipal de Salvador, edição consolidada até a Emenda nº 41/2024; a edição não imprime a data de promulgação original; não certifica atualização posterior',
    'marcas_obrigatorias': ['Lei Orgânica do Município de Salvador', 'Edição consolidada até a Emenda nº 41',
                           'O Município de Salvador, Capital do Estado da Bahia'],
}, {
    'municipio': 'Salvador', 'uf': 'BA', 'codigo_ibge': '2927408',
    'tipo': 'Plano diretor', 'tipo_na_fonte': 'Lei', 'categoria': 'plano-diretor',
    'numero': '9069', 'data': '2016-06-30',
    'titulo': 'Lei nº 9.069, de 30 de junho de 2016',
    'slug': 'plano-diretor-9069-2016', 'cache': 'dom-6620-2016-06-30.pdf',
    'fonte': 'https://portal-api.dioly.com.br/uploads/pdfs/59331b95-e95d-401a-8fef-80b5220dc737_dom-6620-30-06-2016.pdf',
    'fonte_texto': 'https://portal-api.dioly.com.br/uploads/pdfs/59331b95-e95d-401a-8fef-80b5220dc737_dom-6620-30-06-2016.pdf',
    'publicacao': 'DOM nº 6620 de 30/06/2016',
    'data_publicacao': '2016-06-30',
    'codigo_identificador': 'DOM-6620-LEI-9069',
    'extrator': 'dioly-raw-v2',
    'versao_texto': 'publicação original no Diário Oficial do Município (CMS/Dioly), edição extra nº 6620; anexos tipográficos da mesma edição; mapas raster do Anexo 03 permanecem no PDF-fonte e não contam como norma nova; PDF CMS pdducorpodalei.pdf é o PL 396/2015 e foi descartado; não certifica atualização posterior',
    'marcas_obrigatorias': [
        'LEI Nº 9.069/2016',
        'Plano Diretor de Desenvolvimento Urbano',
        'GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 30 de junho de 2016',
    ],
}, {
    'municipio': 'Salvador', 'uf': 'BA', 'codigo_ibge': '2927408',
    'tipo': 'Código municipal', 'tipo_na_fonte': 'Lei', 'categoria': 'codigos',
    'numero': '9148', 'data': '2016-09-08',
    'titulo': 'Lei nº 9.148, de 8 de setembro de 2016',
    'slug': 'louos-9148-2016', 'cache': 'dom-6672-2016-09-08.pdf',
    'fonte': 'https://portal-api.dioly.com.br/uploads/pdfs/be6cece9-e772-4a09-bfe4-5f71ae42d328_dom-6672-08-09-2016.pdf',
    'fonte_texto': 'https://portal-api.dioly.com.br/uploads/pdfs/be6cece9-e772-4a09-bfe4-5f71ae42d328_dom-6672-08-09-2016.pdf',
    'publicacao': 'DOM nº 6672 de 08/09/2016',
    'data_publicacao': '2016-09-08',
    'codigo_identificador': 'DOM-6672-LEI-9148',
    'extrator': 'dioly-raw-v2',
    'versao_texto': 'publicação original no Diário Oficial do Município (CMS/Dioly), edição nº 6672; anexos tipográficos da mesma edição; mapas raster permanecem no PDF-fonte e não contam como norma nova; PDF CMS louoscorpodalei.pdf não imprime o número 9.148 e não foi usado como texto; não certifica atualização posterior',
    'marcas_obrigatorias': [
        'LEI Nº 9.148/2016',
        'Ordenamento do Uso e da Ocupação do Solo',
        'GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 08 de setembro de 2016',
    ],
}]

PULAR = [{
    'municipio': 'Salvador', 'uf': 'BA', 'codigo_ibge': '2927408',
    'tipo': 'Código tributário', 'numero': '7186', 'ano': '2006',
    'status': 'sem_fonte_https',
    'motivo': 'Lei 7.186/2006: índice Dioly DOM sem edições de 2006–2007 (acervo começa ~2010/11); busca q="Codigo Tributario" devolve só DOM 6937/2017 e 8910/2024; ocorrências de 7.186 são citações posteriores, não a promulgação; leismunicipais (Cloudflare) e flipbook http cmsba.dyndns.org fora do escopo',
}]


def numero_epigrafe(numero):
    s = re.sub(r"\D", "", str(numero or ""))
    if not s:
        return ""
    s = s.lstrip("0") or "0"
    if len(s) > 3:
        s = s[:-3] + "." + s[-3:]
    return s


def recortar_lei_dom(texto, numero, ano):
    """Recorta a lei numerada no DOM extra; não corta no colofão precoce do InDesign."""
    alvo = re.sub(r"\D", "", str(numero)).lstrip("0") or "0"
    inicio = None
    for m in EPIGRAFE_LEI.finditer(texto):
        n = re.sub(r"\D", "", m.group("num")).lstrip("0") or "0"
        if n == alvo and m.group("ano") == str(ano):
            inicio = m.start()
            break
    if inicio is None:
        raise ValueError("epígrafe da lei %s/%s ausente" % (numero, ano))
    corpo = texto[inicio:]
    gab = ASSINATURA_GABINETE.search(corpo)
    fins = list(COLOFON.finditer(corpo))
    if fins:
        ultimo = fins[-1]
        depois = corpo[ultimo.end():]
        if (gab is None or ultimo.start() > gab.start()) and not re.search(
                r"Art\.|ANEXO|QUADRO", depois, re.I):
            corpo = corpo[:ultimo.start()]
    return corpo.strip() + "\n"


def limpar_chrome_dom(texto):
    """Remove masthead, colofão e EDIÇÃO EXTRA vertical; preserva a assinatura do gabinete."""
    texto = COLOFON_BLOCO.sub("\n", texto)
    linhas = []
    for ln in texto.splitlines():
        s = ln.strip()
        if not s:
            linhas.append("")
            continue
        if LETRA_VERTICAL.match(s):
            continue
        if CHROME_DOM.match(s):
            continue
        if re.fullmatch(r"\d{1,3}", s):
            continue
        linhas.append(ln)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip() + "\n"


CHROME_MD = re.compile(
    r"DI[AÁ]RIO OFICIAL DO(?:\s+SALVADOR-BAHIA)?|"
    r"ANO\s+[IVXLC]+\s*\|\s*N\s*[ºo°.]?\s*[\d.]+(?:\s+\d{1,3})?",
    re.I)


def limpar_chrome_md(md):
    md = CHROME_MD.sub("", md)
    md = re.sub(r"[ \t]{2,}", " ", md)
    md = re.sub(r"\n[ \t]+", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def corpo_dom_raw(pdf, numero, ano):
    bruto = texto_raw(pdf)
    recorte = recortar_lei_dom(bruto, numero, ano)
    limpo = limpar_chrome_dom(recorte)
    return limpar_chrome_md(texto_pdf_para_md(juntar_hifen(limpo)))


def campos_meta(item):
    chaves = ['titulo', 'tipo', 'tipo_na_fonte', 'numero', 'data', 'municipio', 'uf',
              'codigo_ibge', 'versao_texto', 'fonte', 'fonte_texto', 'publicacao',
              'data_publicacao', 'codigo_identificador', 'extrator']
    return {k: item[k] for k in chaves if k in item and item[k] not in (None, "")}


def gravar_markdown(destino, item, corpo, sha_fonte, baixado_em):
    meta = campos_meta(item)
    meta.update({
        'sha256_fonte': sha_fonte,
        'sha256_texto': hashlib.sha256(corpo.encode()).hexdigest(),
        'baixado_em': baixado_em,
    })
    linhas = ["---"]
    for k, v in meta.items():
        linhas.append("%s: %s" % (k, yaml_str(v)))
    linhas += ["revogada: null", "---", "", "# " + item["titulo"], "", corpo]
    if not corpo.endswith("\n"):
        linhas.append("")
    texto = "\n".join(linhas)
    if not texto.endswith("\n"):
        texto += "\n"
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("x") as f:
        f.write(texto)
    return texto


def conferir_marcas(corpo, item):
    normal = normalizar_chave(corpo)
    for marca in item["marcas_obrigatorias"]:
        if normalizar_chave(marca) not in normal:
            raise ValueError("marca de identidade/data ausente: " + marca)
    if not re.search(r"Art\.?\s*1[º°]", corpo, re.I):
        raise ValueError("artigo inicial não reconhecido")
    if item.get("extrator") == "dioly-raw-v2" and not ASSINATURA_GABINETE.search(corpo):
        raise ValueError("assinatura do gabinete ausente")


def baixar_fonte(rede, item, destino, so_cache):
    if destino.exists() and destino.stat().st_size > 100 and destino.read_bytes()[:4] == b"%PDF":
        return destino.read_bytes(), True
    if so_cache:
        raise ValueError("PDF ausente no cache: " + str(destino))
    st, bruto, _ = rede.get(url_segura(item["fonte_texto"]), tentativas=4, timeout=180)
    if st != 200 or not bruto.startswith(b"%PDF"):
        raise ValueError("fonte indisponível ou não é PDF: HTTP " + str(st))
    destino.parent.mkdir(parents=True, exist_ok=True)
    tmp = destino.with_suffix(destino.suffix + ".tmp")
    tmp.write_bytes(bruto)
    tmp.replace(destino)
    return bruto, False


def processar_item(item, ibge, ibge_path, rede, so_cache, hoje):
    municipio = ibge[item["codigo_ibge"]]
    uf = municipio["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]
    if municipio["nome"] != item["municipio"] or uf != item["uf"]:
        raise ValueError("identidade IBGE diverge do catálogo")
    slug_mun = normalizar_chave(municipio["nome"]).replace(" ", "-")
    destino = RAIZ / "municipais" / uf / slug_mun / item["categoria"] / item["data"][:4] / (item["slug"] + ".md")
    if destino.exists():
        print("já existente", destino, flush=True)
        return None
    outros = list(destino.parent.parent.glob("**/*.md"))
    if outros:
        raise ValueError("categoria já contém publicação; revisar versão antes de criar duplicata: " + str(outros))
    pasta = RAIZ / "municipais/_fonte/capitais" / slug_mun
    pasta.mkdir(parents=True, exist_ok=True)
    fonte = pasta / item["cache"]
    bruto, _cache = baixar_fonte(rede, item, fonte, so_cache)
    if item.get("extrator") == "dioly-raw-v2":
        corpo = corpo_dom_raw(fonte, item["numero"], item["data"][:4])
    else:
        corpo, motivo = documento_para_md(bruto, item["fonte_texto"])
        if motivo:
            raise ValueError(motivo)
    conferir_marcas(corpo, item)
    sha_fonte = hashlib.sha256(bruto).hexdigest()
    texto = gravar_markdown(destino, item, corpo, sha_fonte, hoje)
    comprovacao = {**item, "arquivo": str(destino.relative_to(RAIZ)),
                   "sha256": hashlib.sha256(texto.encode()).hexdigest(),
                   "arquivo_fonte": str(fonte.relative_to(RAIZ)), "sha256_fonte": sha_fonte,
                   "sha256_corpo": hashlib.sha256(corpo.encode()).hexdigest(),
                   "ibge_sha256": hashlib.sha256(ibge_path.read_bytes()).hexdigest(),
                   "verificado_em": dt.datetime.now().isoformat(),
                   "observacao": item.get("versao_texto", "")}
    with (pasta / (item["slug"] + ".manifesto.json")).open("w") as f:
        json.dump(comprovacao, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("gravado", destino, flush=True)
    return str(destino.relative_to(RAIZ))


def gravar_lote(arquivos, pular, hoje):
    lote = RAIZ / "municipais/_lotes/20261028-salvador-planos"
    lote.mkdir(parents=True, exist_ok=True)
    manifesto = {
        "municipio": "Salvador", "uf": "BA", "codigo_ibge": "2927408",
        "fonte_api": API_DIOLY, "rps_max": 2, "extrator": "dioly-raw-v2",
        "arquivos": arquivos, "pular": pular, "baixado_em": hoje,
        "observacao": (
            "PDDU Lei 9.069/2016 = DOM extra 6620 (30/06/2016). "
            "LOUOS Lei 9.148/2016 = DOM 6672 (08/09/2016). "
            "CMS /uploads/pddu/pdducorpodalei.pdf é PL 396/2015, não a lei sancionada. "
            "Mapas SSA_PDDU_15 e flipbook http cmsba.dyndns.org não usados. "
            "Anexos tipográficos entram no mesmo .md; mapas raster ficam no PDF-fonte. "
            "Código tributário 7.186/2006 sem PDF oficial HTTPS."
        ),
    }
    (lote / "manifesto.json").write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n")
    (lote / "lista.txt").write_text("\n".join(arquivos) + ("\n" if arquivos else ""))
    falhas = lote / "falhas.jsonl"
    with falhas.open("w", encoding="utf-8") as f:
        for item in pular:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    return lote


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--so-cache", action="store_true",
                    help="não baixa; exige PDF já gravado em municipais/_fonte/capitais/")
    ap.add_argument("--rps", type=float, default=2)
    a = ap.parse_args(argv)
    if not 0 < a.rps <= 2:
        ap.error("--rps máximo 2")
    ibge_path = RAIZ / "municipais/_indice/ibge-municipios.json"
    ibge = {str(x["id"]): x for x in json.loads(ibge_path.read_text())}
    rede = Rede(rps=a.rps)
    hoje = dt.date.today().isoformat()
    gravados = []
    for item in CATALOGO:
        path = processar_item(item, ibge, ibge_path, rede, a.so_cache, hoje)
        if path:
            gravados.append(path)
    lote = gravar_lote(gravados, PULAR, hoje)
    print("lote", lote, "novos", len(gravados), "pular", len(PULAR), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
