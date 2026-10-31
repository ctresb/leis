"""Gates de identidade inicial, edição e granularidade para o perfil PDF TO."""
import re,datetime
MONTH={m:i for i,m in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split(),1)}
BROAD=re.compile(r'(?m)(?:^|[ \t]{3,})[“\"\']?(LEI(?:\s+(?:ORDIN[ÁA]RIA|COMPLEMENTAR))?)\s+(?:N[º°o.]*\s*)?([\d.]+(?:-[A-Z]+)?)\s*,?\s+DE\s+(\d{1,2})\s*[º°o]?\s+DE\s+([A-ZÇ]+)\s+DE\s+(\d{4})',re.I)
ACT=re.compile(r'(?m)(?:^|[ \t]{3,})(?:DECRETO|PORTARIA|RESOLUÇÃO|DELIBERAÇÃO|INSTRUÇÃO\s+NORMATIVA|ORDEM\s+DE\s+SERVIÇO|EDITAL|AVISO|ATO|MEDIDA\s+PROVISÓRIA)\s*(?:N[º°o.]*)?\s+[\d.]+',re.I)
PRE=re.compile(r'Faço\s+saber.{0,650}?seguinte\s+Lei(?:\s+Complementar)?\s*:',re.I|re.S)
EDITORIAL=re.compile(r'\bred[aã]ç[aã]o\s+(?:dada|determinada|alterada|atualizada|estabelecida)|\b(?:acrescentad[oa]s?|acrescid[oa]s?|inclu[íi]d[oa]s?|inserid[oa]s?|suprimid[oa]s?|substitu[íi]d[oa]s?|alterad[oa]s?|revogad[oa]s?)\s+(?:pel[ao]s?|por)\b|\bdeclarad[oa]\s+inconstitucional\b',re.I)
DOCUMENT=re.compile(r'\b(?:(?:ficam?|é|são|considera-se|consideram-se)\s+(?:aprovad[oa]s?|ratificad[oa]s?|homologad[oa]s?)|aprova|ratifica|homologa)\b.{0,300}?\b(?:documentos?|planos?|programas?|regulamentos?|regimentos?|estatutos?|protocolos?|conv[eê]nios?|termos?|c[oó]digos?|manuais|manual|pol[ií]ticas?)\b',re.I|re.S)
def primeira_epigrafe(text,offset):
 # Fonte TO desse perfil tem epígrafe no início; asterisco é marcador editorial
 # observado no PDF e fica intacto no corpo. Outros prefixos exigem contexto.
 if text[:offset].strip() not in ['', '*']:raise ValueError('epígrafe não abre o documento; possível citação/projeto ou prefixo desconhecido')
 return True

def granularidade(text,kind,num,date,closings):
 pre=list(PRE.finditer(text))
 if len(pre)!=1 or len(closings)!=1:raise ValueError('mais de uma promulgação/fecho ou estrutura ambígua exige contexto')
 headers=[]
 for x in BROAD.finditer(text):
  n=re.sub(r'^0+(?=\d)','',x[2].replace('.','').upper());t='Lei Complementar' if 'COMPLEMENTAR' in x[1].upper() else 'Lei Ordinária';d=datetime.date(int(x[5]),MONTH[x[4].lower()],int(x[3])).isoformat();headers.append(dict(tipo=t,numero=n,data=d))
  if (t,n,d)!=(kind,num,date):raise ValueError('epígrafe secundária de lei exige contexto; não fundir ou cortar')
 if not headers:raise ValueError('cabeçalho inicial fora do padrão comprovado')
 acts=list(ACT.finditer(text))
 if acts:raise ValueError('possível outro ato em linha/coluna exige contexto')
 return dict(cabecalhos=headers,promulgacoes=1,fechos=1,outros_atos=[])

def anotacoes(text):return [text[max(0,m.start()-100):m.end()+200] for m in EDITORIAL.finditer(text)]
def documentos(text):
 preludes=[(p.start(),p.end()) for p in PRE.finditer(text)]
 return [text[max(0,m.start()-90):m.end()+240] for m in DOCUMENT.finditer(text) if not any(a<=m.start()<b for a,b in preludes)]
