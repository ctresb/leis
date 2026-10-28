"""Baixa a legislação federal (normas.leg.br) e grava em Markdown.

Índice: listas do Senado em federal/_indice/*.json.
Texto: versão compilada vigente ("Current") quando existe; senão Original antes de Intermediate.
Decretos com apenas errata ou sem artigo próprio ficam pendentes de revisão da íntegra.
Retomável: pula normas cujo .md já existe. HTML bruto fica em federal/_fonte (gzip).

Uso: python3 -I scripts/baixar_federal.py [--limite N] [--tipos LEI,LCP,...] [--workers 4] [--rps 4]
"""
import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
import re
import sys
import threading
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import AVISO_OCR, AVISO_SEM_TEXTO, extrair_texto, ocr_pdf, texto_pdf_para_md  # noqa: E402
from html2md import convert  # noqa: E402
from integridade_html_federal import Visivel
from integridade_anexos_decreto import anexo_proprio_ausente
from identidade_decreto import divergencia_epigrafe_decreto, extrair_epigrafe_decreto  # noqa: E402

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "federal")
RAIZ = os.path.abspath(RAIZ)
UA = "Mozilla/5.0 (compatible; constituicao-md/1.0)"
API_NORMA = "https://normas.leg.br/api/public/normas?urn={}&tipo_documento=maior-detalhe"
API_SENADO = "https://legis.senado.leg.br/dadosabertos/legislacao/{}.json"

# tipo do Senado -> (pasta, prefixo do arquivo, autoridade e tipo na URN LexML, nome legível).
# A autoridade quase sempre é `federal`, mas as resoluções pertencem à Casa que as editou — é o
# que o próprio portal responde: `urn:lex:br:senado.federal:resolucao:2024-12-19;55`. Errar a
# autoridade não perde a norma (há o recuo pela API do Senado, em `obter_metadados`), só gasta uma
# requisição a mais por item.
TIPOS = {
    "LEI-n": ("leis-ordinarias", "lei", "federal", "lei", "Lei Ordinária"),
    "LEI-sn": ("leis-ordinarias", "lei-sn", "federal", "lei", "Lei (não numerada)"),
    "LCP": ("leis-complementares", "lcp", "federal", "lei.complementar", "Lei Complementar"),
    "LDL": ("leis-delegadas", "ldl", "federal", "lei.delegada", "Lei Delegada"),
    "LCT": ("leis-constitucionais", "lct", "federal", "lei.constitucional", "Lei Constitucional"),
    "DEL": ("decretos-lei", "del", "federal", "decreto.lei", "Decreto-Lei"),
    "DEL-mpv": ("decretos-lei", "del", "federal", "decreto.lei", "Decreto-Lei"),
    "EMC-n": ("emendas-constitucionais", "emc", "federal", "emenda.constitucional",
              "Emenda Constitucional"),
    "EMR": ("emendas-constitucionais", "emr", "federal", "emenda.constitucional.revisao",
            "Emenda Constitucional de Revisão"),
    "DEC-n": ("decretos", "dec", "federal", "decreto", "Decreto"),
    "DEC-sn": ("decretos-nao-numerados", "dec-sn", "federal", "decreto", "Decreto (não numerado)"),
    "DLG": ("decretos-legislativos", "dlg", "federal", "decreto.legislativo", "Decreto Legislativo"),
    "DPL-n": ("decretos-legislativos", "dpl", "federal", "decreto.legislativo",
              "Decreto do Poder Legislativo"),
    "MPV-ss": ("medidas-provisorias", "mpv", "federal", "medida.provisoria", "Medida Provisória"),
    "MPV-cs": ("medidas-provisorias", "mpv", "federal", "medida.provisoria", "Medida Provisória"),
    "MPV-n": ("medidas-provisorias", "mpv", "federal", "medida.provisoria", "Medida Provisória"),
    "RSF": ("resolucoes-senado", "rsf", "senado.federal", "resolucao", "Resolução do Senado Federal"),
    "RCN": ("resolucoes-congresso", "rcn", "congresso.nacional", "resolucao",
            "Resolução do Congresso Nacional"),
    "RRC": ("resolucoes-congresso", "rrc", "congresso.nacional", "resolucao",
            "Resolução da Revisão Constitucional"),
}


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


