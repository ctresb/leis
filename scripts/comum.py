"""Utilitários compartilhados pelos baixadores estaduais: rede com limite de taxa, gravação de Markdown e execução."""
import collections
import datetime as dt
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

from html2md import HEADINGS, LABEL, convert

RAIZ_ESTADUAIS = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "estaduais"))
UA = "Mozilla/5.0 (compatible; constituicao-md/1.0)"


class Limitador:
    """Limita requisições por segundo entre todas as threads."""

    def __init__(self, rps):
        self.intervalo = 1.0 / rps
        self.prox = time.monotonic()
        self.lock = threading.Lock()

    def esperar(self):
        with self.lock:
            agora = time.monotonic()
            espera = self.prox - agora
            self.prox = max(agora, self.prox) + self.intervalo
        if espera > 0:
            time.sleep(espera)


class Rede:
    def __init__(self, rps=3, headers=None):
        self.limite = Limitador(rps)
        self.headers = {"User-Agent": UA, "Accept-Encoding": "gzip", **(headers or {})}

    def get(self, url, accept="*/*", tentativas=4, timeout=120):
        req = urllib.request.Request(url, headers={**self.headers, "Accept": accept})
        ultimo = None
        for n in range(tentativas):
            self.limite.esperar()
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    dados = r.read()
                    if r.headers.get("Content-Encoding") == "gzip":
                        dados = gzip.decompress(dados)
                    return r.status, dados, r.headers.get("Content-Type") or ""
            except urllib.error.HTTPError as e:
                if e.code in (400, 403, 404, 410):
                    return e.code, b"", ""
                ultimo = e
            except Exception as e:  # rede, IncompleteRead, timeout
                ultimo = e
            time.sleep(2 * (n + 1) ** 2)
        raise RuntimeError(f"falhou após {tentativas} tentativas: {url}: {ultimo}")


def decodificar(dados, content_type=""):
    """Decodifica HTML respeitando BOM, charset do cabeçalho ou da <meta>; cai para cp1252."""
    if dados[:2] in (b"\xff\xfe", b"\xfe\xff"):  # UTF-16 com BOM (HTML exportado do Word)
        return dados.decode("utf-16", errors="replace")
    if dados[:3] == b"\xef\xbb\xbf":
        return dados[3:].decode("utf-8", errors="replace")
    m = re.search(r"charset=([\w-]+)", content_type, re.I) or re.search(rb"charset=[\"']?([\w-]+)", dados[:3000], re.I)
    cs = m.group(1) if m else None
    if isinstance(cs, bytes):
        cs = cs.decode("ascii", "ignore")
    for enc in filter(None, [cs, "utf-8", "cp1252"]):
        try:
            return dados.decode(enc)
        except (LookupError, UnicodeDecodeError):
            continue
    return dados.decode("utf-8", errors="replace")


def yaml_str(v):
    return json.dumps(v if v is not None else "", ensure_ascii=False)


def slugify(s):
    s = re.sub(r"[^\w.-]+", "-", s.strip().lower(), flags=re.UNICODE)
    return re.sub(r"-{2,}", "-", s).strip("-")


