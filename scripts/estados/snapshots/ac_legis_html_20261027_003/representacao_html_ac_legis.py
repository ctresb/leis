"""Campo normativo LEGIS/AC explícito, com fonte integral preservada pelo chamador.

Retém anexos/controles não vazios ou qualquer texto após o rodapé. Só exclui a
interface fixa e vazia de downloads comprovada, nunca um anexo por suposição.
"""
from html.parser import HTMLParser
import hashlib,re
from lxml import html
from representacao_html_dou import representar_fragmento,MODO_HTML_NATIVO
MODO='html-nativo-body-law-legis-ac-v1'
SHA=lambda s:hashlib.sha256(s.encode()).hexdigest()

class _Limites(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=False);self.s=s;self.lines=[0]+[m.end() for m in re.finditer('\n',s)];self.start=None;self.end=None;self.fields=0;self.footers=0;self.span=0;self.divs=0;self.depth_end=None
 def pos(self):
  l,c=self.getpos();return self.lines[l-1]+c
 def handle_starttag(self,t,a):
  attrs=dict(a)
  if t=='div' and attrs.get('id')=='body-law':self.fields+=1;self.start=self.pos();self.divs=1
  elif self.start is not None and self.end is None and t=='div':self.divs+=1
  if t=='span' and attrs.get('id')=='texto_publicado_doe':self.footers+=1;self.span=1
  elif self.span and t=='span':self.span+=1
 def handle_endtag(self,t):
  if self.start is not None and self.end is None and t=='div':self.divs-=1
  if self.span and t=='span':
   self.span-=1
   if not self.span:self.end=self.s.index('>',self.pos())+1;self.depth_end=self.divs


def _posterior_vazio(node):
 if isinstance(node,html.HtmlComment):
  # Placeholder comentado literal da própria interface; não condicional Word.
  d=html.fromstring('<div>'+(node.text or '')+'</div>')
  return d.text_content().strip()=='*' and all(e.tag in ['div','p','span'] for e in d.iter()) and not any(k.lower().startswith('on') for e in d.iter() for k in e.attrib)
 if node.tag=='p':return not node.attrib and len(node)==0 and not (node.text or '').strip()
 if node.tag!='div' or set(node.get('class','').split())!={'row'}:return False
 if re.sub(r'\s','',node.get('style','')).lower() not in ['display:none;','display:none']:return False
 if set(node.attrib)-{'class','style'}:return False
 if any(e.tag not in ['div','table','thead','tr','th','tbody'] for e in node.iter()):return False
 if any(k.lower().startswith(('on','data-')) for e in node.iter() for k in e.attrib):return False
 if node.xpath('.//tbody/tr|.//a|.//img|.//script'):return False
 headers=[' '.join(e.text_content().split()) for e in node.xpath('.//thead/tr/th')]
 return headers==['NOME DO ARQUIVO','LINK PARA DOWNLOAD'] and re.sub(r'\s','',node.text_content())==re.sub(r'\s','',''.join(headers))


def extrair_campo(source):
 d=html.document_fromstring(source);fields=d.xpath('//*[@id="body-law"]');footers=d.xpath('//*[@id="texto_publicado_doe"]')
 if len(fields)!=1 or len(footers)!=1:raise ValueError('campo/rodapé não único')
 field,footer=fields[0],footers[0]
 if footer.getparent() is not field:raise ValueError('rodapé não é filho direto do campo; estrutura exige revisão')
 if not footer.text_content().strip().startswith('Este texto não substitui o publicado no DOE'):raise ValueError('marcador final não é a ressalva editorial esperada')
 if (footer.tail or '').strip():raise ValueError('texto posterior ao rodapé exige contexto')
 excluded=[]
 for sibling in footer.itersiblings():
  if not _posterior_vazio(sibling) or (sibling.tail or '').strip():raise ValueError('material/anexo posterior ao rodapé exige contexto')
  excluded.append(dict(tag=sibling.tag if isinstance(sibling.tag,str) else 'comentario',sha256_HTML_derivado=SHA(html.tostring(sibling,encoding='unicode')),texto=' '.join(sibling.text_content().split()) if isinstance(sibling.tag,str) else 'placeholder comentado de asterisco'))
 p=_Limites(source);p.feed(source);p.close()
 if p.fields!=1 or p.footers!=1 or p.start is None or p.end is None or p.depth_end!=1:raise ValueError('limites/fechamento do campo não comprovados')
 raw=source[p.start:p.end];fragment=raw+'</div>'
 return fragment,dict(inicio=p.start,fim_rodape=p.end,sha256_intervalo_literal=SHA(raw),fechamento_contêiner='</div> acrescentado exclusivamente para fechar o contêiner do fragmento após o marcador final; nenhum texto normativo modificado.',posterior_nao_normativo_comprovado=excluded,limite='Campo até ressalva editorial, mantendo a fonte HTML integral. Somente espaço/placeholder de asterisco e interface vazia posterior são excluídos; links/anexos/texto adicionais geram retenção.')

class _Textos(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=False);self.s=s;self.lines=[0]+[m.end() for m in re.finditer('\n',s)];self.ranges=[]
 def handle_data(self,data):
  l,c=self.getpos();start=self.lines[l-1]+c;self.ranges.append((start,start+len(data)))


def representar(fragmento,*,modo):
 if modo!=MODO:raise ValueError('modo LEGIS/AC desconhecido')
 s=fragmento.replace('\r\n','\n').replace('\r','\n');p=_Textos(s);p.feed(s);p.close();newlines=[]
 for a,b in p.ranges:
  newlines.extend(a+m.start() for m in re.finditer('\n',s[a:b]))
 parts=[];last=0
 for i in newlines:parts.extend([s[last:i],'&#10;']);last=i+1
 parts.append(s[last:]);s=''.join(parts)
 if re.search(r'\n[ \t]*\n',s):raise ValueError('linha vazia em markup/atributo exige revisão')
 prefix='<div class="texto-dou">';out=representar_fragmento(prefix+s+'</div>',modo=MODO_HTML_NATIVO)
 if not out.startswith(prefix) or not out.endswith('</div>'):raise ValueError('wrapper temporário divergiu')
 return out[len(prefix):-6]
