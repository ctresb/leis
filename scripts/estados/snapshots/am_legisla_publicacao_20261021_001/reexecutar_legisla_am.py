"""Replay privado de candidatos Legisla.AM por fonte, CSS e CommonMark integrais."""
import argparse,gzip,json
from pathlib import Path
from am_legisla_candidatos import contexto,revisar,compor,SHA
from auditar_legisla_am_cache import auditar
from representacao_html_legisla_am import extrair_campo

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--manifesto',required=True);ap.add_argument('--saida',required=True);a=ap.parse_args();m=json.loads(Path(a.manifesto).read_text());ctx=contexto();bad=0;ids=set();keys=set()
    for p,s in m['dependencias'].items():
        if SHA(Path(p).read_bytes())!=s:raise ValueError('dependência alterada: '+p)
    with Path(a.saida).open('x') as out:
        for r in m['documentos']:
            row=dict(destino=r['destino'],aceito=False)
            try:
                cap=r['captura'];z=Path(r['candidato']).read_bytes();raw=gzip.decompress(z);source=Path(cap['cache']).read_bytes();qa=auditar(cap,source,contexto_css=ctx);remaining,review=revisar(qa,r['revisao_contextual'],cap['sha256_fonte'])
                if remaining:raise ValueError('retenção contextual não resolvida')
                if SHA(raw)!=r['sha256_candidato'] or SHA(z)!=r['sha256_candidato_gzip']:raise ValueError('candidato mudou')
                field,_=extrair_campo(gzip.decompress(source).decode('utf8'));expected,meta=compor(cap,qa,field,review)
                if raw!=expected:raise ValueError('MD difere da composição integral e metadados comprovados')
                key=(qa['tipo'],qa['numero'],qa['data'][:4]);id_=cap['item']['id_legisla']
                if key in keys or id_ in ids:raise ValueError('identidade repetida no lote')
                ids.add(id_);keys.add(key);row.update(aceito=True,sha256_candidato=SHA(raw),QA=qa)
            except Exception as e:bad+=1;row['erro']=type(e).__name__+': '+str(e)
            out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush()
    print(json.dumps(dict(total=len(m['documentos']),falhas=bad)))
    if bad:raise SystemExit(1)
if __name__=='__main__':main()
