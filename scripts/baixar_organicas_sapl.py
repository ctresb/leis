"""Leis orgânicas e emendas integrais em SAPLs municipais oficiais; cache retomável."""
import argparse
import datetime as dt
import hashlib
import fcntl
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import Rede, documento_para_md, normalizar_chave, yaml_str
from granularidade_sapl import alertas_multiplos_atos, alertas_outras_publicacoes

RAIZ = Path(__file__).resolve().parent.parent / "municipais"
FONTES = [("Lapa", "PR", "sapl.lapa.pr.leg.br"),
          ("Santo Antônio do Paraíso", "PR", "sapl.santoantoniodoparaiso.pr.leg.br"),
          ("Bariri", "SP", "sapl.bariri.sp.leg.br"),
          ("Registro", "SP", "sapl.registro.sp.leg.br"),
          ("Jardinópolis", "SP", "sapl.jardinopolis.sp.leg.br"),
          ("Igarapava", "SP", "sapl.igarapava.sp.leg.br")]


TRAVAS_HOST = {}
REDES_HOST = {}


def rede_host(host, rps):
    if host not in TRAVAS_HOST:
        pasta = RAIZ / "_indice/organicas-sapl/travas"
        pasta.mkdir(parents=True, exist_ok=True)
        trava = (pasta / (host + ".lock")).open("a")
        fcntl.flock(trava, fcntl.LOCK_EX)
        TRAVAS_HOST[host] = trava
    if host not in REDES_HOST:
        REDES_HOST[host] = Rede(rps=rps)
    return REDES_HOST[host]


def salvar_registro(caminho, registro, codigo, host, modo=None):
    with caminho.with_suffix(".lock").open("a") as trava:
        fcntl.flock(trava, fcntl.LOCK_EX)
        atual = json.loads(caminho.read_text()) if caminho.exists() else registro
        linha = atual.setdefault(str(codigo), registro[str(codigo)])
        linha["estado_descoberta"] = registro[str(codigo)]["estado_descoberta"]
        destino = linha.setdefault("fontes", {}).setdefault(host, {})
        recebido = registro[str(codigo)]["fontes"][host]
        for campo in ("identidade", "estado"):
            if campo in recebido:
                destino[campo] = recebido[campo]
        if modo is not None:
            destino.setdefault(modo, {}).update(recebido.get(modo, {}))
        escrever(caminho, json.dumps(atual, ensure_ascii=False).encode())


def categoria_norma(tipo, norma=None):
    t = normalizar_chave(tipo)
    if re.search(r"projeto|proposta|requerimento|indicacao|veto|mensagem|parecer", t):
        return None
    if re.search(r"\blei delegada\b", t):
        return None  # tipo distinto; não rotular silenciosamente como lei ordinária
    if "organica" in t or t == "loman" or t == "emenda a loman":
        return ("emendas-lei-organica", "Emenda à Lei Orgânica") if "emenda" in t else ("lei-organica", "Lei Orgânica")
    if "decreto legislativo" in t:
        return "decretos-legislativos", "Decreto legislativo"
    if "decreto" in t:
        return "decretos", "Decreto"
    if "resolucao" in t:
        return "resolucoes", "Resolução"
    if re.search(r"\blei\b|codigo", t):
        e = normalizar_chave((norma or {}).get("ementa", ""))
        if re.match(r"(?:institui|aprova|dispoe sobre) (?:o |a |um |uma )?(?:novo )?plano diretor", e):
            return "plano-diretor", "Plano diretor"
        if re.match(r"(?:institui|aprova|dispoe sobre) (?:o |a |um |uma )?(?:novo )?codigo tributario", e):
            return "codigo-tributario", "Código tributário"
        if re.match(r"(?:institui|aprova|dispoe sobre) (?:o |a |um |uma )?(?:novo )?codigo (?:de obras|de posturas|de zoneamento)", e):
            return "codigos", "Código municipal"
        return ("leis-complementares", "Lei complementar") if "complementar" in t else ("leis-ordinarias", "Lei ordinária")
    return None


def escrever(p, b):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_bytes(b)
    tmp.replace(p)


