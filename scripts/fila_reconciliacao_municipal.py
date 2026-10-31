"""Fila offline retomável: prepara candidatos e revisões, nunca aplica nem acessa HTTP."""
import argparse
import concurrent.futures
import fcntl
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import datetime as dt

REPO=Path(__file__).resolve().parent.parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def salvar(path,dados):
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(dados,ensure_ascii=False,indent=2))
    tmp.replace(path)


def executar(edicao,chave,raiz,saida,fingerprints):
    def conferir_pipeline():
        if any(sha(REPO/"scripts"/nome)!=valor for nome,valor in fingerprints.items()):
            raise RuntimeError("pipeline mudou durante a fila; candidato não aprovado, retomar com novos SHAs")
    conferir_pipeline()
    log=saida/"logs"/(chave+".txt")
    log.parent.mkdir(parents=True,exist_ok=True)
    comando=[sys.executable,"-I",str(REPO/"scripts/reconciliar_diarios_municipais.py"),
             "--pdf",edicao["pdf"],"--fonte",edicao["fonte"],"--data",edicao["data"],
             "--raiz",str(raiz),"--saida",str(saida/"candidatos")]
    with log.open("w") as f:
        r=subprocess.run(comando,stdout=f,stderr=subprocess.STDOUT)
    conferir_pipeline()
    resultado={"pdf":edicao["pdf"],"fonte":edicao["fonte"],"sha256_pdf":edicao["sha256_pdf"],
               "exit_code":r.returncode,"log":str(log),"verificado_em":dt.datetime.now().isoformat()}
    try:
        resumo=json.loads(log.read_text().splitlines()[-1])
        resultado.update(resumo)
        if resumo.get("estado")=="aplicado":
            raise RuntimeError("a fila não permite aplicação")
    except (ValueError,IndexError):
        resultado["estado"]="falha de preparação"
    return resultado


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--inventario",type=Path,required=True)
    ap.add_argument("--saida",type=Path,required=True)
    ap.add_argument("--raiz",type=Path,default=REPO)
    ap.add_argument("--trabalhadores",type=int,choices=range(1,5),default=2)
    ap.add_argument("--max-pdfs",type=int,default=0)
    ap.add_argument("--repetir-pendentes",action="store_true")
    a=ap.parse_args()
    if a.max_pdfs<0:ap.error("--max-pdfs deve ser não negativo")
    if not (a.raiz/"municipais/_indice/ibge-municipios.json").is_file():
        ap.error("cadastro IBGE local obrigatório; a fila não consulta rede")
    a.saida.mkdir(parents=True,exist_ok=True)
    with (a.saida/"fila.lock").open("a") as trava:
        try:fcntl.flock(trava,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:ap.error("fila offline já em execução")
        checkpoint=a.saida/"checkpoint.json"
        dados=json.loads(checkpoint.read_text()) if checkpoint.exists() else {}
        inventario=json.loads(a.inventario.read_text())
        fingerprints={p:sha(REPO/"scripts"/p) for p in
                      ("baixar_municipal.py","extrair_diario_municipal.py","reconciliar_diarios_municipais.py")}
        versao="".join(fingerprints.values())
        classificador=fingerprints["baixar_municipal.py"]
        tarefas=[]
        falhas_preflight=0
        for e in inventario["edicoes"]:
            # Só entradas com URL/data e PDF cujo hash confere com o inventário provado.
            if not e.get("prova_calendario") or not e.get("fonte") or not e.get("data"):
                continue
            chave=hashlib.sha256((e["fonte"]+e["sha256_pdf"]+versao).encode()).hexdigest()
            anterior=dados.get(chave)
            if anterior and (not a.repetir_pendentes or anterior.get("estado")=="preparado"):
                continue
            try:
                valido=sha(Path(e["pdf"]))==e["sha256_pdf"]
            except OSError:
                valido=False
            if not valido:
                falhas_preflight+=1
                dados[chave]={"estado":"PDF ausente ou mudou; exige novo inventário","pdf":e["pdf"]}
                salvar(checkpoint,dados)
                continue
            tarefas.append((e,chave))
        if a.max_pdfs:tarefas=tarefas[:a.max_pdfs]
        with concurrent.futures.ThreadPoolExecutor(max_workers=a.trabalhadores) as pool:
            pendentes={pool.submit(executar,e,c,a.raiz,a.saida,fingerprints):c for e,c in tarefas}
            for futuro in concurrent.futures.as_completed(pendentes):
                chave=pendentes[futuro]
                try:registro=futuro.result()
                except Exception as erro:registro={"estado":"falha de preparação","erro":str(erro)}
                registro["sha256_classificador"]=classificador
                registro["sha256_extrator"]=fingerprints["extrair_diario_municipal.py"]
                registro["sha256_reconciliador"]=fingerprints["reconciliar_diarios_municipais.py"]
                registro["sha256_pipeline"]=hashlib.sha256(versao.encode()).hexdigest()
                dados[chave]=registro
                salvar(checkpoint,dados)
                print(json.dumps(registro,ensure_ascii=False),flush=True)
        print(json.dumps({"processados":len(tarefas),"falhas_preflight":falhas_preflight,"checkpoint":str(checkpoint),
                          "pdfs_sem_calendario_retidos":len(inventario.get("pdfs_sem_calendario",[]))}),flush=True)
        return int(bool(falhas_preflight) or any(dados[c].get("estado")!="preparado" for _,c in tarefas))

if __name__=="__main__":
    raise SystemExit(main())
