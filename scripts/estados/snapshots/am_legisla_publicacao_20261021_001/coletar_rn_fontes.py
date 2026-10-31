"""Captura serial de uma seleção explícita do índice oficial RN, sem gerar Markdown.

Preserva cada resposta por SHA e interrompe recusas ou três falhas consecutivas.
"""
import argparse,datetime,gzip,hashlib,json,time,urllib.request,urllib.error
from pathlib import Path
from zoneinfo import ZoneInfo

def capturar(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; legislative archive)"}),timeout=40) as resp:
            return resp.status,resp.read(),dict(resp.headers),resp.url
    except urllib.error.HTTPError as e:
        return e.code,e.read(),dict(e.headers),e.url


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--selecao',required=True);ap.add_argument('--lote',required=True);args=ap.parse_args()
    items=json.loads(Path(args.selecao).read_text());base=Path('estaduais/RN/_fonte/auditorias')/args.lote;base.mkdir(parents=True,exist_ok=True);log=base/'capturas.jsonl';rows=[];bad=0
    if log.exists():raise ValueError('Lote já existe; não reiniciar captura')
    with log.open('x') as out:
        for it in items:
            url=it['url']
            if not url.startswith('https://www.al.rn.leg.br/storage/legislacao/') or not url.lower().endswith('.pdf'):raise ValueError(url)
            started=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat();r=dict(item=it,iniciado_em=started,url=url)
            try:
                st,b,headers,final=capturar(url)
            except Exception as e:
                r.update(erro=type(e).__name__+': '+str(e));bad+=1
            else:
                sha=hashlib.sha256(b).hexdigest();p=base/(sha+'.bin.gz')
                if not p.exists():p.write_bytes(gzip.compress(b))
                r.update(http=st,headers=headers,url_final=final,cache=str(p),sha256_fonte=sha,sha256_cache=hashlib.sha256(p.read_bytes()).hexdigest(),PDF=b.startswith(b'%PDF-'));bad=0 if st==200 and b.startswith(b'%PDF-') else bad+1
            r['finalizado_em']=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat();out.write(json.dumps(r,ensure_ascii=False)+'\n');out.flush();rows.append(r);print(len(rows),r.get('http',r.get('erro')),it['titulo'],flush=True)
            if r.get('http') in (401,403,429) or bad>=3:break
            time.sleep(1.2)
    manifest=Path('scripts/estados/manifestos')/(args.lote+'.json');manifest.write_text(json.dumps(dict(selecao=args.selecao,sha256_selecao=hashlib.sha256(Path(args.selecao).read_bytes()).hexdigest(),total_selecionado=len(items),total_capturado=len(rows),capturas=rows,sem_MD=True),ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
