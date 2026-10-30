"""Leis municipais do Portal Legislativo da Cittatec (EPROCLEG), pela API pública open-data-leg.

    python3 -I scripts/baixar_cittatec.py --tenant cmnovaprata --uf RS --municipio "NOVA PRATA"
    python3 -I scripts/baixar_cittatec.py --tenant cmnovaprata --uf RS --municipio "NOVA PRATA" --classificacao 35

Lista as normas pela GraphQL pública, lê número, ano e data em /processos/{id}, baixa o arquivo
original pelo GED e extrai o texto com pdftotext (poppler). Os PDFs ficam em _fonte/cittatec/<tenant>/.
O que não tem texto recuperável vai para municipais/<UF>/<municipio>/_falhas.jsonl.
"""
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import CANONICO, normalizar_chave, slugify, yaml_str

RAIZ = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0"
CLASSIFICACOES = {"LEI ORDINÁRIA": "lei ordinaria", "LEI COMPLEMENTAR": "lei complementar",
                  "EMENDA A LEI ORGÂNICA": "emenda a lei organica", "LEI ORGÂNICA": "lei organica",
                  "DECRETO LEGISLATIVO": "decreto legislativo", "RESOLUÇÃO": "resolucao"}
MESES = {m: i for i, m in enumerate(["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho",
                                     "agosto", "setembro", "outubro", "novembro", "dezembro"], 1)}
EPIGRAFE = re.compile(r"^\s*((?:LEI|EMENDA|DECRETO|RESOLU)[^\n]{0,40}?N\s*[.º°o]*\s*([\d.]+)\s*(?:/\s*(\d{2,4}))?[^\n]*)",
                      re.I | re.M)
DATA_EXTENSO = re.compile(r"\b(\d{1,2})\s*(?:º|°|o)?\s+(?:de\s+)?([a-zç]+)\s+(?:de\s+)?(\d\.?\d{3})\b", re.I)
LISTA = """query {{ proposicoes(page: {pagina}, size: {tamanho}, filters: [{{key: ANO, value: "[{ano},{ano}]"}},
{{key: CLASSIFICACAO, value: "{classificacao}"}}]) {{ id processo {{ id documento {{ id }} descricao titulo }} }} }}"""
TAMANHOS = (50, 37, 23, 10, 7)
LOCK = threading.Lock()
GRAVADOS = {}


class Portal:
    def __init__(self, tenant):
        self.base = f"https://{tenant}.cittatec.com.br/api"
        self.cabecalhos = {"User-Agent": UA, "ID-Tenant": tenant, "Accept": "application/json"}

    def pedir(self, url, corpo=None, binario=False, cabecalhos=None):
        for tentativa in range(5):
            try:
                req = urllib.request.Request(url, corpo, cabecalhos or self.cabecalhos)
                if corpo:
                    req.add_header("Content-Type", "application/json")
                with urllib.request.urlopen(req, timeout=180) as r:
                    dados = r.read()
                return dados if binario else json.loads(dados)
            except urllib.error.HTTPError as e:
                if e.code < 500 or tentativa == 4:
                    raise
            except (urllib.error.URLError, TimeoutError, ConnectionError):
                if tentativa == 4:
                    raise
            time.sleep(2 ** tentativa)

    def classificacoes(self):
        return self.pedir(f"{self.base}/open-data-leg/public/classificacoes?modulo=LEGISLATIVO&page=0&size=200")

    def pagina(self, classificacao, ano, tamanho):
        todas, pagina = [], 0
        while True:
            consulta = LISTA.format(pagina=pagina, tamanho=tamanho, ano=ano, classificacao=classificacao)
            r = self.pedir(f"{self.base}/open-data-leg/public/graphql", json.dumps({"query": consulta}).encode())
            if r.get("errors"):
                raise RuntimeError(r["errors"])
            lote = r["data"]["proposicoes"]
            todas += lote
            if len(lote) < tamanho:
                return todas
            pagina += 1

    def proposicoes(self, classificacao, primeiro_ano=1900):
        todas, incompletos = {}, {}
        for ano in range(primeiro_ano, dt.date.today().year + 1):
            vistos, linhas = {}, 0
            for tamanho in TAMANHOS:
                lote = self.pagina(classificacao, ano, tamanho)
                linhas = len(lote)
                vistos.update((x["id"], x) for x in lote)
                if len(vistos) == linhas:
                    break
            if len(vistos) < linhas:
                incompletos[ano] = {"linhas": linhas, "distintos": len(vistos)}
            todas.update(vistos)
        return list(todas.values()), incompletos

    def processo(self, pid):
        return self.pedir(f"{self.base}/open-data-leg/public/processos/{pid}")

    def documento(self, doc):
        return self.pedir(f"{self.base}/ged/public/documentos/{doc}")

    def arquivo(self, doc):
        for original in ("true", "false"):
            try:
                url = self.pedir(f"{self.base}/ged/public/documentos/{doc}/visualizar?arquivoOriginal={original}")["url"]
            except urllib.error.HTTPError as e:
                if e.code == 400:
                    continue
                raise
            return self.pedir(url, binario=True, cabecalhos={"User-Agent": UA})
        return None


