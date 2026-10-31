"""Captura serial de links HTML SPL observados em seleção congelada; sem MD."""
import argparse,datetime,gzip,hashlib,json,os,time
from pathlib import Path
from urllib.parse import urlparse
from coletar_rn_fontes import capturar
from spl_indice_html import BASES
SHA=lambda b:hashlib.sha256(b).hexdigest()

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--selecao',required=True);ap.add_argument('--pasta',required=True);ap.add_argument('--recibo',required=True);a=ap.parse_args();source=Path(a.selecao);selection=json.loads(source.read_text());base=Path(a.pasta);base.mkdir(parents=True,exist_ok=False);rows=[];bad=0;stop=False
 with (base/'capturas.jsonl').open('x') as out:
  for item in selection:
   if not Path('.git').exists():raise RuntimeError('volume/repositório ausente; não criar caminhos')
   if len(item['textos_completos_observados'])!=1:rows.append(dict(item=item,erro='link integral não único'));continue
   url=item['textos_completos_observados'][0]
   if urlparse(url).netloc!=urlparse(BASES[item['UF']]).netloc:raise ValueError('origem diferente da fonte oficial')
   time.sleep(1.2)
   try:
    st,b,h,end=capturar(url);p=base/(SHA(b)+'.bin.gz')
    if not p.exists():p.write_bytes(gzip.compress(b))
    row=dict(item=item,url=url,url_final=end,http=st,cache=str(p),sha256_fonte=SHA(b),sha256_cache=SHA(p.read_bytes()),headers={k:v for k,v in h.items() if k.lower() not in ['set-cookie','cookie','authorization','proxy-authorization']},capturado_em=datetime.datetime.now().astimezone().isoformat());bad=bad+1 if st>=500 else 0
   except Exception as e:row=dict(item=item,url=url,erro=type(e).__name__+': '+str(e),capturado_em=datetime.datetime.now().astimezone().isoformat());bad+=1
   rows.append(row);out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush();os.fsync(out.fileno());print(item['UF'],item['id'],row.get('http',row.get('erro')),len(rows),'/',len(selection),flush=True)
   if row.get('http') in [401,403,429] or bad>=3:stop=True;break
 receipt=dict(preparado_em=datetime.datetime.now().astimezone().isoformat(),selecao=str(source),sha256_selecao=SHA(source.read_bytes()),total_selecionado=len(selection),capturas=rows,parada_conservadora=stop,sem_MD=True,headers_sessao_omitidos=True);Path(a.recibo).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
 if stop:raise SystemExit(1)
if __name__=='__main__':main()
