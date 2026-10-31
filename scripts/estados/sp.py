"""São Paulo — ALESP.

Índice: legislacao_normas.zip do Portal de Dados Abertos da ALESP (atualizado diariamente, desde 1835).
Metadados e links do texto: API baleg (https://baleg-api-prd.al.sp.gov.br/norma/{id}).
Texto: HTML do repositório da ALESP (versão atualizada quando existe).
"""
import io
import json
import os
import sys
import xml.etree.ElementTree as ET
import zipfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from comum import RAIZ_ESTADUAIS, Rede, caminhos, documento_para_md, executar, gravar  # noqa: E402

UF = "SP"
INDICE_URL = "https://www.al.sp.gov.br/repositorioDados/legislacao/legislacao_normas.zip"
API = "https://baleg-api-prd.al.sp.gov.br/norma/{}"
# IdTipo da ALESP -> (pasta, nome, prefixo). O XML do índice só traz o IdTipo; os rótulos foram
# confirmados um a um na API baleg. Os seis primeiros prefixos já estão gravados e não mudam.
# Fora ficam Ato da Mesa (21), Ato do Presidente (22) e Decisão da Mesa (12): são atos internos de
# administração da Casa, não norma.
TIPOS = {
    "59": ("constituicao", "Constituição Estadual", "ce"),
    "55": ("emendas-constitucionais", "Emenda Constitucional", "ec"),
    "2": ("leis-complementares", "Lei Complementar", "lc"),
    "9": ("leis-ordinarias", "Lei Ordinária", "lei"),
    "25": ("decretos-lei", "Decreto-Lei", "dl"),
    "1": ("decretos-lei-complementares", "Decreto-Lei Complementar", "dlc"),
    "3": ("decretos", "Decreto", "dec"),
    "28": ("decretos-legislativos", "Decreto Legislativo", "dlg"),
    "14": ("resolucoes", "Resolução", "res"),
    "19": ("resolucoes", "Resolução", "res-alesp"),
}
CABECALHO = {"Assembleia Legislativa do Estado de São Paulo", "Ficha informativa",
    "Assembleia Legislativa do Estado de São Paulo Ficha informativa"}
rede = Rede(rps=4)


def indice(refazer=False):
    pasta = os.path.join(RAIZ_ESTADUAIS, UF, "_indice")
    os.makedirs(pasta, exist_ok=True)
    arq = os.path.join(pasta, "legislacao_normas.zip")
    if not os.path.exists(arq) or refazer:
        st, dados, _ = rede.get(INDICE_URL, timeout=600)
        if st != 200:
            sys.exit(f"índice indisponível: HTTP {st}")
        with open(arq, "wb") as f:
            f.write(dados)
    itens = {}
    with zipfile.ZipFile(arq) as z, z.open(z.namelist()[0]) as f:
        for _, el in ET.iterparse(f):
            if el.tag == "LegislacaoNorma":
                if el.findtext("IdTipo") in TIPOS:
                    norma = {c.tag: (c.text or "") for c in el}
                    itens[norma["IdNorma"]] = norma
                el.clear()
    return list(itens.values())


def processar(n):
    pasta, nome, prefixo = TIPOS[n["IdTipo"]]
    ano, mes, dia = n["Data"][:10].split("-")
    if pasta == "constituicao" and int(ano) < 1988:
        pasta = "constituicoes-historicas"
    slug = f"{prefixo}-{n['Numero'] or 'sn'}-{ano}-{mes}-{dia}-id{n['IdNorma']}"
    md, fonte = caminhos(UF, pasta, ano, slug)
    if os.path.exists(md):
        return "pulado", None
    st, dados, _ = rede.get(API.format(n["IdNorma"]), "application/json")
    if st != 200 or not dados:
        return "sem_texto", {"id": n["IdNorma"], "http": st, "motivo": "api"}
    info = json.loads(dados)
    url = info.get("urlIntegraAtualizada") or info.get("urlTextoAtualizado") or info.get("urlIntegraOriginal")
    if not url:
        return "sem_texto", {"id": n["IdNorma"], "motivo": "sem link de texto"}
    url = url.replace(" ", "%20")
    st, bruto, ctype = rede.get(url, "text/html")
    if st != 200 or not bruto:
        return "sem_texto", {"id": n["IdNorma"], "url": url, "http": st}
    corpo, motivo = documento_para_md(bruto, url, ctype, CABECALHO)
    if corpo is None:
        return "sem_texto", {"id": n["IdNorma"], "url": url, "motivo": motivo}
    titulo = info.get("nomeNorma") or f"{nome} nº {n['Numero']}"
    situacao = info.get("dsSituacao") or ""
    meta = [
        ("titulo", titulo),
        ("uf", UF),
        ("tipo", nome),
        ("numero", info.get("nuNorma") or n["Numero"]),
        ("data", f"{ano}-{mes}-{dia}"),
        ("ementa", " ".join((info.get("dsEmenta") or n.get("Ementa") or "").split())),
        ("situacao", situacao),
        ("revogada", {"revogada": True, "revogado": True, "vigente": False, "em vigor": False}.get(situacao.strip().lower())),
        ("versao_texto", "original" if url == (info.get("urlIntegraOriginal") or "").replace(" ", "%20") else "atualizada"),
        ("publicacao", info.get("nomePublicacaoDO") or ""),
        ("fonte", f"https://www.al.sp.gov.br/norma/{n['IdNorma']}"),
    ]
    gravar(md, fonte, bruto, meta, f"# {titulo}\n\n{corpo}")
    return "ok", None


if __name__ == "__main__":
    itens = indice(refazer="--refazer" in sys.argv)
    itens.sort(key=lambda n: n["Data"], reverse=True)
    print(f"[{UF}] {len(itens)} normas no índice", flush=True)
    limite = [a for a in sys.argv[1:] if a.isdigit()]
    if limite:
        itens = itens[: int(limite[0])]
    executar(UF, itens, processar)
