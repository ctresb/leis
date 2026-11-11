"""Baixa e converte automaticamente a legislação de Franca-SP (Diário Oficial DOMF + Câmara Municipal Siscam + Portal PMF).

Fontes oficiais públicas utilizadas (sem WAF/bloqueio, respeitando limite de 1 req/s):
  1. API REST do Diário Oficial do Município de Franca (DOMF):
     - Lista de datas publicadas (2014–hoje, +3.130 edições):
       https://webpmf.franca.sp.gov.br/pmf-diario/rest/diario/init
     - Consulta de edições por data (dd-mm-yyyy):
       https://webpmf.franca.sp.gov.br/pmf-diario/rest/diario/buscaPorArquivo/<dd-mm-yyyy>
     - Busca por termo no índice do Diário Oficial:
       https://webpmf.franca.sp.gov.br/pmf-diario/rest/diario/buscarIndice/<termo>/<exata|todos|qualquer>
     - PDFs oficiais (texto digital nativo):
       https://webpmf.franca.sp.gov.br/arquivos/diario-oficial/documentos/<arquivo.pdf>
  2. Índices CSV e anexos da Câmara Municipal de Franca (Siscam):
     - Normas Jurídicas (GrupoId=4) e Proposituras Sancionadas/Promulgadas (GrupoId=3, TipoId=35,36,37,38,39):
       https://www.franca.sp.leg.br/Siscam/Documentos?Pesquisa=Avancada&ShowSearch=False&GrupoId=3&TipoId=<id>&Export=Csv
  3. PDFs diretos no Portal da Prefeitura:
     - https://www3.franca.sp.gov.br/pdf/Lei_Complementar_432.pdf

Exemplos de uso:
    python3 -I scripts/baixar_franca_sp.py --ultimas 10 --camara
    python3 -I scripts/baixar_franca_sp.py --de 2026-01-01 --ate 2026-11-11
    python3 -I scripts/baixar_franca_sp.py --termo Complementar --max-edicoes 20
"""
import argparse
import csv
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import urllib.parse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import Rede, texto_pdf_para_md, yaml_str  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
MUNICIPIO = "Franca"
UF = "SP"
CODIGO_IBGE = "3516200"
SLUG_MUNICIPIO = "franca"

MESES = {
    "janeiro": "01", "fevereiro": "02", "marco": "03", "março": "03",
    "abril": "04", "maio": "05", "junho": "06", "julho": "07",
    "agosto": "08", "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12",
}

RX_ATO_OU_SECAO = re.compile(
    r"(?m)^(?:"
    r"((?:LEI\s+COMPLEMENTAR|LEI\s+ORDIN[ÁA]RIA|LEI\s+MUNICIPAL|LEI|DECRETO\s+LEGISLATIVO|DECRETO\s+MUNICIPAL|DECRETO|"
    r"EMENDA\s+[ÀA]\s+LEI\s+ORG[ÂA]NICA|RESOLU[ÇC][ÃA]O)\s+N[º°o°]\s*[\d.]+(?:/\d{4})?\s*,\s*DE\s+\d{1,2}[º°]?\s+DE\s+"
    r"[A-ZÇÃÕÁÉÍÓÚ]+\s+DE\s+\d{4}[^\n]*)"
    r"|"
    r"((?:PORTARIA|EDITAL|AVISO|EXTRATO|TERMO|CONV[ÊE]NIO|PORTARIAS|DESPACHO|ATA\s+DE|RELAT[ÓO]RIO|BALANCETE|"
    r"NOTIFICA[ÇC][ÃA]O|AUTO\s+DE\s+INFRA[ÇC][ÃA]O)\b[^\n]*|"
    r"(?:ADMINISTRA[ÇC][ÃA]O\s+E\s+RECURSOS\s+HUMANOS|FINAN[ÇC]AS|INFRAESTRUTURA|SA[ÚU]DE|EDUCA[ÇC][ÃA]O|"
    r"A[ÇC][ÃA]O\s+SOCIAL|MEIO\s+AMBIENTE|SEGURAN[ÇC]A|INOVA[ÇC][ÃA]O\s+E\s+DESENVOLVIMENTO|ESPORTE\s+E\s+CULTURA|"
    r"PROCURADORIA\s+GERAL|AVISOS\s+DE\s+LICITA[ÇC][ÃA]O|C[ÂA]MARA\s+MUNICIPAL\s+DE\s+FRANCA|"
    r"FACULDADE\s+DE\s+DIREITO\s+DE\s+FRANCA|FUNDA[ÇC][ÃA]O\s+ESPORTE|FEAC|UNI-FACEF|SASSOM|EMDEF|PROHAB|"
    r"ENTIDADES\s+SEM\s+FINS\s+LUCRATIVOS|CONSELHOS\s+MUNICIPAIS|DEPARTAMENTO\s+DE\s+[A-ZÇÃÕÁÉÍÓÚ\s]{3,}|"
    r"SECRETARIA\s+MUNICIPAL\s+DE\s+[A-ZÇÃÕÁÉÍÓÚ\s]{3,})[^\n]*)"
    r")$"
)

