"""Replay offline LEGIS/AC: fonte integral, CSS/JS, identidade e CommonMark."""
import argparse,hashlib,json,sys
from pathlib import Path
from auditar_legis_ac import AuditorAC
from representacao_html_ac_legis import MODO
from metadados_legis_ac import verificar as verificar_metadados
SHA=lambda b:hashlib.sha256(b).hexdigest()
def metadata(blob):
 text=blob.decode('utf-8');assert text.startswith('---\n');h,b=text[4:].split('\n---\n',1);out={}
 for line in h.splitlines():
  k,v=line.split(': ',1)
  if k in out:raise ValueError('metadado repetido')
  out[k]=json.loads(v)
 return out,b

def conferir_revisao_contextual(revisao,row,q):
 it=row['item']
 if not revisao or revisao.get('decisao')!='apto_contextual':raise ValueError('revisão contextual explícita ausente')
 if any(revisao.get(k)!=it[k] for k in ['id_LEGIS','tipo','numero','data']):raise ValueError('identidade da revisão contextual diverge')
 if revisao.get('sha256_fonte')!=row['sha256_fonte'] or revisao.get('sha256_corpo')!=q['sha256_corpo'] or revisao.get('sha256_matrizes')!=q['fidelidade']['sha256_matrizes']:raise ValueError('fonte/corpo/matriz da revisão contextual diverge')
 if revisao.get('contextos_objetos')!=q['contextos_objetos'] or revisao.get('epigrafes_contextuais')!=q['epigrafes_contextuais'] or not revisao.get('fundamento'):raise ValueError('contextos/fundamento da revisão divergem')
 if q['epigrafes_contextuais']:raise ValueError('epígrafes secundárias exigem outro procedimento contextual')
 return True

def replay(manifesto,hashes):
 m=json.loads(Path(manifesto).read_text());maps=json.loads(Path(hashes).read_text())
 if maps.get(str(Path(manifesto)))!=SHA(Path(manifesto).read_bytes()):raise ValueError('manifesto fora do mapa')
 for p,sha in maps.items():
  path=Path(p)
  if path.is_absolute() or '..' in path.parts or SHA(path.read_bytes())!=sha:raise ValueError('dependência/caminho divergente: '+p)
 reviews={}
 if m.get('revisoes_contextuais'):
  rr=m['revisoes_contextuais'];raw=Path(rr['arquivo']).read_bytes()
  if SHA(raw)!=rr['sha256'] or maps.get(rr['arquivo'])!=rr['sha256']:raise ValueError('recibo contextual fora do mapa ou SHA divergente')
  for r in json.loads(raw)['revisoes']:
   if r['id_LEGIS'] in reviews:raise ValueError('revisão contextual repetida')
   reviews[r['id_LEGIS']]=r
 a=AuditorAC(m['CSS'],m['JS']);count=0
 for r in m['documentos']:
  blob=Path(r['privado']).read_bytes()
  if SHA(blob)!=r['sha256_md']:raise ValueError('candidato SHA divergente')
  meta,body=metadata(blob);verificar_metadados(meta,r['captura']);heading,sep,norm=body.partition('\n\n');it=r['captura']['item']
  if not sep or heading!='# '+meta['titulo'] or meta['representacao_corpo']!=MODO:raise ValueError('H1/modo divergente')
  if any(meta[k]!=it[k] for k in ['tipo','numero','data']) or meta['fonte']!=it['fonte'] or meta['arquivo']!=r['captura']['url'] or meta['revogada'] is not None or meta['uf']!='AC':raise ValueError('identidade/status não conservador')
  if meta['edicao']!=m['edicao'] or meta['sha256_texto']!=SHA(norm.encode()):raise ValueError('edição/SHA corpo divergente')
  native,q=a.auditar(r['captura'],norm)
  if q['sha256_corpo']!=r['QA']['sha256_corpo'] or q['fidelidade']!=r['QA']['fidelidade']:raise ValueError('replay de fidelidade diverge')
  if q['contextos_objetos'] or q['epigrafes_contextuais']:conferir_revisao_contextual(reviews.get(it['id_LEGIS']),r['captura'],q)
  count+=1
 if count!=m['total']:raise ValueError('total divergente')
 return dict(total=count,aprovados=count,falhas=0,rede=False,promovidos=0)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--manifesto',required=True);p.add_argument('--hashes',required=True);p.add_argument('--recibo',required=True);a=p.parse_args();r=replay(a.manifesto,a.hashes)
 with Path(a.recibo).open('x') as f:f.write(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(r))
if __name__=='__main__':main()
