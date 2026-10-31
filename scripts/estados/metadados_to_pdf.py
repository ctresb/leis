"""Esquema README para novos PDFs TO; não infere situação jurídica."""
import datetime,json,hashlib
ORDEM=('titulo','uf','tipo','numero','data','ano','ementa','situacao','revogada','versao_texto','publicacao','data_publicacao','urn','fonte','arquivo','baixado_em')
VERSAO='PDF digital ALETO, camada textual capturada; edição não certificada'
MODO='camada-textual-preformatada-pdf-aleto-v1'
SHA=lambda b:hashlib.sha256(b).hexdigest()
def data_captura(row):
 stamp=row.get('capturado_em')
 if not isinstance(stamp,str):raise ValueError('captura real ausente')
 t=datetime.datetime.fromisoformat(stamp.replace('Z','+00:00'))
 if t.tzinfo is None or t.utcoffset() is None:raise ValueError('captura sem fuso')
 return t.astimezone(datetime.timezone(datetime.timedelta(hours=-3))).date().isoformat()
def verificar(meta,row):
 if any(k not in meta for k in ['titulo','tipo','numero','data','versao_texto','fonte','baixado_em']):raise ValueError('campo obrigatório README ausente')
 if meta.get('uf')!='TO' or meta['versao_texto']!=VERSAO or meta['baixado_em']!=data_captura(row) or meta.get('representacao_corpo')!=MODO:raise ValueError('esquema/edição/captura divergente')
 expected=[k for k in ORDEM if k in meta]
 if list(meta)[:len(expected)]!=expected:raise ValueError('ordem canônica README divergente')
 return True

def criar(row,q,body):
 if SHA(body.encode())!=q['sha256_corpo']:raise ValueError('corpo não auditado')
 meta=dict(titulo=q['epigrafe'],uf='TO',tipo=q['tipo'],numero=q['numero'],data=q['data'],situacao=None,revogada=None,versao_texto=VERSAO,fonte=row['url'],arquivo=row['url_final'],baixado_em=data_captura(row))
 if q.get('ementa_PDF'):meta['ementa']=q['ementa_PDF']
 if q.get('publicacao_literal'):meta['publicacao']=q['publicacao_literal']
 meta={k:meta[k] for k in ORDEM if k in meta};meta.update(id_fonte='ALETO:'+row['item']['id_ALETO'],representacao_corpo=MODO,sha256_texto=q['sha256_corpo'],sha256_fonte=row['sha256_fonte'],edicao='PDF distribuído pelo portal oficial da Assembleia Legislativa do Tocantins, na edição capturada. Camada textual inteira preservada com linhas, números e paginação; nenhum OCR aplicado nesta coleta. Edição de publicação no DOE e vigência global não certificadas. Candidatos com gráficos, anotações, compilações ou contexto de anexos pendente ficam separados.')
 verificar(meta,row);return ('---\n'+''.join(k+': '+json.dumps(v,ensure_ascii=False)+'\n' for k,v in meta.items())+'---\n# '+meta['titulo']+'\n\n'+body).encode()
