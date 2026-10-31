"""QA offline do campo oficial Legisla.AM; não cria Markdown nem acessa rede.

A identidade decorre da epígrafe própria e do título literal do índice, nunca do
ano da URL. Divergências ficam explícitas para deduplicação adicional. CSS externo
não capturado impede publicação, mesmo quando o fragmento parece simples.
"""
import gzip,hashlib,re,urllib.parse
from markdown_it import MarkdownIt
from representacao_html_legisla_am import extrair_campo,representar,MODO
from pe_fidelidade_visivel import texto_visivel_html,assinatura_numerica
from auditar_pe_recuperacao_utf8 import matrizes
from anexos_fonte import remissoes_sem_representacao
from avisos_fonte import avisos_de_omissao
from auditar_pe_cache import APP
from legisla_am_identidade import identidade
from legisla_am_citacoes import conferir_citacoes
SHA=lambda b:hashlib.sha256(b).hexdigest()

def dispositivo_proprio(visible):
    m=re.search(r'(?:presente|seguinte)\s+L\s*E\s*I\s*[:.]?\s*(?:(?-i:CAP[IÍ]TULO|T[IÍ]TULO|SE[CÇ][AÃ]O|LIVRO|PARTE)\b(?-i:[A-ZÀ-Ý0-9\s,/()–-]){0,300})?(Art[.]\s*1\s*[.º°o]*\s)',visible,re.I)
    first=re.search(r'\bArt[.]\s*1\s*[.º°o]*\s',visible)
    if not m or not first or first.start()!=m.start(1):raise ValueError('artigo inicial próprio após promulgação/sanção não comprovado')
    before=visible[max(0,m.start()-400):m.start()]
    if not re.search(r'\b(?:sanciono|promulgo|promulga)\b',before,re.I):raise ValueError('sanção/promulgação própria não comprovada')
    return visible[max(0,m.start()-80):m.end()+100]

def auditar(r,packed,*,contexto_css=None):
    if r.get('http')!=200:raise ValueError('captura individual HTTP 200 não comprovada')
    source=gzip.decompress(packed)
    if SHA(packed)!=r['sha256_cache'] or SHA(source)!=r['sha256_fonte']:raise ValueError('fonte ou gzip diverge')
    source=source.decode('utf8',errors='strict');item=r['item'];url=urllib.parse.urlparse(item['url'])
    if url.scheme!='https' or url.netloc!='legisla.imprensaoficial.am.gov.br' or not re.fullmatch(r'/diario_am/12/\d{4}/\d{1,2}/'+re.escape(item['id_legisla']),url.path):raise ValueError('identidade URL/categoria oficial não confere')
    field,limits=extrair_campo(source);visible=texto_visivel_html(field);own=identidade(visible[:1000]);idx=identidade(item['titulo'])
    if (own['numero'],own['data'])!=(idx['numero'],idx['data']):raise ValueError('epígrafe própria diverge do título literal do índice')
    dispositivo=dispositivo_proprio(visible)
    out=representar(field,modo=MODO);render=MarkdownIt('commonmark',{'html':True}).render(out);new=texto_visivel_html(render)
    if new!=visible or assinatura_numerica(new)!=assinatura_numerica(visible):raise ValueError('CommonMark/sinais divergem do campo integral')
    if matrizes(field)!=matrizes(render):raise ValueError('tabelas integrais divergem')
    holds=[]
    if avisos_de_omissao(visible):holds.append('aviso de omissão exige contexto')
    if remissoes_sem_representacao(visible):holds.append('remissão a conteúdo exige contexto')
    if APP.search(visible) and not re.search(r'\b(?:ANEXO|REGULAMENTO|REGIMENTO|ESTATUTO|PLANO|MANUAL)\s+(?:ÚNICO|[IVX0-9]+)\b',visible):holds.append('objeto aprovado exige revisão contextual')
    css_proof=contexto_css.conferir(source) if contexto_css is not None else None
    if css_proof is None:holds.append('CSS externo/herdado ainda não capturado e revisto')
    elif css_proof['retencoes']:holds.append('CSS contextual possui regras pendentes')
    citacoes=conferir_citacoes(field,own)
    if not citacoes['todas_contextualizadas']:holds.append('outra epígrafe completa exige revisão de granularidade/citação')
    return dict(**own,dispositivo_proprio=dispositivo,limites_campo=limits,sha256_fonte=SHA(gzip.decompress(packed)),sha256_campo=SHA(field.encode()),sha256_representacao=SHA(out.encode()),CommonMark_visivel_integral=True,sinais_numericos_iguais=True,tabelas=len(matrizes(field)),numero_coletor=item.get('numero'),ano_URL=item.get('ano_URL',item['ano']),divergencia_numero_coletor=item.get('numero')!=own['numero'],divergencia_ano_URL=item.get('ano_URL',item['ano'])!=own['data'][:4],retencoes=holds,contexto_CSS=css_proof,citacoes=citacoes,publicavel=False if holds else True)
