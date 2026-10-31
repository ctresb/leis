"""Replay somente leitura do lote AM de leis PDF recentes."""
import argparse,hashlib,json
from pathlib import Path
from auditar_sapl_recentes_pdf import auditar

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--manifesto',required=True);ap.add_argument('--saida',required=True);a=ap.parse_args();m=json.loads(Path(a.manifesto).read_text());bad=0
    with Path(a.saida).open('x') as out:
        for r in m['documentos']:
            raw=Path(r['path']).read_bytes();q=dict(path=r['path'],sha256_md=hashlib.sha256(raw).hexdigest(),aceito=False)
            try:
                if q['sha256_md']!=r['sha256_md']:raise ValueError('MD diverge do pacote')
                body,proof=auditar(r['captura'],raw);q.update(aceito=True,QA=proof)
            except Exception as e:q['erro']=type(e).__name__+': '+str(e);bad+=1
            out.write(json.dumps(q,ensure_ascii=False)+'\n')
    print(json.dumps(dict(total=len(m['documentos']),falhas=bad)))
    if bad:raise SystemExit(1)
if __name__=='__main__':main()
