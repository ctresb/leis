"""Replay offline dos candidatos privados SPL/Agape; não promove documentos."""
import argparse,json,hashlib
from pathlib import Path
from auditar_spl_html_recente import auditar

def main():
 p=argparse.ArgumentParser();p.add_argument('--manifesto',required=True);p.add_argument('--saida',required=True);a=p.parse_args();m=json.loads(Path(a.manifesto).read_text());rows=[];bad=0
 for r in m['documentos']:
  try:
   b=Path(r['privado']).read_bytes()
   if hashlib.sha256(b).hexdigest()!=r['sha256_md']:raise ValueError('MD privado diverge do congelado')
   h,body=b.decode().split('\n---\n',1);meta={k:json.loads(v) for ln in h.splitlines()[1:] if ': ' in ln for k,v in [ln.split(': ',1)]}
   if any(meta.get(k)!=r['captura']['item'][k] for k in ('tipo','numero','data')) or meta.get('revogada') is not None:raise ValueError('metadados divergem/estado não conservador')
   norm=body.split('\n',2)[2];_,q=auditar(r['captura'],m['imagens'],norm);rows.append(dict(path=r['path'],aceito=True,QA=q))
  except Exception as e:bad+=1;rows.append(dict(path=r['path'],aceito=False,erro=type(e).__name__+': '+str(e)))
 Path(a.saida).open('x').write(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows));print(json.dumps(dict(total=len(rows),falhas=bad)))
 if bad:raise SystemExit(1)
if __name__=='__main__':main()
