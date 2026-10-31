"""Verifica VML legado do cabeçalho contra o fallback raster já revisto; sem rede."""
import re
from html.parser import HTMLParser
from urllib.parse import urljoin
from pe_fidelidade_visivel import texto_visivel_html
class _A(HTMLParser):
    def handle_starttag(self,tag,attrs):self.tag=tag;self.attrs=dict(attrs)
def attrs(tag):
    p=_A();p.feed(tag);return p.attrs

def conferir(source,base,imagens_verificadas):
    parts=re.split(r'<body\b[^>]*>',source,maxsplit=1,flags=re.I)
    if len(parts)!=2:raise ValueError('body não encontrado para análise VML')
    body=re.split(r'</body\s*>',parts[1],maxsplit=1,flags=re.I)[0]
    if re.search(r'<m:oMath(?:Para)?\b',body,re.I):raise ValueError('OfficeMath exige representação própria')
    if re.search(r'<v:(?:group|line|rect|oval|curve|polyline|roundrect|arc|image|textbox|textpath)\b',body,re.I):raise ValueError('desenho/textbox VML exige revisão própria')
    starts=list(re.finditer(r'<v:shape\b[^>]*>',body,re.I));blocks=list(re.finditer(r'<v:shape\b[^>]*>[\s\S]*?</v:shape\s*>',body,re.I));
    if len(starts)>1:raise ValueError('mais de uma picture VML exige revisão própria')
    if len(starts)!=len(blocks):raise ValueError('shape VML sem fechamento')
    allowed={r['url']:r for r in imagens_verificadas};fallback=[]
    for m in re.finditer(r'<img\b[^>]*>',body,re.I):
        a=attrs(m[0]);url=urljoin(base,a.get('src',''))
        if url in allowed:fallback.append(dict(url=url,refs=set(a.get('v:shapes','').split()),sha256=allowed[url]['sha256']))
    out=[]
    for m in blocks:
        a=attrs(re.match(r'<v:shape\b[^>]*>',m[0],re.I)[0]);ids={a[k] for k in ['id','o:spid'] if a.get(k)};matches=[r for r in fallback if ids & r['refs']]
        if a.get('type')!='#_x0000_t75' or not re.search(r'<v:imagedata\b',m[0],re.I) or len(matches)!=1:raise ValueError('VML sem fallback raster decorativo comprovado')
        if re.search(r'\bLEI\b|\bArt[.]',texto_visivel_html(body[:m.start()]),re.I):raise ValueError('VML fora do cabeçalho exige revisão própria')
        out.append(dict(IDs=sorted(ids),tipo=a['type'],fallback=matches[0]['url'],sha256_fallback=matches[0]['sha256'],prova='Picture VML único no cabeçalho institucional, associado por ID ao mesmo fallback raster inspecionado; sem grupo/textbox/OfficeMath ou vetor no articulado.'))
    return dict(pictures_VML_cabecalho=out,OfficeMath_ou_outros_vetores=False,limite='Verificação do fallback da edição HTML pública; não certifica equivalência visual da renderização Word/IE legada.')
