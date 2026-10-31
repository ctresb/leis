"""Validação e promoção privada LEGIS/AC HTML. Dry-run padrão; --apply reservado ao ROOT.

Sem Git de escrita. O manifesto congelado permanece intacto. Publicação por arquivo
usa link atômico sem substituição; a transação inteira é registrada em journal.
"""
import argparse, datetime, gzip, hashlib, json, os, re, shutil, subprocess, tempfile
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from metadados_legis_ac import verificar as verificar_metadados

SHA=lambda b:hashlib.sha256(b).hexdigest()

def agora():return datetime.datetime.now().astimezone().isoformat()
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def run_git(root,*args):return subprocess.check_output(['git','-C',str(root),*args])
def gravar_json(path,data):
 with path.open('x',encoding='utf-8',newline='\n') as f:
  json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def relpath(root,text):
 p=Path(text)
 if p.is_absolute() or '..' in p.parts:raise ValueError('caminho não relativo seguro: '+str(p))
 result=root/p
 if not result.resolve().is_relative_to(root):raise ValueError('caminho fora do repositório')
 return result

def metadata(blob):
 # Escopo: campos escalares dos cabeçalhos realmente gravados pelo projeto.
 text=blob.decode('utf-8',errors='strict')
 if not text.startswith('---\n'):raise ValueError('cabeçalho inicial ausente')
 header,body=text[4:].split('\n---\n',1);out={}
 for ln in header.splitlines():
  if ': ' not in ln:continue
  k,v=ln.split(': ',1)
  if not re.fullmatch('[a-z][a-z0-9_]*',k):continue
  if k in out:raise ValueError('campo repetido: '+k)
  try:out[k]=json.loads(v)
  except json.JSONDecodeError:
   # YAML escalar simples de coletas antigas; nunca executar expressão ou inferir ID.
   out[k]=v
 return out,body

def identidade(path,meta):
 parts=path.split('/')
 if len(parts)<5 or parts[:2]!=['estaduais','AC']:raise ValueError('caminho canônico fora de AC')
 number=str(meta.get('numero','')).replace('.','').replace(' ','').upper()
 date=str(meta.get('data',''))
 if not re.fullmatch(r'\d+(?:-[A-Z]+)?',number) or not re.match(r'^\d{4}-\d{2}-\d{2}$',date):
  raise ValueError('número/data indisponível no cabeçalho: '+path)
 number=re.sub(r'^0+(?=\d)','',number)
 return (parts[2],number,date[:4])

def id_oficial(meta):
 u=urlsplit(str(meta.get('fonte','')))
 if u.hostname=='legis.ac.gov.br':
  match=re.fullmatch(r'/detalhar/(\d+)',u.path)
  return ('LEGIS-AC',match[1]) if match else None
 if u.hostname=='sapl.al.ac.leg.br':
  match=re.fullmatch(r'/(?:norma|normajuridica)/(\d+)/?',u.path)
  return ('SAPL-AC',match[1]) if match else None
 return None

def arquivo(meta):
 raw=str(meta.get('arquivo') or '')
 if not raw:return None
 u=urlsplit(raw)
 # HTTP/HTTPS do mesmo recurso constituem alias; preservar path/query literal.
 return (u.hostname,u.path,u.query)

def indices(rows):
 byid={};bykey={};byurl={};paths=set()
 for r in rows:
  path=r['path'];m=r['meta'];paths.add(path)
  id=id_oficial(m);url=arquivo(m)
  if id:byid.setdefault(id,[]).append(path)
  if url:byurl.setdefault(url,[]).append(path)
  # Todos os blobs permanecem no inventário e nos índices ID/URL/path.
  # Constituição e outros tipos sem número não colidem por chave de lei.
  if path.split('/')[2] in ('leis-ordinarias','leis-complementares'):
   if not str(m.get('data') or ''):
    n=str(m.get('numero','')).replace('.','').replace(' ','').upper()
    if not re.fullmatch(r'\d+(?:-[A-Z]+)?',n):raise ValueError('número HEAD indeterminado: '+path)
    n=re.sub(r'^0+(?=\d)','',n);key=(path.split('/')[2],n,'*')
   else:key=identidade(path,m)
   bykey.setdefault(key,[]).append(path)
 return byid,bykey,byurl,paths

def conferir_dedup(rows,candidates):
 byid,bykey,byurl,paths=indices(rows);seen_id=set();seen_key=set();seen_url=set();seen_paths=set()
 for r in candidates:
  p=r['path'];m=r['meta'];id=id_oficial(m);key=identidade(p,m);url=arquivo(m)
  if not id or id[0]!='LEGIS-AC' or not url:raise ValueError('identidade/fonte do candidato incompleta')
  if p in paths or id in byid or key in bykey or (key[0],key[1],'*') in bykey or url in byurl:raise ValueError('colisão em HEAD: '+p)
  if p in seen_paths or id in seen_id or key in seen_key or url in seen_url:raise ValueError('colisão interna: '+p)
  seen_paths.add(p);seen_id.add(id);seen_key.add(key);seen_url.add(url)