def texto_do_pdf(caminho):
    bruto = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(caminho), "-"], capture_output=True, check=True).stdout
    paginas = bruto.decode("utf-8", errors="replace").split("\f")
    linhas = []
    for pagina in paginas:
        for linha in pagina.splitlines():
            linha = re.sub(r"[ \t ]+", " ", linha).strip()
            if re.fullmatch(r"\d{1,3}\s*/\s*\d{1,3}", linha):
                continue
            linhas.append(linha)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()


def data_por_extenso(texto):
    for m in DATA_EXTENSO.finditer(texto):
        mes = MESES.get(normalizar_chave(m.group(2)))
        if not mes:
            continue
        try:
            return dt.date(int(m.group(3).replace(".", "")), mes, int(m.group(1))).isoformat()
        except ValueError:
            continue
    return ""


def epigrafe(texto):
    linhas = texto.splitlines()
    for i, linha in enumerate(linhas[:15]):
        m = EPIGRAFE.match(linha)
        if m:
            titulo = m.group(1).strip()
            seguinte = linhas[i + 1].strip() if i + 1 < len(linhas) else ""
            if not re.search(r"\b\d{4}\.?$", titulo) and re.fullmatch(r"(?:DE\s+)?\d{4}\.?", seguinte, re.I):
                titulo = f"{titulo} {seguinte}"
            numero = re.sub(r"^(\d+)\.(?:19|20)\d{2}$", r"\1", m.group(2)).replace(".", "")
            return titulo, numero, " ".join(linhas[i:i + 2])
    return "", "", ""


def falha(destino, registro):
    with LOCK, open(destino, "a", encoding="utf-8") as f:
        f.write(json.dumps(registro, ensure_ascii=False) + "\n")


