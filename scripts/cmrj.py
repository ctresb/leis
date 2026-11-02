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
ATO_EPIGRAFE = r"(?:lei\s+complementar|emenda\s+[àa]\s+lei\s+org[âa]nica|lei)"
NUM_EPIGRAFE = r"\d+(?:\.\d{3})*"
EPIGRAFE_DATA = re.compile(
    rf"{ATO_EPIGRAFE}\s+n[º°o]\.?\s*{NUM_EPIGRAFE}(?:\\?\*)?,\s*de\s+"
    r"(\d{1,2})(?:[º°o.])?\s+de\s+(\w+)\s+de\s+(\d{4})", re.I)
HEADER_DATA = re.compile(
    r"Data da (?:Lei|promulga[cç][aã]o)\s+(\d{1,2})/(\d{1,2})/(\d{4})", re.I)
FORMA_VIGENCIA = re.compile(
    r"Forma de Vig[eê]ncia\s+(Sancionada(?:/Promulgada)?|Promulgada)\b", re.I)
SERIES = {
    "emenda": {
        "pasta": "emendas-lei-organica",
        "cache": "emendas",
        "tipo": "Emenda à Lei Orgânica",
        "tipo_na_fonte": "Emenda à Lei Orgânica",
        "skip_numeros": frozenset(),
        "so_promulgadas": False,
    },
    "leicomp": {
        "pasta": "leis-complementares",
        "cache": "leis-complementares",
        "tipo": "Lei Complementar",
        "tipo_na_fonte": "Lei Complementar",
        "skip_numeros": frozenset({"197", "198", "270"}),
        "so_promulgadas": True,
    },
    "leiord": {
        "pasta": "leis-ordinarias",
        "cache": "leis-ordinarias",
        "tipo": "Lei Ordinária",
        "tipo_na_fonte": "Lei",
        "skip_numeros": frozenset(),
        "so_promulgadas": True,
    },
}


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
    md = re.sub(r"^(?:\*\*)?Texto da Lei(?:\*\*)?\s*", "", md)
    if len(re.sub(r"\W", "", md)) < 80:
        raise ValueError("texto integral vazio após conversão")
    return md.strip() + "\n", html


def grafia_numero(numero):
    """Dígitos do XML com pontos milhares opcionais (9.682 ↔ 9682)."""
    digitos = re.sub(r"\D", "", str(numero or ""))
    if not digitos:
        return NUM_EPIGRAFE
    return r"[.\s]*".join(digitos)


def epigrafe_data(numero=None):
    n = grafia_numero(numero) if numero else NUM_EPIGRAFE
    return re.compile(
        rf"{ATO_EPIGRAFE}\s+n[º°o]\.?\s*{n}(?:\\?\*)?,?\s*de\s+"
        r"(\d{1,2})(?:[º°o.])?\s+de\s+(\w+)\s+de\s+(\d{4})", re.I)


def data_do_documento(html, corpo="", numero=""):
    """Data legal: epígrafe do próprio número; senão campo Lotus (MM/DD/AAAA)."""
    for pat in (epigrafe_data(numero) if numero else None, EPIGRAFE_DATA):
        if pat is None:
            continue
        m = pat.search(corpo or "")
        if m and normalizar_chave(m.group(2)) in MESES:
            return f"{m.group(3)}-{MESES[normalizar_chave(m.group(2))]:02d}-{int(m.group(1)):02d}"
    plano = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html or ""))
    m = HEADER_DATA.search(plano)
    if not m:
        return ""
    mes, dia, ano = int(m.group(1)), int(m.group(2)), int(m.group(3))
    dt.date(ano, mes, dia)  # valida MM/DD
    return f"{ano}-{mes:02d}-{dia:02d}"


def cache_html(serie, unid, ano_hint):
    pasta = RAIZ / "municipais/_fonte/cmrj" / serie["cache"]
    unid = unid.lower()
    hits = sorted(pasta.rglob(unid + ".html.gz"))
    if hits:
        return hits[0]
    return pasta / (ano_hint or "sem-ano") / (unid + ".html.gz")


def forma_vigencia(html):
    """Campo Lotus 'Forma de Vigência' (Promulgada / Sancionada / Sancionada/Promulgada)."""
    plano = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html or ""))
    m = FORMA_VIGENCIA.search(plano)
    return m.group(1).strip() if m else ""


def e_promulgada(forma, html=""):
    """Ato já convertido em lei (sancionado e/ou promulgado); exclui projeto/minuta."""
    if re.search(r"promulgad|sancionad", normalizar_chave(forma)):
        return True
    plano = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html or ""))
    return bool(re.search(r"promulg[ao]\s+a\s+lei|sanciono\s+a\s+seguinte", plano, re.I))


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


