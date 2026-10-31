"""Goiás — Legisla Goiás (Casa Civil, legisla.casacivil.go.gov.br).

Índice: /api/v2/pesquisa/legislacoes?tipo_legislacao=N (15 por página).
Texto: campo `conteudo` (HTML) do detalhe /api/v2/pesquisa/legislacoes/{id}.

  python3 -I scripts/estados/go.py              # índice (em cache) e baixa o que falta
  python3 -I scripts/estados/go.py --refazer    # refaz o índice antes de baixar
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from comum import RAIZ_ESTADUAIS, Rede, caminhos, executar, gravar, html_para_md  # noqa: E402

UF = "GO"
API = "https://legisla.casacivil.go.gov.br/api/v2/pesquisa/legislacoes"
# id do tipo na API -> (pasta, tipo canônico, prefixo do arquivo). Os seis primeiros prefixos já
# estão gravados no acervo e não mudam: é por eles que uma nova rodada reconhece o que já existe.
# O decreto orçamentário e a portaria orçamentária abrem e remanejam crédito — são norma, e são
# quase um terço do que o Legisla Goiás publica.
TIPOS = {
    12: ("constituicao", "Constituição Estadual", "ce"),
    13: ("emendas-constitucionais", "Emenda Constitucional", "ec"),
    1: ("leis-complementares", "Lei Complementar", "lc"),
    2: ("leis-ordinarias", "Lei Ordinária", "lei"),
    4: ("leis-delegadas", "Lei Delegada", "ld"),
    8: ("decretos-lei", "Decreto-Lei", "dl"),
    3: ("decretos", "Decreto", "dec"),
    5: ("decretos", "Decreto", "dec-orc"),
    6: ("portarias", "Portaria", "port-orc"),
    7: ("resolucoes", "Resolução", "res"),
}
rede = Rede(rps=4)


def indice(refazer=False):
    pasta = os.path.join(RAIZ_ESTADUAIS, UF, "_indice")
    arq = os.path.join(pasta, "legislacoes.json")
    if os.path.exists(arq) and not refazer:
        return json.load(open(arq, encoding="utf-8"))
    itens = []
    for tid in TIPOS:
        pag = 1
        while True:
            st, dados, _ = rede.get(f"{API}?page={pag}&tipo_legislacao={tid}", "application/json")
            res = json.loads(dados)["resultados"] if st == 200 else []
            if not res:
                break
            itens += res
            pag += 1
        print(f"[{UF}] índice tipo {tid}: {len(itens)} acumulado", flush=True)
    os.makedirs(pasta, exist_ok=True)
    with open(arq, "w", encoding="utf-8") as f:
        json.dump(itens, f, ensure_ascii=False)
    return itens


def processar(it):
    pasta, nome, prefixo = TIPOS[int(it["tipo_legislacao"]["id"])]
    numero = (it.get("numero") or "sn").replace(".", "")
    slug = f"{prefixo}-{numero}-{it['ano']}-id{it['id']}"
    md, fonte = caminhos(UF, pasta, it["ano"], slug)
    if os.path.exists(md):
        return "pulado", None
    st, dados, _ = rede.get(f"{API}/{it['id']}", "application/json")
    if st != 200:
        return "sem_texto", {"id": it["id"], "http": st}
    d = json.loads(dados)
    html = d.get("conteudo") or ""
    if not html.strip():
        return "sem_texto", {"id": it["id"], "motivo": "sem conteúdo"}
    situacao = ((d.get("estado_legislacao") or it.get("estado_legislacao") or {}).get("nome")) or ""
    data = d.get("data_legislacao") or ""
    titulo = f"{nome} nº {it.get('numero') or 's/n'}, de {'/'.join(reversed(data.split('-')))}" if nome != "Constituição Estadual" else "Constituição do Estado de Goiás"
    diarios = d.get("diarios_estaduais") or []
    meta = [
        ("titulo", titulo),
        ("uf", UF),
        ("tipo", nome),
        ("numero", it.get("numero") or ""),
        ("data", data),
        ("ementa", " ".join((d.get("ementa") or "").split())),
        ("situacao", situacao),
        ("revogada", situacao == "Revogada"),
        ("versao_texto", "compilada (Legisla Goiás)"),
        ("publicacao", f"DOE nº {diarios[0].get('numero')}, {diarios[0].get('data')}" if diarios and diarios[0].get("numero") else ""),
        ("fonte", f"https://legisla.casacivil.go.gov.br/pesquisa_legislacao/{it['id']}"),
    ]
    gravar(md, fonte, html, meta, f"# {titulo}\n\n{html_para_md(html)}")
    return "ok", None


if __name__ == "__main__":
    itens = indice(refazer="--refazer" in sys.argv)
    itens.sort(key=lambda i: (str(i["ano"]), i["data_legislacao"][3:5], i["data_legislacao"][:2]), reverse=True)
    print(f"[{UF}] {len(itens)} normas no índice", flush=True)
    limite = [a for a in sys.argv[1:] if a.isdigit()]
    if limite:
        itens = itens[: int(limite[0])]
    executar(UF, itens, processar)
