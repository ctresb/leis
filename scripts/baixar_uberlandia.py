"""Uberlândia (MG) — Diário Oficial do Município, texto integral em HTML (plataforma Dynamika).

`diario.uberlandia.mg.gov.br` serve cada publicação como página HTML: título, data de
veiculação, edição, órgão e o corpo do ato. Não há PDF, captcha nem WAF no caminho, e o
`robots.txt` libera tudo. A cobertura é a das edições que o portal guarda — a plataforma nova
substituiu o portal antigo em 2026 e só lista as edições publicadas nela.

A categoria de cada publicação já vem na página da edição, então só as categorias pedidas são
buscadas uma a uma; o que a edição não informa é buscado e decidido pela página do documento.

As outras duas rotas de Uberlândia não entram, e o motivo fica registrado para quem tentar:
a Câmara mantém o índice histórico (19.012 normas no OpenLegis/SAGL, metadados em
`normas_table_json` e `@@normas/<cod>`), mas o texto integral só sai em PDF atrás de captcha
(`@@documento_publico_gate_api`); o portal antigo da prefeitura, com os diários de anos
anteriores, responde 403 do Akamai.

    python3 -I scripts/baixar_uberlandia.py                  # edições disponíveis
    python3 -I scripts/baixar_uberlandia.py --listar         # só mostra o que acharia
    python3 -I scripts/baixar_uberlandia.py --categorias "Lei Ordinária,Lei Complementar"
"""
import argparse
import datetime as dt
import gzip
import hashlib
import html as htmllib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import Rede, canonico, html_para_md, normalizar_chave, slugify, yaml_str  # noqa: E402

MUNICIPIO = "Uberlândia"
UF = "MG"
BASE = "https://diario.uberlandia.mg.gov.br"
RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "municipais"))
FONTE = os.path.join(RAIZ, "_fonte", "uberlandia")
FALHAS = os.path.join(RAIZ, "_falhas.jsonl")
rede = Rede(rps=2, headers={"Accept-Language": "pt-BR"})

