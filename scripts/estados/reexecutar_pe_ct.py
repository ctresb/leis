"""Replay serial dos candidatos privados -CT, sem promover arquivos canônicos."""
import argparse,gzip,hashlib,json
from pathlib import Path
from pe_identidade_ct import auditar_ct

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--manifesto',required=True);ap.add_argument('--saida',required=True);a=ap.parse_args();m=json.loads(Path(a.manifesto).read_text());bad=0
    with Path(a.saida).open('x') as out:
        for r in m['documentos']:
            row=dict(destino=r['destino'],aceito=False)
            try:
                z=Path(r['candidato']).read_bytes();b=gzip.decompress(z)
                if hashlib.sha256(z).hexdigest()!=r['sha256_candidato_gzip'] or hashlib.sha256(b).hexdigest()!=r['sha256_candidato']:raise ValueError('candidato mudou')
                cap=r['captura'];source=gzip.decompress(Path(cap['captura']).read_bytes())
                if hashlib.sha256(source).hexdigest()!=cap['sha256_resposta']:raise ValueError('fonte mudou')
                proof=auditar_ct(b,source,cap['item_indice'],cap['content_type']);row.update(aceito=True,QA=proof)
            except Exception as e:row['erro']=type(e).__name__+': '+str(e);bad+=1
            out.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(json.dumps(dict(total=len(m['documentos']),falhas=bad)))
    if bad:raise SystemExit(1)
if __name__=='__main__':main()