def numero_ato(item):
    return re.sub(r"\D", "", item.get("numero") or "") or (item.get("numero") or "")


def titulo_ato(tipo, numero, data, ementa=""):
    if data:
        d = dt.date.fromisoformat(data)
        meses = {v: k for k, v in MESES.items() if k != "marco"}
        meses[3] = "março"
        data_ext = f"{d.day} de {meses[d.month]} de {d.year}"
        return f"{tipo} nº {numero}, de {data_ext}"
    return f"{tipo} nº {numero}" + (f" — {ementa}" if ementa else "")


def titulo_emenda(numero, data, ementa):
    return titulo_ato("Emenda à Lei Orgânica", numero, data, ementa)


def fontes_municipio():
    """URLs e UNIDs já versionados em qualquer série do Rio (LO, emendas, planos, códigos)."""
    vistos = set()
    raiz = RAIZ / "municipais" / UF / "rio-de-janeiro"
    if not raiz.exists():
        return vistos
    for p in raiz.rglob("*.md"):
        if any(part.startswith("_") for part in p.parts):
            continue
        cab = p.read_text(encoding="utf-8", errors="replace").split("\n---\n", 1)[0]
        for chave in ("fonte", "fonte_texto"):
            m = re.search(rf"^{chave}:\s*(.*)$", cab, re.M)
            if not m:
                continue
            val = m.group(1).strip().strip('"')
            if not val:
                continue
            vistos.add(val)
            um = re.search(r"/0/([0-9A-Fa-f]+)\?", val)
            if um:
                vistos.add(um.group(1).upper())
    return vistos


def ja_existe_unid(pasta, unid):
    raiz = RAIZ / "municipais" / UF / "rio-de-janeiro" / pasta
    if not raiz.exists():
        return False
    marca = unid[:12].lower()
    return any(marca in p.name.lower() for p in raiz.rglob("*.md"))


