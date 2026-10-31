"""Paraná — Sistema Estadual de Legislação (Casa Civil, legislacao.pr.gov.br).

Índice: listarAtosAno.do?action=listarAtos&anoAto=AAAA (POST com codTipoAto), um ano por vez.
Texto: exibirAto.do?action=iniciarProcesso&codAto=N (rota pública do ato).
"""
import datetime as dt
import gzip
import html as htmllib
import http.cookiejar
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from comum import RAIZ_ESTADUAIS, UA, Rede, caminhos, decodificar, executar, gravar, html_para_md  # noqa: E402

UF = "PR"
B = "https://www.legislacao.pr.gov.br/legislacao"
# codTipoAto do sistema da Casa Civil -> (pasta, tipo canônico, prefixo do arquivo). O seletor da
# pesquisa oferece sete tipos; o infralegal entra junto, como nos demais estados.
TIPOS = {
    "10": ("constituicao", "Constituição Estadual", "ce"),
    "9": ("emendas-constitucionais", "Emenda Constitucional", "ec"),
    "3": ("leis-complementares", "Lei Complementar", "lc"),
    "1": ("leis-ordinarias", "Lei Ordinária", "lei"),
    "11": ("decretos", "Decreto", "dec"),
    "13": ("resolucoes", "Resolução", "res"),
    "14": ("portarias", "Portaria", "port"),
}
rede = Rede(rps=1)  # o WAF já devolveu 403 a partir da segunda requisição; mantém-se devagar
_sessao = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
LINHA = re.compile(
    r"codAto=(\d+)&indice.*?_epigrafeAto\">(.*?)</div>.*?_descricaoItemAto\">(.*?)</div>.*?_dataPublicacao\">(.*?)</div>",
    re.S,
)
MESES = {m: i for i, m in enumerate(
    "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split(), 1)}


def limpar(s):
    return " ".join(htmllib.unescape(re.sub(r"<[^>]+>", " ", s)).split())


def post(caminho, dados, tentativas=4):
    req = urllib.request.Request(f"{B}/{caminho}", data=urllib.parse.urlencode(dados).encode(), headers={"User-Agent": UA})
    for n in range(tentativas):
        rede.limite.esperar()
        try:
            with _sessao.open(req, timeout=300) as r:
                return decodificar(r.read(), r.headers.get("Content-Type") or "")
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 429):
                raise RuntimeError(f"fonte recusou acesso (HTTP {e.code}); coleta interrompida") from e
            if n == tentativas - 1:
                raise
            time.sleep(30 * (n + 1))
        except Exception:
            if n == tentativas - 1:
                raise
            time.sleep(30 * (n + 1))


def indice(refazer=False):
    pasta = os.path.join(RAIZ_ESTADUAIS, UF, "_indice")
    arq = os.path.join(pasta, "atos.json")
    if os.path.exists(arq) and not refazer:
        return json.load(open(arq, encoding="utf-8"))
    itens = {}
    os.makedirs(pasta, exist_ok=True)
    for tipo in TIPOS:
        st, dados, ctype = rede.get(f"{B}/listarAtosAno.do?action=iniciarProcesso&tipoAto={tipo}&orgaoUnidade=1100&retiraLista=true&site=1")
        html = decodificar(dados, ctype)
        if st != 200:
            raise RuntimeError(f"índice tipo {tipo}: HTTP {st}")
        anos = sorted({a for _, a in re.findall(r"listarAtos\('(\d{4})', '(\d{4})'\)", html)}, reverse=True)
        if not anos:  # tipo com um único ato (Constituição): a página já é o próprio ato
            for cod in dict.fromkeys(re.findall(r'name="codAto" value="(\d+)"', html)):
                itens[cod] = {"codAto": cod, "tipo": tipo, "epigrafe": "", "ementa": "", "publicacao": ""}
        for ano in anos:
            cache = os.path.join(pasta, f"tipo-{tipo}-{ano}.html")
            if os.path.exists(cache) and not refazer:
                with open(cache, encoding="utf-8") as f:
                    h = f.read()
            else:
                h = post(
                    f"listarAtosAno.do?action=listarAtos&anoAto={ano}&isPaginado=false",
                    dict(codTipoAto=tipo, codTipoAtoSelecionado=tipo, codOrgaoUnidade="1100", codOrgaoUnidadeSelecionado="1100",
                         pesquisou="", anoAtoPesquisado="0", paginaAtual="", isPaginado="false", site="1"),
                )
                with open(cache, "w", encoding="utf-8") as f:
                    f.write(h)
            for cod, epi, ementa, pub in LINHA.findall(h):
                itens[cod] = {"codAto": cod, "tipo": tipo, "ano": ano, "epigrafe": limpar(epi), "ementa": limpar(ementa), "publicacao": limpar(pub)}
        print(f"[{UF}] índice tipo {tipo}: {sum(1 for i in itens.values() if i['tipo'] == tipo)}", flush=True)
    lista = list(itens.values())
    os.makedirs(pasta, exist_ok=True)
    with open(arq, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False)
    return lista


def processar(it):
    pasta, nome, prefixo = TIPOS[it["tipo"]]
    url = f"{B}/exibirAto.do?action=iniciarProcesso&codAto={it['codAto']}"
    epi = it.get("epigrafe") or ""
    num = re.search(r"([\d.]+)\s*-\s*(\d{1,2}) de (\w+) de (\d{4})", epi)
    ano = it.get("ano") or (num.group(4) if num else "sem-ano")
    numero = num.group(1).replace(".", "") if num else "sn"
    slug = f"{prefixo}-{numero}-{ano}-id{it['codAto']}"
    md, fonte = caminhos(UF, pasta, ano, slug)
    if os.path.exists(md):
        return "pulado", None
    cache = os.path.join(RAIZ_ESTADUAIS, UF, "_indice", "documentos", it["codAto"] + ".html.gz")
    if os.path.exists(cache):
        st, bruto, ctype = 200, gzip.decompress(open(cache, "rb").read()), "text/html;charset=UTF-8"
    else:
        st, bruto, ctype = rede.get(url, timeout=60, tentativas=1)
    if st != 200:
        return "sem_texto", {"codAto": it["codAto"], "http": st}
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    with open(cache, "wb") as f:
        f.write(gzip.compress(bruto))
    html = decodificar(bruto, ctype)
    ini = html.find("<h3>")
    fim = html.find("</form>", ini)
    if ini < 0:
        return "sem_texto", {"codAto": it["codAto"], "motivo": "sem texto"}
    trecho = html[ini : fim if fim > 0 else None]
    titulo = limpar(re.search(r"<h3>(.*?)</h3>", trecho, re.S).group(1)) or epi
    corpo = html_para_md(trecho)
    if len(re.sub(r"\W", "", corpo)) < 40:
        return "sem_texto", {"codAto": it["codAto"], "motivo": "texto vazio"}
    data = ""
    m = re.search(r"(\d{1,2}) de (\w+) de (\d{4})", titulo)
    if m and m.group(2).lower() in MESES:
        data = f"{m.group(3)}-{MESES[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    data_original = data
    if data:
        try:
            if dt.date.fromisoformat(data) > dt.date.today():
                data = ""
        except ValueError:
            data = ""
    meta = [
        ("titulo", titulo),
        ("uf", UF),
        ("tipo", nome),
        ("numero", num.group(1) if num else ""),
        ("data", data),
        ("ementa", it.get("ementa") or ""),
        ("versao_texto", "compilada (Casa Civil do Paraná)"),
        ("fonte", url),
    ]
    if data_original and not data:
        meta.append(("data_na_fonte", data_original))
    gravar(md, fonte, trecho, meta, f"# {titulo}\n\n{corpo}")
    return "ok", None


if __name__ == "__main__":
    itens = indice(refazer="--refazer" in sys.argv)
    itens.sort(key=lambda i: (i.get("ano") or "", int(i["codAto"])), reverse=True)
    print(f"[{UF}] {len(itens)} normas no índice", flush=True)
    limite = [a for a in sys.argv[1:] if a.isdigit()]
    if limite:
        itens = itens[: int(limite[0])]
    executar(UF, itens, processar, workers=3)
