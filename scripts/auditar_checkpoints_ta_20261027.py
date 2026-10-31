"""Preflight offline de caches e checkpoints TA; nunca busca nem reescreve fontes."""
import argparse
import collections
import gzip
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def sha(data):return hashlib.sha256(data).hexdigest()

def validar(host,folder,cache):
    errors=[];blocked=[];ledger=[]
    for meta in sorted(cache.glob('*.meta.json')):
        info=json.loads(meta.read_text());stem=meta.name[:-10];paths=[cache/(stem+ext) for ext in ('.json','.html') if (cache/(stem+ext)).is_file()]
        if len(paths)!=1:errors.append(dict(metadata=str(meta),erro='Par bruto/metadata ausente ou ambiguo'));continue
        raw=paths[0].read_bytes()
        if sha(raw)!=info['sha256']:errors.append(dict(arquivo=str(paths[0]),erro='SHA divergente'))
        if info['status'] in (403,429):blocked.append(dict(metadata=str(meta),url=info.get('url'),status=info['status']))
        if paths[0].suffix=='.json' and info['status']==200:
            try:json.loads(raw)
            except Exception as exc:errors.append(dict(arquivo=str(paths[0]),erro='JSON invalido: '+str(exc)))
        ledger.append(dict(arquivo=str(paths[0]),sha256=sha(raw),bytes=len(raw),metadata=str(meta),sha256_metadata=sha(meta.read_bytes()),status=info['status']))
    for path in cache.iterdir():
        if path.suffix in ('.html','.json') and not path.name.endswith('.meta.json') and not path.with_suffix('.meta.json').is_file():errors.append(dict(arquivo=str(path),erro='Bruto orfao, sem metadata'))
    journal=folder/'resultados.jsonl';raw=journal.read_bytes();end=raw.rfind(b'\n')+1
    if end!=len(raw):errors.append(dict(arquivo=str(journal),erro='Linha final parcial'))
    rows=[json.loads(s) for s in raw[:end].decode().splitlines()];latest={str(r['ta_id']):r for r in rows}
    cp=folder/'checkpoint.json';checkpoint=json.loads(cp.read_text()) if cp.exists() else {}
    if not isinstance(checkpoint,dict) or set(checkpoint)-set(latest):errors.append(dict(arquivo=str(cp),erro='Checkpoint sem correspondencia no diario'))
    manifest=folder/'manifesto.json';summary=None
    if manifest.exists():
        summary=json.loads(manifest.read_text());summary={k:summary.get(k) for k in ('metadados_unicos_observados','total_api_declarado','catalogo_numericamente_consistente','candidatos','script_sha256')}
        if summary['metadados_unicos_observados']!=len(latest) or summary['total_api_declarado']!=len(latest) or not summary['catalogo_numericamente_consistente']:errors.append(dict(arquivo=str(manifest),erro='Manifesto e diario divergem'))
    result=dict(host=host,folder=str(folder),cache=str(cache),pares=len(ledger),linhas=len(rows),ids_unicos=len(latest),sha256_journal=sha(raw),sha256_checkpoint=sha(cp.read_bytes()) if cp.exists() else None,manifesto=summary,manifesto_sha256=sha(manifest.read_bytes()) if manifest.exists() else None,erros=errors,bloqueios=blocked,apto_retomada=not errors and not blocked and summary is None,concluido=not errors and bool(summary),limite='Integridade de checkpoint e cache; nao certifica integralidade juridica, vigencia ou publicabilidade das normas.')
    return result,ledger

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--saida',type=Path,required=True);a=ap.parse_args();a.saida.mkdir(exist_ok=False)
    rows=[]
    for host,base in [('sapl.portovelho.ro.leg.br','20261020-textos-articulados-captura'),('sapl.agudo.rs.leg.br','20261021-textos-articulados-fila-sigi'),('sapl.amontada.ce.leg.br','20261021-textos-articulados-fila-sigi')]:
        result,ledger=validar(host,ROOT/'municipais/_lotes'/base/host,ROOT/'municipais/_fonte/texto-articulado-sapl'/host);path=a.saida/(host+'.pares.jsonl.gz');path.write_bytes(gzip.compress(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in ledger).encode(),mtime=0));result['ledger']=dict(arquivo=str(path),sha256=sha(path.read_bytes()));rows.append(result);print(json.dumps(dict(host=host,pares=result['pares'],ids=result['ids_unicos'],erros=len(result['erros']),bloqueios=len(result['bloqueios']),apto_retomada=result['apto_retomada'],concluido=result['concluido'])),flush=True)
    (a.saida/'controle.json').write_text(json.dumps(dict(resultados=rows,codigo_sha256=sha(Path(__file__).read_bytes())),ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