RX_EPIGRAFE = re.compile(
    r"^(LEI\s+COMPLEMENTAR|LEI\s+ORDIN[ÁA]RIA|LEI\s+MUNICIPAL|LEI|DECRETO\s+LEGISLATIVO|DECRETO\s+MUNICIPAL|DECRETO|"
    r"EMENDA\s+[ÀA]\s+LEI\s+ORG[ÂA]NICA|RESOLU[ÇC][ÃA]O)\s+N[º°o°]\s*([\d.]+)(?:/\d{4})?\s*,\s*DE\s+"
    r"(\d{1,2})[º°]?\s+DE\s+([A-ZÇÃÕÁÉÍÓÚ]+)\s+DE\s+(\d{4})",
    re.I,
)


def data_iso(dia: str, mes_nome: str, ano: str) -> str | None:
    mes = MESES.get(mes_nome.lower().strip())
    if not mes:
        return None
    d = int(re.sub(r"\D", "", dia))
    return f"{ano}-{mes}-{d:02d}"


def categoria_e_tipo(tipo_bruto: str, ementa: str) -> tuple[str, str, str]:
    t = re.sub(r"\s+", " ", tipo_bruto).strip().upper()
    e = re.sub(r"\s+", " ", ementa or "").strip().lower()
    if re.search(r"EMENDA\s+[ÀA]\s+LEI\s+ORG", t):
        return "emendas-lei-organica", "Emenda à Lei Orgânica", "emenda-lei-organica"
    if re.match(r"^LEI\s+ORG", t):
        return "lei-organica", "Lei Orgânica", "lei-organica"
    if re.search(r"DECRETO\s+LEGISLATIVO", t):
        return "decretos-legislativos", "Decreto Legislativo", "decreto-legislativo"
    if re.match(r"^DECRETO", t):
        return "decretos", "Decreto", "decreto"
    if re.match(r"^RESOLU", t):
        return "resolucoes", "Resolução", "resolucao"
    if "COMPLEMENTAR" in t:
        if re.match(r"^(?:institui|aprova|disp[õo]e sobre)\s+(?:o|a|um|uma)?\s*(?:novo\s+)?plano diretor", e):
            return "plano-diretor", "Lei Complementar", "lei-complementar"
        if re.match(r"^(?:institui|aprova|disp[õo]e sobre)\s+(?:o|a|um|uma)?\s*(?:novo\s+)?c[óo]digo tribut[áa]rio", e):
            return "codigo-tributario", "Lei Complementar", "lei-complementar"
        if re.match(r"^(?:institui|aprova|disp[õo]e sobre)\s+(?:o|a|um|uma)?\s*(?:novo\s+)?(?:c[óo]digo|parcelamento do solo)", e):
            return "codigos", "Lei Complementar", "lei-complementar"
        return "leis-complementares", "Lei Complementar", "lei-complementar"
    return "leis-ordinarias", "Lei Ordinária", "lei-ordinaria"


def limpar_texto_domf(texto: str) -> str:
    texto = re.sub(
        r"(?s)EXPEDIENTE\s+Diário Oficial do Município de Franca.*?Date:\s*\d{4}\.\d{2}\.\d{2}\s*(?:\d{2}:\d{2}:\d{2}\s*[+-]\d{2}'\d{2}')?",
        "",
        texto,
    )
    texto = re.sub(r"(?im)^\s*w\s*w\s*w\s*\.\s*f\s*r\s*a\s*n\s*c\s*a.*$", "", texto)
    texto = re.sub(
        r"(?im)^[a-zçãõáéíóú-]+\s*,\s*\d{1,2}\s+de\s+[a-zç]+\s+de\s+\d{4}\s*-\s*ano\s+\d+\s*-\s*n[º°]\s*[\d.]+.*$",
        "",
        texto,
    )
    return texto


