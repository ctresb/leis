"""Pernambuco — Alepe Legis (legis.alepe.pe.gov.br).

Índice: lista.aspx?tiponorma=N, um ano por vez (postback ASP.NET do seletor ddlAno).
Texto: texto.aspx?id=N&tipo=TEXTOATUALIZADO (quando existe) ou TEXTOORIGINAL; conteúdo em div#divTexto.
"""
import html as htmllib
import http.cookiejar
import datetime as dt
import gzip
import hashlib
import json
import os
import re
import sys
import tempfile
import threading
import urllib.parse
import urllib.request
from html.parser import HTMLParser

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from comum import RAIZ_ESTADUAIS, UA, Rede, caminhos, decodificar, executar, gravar, html_para_md  # noqa: E402
from pe_identidade import identidade_do_texto, numero_indice

UF = "PE"
BASE = "https://legis.alepe.pe.gov.br"
# tiponorma do Alepe Legis -> (pasta, tipo canônico, prefixo). O tipo 6 é "Decreto do Executivo",
# com acervo de 1996 a hoje, e ficava inteiro de fora. Os quatro primeiros prefixos já estão
# gravados e não mudam.
TIPOS = {
    "13": ("emendas-constitucionais", "Emenda Constitucional", "ec"),
    "2": ("leis-complementares", "Lei Complementar", "lc"),
    "1": ("leis-ordinarias", "Lei Ordinária", "lei"),
    "11": ("decretos-lei", "Decreto-Lei", "dl"),
    "6": ("decretos", "Decreto", "dec"),
    "4": ("resolucoes", "Resolução", "res"),
    "5": ("decretos-legislativos", "Decreto Legislativo", "dl"),
    "8": ("portarias", "Portaria", "port"),
}
rede = Rede(rps=1)
LINHA = re.compile(
    r"nome-norma\"><a href='texto\.aspx\?id=(\d+)[^>]*>([^<]+)</a></span>\s*<span class=\"publicacao\">([^<]*)</span>(.*?)</tr>",
    re.S,
)


def listar_ano(op, tipo, ano, campos):
    dados = dict(campos, __EVENTTARGET="ctl00$conteudo$ddlAno", __EVENTARGUMENT="")
    dados["ctl00$conteudo$ddlAno"] = ano
    url = f"{BASE}/lista.aspx?tiponorma={tipo}"
    rede.limite.esperar()
    req = urllib.request.Request(
        url, data=urllib.parse.urlencode(dados).encode(), headers={"User-Agent": UA, "Content-Type": "application/x-www-form-urlencoded"}
    )
    return op.open(req, timeout=180).read().decode("utf-8", "replace")


