"""Snapshot offline de candidatos ainda não examinados da fila SIGI existente.

Não abre rede ou reinicia clientes. Copia linhas originais completas e metadados
existentes, registra SHA e tamanho do prefixo de origem e preserva timestamps.
Portais sem tipos/anexos completos permanecem pendentes.
"""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def sha(b):return hashlib.sha256(b).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fila',type=Path,required=True);ap.add_argument('--snapshot-anterior',type=Path,required=True);ap.add_argument('--ultimo-gate',type=Path,required=True);ap.add_argument('--saida',type=Path,required=True);a=ap.parse_args();a.saida.mkdir(exist_ok=False)
 prior=json.loads(a.snapshot_anterior.read_text());excluded=set();proofs=[]
 for p in dict.fromkeys([r['path'] for r in prior['exclusoes']]+[str(a.ultimo_gate)]):
  raw=Path(p).read_bytes();proofs.append(dict(path=p,sha256=sha(raw),bytes=len(raw)))
  for r in map(json.loads,raw.decode().splitlines()):excluded.add((r['host'],r['ta_id']))
 reports=[];pending=[];total=0
 for journal in sorted(a.fila.glob('*/resultados.jsonl')):
  host=journal.parent.name;raw=journal.read_bytes();complete=raw[:raw.rfind(b'\n')+1];latest={}
  for line in complete.splitlines(keepends=True):
   row=json.loads(line);latest[row['ta_id']]=(row,line)
  chosen=[(row,line) for row,line in latest.values() if row['estado']=='candidato_estruturado_para_auditoria' and (host,row['ta_id']) not in excluded]
  if not chosen:continue
  annex=journal.parent/'anexos-index.json';url=f'https://{host}/api/norma/tiponormajuridica/?page_size=100&page=1';types=ROOT/'municipais/_indice/organicas-sapl'/host/(sha(url.encode())+'.json')
  try:
   if not annex.is_file() or not types.is_file():raise ValueError('Índice de anexos ou tipos ainda ausente')
   annex_raw=annex.read_bytes();types_raw=types.read_bytes();annex_data=json.loads(annex_raw);type_data=json.loads(types_raw)
   if type_data['pagination'].get('next_page') or not annex_data.get('completo'):raise ValueError('Índice de tipos ou anexos incompleto')
  except Exception as error:pending.append(dict(host=host,candidatos=len(chosen),motivo=str(error)));continue
  dest=a.saida/host;dest.mkdir();selected=b''.join(line for _,line in chosen);(dest/'resultados.jsonl').write_bytes(selected);(dest/'anexos-index.json').write_bytes(annex_raw);total+=len(chosen)
  reports.append(dict(host=host,origem=str(journal),bytes_prefixo=len(complete),sha256_prefixo=sha(complete),candidatos=len(chosen),snapshot=str(dest/'resultados.jsonl'),sha256_snapshot=sha(selected),anexos_origem=str(annex),sha256_anexos=sha(annex_raw),tipos_origem=str(types.relative_to(ROOT)),sha256_tipos=sha(types_raw),linhas=[dict(ta_id=r['ta_id'],norma_id=r['norma_id'],sha256_linha_original=sha(line)) for r,line in chosen]))
 result=dict(candidatos=total,portais=len(reports),fontes=reports,exclusoes=proofs,pendentes=pending,codigo_sha256=sha(Path(__file__).read_bytes()),limite='Entrada privada derivada de linhas originais; não prova catálogo completo, vigência ou publicação. Gates de API municipal, identidade, fonte, contexto, render e dedup continuam obrigatórios.')
 (a.saida/'controle-entrada.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(candidatos=total,portais=len(reports),pendentes=len(pending))))
if __name__=='__main__':main()
