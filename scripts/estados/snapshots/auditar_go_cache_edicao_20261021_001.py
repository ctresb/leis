"""Inventário offline GO: sinais de edição/status, sem certificar vigência ou alterar MD.

Apenas tachado literal de tags/estilo inline é atribuído a trechos; CSS local/externo
é inventariado e exige revisão contextual. Repetição não tachada não vira máscara.
"""
import argparse, collections, datetime, gzip, hashlib, json, re
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo
from markdown_it import MarkdownIt
from pe_fidelidade_visivel import texto_visivel_html
PARSER=MarkdownIt("commonmark", {"html":True}).enable("table")

SHA = lambda b: hashlib.sha256(b).hexdigest()
SP = lambda s: ' '.join(s.split())
VOID = {'br','hr','img','meta','link','input','wbr','col','area','base','embed','param','source'}
POT = re.compile(r'line-through|display\s*:\s*none|visibility\s*:\s*(?:hidden|collapse)|mso-hide\s*:\s*all|(?:^|[;{])\s*opacity\s*:\s*0(?:\.0*)?\s*(?:!important\s*)?(?:[;}]|$)|font-size\s*:\s*0(?:\.0*)?(?:[a-z%]+)?\s*(?:!important\s*)?(?:[;}]|$)',re.I)
class Sinais(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.stack=[];self.old=[];self.live=[];self.attrs=collections.Counter();self.visual=collections.Counter();self.blocks=[];self.current=[];self.css=[];self.rules=[]
    def handle_starttag(self,t,a):
        a=dict(a); inherited=any(x[1] for x in self.stack);skip=t in {'head','style','script','title','xml'} or any(x[2] for x in self.stack)
        old=inherited or t in {'strike','s','del'} or bool(re.search('line-through',a.get('style',''),re.I))
        for k in ('class','style'):
            if k in a:self.attrs[k+'='+a[k]]+=1
        if t in {'img','svg','canvas','object','iframe','embed','video','audio'}:self.visual[t]+=1
        if t in {'p','div','li','tr','td','th','br'}:self.handle_data(' ')
        if t not in VOID:self.stack.append((t,old,skip))
    def handle_endtag(self,t):
        if t=='style' and self.css:self.rules.append(''.join(self.css));self.css=[]
        if t in {'p','div','li','tr','td','th'}:self.handle_data(' ')
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==t:del self.stack[i:];break
        if self.current and not any(x[1] for x in self.stack):
            text=SP(''.join(self.current));self.current=[]
            if len(text)>=70:self.blocks.append(text)
    def handle_data(self,d):
        if any(x[0]=='style' for x in self.stack):self.css.append(d)
        if any(x[2] for x in self.stack):return
        old=any(x[1] for x in self.stack)
        (self.old if old else self.live).append(d)
        if old:self.current.append(d)

def metadata(raw):
    front=raw.split('\n---\n',1)[0];out={}
    for line in front.splitlines():
        if ': ' not in line:continue
        k,v=line.split(': ',1)
        try:out[k]=json.loads(v)
        except (ValueError,TypeError):out[k]=v
    return out

def one(path,indice):
    p=Path(path); b=p.read_bytes(); md=b.decode('utf-8');m=metadata(md); cache=Path('estaduais/GO/_fonte')/p.relative_to('estaduais/GO');cache=cache.with_suffix('.html.gz')
    r=dict(path=path,sha256_md=SHA(b),cache=str(cache),numero=m.get('numero'),data=m.get('data'),situacao=m.get('situacao'),revogada=m.get('revogada'),versao_texto=m.get('versao_texto'))
    ident=re.search(r'-id(\d+)\.md$',path); ident=ident[1] if ident else '';it=indice.get(ident);r['id_oficial']=ident;r['item_indice']=it
    if not cache.exists():return dict(r,erro='cache ausente; sem inferência de defeito')
    z=cache.read_bytes();src=gzip.decompress(z);s=src.decode('utf-8');q=Sinais();q.feed(s);q.close();live=SP(''.join(q.live));body=texto_visivel_html(PARSER.render(md.split('\n---\n',1)[1])) if q.blocks else '';examples=[]
    for t in q.blocks:
        if t in body and t not in live and t not in examples:examples.append(t)
    status=((it or {}).get('estado_legislacao') or {}).get('nome'); supported={'Em Vigor':False,'Revogada':True};r.update(sha256_cache=SHA(z),sha256_fonte=SHA(src),bytes_fonte=len(src),situacao_indice=status,revogada_proposta=supported.get(m.get('situacao')),status_exige_revisao=m.get('situacao') not in supported and m.get('revogada') is not None,atributos=dict(q.attrs),visuais=dict(q.visual),caracteres_tachados=len(SP(''.join(q.old))),regras_CSS_potenciais=[x for x in q.rules if POT.search(x)],atributos_potenciais={k:v for k,v in q.attrs.items() if POT.search(k) or re.search('strike|tachad|riscad|revogad|ocult|desativ',k,re.I)},trechos_tachados_exclusivos_presentes_MD=examples[:8],total_trechos_exclusivos=len(examples),limite='Trecho literal tachado encontrado no Markdown não prova sozinho apresentação vigente: exige renderização CommonMark e contexto. CSS externo não certificado. Cache é campo conteudo, não resposta JSON integral.')
    return r

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--lista',required=True);ap.add_argument('--saida',required=True);a=ap.parse_args();idx={str(x['id']):x for x in json.loads(Path('estaduais/GO/_indice/legislacoes.json').read_text())}
    with Path(a.saida).open('x') as out:
        for n,p in enumerate(Path(a.lista).read_text().splitlines(),1):
            if not p.startswith('estaduais/GO/') or '..' in Path(p).parts:raise ValueError(p)
            r=one(p,idx);r['auditado_em']=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat();out.write(json.dumps(r,ensure_ascii=False)+'\n');out.flush()
            if n%100==0:print('PROGRESSO',n,flush=True)
