"""Sinais de visibilidade da camada CE: clip, Forms, Tr e ExtGState, sem alterar PDF."""
import argparse,collections,copy,gzip,hashlib,json
from pathlib import Path
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTChar,LTFigure
from pdfminer.pdftypes import dict_value,resolve1
from pdfminer.psparser import literal_name
from inventariar_BT_ce import flatten
PDF_SHA='f0e84e410d6a07bf076497ba55c56b9d0685ccc3e6eb6e7029fda0598c3740aa'
DEFAULT=dict(alpha_preenchimento=1,alpha_traco=1,mascara='None',blend='Normal',transferencia='Default',fonte_ExtGState=False,overprint_preenchimento=False,overprint_traco=False)

class Device(PDFPageAggregator):
    def render_string(self,textstate,seq,ncs,graphicstate):
        self.mode=int(textstate.render);return super().render_string(textstate,seq,ncs,graphicstate)
    def render_char(self,*args,**kwargs):
        advance=super().render_char(*args,**kwargs);glyph=self.cur_item._objs[-1]
        if not isinstance(glyph,LTChar):raise ValueError('não LTChar')
        glyph.visibility=dict(clips=copy.deepcopy(getattr(self,'clips',[])),em_Form=isinstance(self.cur_item,LTFigure),Tr=getattr(self,'mode',None),ExtGState=copy.deepcopy(getattr(self,'vstate',DEFAULT)))
        return advance

class Interpreter(PDFPageInterpreter):
    def init_state(self,ctm):
        super().init_state(ctm);self.clips=copy.deepcopy(getattr(self,'inherited_clips',[]));self.vstate=copy.deepcopy(getattr(self,'inherited_vstate',DEFAULT));self.extra_stack=[];self._sync()
    def _sync(self):self.device.clips=copy.deepcopy(self.clips);self.device.vstate=copy.deepcopy(self.vstate)
    def dup(self):
        child=super().dup();child.inherited_clips=copy.deepcopy(self.clips);child.inherited_vstate=copy.deepcopy(self.vstate);return child
    def do_q(self):self.extra_stack.append((copy.deepcopy(self.clips),copy.deepcopy(self.vstate)));super().do_q()
    def do_Q(self):
        super().do_Q()
        if self.extra_stack:self.clips,self.vstate=self.extra_stack.pop()
        self._sync()
    def do_W(self):self.clips.append(dict(regra='W',CTM=list(self.ctm),caminho=list(self.curpath)));self._sync();super().do_W()
    def do_W_a(self):self.clips.append(dict(regra='W*',CTM=list(self.ctm),caminho=list(self.curpath)));self._sync();super().do_W_a()
    def do_Do(self,name):super().do_Do(name);self._sync()
    def do_gs(self,name):
        states=dict_value(self.resources.get('ExtGState',{}));params=dict_value(states.get(literal_name(name),{}))
        for key,target in [('ca','alpha_preenchimento'),('CA','alpha_traco')]:
            if key in params:
                value=resolve1(params[key]);self.vstate[target]=float(value) if isinstance(value,(int,float)) else 'desconhecido'
        for key,target in [('SMask','mascara'),('BM','blend')]:
            if key in params:
                value=resolve1(params[key]);self.vstate[target]=literal_name(value) if not isinstance(value,(dict,list)) else 'estrutura_nao_simples'
        transfer=params.get('TR2',params.get('TR'))
        if transfer is not None:
            value=resolve1(transfer);self.vstate['transferencia']=literal_name(value) if not isinstance(value,(dict,list)) else 'funcao_nao_simples'
        if 'Font' in params:self.vstate['fonte_ExtGState']=True
        if 'OP' in params:
            self.vstate['overprint_traco']=bool(resolve1(params['OP']))
            if 'op' not in params:self.vstate['overprint_preenchimento']=self.vstate['overprint_traco']
        if 'op' in params:self.vstate['overprint_preenchimento']=bool(resolve1(params['op']))
        self._sync();super().do_gs(name)

def motivos(v):
    reasons=[];s=v['ExtGState']
    if v['clips']:reasons.append('clip_explicito_ativo_nao_certificado')
    if v['em_Form']:reasons.append('texto_em_Form_BBox_nao_certificado')
    if v['Tr']!=0:reasons.append('Tr_fora_do_preenchimento_normal')
    if s['alpha_preenchimento']!=1:reasons.append('alpha_fora_de_1')
    if s['mascara']!='None':reasons.append('mascara_nao_trivial')
    if s['blend'] not in ['Normal','Compatible']:reasons.append('blend_nao_trivial')
    if s['transferencia'] not in ['Default','Identity']:reasons.append('transferencia_nao_trivial')
    if s['fonte_ExtGState']:reasons.append('fonte_em_ExtGState')
    return reasons

def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',required=True);p.add_argument('--prova-glifos',required=True);p.add_argument('--controle',required=True);a=p.parse_args();pdf=Path(a.pdf);assert hashlib.sha256(pdf.read_bytes()).hexdigest()==PDF_SHA;out=Path(a.controle);out.mkdir(exist_ok=False,parents=True);manager=PDFResourceManager();device=Device(manager,laparams=None);interpreter=Interpreter(manager,device);summary=[];totals=collections.Counter()
    with pdf.open('rb') as stream,gzip.open(a.prova_glifos,'rt',encoding='utf8') as old,gzip.open(out/'sinais-visibilidade.jsonl.gz','wt',encoding='utf8') as log:
        for number,page in enumerate(PDFPage.get_pages(stream),1):
            prior=json.loads(next(old));assert prior['pagina']==number;interpreter.process_page(page);chars=list(flatten(device.get_result()));assert len(chars)==len(prior['glifos']);anomalies=[];modes=collections.Counter();form_count=0;clip_count=0
            for index,(glyph,expected) in enumerate(zip(chars,prior['glifos'])):
                if glyph.get_text()!=expected['texto'] or glyph.fontname!=expected['fonte'] or any(abs(x-y)>1e-7 for x,y in zip(glyph.matrix,expected['matriz'])):raise ValueError('camada de glifos mudou')
                vis=glyph.visibility;modes[vis['Tr']]+=1;form_count+=int(vis['em_Form']);clip_count+=int(bool(vis['clips']));reasons=motivos(vis)
                if reasons:anomalies.append(dict(id=index,texto=glyph.get_text(),visibilidade=vis,motivos=reasons))
            row=dict(pagina=number,glifos=len(chars),Tr=dict(modes),em_Form=form_count,com_clip_ativo=clip_count,total_sinais=len(anomalies),sinais=anomalies);log.write(json.dumps(row,ensure_ascii=False)+'\n');log.flush();summary.append({k:v for k,v in row.items() if k!='sinais'});totals.update(dict(glifos=len(chars),sinais=len(anomalies),em_Form=form_count,com_clip_ativo=clip_count))
    receipt=dict(sha256_PDF=PDF_SHA,paginas=len(summary),totais=dict(totals),documentos=summary,limites='Auditoria conservadora de sinais da camada textual, não prova geral de visibilidade por pixels: não resolve oclusão por pinturas posteriores, nem aparência/cor. Clip explícito, Form, Tr especial e ExtGState não triviais são retidos para contexto. Não recorta/reescreve PDF nem conclui vigência. PDF integral continua primário.')
    (out/'recibo.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(paginas=len(summary),totais=dict(totals))),flush=True)
if __name__=='__main__':main()