def campos_ocultos(html):
    return {n: htmllib.unescape(v) for n, v in re.findall(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"', html)}


def linhas(html, tipo):
    for id_, nome, pub, resto in LINHA.findall(html):
        textos = re.findall(r"tipo=(TEXTO[A-Z]+)", resto)
        ementa = re.search(r'class="ementa-norma[^"]*">\s*<div class="fLeft">(.*?)</div>', resto, re.S)
        yield {
            "id": id_,
            "tipo": tipo,
            "nome": " ".join(htmllib.unescape(nome).split()),
            "publicacao": " ".join(htmllib.unescape(pub).split()),
            "textos": sorted(set(textos)),
            "ementa": " ".join(htmllib.unescape(re.sub(r"<[^>]+>", " ", ementa.group(1))).split()) if ementa else "",
        }


def indice(refazer=False):
    pasta = os.path.join(RAIZ_ESTADUAIS, UF, "_indice")
    arq = os.path.join(pasta, "lista.json")
    if os.path.exists(arq) and not refazer:
        return json.load(open(arq, encoding="utf-8"))
    itens = {}
    for tipo in TIPOS:
        op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        rede.limite.esperar()
        pagina = op.open(urllib.request.Request(f"{BASE}/lista.aspx?tiponorma={tipo}", headers={"User-Agent": UA}), timeout=180)
        html = pagina.read().decode("utf-8", "replace")
        anos = re.findall(r'<option[^>]*value="(\d{4})"', html.split('id="ddlAno"', 1)[1].split("</select>", 1)[0]) if 'id="ddlAno"' in html else []
        if not anos:
            for it in linhas(html, tipo):
                itens[it["id"]] = it
        for ano in anos:
            h = listar_ano(op, tipo, ano, campos_ocultos(html))
            for it in linhas(h, tipo):
                it["ano"] = ano
                itens[it["id"]] = it
        print(f"[{UF}] índice tipo {tipo}: {sum(1 for i in itens.values() if i['tipo'] == tipo)}", flush=True)
    lista = list(itens.values())
    os.makedirs(pasta, exist_ok=True)
    with open(arq, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False)
    return lista


class _LimiteTexto(HTMLParser):
    def __init__(self, html, fragmento):
        super().__init__(convert_charrefs=False)
        self.inicio = 0 if fragmento else None
        self.fim = None
        self.profundidade = 1 if fragmento else 0
        self.linhas = [0] + [m.end() for m in re.finditer("\n", html)]

    def posicao(self):
        linha, coluna = self.getpos()
        return self.linhas[linha - 1] + coluna

    def handle_starttag(self, tag, attrs):
        if tag != "div" or self.fim is not None:
            return
        if self.inicio is None:
            if dict(attrs).get("id") == "divTexto":
                self.inicio = self.posicao() + len(self.get_starttag_text())
                self.profundidade = 1
        else:
            self.profundidade += 1

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag == "div" and self.inicio is not None and self.fim is None:
            self.profundidade -= 1
            if self.profundidade == 0:
                self.fim = self.posicao()


def limites_texto_html(html, fragmento=False):
    limite = _LimiteTexto(html, fragmento)
    limite.feed(html)
    if limite.inicio is None:
        return None
    if limite.fim is None:
        raise ValueError("divTexto sem fechamento comprovado; extração recusada")
    return limite.inicio, limite.fim


def texto_html(html):
    limites = limites_texto_html(html)
    return html[limites[0]:limites[1]] if limites else ""


_ID_LOCK = threading.Lock()
_ID_RAIZ = None
_ID_PATHS = {}
_KEY_PATHS = {}


def _paths_id(ident):
    global _ID_RAIZ, _ID_PATHS, _KEY_PATHS
    raiz = os.path.join(RAIZ_ESTADUAIS, UF)
    with _ID_LOCK:
        if _ID_RAIZ != raiz:
            encontrados = {}
            chaves = {}
            for base, dirs, files in os.walk(raiz):
                dirs[:] = [d for d in dirs if not d.startswith("_")]
                for arquivo in files:
                    m = re.search(r"-id(\d+)\.md$", arquivo, re.I)
                    if m:
                        path = os.path.join(base, arquivo)
                        encontrados.setdefault(m[1], []).append(path)
                        key = re.match(r"(?:ec|lc|lei|dl|dec|res|port)-([\d.A-Za-z-]+)-(\d{4})-id\d+\.md$", arquivo)
                        if key:
                            folder = os.path.relpath(base, raiz).split(os.sep)[0]
                            chaves.setdefault((folder, key[1].replace(".", "").lstrip("0").upper(), key[2]), []).append(path)
            _ID_RAIZ, _ID_PATHS, _KEY_PATHS = raiz, encontrados, chaves
        return list(_ID_PATHS.get(str(ident), []))


def _existente(it, esperado):
    paths = _paths_id(it["id"])
    if not paths:
        return None
    divergencias = []
    for path in paths:
        try:
            meta = {}
            with open(path, encoding="utf-8") as f:
                header = f.read().split("\n---\n", 1)[0]
            for line in header.splitlines():
                k, sep, v = line.partition(":")
                if sep:
                    try: meta[k] = json.loads(v.strip())
                    except ValueError: meta[k] = v.strip()
            url = urllib.parse.urlparse(meta.get("fonte", ""))
            if url.netloc != urllib.parse.urlparse(BASE).netloc or url.path != "/texto.aspx" or urllib.parse.parse_qs(url.query).get("id") != [str(it["id"])]:
                divergencias.append("fonte existente diverge do ID/portal oficial")
            modo = "TEXTOATUALIZADO" if "TEXTOATUALIZADO" in it["textos"] else "TEXTOORIGINAL"
            if urllib.parse.parse_qs(url.query).get("tipo") != [modo]:
                divergencias.append("edição disponível no índice difere da fonte existente; revisão necessária")
            if meta.get("publicacao") != it.get("publicacao"):
                divergencias.append("publicação literal do índice mudou; revisão necessária")
            normal = lambda n: re.sub(r"[.\s]", "", str(n)).upper().lstrip("0")
            if meta.get("uf") != UF or meta.get("tipo") != TIPOS[it["tipo"]][1] or normal(meta.get("numero", "")) != normal(numero_indice(it)):
                divergencias.append("tipo/UF/número existente diverge do índice")
            if it.get("ano") and str(meta.get("ano", "")) != str(it["ano"]):
                divergencias.append("ano existente difere do agrupamento do índice; requer auditoria")
            if not meta.get("data") or not meta.get("ano"):
                divergencias.append("data/ano existentes incompletos; requer auditoria")
        except (OSError, ValueError, TypeError) as e:
            divergencias.append("metadados existentes indisponíveis: " + str(e))
    if len(paths) == 1 and os.path.abspath(paths[0]) == os.path.abspath(esperado) and not divergencias:
        return "pulado", None
    return "pulado", {"id": str(it["id"]), "motivo": "ID oficial já existente; não criar alias nem refazer download", "paths": paths, "divergencias": divergencias}


def processar(it):
    pasta, nome, prefixo = TIPOS[it["tipo"]]
    num = re.search(r"n[°º]\s*([\d.]+(?:-[A-Za-z]+)?)", it["nome"])
    numero = num.group(1).replace(".", "") if num else "sn"
    ano = it.get("ano") or "sem-ano"
    slug = f"{prefixo}-{numero}-{ano}-id{it['id']}"
    md, fonte = caminhos(UF, pasta, ano, slug)
    existente = _existente(it, md)
    if existente:
        return existente
    tipo_txt = "TEXTOATUALIZADO" if "TEXTOATUALIZADO" in it["textos"] else "TEXTOORIGINAL"
    url = f"{BASE}/texto.aspx?id={it['id']}&tipo={tipo_txt}"
    st, bruto, ctype = rede.get(url, timeout=180)
    if st != 200:
        return "sem_texto", {"id": it["id"], "http": st}
    captura = os.path.join(RAIZ_ESTADUAIS, UF, "_fonte", "respostas", str(it["id"]), tipo_txt, hashlib.sha256(bruto).hexdigest() + ".html.gz")
    os.makedirs(os.path.dirname(captura), exist_ok=True)
    try:
        with gzip.open(captura, "rb") as f:
            integra = hashlib.sha256(f.read()).digest() == hashlib.sha256(bruto).digest()
    except (OSError, EOFError):
        integra = False
    if not integra:
        with tempfile.NamedTemporaryFile(dir=os.path.dirname(captura), delete=False) as f:
            temporario = f.name
            f.write(gzip.compress(bruto))
        os.replace(temporario, captura)
    html = decodificar(bruto, ctype)
    trecho = texto_html(html)
    if not trecho:
        return "sem_texto", {"id": it["id"], "motivo": "sem divTexto"}
    corpo = html_para_md(trecho)
    if len(re.sub(r"\W", "", corpo)) < 40:
        return "sem_texto", {"id": it["id"], "motivo": "texto vazio"}
    data = re.search(r"(\d{2})/(\d{2})/(\d{4})", it["publicacao"])
    data_publicacao = ""
    if data:
        try:
            publicada = dt.date(int(data[3]), int(data[2]), int(data[1]))
            if publicada <= dt.date.today():
                data_publicacao = publicada.isoformat()
        except ValueError:
            pass
    titulo = it["nome"]
    try:
        _, data_norma, epigrafe = identidade_do_texto(it, corpo)
    except (ValueError, KeyError) as e:
        return "sem_texto", {"id": it["id"], "motivo": str(e), "captura": captura}
    ano_indice = it.get("ano")
    ano = data_norma[:4]
    slug = f"{prefixo}-{numero}-{ano}-id{it['id']}"
    md, fonte = caminhos(UF, pasta, ano, slug)
    if os.path.exists(md):
        return "pulado", {"id": it["id"], "motivo": "destino da epígrafe já existe; não sobrescrever", "path": md}
    chave = (pasta, numero.lstrip("0").upper(), ano)
    with _ID_LOCK:
        colisoes = list(_KEY_PATHS.get(chave, []))
    if colisoes:
        return "sem_texto", {"id": it["id"], "motivo": "tipo/número/ano já existente com ID diferente; reconciliação necessária", "paths": colisoes, "captura": captura}
    meta = [
        ("titulo", titulo),
        ("uf", UF),
        ("tipo", nome),
        ("numero", num.group(1) if num else ""),
        ("data", data_norma),
        ("ano", ano),
        ("ementa", it["ementa"]),
        ("publicacao", it["publicacao"]),
        ("data_publicacao", data_publicacao),
        ("revogada", None),
        ("versao_texto", "atualizada" if tipo_txt == "TEXTOATUALIZADO" else "original"),
        ("fonte", url),
    ]
    if ano_indice and str(ano_indice) != ano:
        meta.append(("ano_indice", str(ano_indice)))
    if data and not data_publicacao:
        meta.append(("data_publicacao_na_fonte", "/".join(data.groups())))
    gravar(md, fonte, bruto, meta, f"# {titulo}\n\n{corpo}")
    with _ID_LOCK:
        _ID_PATHS.setdefault(str(it["id"]), []).append(md)
        _KEY_PATHS.setdefault(chave, []).append(md)
    return "ok", None


if __name__ == "__main__":
    itens = indice(refazer="--refazer" in sys.argv)
    itens.sort(key=lambda i: (i.get("ano") or "", int(i["id"])), reverse=True)
    print(f"[{UF}] {len(itens)} normas no índice", flush=True)
    limite = [a for a in sys.argv[1:] if a.isdigit()]
    if limite:
        itens = itens[: int(limite[0])]
    executar(UF, itens, processar, workers=1)
