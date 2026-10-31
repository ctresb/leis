# -*- coding: utf-8 -*-
from pathlib import Path
import sys,json,re,gzip,hashlib,html,collections
from html.parser import HTMLParser
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from markdown_it import MarkdownIt
from pe import limites_texto_html
from pe_fidelidade_visivel import texto_visivel_html,_heading_comprovado,assinatura_numerica
R=Path.cwd();parser=MarkdownIt('commonmark',{'html':True}).enable('table');sha=lambda b:hashlib.sha256(b).hexdigest()
class Counters(HTMLParser):
 def __init__(self,lists):super().__init__(convert_charrefs=False);self.lists=iter(lists);self.stack=[];self.out=[];self.proofs=[]
 def handle_starttag(self,tag,attrs):
  self.out.append(self.get_starttag_text());d=dict(attrs)
  if tag=='ol':
   ast=next(self.lists);start=int(d.get('start','1'));assert start==ast['start'];self.stack.append(dict(n=start,ast=ast));self.proofs.append(dict(ast=ast,html_start=d.get('start'),inicio_efetivo=start,contadores=[]))
  elif tag=='ul':self.stack.append(None)
  elif tag=='li' and self.stack and self.stack[-1] is not None:
   ctx=self.stack[-1];n=int(d.get('value',ctx['n']));ctx['n']=n+1;prefix=str(n)+ctx['ast']['markup']+' ';self.out.append(html.escape(prefix));next(p for p in reversed(self.proofs) if p['ast'] is ctx['ast'])['contadores'].append(n)
 def handle_endtag(self,tag):
  self.out.append('</'+tag+'>')
  if tag in ('ol','ul'):self.stack.pop()
 def handle_data(self,s):self.out.append(s)
 def handle_entityref(self,s):self.out.append('&'+s+';')
 def handle_charref(self,s):self.out.append('&#'+s+';')
def one(p):
 raw=(R/p).read_bytes();body=raw.decode().split('\n---\n',1)[1].split('\n',1)[1];body=re.sub(r'^# [^\n]*\n','',body,count=1).strip();cache=R/'estaduais/PE/_fonte'/Path(p).relative_to('estaduais/PE').with_suffix('.html.gz');z=cache.read_bytes();s=gzip.decompress(z).decode();a,b=limites_texto_html(s,fragmento='id="divTexto"' not in s);field=s[a:b];assert not re.search(r'<(?:ol|ul)\b',field,re.I),'Listas HTML nativas exigem outra associação contextual';source=texto_visivel_html(field);tokens=parser.parse(body);lists=[]
 for t in tokens:
  if t.type=='ordered_list_open':lists.append(dict(start=t.attrGet('start') or 1,markup=t.markup,linhas=t.map))
 rendered=parser.render(body);c=Counters(lists);c.feed(rendered);normalized,headings=_heading_comprovado(texto_visivel_html(''.join(c.out)),body,source);ok=source==normalized;nums=assinatura_numerica(source)==assinatura_numerica(normalized);i=next((i for i,(x,y) in enumerate(zip(source,normalized)) if x!=y),min(len(source),len(normalized)))
 return dict(path=p,sha256_md=sha(raw),cache=str(cache.relative_to(R)),sha256_cache=sha(z),sha256_campo=sha(field.encode()),sha256_html_renderizado=sha(rendered.encode()),listas=c.proofs,normalizacao_apresentacao='Delimitador de lista manual da AST preservado; apenas número efetivo do HTML ol/start/li incrementado. Não copiar números manuais da fonte.',igualdade_visivel=ok,assinatura_numerica_confere=nums,aceito=ok and nums,contexto=None if ok else dict(fonte=source[max(0,i-100):i+200],md=normalized[max(0,i-100):i+200]))

if __name__ == '__main__':
 import argparse
 ap=argparse.ArgumentParser(description='QA somente leitura de CommonMark, com contadores efetivos de listas; requer markdown-it-py==4.0.0.')
 ap.add_argument('--lista',required=True);ap.add_argument('--saida',required=True);args=ap.parse_args()
 with Path(args.saida).open('x') as output:
  for p in Path(args.lista).read_text().splitlines():
   if not p:continue
   if not p.startswith('estaduais/PE/decretos/') or '..' in Path(p).parts or not p.endswith('.md'):raise ValueError(p)
   try:r=one(p)
   except Exception as e:r=dict(path=p,aceito=False,erro=type(e).__name__+': '+str(e))
   output.write(json.dumps(r,ensure_ascii=False)+'\n');output.flush()
