"""Candidatos privados Legisla.AM; não promove MD nem faz rede/Git."""
import argparse,datetime,gzip,hashlib,json,re
from pathlib import Path
from zoneinfo import ZoneInfo
from am_legisla import chaves_disco
from auditar_legisla_am_cache import auditar
from legisla_am_css import ContextoCSS
from representacao_html_legisla_am import extrair_campo,representar,MODO
SHA=lambda b:hashlib.sha256(b).hexdigest()
CSS_MANIFESTS=['scripts/estados/manifestos/legisla-am-publico-20261027-001/am-legisla-css-captura-20261021-001.json', 'scripts/estados/manifestos/legisla-am-publico-20261027-001/am-legisla-css-captura-20261021-002.json', 'scripts/estados/manifestos/legisla-am-publico-20261027-001/am-legisla-css-captura-20261021-003.json']

def contexto():
    receipts=[]
    for p in CSS_MANIFESTS:
        for r in json.loads(Path(p).read_text())['capturas']:
            if '.css' in r['url']:receipts.append(r)
    return ContextoCSS(receipts)

def revisar(qa,review,sha):
    if not review:return qa['retencoes'],None
    if review['sha256_fonte']!=sha:raise ValueError('revisão contextual pertence a outra fonte')
    if review['resultado']!='contexto_completo_com_citacao_ou_tabela_propria':return qa['retencoes'],review
    old=set(review['retencoes_automaticas_revisadas']);current=set(qa['retencoes'])
    removed=old-current;allowed={'outra epígrafe completa exige revisão de granularidade/citação'} if qa.get('citacoes',{}).get('todas_contextualizadas') else set()
    if current-old or removed-allowed:raise ValueError('retenções contextuais mudaram; revisão anterior insuficiente')
    return [],review

def compor(r,qa,field,review=None):
    item=r['item'];body=representar(field,modo=MODO);meta=dict(titulo=item['titulo'],uf='AM',tipo=qa['tipo'],numero=qa['numero'],data=qa['data'],ano=qa['data'][:4],ementa='',revogada=None,versao_texto='Campo matéria integral fornecido pelo Legisla.AM; edição histórica/compilação não declarada',representacao_corpo=MODO,fonte=item['url'],id_legisla=item['id_legisla'],ano_URL=item.get('ano_URL',item['ano']),titulo_indice=item['titulo'],numero_indice_coletor=item.get('numero'),capturado_em=r['capturado_em'],baixado_em=r['capturado_em'][:10],sha256_fonte=r['sha256_fonte'],sha256_campo=qa['sha256_campo'],sha256_texto=SHA(body.encode()))
    if review:meta['observacao_contextual_fonte']=review['fundamento_literal_contextual']
    raw=('---\n'+''.join(k+': '+json.dumps(v,ensure_ascii=False)+'\n' for k,v in meta.items())+'---\n\n# '+meta['titulo']+'\n\n'+body+'\n').encode();return raw,meta

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--log',required=True);ap.add_argument('--lote',required=True);ap.add_argument('--revisoes',required=True);ap.add_argument('--baseline');a=ap.parse_args();log=Path(a.log).read_bytes();log=gzip.decompress(log) if a.log.endswith('.gz') else log;assert log.endswith(b'\n');rows=[json.loads(s) for s in log.splitlines()];keys=chaves_disco();ctx=contexto();reviews={r['id_legisla']:r for r in json.loads(Path(a.revisoes).read_text())['documentos']};base=Path('estaduais/AM/_fonte/auditorias')/a.lote;base.mkdir(exist_ok=False);docs=[];holds=[];bykey={};crosskeys={}
    if a.baseline:
        for prior in json.loads(Path(a.baseline).read_text())['documentos']:
            if '/leis-promulgadas/' not in prior['path']:continue
            meta=prior['meta'];num=re.sub(r'[.\s]','',str(meta.get('numero',''))).upper().lstrip('0');year=str(meta.get('data',''))[:4]
            crosskeys.setdefault((num,year),[]).append(prior['path'])
    for r in rows:
        if r['status'] not in ('capturado','cache_recuperado_sem_receipt_http'):continue
        ident=r['item']['id_legisla'];record=dict(id_legisla=ident,captura=r)
        try:
            packed=Path(r['cache']).read_bytes();qa=auditar(r,packed,contexto_css=ctx);key=(qa['numero'],qa['data'][:4]);review=reviews.get(ident);remaining,contextual=revisar(qa,review,r['sha256_fonte'])
            if key in keys:holds.append(dict(**record,motivo='alias de identidade já presente no disco',paths=keys[key],QA=qa));continue
            if key in crosskeys:holds.append(dict(**record,motivo='colisão com série Lei Promulgada do baseline; não fundir/reclassificar automaticamente',paths=crosskeys[key],QA=qa));continue
            if remaining:holds.append(dict(**record,motivo='QA/contexto pendente',retencoes=remaining,QA=qa));continue
            if contextual and contextual['resultado']!='contexto_completo_com_citacao_ou_tabela_propria':holds.append(dict(**record,motivo=contextual['resultado'],revisao=contextual,QA=qa));continue
            if key in bykey:
                prev=bykey[key]
                if prev['QA']['sha256_campo']!=qa['sha256_campo']:
                    prev['reter_colisao_identidade']=True;holds.append(dict(id_legisla=prev['id_legisla'],captura=prev['captura'],motivo='primeiro campo retido por colisão posterior de identidade',candidato_privado_preservado=prev['candidato']));holds.append(dict(**record,motivo='mesma identidade com campos divergentes',outro_ID=prev['id_legisla'],QA=qa))
                else:holds.append(dict(**record,motivo='mesma identidade e campo literal repetido',outro_ID=prev['id_legisla'],QA=qa))
                continue
            source=gzip.decompress(packed).decode('utf8');field,_=extrair_campo(source);raw,meta=compor(r,qa,field,contextual);dest=f"estaduais/AM/leis-ordinarias/{meta['ano']}/lei-{meta['numero']}-{meta['ano']}-legisla{ident}.md";p=base/'candidatos'/(dest+'.gz');p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(gzip.compress(raw));record.update(destino=dest,candidato=str(p),sha256_candidato=SHA(raw),sha256_candidato_gzip=SHA(p.read_bytes()),QA=qa,revisao_contextual=contextual,sem_MD_canonico=True);docs.append(record);bykey[key]=record
        except Exception as e:holds.append(dict(**record,motivo=type(e).__name__+': '+str(e)))
    docs=[r for r in docs if not r.get('reter_colisao_identidade')];manifest=Path('scripts/estados/manifestos')/(a.lote+'.json');manifest.write_text(json.dumps(dict(preparado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat(),log_snapshot=a.log,sha256_log=SHA(log),linhas_log=len(rows),sem_promocao=True,sem_Git=True,documentos=docs,retidos=holds,dependencias={p:SHA(Path(p).read_bytes()) for p in [*CSS_MANIFESTS,a.revisoes]+([a.baseline] if a.baseline else [])}),ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(candidatos=len(docs),retidos=len(holds),manifesto=str(manifest))))
if __name__=='__main__':main()
