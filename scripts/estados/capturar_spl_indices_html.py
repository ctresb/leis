"""Captura serial dos índices HTML SPL com formulário público e checkpoints íntegros.

Não usa exportação CSV, não busca nomes de arquivo presumidos e não gera MD.
"""
import argparse,datetime,gzip,hashlib,http.cookiejar,json,os,time,urllib.request,urllib.parse,urllib.error
from pathlib import Path
from lxml import html
from spl_indice_html import BASES,ler_indice
SHA=lambda b:hashlib.sha256(b).hexdigest()
DDL='ctl00$ContentPlaceHolder1$ddl_ItensExibidos';NEXT='ctl00$ContentPlaceHolder1$lbNext'

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--uf',choices=BASES,required=True);ap.add_argument('--bloco',action='append',required=True,help='tipo:ano observado em índice anterior');ap.add_argument('--pasta',required=True);ap.add_argument('--recibo',required=True);a=ap.parse_args();base=Path(a.pasta);base.mkdir(parents=True,exist_ok=False);op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()));rows=[];items=[];last=0;stop=False;bad=0
 def fetch(url,fields=None):
  nonlocal last,bad
  time.sleep(max(0,1.2-(time.monotonic()-last)));last=time.monotonic();data=urllib.parse.urlencode(fields).encode() if fields is not None else None;req=urllib.request.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (compatible; constituicao-md/1.0)','Content-Type':'application/x-www-form-urlencoded'} if data else {'User-Agent':'Mozilla/5.0 (compatible; constituicao-md/1.0)'})
  try:
   with op.open(req,timeout=120) as res:st=res.status;b=res.read();headers=dict(res.headers.items());end=res.geturl()
  except urllib.error.HTTPError as e:st=e.code;b=e.read();headers=dict(e.headers.items());end=e.geturl()
  p=base/(SHA(b)+'.html.gz')
  if not p.exists():p.write_bytes(gzip.compress(b))
  r=dict(url=url,url_final=end,metodo='POST' if fields is not None else 'GET',campos_publicos=[k for k in fields or {} if not k.startswith('__')],postback=fields.get('__EVENTTARGET') if fields else None,http=st,cache=str(p),sha256_fonte=SHA(b),sha256_cache=SHA(p.read_bytes()),headers={k:v for k,v in headers.items() if k.lower() not in ['set-cookie','cookie','authorization','proxy-authorization']},capturado_em=datetime.datetime.now().astimezone().isoformat());rows.append(r)
  with (base/'capturas.jsonl').open('a') as out:out.write(json.dumps(r,ensure_ascii=False)+'\n');out.flush();os.fsync(out.fileno())
  print(st,r['metodo'],url,flush=True);bad=bad+1 if st>=500 else 0
  if st in [401,403,429] or bad>=3:raise RuntimeError('parada por recusa/falhas consecutivas')
  if st!=200:raise RuntimeError('índice HTTP '+str(st))
  return b,r
 def hidden(b):
  d=html.fromstring(b.decode('utf-8',errors='strict'));return d,{x.get('name'):x.get('value','') for x in d.xpath('//input[translate(@type,"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz")="hidden"]') if x.get('name')}
 try:
  for spec in a.bloco:
   tipo,ano=spec.split(':');ano=int(ano);url=f'{BASES[a.uf]}/legislacao/consulta-legislacao.aspx?tipo={tipo}&ano={ano}';b,r=fetch(url);doc,h=hidden(b);options=doc.xpath('//select[@name="'+DDL+'"]//option/@value')
   if '100' not in options:raise ValueError('opção 100 não observada no formulário')
   b,r=fetch(url,{**h,'__EVENTTARGET':DDL,'__EVENTARGUMENT':'',DDL:'100'});seen=set();page=0
   while True:
    page+=1;parsed=ler_indice(b,url,a.uf,tipo,ano)
    if any(x['id'] in seen for x in parsed):raise ValueError('ID/página repetido, não declarar catálogo completo')
    seen.update(x['id'] for x in parsed)
    for x in parsed:x.update(indice=r,pagina_observada=page);items.append(x)
    with (base/'itens.jsonl').open('a') as out:out.write(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in parsed));out.flush();os.fsync(out.fileno())
    doc,h=hidden(b);n=doc.xpath('//a[contains(@id,"lbNext")]');enabled=[x for x in n if 'aspNetDisabled' not in x.get('class','') and x.get('href','').startswith('javascript:__doPostBack')]
    print('ITENS',spec,page,len(parsed),'acumulado',len(seen),'next',bool(enabled),flush=True)
    if not enabled:break
    if len(enabled)!=1:raise ValueError('próximo não único')
    b,r=fetch(url,{**h,DDL:'100','__EVENTTARGET':NEXT,'__EVENTARGUMENT':''})
 except Exception as e:stop=True;error=type(e).__name__+': '+str(e);print('PARADA',error,flush=True)
 receipt=dict(preparado_em=datetime.datetime.now().astimezone().isoformat(),uf=a.uf,blocos=a.bloco,capturas=rows,total_itens=len(items),itens=str(base/'itens.jsonl'),parada_conservadora=stop,erro=error if stop else None,sem_MD=True,omissao_headers_sessao=True,postback_tokens_nao_gravados=True)
 if (base/'itens.jsonl').exists():receipt['sha256_itens']=SHA((base/'itens.jsonl').read_bytes())
 Path(a.recibo).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
 if stop:raise SystemExit(1)
if __name__=='__main__':main()