def corpo_integral_reconhecivel(corpo, emenda=False):
    if re.search(r"art(?:igo)?\.?\s*1(?:[º°o]|\b)|art(?:igo|\.)\s*[úu]nico", corpo, re.I):
        return True
    # Algumas emendas transcrevem primeiro o artigo que alteram; o próprio ato
    # usa PROMULGA/PROMULGAM e traz sua cláusula de vigência, sem um Art. 1º.
    # Não corrige nem adivinha numeração eventualmente reconhecida por OCR.
    return bool(emenda and len(corpo) > 500
                and re.search(r"\bpromulg(?:o|a|am|amos)\b", corpo, re.I)
                and re.search(r"vigorar|vigor", corpo, re.I))


def motivo_retencao(cache, identificador, bruto):
    path = cache / "retidos-integralidade.json"
    if not path.exists():
        return None
    registro = json.loads(path.read_text()).get(str(identificador))
    if registro and registro.get("sha256_fonte") == hashlib.sha256(bruto).hexdigest():
        return registro["motivo"]
    return None


CARIMBO_CAMPINAS = [
    re.compile(r"(?:CÂMARA MUNICIPAL DE CAMPINAS Estado de São Paulo )?Diretoria de Gestão Documental Coordenadoria de Biblioteca "
               r"\S+@campinas\.sp\.leg\.br(?: –| -)? ?(?:Ramal:? ?\d+)?"),
    re.compile(r"Avenida da Saudade, nº 1\.004 – Ponte Preta – CEP: 13041-670 – Campinas – SP – PABX: \(19\) 3736-1300\.?(?: www\.campinas\.sp\.leg\.br)?"),
]
# a fonte tem erros de grafia nesta linha ("Municipio", "Municípo", "Campina"); a data também varia ("1º de outubro", "novembrode")
AVISO_NAO_SUBSTITUI_CAMPINAS = re.compile(
    r"Texto somente para consulta\. Não substitui o publicado no Diário Oficial do Munic\w+(?: de Campinas?)? em \d{1,2}º? de \w+ ?de \d{4}")
AVISO_REPRODUZIDO_CAMPINAS = re.compile(
    r"Texto para consulta, reproduzido conforme a publicação no Diário Oficial do Município em \d{1,2}º? de \w+ ?de \d{4}")
SUPLEMENTO_CAMPINAS = re.compile(r"TABELAS? [^.\n]{0,80}PUBLICADAS? EM SUPLEMENTO", re.I)


def limpar_carimbo_campinas(corpo):
    """Remove só a capa e o rodapé da biblioteca da Câmara (parágrafo inteiro, correspondência exata).

    Retorna (corpo, notas): o aviso da cópia de consulta e os anexos em suplemento vão para `versao_texto`.
    """
    mantidos, notas = [], []
    for par in corpo.split("\n\n"):
        plano = re.sub(r"\s+", " ", par).strip()
        if AVISO_NAO_SUBSTITUI_CAMPINAS.fullmatch(plano):
            notas.append("cópia de consulta da Câmara, não substitui o Diário Oficial do Município")
        elif AVISO_REPRODUZIDO_CAMPINAS.fullmatch(plano):
            notas.append("cópia de consulta da Câmara, reproduzida conforme a publicação no Diário Oficial do Município")
        elif not any(r.fullmatch(plano) for r in CARIMBO_CAMPINAS):
            mantidos.append(par)
    corpo = "\n\n".join(mantidos)
    if SUPLEMENTO_CAMPINAS.search(corpo):
        notas.append("tabelas e anexos publicados em suplemento, ausentes do texto integral")
    return corpo, notas