def extrair_ementa_do_corpo(corpo_md: str) -> str:
    blocos = corpo_md.split("\n\n")
    if len(blocos) < 2:
        return ""
    m = re.search(r"DE\s+\d{4}\.?\s*(?:\([^)]+\))?\s*(.+)$", blocos[0])
    if m:
        cand = m.group(1).strip(' "“”')
        if len(cand) > 20 and not re.match(r"^(ALEXANDRE|O PREFEITO|A CÂMARA|A MESA|O PRESIDENTE)", cand, re.I):
            return cand
    b1 = blocos[1].strip(' "“”')
    if len(b1) > 15 and not re.match(r"^(ALEXANDRE|O PREFEITO|A CÂMARA|A MESA|O PRESIDENTE|CONSIDERANDO|Art\.)", b1, re.I):
        return b1
    return ""


def processar_pdf_domf(rede: Rede, url_pdf: str, edicao_num: str = "", data_pub: str = "") -> int:
    url_norm = url_pdf.replace("http://", "https://").replace(
        "://www.franca.sp.gov.br/arquivos/", "://webpmf.franca.sp.gov.br/arquivos/"
    )
    pasta_cache = RAIZ / "municipais/_fonte/SP" / SLUG_MUNICIPIO
    pasta_cache.mkdir(parents=True, exist_ok=True)
    nome_arq = url_norm.rsplit("/", 1)[-1]
    caminho_cache = pasta_cache / nome_arq

    if not caminho_cache.exists():
        st, bruto, _ = rede.get(url_norm, tentativas=3, timeout=90)
        if st != 200 or not bruto.startswith(b"%PDF"):
            print(f"[aviso] falha ao baixar {url_norm}: HTTP {st}", flush=True)
            return 0
        caminho_cache.write_bytes(bruto)

    bruto = caminho_cache.read_bytes()
    with tempfile.TemporaryDirectory() as tmp:
        pdf_tmp = Path(tmp) / "domf.pdf"
        pdf_tmp.write_bytes(bruto)
        r = subprocess.run(["pdftotext", "-q", "-enc", "UTF-8", str(pdf_tmp), "-"], capture_output=True, check=True)
        texto_bruto = r.stdout.decode("utf-8", errors="replace")

    if not edicao_num or not data_pub:
        m_cab = re.search(
            r"(\d{1,2})\s+de\s+([a-zç]+)\s+de\s+(\d{4})\s*-\s*ano\s+\d+\s*-\s*n[º°]\s*([\d.]+)",
            texto_bruto,
            re.I,
        )
        if m_cab:
            if not data_pub:
                data_pub = data_iso(m_cab.group(1), m_cab.group(2), m_cab.group(3)) or ""
            if not edicao_num:
                edicao_num = m_cab.group(4).replace(".", "")

    texto_limpo = limpar_texto_domf(texto_bruto)
    matches = list(RX_ATO_OU_SECAO.finditer(texto_limpo))
    salvos = 0
    sha_fonte = hashlib.sha256(bruto).hexdigest()

    for i, m in enumerate(matches):
        cab_ato = m.group(1)
        if not cab_ato:
            continue
        inicio = m.start()
        fim = matches[i + 1].start() if i + 1 < len(matches) else len(texto_limpo)
        recorte = texto_limpo[inicio:fim].strip()

        m_ep = RX_EPIGRAFE.match(cab_ato.strip())
        if not m_ep:
            continue
        tipo_bruto, num_fmt, dia, mes, ano = m_ep.groups()
        num_limpo = re.sub(r"\D", "", num_fmt)
        dt_iso = data_iso(dia, mes, ano)
        if not dt_iso:
            continue

        corpo_md = texto_pdf_para_md(recorte).strip()
        if len(corpo_md) < 80 or not re.search(r"\bArt\.?\s*1", corpo_md, re.I):
            continue

        ementa = extrair_ementa_do_corpo(corpo_md)
        categoria, tipo_canonico, prefixo_slug = categoria_e_tipo(tipo_bruto, ementa)
        slug = f"{prefixo_slug}-{num_limpo}-{ano}"
        destino = RAIZ / "municipais" / UF / SLUG_MUNICIPIO / categoria / ano / f"{slug}.md"

        titulo = f"{tipo_canonico} nº {num_fmt}, de {int(dia)} de {mes.lower()} de {ano}"
        sha_texto = hashlib.sha256(corpo_md.encode("utf-8")).hexdigest()
        versao = (
            f"publicação oficial no Diário Oficial do Município de Franca (DOMF nº {edicao_num})"
            if edicao_num
            else "publicação oficial no Diário Oficial do Município de Franca"
        )

        linhas = [
            "---",
            f"titulo: {yaml_str(titulo)}",
            f"municipio: {yaml_str(MUNICIPIO)}",
            f"uf: {yaml_str(UF)}",
            f"codigo_ibge: {yaml_str(CODIGO_IBGE)}",
            f"tipo: {yaml_str(tipo_canonico)}",
            f"numero: {yaml_str(num_limpo)}",
            f"data: {dt_iso}",
        ]
        if ementa:
            linhas.append(f"ementa: {yaml_str(ementa)}")
        linhas += [
            f"situacao: {yaml_str('Em vigor')}",
            "revogada: false",
            f"versao_texto: {yaml_str(versao)}",
        ]
        if edicao_num and data_pub:
            p = data_pub.split("-")
            linhas.append(f"publicacao: {yaml_str(f'DOMF nº {edicao_num} de {p[2]}/{p[1]}/{p[0]}')}")
            linhas.append(f"data_publicacao: {data_pub}")
        linhas += [
            f"fonte: {yaml_str(f'{url_norm}#{slug}')}",
            f"arquivo: {yaml_str(url_norm)}",
            f"sha256_fonte: {yaml_str(sha_fonte)}",
            f"sha256_texto: {yaml_str(sha_texto)}",
            f"baixado_em: {dt.date.today().isoformat()}",
            "---",
            "",
            f"# {titulo}",
            "",
            corpo_md,
            "",
        ]
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text("\n".join(linhas), encoding="utf-8")
        salvos += 1
        print(f"  [salvo] {destino.relative_to(RAIZ)}", flush=True)
    return salvos