# Vocabulário canônico de tipos de norma. Cada fonte nomeia o mesmo instrumento à sua maneira
# ("LEI ORDINARIA", "Lei", "Lei ordinária"); aqui tudo converge para um par (pasta, tipo).
# Instrumentos que a fonte distingue de verdade (lei promulgada, decreto-lei complementar,
# lei orgânica) continuam separados. `scripts/normalizar.py` aplica o mesmo mapa ao acervo já
# gravado — os dois precisam concordar.
CANONICO = {
    "constituicao estadual": ("constituicao", "Constituição Estadual"),
    "constituicao do estado": ("constituicao", "Constituição Estadual"),
    "emenda constitucional": ("emendas-constitucionais", "Emenda Constitucional"),
    "emenda a constituicao": ("emendas-constitucionais", "Emenda Constitucional"),
    "emenda a constituicao estadual": ("emendas-constitucionais", "Emenda Constitucional"),
    "emenda a ce": ("emendas-constitucionais", "Emenda Constitucional"),
    "lei": ("leis-ordinarias", "Lei Ordinária"),
    "lei ordinaria": ("leis-ordinarias", "Lei Ordinária"),
    "lei nao numerada": ("leis-ordinarias", "Lei Ordinária"),
    "lei complementar": ("leis-complementares", "Lei Complementar"),
    "lei complementar consolidada": ("leis-complementares", "Lei Complementar"),
    "lei delegada": ("leis-delegadas", "Lei Delegada"),
    "lei constitucional": ("leis-constitucionais", "Lei Constitucional"),
    "lei promulgada": ("leis-promulgadas", "Lei Promulgada"),
    "lei ordinaria promulgada": ("leis-promulgadas", "Lei Promulgada"),
    "decreto lei": ("decretos-lei", "Decreto-Lei"),
    "decreto lei complementar": ("decretos-lei-complementares", "Decreto-Lei Complementar"),
    "lei organica": ("lei-organica", "Lei Orgânica"),
    "emenda a lei organica": ("emendas-lei-organica", "Emenda à Lei Orgânica"),
    "emenda constitucional de revisao": ("emendas-constitucionais", "Emenda Constitucional de Revisão"),
    # Executivo e Congresso: tipos que entraram com a esfera federal completa
    "decreto": ("decretos", "Decreto"),
    "decreto numerado": ("decretos", "Decreto"),
    "decreto executivo": ("decretos", "Decreto"),
    "decreto do executivo": ("decretos", "Decreto"),
    "decreto nao numerado": ("decretos-nao-numerados", "Decreto (não numerado)"),
    "decreto legislativo": ("decretos-legislativos", "Decreto Legislativo"),
    "decreto do poder legislativo": ("decretos-legislativos", "Decreto do Poder Legislativo"),
    "medida provisoria": ("medidas-provisorias", "Medida Provisória"),
    "resolucao do senado federal": ("resolucoes-senado", "Resolução do Senado Federal"),
    "resolucao da camara dos deputados": ("resolucoes-camara", "Resolução da Câmara dos Deputados"),
    "resolucao do congresso nacional": ("resolucoes-congresso", "Resolução do Congresso Nacional"),
    "resolucao da revisao constitucional": ("resolucoes-congresso", "Resolução da Revisão Constitucional"),
    "regimento interno": ("regimentos", "Regimento Interno"),
    # infralegal e jurisprudência: o vocabulário já fica fechado antes de os raspadores chegarem,
    # para que nenhuma fonte nova invente uma grafia própria (ver scripts/plano.py)
    "resolucao": ("resolucoes", "Resolução"),
    "resolucao normativa": ("resolucoes", "Resolução"),
    # como as Assembleias do AM e de outras nomeiam a resolução da própria Casa
    "resolucao legislativa": ("resolucoes", "Resolução"),
    "resolucao da assembleia": ("resolucoes", "Resolução"),
    "resolucao de plenario": ("resolucoes", "Resolução"),
    "resolucao de mesa": ("resolucoes", "Resolução"),
    "regimento interno resolucao 08 2023": ("regimentos", "Regimento Interno"),
    "resolucao da diretoria colegiada": ("resolucoes", "Resolução da Diretoria Colegiada"),
    "deliberacao": ("deliberacoes", "Deliberação"),
    "portaria": ("portarias", "Portaria"),
    "instrucao normativa": ("instrucoes-normativas", "Instrução Normativa"),
    "circular": ("circulares", "Circular"),
    "parecer normativo": ("pareceres-normativos", "Parecer Normativo"),
    "provimento": ("provimentos", "Provimento"),
    "norma regulamentadora": ("normas-regulamentadoras", "Norma Regulamentadora"),
    "solucao de consulta": ("solucoes-de-consulta", "Solução de Consulta"),
    "ato normativo": ("atos-normativos", "Ato Normativo"),
    "recomendacao": ("recomendacoes", "Recomendação"),
    "ato declaratorio interpretativo": ("atos-declaratorios", "Ato Declaratório Interpretativo"),
    "ato declaratorio normativo": ("atos-declaratorios", "Ato Declaratório Normativo"),
    "convenio icms": ("convenios", "Convênio ICMS"),
    "protocolo icms": ("protocolos", "Protocolo ICMS"),
    "ajuste sinief": ("ajustes-sinief", "Ajuste SINIEF"),
    "sumula": ("sumulas", "Súmula"),
    "sumula vinculante": ("sumulas-vinculantes", "Súmula Vinculante"),
    "tratado": ("tratados", "Tratado"),
    "convencao": ("tratados", "Convenção"),
}
_ACENTOS = str.maketrans("áàâãäéèêëíìîïóòôõöúùûüçÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ",
                         "aaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC")


