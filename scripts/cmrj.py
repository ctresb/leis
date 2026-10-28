"""Câmara Municipal do Rio de Janeiro — base Domino `contlei.nsf`.

Índice: views Lotus via ?ReadViewEntries (XML), paginadas com Count≤1000.
Texto: documento ?OpenDocument (HTML integral da seção "Texto da …").
"""
import argparse
import datetime as dt
import gzip
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urljoin

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import Rede, decodificar, html_para_md, normalizar_chave, yaml_str

RAIZ = Path(__file__).resolve().parent.parent
BASE = "https://aplicnt.camara.rj.gov.br/APL/Legislativos/contlei.nsf"
IBGE = "3304557"
MUNICIPIO = "Rio de Janeiro"
UF = "RJ"
MESES = {m: i for i, m in enumerate(
    "janeiro fevereiro marco abril maio junho julho agosto setembro outubro novembro dezembro".split(), 1)}
MESES["março"] = 3
EPIGRAFE_DATA = re.compile(
    r"(?:lei\s+complementar|emenda\s+[àa]\s+lei\s+org[âa]nica)\s+"
    r"n[º°o]\.?\s*\d+(?:\\?\*)?,\s*de\s+(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})", re.I)
HEADER_DATA = re.compile(
    r"Data da (?:Lei|promulga[cç][aã]o)\s+(\d{1,2})/(\d{1,2})/(\d{4})", re.I)


def escrever(path, dados):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    if isinstance(dados, str):
        tmp.write_text(dados, encoding="utf-8")
    else:
        tmp.write_bytes(dados)
    tmp.replace(path)


def identidade_rio():
    ibge_path = RAIZ / "municipais/_indice/ibge-municipios.json"
    municipios = json.loads(ibge_path.read_text())
    item = next(x for x in municipios if str(x["id"]) == IBGE)
    uf = item["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]
    if item["nome"] != MUNICIPIO or uf != UF:
        raise ValueError("identidade IBGE diverge do município do Rio de Janeiro")
    return ibge_path, item


def ler_view(rede, view, count=1000):
    """Lê todas as entradas de uma view Domino, paginando pelo position."""
    if not 1 <= count <= 1000:
        raise ValueError("Count Lotus deve estar entre 1 e 1000")
    itens, vistos, inicio = [], set(), "1"
    total = None
    while True:
        url = f"{BASE}/{view}?ReadViewEntries&Start={inicio}&Count={count}"
        st, dados, _ = rede.get(url, "text/xml", timeout=180)
        if st != 200:
            raise RuntimeError(f"view {view}: HTTP {st}")
        total, pagina = entradas_xml(dados)
        novas = [e for e in pagina if e["unid"] not in vistos]
        for e in novas:
            vistos.add(e["unid"])
            itens.append(e)
        if not novas or len(pagina) < count:
            break
        inicio = str(int(float(pagina[-1]["position"])) + 1)
    if total is not None and len(itens) != total:
        raise RuntimeError(f"view {view}: índice {len(itens)} diverge de toplevelentries={total}")
    return itens


def entradas_xml(dados):
    raiz = ET.fromstring(dados)
    total = int(raiz.get("toplevelentries") or 0)
    itens = []
    for e in raiz.findall("viewentry"):
        if not e.get("unid"):
            continue
        campos = {}
        for d in e.findall("entrydata"):
            textos = [t.text or "" for t in d.findall(".//text")]
            nums = [n.text or "" for n in d.findall(".//number")]
            campos[d.get("name")] = " | ".join(x for x in textos + nums if x)
        itens.append({
            "unid": e.get("unid"),
            "position": e.get("position"),
            "numero": campos.get("$8", "").strip(),
            "ano": campos.get("ComplL", "").strip(),
            "situacao": campos.get("Status", "").strip(),
            "ementa": campos.get("$9", "").strip(),
            "autoria": campos.get("$2", "").strip(),
            "campos": campos,
        })
    return total, itens


def url_documento(unid):
    return f"{BASE}/0/{unid}?OpenDocument"


def limpar_chrome(html):
    html = re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.I | re.S)
    html = re.sub(r"<object\b[^>]*>.*?</object>", "", html, flags=re.I | re.S)
    html = re.sub(r"<img\b[^>]*>", "", html, flags=re.I)
    return html


