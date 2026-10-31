"""Objetos BT da fonte CE, reconciliados literalmente com todos os glifos anteriores."""
import argparse,collections,gzip,hashlib,json,re
from pathlib import Path
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTChar
PDF_SHA='f0e84e410d6a07bf076497ba55c56b9d0685ccc3e6eb6e7029fda0598c3740aa'
class Device(PDFPageAggregator):
    def render_char(self,*args,**kwargs):
        advance=super().render_char(*args,**kwargs);glyph=self.cur_item._objs[-1]
        if not isinstance(glyph,LTChar):raise ValueError('objeto inesperado após render_char')
        glyph.btid=self.btid;return advance
class Interpreter(PDFPageInterpreter):
    def do_BT(self):self.device.btid+=1;super().do_BT()
def flatten(node):
    if isinstance(node,LTChar):yield node
    elif hasattr(node,'_objs'):
        for child in node._objs:yield from flatten(child)

def reconhecer_marcador(group):
    text=''.join(g['texto'] for g in group)
    return bool(re.fullmatch(r'\d+',text) and abs(group[0]['bbox'][0]-56.6929)<.03 and 400<group[0]['bbox'][1]<735 and all(abs(g['tamanho']-8)<.002 and 'AsapCondensed-Light' in g['fonte'] for g in group))

def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',required=True);p.add_argument('--prova-glifos',required=True);p.add_argument('--controle',required=True);a=p.parse_args();pdf=Path(a.pdf);assert hashlib.sha256(pdf.read_bytes()).hexdigest()==PDF_SHA;out=Path(a.controle);out.mkdir(exist_ok=False,parents=True);manager=PDFResourceManager();device=Device(manager,laparams=None);device.btid=0;interpreter=Interpreter(manager,device);summary=[]
    with pdf.open('rb') as stream,gzip.open(a.prova_glifos,'rt',encoding='utf8') as old,gzip.open(out/'objetos-BT.jsonl.gz','wt',encoding='utf8') as log:
        for number,page in enumerate(PDFPage.get_pages(stream),1):
            prior=json.loads(next(old));assert prior['pagina']==number;device.btid=0;interpreter.process_page(page);chars=list(flatten(device.get_result()));assert len(chars)==len(prior['glifos']);groups=collections.defaultdict(list)
            for index,(glyph,expected) in enumerate(zip(chars,prior['glifos'])):
                if glyph.get_text()!=expected['texto'] or glyph.fontname!=expected['fonte']:raise ValueError('texto/fonte não reconciliados')
                if any(abs(float(x)-float(y))>1e-7 for x,y in zip(glyph.matrix,expected['matriz'])):raise ValueError('matriz mudou')
                if any(abs(float(x)-float(y))>1e-7 for x,y in zip([glyph.x0,793.701-glyph.y1,glyph.x1,793.701-glyph.y0],expected['bbox'])):raise ValueError('caixa mudou')
                groups[glyph.btid].append(dict(expected,id=index))
            objects=[];markers=[]
            for btid,glyphs in groups.items():
                bbox=[min(g['bbox'][0] for g in glyphs),min(g['bbox'][1] for g in glyphs),max(g['bbox'][2] for g in glyphs),max(g['bbox'][3] for g in glyphs)];record=dict(BT=btid,ids=[g['id'] for g in glyphs],bbox=bbox,texto=''.join(g['texto'] for g in glyphs),marcador_numerico_perfil_CE=reconhecer_marcador(glyphs));objects.append(record)
                if record['marcador_numerico_perfil_CE']:markers.append(dict(BT=btid,numero=record['texto'],bbox=bbox,ids=record['ids']))
            log.write(json.dumps(dict(pagina=number,objetos_BT=objects,marcadores_notas_propostos=markers),ensure_ascii=False)+'\n');log.flush();summary.append(dict(pagina=number,glifos=len(chars),BTs=len(objects),marcadores=markers))
    receipt=dict(sha256_PDF=PDF_SHA,paginas=len(summary),glifos=sum(p['glifos'] for p in summary),texto_fontes_matrizes_caixas_reconciliados=True,documentos=summary,limite='Marcadores são candidatos documentais por objetos BT/posição/tipografia, não cortes automáticos. Exige contexto, referências e integridade do bloco de notas antes de usar como limite de fluxo. Nenhuma alteração canônica ou inferência de vigência.')
    (out/'recibo.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(paginas=len(summary),glifos=receipt['glifos'],marcadores=sum(len(p['marcadores']) for p in summary))),flush=True)
if __name__=='__main__':main()
