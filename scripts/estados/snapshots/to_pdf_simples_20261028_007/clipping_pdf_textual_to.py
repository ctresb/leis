"""Prova conservadora de recortes retangulares em PDFs TO exclusivamente textuais.

Todos os glifos, incluindo espaços, recebem a caixa de TODOS os contornos da fonte,
união do FontBBox declarado e caixas do programa incorporado. Essa caixa amplia o
risco de retenção; não depende da caixa aproximada do texto extraído. Todos os glifos
precisam caber em todos os recortes e na página com margem de segurança de1pt.
"""
import io,json,hashlib,math
from functools import lru_cache
from pypdf import PdfReader
from pypdf.generic import ContentStream
from pdfminer.pdfdevice import PDFTextDevice
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdftypes import resolve1,stream_value
from pdfminer.psparser import literal_name
from pdfminer.utils import apply_matrix_pt
import fontTools
if fontTools.__version__!='4.60.1':raise RuntimeError('fontTools deve ser4.60.1 conforme perfil congelado')
from fontTools.cffLib import CFFFontSet
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import ControlBoundsPen
SHA=lambda b:hashlib.sha256(b).hexdigest()
PAINT={b'S',b's',b'f',b'F',b'f*',b'B',b'B*',b'b',b'b*',b'Do',b'sh',b'BI'}
PATH={b'm',b'l',b'h',b're',b'W',b'W*',b'n'}
BASIC={b'q',b'Q',b'cm',b'BT',b'ET',b'Tf',b'Tr',b'Tm',b'Td',b'TD',b'T*',b'Tj',b'TJ',b'Tw',b'Tc',b'Ts',b'Tz',b'TL',b'\"',b"'",b'g',b'G',b'rg',b'RG',b'k',b'K',b'gs',b'BDC',b'BMC',b'EMC',b'MP',b'DP',b'BX',b'EX',b'i'}
SAFETY=1.0

def finite(values):
 values=tuple(float(x) for x in values)
 if not all(math.isfinite(x) for x in values):raise ValueError('geometria não finita')
 return values

def union(boxes):
 boxes=[finite(x) for x in boxes if x is not None]
 if not boxes:raise ValueError('contornos de fonte ausentes')
 return min(b[0] for b in boxes),min(b[1] for b in boxes),max(b[2] for b in boxes),max(b[3] for b in boxes)

def inside(box,clip):return box[0]>=clip[0]+SAFETY and box[1]>=clip[1]+SAFETY and box[2]<=clip[2]-SAFETY and box[3]<=clip[3]-SAFETY

def intersect(a,b):return max(a[0],b[0]),max(a[1],b[1]),min(a[2],b[2]),min(a[3],b[3])

def concat(m,n):
 a,b,c,d,e,f=m;A,B,C,D,E,F=n
 return finite((a*A+c*B,b*A+d*B,a*C+c*D,b*C+d*D,a*E+c*F+e,b*E+d*F+f))

def point(m,x,y):return m[0]*x+m[2]*y+m[4],m[1]*x+m[3]*y+m[5]

def rectangle(points):
 if len(points)!=4:raise ValueError('recorte não é retângulo simples de quatro vértices')
 xs={p[0] for p in points};ys={p[1] for p in points}
 if len(xs)!=2 or len(ys)!=2 or set(points)!={(x,y) for x in xs for y in ys}:raise ValueError('recorte com rotação/shear/polígono fora do perfil')
 for a,b in zip(points,points[1:]+points[:1]):
  if (a[0]==b[0])==(a[1]==b[1]):raise ValueError('recorte cruzado/degenerado fora do perfil')
 return min(xs),min(ys),max(xs),max(ys)