def extrair_texto_html(html):
    m = re.search(r'<div id="xSec2"[^>]*>(.*?)</div>\s*<script', html, re.I | re.S)
    if m:
        return m.group(1)
    ini = re.search(r'<a\s+name\s*=\s*["\']TOPO["\']', html, re.I)
    fim = re.search(r"Atalho para outros documentos", html, re.I)
    if ini and fim and fim.start() > ini.start():
        return html[ini.start():fim.start()]
    raise ValueError("texto integral não localizado no HTML Domino")


def corpo_documento(bruto, content_type=""):
    html = decodificar(bruto, content_type)
    trecho = limpar_chrome(extrair_texto_html(html))
    md = html_para_md(trecho).strip()
    md = re.sub(r"^(?:\*\*)?Texto da Emenda(?:\*\*)?\s*", "", md)
    md = re.sub(r"^(?:\*\*)?Texto Lei Complementar(?:\*\*)?\s*", "", md)
    if len(re.sub(r"\W", "", md)) < 80:
        raise ValueError("texto integral vazio após conversão")
    return md.strip() + "\n", html


def data_do_documento(html, corpo=""):
    """Data legal: epígrafe por extenso; senão campo Lotus (MM/DD/AAAA)."""
    m = EPIGRAFE_DATA.search(corpo or "")
    if m and normalizar_chave(m.group(2)) in MESES:
        return f"{m.group(3)}-{MESES[normalizar_chave(m.group(2))]:02d}-{int(m.group(1)):02d}"
    plano = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html or ""))
    m = HEADER_DATA.search(plano)
    if not m:
        return ""
    mes, dia, ano = int(m.group(1)), int(m.group(2)), int(m.group(3))
    dt.date(ano, mes, dia)  # valida MM/DD
    return f"{ano}-{mes:02d}-{dia:02d}"


def anexos_pdf(html, unid):
    """PDFs anexos do próprio documento Domino (não conta como norma nova)."""
    encontrados, vistos = [], set()
    for href in re.findall(r'href="([^"]+)"', html, re.I):
        if "$FILE/" not in href.upper() or unid.lower() not in href.lower():
            continue
        if not re.search(r"\.pdf(?:$|\?)", href, re.I):
            continue
        if href in vistos:
            continue
        vistos.add(href)
        nome = unquote(href.split("$FILE/")[-1])
        encontrados.append((urljoin(BASE + "/", href), nome))
    return encontrados


def titulo_emenda(numero, data, ementa):
    if data:
        d = dt.date.fromisoformat(data)
        meses = {v: k for k, v in MESES.items() if k != "marco"}
        meses[3] = "março"
        data_ext = f"{d.day} de {meses[d.month]} de {d.year}"
        return f"Emenda à Lei Orgânica nº {numero}, de {data_ext}"
    return f"Emenda à Lei Orgânica nº {numero}" + (f" — {ementa}" if ementa else "")