def normalizar_chave(s):
    """Minúsculas, sem acento e com um espaço entre palavras — a forma das chaves de CANONICO."""
    return re.sub(r"[^a-z0-9]+", " ", (s or "").translate(_ACENTOS).lower()).strip()


def canonico(bruto):
    """(pasta, tipo) canônicos a partir do nome que a fonte usa. Avisa quando não reconhece."""
    limpo = re.sub(r"\s*\(\d{4}\)\s*$", "", bruto)  # "Constituição Estadual (1891)"
    chave = normalizar_chave(limpo)
    if chave in CANONICO:
        return CANONICO[chave]
    print(f"[aviso] tipo fora do vocabulário canônico: {bruto!r}", flush=True)
    return slugify(bruto), bruto


def caminhos(uf, pasta, ano, slug):
    base = os.path.join(RAIZ_ESTADUAIS, uf)
    return (
        os.path.join(base, pasta, str(ano), slug + ".md"),
        os.path.join(base, "_fonte", pasta, str(ano), slug + ".html.gz"),
    )


def gravar(md_path, fonte_path, html_bruto, meta, corpo_md):
    """Grava o HTML bruto (gzip) e o .md com front matter. `meta` é uma lista de pares (chave, valor)."""
    os.makedirs(os.path.dirname(fonte_path), exist_ok=True)
    with gzip.open(fonte_path, "wb") as f:
        f.write(html_bruto if isinstance(html_bruto, bytes) else html_bruto.encode("utf-8"))
    linhas = ["---"]
    for k, v in meta:
        if isinstance(v, bool):
            linhas.append(f"{k}: {'true' if v else 'false'}")
        elif k == "revogada" and v is None:
            linhas.append("revogada: null")
        elif k == "data" and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v or ""):
            linhas.append(f"{k}: {v}")
        else:
            linhas.append(f"{k}: {yaml_str(v)}")
    linhas += [f"baixado_em: {dt.date.today().isoformat()}", "---", ""]
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    tmp = md_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas) + corpo_md)
    os.replace(tmp, md_path)


def html_para_md(html, remover_inicio=()):
    """Converte e remove linhas de cabeçalho institucional do início do texto."""
    md = convert(html)
    blocos = md.split("\n\n")

    def descartavel(bloco):
        linhas = [re.sub(r"[*\\\s]+", " ", ln).strip() for ln in bloco.split("\n")]
        return all(ln in remover_inicio for ln in linhas if ln)

    while blocos and remover_inicio and descartavel(blocos[0]):
        blocos = blocos[1:]
    return "\n\n".join(blocos)


def executar(uf, itens, processar, workers=4):
    """Roda `processar(item)` em paralelo. processar retorna ("ok"|"pulado"|"sem_texto", extra|None)."""
    os.makedirs(os.path.join(RAIZ_ESTADUAIS, uf), exist_ok=True)
    falhas_path = os.path.join(RAIZ_ESTADUAIS, uf, "_falhas.jsonl")
    cont = collections.Counter({"ok": 0, "pulado": 0, "sem_texto": 0, "erro": 0})
    inicio = time.time()
    with ThreadPoolExecutor(workers) as ex, open(falhas_path, "a", encoding="utf-8") as falhas:
        futs = {ex.submit(processar, it): it for it in itens}
        for n, fut in enumerate(as_completed(futs), 1):
            try:
                status, extra = fut.result()
            except Exception as e:
                status, extra = "erro", {"item": str(futs[fut])[:300], "erro": str(e)[:300]}
            cont[status] += 1
            if extra:
                extra["status"] = status
                falhas.write(json.dumps(extra, ensure_ascii=False) + "\n")
                falhas.flush()
            if n % 100 == 0 or n == len(itens):
                taxa = n / max(1, time.time() - inicio)
                print(f"[{uf}] {n}/{len(itens)} {dict(cont)} ~{(len(itens) - n) / max(taxa, 1e-9) / 60:.0f} min restantes", flush=True)
    print(f"[{uf}] FIM {dict(cont)}", flush=True)
    return cont


def imagem_bruta(bruto):
    return (bruto.startswith((b"\xff\xd8\xff", b"\x89PNG\r\n\x1a\n", b"GIF87a", b"GIF89a", b"II*\0", b"MM\0*", b"BM"))
            or bruto[:4] == b"RIFF" and bruto[8:12] == b"WEBP")


