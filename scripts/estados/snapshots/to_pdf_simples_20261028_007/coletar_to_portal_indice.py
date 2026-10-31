"""Índice oficial ALETO serial em lotes; sem PDF ou Markdown canônico."""
import argparse,datetime,gzip,hashlib,json,math,re,subprocess,time
from pathlib import Path
from urllib.parse import urljoin
from lxml import html
B='https://www.al.to.leg.br';SHA=lambda b:hashlib.sha256(b).hexdigest()
def parse(raw):
 text=raw.decode('utf-8',errors='strict');d=html.fromstring(text);visible=' '.join(d.text_content().split());count=re.search(r'Registros encontrados:\s*(\d+)',visible)
 if not count:raise ValueError('resposta sem contagem oficial da listagem')
 items=[];out=[]
 for a in d.xpath('//h4/a'):
  href=a.get('href','');title=' '.join(a.text_content().split());row=a.getparent().getparent().getparent()
  if len(row.xpath('.//h4/a'))!=1:raise ValueError('limite do cartão não comprovado')
  ident=re.fullmatch(r'/arquivo/(\d+)',href);m=re.fullmatch(r'Lei nº ([\d.]+(?:-[A-Za-z]+)?) de (\d{4}) \((ordinária|complementar)\)',title)
  if not ident or not m:out.append(dict(titulo=title,href=href,motivo='tipo/título fora do parser de leis'));continue
  dates=[' '.join(x.text_content().split()) for x in row.xpath('./div/p/small') if 'Data:' in x.text_content()];date=re.fullmatch(r'\|?\s*Data:\s*(\d{2})/(\d{2})/(\d{4})',dates[0]) if len(dates)==1 else None
  dt=datetime.date(int(date[3]),int(date[2]),int(date[1])).isoformat() if date else None;ementas=row.xpath('./div/em/strong');ementa=' '.join(ementas[0].text_content().split()) if len(ementas)==1 else None
  num=m[1].replace('.','').upper();mnum=re.fullmatch(r'(\d+)(-[A-Z]+)?',num);num=str(int(mnum[1]))+(mnum[2] or '')
  items.append(dict(id_ALETO=ident[1],fonte=urljoin(B,href),titulo_indice=title,numero=num,ano_titulo=m[2],tipo='Lei Ordinária' if m[3]=='ordinária' else 'Lei Complementar',pasta='leis-ordinarias' if m[3]=='ordinária' else 'leis-complementares',data_cartao=dt,data_literal=dates[0] if dates else None,ementa=ementa,divergencia_ano_cartao_titulo=dt is not None and dt[:4]!=m[2],indicacao_editorial_compilacao=bool(re.search(r'\(?Revogad[oa]\s+pela|Redaç[aã]o\s+dada|Alterad[oa]\s+pela',ementa or '',re.I))))
 return int(count[1]),items,out

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--saida',required=True);ap.add_argument('--recibo',required=True);ap.add_argument('--inicio-ano',type=int,default=2000);ap.add_argument('--inicio-pagina',type=int,default=1);ap.add_argument('--fim-ano',type=int,default=2019);ap.add_argument('--limite-paginas',type=int,default=60);ap.add_argument('--reuso',action='append',default=[]);a=ap.parse_args();base=Path(a.saida);base.mkdir(parents=True,exist_ok=False);root=Path.cwd();device=root.stat().st_dev;reuse={}
 for name in a.reuso:
  previous=json.loads(Path(name).read_text());previous=previous['capturas'] if isinstance(previous,dict) else previous
  for r in previous:
   if r.get('http')==200:reuse[r['url']]=r
 captures=[];items=[];outside=[];ano=a.inicio_ano;page=a.inicio_pagina;last=0;stop=None
 for i in range(a.limite_paginas):
  if ano>a.fim_ano:break
  if not (root/'.git').exists() or root.stat().st_dev!=device:raise RuntimeError('volume/repositório indisponível; não recriar caminhos')
  url=f'{B}/legislacaoEstadual?documento.ano={ano}&pagPaginaAtual={page}'
  if url in reuse:
   r=dict(reuse[url]);z=Path(r['cache']).read_bytes();b=gzip.decompress(z);assert SHA(z)==r['sha256_cache'] and SHA(b)==r['sha256_fonte'];r['reutilizado']=True
  else:
   time.sleep(max(0,1.2-(time.monotonic()-last)));last=time.monotonic();raw=base/'resposta-privada.body';head=base/'headers-sessao-privados';start=datetime.datetime.now().astimezone().isoformat();p=subprocess.run(['/usr/bin/curl','--silent','--show-error','--location','--max-time','50','--dump-header',str(head),'--output',str(raw),'--write-out','%{http_code} %{url_effective}',url],capture_output=True,text=True);r=dict(url=url,iniciado_em=start,capturado_em=datetime.datetime.now().astimezone().isoformat(),retorno_curl=p.returncode)
   if p.returncode:r['erro']=p.stderr.strip();captures.append(r);stop='erro de captura';break
   code,end=p.stdout.split(' ',1);b=raw.read_bytes();z=gzip.compress(b,mtime=0);cache=base/(SHA(b)+'.html.gz');cache.write_bytes(z);headers={}
   for ln in head.read_text().splitlines():
    if ': ' in ln:
     k,v=ln.split(': ',1)
     if k.lower() not in ['set-cookie','cookie','authorization','proxy-authorization']:headers[k]=v
   r.update(http=int(code),url_final=end,cache=str(cache),sha256_fonte=SHA(b),sha256_cache=SHA(z),headers=headers,headers_sessao_omitidos=True)
  r.update(ano_filtro=ano,pagina=page);captures.append(r)
  if r.get('http')!=200:stop='HTTP não200; sem contorno/repetição';break
  try:count,rows,other=parse(b)
  except Exception as e:r['retencao']=str(e);stop='parser exige contexto';break
  if len(rows)+len(other)>20 or count>20000:r['retencao']='quantidade fora do padrão observado';stop='paginação exige contexto';break
  pages=max(1,math.ceil(count/20));r.update(total_registros_declarado=count,paginas_esperadas=pages)
  if count and not rows and not other:r['retencao']='página vazia antes do fechamento declarado';stop='paginação vazia';break
  for it in rows:it.update(indice=r,ano_filtro=ano,pagina=page)
  items.extend(rows);outside.extend(other);print(ano,page,r['http'],len(rows),count,flush=True)
  if page>=pages:ano+=1;page=1
  else:page+=1
  receipt=dict(codigo=str(Path(__file__).resolve().relative_to(root)),sha256_codigo=SHA(Path(__file__).read_bytes()),capturado_em=datetime.datetime.now().astimezone().isoformat(),capturas=captures,itens=items,fora_escopo=outside,checkpoint=dict(ano=ano,pagina=page),fim_ano=a.fim_ano,parada=stop,sem_MD=True,qualificados=0,metas_inalteradas=True)
  Path(a.recibo).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
 receipt=dict(codigo=str(Path(__file__).resolve().relative_to(root)),sha256_codigo=SHA(Path(__file__).read_bytes()),capturado_em=datetime.datetime.now().astimezone().isoformat(),capturas=captures,itens=items,fora_escopo=outside,checkpoint=dict(ano=ano,pagina=page),fim_ano=a.fim_ano,parada=stop,sem_MD=True,qualificados=0,metas_inalteradas=True)
 Path(a.recibo).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
