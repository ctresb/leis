"""QA inicial TO para PDF exclusivamente textual; complexos ficam para contexto.

Sem OCR, exclusão de linhas, certificação de vigência ou escrita canônica. Raster,
vetores, anotações, anexos e compilações não recebem exceções automáticas.
"""
import gzip,hashlib,json,re,datetime,io
from pathlib import Path
from urllib.parse import urlsplit
import pdfplumber
from pypdf import PdfReader
from pypdf.generic import ContentStream
from markdown_it import MarkdownIt
from pdf_texto_fiel import extrair_camada_textual
from visibilidade_pdf_to import conferir as conferir_visibilidade
from clipping_pdf_textual_to import conferir as conferir_clipping,PATH
from contexto_to_pdf import primeira_epigrafe,granularidade,anotacoes,documentos
from edicao_anotada_to import conferir_anotacoes
from formulas_to_pdf import FECHO,artigo_inicial,cargo_assinatura
from referencias_inline_to import conferir_referencias
from coletar_to_portal_indice import parse as parse_index
SHA=lambda b:hashlib.sha256(b).hexdigest()
MESES={m:i for i,m in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split(),1)}
HEAD=re.compile(r'\b(LEI(?:\s+COMPLEMENTAR)?)\s+N[º°o.]*\s*([\d.]+(?:\s*-\s*[A-Z]+)?),?\s+DE\s+(\d{1,2})\s*[º°]?\s+DE\s+([A-ZÇ]+)\s+DE\s+(\d{4})',re.I)
# FECHO: gramática sucessora documentada em formulas_to_pdf, sem corrigir o texto.
OPS={b'q',b'Q',b'cm',b'BT',b'ET',b'Tf',b'Tr',b'Tm',b'Td',b'TD',b'T*',b'Tj',b'TJ',b'Tw',b'Tc',b'Ts',b'Tz',b'TL',b'"',b"'",b'g',b'G',b'rg',b'RG',b'k',b'K',b'gs',b'BDC',b'BMC',b'EMC',b'MP',b'DP',b'BX',b'EX'}
OPS |= PATH | {b'i'}
def number(s):
 s=re.sub(r'[.\s]','',s).upper();m=re.fullmatch(r'(\d+)(-[A-Z]+)?',s)
 if not m:raise ValueError('número não reconhecido')
 return str(int(m[1]))+(m[2] or '')
def day(d,m,y):return datetime.date(int(y),MESES[m.lower()],int(d)).isoformat()
def conferir_pdf_simples(raw):
 reader=PdfReader(io.BytesIO(raw));catalog=reader.trailer['/Root'];info=[]
 if len(reader.pages)>30:raise ValueError('PDF longo exige revisão de granularidade/anexos')
 if any(k in catalog for k in ['/OpenAction','/AA']):raise ValueError('PDF contém ação; revisão necessária')
 names=catalog.get('/Names',{});names=names.get_object() if hasattr(names,'get_object') else names
 if any(k in names for k in ['/EmbeddedFiles','/JavaScript']):raise ValueError('PDF contém anexo/ação não representado')
 form=catalog.get('/AcroForm');form=form.get_object() if form else {}
 if form.get('/Fields') or form.get('/XFA'):raise ValueError('PDF contém formulário não representado')
 with pdfplumber.open(io.BytesIO(raw)) as doc:
  for i,page in enumerate(doc.pages):
   if page.images or page.lines or page.rects or page.curves:raise ValueError('PDF com raster/vetor exige revisão gráfica individual')
   p=reader.pages[i]
   if p.get('/Annots') or p.get('/AA'):raise ValueError('PDF contém anotações; contexto necessário')
   res=p.get('/Resources',{});res=res.get_object() if hasattr(res,'get_object') else res
   if res.get('/XObject'):raise ValueError('XObject exige revisão gráfica/recursiva')
   fonts=res.get('/Font',{});fonts=fonts.get_object() if hasattr(fonts,'get_object') else fonts
   for font in fonts.values():
    if font.get_object().get('/Subtype')=='/Type3':raise ValueError('fonte Type3 exige revisão')
   states=res.get('/ExtGState',{});states=states.get_object() if hasattr(states,'get_object') else states
   for st in states.values():
    st=st.get_object()
    if set(st)-{'/Type','/OPM','/OP','/op','/SA','/SM','/BM','/ca','/CA','/SMask'}:raise ValueError('estado gráfico PDF desconhecido')
    if float(st.get('/ca',1))!=1 or float(st.get('/CA',1))!=1 or st.get('/BM','/Normal')!='/Normal' or st.get('/SMask','/None')!='/None':raise ValueError('transparência/ocultação PDF exige revisão')
   operations=ContentStream(p.get_contents(),reader).operations
   if any(op not in OPS for args,op in operations):raise ValueError('operador PDF fora do subconjunto puramente textual')
   if any(op==b'Tr' and args!=[0] for args,op in operations):raise ValueError('modo de renderização textual não padrão')
   for c in page.chars:
    color=c.get('non_stroking_color');black=color in (0,0.0,(0,),(0.0,),(0,0,0),(0.0,0.0,0.0),(0,0,0,1))
    if not black:raise ValueError('texto colorido/oculto exige contexto')
    if not c.get('upright') or c['x0'] < -1 or c['x1']>page.width+1 or c['top'] < -1 or c['bottom']>page.height+1:raise ValueError('texto rotacionado/fora da página exige contexto')
    if re.search(r'wingdings|webdings|symbol',c.get('fontname',''),re.I):raise ValueError('fonte simbólica exige contexto')
   info.append(dict(pagina=i+1,caracteres=len(page.chars),raster=0,linhas=0,retangulos=0,curvas=0,anotacoes=0,operadores=sorted(set(op.decode() for args,op in operations))))
 return info