def extrair_texto(bruto, url="", content_type=""):
    """Retorna (html, texto): PDF -> pdftotext; imagem -> OCR; DOC/DOCX/ODT/RTF -> textutil; HTML direto."""
    ext = os.path.splitext(url.split("?")[0])[1].lower()
    if imagem_bruta(bruto):
        return None, ocr_imagem(bruto)[0]
    if bruto[:4] == b"%PDF":
        with tempfile.TemporaryDirectory() as tmp:
            pdf = os.path.join(tmp, "a.pdf")
            open(pdf, "wb").write(bruto)
            r = subprocess.run(["pdftotext", "-q", "-layout", "-enc", "UTF-8", pdf, "-"], capture_output=True, timeout=300)
            texto = r.stdout.decode("utf-8", "replace")
        return None, texto
    if ext in (".doc", ".docx", ".odt", ".rtf") or bruto[:2] == b"PK" or bruto[:5] == b"{\\rtf" or bruto.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "a" + (".doc" if bruto.startswith(b"\xd0\xcf\x11\xe0") else ext or ".doc"))
            open(src, "wb").write(bruto)
            r = subprocess.run(["textutil", "-convert", "html", "-stdout", src], capture_output=True, timeout=300)
            return r.stdout.decode("utf-8", "replace"), None
    return decodificar(bruto, content_type), None


# Preposições e artigos nunca fecham um dispositivo; "e"/"ou" ficam de fora porque terminam incisos.
FIM_CONECTIVO = re.compile(r"\s(?:a|à|ao|o|as|os|da|de|do|das|dos|na|no|nas|nos|em|com|pela|pelo)$")


def texto_pdf_para_md(texto):
    """Reconstrói parágrafos de texto extraído de PDF e marca artigos/títulos."""
    # cabeçalhos/rodapés: linhas que se repetem em mais da metade das páginas
    paginas = [p for p in texto.split("\f") if p.strip()]
    repetidas = set()
    if len(paginas) >= 2:
        freq = collections.Counter(ln for p in paginas for ln in {re.sub(r"\s+", " ", x).strip() for x in p.split("\n")} if ln)
        repetidas = {ln for ln, c in freq.items() if c > len(paginas) / 2 and not re.match(r"^(Art|§)", ln)}
    # fios decorativos (____ ou ----); as reticências de emendas ("Art. 5º .....") ficam
    linhas = [re.sub(r"_{5,}|[-–—=]{8,}", " ", ln).strip() for ln in texto.replace("\f", "\n").split("\n")]
    linhas = ["" if re.sub(r"\s+", " ", ln) in repetidas or re.fullmatch(r"\d{1,3}", ln) else ln for ln in linhas]
    paras, atual = [], []
    inicio_bloco = re.compile(
        r"^(Art\.? ?\d|§ ?\d|Parágrafo único|[IVXLC]+ ?[-–—]|[a-z]\) |TÍTULO|CAPÍTULO|SEÇÃO|SUBSEÇÃO|LIVRO|ANEXO|"
        r"LEI |LEI COMPLEMENTAR|EMENDA|DECRETO|O GOVERNADOR|A GOVERNADORA|O PRESIDENTE|A MESA)", re.I
    )
    for ln in linhas:
        if not ln:
            if atual:
                paras.append(" ".join(atual))
                atual = []
            continue
        # citação quebrada na linha ("nos termos da / Lei nº 16.301…") continua a frase
        if atual and inicio_bloco.match(ln) and not FIM_CONECTIVO.search(atual[-1]):
            paras.append(" ".join(atual))
            atual = []
        atual.append(re.sub(r"\s{2,}", " ", ln))
    if atual:
        paras.append(" ".join(atual))
    out = []
    for p in paras:
        lvl = next((lv for rx, lv in HEADINGS if rx.match(p)), None)
        if lvl and len(p) < 200:
            out.append("#" * lvl + " " + p)
            continue
        m = LABEL.match(p)
        p = p.replace("*", "\\*").replace("_", "\\_")
        if m:
            p = f"**{m.group(1)}**{p[len(m.group(1)):]}"
        out.append(p)
    return "\n\n".join(out) + "\n"


