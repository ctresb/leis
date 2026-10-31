"""Replay único de subconjuntos Legisla.AM por fontes/snapshots intactos e HEAD."""
import argparse,gzip,hashlib,importlib.util,json,subprocess,sys
from pathlib import Path
from legisla_am_assinatura import conferir as conferir_assinatura
from legisla_am_dispositivo import dispositivo_proprio
from representacao_html_legisla_am import extrair_campo
from pe_fidelidade_visivel import texto_visivel_html
from am_legisla_head import conferir as conferir_HEAD
SHA=lambda b:hashlib.sha256(b).hexdigest()
def main():
    if not Path('.git').exists():raise ValueError('repositório/volume ausente')
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--plano',required=True);ap.add_argument('--head',required=True);ap.add_argument('--execucao',required=True);a=ap.parse_args();plan=json.loads(Path(a.plano).read_text());head=json.loads(Path(a.head).read_text());invraw=Path(head['inventario']).read_bytes();mapraw=Path(head['destinos']).read_bytes()
    if SHA(invraw)!=head['sha256_inventario'] or SHA(mapraw)!=head['sha256_destinos']:raise ValueError('entrada HEAD divergente')
    inv=json.loads(invraw)
    if inv['HEAD']!=head['HEAD']:raise ValueError('HEAD declarado divergente')
    groups=[];allrows=[];checked=set();signature_counts={}
    for group in plan['grupos']:
        ctrl=Path(group['controle_origem']);receipt=Path(group['recibo_congelamento'])
        if SHA(ctrl.read_bytes())!=group['sha256_controle'] or SHA(receipt.read_bytes())!=group['sha256_recibo']:raise ValueError('controle/recibo congelado divergente')
        m=json.loads(ctrl.read_text());r=json.loads(receipt.read_text());code={Path(q['congelado']).name:q['congelado'] for q in r['codigo']}
        for p,s in {**r['fontes_congeladas'],**{q['congelado']:q['sha256'] for q in r['codigo']},**m['dependencias']}.items():
            if p not in checked and SHA(Path(p).read_bytes())!=s:raise ValueError('snapshot mudou: '+p)
            checked.add(p)
        selected=set(group['incluidos']);rows=[q for q in m['documentos'] if q['destino'] in selected]
        if len(rows)!=len(selected) or selected&set(group['retidos']):raise ValueError('seleção inconsistente')
        for row in rows:
            cap=row['captura'];raw=gzip.decompress(Path(cap['cache']).read_bytes())
            if SHA(raw)!=cap['sha256_fonte']:raise ValueError('fonte primária diverge')
            field,_=extrair_campo(raw.decode('utf8'));text=texto_visivel_html(field);dispositivo_proprio(text);sig=conferir_assinatura(text,row['QA']['data']);signature_counts[sig['status']]=signature_counts.get(sig['status'],0)+1
            if sig['reter']:raise ValueError('conflito de data retido indevidamente selecionado: '+row['destino'])
        m['documentos']=rows;allrows.extend(rows);groups.append((group,m,code))
    if len(allrows)!=plan['total'] or len({r['destino'] for r in allrows})!=plan['total']:raise ValueError('união não é distinta')
    conferir_HEAD(allrows,inv,json.loads(mapraw));out=Path(a.execucao);out.mkdir(exist_ok=False)
    for group,m,code in groups:
        subset=out/(group['nome']+'-controle.json');subset.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');replay=out/(group['nome']+'-replay.jsonl');subprocess.run([sys.executable,code['reexecutar_legisla_am.py'],'--manifesto',str(subset),'--saida',str(replay)],check=True);results=[json.loads(s) for s in replay.read_text().splitlines()]
        if len(results)!=len(m['documentos']) or not all(q['aceito'] for q in results):raise ValueError('replay incompleto')
    summary=dict(total=len(allrows),grupos={g['nome']:len(m['documentos']) for g,m,c in groups},HEAD=inv['HEAD'],HEAD_ausentes=len(allrows),aliases=0,assinaturas=signature_counts,dispositivo_proprio=len(allrows),retidos=plan['total_retidos'],sem_promocao=True,sha256_plano=SHA(Path(a.plano).read_bytes()),sha256_entrada_HEAD=SHA(Path(a.head).read_bytes()))
    (out/'resumo.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary))
if __name__=='__main__':main()