def gravar_norma(portal, item, chave, a, pasta_municipio, cache, falhas):
    pid = item["processo"]["id"]
    doc = item["processo"]["documento"]["id"]
    titulo_portal = item["processo"]["titulo"].strip()
    fonte = f"https://{a.tenant}.cittatec.com.br/portal-legislativo/proposicoes/texto-original/{pid}"
    base = {"processo": pid, "documento": doc, "titulo_portal": titulo_portal, "fonte": fonte,
            "data": dt.date.today().isoformat()}
    proc = portal.processo(pid)
    ged = portal.documento(doc)
    pdf = cache / f"{doc}.pdf"
    if not pdf.exists():
        conteudo = portal.arquivo(doc)
        if not conteudo:
            falha(falhas, base | {"status": "sem_arquivo"})
            return "falha"
        if not conteudo.startswith(b"%PDF"):
            falha(falhas, base | {"status": "nao_pdf", "inicio": conteudo[:20].hex()})
            return "falha"
        pdf.write_bytes(conteudo)
    sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
    if ged.get("hashArquivo") and ged["hashArquivo"] != sha:
        falha(falhas, base | {"status": "hash_divergente", "sha256_pdf": sha, "hash_ged": ged["hashArquivo"]})
        return "falha"
    texto = texto_do_pdf(pdf)
    if len(re.findall(r"\w+", texto)) < 15:
        falha(falhas, base | {"status": "pdf_sem_texto", "sha256_pdf": sha})
        return "falha"
    linha_epigrafe, numero_epigrafe, contexto = epigrafe(texto)
    numero = str(proc.get("nroDocumento") or "")
    observacoes = []
    if numero_epigrafe and numero_epigrafe.lstrip("0") != numero.lstrip("0"):
        observacoes.append(f"Número no portal: {numero or 'ausente'}; número na epígrafe do texto: {numero_epigrafe}.")
        numero = numero_epigrafe
    data = data_por_extenso(contexto)
    ano = data[:4] or str(proc.get("anoDocumento") or "")
    if not ano or not numero:
        falha(falhas, base | {"status": "sem_numero_ou_ano", "sha256_pdf": sha})
        return "falha"
    pasta, tipo = CANONICO[chave]
    titulo = linha_epigrafe or titulo_portal
    nome = slugify(f"{slugify(chave)}-{numero}-{ano}-{sha[:8]}")[:110] + ".md"
    md = pasta_municipio / pasta / ano / nome
    cab = ["---", f"titulo: {yaml_str(titulo)}", f"uf: {yaml_str(a.uf)}", f"municipio: {yaml_str(a.municipio)}",
           f"tipo: {yaml_str(tipo)}", f"numero: {yaml_str(numero)}", f"data: {data if data else yaml_str('')}",
           f"ano: {yaml_str(ano)}"]
    if item["processo"].get("descricao"):
        cab.append(f"ementa: {yaml_str(re.sub(r'\s+', ' ', item['processo']['descricao']).strip())}")
    cab += ["revogada: null", 'versao_texto: "texto disponibilizado no Portal Legislativo da Câmara"']
    if observacoes:
        cab.append(f"observacao: {yaml_str(' '.join(observacoes))}")
    cab += [f"sha256_pdf: {yaml_str(sha)}", f"documento_ged: {yaml_str(doc)}",
            f"fonte: {yaml_str(fonte)}", f"baixado_em: {dt.date.today().isoformat()}", "---", ""]
    corpo = f"# {titulo}\n\n{texto}\n"
    md.parent.mkdir(parents=True, exist_ok=True)
    with LOCK:
        if sha in GRAVADOS:
            registro = base | {"status": "mesmo_arquivo_de_outro_processo", "sha256_pdf": sha,
                               "processo_gravado": GRAVADOS[sha]}
        else:
            existentes = [e.name for e in md.parent.glob(f"{slugify(chave)}-{numero}-{ano}-*.md") if e.name != nome]
            registro = base | {"status": "numero_repetido", "sha256_pdf": sha, "existentes": existentes} if existentes else None
        if not registro:
            GRAVADOS[sha] = pid
            tmp = md.with_suffix(".md.tmp")
            tmp.write_text("\n".join(cab) + corpo, encoding="utf-8")
            os.replace(tmp, md)
    if registro:
        falha(falhas, registro)
        return "falha"
    return "gravada"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tenant", required=True)
    ap.add_argument("--uf", required=True)
    ap.add_argument("--municipio", required=True)
    ap.add_argument("--classificacao", action="append", help="id da classificação; padrão: leis e emendas à LO")
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--paralelo", type=int, default=4)
    a = ap.parse_args()
    portal = Portal(a.tenant)
    nomes = {str(c["id"]): c["descricao"].strip() for c in portal.classificacoes()}
    alvos = a.classificacao or [i for i, n in nomes.items() if n in ("LEI ORDINÁRIA", "LEI COMPLEMENTAR",
                                                                     "EMENDA A LEI ORGÂNICA", "LEI ORGÂNICA")]
    pasta_municipio = RAIZ / "municipais" / a.uf / slugify(normalizar_chave(a.municipio))[:60]
    cache = RAIZ / "_fonte" / "cittatec" / a.tenant
    cache.mkdir(parents=True, exist_ok=True)
    falhas = pasta_municipio / "_falhas.jsonl"
    pasta_municipio.mkdir(parents=True, exist_ok=True)
    falhas.unlink(missing_ok=True)
    total = {}
    for cid in alvos:
        chave = CLASSIFICACOES.get(nomes.get(cid, ""))
        if not chave or chave not in CANONICO:
            sys.exit(f"classificação {cid} ({nomes.get(cid)}) sem tipo canônico")
        itens, incompletos = portal.proposicoes(cid)
        for ano, n in incompletos.items():
            falha(falhas, {"classificacao": nomes[cid], "ano": ano, "status": "listagem_incompleta", **n,
                           "data": dt.date.today().isoformat()})
        (cache / f"lista-{cid}.json").write_text(json.dumps(itens, ensure_ascii=False, indent=1), encoding="utf-8")
        if a.limite:
            itens = itens[:a.limite]
        with concurrent.futures.ThreadPoolExecutor(a.paralelo) as ex:
            futuros = {ex.submit(gravar_norma, portal, i, chave, a, pasta_municipio, cache, falhas): i for i in itens}
            for f in concurrent.futures.as_completed(futuros):
                try:
                    r = f.result()
                except Exception as e:
                    i = futuros[f]
                    falha(falhas, {"processo": i["processo"]["id"], "titulo_portal": i["processo"]["titulo"],
                                   "status": "erro", "erro": repr(e)[:300], "data": dt.date.today().isoformat()})
                    r = "falha"
                total[(nomes[cid], r)] = total.get((nomes[cid], r), 0) + 1
    print(json.dumps({f"{c} {r}": n for (c, r), n in sorted(total.items())}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