LIMITE = None


def http_get(url, accept="*/*", tentativas=4):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept, "Accept-Encoding": "gzip"})
    ultimo = None
    for n in range(tentativas):
        LIMITE.esperar()
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                dados = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    dados = gzip.decompress(dados)
                return r.status, dados
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 429):
                raise RuntimeError(f"fonte recusou HTTP {e.code}: {url}") from e
            if e.code in (400, 404):
                return e.code, b""
            ultimo = e
        except Exception as e:  # rede, IncompleteRead, timeout
            ultimo = e
        time.sleep(2 * (n + 1) ** 2)
    raise RuntimeError(f"falhou após {tentativas} tentativas: {url}: {ultimo}")


def expandir_tipos(tipos):
    if not tipos:
        return set(TIPOS)
    if isinstance(tipos, str):
        tipos = tipos.split(",")
    selecionados = set()
    for valor in tipos:
        tipo = valor.strip()
        if not tipo:
            raise ValueError("seleção de tipos vazia")
        if tipo in {"LEI", "MPV", "DPL", "EMC", "DEC", "DEL"}:
            selecionados.update(t for t in TIPOS if t == tipo or t.startswith(tipo + "-"))
        elif tipo in TIPOS:
            selecionados.add(tipo)
        else:
            raise ValueError("tipo/alias desconhecido: " + tipo)
    return selecionados


def carregar_indice(tipos):
    selecionados = expandir_tipos(tipos)
    itens = []
    for arq in sorted(os.listdir(os.path.join(RAIZ, "_indice"))):
        if not arq.endswith(".json"):
            continue
        docs = json.load(open(os.path.join(RAIZ, "_indice", arq), encoding="utf-8"))
        docs = docs["ListaDocumento"]["documentos"]["documento"]
        for d in docs if isinstance(docs, list) else [docs]:
            if d["tipo"] not in selecionados:
                continue
            itens.append(d)
    if not itens:
        raise ValueError("seleção de tipos sem documentos no índice oficial")
    return itens


def numero_oficial(d):
    numero = str(d.get("numero") or "")
    if d.get("complemento"):
        numero += "-" + str(d["complemento"]).upper()
    if d.get("reedicao"):
        numero += "-" + str(d["reedicao"])
    return numero


def montar(d):
    pasta, prefixo, autoridade, tipo_urn, nome = TIPOS[d["tipo"]]
    dia, mes, ano = d["dataassinatura"].split("/")
    data = f"{ano}-{mes}-{dia}"
    # as séries "sem número" (lei e decreto não numerados) se identificam pela data mais um
    # sequencial do próprio Senado, que entra na URN como `seq-sf-N`
    if d["tipo"].endswith("-sn") or d["tipo"] == "LEI-sn":
        seq = d.get("sequencia", "0")
        urn = f"urn:lex:br:{autoridade}:{tipo_urn}:{data};seq-sf-{seq}"
        slug = f"{prefixo}-{data}-s{seq}"
    else:
        # medida provisória reeditada: o número oficial carrega a reedição ("1.463-2"), e é assim
        # que ela entra na URN. Antes da EC 32/2001 uma MP podia ser reeditada dezenas de vezes,
        # e cada reedição é uma norma distinta, com texto próprio.
        numero = numero_oficial(d).lower()
        urn = f"urn:lex:br:{autoridade}:{tipo_urn}:{data};{numero}"
        slug = f"{prefixo}-{numero}-{data}"
    md = os.path.join(RAIZ, pasta, ano, slug + ".md")
    fonte = os.path.join(RAIZ, "_fonte", pasta, ano, slug + ".html.gz")
    return {"urn": urn, "slug": slug, "md": md, "fonte": fonte, "data": data, "nome": nome}


