"""Inventário/captura serial da lista oficial Legisla.AM, sem gerar Markdown.

Segue somente paginação rel=next observada. Tipos/números/anos existentes no disco
não são baixados novamente. Não presume integralidade ou vigência dos candidatos.
"""
import argparse,datetime,gzip,hashlib,html,json,re,time,urllib.parse
from pathlib import Path
from zoneinfo import ZoneInfo
from coletar_rn_fontes import capturar
BASE='https://legisla.imprensaoficial.am.gov.br'
SHA=lambda b:hashlib.sha256(b).hexdigest()
CLEAN=lambda s:' '.join(html.unescape(re.sub(r'<[^>]*>',' ',s)).split())

def itens_lista(source):
    rows=[]
    for block in re.findall(r'<li class="item-li">(.*?)</li>',source,re.S):
        title=re.search(r'<h5>(.*?)</h5>',block,re.S);link=re.search(r'href="([^"]+)"[^>]*>.*?Texto integral',block,re.S)
        if not title or not link:raise ValueError('item de índice sem título/link')
        url=urllib.parse.urljoin(BASE,html.unescape(link[1]));u=urllib.parse.urlparse(url);m=re.fullmatch(r'/diario_am/12/(\d{4})/(\d{1,2})/(\d+)',u.path)
        if not m or u.netloc!=urllib.parse.urlparse(BASE).netloc:raise ValueError('URL fora da categoria oficial de leis')
        t=CLEAN(title[1]);n=re.search(r'LEI\s*N\s*[.º°o\s]*([\d.]+(?:-[A-Z]+)?)',t,re.I)
        kind='Lei Ordinária' if n else ('Lei Complementar' if re.search(r'LEI\s+COMPLEMENTAR',t,re.I) else 'Tipo/número inconclusivo')
        pub=re.search(r'<p>(.*?)</p>',block,re.S)
        rows.append(dict(id_legisla=m[3],titulo=t,numero=n[1].replace('.','').lstrip('0') if n else None,tipo_indice=kind,ano=m[1],mes=m[2],url=url,publicacao_indice=CLEAN(pub[1]) if pub else ''))
    nxt=re.search(r'<a\b(?=[^>]*rel="next")[^>]*href="([^"]+)"',source)
    return rows,urllib.parse.urljoin(BASE,html.unescape(nxt[1])) if nxt else None

