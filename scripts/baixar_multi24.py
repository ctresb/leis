"""Leis municipais publicadas como PDF no Portal da Transparência Multi24h, com OCR das digitalizações.

    python3 -I scripts/baixar_multi24.py --host novaprata --uf RS --municipio "NOVA PRATA" \\
        --secao 20047 --secao 20043 --secao 21523

Cada --secao é o id de uma página "dinamico" do portal com a lista de PDFs. Os PDFs ficam em
_fonte/multi24/<host>/. Com --motor lighton (padrão), o texto das páginas sem camada de texto vem do
cache <id>.<sha>.lighton.json gerado na GPU por scripts/ocr_lighton.py (LightOnOCR-3-0.8B, revisão fixa):

    python -I scripts/ocr_lighton.py _fonte/multi24/novaprata --revisao 36d8636925327c671bd8e479c517a004f7566bd9

Com --motor tesseract, passam por Tesseract 5 com o modelo tessdata_best/por.traineddata em
scripts/bin/tessdata/ (SHA-256 conferido, como em comum.ocr_imagem).
Normas que já existem no acervo com o mesmo tipo, número e ano não são regravadas.
O que não vira norma vai para municipais/<UF>/<municipio>/_falhas_multi24.jsonl.
"""
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar_cittatec import data_por_extenso, epigrafe
from comum import CANONICO, normalizar_chave, slugify, yaml_str

RAIZ = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0"
TESSDATA = RAIZ / "scripts" / "bin" / "tessdata"
MODELO_SHA = "711de9dbb8052067bd42f16b9119967f30bada80d57e2ef24f65d09f531adb04"
MOTORES = {"tesseract": "Tesseract 5, português, tessdata_best, 300 dpi",
           "lighton": "LightOnOCR-3-0.8B (lightonai, revisão {revisao}), 400 dpi, transcrição sem amostragem"}
ITEM = re.compile(r'<a href="(\?entidade=\d+&secao=download&sub=menu&id=(\d+))"[^>]*>([^<]*)</a>\s*</span>'
                  r'\s*<span class="publicacao">\(Publicado em (\d{2})/(\d{2})/(\d{4})[^)]*\)')
PARAGRAFO = re.compile(r"(?<![R\w])\$\s?(?=\d{1,2}\s?\.?\s?[º°o]|[Úú]nico)", re.I)
NUMERO_NOME = re.compile(r"^\W*LEI\b(?:\s+MUNICIPAL)?\s*(?:N[º°ª.\s]{0,4})?([\d][\d.]*)", re.I)


def pedir(url):
    for tentativa in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=180) as r:
                return r.read()
        except OSError:
            if tentativa == 4:
                raise
            time.sleep(2 ** tentativa)


def listar(base, secao):
    pagina = pedir(f"{base}?entidade=1&secao=dinamico&id={secao}").decode("latin-1")
    return [{"secao": secao, "href": h, "id": i, "nome": html.unescape(re.sub(r"\s+", " ", n)).strip(),
             "publicado": f"{a}-{m}-{d}"} for h, i, n, d, m, a in ITEM.findall(pagina)]


def conferir_modelo():
    if not shutil.which("tesseract"):
        sys.exit("tesseract não encontrado")
    modelo = TESSDATA / "por.traineddata"
    if not modelo.is_file() or hashlib.sha256(modelo.read_bytes()).hexdigest() != MODELO_SHA:
        sys.exit(f"modelo ausente ou com SHA-256 diferente: {modelo}")


def texto_pagina(pdf, pagina, pasta):
    camada = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", "-f", str(pagina), "-l", str(pagina), str(pdf), "-"],
                            capture_output=True, check=True).stdout.decode("utf-8", "replace")
    if len(re.sub(r"\W", "", camada)) >= 300:
        return camada, False
    raiz = os.path.join(pasta, f"p{pagina}")
    subprocess.run(["pdftoppm", "-r", "300", "-gray", "-png", "-f", str(pagina), "-l", str(pagina), "-singlefile",
                    str(pdf), raiz], check=True, capture_output=True)
    r = subprocess.run(["tesseract", raiz + ".png", "stdout", "--tessdata-dir", str(TESSDATA), "-l", "por",
                        "--oem", "1", "--psm", "3"], capture_output=True, timeout=600,
                       env={**os.environ, "OMP_THREAD_LIMIT": "1"})
    return PARAGRAFO.sub("§ ", r.stdout.decode("utf-8", "replace")), True


