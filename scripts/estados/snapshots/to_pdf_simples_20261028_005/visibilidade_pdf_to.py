"""Gate complementar de camadas opcionais, recorte e texto alternativo em PDF TO."""
import io
from pypdf import PdfReader
from pypdf.generic import ContentStream,DictionaryObject

def conferir(raw):
 pdf=PdfReader(io.BytesIO(raw));cat=pdf.trailer['/Root'];pages=[]
 if cat.get('/OCProperties'):raise ValueError('camadas opcionais PDF exigem revisão visual/contextual')
 for i,page in enumerate(pdf.pages):
  if list(page.cropbox)!=list(page.mediabox):raise ValueError('CropBox difere da página; recorte exige contexto')
  res=page.get('/Resources',{});res=res.get_object() if hasattr(res,'get_object') else res
  if res.get('/Properties'):raise ValueError('Properties nomeadas em PDF exigem contexto')
  spaces=res.get('/ColorSpace',{});spaces=spaces.get_object() if hasattr(spaces,'get_object') else spaces
  if any(k in spaces for k in ['/DefaultGray','/DefaultRGB','/DefaultCMYK']):raise ValueError('cores padrão substituídas exigem contexto')
  marked=[]
  for args,op in ContentStream(page.get_contents(),pdf).operations:
   if op not in [b'BDC',b'BMC',b'DP',b'MP']:continue
   if not args or args[0]=='/OC':raise ValueError('marcação opcional/desconhecida exige contexto')
   if op in [b'BDC',b'DP']:
    if len(args)!=2 or not isinstance(args[1],DictionaryObject) or set(args[1])-{'/MCID'}:raise ValueError('texto alternativo/propriedades de marcação exigem contexto')
   elif len(args)!=1:raise ValueError('marcação PDF fora do padrão comprovado')
   marked.append(dict(operador=op.decode(),tag=str(args[0]),MCID=int(args[1]['/MCID']) if len(args)==2 and '/MCID' in args[1] else None))
  pages.append(dict(pagina=i+1,CropBox=list(page.cropbox),MediaBox=list(page.mediabox),marcacoes=marked))
 return dict(total_paginas=len(pages),sem_camadas_opcionais=True,sem_recorte=True,sem_texto_alternativo=True,paginas=pages)