# Categoria como o DOM a escreve, já normalizada por comum.normalizar_chave, -> chave de
# comum.CANONICO. Categoria fora do mapa é ignorada, para não inventar pasta fora do vocabulário.
CATEGORIAS = {
    "lei ordinaria": "lei ordinaria",
    "lei complementar": "lei complementar",
    "decreto": "decreto",
    "decreto s n": "decreto nao numerado",
    "resolucao": "resolucao",
    "instrucao normativa": "instrucao normativa",
    "portaria": "portaria",
}
PADRAO = ("lei ordinaria", "lei complementar", "decreto", "resolucao")
MESES = {"janeiro": 1, "fevereiro": 2, "marco": 3, "abril": 4, "maio": 5, "junho": 6, "julho": 7,
         "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}
DATA_EXTENSO = re.compile(r"(\d{1,2})\s+DE\s+([A-ZÁÂÃÀÉÊÍÓÔÕÚÇ]+)\s+DE\s+(\d{4})", re.I)
NUMERO = re.compile(r"N[º°O]\s*([\d.]+)", re.I)
# Bloco de uma edição na listagem e de uma publicação dentro da edição: mesma marcação, com ou
# sem atributos entre a classe e o data-key.
BLOCO = re.compile(r'class="box-publicacao"[^>]*data-key="(\d+)">(.*?)'
                   r'(?=class="box-publicacao"|$)', re.S)
ROTULO_EDICAO = re.compile(r"<h4[^>]*>\s*([^<]+?)\s*</h4>")
DATA_SIMPLES = re.compile(r"(\d{1,2} de [A-Za-zçãéêíóôõúÁÂÃÀÉÊÍÓÔÕÚ]+ de \d{4})")
CATEGORIA_BLOCO = re.compile(r"Categoria:\s*([^<]+)")
# O portal emite um token CSRF por requisição, então os bytes crus nunca se repetem: o hash e o
# original arquivado usam o HTML com o valor do token neutralizado, para que `sha256sum` do
# arquivo bata com `sha256_fonte`.
CSRF = re.compile(rb'(name="csrf-token" content=")[^"]*')
DOC_LINK = re.compile(r"/documento/view/(\d+)/([a-z0-9-]+)")
TITULO = re.compile(r"<h2[^>]*>\s*<strong>(.*?)</strong>", re.S)


def texto(bruto):
    return " ".join(htmllib.unescape(re.sub(r"<[^>]+>", " ", bruto)).split())


def data_extenso(expr):
    """'19 de outubro de 2026' -> '2026-10-19'; None quando o mês não é reconhecido."""
    m = re.search(r"(\d{1,2}) de ([\wçãéêíóôõúáâãà]+) de (\d{4})", expr, re.I)
    if not m:
        return None
    mes = normalizar_chave(m.group(2))
    if mes not in MESES:
        return None
    try:
        return dt.date(int(m.group(3)), MESES[mes], int(m.group(1))).isoformat()
    except ValueError:
        return None


def edicoes(limite_paginas=40):
    """[(id, número, data)] das edições listadas, mais recentes primeiro."""
    saida, vistos = [], set()
    for pagina in range(limite_paginas):
        st, bruto, _ = rede.get(f"{BASE}/diario-oficial/index?page={pagina}")
        if st != 200 or not bruto:
            raise RuntimeError(f"listagem de edições HTTP {st}")
        pagina_html = bruto.decode("utf-8", "replace")
        achou = False
        for m in BLOCO.finditer(pagina_html):
            ident, bloco = m.group(1), m.group(2)
            if ident in vistos:
                continue
            vistos.add(ident)
            achou = True
            rotulo = ROTULO_EDICAO.search(bloco)
            data = DATA_SIMPLES.search(bloco)
            saida.append((ident, rotulo.group(1) if rotulo else "",
                          data_extenso(data.group(1)) if data else None))
        if not achou:
            break
    if not saida:
        raise RuntimeError("listagem de edições vazia: layout do portal mudou ou acesso bloqueado")
    return saida


def publicacoes_da_edicao(ident):
    """[(id_documento, slug, categoria, título)] das publicações da edição, na ordem que aparecem."""
    st, bruto, _ = rede.get(f"{BASE}/diario-oficial/view/{ident}")
    if st != 200 or not bruto:
        raise RuntimeError(f"edição {ident} HTTP {st}")
    pagina = bruto.decode("utf-8", "replace")
    vistos, saida = set(), []
    for m in BLOCO.finditer(pagina):
        codigo, bloco = m.group(1), m.group(2)
        link = DOC_LINK.search(bloco)
        if not link or codigo in vistos:
            continue
        vistos.add(codigo)
        categoria = CATEGORIA_BLOCO.search(bloco)
        titulo = ROTULO_EDICAO.search(bloco)
        saida.append((codigo, link.group(2), categoria.group(1).strip() if categoria else "",
                      texto(titulo.group(1)) if titulo else ""))
    if not saida:
        raise RuntimeError(f"edição {ident} sem publicações reconhecidas: layout do portal mudou")
    return saida


def campo(pagina, rotulo):
    m = re.search(rf"{rotulo}:\s*</strong>\s*([^<]*)", pagina)
    return texto(m.group(1)) if m else ""


def corpo(pagina):
    """Markdown do ato: o texto vem depois do bloco de impressão/compartilhamento da página."""
    corte = max(pagina.find(".modal -->"), pagina.find('id="divImpressao"'))
    if corte < 0:
        raise RuntimeError("bloco de impressão ausente: layout da página do documento mudou")
    trecho = pagina[corte:]
    if "<hr />" in trecho:
        trecho = trecho[trecho.find("<hr />") + 6:]
    fim = trecho.find('<div class="col-12 col-lg-4 dontPrint">')
    if fim > 0:
        trecho = trecho[:fim]
    trecho = re.sub(r"<script.*?</script>|<style.*?</style>", "", trecho, flags=re.S)
    return re.sub(r"\n{3,}", "\n\n", html_para_md(trecho).strip())


def ler(codigo, slug, data_edicao):
    """(metadados, html) da publicação; metadados é None quando não é norma ou o texto não veio."""
    st, bruto, _ = rede.get(f"{BASE}/documento/view/{codigo}/{slug}")
    if st != 200 or not bruto:
        raise RuntimeError(f"documento {codigo} HTTP {st}")
    pagina = bruto.decode("utf-8", "replace")
    categoria = campo(pagina, "Categoria")
    chave = CATEGORIAS.get(normalizar_chave(categoria))
    if not chave:
        raise RuntimeError(f"categoria fora do mapa no documento: {categoria!r}")
    achado = TITULO.search(pagina)
    titulo = texto(achado.group(1)) if achado else ""
    if not titulo:
        raise RuntimeError(f"documento {codigo} sem título reconhecível")
    corpo_md = corpo(pagina)
    if len(corpo_md) < 80:
        return None, bruto
    epigrafe = DATA_EXTENSO.search(titulo)
    data = data_extenso(epigrafe.group(0)) if epigrafe else None
    publicacao = campo(pagina, "Data de Veiculação")
    data_publicacao = data_extenso(publicacao) or data_edicao or ""
    numero = NUMERO.search(titulo)
    return {
        "chave": chave,
        "titulo": titulo,
        "numero": numero.group(1).replace(".", "") if numero else "",
        "data": data or data_publicacao,
        "ano": (data or data_publicacao)[:4],
        "data_publicacao": data_publicacao,
        "publicacao": campo(pagina, "Publicado Em"),
        "orgao": campo(pagina, "Orgão/Secretaria"),
        "corpo": corpo_md,
        "fonte": f"{BASE}/documento/view/{codigo}/{slug}",
        "id": codigo,
    }, bruto


def fonte_limpa(bruto):
    """HTML sem o valor do token CSRF: é isso que se arquiva e se resume em hash."""
    return CSRF.sub(rb"\1", bruto if isinstance(bruto, bytes) else bruto.encode("utf-8"))


def hash_fonte(bruto):
    return hashlib.sha256(fonte_limpa(bruto)).hexdigest()


def gravar(doc, sha_fonte):
    """Grava o .md canônico. Devolve "novo", "pulado" ou "divergente"."""
    pasta, tipo = canonico(doc["chave"])
    slug = slugify(f"{doc['chave']}-{doc['numero'] or 'sn'}-{doc['ano']}-dom-{doc['id']}")[:110]
    md = os.path.join(RAIZ, UF, slugify(normalizar_chave(MUNICIPIO)), pasta, doc["ano"], slug + ".md")
    sha_texto = hashlib.sha256(doc["corpo"].encode()).hexdigest()
    if os.path.exists(md):
        with open(md, encoding="utf-8") as f:
            gravado = f.read()
        esperado = re.search(r'^sha256_texto: "([0-9a-f]{64})"', gravado, re.M)
        return "pulado" if esperado and esperado.group(1) == sha_texto else "divergente"
    cabecalho = [
        "---", f"titulo: {yaml_str(doc['titulo'])}", f"uf: {yaml_str(UF)}",
        f"municipio: {yaml_str(MUNICIPIO)}", f"tipo: {yaml_str(tipo)}",
        f"numero: {yaml_str(doc['numero'])}",
        f"data: {doc['data'] if doc['data'] else yaml_str('')}", f"ano: {yaml_str(doc['ano'])}",
        "revogada: null", 'versao_texto: "publicação original"',
        f"publicacao: {yaml_str(doc['publicacao'])}",
        f"data_publicacao: {doc['data_publicacao']}",
        f"orgao: {yaml_str(doc['orgao'])}", f"fonte: {yaml_str(doc['fonte'])}",
        f"sha256_fonte: {yaml_str(sha_fonte)}", f"sha256_texto: {yaml_str(sha_texto)}",
        f"baixado_em: {dt.date.today().isoformat()}", "---", "",
    ]
    os.makedirs(os.path.dirname(md), exist_ok=True)
    tmp = md + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(cabecalho) + f"# {doc['titulo']}\n\n" + doc["corpo"] + "\n")
    os.replace(tmp, md)
    return "novo"


