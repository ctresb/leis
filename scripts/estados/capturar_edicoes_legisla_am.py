"""Captura serial e retomável das páginas oficiais de edições já identificadas.

Fonte: índices/rotas do viewer público preservados. Não gera Markdown/PDFs novos,
nem presume que a paginação capturada constitua um ato individual.
"""
import argparse,datetime,gzip,hashlib,json,os,time
from pathlib import Path
from zoneinfo import ZoneInfo
from coletar_rn_fontes import capturar
SHA=lambda b:hashlib.sha256(b).hexdigest()
def main():
    if not Path('.git').exists():raise ValueError('repositório/volume ausente')
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--origem',required=True);ap.add_argument('--lote',required=True);ap.add_argument('--retomar',action='store_true');a=ap.parse_args();origin=Path(a.origem);m=json.loads(origin.read_text());base=Path('estaduais/AM/_fonte/auditorias')/a.lote
    if base.exists() and not a.retomar:raise ValueError('lote já iniciado; preservar')
    base.mkdir(exist_ok=a.retomar);log=base/'capturas.jsonl';previous={}
    if log.exists():
        for line in log.read_text().splitlines():
            r=json.loads(line)
            if r.get('http')==200 and r.get('PDF'):previous[(r['edicao_id'],r['pagina'])]=r
    indices=[r for r in m['capturas'] if r['tipo']=='indice_paginas'];reuse={(r['edicao_id'],int(r['pagina'])):r for r in m['capturas'] if r.get('PDF')};plan=[]
    for r in indices:
        raw=gzip.decompress(Path(r['cache']).read_bytes())
        if SHA(raw)!=r['sha256_fonte']:raise ValueError('índice primário divergente')
        idx=json.loads(raw);pages=[int(q['pagina']) for q in idx['itens']]
        if idx['erro'] or pages!=list(range(1,len(pages)+1)) or any(str(q['id'])!=r['edicao_id'] for q in idx['itens']):raise ValueError('índice de páginas inconclusivo')
        plan.extend(dict(edicao_id=r['edicao_id'],pagina=p,indice_SHA256=r['sha256_fonte']) for p in pages)
    rows=[];bad=0;stopped=False
    with log.open('a' if a.retomar else 'x') as out:
        for item in plan:
            if not Path('.git').exists():raise ValueError('volume ausente; interromper sem recriar diretórios')
            key=(item['edicao_id'],item['pagina']);old=previous.get(key) or reuse.get(key);side=base/(key[0]+'-'+str(key[1])+'.json')
            if old:
                packed=Path(old['cache']).read_bytes();raw=gzip.decompress(packed)
                if SHA(packed)!=old['sha256_cache'] or SHA(raw)!=old['sha256_fonte']:raise ValueError('cache anterior divergente')
                r=dict(old,**item,origem='captura anterior reutilizada por edição/página e SHA')
            elif side.exists():
                r=json.loads(side.read_text());packed=Path(r['cache']).read_bytes()
                if SHA(packed)!=r['sha256_cache'] or SHA(gzip.decompress(packed))!=r['sha256_fonte']:raise ValueError('sidecar/cache divergente')
                r['origem']='sidecar durável anterior reutilizado'
            else:
                url='https://diario.imprensaoficial.am.gov.br/apifront/portal/edicoes/pdf_diario/'+key[0]+'/'+str(key[1]);r=dict(**item,url=url,iniciado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat());time.sleep(1.2)
                try:st,b,h,end=capturar(url)
                except Exception as e:r.update(erro=type(e).__name__+': '+str(e));bad+=1
                else:
                    packed=gzip.compress(b);p=base/(SHA(b)+'.pdf.gz');r.update(http=st,url_final=end,cache=str(p),sha256_fonte=SHA(b),sha256_cache=SHA(packed),PDF=b.startswith(b'%PDF-'),bytes=len(b),headers={k:v for k,v in h.items() if k.lower() not in ('set-cookie','cookie','authorization','proxy-authorization')},finalizado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat())
                    # Receipt e hashes primeiro: eventual interrupção não inventa proveniência.
                    with side.open('x') as s:s.write(json.dumps(r,ensure_ascii=False)+'\n');s.flush();os.fsync(s.fileno())
                    if not p.exists():p.write_bytes(packed)
                    bad=0 if st==200 and r['PDF'] else bad+1
            if key not in previous:out.write(json.dumps(r,ensure_ascii=False)+'\n');out.flush();os.fsync(out.fileno())
            rows.append(r);print(key[0],key[1],r.get('http',r.get('erro')),'PDF',r.get('PDF'),flush=True)
            if r.get('http') in (401,403,429) or bad>=3:stopped=True;break
    manifest=Path('scripts/estados/manifestos')/(a.lote+'.json');manifest.write_text(json.dumps(dict(finalizado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat(),origem=a.origem,sha256_origem=SHA(origin.read_bytes()),paginas_planejadas=len(plan),PDFs_capturados=sum(r.get('http')==200 and r.get('PDF',False) for r in rows),parada_conservadora=stopped,edicoes={r['edicao_id']:len(json.loads(gzip.decompress(Path(r['cache']).read_bytes()))['itens']) for r in indices},capturas=rows,sem_MD=True,representacao='Páginas PDF individuais fornecidas pelo viewer; não declara arquivo PDF integral único do emissor.'),ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
