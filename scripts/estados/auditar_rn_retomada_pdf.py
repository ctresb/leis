"""QA RN de PDF oficial: identidade própria e camada integral sem excluir números.

Recursos raster só são aceitos por hash exato visualmente revisto. A revisão humana
das páginas e dos anexos é registrada no manifesto de publicação, separadamente.
"""
import gzip,hashlib,json,re
from pathlib import Path
from pdf_texto_fiel import extrair_camada_textual,conferir_visuais_pdf

MESES={m:i for i,m in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split(),1)}
BRASOES=('fa8f45cbee563a8d2b2cd9e7cabff21672bc5e88a6c8e4715a5eb5308e305268','b73976f9c0333613f04710b41544c76a09ee78671eefdbc58694f95e17fa6034','c8b0ad00468157a4879b6b452ece4f4407b8c8b90576f9d309350bcb9ee2faa5')
DIMENSOES=((211,220),(215,225))
SHA=lambda b:hashlib.sha256(b).hexdigest()
SP=lambda s:' '.join(s.split())

def identidade(texto,item):
    m=re.search(r'(?m)^\s*(LEI(?:\s+COMPLEMENTAR)?)\s+N[º°o.]?\s*([\d.]+),\s*DE\s+(\d{1,2})\s+DE\s+([A-ZÇ]+)\s+DE\s+(\d{4})[.]?',texto[:2000],re.I)
    if not m:raise ValueError('epígrafe própria não reconhecida')
    expected=re.search(r'(\d[\d.]*)\s+de\s+(\d{1,2})[.](\d{1,2})[.](\d{4})',item['titulo'],re.I)
    if not expected:raise ValueError('identidade do índice não reconhecida')
    numero=m[2].replace('.','');data=f'{m[5]}-{MESES[m[4].lower()]:02d}-{int(m[3]):02d}';dateindex=f'{expected[4]}-{int(expected[3]):02d}-{int(expected[2]):02d}'
    if numero!=expected[1].replace('.','') or data!=dateindex:raise ValueError('número/data próprios divergem do índice')
    complement='COMPLEMENTAR' in m[1].upper()
    if complement != (item['lista']=='leis-complementares'):raise ValueError('tipo próprio diverge do índice')
    if not re.search(r'Art[.]\s*1[º°o]?\s',texto):raise ValueError('dispositivo próprio inicial ausente')
    return dict(numero=numero,data=data,tipo='Lei Complementar' if complement else 'Lei Ordinária',epigrafe=SP(m[0]))

def auditar(captura,raw_md=None):
    if captura.get('http')!=200 or not captura.get('PDF'):raise ValueError('captura não comprova PDF oficial HTTP200')
    z=Path(captura['cache']).read_bytes();b=gzip.decompress(z)
    if SHA(z)!=captura['sha256_cache'] or SHA(b)!=captura['sha256_fonte']:raise ValueError('fonte/cache diverge da captura')
    body,text=extrair_camada_textual(b);identity=identidade(text,captura['item']);visual=conferir_visuais_pdf(b,DIMENSOES,BRASOES)
    if raw_md is not None:
        md=raw_md.decode('utf8');header,rest=md.split('\n---\n',1);actual=rest.split('\n',2)[2]
        if actual!=body:raise ValueError('corpo diverge da camada PDF completa')
        meta={}
        for line in header.splitlines():
            if ': ' in line:
                k,v=line.split(': ',1)
                try:meta[k]=json.loads(v)
                except ValueError:meta[k]=v
        for k in ('numero','data','tipo'):
            if meta[k]!=identity[k]:raise ValueError('metadado não confere com epígrafe: '+k)
        if meta.get('fonte')!=captura['url'] or meta.get('revogada') is not None:raise ValueError('fonte/revogação não comprovadas')
    return body,dict(**identity,sha256_fonte=SHA(b),sha256_camada=SHA(text.encode()),sha256_corpo=SHA(body.encode()),pdfimages=visual,fonte_sem_remocao_de_linhas=True,total_paginas=len(text.split('\f'))-(1 if text.endswith('\f') else 0))
