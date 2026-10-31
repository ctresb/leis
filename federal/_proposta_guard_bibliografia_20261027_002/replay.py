from pathlib import Path
import json,gzip,hashlib,sys,importlib.util,collections
D=Path(__file__).resolve().parent;ROOT=D.parents[1];sys.path.insert(0,str(ROOT/'scripts'));fields=lambda text: (None,None,text.split('---',2)[2])
from integridade_html_federal import Visivel
spec=importlib.util.spec_from_file_location('guard_proposto_bibliografia',D/'integridade_anexos_decreto.py');guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard);sha=lambda b:hashlib.sha256(b).hexdigest();rows=[];delta=[];counts={}
for folder,n in [('001','9061'),('002','3608')]:
 count=0;changed=0
 p=ROOT/f'federal/_fonte/auditorias/retomada_federal_20261027_{folder}/fontes{n}/fontes{n}_parte001.jsonl.gz'
 with gzip.open(p,'rt') as f:
  for line in f:
   r=json.loads(line);src=r['html_original'];md=r['md_final'];assert sha(src.encode())==r['sha256_html'] and sha(md.encode())==r['sha256_md_final'];parsed=Visivel();parsed.feed(src);body=fields(md)[2];before=guard._anexo_proprio_ausente_guard56(body,parsed);after=guard.anexo_proprio_ausente(body,parsed);count+=1
   if before!=after:delta.append({'path':r['path'],'pacote':n,'sha256_md':r['sha256_md_final'],'sha256_html':r['sha256_html'],'guard56':before,'guard_proposto':after});changed+=1
 counts[n]={'corpos':count,'deltas':changed};print(n,counts[n],flush=True)
inv=json.loads((ROOT/'federal/_fonte/auditorias/retomada_federal_20261027_004/overlay_placeholders_publicados12669_v2.json').read_text());expected={r['path'] for r in inv['registros']};actual={r['path'] for r in delta};result={'resumo':counts,'sha256_guard_proposto':sha((D/'integridade_anexos_decreto.py').read_bytes()),'deltas':delta,'inventario65_sem_alerta':sorted(expected-actual),'alertas_fora_inventario65':sorted(actual-expected),'limites':'Replay somente leitura de 12.669 corpos congelados. Nenhuma máscara aplicada. Alertas exigem revisão individual; inclui deliberadamente o controle 18.735, cuja relação pode já estar reproduzida.'};p=D/'replay12669_v2.json';assert not p.exists();p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');assert not expected-actual and not actual-expected