OCR_BIN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin", "ocr")
_ocr_vagas = threading.Semaphore(2)  # OCR é pesado: no máximo 2 simultâneos por processo
AVISO_OCR = "> Texto obtido por OCR a partir de PDF escaneado; pode conter erros de reconhecimento.\n\n"
AVISO_OCR_IMAGEM = "> Texto obtido por OCR a partir de imagem; pode conter erros de reconhecimento.\n\n"
AVISO_SEM_TEXTO = ("> A fonte oficial não disponibiliza o texto desta norma: o documento servido "
                   "está vazio. Só os metadados foram preservados.\n\n")


def ocr_pdf(bruto):
    """OCR com o Vision do macOS (scripts/bin/ocr, compilado de ocr.swift)."""
    if not os.path.exists(OCR_BIN):
        return ""
    with _ocr_vagas, tempfile.TemporaryDirectory() as tmp:
        pdf = os.path.join(tmp, "a.pdf")
        open(pdf, "wb").write(bruto)
        r = subprocess.run([OCR_BIN, pdf], capture_output=True, timeout=1800)
        return r.stdout.decode("utf-8", "replace")


def ocr_imagem(bruto):
    programa = shutil.which("tesseract")
    dados = os.path.join(os.path.dirname(OCR_BIN), "tessdata")
    modelo = os.path.join(dados, "por.traineddata")
    aprovado = "711de9dbb8052067bd42f16b9119967f30bada80d57e2ef24f65d09f531adb04"
    if programa and os.path.isfile(modelo):
        with open(modelo, "rb") as f:
            confere = hashlib.sha256(f.read()).hexdigest() == aprovado
        if confere:
            try:
                with _ocr_vagas:
                    r = subprocess.run([programa, "stdin", "stdout", "--tessdata-dir", dados,
                                        "-l", "por", "--oem", "1", "--psm", "3"], input=bruto,
                                       capture_output=True, timeout=180, env={**os.environ, "OMP_THREAD_LIMIT": "1"})
                texto = r.stdout.decode("utf-8", "replace")
                if r.returncode == 0 and len(re.sub(r"\W", "", texto)) >= 80:
                    return texto, "Tesseract, português, tessdata_best"
            except (OSError, subprocess.TimeoutExpired):
                pass
    return ocr_pdf(bruto), "Vision do macOS"


def pdf_escaneado(texto):
    """Pouco texto por página = PDF de imagem (às vezes só com um carimbo ou cabeçalho em texto)."""
    paginas = max(1, len([p for p in texto.split("\f") if p.strip()]))
    return len(re.sub(r"\W", "", texto)) / paginas < 300


def documento_para_md(bruto, url="", content_type="", remover_inicio=()):
    """Converte um documento baixado (HTML, PDF, DOC...) em Markdown. Retorna (corpo, None) ou (None, motivo)."""
    if b"\0" in bruto[:4096] and not (imagem_bruta(bruto) or bruto.startswith(
            (b"%PDF", b"\xd0\xcf\x11\xe0", b"PK", b"\xff\xfe", b"\xfe\xff"))):
        return None, "formato binário não reconhecido; arquivo oficial possivelmente corrompido"
    motor_imagem = ""
    if imagem_bruta(bruto):
        texto, motor_imagem = ocr_imagem(bruto)
        html = None
    else:
        html, texto = extrair_texto(bruto, url, content_type)
    if texto is not None:
        aviso = AVISO_OCR_IMAGEM.replace("imagem;", f"imagem ({motor_imagem});") if motor_imagem else ""
        if not imagem_bruta(bruto) and pdf_escaneado(texto):
            texto_ocr = ocr_pdf(bruto)
            if len(re.sub(r"\W", "", texto_ocr)) > len(re.sub(r"\W", "", texto)):
                texto, aviso = texto_ocr, AVISO_OCR
        corpo = texto_pdf_para_md(texto)
        if len(re.sub(r"\W", "", corpo)) < 80:
            return None, "imagem sem texto legível por OCR" if imagem_bruta(bruto) else "PDF sem texto legível (nem por OCR)"
        if len(corpo) < 1500 and re.search(r"não consta do acervo|não foi encontrada nos acervos", corpo, re.I):
            return None, "a fonte informa que o texto não está no acervo"
        return aviso + corpo, None
    corpo = html_para_md(html, remover_inicio)
    if len(re.sub(r"\W", "", corpo)) < 40:
        return None, "documento vazio"
    return corpo, None