def descobrir_urls_camara(rede: Rede) -> list[str]:
    urls = []
    for tipo_id in (36, 35, 37, 38, 39):
        url_csv = (
            "https://www.franca.sp.leg.br/Siscam/Documentos?Pesquisa=Avancada&ShowSearch=False"
            f"&GrupoId=3&Numeracao=Documento&Ordenacao=3&ItemsPerPage=100&NoTexto=false&TipoId={tipo_id}&Export=Csv"
        )
        st, bruto, _ = rede.get(url_csv, tentativas=3, timeout=60)
        if st != 200:
            continue
        texto = bruto.decode("utf-8-sig", errors="replace")
        for row in csv.DictReader(io.StringIO(texto)):
            obs = row.get("Observacoes") or ""
            m_url = re.search(
                r"https?://(?:webpmf|www)\.franca\.sp\.gov\.br/arquivos/diario-oficial/documentos/[^\s\"<>]+\.pdf",
                obs,
            )
            if m_url:
                u = m_url.group(0).rstrip("-")
                if u not in urls:
                    urls.append(u)
                continue
            m_dt1 = re.search(r"(?i)(?:DOMF|Di[áa]rio Oficial)[^\d]{1,25}(\d{1,2})[./](\d{1,2})[./](\d{4})", obs)
            if m_dt1:
                q_date = f"{int(m_dt1.group(1)):02d}-{int(m_dt1.group(2)):02d}-{int(m_dt1.group(3)):04d}"
                marcador = f"DATE:{q_date}"
                if marcador not in urls:
                    urls.append(marcador)
                continue
            m_dt2 = re.search(
                r"(?i)(?:DOMF|Di[áa]rio Oficial)\s+(?:no dia|em)\s+(\d{1,2})\s+de\s+([a-zç]+)\s+de\s+(\d{4})",
                obs,
            )
            if m_dt2:
                iso_d = data_iso(m_dt2.group(1), m_dt2.group(2), m_dt2.group(3))
                if iso_d:
                    p = iso_d.split("-")
                    marcador = f"DATE:{p[2]}-{p[1]}-{p[0]}"
                    if marcador not in urls:
                        urls.append(marcador)
    return urls


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ultimas", type=int, default=5, help="Baixa as últimas N edições do Diário Oficial de Franca")
    ap.add_argument("--termo", default="", help="Busca edições no índice do DOMF por termo (ex.: Complementar)")
    ap.add_argument("--de", default="", help="Data inicial ISO (YYYY-MM-DD) para varrer edições do DOMF")
    ap.add_argument("--ate", default="", help="Data final ISO (YYYY-MM-DD) para varrer edições do DOMF")
    ap.add_argument("--camara", action="store_true", help="Cruza com os índices CSV da Câmara Municipal (Siscam)")
    ap.add_argument("--max-edicoes", type=int, default=10, help="Limite de edições por modalidade de busca")
    args = ap.parse_args()

    rede = Rede(rps=1)

    if args.camara:
        urls_cam = descobrir_urls_camara(rede)
        print(f"[câmara] {len(urls_cam)} referências de edições do DOMF no Siscam", flush=True)
        for ref in urls_cam[: args.max_edicoes]:
            if ref.startswith("DATE:"):
                q_date = ref[5:]
                st_d, bruto_d, _ = rede.get(
                    f"https://webpmf.franca.sp.gov.br/pmf-diario/rest/diario/buscaPorArquivo/{q_date}"
                )
                if st_d == 200 and bruto_d:
                    p = q_date.split("-")
                    dt_iso_val = f"{p[2]}-{p[1]}-{p[0]}"
                    for arq in json.loads(bruto_d.decode("utf-8", errors="replace")):
                        u = f"https://webpmf.franca.sp.gov.br/arquivos/diario-oficial/documentos/{arq['nome']}"
                        processar_pdf_domf(rede, u, str(arq.get("nomeExibicao") or ""), dt_iso_val)
            else:
                processar_pdf_domf(rede, ref)

    if args.termo:
        termo_q = urllib.parse.quote(args.termo)
        st, bruto, _ = rede.get(
            f"https://webpmf.franca.sp.gov.br/pmf-diario/rest/diario/buscarIndice/{termo_q}/exata"
        )
        if st == 200 and bruto:
            itens = json.loads(bruto.decode("utf-8", errors="replace"))
            for arq in itens[: args.max_edicoes]:
                u = f"https://webpmf.franca.sp.gov.br/arquivos/diario-oficial/documentos/{arq['nome']}"
                processar_pdf_domf(rede, u, str(arq.get("nomeExibicao") or ""))

    if args.ultimas > 0 or (args.de and args.ate):
        st, bruto, _ = rede.get("https://webpmf.franca.sp.gov.br/pmf-diario/rest/diario/init")
        if st == 200 and bruto:
            dias = json.loads(bruto.decode("utf-8", errors="replace"))
            datas = []
            for d_str in dias:
                partes = d_str.split("-")
                if len(partes) == 3:
                    m, d, y = int(partes[0]), int(partes[1]), int(partes[2])
                    datas.append((f"{y:04d}-{m:02d}-{d:02d}", f"{d:02d}-{m:02d}-{y:04d}"))
            datas.sort()
            if args.de and args.ate:
                selecionadas = [x for x in datas if args.de <= x[0] <= args.ate]
            else:
                selecionadas = datas[-args.ultimas :]
            for dt_iso_val, query_val in selecionadas:
                st_d, bruto_d, _ = rede.get(
                    f"https://webpmf.franca.sp.gov.br/pmf-diario/rest/diario/buscaPorArquivo/{query_val}"
                )
                if st_d == 200 and bruto_d:
                    for arq in json.loads(bruto_d.decode("utf-8", errors="replace")):
                        u = f"https://webpmf.franca.sp.gov.br/arquivos/diario-oficial/documentos/{arq['nome']}"
                        processar_pdf_domf(rede, u, str(arq.get("nomeExibicao") or ""), dt_iso_val)


if __name__ == "__main__":
    main()
