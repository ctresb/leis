"""Reparo privado de um ato comprovado na edição FAMURS 4260; não grava canônico."""
import argparse,datetime,hashlib,html,json,re,subprocess,sys
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo
sys.path.insert(0,str(Path(__file__).resolve().parent))
from auditar_municipal import metadados
ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT/'municipais/_lotes/20261021-alvorada4238-reparo'
POP=Path('/opt/homebrew/bin')
RECTS=[(22,551,295,800),(305,33,576,565)]
NS={'h':'http://www.w3.org/1999/xhtml'}

def sha(raw):return hashlib.sha256(raw).hexdigest()
def compact(text):return ''.join(text.split())
def command(name,args):return subprocess.check_output([str(POP/name)]+[str(x) for x in args],stderr=subprocess.PIPE)
def crop(pdf,rect,page=29):
 x,y,right,bottom=rect
 return command('pdftotext',['-f',page,'-l',page,'-x',x,'-y',y,'-W',right-x,'-H',bottom-y,'-layout','-nopgbrk',pdf,'-']).decode().rstrip()+'\n'

def nodes_by_column(page):
 result=[]
 for rect in RECTS:
  selected=[]
  for node in page.findall('text'):
   a=node.attrib;cx=(float(a['left'])+float(a['width'])/2)/1.5;cy=(float(a['top'])+float(a['height'])/2)/1.5
   if rect[0]<cx<rect[2] and rect[1]<cy<rect[3]:selected.append(node)
  selected.sort(key=lambda e:float(e.attrib['top'])+float(e.attrib['height']));groups=[]
  for node in selected:
   baseline=float(node.attrib['top'])+float(node.attrib['height'])
   if groups and baseline-groups[-1][0]<=2.5:groups[-1][1].append(node)
   else:groups.append([baseline,[node]])
  for _,group in groups:result.extend(sorted(group,key=lambda e:float(e.attrib['left'])))
 return result

def runs(node,bold=False,italic=False):
 bold=bold or node.tag=='b';italic=italic or node.tag=='i'
 if node.tag not in {'text','b','i'}:raise ValueError('Tag tipográfica não prevista neste caso')
 if node.text:yield node.text,bold,italic
 for child in node:
  yield from runs(child,bold,italic)
  if child.tail:yield child.tail,bold,italic

def estilizar(native,page):
 fonts={e.attrib['id']:e.attrib for e in page.findall('fontspec')};ordered=nodes_by_column(page)
 if compact(''.join(''.join(e.itertext()) for e in ordered))!=compact(native):raise ValueError('XML tipográfico e extração espacial divergem')
 indexes=[i for i,c in enumerate(native) if not c.isspace()];cursor=0;rawcursor=0;parts=[];emphases=[]
 for node in ordered:
  font=fonts[node.attrib['font']]
  if font['color']!='#000000':raise ValueError('Cor no ato exige revisão contextual')
  family=font['family'].lower()
  for text,bold,italic in runs(node,'bold' in family,'italic' in family):
   size=len(compact(text))
   if not size:continue
   start,end=indexes[cursor],indexes[cursor+size-1]+1
   if compact(native[start:end])!=compact(text):raise ValueError('Fragmento tipográfico não corresponde aos glifos nativos')
   parts.append(html.escape(native[rawcursor:start],quote=False));value=html.escape(native[start:end],quote=False)
   if italic:value='<em>'+value+'</em>'
   if bold:value='<strong>'+value+'</strong>'
   parts.append(value)
   if bold or italic:emphases.append(dict(inicio=start,fim=end,negrito=bold,italico=italic,texto=native[start:end]))
   cursor+=size;rawcursor=end
 parts.append(html.escape(native[rawcursor:],quote=False))
 if cursor!=len(indexes):raise ValueError('Glifos sem representação')
 return '<pre>'+''.join(parts)+'</pre>',emphases