def gravar_emenda(item, bruto, ctype):
    unid = item["unid"]
    numero = re.sub(r"\D", "", item["numero"]) or item["numero"]
    corpo, html = corpo_documento(bruto, ctype)
    if not re.search(r"art(?:igo)?\.?\s*1(?:[º°o]|\b)", corpo, re.I) and not (
            len(corpo) > 500 and re.search(r"\bpromulg", corpo, re.I)):
        raise ValueError("texto sem artigo inicial reconhecível")
    data = data_do_documento(html, corpo)
    ano = (data[:4] if data else item["ano"]) or "sem-ano"
    slug = f"emendas-lei-organica-{normalizar_chave(numero)}-{ano}-cmrj-{unid[:12].lower()}"
    destino = (RAIZ / "municipais" / UF / "rio-de-janeiro" / "emendas-lei-organica" / ano / (slug + ".md"))
    fonte = RAIZ / "municipais/_fonte/cmrj/emendas" / ano / (unid.lower() + ".html.gz")
    if destino.exists():
        return "pulado", destino
    titulo = titulo_emenda(numero, data, item["ementa"])
    meta = {
        "titulo": titulo,
        "tipo": "Emenda à Lei Orgânica",
        "tipo_na_fonte": "Emenda à Lei Orgânica",
        "numero": numero,
        "data": data,
        "municipio": MUNICIPIO,
        "uf": UF,
        "codigo_ibge": IBGE,
        "situacao": item["situacao"],
        "ementa": item["ementa"],
        "versao_texto": ("texto integral HTML da base de legislação da Câmara Municipal do Rio de Janeiro "
                         "(Domino/contlei.nsf, view emenda); a própria fonte declara que o texto não substitui "
                         "o publicado no Diário Oficial"),
        "fonte": url_documento(unid),
        "fonte_texto": url_documento(unid),
        "sha256_fonte": hashlib.sha256(bruto).hexdigest(),
        "sha256_texto": hashlib.sha256(corpo.encode()).hexdigest(),
        "baixado_em": dt.date.today().isoformat(),
        "revogada": None,
    }
    cab = ["---"] + [k + ": " + ("null" if v is None else yaml_str(v)) for k, v in meta.items()]
    cab += ["---", "", "# " + titulo, "", corpo.rstrip("\n"), ""]
    escrever(destino, "\n".join(cab) + "\n")
    escrever(fonte, gzip.compress(bruto))
    return "ok", destino


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rps", type=float, default=3)
    ap.add_argument("--view", default="emenda")
    args = ap.parse_args()
    ibge_path, _ = identidade_rio()
    rede = Rede(rps=args.rps)
    itens = ler_view(rede, args.view)
    pasta = RAIZ / "municipais/_fonte/cmrj"
    escrever(pasta / f"{args.view}-indice.json", json.dumps({
        "fonte": f"{BASE}/{args.view}?ReadViewEntries",
        "view": args.view,
        "consultado_em": dt.datetime.now().isoformat(),
        "ibge_sha256": hashlib.sha256(ibge_path.read_bytes()).hexdigest(),
        "total": len(itens),
        "itens": itens,
    }, ensure_ascii=False, indent=2))
    print(f"[cmrj] view {args.view}: {len(itens)} atos", flush=True)
    cont = {"ok": 0, "pulado": 0, "erro": 0}
    falhas = pasta / "falhas.jsonl"
    for it in itens:
        url = url_documento(it["unid"])
        cache = pasta / "emendas" / (it.get("ano") or "sem-ano") / (it["unid"].lower() + ".html.gz")
        try:
            if cache.exists():
                bruto = gzip.decompress(cache.read_bytes())
                ctype = "text/html; charset=UTF-8"
            else:
                st, bruto, ctype = rede.get(url, timeout=180)
                if st != 200 or not bruto:
                    raise RuntimeError(f"HTTP {st}")
            status, destino = gravar_emenda(it, bruto, ctype)
            cont[status] += 1
            print(status, it["numero"], destino, flush=True)
        except Exception as e:
            cont["erro"] += 1
            with falhas.open("a", encoding="utf-8") as f:
                f.write(json.dumps({"unid": it["unid"], "numero": it["numero"],
                                    "erro": str(e), "quando": dt.datetime.now().isoformat()},
                                   ensure_ascii=False) + "\n")
            print("erro", it["numero"], e, flush=True)
    print(f"[cmrj] FIM {cont}", flush=True)
    if cont["erro"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