def rects(page):
 box=finite(page.mediabox)
 if box[0]!=0 or box[1]!=0 or page.rotation or float(page.get('/UserUnit',1))!=1:raise ValueError('origem/rotação/UserUnit fora do perfil geométrico')
 if finite(page.cropbox)!=box:raise ValueError('CropBox distinto exige contexto')
 m=(1.,0.,0.,1.,0.,0.);clip=box;stack=[];path=[];closed=False;pending=None;records=[]
 for index,(args,op) in enumerate(ContentStream(page.get_contents(),page.pdf).operations):
  if op in PAINT:raise ValueError('pintura/objeto gráfico fora do perfil textual de recorte')
  if op not in BASIC|PATH:raise ValueError('operador fora do perfil geométrico comprovado')
  if op==b'q':stack.append((m,clip))
  elif op==b'Q':
   if not stack:raise ValueError('restore sem save')
   m,clip=stack.pop()
  elif op==b'cm':
   if len(args)!=6:raise ValueError('CTM incompleta')
   m=concat(m,finite(args))
  elif op==b'm':
   if path or len(args)!=2:raise ValueError('múltiplos subcaminhos/holes exigem contexto')
   path=[point(m,*finite(args))];closed=False
  elif op==b'l':
   if not path or closed or len(args)!=2:raise ValueError('caminho de recorte inconsistente')
   path.append(point(m,*finite(args)))
  elif op==b'h':
   if not path or closed:raise ValueError('fechamento de caminho inconsistente')
   closed=True
  elif op==b're':
   if path or len(args)!=4:raise ValueError('múltiplos retângulos exigem contexto')
   x,y,w,h=finite(args);path=[point(m,x,y),point(m,x+w,y),point(m,x+w,y+h),point(m,x,y+h)];closed=True
  elif op in [b'W',b'W*']:
   if pending is not None:raise ValueError('mais de um operador de recorte pendente')
   pending=rectangle(path)
  elif op==b'n':
   if path and pending is None:raise ValueError('caminho sem recorte fora do perfil')
   if pending is not None:
    clip=intersect(clip,pending)
    if clip[0]>=clip[2] or clip[1]>=clip[3]:raise ValueError('interseção de recortes vazia')
    records.append(dict(operador=index,retangulo=pending,intersecao_ativa=clip))
   path=[];closed=False;pending=None
  elif op in [b'c',b'v',b'y']:raise ValueError('curva em caminho de recorte exige contexto')
 if stack or path or pending is not None:raise ValueError('estado/caminho gráfico não encerrado')
 return box,records

@lru_cache(maxsize=256)
def program_bounds(raw,kind):
 if len(raw)>20_000_000:raise ValueError('programa de fonte excede perfil')
 boxes=[]
 if kind=='Type1C':
  cff=CFFFontSet();cff.decompile(io.BytesIO(raw),None)
  if len(cff.fontNames)!=1:raise ValueError('coleção CFF exige contexto')
  top=cff[cff.fontNames[0]]
  if hasattr(top,'ROS') or list(top.FontMatrix)!=[.001,0,0,.001,0,0]:raise ValueError('CFF CID/FontMatrix fora do perfil')
  glyphs=top.CharStrings
  if len(glyphs.keys())>65536:raise ValueError('quantidade de glifos fora do perfil')
  for name in glyphs.keys():
   pen=ControlBoundsPen(glyphs);pen.skipMissingComponents=False;glyphs[name].draw(pen)
   if pen.bounds:boxes.append(pen.bounds)
  if not boxes:raise ValueError('programa sem contornos demonstrados')
  boxes.append(top.FontBBox);units=1000
 elif kind=='TrueType':
  font=TTFont(io.BytesIO(raw),lazy=False)
  if 'fvar' in font:raise ValueError('fonte variável exige contexto')
  units=font['head'].unitsPerEm
  if not 16<=units<=16384:raise ValueError('unidades da fonte indeterminadas')
  glyphs=font.getGlyphSet()
  if len(glyphs.keys())>65536:raise ValueError('quantidade de glifos fora do perfil')
  for name in glyphs.keys():
   pen=ControlBoundsPen(glyphs);pen.skipMissingComponents=False;glyphs[name].draw(pen)
   if pen.bounds:boxes.append(pen.bounds)
  if not boxes:raise ValueError('programa sem contornos demonstrados')
  h=font['head'];boxes.append((h.xMin,h.yMin,h.xMax,h.yMax));font.close()
 else:raise ValueError('programa de fonte não suportado')
 box=tuple(v*1000/units for v in union(boxes))
 return box