class MetadadosFonte(dict):
    pass


def registrar_metadados(urn, bruto):
    sha = hashlib.sha256(bruto).hexdigest()
    pasta = os.path.join(RAIZ, "_fonte", "metadados-normas", hashlib.sha256(urn.encode()).hexdigest())
    os.makedirs(pasta, exist_ok=True)
    path = os.path.join(pasta, sha + ".json.gz")
    if not os.path.exists(path):
        with tempfile.NamedTemporaryFile(dir=pasta, suffix=".tmp", delete=False) as f:
            f.write(gzip.compress(bruto))
            tmp = f.name
        os.replace(tmp, path)
    with gzip.open(path, "rb") as f:
        if hashlib.sha256(f.read()).hexdigest() != sha:
            raise ValueError("captura imutável de metadados corrompida")
    return {"path": path, "sha256": sha}


def obter_metadados(urn, id_senado):
    st, corpo = http_get(API_NORMA.format(urllib.parse.quote(urn, safe=":;@!~$-.")), "application/json")
    meta = MetadadosFonte(json.loads(corpo)) if st == 200 and corpo.strip() else MetadadosFonte()
    if meta.get("legislationIdentifier") == urn:
        meta.captura = registrar_metadados(urn, corpo)
    if meta.get("encoding") and meta.get("legislationIdentifier") == urn:
        return urn, meta
    # URN montada não bateu: pergunta ao Senado qual é a URN oficial
    st, corpo = http_get(API_SENADO.format(id_senado), "application/json")
    if st == 200 and corpo:
        ident = json.loads(corpo)["DetalheDocumento"]["documentos"]["documento"][0]["identificacao"]
        url = ident.get("urlDocumento") or ""
        if "urn=" in url and url.split("urn=", 1)[1] and url.split("urn=", 1)[1] != urn:
            urn2 = urllib.parse.unquote(url.split("urn=", 1)[1])
            st, corpo = http_get(API_NORMA.format(urllib.parse.quote(urn2, safe=":;@!~$-.")), "application/json")
            meta = MetadadosFonte(json.loads(corpo)) if st == 200 and corpo.strip() else MetadadosFonte()
            if meta.get("legislationIdentifier") == urn2:
                meta.captura = registrar_metadados(urn2, corpo)
            return urn2, meta if meta.get("legislationIdentifier") == urn2 else {}
    return urn, meta if meta.get("legislationIdentifier") == urn else {}


def como_lista(v):
    # JSON-LD: um único valor vem como objeto, vários como lista
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def escolher_texto(meta):
    encs = [
        e
        for e in como_lista(meta.get("encoding"))
        if isinstance(e, dict) and e.get("contentUrl") and "html" in (e.get("encodingFormat") or "text/html")
    ]
    if not encs:
        return None
    atual = [e for e in encs if e.get("version") == "Current"]
    if atual:
        return atual[0]
    originais = [e for e in encs if e.get('version') == 'Original']
    if originais:
        return sorted(originais, key=lambda e: e.get('datePublished') or '')[-1]
    return sorted(encs, key=lambda e: e.get("datePublished") or "")[-1]


def motivo_texto_parcial_decreto(tipo, corpo):
    if tipo != "DEC-n":
        return None
    limpo = re.sub(r"[*_`\\]", "", corpo)
    artigo = re.search(r"^\s*(?:Artigo|Art\.?)\s*[.º°o]*\s*(?:\d|[úu]nico)", limpo, re.I | re.M)
    errata = re.search(r"^\s*RETIFICA[ÇC][ÃA]O\s*$", limpo, re.I | re.M)
    # A errata pode estar anexada depois da norma completa. O problema é o
    # documento que começa como retificação, mesmo quando cita um artigo inteiro.
    if errata and (not artigo or errata.start() < artigo.start()):
        return "Documento de retificação avulsa; buscar a versão integral da norma"
    if not artigo:
        return "Sem artigo normativo próprio; íntegra/comando decisório exige revisão específica"
    return None