def chaves_disco():
    keys={}
    for p in Path('estaduais/AM/leis-ordinarias').glob('*/*.md'):
        meta={}
        with p.open() as f:
            next(f)
            for line in f:
                if line.rstrip('\n')=='---':break
                if ': ' in line:
                    k,v=line.rstrip('\n').split(': ',1)
                    try:meta[k]=json.loads(v)
                    except ValueError:meta[k]=v
        num=str(meta.get('numero') or '').replace('.','').lstrip('0');year=str(meta.get('data') or '')[:4]
        if num and re.fullmatch(r'\d{4}',year):keys.setdefault((num.upper(),year),[]).append(str(p))
        else:
            # Não permite que metadado incompleto transforme possível alias em novo documento.
            m=re.search(r'-(\d+(?:-[A-Za-z]+)?)-(\d{4})-id\d+[.]md$',p.name)
            if m:keys.setdefault((m[1].lstrip('0').upper(),m[2]),[]).append(str(p))
    return keys

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--lote',required=True);ap.add_argument('--retomar',action='store_true');a=ap.parse_args();idx=Path('estaduais/AM/_indice')/a.lote;src=Path('estaduais/AM/_fonte/auditorias')/a.lote
    if (idx.exists() or src.exists()) and not a.retomar:raise ValueError('lote já iniciado; preservar e reconciliar antes de retomar')
    idx.mkdir(parents=True,exist_ok=True);src.mkdir(parents=True,exist_ok=True);keys=chaves_disco();seen=set();page=1;rows=[];receipts=[];stopped=False;url=BASE+'/diario_am/12?direction=desc&modo=lista&sort=data';selected={}
    if a.retomar:
        rows=list(map(json.loads,(idx/'progresso.jsonl').read_text().splitlines()));seen={r['item']['id_legisla'] for r in rows};receipts=list({r['indice']['url']:r['indice'] for r in rows}.values())
        for r in rows:
            if r['status']=='capturado':selected.setdefault((r['item']['numero'].upper(),r['item']['ano']),[]).append(r['item']['id_legisla'])
        if rows:url=rows[-1]['indice']['url'];page=int(urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get('page',['1'])[0])
    with (idx/'progresso.jsonl').open('a' if a.retomar else 'x') as log:
        while url:
            if urllib.parse.urlparse(url).netloc!=urllib.parse.urlparse(BASE).netloc:raise ValueError('paginação fora da fonte')
            cache=idx/f'pagina-{page:04}.html.gz'
            if cache.exists():
                b=gzip.decompress(cache.read_bytes());st=200;headers={};final=url
            elif page==1:
                original=Path('estaduais/AM/_indice/legisla-retomada-20261021-001/leis-ordinarias-lista.html.gz');b=gzip.decompress(original.read_bytes());st=200;headers={};final=url
            else:
                try:st,b,headers,final=capturar(url)
                except Exception as e:stopped=True;receipts.append(dict(url=url,erro=type(e).__name__+': '+str(e)));break
            reused=cache.exists()
            if not reused:cache.write_bytes(gzip.compress(b))
            receipt=next((r for r in receipts if r['url']==url),None)
            if receipt is None:
                receipt=dict(url=url,http=st,cache=str(cache),sha256_fonte=SHA(b),auditado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat(),origem='cache anterior preservado; hora HTTP original não recuperada' if reused else 'captura HTTP atual',headers=headers);receipts.append(receipt)
                if not reused:receipt['capturado_em']=receipt['auditado_em']
            (idx/f'pagina-{page:04}.meta.json').write_text(json.dumps(receipt,ensure_ascii=False)+'\n')
            if st!=200:stopped=True;break
            items,nexturl=itens_lista(b.decode('utf8'))
            if not items:raise ValueError('índice vazio inconclusivo')
            for it in items:
                if it['id_legisla'] in seen:continue
                seen.add(it['id_legisla']);key=((it['numero'] or '').upper(),it['ano']);r=dict(item=it,indice=receipt,chaves_disco=keys.get(key,[]),status='preexistente' if key in keys else 'candidato_ausente')
                if it.get('tipo_indice')!='Lei Ordinária':r.update(status='categoria_divergente_retida',motivo='Título do item não corresponde à categoria de leis ordinárias; não reclassificar automaticamente')
                elif key in selected:r.update(status='alias_indice_retido',outros_ids_mesma_identidade=selected[key])
                elif key not in keys:
                    time.sleep(1.2)
                    try:code,raw,h,end=capturar(it['url'])
                    except Exception as e:r.update(status='erro_captura',erro=type(e).__name__+': '+str(e));stopped=True
                    else:
                        sh=SHA(raw);p=src/(it['id_legisla']+'-'+sh+'.html.gz');p.write_bytes(gzip.compress(raw));r.update(http=code,headers=h,url_final=end,cache=str(p),sha256_fonte=sh,sha256_cache=SHA(p.read_bytes()),capturado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat(),status='capturado' if code==200 else 'http_retido');stopped=code!=200
                if r['status']=='capturado':selected.setdefault(key,[]).append(it['id_legisla'])
                rows.append(r);log.write(json.dumps(r,ensure_ascii=False)+'\n');log.flush()
                if stopped:break
            print('PAGINA',page,'total',len(rows),'capturados',sum(r['status']=='capturado' for r in rows),flush=True)
            if stopped:break
            url=nexturl;page+=1;time.sleep(1.2)
    manifest=Path('scripts/estados/manifestos')/(a.lote+'.json');manifest.write_text(json.dumps(dict(finalizado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat(),parada_conservadora=stopped,sem_MD=True,total_indice=len(rows),total_capturado=sum(r['status']=='capturado' for r in rows),indices=receipts,documentos=rows),ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