def gravar_ato(serie, item, bruto, ctype, view):
    unid = item["unid"]
    numero = numero_ato(item)
    corpo, html = corpo_documento(bruto, ctype)
    if not re.search(r"art(?:igo)?\.?\s*1(?:[º°o]|\b)", corpo, re.I) and not (
            len(corpo) > 500 and re.search(r"\bpromulg", corpo, re.I)):
        raise ValueError("texto sem artigo inicial reconhecível")
    data = data_do_documento(html, corpo, numero)
    ano = (data[:4] if data else item["ano"]) or "sem-ano"
    slug = f"{serie['pasta']}-{normalizar_chave(numero)}-{ano}-cmrj-{unid[:12].lower()}"
    destino = (RAIZ / "municipais" / UF / "rio-de-janeiro" / serie["pasta"] / ano / (slug + ".md"))
    fonte = cache_html(serie, unid, ano)
    if destino.exists():
        return "pulado", destino
    titulo = titulo_ato(serie["tipo"], numero, data, item["ementa"])
    meta = {
        "titulo": titulo,
        "tipo": serie["tipo"],
        "tipo_na_fonte": serie["tipo_na_fonte"],
        "numero": numero,
        "data": data,
        "municipio": MUNICIPIO,
        "uf": UF,
        "codigo_ibge": IBGE,
        "situacao": item["situacao"],
        "ementa": item["ementa"],
        "versao_texto": ("texto integral HTML da base de legislação da Câmara Municipal do Rio de Janeiro "
                         f"(Domino/contlei.nsf, view {view}); a própria fonte declara que o texto não substitui "
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


def gravar_emenda(item, bruto, ctype):
    return gravar_ato(SERIES["emenda"], item, bruto, ctype, "emenda")


def ano_item(item):
    try:
        return int(item.get("ano") or 0)
    except (TypeError, ValueError):
        return 0


def filtrar_anos(itens, ano_min=0, ano_max=0):
    if not ano_min and not ano_max:
        return list(itens)
    out = []
    for it in itens:
        a = ano_item(it)
        if ano_min and a < ano_min:
            continue
        if ano_max and a > ano_max:
            continue
        out.append(it)
    return out


def histograma_anos(itens):
    from collections import Counter
    return dict(sorted(Counter(str(i.get("ano") or "") for i in itens).items()))


def selecionar_itens(itens, serie, view, fontes, limite):
    escolhidos, pulados = [], []
    for it in itens:
        numero = numero_ato(it)
        unid = (it.get("unid") or "").upper()
        url = url_documento(it["unid"]) if it.get("unid") else ""
        if numero in serie["skip_numeros"]:
            pulados.append(("reservado", numero, it.get("unid")))
            continue
        if url in fontes or unid in fontes:
            pulados.append(("fonte-existente", numero, it.get("unid")))
            continue
        if ja_existe_unid(serie["pasta"], it["unid"]):
            pulados.append(("md-existente", numero, it.get("unid")))
            continue
        escolhidos.append(it)
        if limite and len(escolhidos) >= limite:
            break
    resto = max(0, len(itens) - len(pulados) - len(escolhidos))
    print(f"[cmrj] view {view}: {len(itens)} atos, {len(escolhidos)} a gravar, "
          f"{len(pulados)} pulados, {resto} fora do limite", flush=True)
    return escolhidos, pulados, resto


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rps", type=float, default=3)
    ap.add_argument("--view", default="emenda", choices=sorted(SERIES))
    ap.add_argument("--limite", type=int, default=0, help="máximo de novos .md neste lote (0 = teto da série)")
    ap.add_argument("--max-md", type=int, default=500, help="teto mole de novos .md")
    ap.add_argument("--ano-min", type=int, default=0)
    ap.add_argument("--ano-max", type=int, default=0)
    args = ap.parse_args()
    serie = SERIES[args.view]
    limite = args.limite or args.max_md
    ibge_path, _ = identidade_rio()
    rede = Rede(rps=args.rps)
    itens = ler_view(rede, args.view)
    pasta = RAIZ / "municipais/_fonte/cmrj"
    anos_indice = histograma_anos(itens)
    escrever(pasta / f"{args.view}-indice.json", json.dumps({
        "fonte": f"{BASE}/{args.view}?ReadViewEntries",
        "view": args.view,
        "consultado_em": dt.datetime.now().isoformat(),
        "ibge_sha256": hashlib.sha256(ibge_path.read_bytes()).hexdigest(),
        "total": len(itens),
        "anos": anos_indice,
        "itens": itens,
    }, ensure_ascii=False, indent=2))
    janela = filtrar_anos(itens, args.ano_min, args.ano_max)
    if args.ano_min or args.ano_max:
        print(f"[cmrj] janela {args.ano_min or '…'}-{args.ano_max or '…'}: "
              f"{len(janela)}/{len(itens)} atos", flush=True)
    fontes = fontes_municipio()
    escolhidos, pulados, resto = selecionar_itens(janela, serie, args.view, fontes, limite)
    print(f"[cmrj] view {args.view}: {len(itens)} atos", flush=True)
    cont = {"ok": 0, "pulado": 0, "erro": 0, "nao-promulgada": 0}
    falhas = pasta / "falhas.jsonl"
    for it in escolhidos:
        url = url_documento(it["unid"])
        cache = cache_html(serie, it["unid"], it.get("ano") or "sem-ano")
        try:
            if cache.exists():
                bruto = gzip.decompress(cache.read_bytes())
                ctype = "text/html; charset=UTF-8"
            else:
                st, bruto, ctype = rede.get(url, timeout=180)
                if st != 200 or not bruto:
                    raise RuntimeError(f"HTTP {st}")
            html = decodificar(bruto, ctype)
            if serie["so_promulgadas"]:
                forma = forma_vigencia(html)
                if not e_promulgada(forma, html):
                    cont["nao-promulgada"] += 1
                    print("nao-promulgada", it["numero"], forma or "(vazio)", flush=True)
                    continue
            status, destino = gravar_ato(serie, it, bruto, ctype, args.view)
            cont[status] += 1
            print(status, it["numero"], destino, flush=True)
        except Exception as e:
            cont["erro"] += 1
            with falhas.open("a", encoding="utf-8") as f:
                f.write(json.dumps({"unid": it["unid"], "numero": it["numero"], "view": args.view,
                                    "erro": str(e), "quando": dt.datetime.now().isoformat()},
                                   ensure_ascii=False) + "\n")
            print("erro", it["numero"], e, flush=True)
    escrever(pasta / f"{args.view}-lote.json", json.dumps({
        "view": args.view,
        "consultado_em": dt.datetime.now().isoformat(),
        "indice": len(itens),
        "anos_indice": anos_indice,
        "janela": {"ano_min": args.ano_min, "ano_max": args.ano_max, "atos": len(janela)},
        "pulados": [{"motivo": m, "numero": n, "unid": u} for m, n, u in pulados],
        "resto_fora_do_limite": resto,
        "contagens": cont,
    }, ensure_ascii=False, indent=2))
    print(f"[cmrj] FIM {cont} resto={resto}", flush=True)
    if cont["erro"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
