"""Patch privado de cabeçalho LEGIS/AC por preimagem. Dry-run padrão; ROOT aplica."""
import argparse,datetime,hashlib,json,os,shutil,tempfile
from pathlib import Path
from metadados_legis_ac import acrescentar,ler,verificar
SHA=lambda b:hashlib.sha256(b).hexdigest()
def safe(root,p):
 v=Path(p)
 if v.is_absolute() or '..' in v.parts:raise ValueError('caminho não relativo seguro')
 r=root/v
 if not r.resolve().is_relative_to(root):raise ValueError('fora do repositório')
 return r

def par(old,new,row):
 expected,proof=acrescentar(old,row)
 if expected!=new:raise ValueError('patch excede adição dos dois campos e ordem README')
 if ler(old)[1]!=ler(new)[1]:raise ValueError('corpo/H1 diverge')
 verificar(ler(new)[0],row);return proof

def validar(root,m,maps):
 for p,sha in maps.items():
  if SHA(safe(root,p).read_bytes())!=sha:raise ValueError('dependência SHA divergente: '+p)
 docs=[]
 for r in m['documentos']:
  it=r['captura']['item'];expected=f"estaduais/AC/{it['pasta']}/{it['data'][:4]}/{'lc' if it['pasta']=='leis-complementares' else 'l'}-{it['numero']}-{it['data'][:4]}-legis{it['id_LEGIS']}.md"
  if r['path']!=expected or it['pasta'] not in ('leis-ordinarias','leis-complementares') or it['UF']!='AC':raise ValueError('escopo/identidade do patch fora de AC')
  dest=safe(root,r['path']);pre=safe(root,r['preimagem']);candidate=safe(root,r['privado']);old=pre.read_bytes();new=candidate.read_bytes()
  meta,_=ler(old)
  if any(meta[k]!=it[k] for k in ['tipo','numero','data']) or meta.get('uf')!='AC' or meta['fonte']!=it['fonte']:raise ValueError('identidade da preimagem diverge')
  if SHA(old)!=r['sha256_preimagem'] or SHA(new)!=r['sha256_md']:raise ValueError('preimagem/candidato SHA divergente')
  if not dest.is_file() or SHA(dest.read_bytes())!=r['sha256_preimagem']:raise ValueError('canônico não é mais a preimagem: '+r['path'])
  proof=par(old,new,r['captura'])
  if proof!=r['prova_metadados']:raise ValueError('prova do cabeçalho diverge')
  docs.append((r,old,new))
 if len(docs)!=m['total'] or m.get('novas_normas')!=0:raise ValueError('escopo do patch divergente')
 return docs

def dump(p,v):
 with p.open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())

def main():
 a=argparse.ArgumentParser(description=__doc__);a.add_argument('--manifesto',required=True);a.add_argument('--hashes',required=True);a.add_argument('--controle',required=True);a.add_argument('--apply',action='store_true');a.add_argument('--confirmar-root',choices=['ROOT']);v=a.parse_args()
 if v.apply and v.confirmar_root!='ROOT':a.error('--apply exclusivo ROOT requer --confirmar-root ROOT')
 root=Path.cwd().resolve();control=safe(root,v.controle)
 if not str(control.relative_to(root)).startswith('estaduais/AC/_fonte/auditorias/'):raise ValueError('controle fora do espaço privado AC')
 control.mkdir(parents=True,exist_ok=False);mp=safe(root,v.manifesto);maps=json.loads(safe(root,v.hashes).read_text());m=json.loads(mp.read_text())
 if maps.get(v.manifesto)!=SHA(mp.read_bytes()):raise ValueError('manifesto fora do mapa')
 docs=validar(root,m,maps);dump(control/'intencao.json',dict(preparado_em=datetime.datetime.now().astimezone().isoformat(),modo='apply_ROOT' if v.apply else 'dry-run',total=len(docs),novas_normas=0,manifesto=v.manifesto,sha256_manifesto=SHA(mp.read_bytes()),mapa=v.hashes,documentos=[dict(path=r['path'],sha256_preimagem=r['sha256_preimagem'],sha256_novo=r['sha256_md'],corpo_H1_inalterado=True) for r,_,_ in docs]))
 if v.apply:
  for r,old,new in docs:
   backup=control/'backup'/r['path'];backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(old)
   if SHA(backup.read_bytes())!=r['sha256_preimagem']:raise ValueError('backup divergente')
  validar(root,m,maps);volume=root.stat().st_dev
  with (control/'journal.jsonl').open('x',encoding='utf-8') as journal:
   for r,old,new in docs:
    if not (root/'.git').exists() or root.stat().st_dev!=volume:raise RuntimeError('volume/repositório indisponível ou alterado')
    dest=safe(root,r['path'])
    if SHA(dest.read_bytes())!=r['sha256_preimagem']:raise ValueError('preimagem mudou antes da troca')
    fd,tmp=tempfile.mkstemp(prefix='.ac-metadados-',dir=dest.parent)
    try:
     with os.fdopen(fd,'wb') as f:f.write(new);f.flush();os.fsync(f.fileno())
     if SHA(dest.read_bytes())!=r['sha256_preimagem']:raise ValueError('preimagem mudou durante preparo')
     os.replace(tmp,dest)
    finally:
     if os.path.exists(tmp):os.unlink(tmp)
    journal.write(json.dumps(dict(path=r['path'],sha256=SHA(dest.read_bytes()),alterado_em=datetime.datetime.now().astimezone().isoformat()))+'\n');journal.flush();os.fsync(journal.fileno())
 dump(control/'resultado.json',dict(total=len(docs),alterados=len(docs) if v.apply else 0,novas_normas=0,sem_Git_escrita=True));print(json.dumps(dict(total=len(docs),alterados=len(docs) if v.apply else 0,novas_normas=0)))
if __name__=='__main__':main()
