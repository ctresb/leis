"""Captura serial somente de recursos raster presentes nas fontes HTML selecionadas."""
import argparse,datetime,gzip,hashlib,json,time,os
from pathlib import Path
from urllib.parse import urljoin,urlparse
from lxml import html
from comum import decodificar
from coletar_rn_fontes import capturar
SHA=lambda b:hashlib.sha256(b).hexdigest()

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--capturas',required=True);ap.add_argument('--pasta',required=True);ap.add_argument('--recibo',required=True);ap.add_argument('--recursos-anteriores',action='append',default=[]);a=ap.parse_args();base=Path(a.pasta);base.mkdir(parents=True,exist_ok=False);inputs=json.loads(Path(a.capturas).read_text());inputs=inputs.get('capturas',inputs) if isinstance(inputs,dict) else inputs;rows=[];seen={};bad=0;stop=False
 for previous in a.recursos_anteriores:
  for row in json.loads(Path(previous).read_text())['capturas']:
   if row.get('http')!=200 or row.get('url_final')!=row.get('url'):continue
   if SHA(Path(row['arquivo']).read_bytes())!=row['sha256']:raise ValueError('recurso anterior diverge do SHA')
   if row['url'] in seen and seen[row['url']]['sha256']!=row['sha256']:raise ValueError('capturas anteriores da mesma URL divergem')
   seen[row['url']]=dict(row,manifesto_reuso=previous,id_captura_original=row['id'])
 with (base/'capturas.jsonl').open('x') as out:
  for r in inputs:
   raw=gzip.decompress(Path(r['cache']).read_bytes());assert SHA(raw)==r['sha256_fonte'];doc=html.fromstring(decodificar(raw))
   for src in doc.xpath('//img/@src'):
    if not Path('.git').exists():raise RuntimeError('volume/repositório ausente')
    url=urljoin(r['url_final'],src)
    if urlparse(url).netloc!=urlparse(r['url_final']).netloc:raise ValueError('imagem em outra origem exige revisão')
    if url in seen:row=dict(seen[url],id=r['item']['id'],reutilizado=True)
    else:
     time.sleep(1.2)
     try:st,b,h,end=capturar(url)
     except Exception as e:rows.append(dict(id=r['item']['id'],url=url,erro=str(e)));stop=True;break
     p=base/(SHA(b)+'.bin')
     if not p.exists():p.write_bytes(b)
     row=dict(id=r['item']['id'],url=url,url_final=end,http=st,arquivo=str(p),sha256=SHA(b),capturado_em=datetime.datetime.now().astimezone().isoformat());seen[url]=row;bad=bad+1 if st>=500 else 0
    rows.append(row);out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush();os.fsync(out.fileno());print(row['id'],row['http'],row['sha256'][:12],len(rows),flush=True)
    if row['http'] in [401,403,429] or bad>=3:stop=True;break
   if stop:break
 Path(a.recibo).write_text(json.dumps(dict(capturas=rows,parada_conservadora=stop,selecao=a.capturas,sha256_selecao=SHA(Path(a.capturas).read_bytes()),recursos_anteriores={p:SHA(Path(p).read_bytes()) for p in a.recursos_anteriores},headers_sessao_nao_gravados=True),ensure_ascii=False,indent=2)+'\n')
 if stop:raise SystemExit(1)
if __name__=='__main__':main()