def executar(fontes, rps, modo="organicas", max_documentos=0, ano_filtro=None, siglas=()):
    ibge = json.loads((RAIZ / "_indice/ibge-municipios.json").read_text())
    registro_path = RAIZ / "_indice/organicas-sapl/municipios.json"
    registro = json.loads(registro_path.read_text()) if registro_path.exists() else {
        str(x["id"]): {"municipio": x["nome"], "uf": x["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"],
                       "estado_descoberta": "fonte ainda não localizada", "fontes": {}} for x in ibge}
    erros = 0
    for nome, uf, host in fontes:
        rede = rede_host(host, rps)
        cache = RAIZ / "_indice/organicas-sapl" / host
        def obter(url, destino):
            if destino.exists():
                return destino.read_bytes()
            st, b, ct = rede.get(url, tentativas=1)
            if st != 200:
                raise RuntimeError(f"HTTP {st}: {url}")
            escrever(destino, b)
            return b
        def api(caminho):
            url = f"https://{host}/api/{caminho}"
            destino = cache / (hashlib.sha256(url.encode()).hexdigest() + ".json")
            d = json.loads(obter(url, destino))
            return d
        try:
            matches = [x for x in ibge if normalizar_chave(x["nome"]) == normalizar_chave(nome) and
                       x["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"] == uf]
            if len(matches) != 1:
                raise RuntimeError("identidade municipal IBGE ambígua")
            codigo = matches[0]["id"]
            nome = matches[0]["nome"]
            casa = api("base/casalegislativa/")
            if not any(normalizar_chave(c["municipio"]) == normalizar_chave(nome) and c["uf"] == uf
                       for c in casa["results"]):
                raise RuntimeError("identidade da casa SAPL diverge do município IBGE")
            registro[str(codigo)]["estado_descoberta"] = "fonte oficial identificada"
            registro[str(codigo)]["fontes"].setdefault(host, {"identidade": f"https://{host}/api/base/casalegislativa/",
                                                  "estado": "índice em processamento"})
            salvar_registro(registro_path, registro, codigo, host)
            tipos = []
            tipos_reais = []
            page = 1
            while True:
                d = api(f"norma/tiponormajuridica/?page_size=100&page={page}")
                tipos_reais.extend(d["results"])
                tipos += [t for t in d["results"] if categoria_norma(t["descricao"]) and
                          (modo == "legislacao" or categoria_norma(t["descricao"])[0] in
                           ("lei-organica", "emendas-lei-organica"))
                          and (not siglas or t["sigla"] in siglas)]
                if not d["pagination"].get("next_page"):
                    break
                page += 1
            ok = pulado = 0
            indice = []
            eq_path = cache / "equivalencias.json"
            equivalencias = json.loads(eq_path.read_text()) if eq_path.exists() else {}
            pasta_municipio = RAIZ / uf / normalizar_chave(nome).replace(" ", "-")
            # Índice local por município: evita reler todos os corpos a cada ato.
            fontes_md = set()
            hashes_md = {}
            for existente in pasta_municipio.glob("**/*.md"):
                texto_existente = existente.read_text()
                m_fonte = re.search(r'^fonte: (".*")$', texto_existente, re.M)
                m_hash = re.search(r'^sha256_texto: "([a-f0-9]{64})"$', texto_existente, re.M)
                if m_fonte:
                    fontes_md.add(json.loads(m_fonte[1]))
                if m_hash:
                    hashes_md.setdefault(m_hash[1], []).append(existente)
            for tipo in tipos:
                page = 1
                vistos = set()
                while True:
                    d = api(f"norma/normajuridica/?tipo={tipo['id']}&page_size=100&page={page}" + (f"&ano={ano_filtro}" if ano_filtro else ""))
                    if any(n["tipo"] != tipo["id"] for n in d["results"]):
                        raise RuntimeError("API ignorou o filtro de tipo; índice não confiável")
                    vistos.update(n["id"] for n in d["results"])
                    indice.extend(d["results"])
                    for n in d["results"]:
                        try:
                            emenda = "emenda" in tipo["descricao"].lower()
                            categoria, tipo_canonico = categoria_norma(tipo["descricao"], n)
                            identity = f"https://{host}/norma/{n['id']}"
                            if identity in fontes_md:
                                pulado += 1
                                continue
                            if max_documentos and ok >= max_documentos:
                                continue
                            url = n.get("texto_integral")
                            if not url:
                                raise RuntimeError("norma sem texto integral")
                            if urlsplit(url).hostname == host:
                                url = "https://" + url.split("://", 1)[1]
                            fonte = RAIZ / "_fonte/organicas-sapl" / host / f"{n['id']}.bin"
                            b = obter(url, fonte)
                            retencao = motivo_retencao(cache, n["id"], b)
                            if retencao:
                                raise RuntimeError("fonte retida para revisão de integralidade: " + retencao)
                            corpo, motivo = documento_para_md(b, url)
                            if motivo:
                                raise RuntimeError(motivo)
                            notas_texto = []
                            if host == "sapl.campinas.sp.leg.br":
                                corpo, notas_texto = limpar_carimbo_campinas(corpo)
                            granularidade = alertas_multiplos_atos(corpo, tipo["descricao"], n["numero"])
                            outras_publicacoes = alertas_outras_publicacoes(corpo)
                            if outras_publicacoes:
                                raise RuntimeError("possível aviso/extrato de outra publicação no anexo; revisar: " + json.dumps(outras_publicacoes, ensure_ascii=False))
                            if granularidade:
                                raise RuntimeError("anexo contém epígrafe de outra norma; revisar granularidade: " +
                                                   json.dumps(granularidade, ensure_ascii=False))
                            if not corpo_integral_reconhecivel(corpo, emenda):
                                raise RuntimeError("texto sem artigo inicial reconhecível; revisar integralidade")
                            # Guarda versões iguais uma vez por município, preservando o índice original.
                            digest = hashlib.sha256(corpo.encode()).hexdigest()
                            iguais = hashes_md.get(digest, [])
                            if iguais:
                                equivalencias[str(n["id"])] = {"arquivo": str(iguais[0].relative_to(RAIZ)),
                                    "fonte": identity, "fonte_texto": url, "sha256_texto": digest}
                                escrever(eq_path, json.dumps(equivalencias, ensure_ascii=False).encode())
                                pulado += 1
                                continue
                            data = n.get("data") or ""
                            data_cadastro = data
                            ano_documento = str(n["ano"])
                            observacao_data = ""
                            if host == "sapl.lapa.pr.leg.br" and n["id"] == 3799:
                                if "Edifício da Câmara Municipal da Lapa, em 4 de abril de 1990" not in corpo:
                                    raise RuntimeError("assinatura da lei orgânica Lapa não confirmada")
                                data = "1990-04-04"
                                observacao_data = "Data da assinatura no texto integral; cadastro SAPL usa a data da Emenda 01/2020."
                            if host == "sapl.igarapava.sp.leg.br" and n["id"] == 1373:
                                if "Igarapava/SP, ano de 1990." not in corpo:
                                    raise RuntimeError("ano da assinatura de Igarapava não confirmado")
                                data = ""
                                ano_documento = "1990"
                                observacao_data = "Texto integral assinado apenas com ano de 1990; cadastro apresenta 2011-11-04, sem confirmação no documento."
                            ano = data[:4] if data else ano_documento
                            numero = str(n["numero"])
                            titulo = n["__str__"]
                            meta = {"titulo": titulo, "tipo": tipo_canonico, "tipo_na_fonte": tipo["descricao"],
                                    "numero": numero, "data": data, "municipio": nome, "uf": uf,
                                    "codigo_ibge": str(codigo), "versao_texto": "; ".join(filter(None, ["texto integral anexado no SAPL municipal", n.get("observacao", "").strip(), *notas_texto])) if notas_texto else "texto integral anexado no SAPL municipal; " + n.get("observacao", ""),
                                    "fonte": identity, "fonte_texto": url,
                                    "sha256_fonte": hashlib.sha256(b).hexdigest(), "sha256_texto": digest,
                                    "baixado_em": dt.date.today().isoformat()}
                            if data != data_cadastro:
                                meta["data_no_cadastro"] = data_cadastro
                                meta["observacao_data"] = observacao_data
                                meta["ano_na_fonte"] = ano_documento
                                titulo = "Lei Orgânica do Município da Lapa, de 4 de abril de 1990" if host == "sapl.lapa.pr.leg.br" else "Lei Orgânica do Município de Igarapava, de 1990"
                                meta["titulo"] = titulo
                            cab = ["---"] + [f"{k}: {yaml_str(v)}" for k, v in meta.items()] + ["---", "", f"# {titulo}", "", corpo, ""]
                            arq = pasta_municipio / categoria / ano / f"{categoria}-{normalizar_chave(numero)}-{ano}-sapl-{n['id']}.md"
                            escrever(arq, "\n".join(cab).encode())
                            fontes_md.add(identity)
                            hashes_md.setdefault(digest, []).append(arq)
                            ok += 1
                        except Exception as e:
                            erros += 1
                            cache.mkdir(parents=True, exist_ok=True)
                            with (cache / "falhas.jsonl").open("a") as f:
                                f.write(json.dumps({"id": n["id"], "erro": str(e), "quando": dt.datetime.now().isoformat()}) + "\n")
                            print(host, n["id"], "FALHA", e, flush=True)
                    if not d["pagination"].get("next_page"):
                        if len(vistos) != d["pagination"]["total_entries"]:
                            raise RuntimeError("contagem do índice diverge do total oficial")
                        break
                    page += 1
            parcial = bool(ano_filtro or siglas)
            nome_indice = "indice.json" if modo == "organicas" else "indice-legislacao.json"
            if parcial:
                nome_indice = f"indice-legislacao-parcial-{'-'.join(sorted(siglas)) or 'todos'}-{ano_filtro or 'todos'}.json"
            escrever(cache / nome_indice, json.dumps({"fonte": f"https://{host}/api/norma/normajuridica/",
                     "municipio": nome, "uf": uf, "codigo_ibge": codigo, "modo": modo, "tipos_reais": tipos_reais, "tipos": tipos,
                     "normas": indice, "consultado_em": dt.date.today().isoformat()}, ensure_ascii=False).encode())
            presentes = {n["id"] for n in indice if "https://" + host + "/norma/" + str(n["id"]) in fontes_md}
            if parcial:
                print(host, "IBGE", codigo, "PARCIAL", f"ano={ano_filtro or 'todos'} siglas={','.join(sorted(siglas)) or 'todas'}",
                      "novos", ok, "já existentes", pulado, "índice", len(indice), "com md", len(presentes), flush=True)
                continue
            registro = json.loads(registro_path.read_text())
            registro[str(codigo)]["fontes"][host].setdefault(modo, {}).update({"estado": "índice de tipos normativos completo capturado", "limite_textos": max_documentos,
                "registros": len(indice), "textos_md": len(presentes), "ids_equivalentes": list(equivalencias), "ids_sem_md": [n["id"] for n in indice if n["id"] not in presentes and str(n["id"]) not in equivalencias], "normas_distintas": len({(n["tipo"], n["numero"], n["ano"]) for n in indice}),
                "leis_organicas_distintas": len({(n["numero"], n["ano"]) for n in indice if not
                    any(t["id"] == n["tipo"] and "emenda" in t["descricao"].lower() for t in tipos)}),
                "consultado_em": dt.date.today().isoformat()})
            salvar_registro(registro_path, registro, codigo, host, modo)
            print(host, "IBGE", codigo, "novos", ok, "já existentes", pulado, flush=True)
        except Exception as e:
            erros += 1
            cache.mkdir(parents=True, exist_ok=True)
            with (cache / "falhas.jsonl").open("a") as f:
                f.write(json.dumps({"erro": str(e), "quando": dt.datetime.now().isoformat()}) + "\n")
            print(host, "FALHA", e, flush=True)
    return bool(erros)


