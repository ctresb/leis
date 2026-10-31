"""Versao 2: retoma checkpoints TA com saida absoluta e depois a fila original.

Conserva o checkpoint anterior em recibo privado. Usa a mesma trava global, a
mesma pré-validação SIGI/Casa e os mesmos caches/limites do coletor congelado.
"""
import argparse,datetime,fcntl,hashlib,json,os,sys
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import fila_textos_articulados_sapl as fila
ROOT=Path(__file__).resolve().parent.parent

def selecionar(state,hosts):
    result=[]
    if len(hosts)!=len(set(hosts)) or len(hosts)>2:raise ValueError('Hosts repetidos ou mais de dois')
    for host in hosts:
        record=state[host]
        if record.get('fim') or record.get('erro') or record['estado']!='iniciado; não repetir automaticamente':raise ValueError('Somente checkpoint interrompido, sem erro da fonte')
        item=record['vinculo_sigi']
        if item.get('host')!=host:raise ValueError('Vínculo do checkpoint diverge do host')
        result.append(item)
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--saida',type=Path,required=True);ap.add_argument('--recibo',type=Path,required=True);ap.add_argument('--host',action='append',required=True);ap.add_argument('--referencia',type=datetime.date.fromisoformat,required=True);a=ap.parse_args();a.saida=a.saida.resolve();lock=(ROOT/'municipais/_indice/organicas-sapl/fila-ta.lock').open('a');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB);checkpoint=a.saida/'fila.json';raw=checkpoint.read_bytes();state=json.loads(raw);items=selecionar(state,a.host);a.recibo.mkdir(exist_ok=False);(a.recibo/'fila.preimagem.json').write_bytes(raw);fingerprint=fila.sha(Path(fila.coletor.__file__).read_bytes());results=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs={pool.submit(fila.executar,item,a.saida,a.referencia,fingerprint):item['host'] for item in items}
        for future in as_completed(jobs):
            host=jobs[future];record=future.result();record['checkpoint_interrompido_anterior']=state[host];state[host]=record;temp=checkpoint.with_suffix('.temporario');temp.write_text(json.dumps(state,ensure_ascii=False,indent=2));temp.replace(checkpoint);results.append(record);(a.recibo/'resultados.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n');print(json.dumps(record,ensure_ascii=False),flush=True)
    (a.recibo/'manifesto.json').write_text(json.dumps(dict(checkpoint_preimagem_sha256=hashlib.sha256(raw).hexdigest(),coletor_sha256=fingerprint,hosts=a.host,resultados=results),ensure_ascii=False,indent=2)+'\n');lock.close();os.execv(sys.executable,[sys.executable,'-I',str(ROOT/'scripts/fila_textos_articulados_sapl.py'),'--saida',str(a.saida),'--trabalhadores','2','--referencia',a.referencia.isoformat()])

if __name__=='__main__':main()
