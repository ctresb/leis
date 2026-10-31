from pathlib import Path
import sys,json,gzip,hashlib,datetime,time,urllib.parse
from zoneinfo import ZoneInfo
sys.path.insert(0,'scripts/estados')
from coletar_rn_fontes import capturar
items=json.loads(Path('scripts/estados/manifestos/sapl-anexos-recentes-20261021-001-selecao.json').read_text());rows=[];blocked=set()
for x in items:
 uf=x['UF'];url=x['item']['texto_integral'].replace('http://','https://');r=dict(UF=uf,item=x['item'],tipo_indice=x['tipo_indice'],url=url,iniciado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat())
 if uf in blocked:continue
 base=Path('estaduais')/uf/'_fonte/auditorias/anexos-recentes-20261021-001';base.mkdir(parents=True,exist_ok=True)
 try:st,b,headers,final=capturar(url)
 except Exception as e:r['erro']=type(e).__name__+': '+str(e);blocked.add(uf)
 else:
  sha=hashlib.sha256(b).hexdigest();p=base/(sha+'.bin.gz')
  if not p.exists():p.write_bytes(gzip.compress(b))
  r.update(http=st,headers=headers,url_final=final,cache=str(p),sha256_fonte=sha,sha256_cache=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=len(b));
  if st!=200:blocked.add(uf)
 r['finalizado_em']=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat();rows.append(r);print(uf,x['item']['id'],r.get('http',r.get('erro')),r.get('bytes'),flush=True);time.sleep(1.2)
Path('scripts/estados/manifestos/sapl-anexos-recentes-20261021-001.json').write_text(json.dumps(dict(capturas=rows,sem_MD=True,sem_retomada_apos_recusa=True),ensure_ascii=False,indent=2)+'\n')
