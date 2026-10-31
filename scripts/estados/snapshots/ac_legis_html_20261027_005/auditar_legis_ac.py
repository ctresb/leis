"""QA offline do campo normativo LEGIS/AC, sem gerar ou promover canônicos."""
import gzip,hashlib,json,re,datetime
from pathlib import Path
from urllib.parse import urlsplit
from lxml import html
from css_contexto_campo import ContextoCSS
from representacao_html_ac_legis import extrair_campo,representar,MODO
from identidade_legis_ac import conferir as conferir_identidade,num,epigrafes_contextuais
from auditar_spl_html_recente import comparar
from html2md import convert
from pe_fidelidade_visivel import texto_visivel_html
from integridade_texto import verificar_integridade_texto
from avisos_fonte import avisos_de_omissao
SHA=lambda b:hashlib.sha256(b).hexdigest()
JS_SHA='089e49439474d44e6f488e7e86a8610dd0ea2cb264d987d537ebf50b0a5810f7'
JS_URL='https://legis.ac.gov.br/detalhar.js'
CARD=re.compile(r'^Lei(?: Complementar)? nº\s*([\d.]+(?:-[A-Z]+)?), de (\d{2})/(\d{2})/(\d{4})$',re.I)

class AuditorAC:
 def __init__(self,css,js):
  self.css=ContextoCSS(css);self.css_urls={r['url'] for r in css};self.indices={};self.js=js
  z=Path(js['cache']).read_bytes();b=gzip.decompress(z)
  if js['retorno_curl']!=0 or js['status_final']!='200 '+JS_URL or SHA(z)!=js['sha256_cache'] or SHA(b)!=JS_SHA or SHA(b)!=js['sha256_fonte']:raise ValueError('JS não corresponde à versão examinada')
 def indice(self,item):
  r=item['indice'];key=r['sha256_fonte']
  if key not in self.indices:
   z=Path(r['cache']).read_bytes();b=gzip.decompress(z)
   if SHA(z)!=r['sha256_cache'] or SHA(b)!=key:raise ValueError('índice SHA divergente')
   if r['retorno_curl']!=0 or not r['status_final'].startswith('200 '):raise ValueError('índice não foi HTTP200')
   d=html.fromstring(b);lookup={}
   for id_,typ in [('tbody_ordinarias','Lei Ordinária'),('tbody_complementares','Lei Complementar')]:
    for tr in d.xpath('//*[@id="'+id_+'"]//tr'):
     a=tr.xpath('.//a[contains(@href,"/detalhar/")]');td=tr.xpath('./td')
     if len(a)!=1 or len(td)!=2:raise ValueError('estrutura do cartão não reconhecida')
     title=' '.join(a[0].text_content().split());m=CARD.fullmatch(title)
     if not m or ('Complementar' in title)!=(typ=='Lei Complementar'):raise ValueError('tipo/epígrafe de cartão divergente')
     u=a[0].get('href');ementa=' '.join(td[1].text_content().split())
     if not ementa.startswith('Ementa'):raise ValueError('rótulo da ementa ausente')
     if u in lookup:raise ValueError('URL repetida entre cartões de leis')
     lookup[u]=dict(tipo=typ,numero=num(m[1]),data=datetime.date(int(m[4]),int(m[3]),int(m[2])).isoformat(),ementa=ementa[len('Ementa'):].strip(),titulo=title)
   self.indices[key]=lookup
  observed=self.indices[key].get(item['fonte'])
  if not observed or (observed['tipo'],observed['numero'],observed['data'])!=(item['tipo'],num(item['numero']),item['data']):raise ValueError('seleção não confere com o cartão oficial congelado')
  return observed
 def auditar(self,row,body_atual=None):
  it=row['item'];observed=self.indice(it);u=urlsplit(row['url']);z=Path(row['cache']).read_bytes();b=gzip.decompress(z)
  if row['http']!=200 or row['url_final']!=row['url'] or row['url']!=it['fonte'] or u.hostname!='legis.ac.gov.br' or u.path!='/detalhar/'+it['id_LEGIS']:raise ValueError('fonte/URL oficial diverge')
  if SHA(z)!=row['sha256_cache'] or SHA(b)!=row['sha256_fonte']:raise ValueError('fonte integral SHA divergente')
  source=b.decode('utf-8-sig',errors='strict')
  if '\ufffd' in source or '\x00' in source:raise ValueError('caractere substituído/NUL na fonte exige contexto')
  d=html.document_fromstring(source)
  if JS_URL not in d.xpath('//script/@src'):raise ValueError('JS específico não foi observado na fonte')
  styles=d.xpath('//link[translate(@rel,"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz")="stylesheet"]/@href')
  if any(u not in self.css_urls for u in styles):raise ValueError('CSS externo da fonte ainda não capturado')
  inputs={}
  for id_ in ['leis_revogadas_guard','opcao_compilacao','resultado_busca']:
   nodes=d.xpath('//*[@id="'+id_+'"]')
   if len(nodes)!=1:raise ValueError('estado da interface JS não único')
   inputs[id_]=nodes[0].get('value','')
  if inputs['opcao_compilacao']!='1':raise ValueError('edição distinta do modo Padrão exige revisão própria')
  if inputs['resultado_busca']!='':raise ValueError('JS de realce/busca pode modificar o DOM; revisão necessária')
  if inputs['leis_revogadas_guard']!='0':raise ValueError('JS aplica ou pode aplicar tachado total; requer apresentação histórica explícita, sem inferir vigência')
  field,scope=extrair_campo(source);fielddom=html.fromstring(field)
  if re.search('[\ue000-\uf8ff]',field):raise ValueError('glifo Unicode privado requer contexto visual')
  # O JS conhecido pode substituir o parágrafo inteiro de certos títulos pelo
  # texto de seu primeiro span. Reter se houver conteúdo adicional potencial.
  for p in fielddom.xpath('.//p'):
   spans=p.xpath('.//span')
   if not spans:continue
   first=' '.join(spans[0].text_content().split());whole=' '.join(p.text_content().split())
   if re.fullmatch(r'(?:TÍTULO|CAPÍTULO|Seção|ANEXO) [IVXLCDM]+',first) and first!=whole:raise ValueError('JS pode substituir título com texto adicional; contexto de edição necessário')
  css=self.css.conferir(source,id_campo='body-law',id_final_campo='texto_publicado_doe')
  if css['retencoes']:raise ValueError('CSS aplicado ao campo exige revisão')
  fullcss=self.css.conferir(source,id_campo='body-law');expected=sum(e['tag']=='div' for e in scope['posterior_nao_normativo_comprovado'])
  allowed=lambda r:r.get('motivo')=='style inline potencialmente oculto/tachado' and r.get('tag')=='div' and r.get('propriedade')=='display' and r.get('valor')=='none'
  if len(fullcss['retencoes'])!=expected or any(not allowed(r) for r in fullcss['retencoes']):raise ValueError('CSS fora do limite normativo não se restringe à interface vazia comprovada')
  native=representar(field,modo=MODO);identity=conferir_identidade(field,it);faith=comparar(field,native);gate=convert(field);issue,proof=verificar_integridade_texto(gate)
  if issue:raise ValueError(issue)
  omissions=avisos_de_omissao(gate)
  if omissions:raise ValueError('aviso literal de conteúdo não representado')
  # Somente alertas para revisão contextual; não certificam a existência/ausência
  # de anexos por contagem nem convertem citações em outro ato.
  t=texto_visivel_html(field)
  if re.search(r'\((?:Redaç[aã]o\s+dada|Inclu[ií]d[oa]|Alterad[oa]|Acrescentad[oa]|Revogad[oa])\b[^)]*\b(?:pela|por)\b[^)]*\)',t,re.I):raise ValueError('indicação literal de incorporação legislativa posterior exige revisão/rotulagem própria de edição')
  rx=re.compile(r'\banexos?\b|\b(?:planta|memorial|mapa|manual)\b|\b(?:aprovad?[oa]?s?|ratificad?[oa]?s?|homologad?[oa]?s?)\b.{0,160}?\b(?:documento|contrato|plano|regulamento|regimento|estatuto|conv[eê]nio|acordo|termo|tabela|quadro|projeto)\b',re.I)
  contexts=[t[max(0,m.start()-100):m.end()+260] for m in rx.finditer(t)]
  q=dict(identidade=identity,ementa_indice=observed['ementa'],escopo=scope,CSS=css,CSS_UI_posterior=fullcss['retencoes'],JS=dict(url=JS_URL,sha256=JS_SHA,estados_literais=inputs,observacao='Snapshot do campo HTML fornecido, sem executar alterações de interface. Campo integralmente tachado, busca ativa ou possível perda textual por JS são retidos; valor0 não é inferência de vigência.'),fidelidade=faith,dispositivo_proprio=proof,modo=MODO,sha256_corpo=SHA(native.encode()),sha256_fragmento_extraido=SHA(field.encode()),contextos_objetos=contexts,epigrafes_contextuais=epigrafes_contextuais(field),revogada=None,limite='Transcrição do campo normativo do HTML LEGIS em modo Padrão, representação nativa literal com LF e entidades equivalentes de whitespace. Fonte integral/CSS/JS preservados. Não certifica equivalência DOE nem situação jurídica global; nenhuma correção de OCR ou nome presumida.')
  if body_atual is not None and body_atual!=native:raise ValueError('corpo privado diverge do snapshot de representação')
  return native,q
