"""Replay conservador de leis AM recentes contra o anexo oficial e sua camada inteira.

Não altera o coletor SAPL geral. Allowlist gráfica limitada aos recursos concretos
revistos no lote de 14/10/2026: brasão, marca-d'água e ornamento sem conteúdo.
"""
import gzip,hashlib,json,re
from pathlib import Path
from pdf_texto_fiel import extrair_camada_textual,conferir_visuais_pdf
from auditar_rn_retomada_pdf import MESES
from markdown_it import MarkdownIt
SHA=lambda b:hashlib.sha256(b).hexdigest()
GRAFICOS_AM=('ba8c56e22e06ad7715e1c01efaf6a7ba1f98699bcf8f2bbba1d1e9cd92a30455','18fb8645fc6b47e1a936330b22258462f06e42d4318dd4a533a3779c5814eb33','2dbf36416f977984f92b1fdf1b2817a1a8ad26e6668941ff152863a9793dde05')

def identidade(text,item):
    m=re.search(r'(?m)^\s*LEI\s+N[º°o.]*\s*([\d.]+),\s*DE\s+(\d{1,2})\s+DE\s+([A-ZÇ]+)\s+DE\s+(\d{4})',text[:1600],re.I)
    if not m:raise ValueError('epígrafe própria de lei não encontrada')
    num=m[1].replace('.','');date=f'{m[4]}-{MESES[m[3].lower()]:02d}-{int(m[2]):02d}'
    if num!=str(item['numero']).replace('.','') or date!=item['data'] or date[:4]!=str(item['ano']):raise ValueError('identidade própria diverge da API')
    if not re.search(r'Art[.]\s*1[º°o]?\s',text):raise ValueError('dispositivo inicial ausente')
    return dict(numero=num,data=date,tipo='Lei Ordinária',epigrafe=' '.join(m[0].split()))

def auditar(r,raw_md=None):
    if r['UF']!='AM' or r['tipo_indice']!='Lei Ordinária' or r.get('http')!=200:raise ValueError('fonte fora do escopo comprovado')
    item=r['item'];url=item['texto_integral'].replace('http://','https://')
    if r['url']!=url or not url.startswith('https://sapl.al.am.leg.br/media/sapl/public/normajuridica/'):raise ValueError('anexo sem identidade oficial')
    z=Path(r['cache']).read_bytes();b=gzip.decompress(z)
    if SHA(z)!=r['sha256_cache'] or SHA(b)!=r['sha256_fonte']:raise ValueError('fonte divergente')
    body,text=extrair_camada_textual(b);identity=identidade(text,item)
    # As dimensões são extraídas da lista; somente o hash exato confere autorização.
    import subprocess,tempfile
    with tempfile.TemporaryDirectory() as tmp:
        p=Path(tmp)/'fonte.pdf';p.write_bytes(b);lines=subprocess.check_output(['/opt/homebrew/bin/pdfimages','-list',str(p)],text=True).splitlines();dims=tuple((int(c[3]),int(c[4])) for line in lines[2:] if (c:=line.split()) and c[0].isdigit())
    visual=conferir_visuais_pdf(b,dims,GRAFICOS_AM)
    pages=text.split('\f');pages=pages[:-1] if pages and not pages[-1].strip() else pages
    if [t.content for t in MarkdownIt('commonmark',{'html':True}).parse(body) if t.type=='fence']!=[p if p.endswith('\n') else p+'\n' for p in pages]:raise ValueError('CommonMark altera camada')
    if raw_md is not None:
        head,rest=raw_md.decode().split('\n---\n',1)
        if rest.split('\n',2)[2]!=body:raise ValueError('corpo diverge da camada integral')
        meta={}
        for line in head.splitlines():
            if ': ' in line:
                k,v=line.split(': ',1)
                try:meta[k]=json.loads(v)
                except ValueError:meta[k]=v
        for k in ('numero','data','tipo'):
            if meta[k]!=identity[k]:raise ValueError('metadado diverge: '+k)
        if meta.get('fonte')!=f"https://sapl.al.am.leg.br/norma/{item['id']}" or meta.get('arquivo')!=r['url'] or meta.get('revogada') is not None:raise ValueError('fonte/revogação não comprovadas')
    return body,dict(**identity,sha256_camada=SHA(text.encode()),sha256_fonte=SHA(b),sha256_corpo=SHA(body.encode()),total_paginas=len(pages),pdfimages=visual,CommonMark_cercas_iguais=True)
