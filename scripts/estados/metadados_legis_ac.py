"""Esquema LEGIS/AC: ordem README e captura real, sem modificar corpo."""
import datetime,hashlib,json
VERSAO='transcrição digital LEGIS/AC, modo Padrão; edição não certificada'
ORDEM=('titulo','uf','tipo','numero','data','ano','ementa','situacao','revogada','versao_texto','publicacao','data_publicacao','urn','fonte','arquivo','baixado_em')
OBRIGATORIOS=('titulo','tipo','numero','data','versao_texto','fonte','baixado_em')
SHA=lambda b:hashlib.sha256(b).hexdigest()
def captura_real(row):
 stamp=row.get('capturado_em')
 if not isinstance(stamp,str):raise ValueError('capturado_em real ausente')
 try:t=datetime.datetime.fromisoformat(stamp.replace("Z","+00:00"))
 except ValueError as e:raise ValueError('capturado_em não é ISO8601 válido') from e
 if t.tzinfo is None or t.utcoffset() is None:raise ValueError('captura sem fuso explícito')
 return stamp

def data_captura(row):
 stamp=captura_real(row);t=datetime.datetime.fromisoformat(stamp.replace('Z','+00:00'))
 return t.astimezone(datetime.timezone(datetime.timedelta(hours=-3))).date().isoformat()

def ordenar(meta):return {k:meta[k] for k in ORDEM if k in meta}|{k:v for k,v in meta.items() if k not in ORDEM}

def verificar(meta,row):
 if any(k not in meta for k in OBRIGATORIOS):raise ValueError('campo obrigatório README ausente')
 if meta['versao_texto']!=VERSAO:raise ValueError('versao_texto não descreve precisamente a edição')
 if meta['baixado_em']!=data_captura(row):raise ValueError('baixado_em não é a data real da captura em UTC-03:00')
 expected=[k for k in ORDEM if k in meta]
 if list(meta)[:len(expected)]!=expected:raise ValueError('ordem do cabeçalho diverge do README')
 if any(k in ORDEM for k in list(meta)[len(expected):]):raise ValueError('campo canônico depois das extensões')
 return True

def montar(meta,row):
 out=dict(meta)
 for k,v in [('versao_texto',VERSAO),('baixado_em',data_captura(row))]:
  if k in out and out[k]!=v:raise ValueError('não substituir metadado existente divergente: '+k)
  out[k]=v
 out=ordenar(out);verificar(out,row);return out

def ler(blob):
 if not blob.startswith(b'---\n') or b'\n---\n' not in blob[4:]:raise ValueError('cabeçalho LF estruturado ausente')
 header,body=blob[4:].split(b'\n---\n',1);meta={}
 for line in header.decode('utf-8',errors='strict').splitlines():
  k,v=line.split(': ',1)
  if k in meta:raise ValueError('metadado repetido')
  meta[k]=json.loads(v)
 return meta,body

def representar(meta,body):
 return ('---\n'+''.join(k+': '+json.dumps(v,ensure_ascii=False)+'\n' for k,v in meta.items())+'---\n').encode()+body

def acrescentar(blob,row):
 before,body=ler(blob);after=montar(before,row);new=representar(after,body);again,newbody=ler(new)
 removed=sorted(set(before)-set(after));changed=sorted(k for k in before if after.get(k)!=before[k]);added=sorted(set(after)-set(before))
 if removed or changed or any(k not in ['versao_texto','baixado_em'] for k in added) or body!=newbody:raise ValueError('transformação excede adição dos dois campos/ordem')
 proof=dict(sha256_preimagem=SHA(blob),sha256_novo=SHA(new),sha256_corpo_com_H1=SHA(body),corpo_com_H1_byte_identico=body==newbody,chaves_adicionadas=added,chaves_removidas=removed,chaves_alteradas=changed,ordem_anterior=list(before),ordem_nova=list(after),captura_literal=captura_real(row),baixado_em_data_UTC_menos3=data_captura(row))
 return new,proof