def auditar(row,body_atual=None):
 it=row['item'];packed=Path(row['cache']).read_bytes();raw=gzip.decompress(packed);original=urlsplit(row['url']);final=urlsplit(row['url_final'])
 if row.get('http')!=200 or original.scheme!='https' or final.scheme!='https' or original.hostname!='www.al.to.leg.br' or final.hostname!='www.al.to.leg.br' or not re.fullmatch(r'/arquivo/\d+',original.path):raise ValueError('fonte oficial/HTTP não confere')
 if SHA(packed)!=row['sha256_cache'] or SHA(raw)!=row['sha256_fonte'] or not raw.startswith(b'%PDF'):raise ValueError('fonte/cache PDF diverge')
 if it['fonte']!=row['url'] or it['id_ALETO']!=original.path.rsplit('/',1)[-1]:raise ValueError('arquivo/ID selecionados divergem da captura')
 index=it['indice'];iu=urlsplit(index['url'])
 if index.get('http')!=200 or iu.scheme!='https' or iu.hostname!='www.al.to.leg.br' or iu.path!='/legislacaoEstadual' or urlsplit(index['url_final']).hostname!='www.al.to.leg.br':raise ValueError('índice oficial não comprovado')
 z=Path(index['cache']).read_bytes();b=gzip.decompress(z)
 if SHA(z)!=index['sha256_cache'] or SHA(b)!=index['sha256_fonte']:raise ValueError('índice congelado diverge')
 _,items,_=parse_index(b);observed=[x for x in items if x['fonte']==row['url']]
 if len(observed)!=1:raise ValueError('arquivo não observado de forma única no índice')
 obs=observed[0]
 for k in ['numero','tipo','pasta','ano_titulo','data_cartao']:
  if it[k]!=obs[k]:raise ValueError('identidade selecionada diverge do cartão')
 body,text=extrair_camada_textual(raw)
 if '\ufffd' in text or re.search('[\ue000-\uf8ff]',text):raise ValueError('camada textual tem glifo não resolvido')
 notas_editoriais=conferir_anotacoes(text)
 headings=list(HEAD.finditer(text))
 if not headings or headings[0].start()>1600:raise ValueError('epígrafe própria não comprovada')
 referencias=conferir_referencias(text,headings)
 h=headings[0];primeira_epigrafe(text,h.start());kind='Lei Complementar' if 'COMPLEMENTAR' in h[1].upper() else 'Lei Ordinária';date=day(h[3],h[4],h[5]);num=number(h[2])
 if (kind,num,date[:4],date)!=(it['tipo'],number(it['numero']),it['ano_titulo'],it['data_cartao']):raise ValueError('tipo/número/data próprios divergem do cartão')
 notes=anotacoes(text)
 if notes and not notas_editoriais:raise ValueError('anotação sem contexto editorial delimitado')
 pre=re.search(r'Faço\s+saber.{0,650}?seguinte\s+Lei(?:\s+Complementar)?\s*:',text,re.I|re.S)
 if not pre or not artigo_inicial(text[pre.end():]):raise ValueError('promulgação/dispositivo próprio inicial não comprovado')
 closings=list(FECHO.finditer(text))
 if not closings or {day(x[1],x[2],x[3]) for x in closings}!={date}:raise ValueError('fecho ausente/divergente ou ambíguo')
 if not cargo_assinatura(text,closings[-1]):raise ValueError('cargo da assinatura não comprovado')
 extra=re.findall(r'(?m)(?:^|[ \t]{3,})(?:DECRETO|PORTARIA|RESOLUÇÃO|EDITAL|AVISO|ATO|MEDIDA\s+PROVISÓRIA)\b[^\n]{0,180}',text)
 if extra:raise ValueError('possível epígrafe/ato alheio em linha/coluna: revisão necessária')
 scope=granularidade(text,kind,num,date,closings)
 objects=[text[max(0,m.start()-90):m.end()+240] for m in re.finditer(r'\banexos?\b|\btabelas?\b|\bquadros?\b|\b(?:mapa|planta|memorial|manual)\b|\b(?:aprova|ratifica|homologa)\b.{0,100}?\b(?:documento|plano|regulamento|regimento|estatuto|protocolo|conv[eê]nio|termo)\b',text,re.I)]
 objects+=documentos(text)
 visual=conferir_pdf_simples(raw);visibilidade=conferir_visibilidade(raw);geometria=conferir_clipping(raw) if any(set(p['operadores']) & {op.decode() for op in PATH} for p in visual) else dict(total_recortes=0,criterio='Nenhum operador de caminho/recorte presente; gates anteriores conservados.');pages=text.split('\f');pages=pages[:-1] if pages and not pages[-1].strip() else pages;render=MarkdownIt('commonmark',{'html':True}).parse(body)
 if [t.content for t in render if t.type=='fence']!=[p if p.endswith('\n') else p+'\n' for p in pages]:raise ValueError('CommonMark não preserva camada textual integral')
 if body_atual is not None and body_atual!=body:raise ValueError('corpo privado diverge da camada PDF completa')
 publication=re.search(r'(?m)^\s*[*]?(?:Publicado|Publicada|Republicado|Republicada) no Diário Oficial[^\n]*',text);ementa=None
 banner=re.search(r'(?m)^\s*O\s+Governador\s+do\s+Estado[^\n]*',text)
 if banner and banner.start()>h.end():
  block=text[h.end():banner.start()].lstrip(' .\r\n')
  block=re.sub(r'^[*]?(?:Publicado|Publicada|Republicado|Republicada) no Diário Oficial[^\n]*\n','',block).strip()
  if len(block)<1800 and not re.search(r'-\s*\n',block) and re.match(r'^(?:Declara|Institui|Altera|Autoriza|Dispõe|Cria|Fixa|Concede|Denomina|Reconhece|Estabelece|Regulamenta|Ratifica|Dispensa|Revoga|Acrescenta|Modifica|Prorroga|Inclui|Obriga|Proíbe|Garante)\b',block,re.I):ementa=' '.join(block.split())
 return body,dict(referencias_inline=referencias,anotacoes_editoriais=notas_editoriais,publicacao_literal=' '.join(publication[0].split()) if publication else None,ementa_PDF=ementa,numero=num,tipo=kind,data=date,epigrafe=' '.join(h[0].split()),fechos=[' '.join(x[0].split()) for x in closings],sha256_corpo=SHA(body.encode()),sha256_camada=SHA(text.encode()),sha256_fonte=SHA(raw),total_paginas=len(pages),granularidade=scope,visuais=visual,visibilidade_complementar=visibilidade,geometria_recortes=geometria,CommonMark_cercas_iguais=True,contextos_objetos=objects,revogada=None,limite='Somente camada textual fornecida no PDF sem raster/vetor/anotações PDF, com anotações textuais editoriais delimitadas e preservadas quando presentes. Não foi aplicado OCR nem certificada vigência global ou equivalência ao DOE. Referências a objetos exigem revisão complementar.')