def yaml_str(v):
    return json.dumps(v if v is not None else "", ensure_ascii=False)


def _e_so_republicacao(md):
    """Arquivo gravado antes da correção que preferia o Original: só a retificação/veto, sem o texto."""
    with open(md, encoding="utf-8") as f:
        cab = f.read(4000)
    return 'versao_texto: "republicação/retificação"' in cab


def processar(d, *, revisao_identidade=False, refazer_republicacao=False):
    """Exige epígrafe própria; modo de revisão só prepara material privado.

    O modo explícito não invalida datas/números completos divergentes e marca
    epígrafes inconclusivas como pendentes. Publicação continua dependente de
    revisão documental complementar, registrada em manifesto separado.
    """
    if revisao_identidade and '_fonte/auditorias/' not in os.path.abspath(RAIZ).replace(os.sep, '/'):
        raise ValueError('Revisão de identidade só pode gravar em área de auditoria, nunca na raiz publicável')
    info = montar(d)
    if os.path.exists(info["md"]) and not (refazer_republicacao and _e_so_republicacao(info["md"])):
        return "pulado", info["slug"], None
    urn, meta = obter_metadados(info["urn"], d["id"])
    if urn != info["urn"]:
        return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn,
                                           "urn_esperada": info["urn"], "motivo": "URN oficial divergente; equivalência requer revisão"}
    enc = escolher_texto(meta)
    if not enc:
        return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn}

    url = enc["contentUrl"].replace("/api/binario/", "/api/public/binario/")
    st, html = http_get(url, "text/html")
    if st != 200 or not html:
        return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn, "url": url, "http": st}

    os.makedirs(os.path.dirname(info["fonte"]), exist_ok=True)
    with gzip.open(info["fonte"], "wb") as f:
        f.write(html)

    # Algumas publicações vêm em PDF apesar do encoding anunciado como HTML pela API.
    if html.startswith(b"%PDF"):
        _, texto = extrair_texto(html, url)
        if not re.search(r"\bArt\.?\s*\d", texto, re.I):
            reconhecido = ocr_pdf(html)
            if re.search(r"\bArt\.?\s*\d", reconhecido, re.I):
                texto = reconhecido
                corpo = AVISO_OCR + texto_pdf_para_md(texto)
            else:
                return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn,
                                                   "url": url, "motivo": "PDF sem corpo normativo extraível; OCR não recuperou artigos"}
        else:
            corpo = texto_pdf_para_md(texto)
    else:
        html_texto = html.decode("utf-8")
        corpo = convert(html_texto)
        if d["tipo"] == "DEC-n":
            parsed = Visivel()
            parsed.feed(html_texto)
            ausente = anexo_proprio_ausente(corpo, parsed)
            if parsed.visual or ausente:
                return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn,
                    "url": url, "motivo": "Conteúdo visual exige validação" if parsed.visual else "Anexo próprio ausente do HTML",
                    "elementos_visuais": parsed.visual, "evidencia_anexo": ausente}
    if not corpo.strip() or "\x00" in corpo:
        return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn,
                                           "url": url, "motivo": "corpo vazio ou contém NUL; fonte preservada"}
    parcial = motivo_texto_parcial_decreto(d["tipo"], corpo)
    if parcial:
        return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn,
                                           "url": url, "motivo": parcial}
    epigrafe_pendente = d["tipo"] == "DEC-n" and not extrair_epigrafe_decreto(corpo)
    if epigrafe_pendente and not revisao_identidade:
        return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn,
            "url": url, "motivo": "Epígrafe própria inconclusiva; identidade exige revisão documental explícita"}
    divergencia = divergencia_epigrafe_decreto(d["tipo"], numero_oficial(d), info["data"], corpo)
    if divergencia:
        return "sem_texto", info["slug"], {"id": d["id"], "norma": d["norma"], "urn": urn,
                                           "url": url, **divergencia}
    versao = {"Current": "compilada (texto vigente)", "Original": "original", "Intermediate": "republicação/retificação"}
    forca = como_lista(meta.get("legislationLegalForce"))
    revogada = False if forca == ["InForce"] else None
    with gzip.open(meta.captura["path"], "rb") as f:
        metadados_brutos = f.read()
    if hashlib.sha256(metadados_brutos).hexdigest() != meta.captura["sha256"]:
        raise ValueError("hash da captura de metadados diverge da resposta associada")
    cab = [
        "---",
        f"titulo: {yaml_str(d['normaNome'].strip())}",
        f"tipo: {yaml_str(info['nome'])}",
        f"numero: {yaml_str(numero_oficial(d))}",
        f"data: {info['data']}",
        f"ementa: {yaml_str((d.get('ementa') or '').strip())}",
        f"revogada: {'false' if revogada is False else 'null'}",
        f"forca_legal_fonte: {yaml_str(json.dumps(forca, ensure_ascii=False))}",
        f"fonte_metadados: {yaml_str(API_NORMA.format(urllib.parse.quote(urn, safe=':;@!~$-.')))}",
        f"sha256_metadados_fonte: {yaml_str(hashlib.sha256(metadados_brutos).hexdigest())}",
        f"versao_texto: {yaml_str(versao.get(enc.get('version'), enc.get('version')))}",
        f"urn: {yaml_str(urn)}",
        f"fonte: {yaml_str('https://normas.leg.br/?urn=' + urn)}",
        f"baixado_em: {dt.date.today().isoformat()}",
        "---",
        "",
    ]
    if epigrafe_pendente:
        cab.insert(-2, 'identidade_pendente_revisao: true')
    os.makedirs(os.path.dirname(info["md"]), exist_ok=True)
    tmp = info["md"] + ".tmp"
    # o corpo começa pelo título em H1, como nos arquivos estaduais
    titulo = d["normaNome"].strip()
    # o portal às vezes serve um documento vazio (só um espaço). Guarda os metadados e diz por quê.
    aviso = "" if corpo.strip() else AVISO_SEM_TEXTO
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(cab) + f"# {titulo}\n\n" + aviso + corpo)
    os.replace(tmp, info["md"])
    return "ok", info["slug"], None