class Pre(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.depth=0;self.text=[];self.count=0
 def handle_starttag(self,tag,attrs):
  if tag=='pre':self.depth+=1;self.count+=1
 def handle_endtag(self,tag):
  if tag=='pre':self.depth-=1
 def handle_data(self,text):
  if self.depth:self.text.append(text)

def conferir_replay(body,native):
 sys.path.insert(0,'/tmp/constituicao-markdown-qa-20261020');from markdown_it import MarkdownIt
 parser=Pre();parser.feed(MarkdownIt('commonmark',{'html':True}).render(body))
 if parser.count!=1 or ''.join(parser.text)!=native:raise ValueError('Replay CommonMark do bloco nativo diverge')
 return True

def preparar():
 case=json.loads((BASE/'caso.json').read_text());pdf=BASE/'fonte-edicao-4260.pdf';pre=(BASE/'preimagem-head.md').read_bytes()
 if sha(pdf.read_bytes())!=case['sha256_pdf'] or sha(pre)!=case['sha256_preimagem']:raise ValueError('PDF ou preimagem diverge')
 columns=[crop(pdf,r) for r in RECTS];native=columns[0].rstrip()+'\n\n'+columns[1]
 bbox=ET.fromstring(command('pdftotext',['-f',29,'-l',29,'-bbox',pdf,'-']));words=bbox.findall('.//h:word',NS);selected=[]
 for r in RECTS:
  selected.extend(w for w in words if r[0]<(float(w.attrib['xMin'])+float(w.attrib['xMax']))/2<r[2] and r[1]<(float(w.attrib['yMin'])+float(w.attrib['yMax']))/2<r[3])
 if compact(''.join(w.text or '' for w in selected))!=compact(native):raise ValueError('Bbox e recortes espaciais divergem')
 if not columns[0].lstrip().startswith('SECRETARIA MUNICIPAL DE GOVERNO E GABINETE\nLEI MUNICIPAL Nº 4.238, DE DOIS DE FEVEREIRO DE 2026.'):raise ValueError('Início de ato diverge')
 if not columns[1].lstrip().startswith('Art. 4º. Esta lei entra em vigor na data da sua publicação.') or not columns[1].rstrip().endswith('Código Identificador:6D5C2FBB'):raise ValueError('Continuação/limite final diverge')
 if any(s in native for s in ['306D4F67','4.239','TERMO DE PERMISSÃO']):raise ValueError('Ato vizinho dentro da seleção')
 header=crop(pdf,(305,260,576,291),23)
 if 'PREFEITURA MUNICIPAL DE ALVORADA' not in header:raise ValueError('Cabeçalho municipal diverge')
 xml=ET.fromstring(command('pdftohtml',['-f',29,'-l',29,'-xml','-hidden','-stdout',pdf]));page=xml.find('page');body,emphases=estilizar(native,page)
 conferir_replay(body,native)
 ibge=json.loads((ROOT/'municipais/_indice/ibge-municipios.json').read_text());cities=[r for r in ibge if r['nome']=='Alvorada' and r['regiao-imediata']['regiao-intermediaria']['UF']['sigla']=='RS']
 if len(cities)!=1:raise ValueError('IBGE municipal ambíguo')
 text=pre.decode();front=text.split('\n---\n',1)[0]
 front=re.sub(r'(?m)^data:[ \t]*$', 'data: "2026-02-02"',front)
 front=front.replace('revogada: false','revogada: null')
 additions=dict(codigo_ibge=str(cities[0]['id']),sha256_texto=sha(body.encode()),sha256_pdf=case['sha256_pdf'],edicao_fonte='4260',pagina_fonte='29',observacao_vigencia='Publicação original; situação de revogação posterior não verificada nesta edição.')
 for key,value in additions.items():front+='\n'+key+': '+json.dumps(value,ensure_ascii=False)
 candidate=front+'\n---\n# '+metadados(text)['titulo']+'\n\n'+body+'\n'
 proof=dict(sha256_pdf=case['sha256_pdf'],sha256_preimagem=case['sha256_preimagem'],sha256_candidato=sha(candidate.encode()),sha256_nativo=sha(native.encode()),sha256_caracteres=sha(compact(native).encode()),caracteres_nao_brancos=len(compact(native)),palavras_bbox=len(selected),replay_commonmark=True,replay_bbox=True,replay_tipografia_xml=True,negritos_italicos_preservados=emphases,fonte_cabecalho=header,codigo_ibge=str(cities[0]['id']),data_epigrafe='DOIS DE FEVEREIRO DE 2026',fecho_data='dois dias do mês de fevereiro do ano de dois mil e vinte e seis',alteracoes_metadados=dict(data='2026-02-02, literal por extenso na epígrafe e no fecho',revogada='null: publicação original não comprova inexistência de revogação posterior',baixado_em='2026-10-15 preservado da preimagem; nenhuma recaptura alegada'),limite='Reparo privado de um ato; não certifica vigência atual nem corrige genericamente o extrator. Limites e tipografia conferidos visualmente nas páginas 23 e 29.')
 return candidate,native,proof

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--saida',type=Path,required=True);a=ap.parse_args();candidate,native,proof=preparar();a.saida.mkdir(exist_ok=False);(a.saida/'candidato.md').write_text(candidate);(a.saida/'nativo-integral.txt').write_text(native);(a.saida/'prova.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:proof[k] for k in ['sha256_candidato','caracteres_nao_brancos','palavras_bbox','replay_commonmark']}))
if __name__=='__main__':main()
