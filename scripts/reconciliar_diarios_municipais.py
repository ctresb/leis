"""Prepara/reconcilia uma edição pelo PDF geométrico; não consulta rede nem Git.

Por padrão grava somente candidatos e manifesto. --aplicar preserva cada versão anterior
por hash antes de substituir/remover documentos da mesma fonte/edição.
"""
import argparse
import fcntl
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import uuid
sys.path.insert(0, str(Path(__file__).resolve().parent))
import baixar_municipal as municipal
from auditar_municipal import metadados
from comum import yaml_str
from extrair_diario_municipal import VERSAO, SHA_EXTRATOR, caminhos_cache

REPO = Path(__file__).resolve().parent.parent


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def salvar(p,d):
    p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".tmp")
    t.write_text(json.dumps(d,ensure_ascii=False,indent=2))
    t.replace(p)


def arquivos_da_fonte(raiz,fonte):
    r=subprocess.run(["rg","-l","-F","--glob","*.md",
                      "fonte: "+yaml_str(fonte),str(raiz/"municipais")],capture_output=True,text=True)
    if r.returncode not in (0,1):
        raise RuntimeError(r.stderr)
    return [Path(x) for x in r.stdout.splitlines() if x]


def registrar_ledger(raiz,dados,manifesto):
    anteriores={r["arquivo"]:r for r in dados["anteriores"]}
    def relativo(path):
        path=Path(path).resolve()
        try:return str(path.relative_to(raiz.resolve()))
        except ValueError:return str(path)
    destinos=[]
    for acao in dados["acoes"]:
        if acao["acao"] in ("gravar","preservar_referencia"):
            destino=raiz/acao["destino"]
            if digest(destino)!=acao["sha256"]:
                raise RuntimeError("destino mudou antes do ledger: "+str(destino))
            anterior=anteriores.get(acao["destino"])
            destinos.append({"acao":"referencia_parcial" if acao["acao"]=="preservar_referencia" else
                             ("novo" if anterior is None else "modificado" if anterior["sha256"]!=acao["sha256"] else "inalterado"),
                             "arquivo":acao["destino"],"codigo":acao["codigo"],"sha256":acao["sha256"],
                             "sha256_bloco":(json.loads(destino.read_text()).get("sha256_bloco") if acao["acao"]=="preservar_referencia"
                                               else acao.get("prova_bloco",{}).get("sha256_bloco")),
                             "cobertura":acao.get("cobertura")})
        else:
            anterior=anteriores[acao["arquivo"]]
            destinos.append({"acao":"retirado","arquivo":acao["arquivo"],"codigo":acao["codigo"],
                             "sha256_anterior":anterior["sha256"],"motivo":acao["motivo"],
                             "sha256_bloco":acao.get("prova_bloco",{}).get("sha256_bloco")})
    snapshots=[]
    for anterior in dados["anteriores"]:
        snapshot=Path(dados["backup"])/anterior["sha256"]/anterior["arquivo"]
        if digest(snapshot)!=anterior["sha256"]:
            raise RuntimeError("snapshot diverge antes do ledger: "+str(snapshot))
        snapshots.append({"arquivo_anterior":anterior["arquivo"],"snapshot":relativo(snapshot),"sha256":anterior["sha256"]})
    registro={k:dados.get(k) for k in ("fonte","data_circulacao","sha256_pdf","extrator","sha256_classificador")}
    registro.update({"pdf":relativo(dados["pdf"]),"cache_metadados":relativo(dados["cache_metadados"]),
                     "manifesto":relativo(manifesto),"sha256_manifesto":digest(manifesto),
                     "destinos":destinos,"snapshots":snapshots,
                     "referencias_parciais":[{k:r.get(k) for k in ("codigo","cobertura","sha256","vinculos_mesma_edicao")} for r in dados.get("referencias_parciais",[])],
                     "provas":[{k:r.get(k) for k in ("fonte","codigo","sha256_bloco","classificacao")} for r in dados.get("provas_especificas_aceitas",[])],
                     "revisao":({"arquivo":relativo(dados["revisao_independente"]["arquivo"]),
                                 "sha256":dados["revisao_independente"]["sha256"]} if dados.get("revisao_independente") else None),
                     "aplicado_em":dados["aplicado_em"]})
    meta=json.loads(Path(dados["cache_metadados"]).read_text())
    registro["sha256_extrator"]=meta.get("sha256_extrator")
    registro["fingerprints_historicos_ausentes"]=[k for k in ("sha256_extrator","sha256_classificador") if not registro.get(k)]
    registro["sha256_texto_pdf"]=meta["sha256_texto"]
    registro["id"]=hashlib.sha256(json.dumps(registro,sort_keys=True).encode()).hexdigest()
    ledger=raiz/"municipais/_reparos_colunas.json"
    with ledger.with_suffix(".json.lock").open("a") as trava:
        fcntl.flock(trava,fcntl.LOCK_EX)
        atual=json.loads(ledger.read_text()) if ledger.exists() else {}
        registros=atual.setdefault("reconciliacoes",[])
        if not any(r.get("id")==registro["id"] for r in registros):
            registros.append(registro)
        salvar(ledger,atual)
    return ledger