def completar_numeros(aplicar=False):
    import hashlib
    mudancas, conflitos = [], []
    for d in carregar_indice(set()):
        if not d.get("complemento") and not d.get("reedicao"):
            continue
        info = montar(d)
        if not os.path.exists(info["md"]):
            continue
        bruto = open(info["md"], "rb").read()
        partes = bruto.split(b"---", 2)
        if len(partes) != 3:
            conflitos.append({"arquivo": info["md"], "motivo": "frontmatter ausente"})
            continue
        cab = partes[1].decode("utf-8")
        urn = re.search(r"^urn:\s*(.+)$", cab, re.M)
        numero = re.search(r"^numero:\s*(.+)$", cab, re.M)
        if not urn or not numero or json.loads(urn[1]) != info["urn"]:
            conflitos.append({"arquivo": info["md"], "urn_esperada": info["urn"], "motivo": "URN não confere com índice"})
            continue
        atual = str(json.loads(numero[1]))
        esperado = numero_oficial(d)
        if atual == esperado:
            continue
        sha = hashlib.sha256(partes[2]).hexdigest()
        registro = {"arquivo": os.path.relpath(info["md"], RAIZ), "id_senado": d["id"], "urn": info["urn"],
                    "numero_anterior": atual, "numero_oficial": esperado, "complemento": d.get("complemento", ""),
                    "reedicao": d.get("reedicao", ""), "sha256_corpo": sha}
        mudancas.append(registro)
        if aplicar:
            partes[1] = re.sub(r"^numero:.*$", lambda _: "numero: " + yaml_str(esperado), cab, count=1, flags=re.M).encode()
            tmp = info["md"] + ".tmp"
            open(tmp, "wb").write(b"---".join(partes))
            os.replace(tmp, info["md"])
            assert hashlib.sha256(open(info["md"], "rb").read().split(b"---", 2)[2]).hexdigest() == sha
    resultado = {"aplicado": aplicar, "criterio": "URN exata do índice oficial; altera apenas numero no frontmatter",
                 "mudancas": mudancas, "conflitos": conflitos}
    if aplicar:
        destino = os.path.join(RAIZ, "_fonte", "auditorias", "numeros-completados-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".json.gz")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with gzip.open(destino, "wb") as f:
            f.write(json.dumps(resultado, ensure_ascii=False, indent=2).encode())
    else:
        destino = "/tmp/constituicao-numeros-manifesto.json"
        with open(destino, "w", encoding="utf-8") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=2)
    print("Números", len(mudancas), "conflitos", len(conflitos), "aplicado", aplicar, "manifesto", destino, flush=True)
    return int(bool(conflitos))