def guardar_bruto(codigo, dados):
    os.makedirs(FONTE, exist_ok=True)
    destino = os.path.join(FONTE, f"documento-{codigo}.html.gz")
    tmp = destino + ".tmp"
    with gzip.open(tmp, "wb") as f:
        f.write(dados)
    os.replace(tmp, destino)


def registrar_falha(url, erro, status="erro"):
    with open(FALHAS, "a", encoding="utf-8") as f:
        f.write(json.dumps({"assoc": "uberlandia", "status": status, "url": url,
                            "erro": str(erro)[:300]}, ensure_ascii=False) + "\n")


def main():
    p = argparse.ArgumentParser(description="Baixa a legislação municipal de Uberlândia-MG do DOM.")
    p.add_argument("--listar", action="store_true", help="mostra o que seria baixado, sem buscar")
    p.add_argument("--max-edicoes", type=int, default=0, help="limita a coleta às N edições mais recentes")
    p.add_argument("--categorias", default="", help="categorias do DOM separadas por vírgula (padrão: %s)"
                   % ", ".join(PADRAO))
    a = p.parse_args()
    pedidas = [normalizar_chave(c) for c in (a.categorias.split(",") if a.categorias else PADRAO)]
    ignoradas = [c for c in pedidas if c not in CATEGORIAS]
    if ignoradas:
        print(f"[aviso] categorias fora do mapa, ignoradas: {', '.join(ignoradas)}", flush=True)
    desejadas = {CATEGORIAS[c] for c in pedidas if c in CATEGORIAS}
    if not desejadas:
        raise SystemExit("nenhuma categoria reconhecida em --categorias")
    lista = edicoes()
    if a.max_edicoes:
        lista = lista[:a.max_edicoes]
    print(f"{len(lista)} edições disponíveis no portal", flush=True)
    contagem = {"novo": 0, "pulado": 0, "divergente": 0, "listado": 0,
                "fora": 0, "sem_texto": 0, "erro": 0}
    for ident, rotulo, data_edicao in lista:
        url_edicao = f"{BASE}/diario-oficial/view/{ident}"
        try:
            docs = publicacoes_da_edicao(ident)
        except Exception as e:
            contagem["erro"] += 1
            registrar_falha(url_edicao, e)
            print(f"[erro] edição {ident}: {e}", flush=True)
            continue
        for codigo, slug, categoria_edicao, titulo_edicao in docs:
            if categoria_edicao:
                chave_edicao = CATEGORIAS.get(normalizar_chave(categoria_edicao))
                if chave_edicao is None or chave_edicao not in desejadas:
                    contagem["fora"] += 1
                    continue
            if a.listar:
                print(f"  {rotulo} | {categoria_edicao or '(categoria na edição: ?)'} | {titulo_edicao[:70]}")
                contagem["listado"] += 1
                continue
            try:
                doc, bruto = ler(codigo, slug, data_edicao)
            except Exception as e:
                contagem["erro"] += 1
                registrar_falha(f"{BASE}/documento/view/{codigo}/{slug}", e)
                print(f"[erro] {codigo}: {e}", flush=True)
                continue
            if not doc:
                contagem["sem_texto"] += 1
                registrar_falha(f"{BASE}/documento/view/{codigo}/{slug}",
                                "corpo convertido com menos de 80 caracteres", status="sem_texto")
                continue
            if doc["chave"] not in desejadas:
                contagem["fora"] += 1
                continue
            estado = gravar(doc, hash_fonte(bruto))
            contagem[estado] += 1
            if estado == "novo":
                guardar_bruto(codigo, fonte_limpa(bruto))
            elif estado == "divergente":
                registrar_falha(doc["fonte"], "texto convertido diverge do sha256_texto gravado; "
                                "arquivo preservado para reconciliação", status="divergente")
                print(f"[divergente] {codigo}: fonte mudou desde a gravação", flush=True)
    print(json.dumps(contagem, ensure_ascii=False))


if __name__ == "__main__":
    main()
