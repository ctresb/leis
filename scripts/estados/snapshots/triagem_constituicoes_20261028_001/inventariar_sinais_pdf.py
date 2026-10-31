"""Alertas geométricos contextuais em fontes preservadas; nunca aplica tachado ou máscara."""
import argparse,gzip,hashlib,io,json,datetime
from pathlib import Path
import pdfplumber
def main():
    p=argparse.ArgumentParser();p.add_argument('--inventario',required=True);p.add_argument('--controle',required=True);a=p.parse_args();m=json.loads(Path(a.inventario).read_text());out=Path(a.controle);out.mkdir(exist_ok=False,parents=True)
    for doc in m['documentos']:
        if doc.get('formato')!='PDF' or Path(doc['path']).parts[1]=='AP':continue
        raw=gzip.decompress(Path(doc['cache']).read_bytes());assert hashlib.sha256(raw).hexdigest()==doc['sha256_fonte'];pages=[];total=0
        with pdfplumber.open(io.BytesIO(raw)) as pdf:
            n=len(pdf.pages)
            for no,page in enumerate(pdf.pages,1):
                chars=page.chars;signals=[]
                for index,r in enumerate(page.rects+page.lines):
                    width=r['x1']-r['x0'];height=r['bottom']-r['top']
                    if width<4 or height>1.6:continue
                    y=(r['top']+r['bottom'])/2;hits=[c for c in chars if c['text'].strip() and c['bottom']>c['top'] and .25<=(y-c['top'])/(c['bottom']-c['top'])<=.75 and min(r['x1'],c['x1'])>max(r['x0'],c['x0'])]
                    if len(hits)<3:continue
                    text=''.join(c['text'] for c in sorted(hits,key=lambda c:c['x0']));signals.append(dict(objeto=index,tipo=r['object_type'],caixa=[r['x0'],r['top'],r['x1'],r['bottom']],cor=r.get('non_stroking_color',r.get('stroking_color')),tag=r.get('tag'),glifos=len(hits),texto_intersectado=text))
                if signals:pages.append(dict(pagina=no,rotacao=page.rotation,sinais=signals));total+=len(signals)
                page.close()
        result=dict(path=doc['path'],OID=doc['OID'],sha256_MD=doc['sha256_MD'],fonte=doc['cache'],sha256_fonte=doc['sha256_fonte'],paginas=n,total_sinais=total,paginas_com_sinais=pages,limite='Apenas alerta geométrico: retas/caixas podem ser tabelas, decoração ou sublinhado. Não classifica risco, não prova perda no MD nem revogação. Exige inspeção visual e cotejo individual por caractere antes de propor alteração. Não reutilizar o perfil AP automaticamente.')
        target=out/(Path(doc['path']).parts[1]+'.json');target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(UF=Path(doc['path']).parts[1],paginas=n,sinais=total)),flush=True)
if __name__=='__main__':main()
