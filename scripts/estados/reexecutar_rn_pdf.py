"""Replay somente leitura dos candidatos RN contra PDF e conteúdo CommonMark."""
import argparse,gzip,hashlib,json,subprocess
from pathlib import Path
from markdown_it import MarkdownIt
from auditar_rn_retomada_pdf import auditar

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--manifesto',required=True);ap.add_argument('--saida',required=True);a=ap.parse_args();m=json.loads(Path(a.manifesto).read_text());parser=MarkdownIt('commonmark',{'html':True});bad=0
    with Path(a.saida).open('x') as out:
        for r in m['documentos']:
            raw=Path(r['path']).read_bytes();result=dict(path=r['path'],sha256_md=hashlib.sha256(raw).hexdigest(),aceito=False)
            try:
                if result['sha256_md']!=r['sha256_md']:raise ValueError('SHA MD diverge do manifesto')
                body,proof=auditar(r['captura'],raw)
                # Conteúdo das cercas é confrontado com a extração bruta preservada por página.
                textfile=Path(r['captura']['cache']).parent/'QA'/str(m['documentos'].index(r)+1)/'camada.txt';text=textfile.read_text();pages=text.split('\f');pages=pages[:-1] if pages and not pages[-1].strip() else pages
                if hashlib.sha256(text.encode()).hexdigest()!=proof['sha256_camada']:raise ValueError('camada preservada diverge de nova extração')
                fences=[t.content for t in parser.parse(body) if t.type=='fence']
                if fences!=[p if p.endswith('\n') else p+'\n' for p in pages]:raise ValueError('CommonMark altera camada textual')
                result.update(aceito=True,QA=proof,CommonMark_cercas_iguais=True)
            except Exception as e:result['erro']=type(e).__name__+': '+str(e);bad+=1
            out.write(json.dumps(result,ensure_ascii=False)+'\n')
    print(json.dumps(dict(total=len(m['documentos']),falhas=bad)))
    if bad:raise SystemExit(1)
if __name__=='__main__':main()
