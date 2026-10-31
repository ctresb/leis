"""HTML nativo explícito do campo materia do Legisla.AM, sem alterar normativa.

Usa somente a validação congelada DOU, sem modificar seu código/modo. O wrapper
texto-dou é temporário e não aparece no resultado. Elementos/classes dependentes
de CSS desconhecido permanecem retidos para revisão contextual.
"""
from html.parser import HTMLParser
import re
from representacao_html_dou import representar_fragmento as validar_dou,MODO_HTML_NATIVO as MODO_DOU
MODO='html-nativo-materia-legisla-am-v1'
VOID={'br','hr','img','meta','link','input','wbr','col','area','base','embed','param','source'}
class Campo(HTMLParser):
    def __init__(self,source):
        super().__init__(convert_charrefs=False);self.source=source;self.lines=[0]+[m.end() for m in re.finditer('\n',source)];self.depth=0;self.start=None;self.end=None;self.count=0
    def pos(self):
        l,c=self.getpos();return self.lines[l-1]+c
    def handle_starttag(self,t,a):
        a=dict(a)
        if t=='div':
            if 'materia' in (a.get('class') or '').split():
                self.count+=1
                if self.start is not None:raise ValueError('campo materia repetido/nested')
                self.start=self.pos();self.depth=1
            elif self.start is not None and self.end is None:self.depth+=1
    def handle_endtag(self,t):
        if t=='div' and self.start is not None and self.end is None:
            self.depth-=1
            if self.depth==0:self.end=self.source.index('>',self.pos())+1

def extrair_campo(source):
    p=Campo(source);p.feed(source);p.close()
    if p.count!=1 or p.start is None or p.end is None:raise ValueError('campo materia único/fechado não comprovado')
    return source[p.start:p.end],(p.start,p.end)

class Textos(HTMLParser):
    def __init__(self,s):
        super().__init__(convert_charrefs=False);self.s=s;self.lines=[0]+[m.end() for m in re.finditer('\n',s)];self.ranges=[];self.classes=[]
    def handle_starttag(self,t,a):
        for k,v in a:
            if k=='class' and v:
                if not (t=='div' and set(v.split())<= {'materia','rounded'}):raise ValueError('classe interna exige CSS contextual: '+v)
                self.classes.extend(v.split())
            if k.lower().startswith('data-'):raise ValueError('atributo dinâmico exige contexto')
            if k=='style' and re.search(r'font-family\s*:\s*["\x27]?\s*(?:Symbol|Wingdings|Webdings)\b',v or '',re.I):raise ValueError('fonte de símbolos exige revisão')
    def handle_startendtag(self,t,a):self.handle_starttag(t,a)
    def handle_data(self,d):
        l,c=self.getpos();p=self.lines[l-1]+c;self.ranges.append((p,p+len(d)))

def representar(fragmento,*,modo):
    if modo!=MODO:raise ValueError('modo Legisla.AM desconhecido')
    s=fragmento.replace('\r\n','\n').replace('\r','\n');p=Textos(s);p.feed(s);p.close();trocas=[]
    for a,b in p.ranges:
        for m in re.finditer('\n',s[a:b]):trocas.append(a+m.start())
    for i in reversed(trocas):s=s[:i]+'&#10;'+s[i+1:]
    if re.search(r'\n[ \t]*\n',s):raise ValueError('linha vazia em markup/atributo exige revisão')
    prefix='<div class="texto-dou">';out=validar_dou(prefix+s+'</div>',modo=MODO_DOU)
    if not out.startswith(prefix) or not out.endswith('</div>'):raise ValueError('wrapper de segurança diverge')
    return out[len(prefix):-6]