def preparar(pdf,fonte,data,raiz,saida,aplicar=False,nao_normativos_confirmados=(),revisao=None,citacoes_confirmadas=()):
    data=dt.date.fromisoformat(data)
    if data>dt.date.today():
        raise RuntimeError("data de circulação futura")
    chave=hashlib.sha256(fonte.encode()).hexdigest()
    trabalho=saida/chave/VERSAO/uuid.uuid4().hex
    trabalho.mkdir(parents=True,exist_ok=True)
    manifesto=trabalho/"manifesto.json"
    anteriores=arquivos_da_fonte(raiz,fonte)
    municipal.RAIZ=str(raiz/"municipais")
    municipal.MUNICIPIOS.clear()
    municipal.municipios_ibge()
    texto=municipal.texto_do_pdf(str(pdf))
    municipal.RAIZ=str(trabalho/"municipais")
    blocos={};falhas=[];referencias=[]
    for uf,cidade,bloco,codigo in municipal.atos(texto):
        if codigo in blocos:
            falhas.append({"codigo":codigo,"erro":"código repetido na mesma edição; exige revisão"})
            continue
        titulo,tipo,pos=municipal.epigrafe(bloco)
        blocos[codigo]={"uf":uf,"municipio":cidade,"titulo":titulo,"tipo":tipo,
                       "sha256_bloco":hashlib.sha256(bloco.encode()).hexdigest()}
        cobertura=municipal.cobertura_bloco(bloco)
        if cobertura:
            referencia=municipal.gravar_referencia(uf,cidade,bloco,codigo,data,fonte,cobertura)
            referencias.append({"codigo":codigo,"cobertura":cobertura,"arquivo":str(referencia),"sha256":digest(referencia)})
            blocos[codigo]["cobertura"]=cobertura
            continue
        if not titulo:
            possivel = municipal.cabecalho_normativo_pendente(bloco)
            if possivel:
                falhas.append({"codigo":codigo,"erro":"cabeçalho normativo não reconhecido; revisão obrigatória",
                               "cabecalho":possivel})
            continue
        if not uf or not cidade:
            falhas.append({"codigo":codigo,"erro":"norma sem cabeçalho municipal confirmado"})
            continue
        try:
            municipal.gravar(uf,cidade,titulo,tipo,bloco[pos:],codigo,data,fonte)
        except Exception as e:
            falhas.append({"codigo":codigo,"erro":str(e)})
    novos={}
    for p in (trabalho/"municipais").glob("*/*/**/*.md"):
        meta=metadados(p.read_text())
        codigo=meta["codigo_identificador"]
        if codigo in novos:
            falhas.append({"codigo":codigo,"erro":"mais de um candidato para mesma identidade"})
        novos[codigo]=p
    aceites_citacoes=set()
    aceites_retiradas=set()
    provas_aceitas=[]
    if revisao:
        revisado=json.loads(Path(revisao).read_text())
        if not isinstance(revisado,dict):
            raise RuntimeError("revisão exige registros por fonte+código+SHA do bloco")
        for registro in revisado.get("alertas",[]):
            if registro.get("fonte")!=fonte or not registro.get("confirmar_alerta_cabecalho"):
                continue
            codigo=registro.get("codigo")
            if blocos.get(codigo,{}).get("sha256_bloco")!=registro.get("sha256_bloco"):
                falhas.append({"codigo":codigo,"erro":"SHA do bloco diverge da revisão específica"})
                continue
            aceites_citacoes.add(codigo)
            provas_aceitas.append(registro)
        for registro in revisado.get("retiradas",[]):
            if registro.get("fonte")!=fonte or not registro.get("confirmar_retirada"):
                continue
            codigo=registro.get("codigo")
            anterior=raiz/registro["arquivo_anterior"]
            if (blocos.get(codigo,{}).get("sha256_bloco")!=registro.get("sha256_bloco")
                    or anterior not in anteriores or digest(anterior)!=registro.get("sha256_anterior")):
                falhas.append({"codigo":codigo,"erro":"bloco/documento anterior diverge da revisão de retirada"})
                continue
            aceites_retiradas.add(codigo)
            provas_aceitas.append(registro)
    for codigo in set(citacoes_confirmadas)-aceites_citacoes:
        falhas.append({"codigo":codigo,"erro":"confirmação de citação sem prova específica válida"})
    for codigo in set(nao_normativos_confirmados)-aceites_retiradas:
        falhas.append({"codigo":codigo,"erro":"confirmação de retirada sem prova específica válida"})
    citacoes_confirmadas=sorted(aceites_citacoes)
    nao_normativos_confirmados=sorted(aceites_retiradas)
    falhas=[f for f in falhas if not (f.get("erro")=="cabeçalho normativo não reconhecido; revisão obrigatória"
                                   and f.get("codigo") in aceites_citacoes)]
    for referencia in referencias:
        caminho=Path(referencia["arquivo"])
        conteudo=json.loads(caminho.read_text())
        vinculos=[]
        if conteudo.get("numero"):
            for codigo,candidato in novos.items():
                norma=blocos[codigo]
                numero=municipal.NUMERO.search(norma["titulo"] or "")
                if (numero and numero.group(1).replace(".", "")==conteudo["numero"]
                        and norma["tipo"]==conteudo.get("tipo")
                        and norma["municipio"]==conteudo.get("municipio")
                        and norma["uf"]==conteudo.get("uf")):
                    vinculos.append({"codigo":codigo,"destino":str(candidato.relative_to(trabalho))})
        conteudo["vinculos_mesma_edicao"]=vinculos
        salvar(caminho,conteudo)
        referencia["vinculos_mesma_edicao"]=vinculos
        referencia["sha256"]=digest(caminho)
    for p in anteriores:
        codigo=metadados(p.read_text()).get("codigo_identificador")
        if codigo not in blocos:
            falhas.append({"arquivo":str(p),"codigo":codigo,"erro":"documento anterior sem código no PDF reconstruído"})
    for p in anteriores:
        codigo=metadados(p.read_text()).get("codigo_identificador")
        if codigo in blocos and codigo not in novos and codigo not in nao_normativos_confirmados:
            falhas.append({"arquivo":str(p),"codigo":codigo,
                           "erro":"retirada não normativa exige revisão explícita do bloco oficial"})
    acoes=[]
    destinos=set()
    for codigo,p in novos.items():
        rel=p.relative_to(trabalho)
        destino=raiz/rel
        destinos.add(destino)
        if destino.exists() and destino not in anteriores:
            falhas.append({"codigo":codigo,"arquivo":str(destino),"erro":"colisão com documento de outra fonte; não substituir"})
        acoes.append({"acao":"gravar","codigo":codigo,"candidato":str(p),"destino":str(rel),"sha256":digest(p),
                      "prova_bloco":blocos[codigo]})
    for referencia in referencias:
        candidato=Path(referencia["arquivo"])
        acoes.append({"acao":"preservar_referencia","codigo":referencia["codigo"],
                      "candidato":str(candidato),"destino":str(candidato.relative_to(trabalho)),
                      "sha256":referencia["sha256"],"cobertura":referencia["cobertura"]})
    antigos=[]
    for p in anteriores:
        meta=metadados(p.read_text());codigo=meta.get("codigo_identificador")
        registro={"arquivo":str(p.relative_to(raiz)),"sha256":digest(p),"codigo":codigo,
                  "numero":meta.get("numero"),"municipio":meta.get("municipio"),
                  "candidatos_mesmo_tipo_numero":[
                      {"codigo":c,"destino":str(n.relative_to(trabalho))}
                      for c,n in novos.items()
                      if (lambda m: m.get("numero")==meta.get("numero") and m.get("tipo")==meta.get("tipo"))(
                          metadados(n.read_text()))]}
        antigos.append(registro)
        if p not in destinos:
            acoes.append({"acao":"retirar_caminho_anterior","arquivo":str(p.relative_to(raiz)),"codigo":codigo,
                          "motivo":"nova rota/título/código confirmado" if codigo in novos else "código sem candidato integral; classificação exige revisão",
                          "prova_bloco":blocos.get(codigo)})
    tx,mt=caminhos_cache(pdf)
    dados={"estado":"preparado" if not falhas else "requer_revisao","extrator":VERSAO,"sha256_extrator":SHA_EXTRATOR,
           "sha256_classificador":municipal.CLASSIFICADOR_SHA,
           "fonte":fonte,"data_circulacao":str(data),"pdf":str(pdf),"sha256_pdf":digest(pdf),
           "cache_texto":str(tx),"cache_metadados":str(mt),"anteriores":antigos,"novos":len(novos),
           "provas_especificas_aceitas":provas_aceitas,"referencias_parciais":referencias,"atos_no_pdf":len(blocos),"nao_normativos_confirmados":list(nao_normativos_confirmados),"citacoes_confirmadas":list(citacoes_confirmadas),"acoes":acoes,"falhas":falhas,"preparado_em":dt.datetime.now().isoformat()}
    if revisao:
        revisao_destino=trabalho/"revisao-independente.json"
        shutil.copyfile(revisao,revisao_destino)
        dados["revisao_independente"]={"arquivo":str(revisao_destino),"sha256":digest(revisao_destino)}
    salvar(manifesto,dados)
    if aplicar:
        if falhas:
            raise RuntimeError("reconciliação não aplicada; manifesto contém falhas: "+str(manifesto))
        backup=raiz/"municipais/_referencias/reconciliacao-geometria"/VERSAO/dados["sha256_pdf"]
        for registro in antigos:
            origem=raiz/registro["arquivo"]
            if digest(origem)!=registro["sha256"]:
                raise RuntimeError("documento mudou durante preparação; preservar e repetir")
            destino=backup/registro["sha256"]/registro["arquivo"]
            destino.parent.mkdir(parents=True,exist_ok=True)
            if not destino.exists():
                shutil.copy2(origem,destino)
        dados["estado"]="aplicando"
        dados["backup"]=str(backup)
        salvar(manifesto,dados)
        for acao in acoes:
            if acao["acao"] in ("gravar","preservar_referencia"):
                origem=Path(acao["candidato"]);destino=raiz/acao["destino"]
                if digest(origem)!=acao["sha256"]:
                    raise RuntimeError("candidato mudou; não aplicar")
                destino.parent.mkdir(parents=True,exist_ok=True)
                tmp=destino.with_name(destino.name+".tmp")
                shutil.copyfile(origem,tmp)
                tmp.replace(destino)
        for acao in acoes:
            if acao["acao"]=="retirar_caminho_anterior":
                (raiz/acao["arquivo"]).unlink()
        dados["estado"]="aplicado"
        dados["aplicado_em"]=dt.datetime.now().isoformat()
        salvar(manifesto,dados)
        registrar_ledger(raiz,dados,manifesto)
    return dados,manifesto


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pdf",type=Path,required=True)
    ap.add_argument("--fonte",required=True)
    ap.add_argument("--data",required=True,help="data oficial de circulação ISO")
    ap.add_argument("--raiz",type=Path,default=REPO)
    ap.add_argument("--saida",type=Path,default=REPO/"municipais/_indice/_reconciliacao-geometria")
    ap.add_argument("--aplicar",action="store_true")
    ap.add_argument("--confirmar-citacao",action="append",default=[],metavar="CODIGO",help="citação conferida no bloco oficial; repetível")
    ap.add_argument("--revisao",type=Path,help="evidência independente preservada junto ao manifesto")
    ap.add_argument("--confirmar-nao-normativo",action="append",default=[],metavar="CODIGO",
                    help="código cuja retirada foi revisada no bloco oficial; repetível")
    a=ap.parse_args()
    d,p=preparar(a.pdf,a.fonte,a.data,a.raiz,a.saida,a.aplicar,a.confirmar_nao_normativo,a.revisao,a.confirmar_citacao)
    print(json.dumps({"estado":d["estado"],"anteriores":len(d["anteriores"]),"novos":d["novos"],"falhas":len(d["falhas"]),"manifesto":str(p)},ensure_ascii=False))
    return int(bool(d["falhas"]))

if __name__=="__main__":
    raise SystemExit(main())