def ler_HEAD(root,controle):
 head=run_git(root,'rev-parse','HEAD').decode().strip()
 tree=run_git(root,'ls-tree','-r','-z',head,'--','estaduais/AC/')
 (controle/'HEAD-ls-tree.z').write_bytes(tree)
 entries=[]
 for part in tree.split(b'\0'):
  if not part:continue
  prefix,path=part.split(b'\t',1);path=path.decode('utf-8',errors='strict')
  if path.endswith('.md') and '/_fonte/' not in path:entries.append((prefix.split()[2].decode(),path))
 # Cada resposta entrega o blob integral. Somente o cabeçalho necessário ao dedup é
 # persistido, junto do OID e SHA integral; não se lê MD do working tree como HEAD.
 proc=subprocess.Popen(['git','-C',str(root),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
 rows=[]
 try:
  for oid,path in entries:
   proc.stdin.write((oid+'\n').encode());proc.stdin.flush()
   response=proc.stdout.readline().decode().split()
   if len(response)!=3 or response[0]!=oid or response[1]!='blob':raise ValueError('cat-file inesperado')
   length=int(response[2]);blob=proc.stdout.read(length)
   if len(blob)!=length or proc.stdout.read(1)!=b'\n':raise ValueError('blob incompleto')
   meta,body=metadata(blob);rows.append(dict(path=path,oid=oid,sha256_md=SHA(blob),meta=meta))
 finally:
  proc.stdin.close();proc.stdout.close();status=proc.wait()
  if status:raise ValueError('cat-file terminou com falha')
 with gzip.open(controle/'HEAD-inventario.jsonl.gz','xt',encoding='utf-8') as out:
  for r in rows:out.write(json.dumps(r,ensure_ascii=False)+'\n')
 return head,rows

def validar(root,manifesto,hashes,total_esperado):
 m=json.loads(manifesto.read_text());maps=json.loads(hashes.read_text())
 relative=str(manifesto.relative_to(root))
 if maps.get(relative)!=digest(manifesto):raise ValueError('manifesto não confere com mapa SHA')
 for path,sha in maps.items():
  if digest(relpath(root,path))!=sha:raise ValueError('dependência SHA divergente: '+path)
 for path,sha in m['codigo'].items():
  if digest(relpath(root,path))!=sha:raise ValueError('código congelado divergente')
 candidates=[]
 for r in m['documentos']:
  p=relpath(root,r['privado']);blob=p.read_bytes()
  if SHA(blob)!=r['sha256_md']:raise ValueError('candidato SHA divergente')
  meta,body=metadata(blob);verificar_metadados(meta,r['captura']);title,sep,norm=body.partition('\n\n')
  if not sep or title!='# '+meta['titulo'] or SHA(norm.encode())!=r['QA']['sha256_corpo']:raise ValueError('H1/corpo divergente')
  item=r['captura']['item']
  expected=f"estaduais/AC/{item['pasta']}/{item['data'][:4]}/{'lc' if item['pasta']=='leis-complementares' else 'l'}-{item['numero']}-{item['data'][:4]}-legis{item['id_LEGIS']}.md"
  if r['path']!=expected or item['pasta'] not in ('leis-ordinarias','leis-complementares'):raise ValueError('destino não é o nome/pasta canônicos da identidade oficial')
  if meta.get('sha256_texto')!=SHA(norm.encode()):raise ValueError('SHA metadado do corpo diverge')
  if any(meta[k]!=item[k] for k in ['tipo','numero','data']) or meta.get('revogada') is not None or meta.get('uf')!='AC' or item.get('UF')!='AC':raise ValueError('metadata não conservadora/divergente')
  if meta.get('representacao_corpo')!='html-nativo-body-law-legis-ac-v1' or meta.get('edicao')!=m['edicao']:raise ValueError('modo/edição não explícitos')
  if meta['arquivo']!=r['captura']['url'] or meta['fonte']!=item['fonte']:raise ValueError('fonte/arquivo divergente')
  z=relpath(root,r['captura']['cache']).read_bytes()
  if SHA(z)!=r['captura']['sha256_cache'] or SHA(gzip.decompress(z))!=r['captura']['sha256_fonte']:raise ValueError('fonte integral SHA divergente')
  if os.path.lexists(relpath(root,r['path'])):raise ValueError('destino já existe em disco: '+r['path'])
  candidates.append(dict(path=r['path'],privado=r['privado'],sha256_md=r['sha256_md'],meta=meta))
 if len(candidates)!=m['total'] or m['total']!=total_esperado:raise ValueError('contagem fora do escopo LEGIS/AC HTML')
 return m,candidates

def publicar_sem_substituir(destino,blob):
 # link() falha atomicamente se qualquer destino surgir entre os checks; nenhum
 # os.replace() é usado sobre um caminho canônico preexistente.
 fd,tmp=tempfile.mkstemp(prefix='.ac-legis-',dir=destino.parent)
 try:
  with os.fdopen(fd,'wb') as out:out.write(blob);out.flush();os.fsync(out.fileno())
  os.link(tmp,destino)
 finally:os.unlink(tmp)

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--manifesto',required=True);ap.add_argument('--hashes',required=True);ap.add_argument('--total-esperado',type=int,required=True)
 ap.add_argument('--controle',required=True,help='diretório privado novo para intenção/journal/preimagens')
 ap.add_argument('--apply',action='store_true');ap.add_argument('--confirmar-root',choices=['ROOT'])
 a=ap.parse_args()
 if a.total_esperado<=0:ap.error("--total-esperado deve ser positivo")
 if a.apply and a.confirmar_root!='ROOT':ap.error('--apply é exclusivo ROOT e requer --confirmar-root ROOT')
 root=Path(run_git(Path.cwd(),'rev-parse','--show-toplevel').decode().strip()).resolve()
 control=relpath(root,a.controle)
 if not str(control.relative_to(root)).startswith('estaduais/AC/_fonte/auditorias/'):raise ValueError('controle deve estar no espaço privado de auditoria AC')
 control.mkdir(parents=True,exist_ok=False)
 volume=root.stat().st_dev
 manifest=relpath(root,a.manifesto);hashes=relpath(root,a.hashes)
 m,candidates=validar(root,manifest,hashes,a.total_esperado)
 head,rows=ler_HEAD(root,control);conferir_dedup(rows,candidates)
 if run_git(root,'rev-parse','HEAD').decode().strip()!=head:raise ValueError('HEAD mudou durante validação; repetir em controle novo')
 intention=dict(preparado_em=agora(),modo='apply_ROOT' if a.apply else 'dry-run',HEAD=head,total_HEAD=len(rows),total=len(candidates),manifesto=a.manifesto,sha256_manifesto=digest(manifest),mapa_sha=a.hashes,sha256_mapa=digest(hashes),dedup='Blobs integrais do HEAD atual: ID no namespace LEGIS/SAPL AC, arquivo por host/path/query, pasta+número literal+ano e paths; também dedup interno.',documentos=[dict(path=r['path'],privado=r['privado'],sha256=r['sha256_md'],preimagem_destino='ausente em disco e HEAD',backup_candidato=str((control/'backup'/r['path']).relative_to(root))) for r in candidates],limite='Commit/push não executados. Atomicidade por arquivo, não global; journal registra progresso para recuperação ROOT.')
 gravar_json(control/'intencao.json',intention)
 if not a.apply:
  gravar_json(control/'resultado.json',dict(finalizado_em=agora(),modo='dry-run',aptos=len(candidates),promovidos=0,HEAD=head));print(json.dumps(dict(modo='dry-run',aptos=len(candidates),promovidos=0,HEAD=head)));return
 # Candidatos originais e fontes continuam preservados; backup adicional antes de
 # qualquer escrita canônica e intenção já fsyncada permitem auditoria da operação.
 for r in candidates:
  backup=control/'backup'/r['path'];backup.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(relpath(root,r['privado']),backup)
  if digest(backup)!=r['sha256_md']:raise ValueError('backup SHA divergente')
 validar(root,manifest,hashes,a.total_esperado)
 with (control/'journal.jsonl').open('x',encoding='utf-8') as journal:
  for r in candidates:
   if not (root/'.git').exists() or root.stat().st_dev!=volume:raise RuntimeError('volume mudou/indisponível')
   if run_git(root,'rev-parse','HEAD').decode().strip()!=head:raise RuntimeError('HEAD mudou antes da troca; parar e consultar journal')
   dest=relpath(root,r['path'])
   if os.path.lexists(dest):raise ValueError('destino surgiu; não substituir')
   dest.parent.mkdir(parents=True,exist_ok=True)
   backup=control/'backup'/r['path'];blob=backup.read_bytes()
   if SHA(blob)!=r['sha256_md']:raise ValueError('backup alterado')
   publicar_sem_substituir(dest,blob)
   journal.write(json.dumps(dict(path=r['path'],sha256=digest(dest),criado_em=agora()),ensure_ascii=False)+'\n');journal.flush();os.fsync(journal.fileno())
 gravar_json(control/'resultado.json',dict(finalizado_em=agora(),modo='apply_ROOT',promovidos=len(candidates),HEAD=head,sem_Git_escrita=True))
 print(json.dumps(dict(modo='apply_ROOT',promovidos=len(candidates),HEAD=head)))
if __name__=='__main__':main()