def catalogo_sigi(rps):
    ibge = json.loads((RAIZ / "_indice/ibge-municipios.json").read_text())
    lookup = {(normalizar_chave(x["nome"]), x["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]): str(x["id"]) for x in ibge}
    rede = Rede(rps=rps)
    pasta = RAIZ / "_indice/organicas-sapl/sigi"
    url = "https://sigi.interlegis.leg.br/api/servicos/"
    registros = []
    pagina = 1
    while url:
        arquivo = pasta / f"pagina-{pagina}.json"
        if arquivo.exists():
            b = arquivo.read_bytes()
        else:
            st, b, _ = rede.get(url, tentativas=1)
            if st != 200:
                raise RuntimeError(f"SIGI HTTP {st}: {url}")
            json.loads(b)
            escrever(arquivo, b)
        d = json.loads(b)
        registros += d["results"]
        url = d["next"]
        pagina += 1
    if len(registros) != d["count"]:
        raise RuntimeError("catálogo SIGI mudou durante paginação; revisão necessária")
    candidatos = []
    nao_vinculados = []
    for r in registros:
        c = r["casa_legislativa"]
        if r["tipo_servico_sigla"] != "SAPL" or c["tipo_orgao_sigla"] != "CM":
            continue
        codigo = lookup.get((normalizar_chave(c["municipio"]), c["uf"]))
        item = {"municipio": c["municipio"], "uf": c["uf"], "url": r["url"],
                "codigo_ibge": codigo, "estado": "candidato oficial SIGI; API municipal ainda não validada"}
        (candidatos if codigo else nao_vinculados).append(item)
    escrever(pasta / "catalogo.json", json.dumps({"fonte": "https://sigi.interlegis.leg.br/api/servicos/",
        "consultado_em": dt.date.today().isoformat(), "total_servicos": len(registros),
        "candidatos_sapl": candidatos, "municipios_nao_vinculados": nao_vinculados}, ensure_ascii=False).encode())
    print("SIGI:", len(registros), "serviços;", len(candidatos), "SAPLs municipais vinculados;",
          len(nao_vinculados), "pendências IBGE", flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--catalogo-sigi", action="store_true", help="captura catálogo oficial de candidatos, sem baixar normas")
    ap.add_argument("--rps", type=float, default=1)
    ap.add_argument("--modo", choices=["organicas", "legislacao"], default="organicas")
    ap.add_argument("--max-documentos", type=int, default=0, help="limita novas conversões; índice permanece completo")
    ap.add_argument("--host", help="reexecuta uma fonte já identificada")
    ap.add_argument("--ano", type=int, help="processa só as normas deste ano (coleta em frações; não atualiza o registro de índice completo)")
    ap.add_argument("--siglas", default="", help="siglas de tipo do SAPL separadas por vírgula, p.ex. LEI,LC")
    ap.add_argument("--descobrir", metavar="HOST", help="valida um SAPL oficial e registra sua identidade IBGE")
    a = ap.parse_args()
    if a.max_documentos < 0:
        ap.error("max-documentos deve ser não negativo")
    if not 0 < a.rps <= 4:
        ap.error("rps deve ser maior que zero e no máximo 4")
    if a.catalogo_sigi:
        catalogo_sigi(a.rps)
        raise SystemExit(0)
    registro_path = RAIZ / "_indice/organicas-sapl/municipios.json"
    fontes = list(FONTES)
    if registro_path.exists():
        for municipio in json.loads(registro_path.read_text()).values():
            fontes.extend((municipio["municipio"], municipio["uf"], host) for host in municipio["fontes"])
    if a.descobrir:
        if not re.fullmatch(r"[a-z0-9.-]+\.(?:leg|gov)\.br", a.descobrir):
            ap.error("informe um host oficial .leg.br ou .gov.br; identidade da casa será confrontada com IBGE")
        url = f"https://{a.descobrir}/api/base/casalegislativa/"
        st, bruto, _ = rede_host(a.descobrir, a.rps).get(url, tentativas=1)
        if st != 200:
            ap.error(f"fonte indisponível: HTTP {st}")
        casas = json.loads(bruto)["results"]
        if len(casas) != 1:
            ap.error("fonte sem identidade única")
        c = casas[0]
        fontes = [(c["municipio"], c["uf"], a.descobrir)]
        escrever(RAIZ / "_indice/organicas-sapl" / a.descobrir / (hashlib.sha256(url.encode()).hexdigest() + ".json"), bruto)
    fontes = list(dict.fromkeys(fontes))
    if a.host and not any(f[2] == a.host for f in fontes):
        ap.error("host não identificado; use --descobrir")
    raise SystemExit(executar([f for f in fontes if not a.host or f[2] == a.host], a.rps, a.modo, a.max_documentos, a.ano, tuple(x for x in a.siglas.split(',') if x)))
