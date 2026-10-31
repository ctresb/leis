"""Replay de seis páginas CE: fonte PDF, glifos, fluxo BT e quatro motores; sem promoção."""
import argparse,gzip,hashlib,io,json,sys,unittest
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument('--raiz',required=True);p.add_argument('--manifesto',required=True);p.add_argument('--qa',required=True);p.add_argument('--qa-html5',required=True);p.add_argument('--controle',required=True);a=p.parse_args();root=Path(a.raiz).resolve();m=json.loads((root/a.manifesto).read_text());out=Path(a.controle);out.mkdir(parents=True,exist_ok=False);sha=lambda b:hashlib.sha256(b).hexdigest()
    for name,digest in m['arquivos'].items():
        rel=Path(name)
        if rel.is_absolute() or '..' in rel.parts:raise ValueError('path não portátil')
        if sha((root/rel).read_bytes())!=digest:raise ValueError('SHA divergente: '+name)
    sys.path[:0]=[str(Path(a.qa).resolve()),str(Path(a.qa_html5).resolve()),str(Path(__file__).resolve().parent)]
    import pdfplumber
    from marcar_prototipo_ce import selecionar,representar
    from organizar_fluxo_BT_ce import fluxo
    from mapear_notas_ce import referencias
    from verificar_motores import comparar,analisar
    raw=(root/m['PDF']).read_bytes()
    if sha(raw)!='f0e84e410d6a07bf076497ba55c56b9d0685ccc3e6eb6e7029fda0598c3740aa':raise ValueError('PDF fora da edição CE fixada')
    receipts=[]
    with pdfplumber.open(io.BytesIO(raw)) as document:
        if len(document.pages)!=200:raise ValueError('fechamento da fonte não confere')
        for item in m['paginas']:
            sample=json.loads(gzip.decompress((root/item['prova']).read_bytes()));number=sample['pagina'];paper=document.pages[number-1];page=sample['camada'];chars=paper.chars
            if len(chars)!=len(page['glifos']):raise ValueError('número de glifos mudou')
            for c,g in zip(chars,page['glifos']):
                if c['text']!=g['texto'] or c['fontname']!=g['fonte']:raise ValueError('texto/fonte mudou')
                if any(abs(x-y)>1e-7 for x,y in zip(c['matrix'],g['matriz'])):raise ValueError('matriz mudou')
                if any(abs(x-y)>1e-7 for x,y in zip([c['x0'],c['top'],c['x1'],c['bottom']],g['bbox'])):raise ValueError('caixa mudou')
            actual=[]
            for index,r in enumerate(paper.rects+paper.lines):
                if r['x1']-r['x0']<4 or r['bottom']-r['top']>1.6:continue
                y=(r['top']+r['bottom'])/2;hits=[c for c in chars if c['text'].strip() and c['bottom']>c['top'] and .25<=(y-c['top'])/(c['bottom']-c['top'])<=.75 and min(r['x1'],c['x1'])>max(r['x0'],c['x0'])]
                if len(hits)<3:continue
                actual.append(dict(objeto=index,tipo=r['object_type'],caixa=[r['x0'],r['top'],r['x1'],r['bottom']],cor=r.get('non_stroking_color',r.get('stroking_color')),tag=r.get('tag'),glifos=len(hits),texto_intersectado=''.join(c['text'] for c in sorted(hits,key=lambda c:c['x0']))))
            if json.dumps(actual,ensure_ascii=False)!=json.dumps(sample['faixas'],ensure_ascii=False):raise ValueError('faixas não reproduzidas da fonte')
            zones,profile,marks=fluxo(page,sample['objetos_BT'])
            if [dict(nome=z,ids=ids) for z,ids in zones]!=page['zonas']:raise ValueError('fluxo de colunas/notas divergiu')
            if referencias(page)!=sample['notas']['referencias'] or marks!=sample['notas']['marcadores']:raise ValueError('números/referências não literais')
            selected,profiles,evidence=selecionar(page,sample['faixas'])
            if sorted(selected)!=sample['selecionados']:raise ValueError('escopo físico mudou')
            marked,record=representar(page,selected);plain,_=representar(page,set())
            prefix='<!doctype html><meta charset="utf-8"><title>CE: amostra privada '+str(number)+'</title><style>body{max-width:85ch;margin:2rem auto}pre{white-space:pre-wrap;font:16px/1.4 monospace}del{text-decoration:line-through}</style>'
            for label,markup in [('historico',marked),('baseline',plain)]:
                artifact=(root/a.manifesto).parent/('pagina-'+str(number)+'-'+label+'.html')
                if artifact.read_bytes()!=(prefix+markup+'\n').encode():raise ValueError('HTML de leitura não reproduzido')
            flags=iter((ch,g['tachado']) for g in record for ch in g['texto'] if not ch.isspace());pairs=[];rank=0;consumed=0
            for ch,deleted,ancestry in analisar(plain,'HTML5lib'):
                if ch.isspace():continue
                if any(tag=='pre' for tag,attrs in ancestry):
                    expected,struck=next(flags)
                    if ch!=expected:raise ValueError('glifo da fonte alterado na camada HTML')
                    consumed+=1
                    if struck:pairs.append((rank,ch))
                rank+=1
            if next(flags,None) is not None:raise ValueError('glifo não representado')
            motors=comparar(plain,marked,pairs,out/('motores-'+str(number)));receipts.append(dict(pagina=number,glifos=len(chars),caracteres_nao_brancos_fonte=consumed,tachados=len(pairs),motores=motors,fluxo=profile));paper.close()
    tests=unittest.TextTestRunner().run(unittest.defaultTestLoader.discover(str(Path(__file__).parent),pattern='test_*.py'))
    if not tests.wasSuccessful():raise ValueError('regressões falharam')
    result=dict(paginas=receipts,testes=tests.testsRun,arquivos_SHA=len(m['arquivos']),fonte_PDF_integral_paginas=200,limite='Amostra privada: não certifica as demais páginas/perfis. Fonte integral inalterada, glifos dessas6 páginas reproduzidos literalmente; sem Git, rede ou escrita canônica.',novas_normas=0)
    (out/'recibo.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(paginas=len(receipts),testes=tests.testsRun)),flush=True)
if __name__=='__main__':main()