def main():
    global LIMITE
    ap = argparse.ArgumentParser()
    ap.add_argument("--auditar-numeros", action="store_true")
    ap.add_argument("--completar-numeros", action="store_true")
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--tipos", default=None)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--rps", type=float, default=4)
    ap.add_argument("--refazer-republicacao", action="store_true",
                    help="regrava arquivos com versao_texto republicação/retificação usando Original/Current")
    ap.add_argument("--amostra", default="", help="lista de normas do Senado (ex.: LEI-10406-2002-01-10,...)")
    a = ap.parse_args()
    if not 0 < a.rps <= 4 or a.workers <= 0:
        ap.error("rps deve estar entre0 e4; workers deve ser positivo")
    try:
        tipos = set(a.tipos.split(",")) if a.tipos is not None else set()
        expandir_tipos(tipos)
    except ValueError as exc:
        ap.error(str(exc))
    if a.auditar_numeros or a.completar_numeros:
        return completar_numeros(a.completar_numeros)
    LIMITE = Limitador(a.rps)

    try:
        itens = carregar_indice(tipos)
    except ValueError as exc:
        ap.error(str(exc))
    if a.amostra:
        alvo = set(a.amostra.split(","))
        itens = [d for d in itens if d["norma"] in alvo]
    # mais recentes primeiro: são as mais consultadas
    itens.sort(key=lambda d: d["dataassinatura"][6:] + d["dataassinatura"][3:5] + d["dataassinatura"][:2], reverse=True)
    if a.limite:
        itens = itens[: a.limite]

    falhas_path = os.path.join(RAIZ, "_falhas.jsonl")
    cont = {"ok": 0, "pulado": 0, "sem_texto": 0, "erro": 0}
    inicio = time.time()
    with ThreadPoolExecutor(a.workers) as ex, open(falhas_path, "a", encoding="utf-8") as falhas:
        futs = {ex.submit(processar, d, refazer_republicacao=a.refazer_republicacao): d for d in itens}
        for n, fut in enumerate(as_completed(futs), 1):
            d = futs[fut]
            try:
                status, slug, extra = fut.result()
            except Exception as e:
                status, slug, extra = "erro", d["norma"], {"id": d["id"], "norma": d["norma"], "erro": str(e)[:300]}
            cont[status] += 1
            if extra:
                extra["status"] = status
                falhas.write(json.dumps(extra, ensure_ascii=False) + "\n")
                falhas.flush()
            if n % 50 == 0 or n == len(itens):
                taxa = n / max(1, time.time() - inicio)
                resta = (len(itens) - n) / max(taxa, 1e-9)
                print(f"{n}/{len(itens)} {cont} ~{resta / 60:.0f} min restantes", flush=True)
    print("FIM", cont, flush=True)


if __name__ == "__main__":
    sys.exit(main())
