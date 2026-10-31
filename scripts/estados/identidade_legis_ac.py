"""Identidade impressa no campo LEGIS/AC; nenhuma inferência de vigência."""
import datetime,re
from lxml import html
from pe_fidelidade_visivel import texto_visivel_html
MESES={m:i for i,m in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split(),1)}
HEAD=re.compile(r'^(LEI(?: COMPLEMENTAR)?)\s+N[.º°o]*\s*([\d.]+(?:\s*-\s*[A-Z]+)?),?\s+DE\s+(\d{1,2})[º°]?\s+DE\s+([A-ZÇ]+)\s+DE\s+(\d{4})[.]?$',re.I)
# Variações literais observadas no portal: dia com ordinal separado,
# "Rio Branco, de 7 ...", ausência do primeiro "de" e fecho legislativo.
# Reconhecer os tokens não acrescenta nem corrige texto/data da fonte.
FECHO=re.compile(r'^(?:Rio\s+Branco(?:\s*[-–—]\s*Acre)?\s*,|Sala\s+das\s+Sessões\s+[“"«]?Deputado\s+Francisco\s+Cartaxo[”"»]?\s*,)\s*(?:de\s+)?(\d{1,2})\s*[º°]?\s+(?:de\s+)?([A-ZÇ]+)\s+de\s+(\d{4})\b',re.I)

def num(v):
 s=re.sub(r'[.\s]','',str(v)).upper();m=re.fullmatch(r'(\d+)(-[A-Z]+)?',s)
 if not m:raise ValueError('número literal não reconhecido')
 return str(int(m[1]))+(m[2] or '')
def date(day,month,year):return datetime.date(int(year),MESES[month.lower()],int(day)).isoformat()
def visible(node):return texto_visivel_html(html.tostring(node,encoding='unicode'))
def conferir(fragmento,item):
 d=html.fromstring(fragmento);quotes=d.xpath('./blockquote')
 if not quotes:raise ValueError('bloco inicial de epígrafe ausente')
 title=visible(quotes[0]);m=HEAD.fullmatch(title)
 if not m:raise ValueError('epígrafe própria inicial não reconhecida')
 typ='Lei Complementar' if 'COMPLEMENTAR' in m[1].upper() else 'Lei Ordinária';day=date(m[3],m[4],m[5]);number=num(m[2])
 if (typ,number,day)!=(item['tipo'],num(item['numero']),item['data']):raise ValueError('epígrafe própria diverge do cartão')
 candidates=[]
 for e in d.xpath('.//p|.//div[not(.//p) and not(.//div)]'):
  text=visible(e);f=FECHO.match(text)
  if f:candidates.append(dict(trecho=text,data=date(f[1],f[2],f[3])))
 if not candidates or {f['data'] for f in candidates}!={day}:raise ValueError('fecho próprio ausente, divergente ou contextual ambíguo')
 footer=d.xpath('.//*[@id="texto_publicado_doe"]')
 if len(footer)!=1:raise ValueError('rodapé editorial não único')
 pub=' '.join(footer[0].text_content().split());dates=[]
 for f in re.finditer(r'\b(\d{2})/(\d{2})/(\d{4})\b',pub):dates.append(datetime.date(int(f[3]),int(f[2]),int(f[1])).isoformat())
 if dates and any(v<day for v in dates):raise ValueError('dúvida cronológica no rodapé DOE')
 return dict(epigrafe=title,tipo=typ,numero=number,data=day,fechos=candidates,publicacao_literal=pub,datas_publicacao=dates,revogada=None,limite='Identidade própria da transcrição digital e consistência com cartão/fecho; não certifica DOE nem vigência.')

def epigrafes_contextuais(fragmento):
 """Blocos/células com cabeçalho impresso: alerta, nunca duplicação automática."""
 d=html.fromstring(fragmento);primary=d.xpath('./blockquote[1]//p');primary=primary[0] if primary else None;rows=[];seen=set()
 prefix=re.compile(HEAD.pattern[:-1]+r'(?=\s|$)',HEAD.flags)
 for node in d.xpath('.//p|.//h1|.//h2|.//h3|.//div[not(.//p) and not(.//div)]|.//td'):
  if node is primary or primary is not None and primary in list(node.iterdescendants()):continue
  text=visible(node);m=prefix.match(text)
  if not m:continue
  key=(m[1],m[2],m[3],m[4],m[5],text)
  if key in seen:continue
  seen.add(key);rows.append(dict(tag=node.tag,tipo_impresso=m[1],numero_impresso=m[2],data=date(m[3],m[4],m[5]),texto_bloco=text,nota='Contexto necessário: pode ser citação, anexo incorporado ou outro ato. Não prova duplicação e não autoriza corte.'))
 return rows