def font_bounds(font):
 if font.is_vertical() or font.hscale!=.001 or font.vscale!=.001:raise ValueError('fonte vertical/matriz de fonte fora do perfil')
 d=font.descriptor
 if d.get('FontFile2'):
  stream=stream_value(d['FontFile2']);kind='TrueType'
 elif d.get('FontFile3'):
  stream=stream_value(d['FontFile3']);kind=literal_name(resolve1(stream.get('Subtype')))
 else:raise ValueError('fonte sem programa incorporado: não demonstrar bbox só pelo extrator')
 raw=stream.get_data();program=program_bounds(raw,kind);bbox=union([program,font.bbox]);return bbox,dict(nome=str(font.fontname),sha256_programa=SHA(raw),tipo_programa=kind,caixa_programa_conservadora=program,FontBBox_declarado=finite(font.bbox),caixa_uniao=bbox)

class Device(PDFTextDevice):
 def __init__(self,manager):super().__init__(manager);self.pages=[];self.fonts={}
 def begin_page(self,page,ctm):self.glyphs=[];self.fontuses={}
 def render_char(self,matrix,font,fontsize,scaling,rise,cid,ncs,graphicstate):
  key=font
  if key not in self.fonts:self.fonts[key]=font_bounds(font)
  bbox,proof=self.fonts[key];self.fontuses[proof['sha256_programa']]=proof
  size,scale,offset=finite((fontsize,scaling,rise));matrix=finite(matrix)
  corners=[apply_matrix_pt(matrix,(x*.001*size*scale,y*.001*size+offset)) for x in [bbox[0],bbox[2]] for y in [bbox[1],bbox[3]]];globalbox=(min(p[0] for p in corners),min(p[1] for p in corners),max(p[0] for p in corners),max(p[1] for p in corners));finite(globalbox)
  self.glyphs.append(dict(cid=cid,matriz=matrix,fontsize=size,escala_horizontal=scale,rise=offset,fonte=proof['sha256_programa'],caixa=globalbox))
  return font.char_width(cid)*fontsize*scaling
 def end_page(self,page):
  self.pages.append(dict(glifos=len(self.glyphs),caixa_glifos=union([r['caixa'] for r in self.glyphs]) if self.glyphs else None,sha256_prova_glifos=SHA(json.dumps(self.glyphs,sort_keys=True,separators=(',',':')).encode()),fontes=sorted(self.fontuses.values(),key=lambda x:x['sha256_programa'])))

def conferir(raw):
 reader=PdfReader(io.BytesIO(raw));clips=[rects(page) for page in reader.pages];manager=PDFResourceManager();device=Device(manager);interpreter=PDFPageInterpreter(manager,device)
 for page in PDFPage.get_pages(io.BytesIO(raw),check_extractable=True):interpreter.process_page(page)
 if len(device.pages)!=len(clips):raise ValueError('contagem de páginas geométricas diverge')
 results=[]
 for i,((media,paths),proof) in enumerate(zip(clips,device.pages),1):
  bbox=proof['caixa_glifos'];limits=[media]+[r['intersecao_ativa'] for r in paths]
  if bbox and any(not inside(bbox,clip) for clip in limits):raise ValueError('caixa conservadora de glifo toca/sai de recorte ou página')
  results.append(dict(pagina=i,MediaBox=media,recortes=paths,margem_seguranca_pt=SAFETY,**proof))
 return json.loads(json.dumps(dict(total_paginas=len(results),total_recortes=sum(len(p['recortes']) for p in results),criterio='Todos os glifos dentro da página e de cada interseção de recortes, usando união conservadora de TODOS os contornos do programa incorporado e FontBBox declarado. CTM/fontsize/escala/rise completos; q/Q preservado. Sem pintura de caminhos.',paginas=results)))