def sem_markdown(texto):
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    texto = re.sub(r"^\W*(?:Note:\s|Signature\b|Stamp\b|Seal\b).*$", "", texto, flags=re.M)
    texto = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", texto)
    texto = re.sub(r"\[(?:Signature|Stamp|Seal|Logo|Image)[^\]]*\]|\([^()\n]*\b(?:Signature|Stamp|Seal|Logo|Image)\b[^()\n]*\)", "", texto,
                   flags=re.I)
    texto = re.sub(r"<br\s*/?>|</?(?:div|p|tr|table|thead|tbody|h\d)\b[^>]*>", "\n", texto, flags=re.I)
    texto = re.sub(r"</t[dh]>\s*<t[dh][^>]*>", " | ", texto, flags=re.I)
    texto = re.sub(r"<[^>]+>", "", texto)
    texto = re.sub(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$", "", texto, flags=re.M)
    texto = re.sub(r"^\s*#{1,6}\s+", "", texto, flags=re.M)
    texto = re.sub(r"\*\*|__", "", texto)
    texto = re.sub(r"(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])", r"\1", texto)
    return html.unescape(texto)


def extrair_lighton(cache_lighton):
    partes, ocr, paginas, truncadas, _, revisao, *_ = json.loads(cache_lighton.read_text(encoding="utf-8"))
    if truncadas:
        raise ValueError(f"OCR truncado nas páginas {truncadas}")
    return limpar("\n\n".join(PARAGRAFO.sub("§ ", sem_markdown(t)) for t in partes)), ocr, paginas, revisao


def limpar(texto):
    linhas = [re.sub(r"[ \t ]+", " ", l).strip() for l in texto.replace("\f", "\n").splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()


def extrair(pdf):
    paginas = int(re.search(r"^Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                                                               text=True).stdout, re.M).group(1))
    partes, ocr = [], False
    with tempfile.TemporaryDirectory() as pasta:
        for n in range(1, paginas + 1):
            t, o = texto_pagina(pdf, n, pasta)
            partes.append(t)
            ocr |= o
    return limpar("\n\n".join(partes)), ocr, paginas


def sem_carimbo(texto):
    linhas = texto.splitlines()
    mural = next((i for i, l in enumerate(linhas[:60]) if re.search(r"\bqua\w{2,4}\s+mur\w*|\bmur\w{1,2}\W?\s+das\s+depend", l, re.I)), None)
    if mural is None:
        caixas = next((i for i, l in enumerate(linhas[:8]) if re.search(r"DECRETO|EDITAL", l, re.I)
                       and re.search(r"PORTARIA", l, re.I) and len(l.strip()) < 60), None)
        cabecalho = next((i for i, l in enumerate(linhas[:25]) if re.search(r"ESTADO DO RIO GRANDE|MUNIC[IÍ]PIO DE", l, re.I)), None)
        if caixas is None or cabecalho is None or cabecalho <= caixas or cabecalho - caixas > 14:
            return texto, False
        return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas[:caixas] + linhas[cabecalho:])).strip(), True
    inicio = mural
    for i in range(mural - 1, max(-1, mural - 5), -1):
        if not linhas[i].strip():
            continue
        if re.search(r"DECRETO|EDITAL|PORTARIA", linhas[i], re.I) and len(linhas[i].strip()) < 60:
            inicio = i
        break
    fim, data_lida = mural + 1, False
    while fim < len(linhas) and fim <= mural + 12:
        l = linhas[fim].strip()
        if not l or re.search(r"Prefeitura\s+Municipal\s+de", l, re.I) \
                or (not data_lida and re.match(r"\W*de\b", l, re.I) and len(l) < 40) \
                or (len(l) <= 12 and not re.search(r"[a-zà-ú]{4,}", l)):
            data_lida |= bool(re.match(r"\W*de\b", l, re.I))
            fim += 1
            continue
        break
    cabecalho = next((i for i in range(mural + 1, min(len(linhas), mural + 16))
                      if re.search(r"ESTADO DO RIO GRANDE|MUNIC[IÍ]PIO DE", linhas[i], re.I)), None)
    if cabecalho is not None and cabecalho > fim:
        fim = cabecalho
    return re.sub(r"\n{3,}", "\n\n", "\n".join(linhas[:inicio] + linhas[fim:])).strip(), True


def sem_carimbos_internos(texto):
    linhas, saida, removidos, i = texto.splitlines(), [], 0, 0
    while i < len(linhas):
        if re.search(r"\bLEI\w{0,2}\W{0,6}DECRETO\W{0,6}EDITAL\W{0,6}PORTAR|Publicado\s+no\s+quadro\s+mural", linhas[i], re.I):
            fim = i + 1
            while fim < len(linhas) and fim <= i + 8:
                l = linhas[fim].strip()
                if not l or re.search(r"Publicado|quadro\s+mural|depend[eê]ncias|Prefeitura\s+Municipal\s+de\s+Nova\s+Prata", l, re.I) \
                        or (len(l) <= 25 and not re.search(r"[A-Za-zÀ-ú]{5,}", l)):
                    fim += 1
                    continue
                break
            removidos += 1
            i = fim
            continue
        saida.append(linhas[i])
        i += 1
    return re.sub(r"\n{3,}", "\n\n", "\n".join(saida)).strip(), removidos


def data_com_ano_do_numero(linha, contexto):
    ano = re.search(r"/\s*((?:19|20)\d{2})\b", linha)
    if not ano:
        return ""
    return data_por_extenso(re.sub(r"(\bde\s+[a-zç]+\s+de\s+)\S+", rf"\g<1>{ano.group(1)}", contexto, count=1, flags=re.I))


def processar(item, a, cache, pasta_municipio):
    base = f"https://{a.host}.multi24h.com.br/multi24/sistemas/transparencia/"
    fonte = base + item["href"]
    registro = {"id": item["id"], "nome_portal": item["nome"], "fonte": fonte, "data": dt.date.today().isoformat()}
    pdf = cache / f"{item['id']}.pdf"
    if not pdf.exists():
        conteudo = pedir(fonte)
        if not conteudo.startswith(b"%PDF"):
            return registro | {"status": "nao_pdf"}
        pdf.write_bytes(conteudo)
    sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
    cache_texto = cache / f"{item['id']}.{sha[:16]}.json"
    motor = MOTORES["tesseract"]
    if a.motor == "lighton":
        cache_lighton = cache / f"{item['id']}.{sha[:16]}.lighton.json"
        if not cache_lighton.exists():
            return registro | {"status": "sem_ocr_lighton", "sha256_pdf": sha}
        texto, ocr, paginas, revisao = extrair_lighton(cache_lighton)
        motor = MOTORES["lighton"].format(revisao=revisao[:7])
    elif cache_texto.exists():
        texto, ocr, paginas = json.loads(cache_texto.read_text(encoding="utf-8"))
        if ocr:
            texto = PARAGRAFO.sub("§ ", texto)
    else:
        texto, ocr, paginas = extrair(pdf)
        cache_texto.write_text(json.dumps([texto, ocr, paginas], ensure_ascii=False), encoding="utf-8")
    if len(re.findall(r"\w+", texto)) < 15:
        return registro | {"status": "sem_texto", "sha256_pdf": sha}
    texto, carimbo = sem_carimbo(texto)
    internos = 0
    if ocr:
        texto, internos = sem_carimbos_internos(texto)
    if ocr:
        linhas = texto.splitlines()
        uteis = [i for i, l in enumerate(linhas) if l.strip()][:15]
        topo = next((i for i in uteis if re.search(r"ESTADO DO RIO GRANDE|MUNIC[IÍ]PIO DE", linhas[i], re.I)
                     or epigrafe(linhas[i])[0]), None)
        if topo and any(linhas[i].strip() for i in range(topo)):
            texto, carimbo = "\n".join(linhas[topo:]).strip(), True
    linha, numero_epigrafe, contexto = epigrafe(texto)
    m = NUMERO_NOME.search(item["nome"])
    numero_nome = re.sub(r"(\.\d{3})\.(?:(?:19|20)\d{2}|\d{2})$", r"\1", m.group(1).rstrip(".")).replace(".", "") if m else ""
    numero = numero_epigrafe or numero_nome
    observacoes = []
    if numero_epigrafe and numero_nome and numero_epigrafe.lstrip("0") != numero_nome.lstrip("0"):
        curto, longo = len(numero_epigrafe.lstrip("0")) < len(numero_nome.lstrip("0")), \
            len(numero_epigrafe.lstrip("0")) > len(numero_nome.lstrip("0")) >= 5
        if curto:
            numero = numero_nome
            observacoes.append(f"Número na epígrafe ilegível no OCR (lido {numero_epigrafe}); "
                               f"usado o do nome do arquivo no portal: {numero_nome}.")
        elif longo:
            return registro | {"status": "numero_ambiguo", "sha256_pdf": sha, "epigrafe": linha,
                               "numero_epigrafe": numero_epigrafe, "numero_nome": numero_nome}
        else:
            observacoes.append(f"Número no nome do arquivo do portal: {numero_nome}; número na epígrafe: {numero_epigrafe}.")
    data = data_por_extenso(contexto)
    if not data and linha:
        data = data_com_ano_do_numero(linha, contexto)
        if data:
            observacoes.append("Ano da data por extenso ilegível no OCR; ano tomado do número da lei na epígrafe.")
    if carimbo:
        observacoes.append("Carimbo de publicação no quadro mural, no topo da primeira página, omitido do texto.")
    if internos:
        observacoes.append("Carimbo de publicação no quadro mural repetido nas páginas seguintes, omitido do texto.")
    ano = data[:4]
    if not numero or not ano:
        return registro | {"status": "sem_numero_ou_data_na_epigrafe", "sha256_pdf": sha, "epigrafe": linha}
    chave = "lei ordinaria"
    pasta, tipo = CANONICO[chave]
    destino = pasta_municipio / pasta / ano
    prefixo = f"{slugify(chave)}-{numero}-{ano}-"
    nome = slugify(f"{prefixo}{sha[:8]}")[:110] + ".md"
    cab = ["---", f"titulo: {yaml_str(linha)}", f"uf: {yaml_str(a.uf)}", f"municipio: {yaml_str(a.municipio)}",
           f"tipo: {yaml_str(tipo)}", f"numero: {yaml_str(numero)}", f"data: {data}", f"ano: {yaml_str(ano)}",
           "revogada: null", 'versao_texto: "cópia digitalizada da lei assinada, publicada no Portal da Transparência"']
    if ocr:
        cab.append(f"ocr: {yaml_str(motor)}")
    if observacoes:
        cab.append(f"observacao: {yaml_str(' '.join(observacoes))}")
    cab += [f"publicado_no_portal: {item['publicado']}", f"paginas_pdf: {paginas}", f"sha256_pdf: {yaml_str(sha)}",
            f"fonte_indice: {yaml_str(base + '?entidade=1&secao=dinamico&id=' + str(item['secao']))}",
            f"fonte: {yaml_str(fonte)}", f"baixado_em: {dt.date.today().isoformat()}", "---", ""]
    divergente = any(o.startswith("Número") for o in observacoes)
    return {"gravar": str(destino / nome), "prefixo": prefixo, "divergente": divergente,
            "conteudo": "\n".join(cab) + f"# {linha}\n\n{texto}\n", "registro": registro | {"sha256_pdf": sha}}


def gravar(g, gravados):
    md = Path(g["gravar"])
    existentes = [e.name for e in md.parent.glob(g["prefixo"] + "*.md") if e.name != md.name]
    if existentes:
        status = "numero_repetido" if any(e in gravados for e in existentes) else "ja_no_acervo"
        return g["registro"] | {"status": status, "existentes": existentes}
    md.parent.mkdir(parents=True, exist_ok=True)
    tmp = md.with_suffix(".md.tmp")
    tmp.write_text(g["conteudo"], encoding="utf-8")
    os.replace(tmp, md)
    gravados.add(md.name)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", required=True)
    ap.add_argument("--uf", required=True)
    ap.add_argument("--municipio", required=True)
    ap.add_argument("--secao", action="append", required=True)
    ap.add_argument("--motor", choices=sorted(MOTORES), default="lighton")
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--paralelo", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    a = ap.parse_args()
    if a.motor == "tesseract":
        conferir_modelo()
    base = f"https://{a.host}.multi24h.com.br/multi24/sistemas/transparencia/"
    cache = RAIZ / "_fonte" / "multi24" / a.host
    cache.mkdir(parents=True, exist_ok=True)
    pasta_municipio = RAIZ / "municipais" / a.uf / slugify(normalizar_chave(a.municipio))[:60]
    itens = {}
    for secao in a.secao:
        for item in listar(base, secao):
            itens.setdefault(item["id"], item)
    itens = list(itens.values())[:a.limite or None]
    (cache / "lista.json").write_text(json.dumps(itens, ensure_ascii=False, indent=1), encoding="utf-8")
    falhas = pasta_municipio / "_falhas_multi24.jsonl"
    registros, pendentes = [], []
    with concurrent.futures.ProcessPoolExecutor(a.paralelo) as ex:
        futuros = {ex.submit(processar, i, a, cache, pasta_municipio): i for i in itens}
        for n, f in enumerate(concurrent.futures.as_completed(futuros), 1):
            try:
                r = f.result()
            except Exception as e:
                i = futuros[f]
                r = {"id": i["id"], "nome_portal": i["nome"], "status": "erro", "erro": repr(e)[:300],
                     "data": dt.date.today().isoformat()}
            (pendentes if "gravar" in r else registros).append(r)
            if n % 25 == 0:
                print(f"{n}/{len(itens)} processadas", flush=True)
    gravados = set()
    for g in sorted(pendentes, key=lambda g: (g["divergente"], int(g["registro"]["id"]))):
        r = gravar(g, gravados)
        if r:
            registros.append(r)
    gravadas = len(gravados)
    registros.sort(key=lambda r: int(r["id"]))
    falhas.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in registros), encoding="utf-8")
    contagem = {}
    for r in registros:
        contagem[r["status"]] = contagem.get(r["status"], 0) + 1
    print(json.dumps({"itens": len(itens), "gravadas": gravadas, **contagem}, ensure_ascii=False))


if __name__ == "__main__":
    main()
