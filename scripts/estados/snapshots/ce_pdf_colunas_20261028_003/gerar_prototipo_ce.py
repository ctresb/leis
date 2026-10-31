"""Protótipo privado CE específico: ordenar glifos espaciais, sem promoção/recorte do PDF."""
import argparse,collections,gzip,hashlib,html,io,json
from pathlib import Path
import pdfplumber
PDF_SHA='f0e84e410d6a07bf076497ba55c56b9d0685ccc3e6eb6e7029fda0598c3740aa'
SHA=lambda b:hashlib.sha256(b).hexdigest()

def organizar(chars,page_number):
    # Apenas o articulado/ADCT de duas colunas tem perfil espacial em estudo.
    if page_number not in set(range(26,141))|set(range(142,153)):
        return [('sem_perfil',list(range(len(chars))))],dict(apto_perfil=False,motivo='Preliminares/apêndices preservados em inventário e PDF; fluxo ainda sem perfil.')
    if any(abs(c['matrix'][1])>.00001 or abs(c['matrix'][2])>.00001 for c in chars):
        raise ValueError('texto rotacionado/oblíquo exige perfil próprio')
    middle=[c for c in chars if c['text'].strip() and 291<c['x0']<305 and c['top']<735]
    first=min((c['top'] for c in middle),default=None)
    if first is not None and first<400:raise ValueError('texto largo acima da zona de notas: perfil não provado')
    cutoff=first-3 if first is not None else None
    groups=collections.defaultdict(list)
    for index,c in enumerate(chars):
        if c['top']>=735:zone='rodape_editorial'
        elif cutoff is not None and c['top']>=cutoff:zone='notas_largura_total'
        elif c['x0']<297.638:zone='coluna_esquerda'
        else:zone='coluna_direita'
        groups[zone].append(index)
    zones=[]
    for zone in ['coluna_esquerda','coluna_direita','notas_largura_total','rodape_editorial']:
        ids=groups.get(zone,[])
        # Mantém a ordem original de pintura dentro de cada quadro; não junta palavras.
        zones.append((zone,ids))
    order=[i for zone,ids in zones for i in ids]
    if len(order)!=len(chars) or set(order)!=set(range(len(chars))):raise ValueError('glifo perdido/repetido')
    return zones,dict(apto_perfil=True,limite_notas_proposto=cutoff,prova='Ordenação por quadros geométricos proposta; limite de notas ainda exige inspeção dos perfis/páginas. Não certificado para publicação.')

def nova_linha(old_baseline,old_size,new_baseline,new_size):
    return abs(new_baseline-old_baseline)>.65*max(old_size,new_size)

def linhas(chars,ids):
    output=[];previous=None
    for index in ids:
        c=chars[index];baseline=c['matrix'][5]
        if previous is not None and nova_linha(previous[0],previous[1],baseline,c.get('size',8)):output.append('\n')
        output.append(c['text']);previous=(baseline,c.get('size',8))
    return ''.join(output)

def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',required=True);p.add_argument('--controle',required=True);a=p.parse_args();raw=Path(a.pdf).read_bytes();assert SHA(raw)==PDF_SHA;out=Path(a.controle);out.mkdir(exist_ok=False,parents=True);summary=[];count=0;htmlparts=['<!doctype html><meta charset="utf-8"><title>CE: protótipo espacial privado, não certificado</title>']
    with pdfplumber.open(io.BytesIO(raw)) as document,gzip.open(out/'glifos-e-ordem.jsonl.gz','wt',encoding='utf8') as log:
        assert len(document.pages)==200
        for number,page in enumerate(document.pages,1):
            chars=page.chars;count+=len(chars)
            if abs(page.width-595.276)>.01 or abs(page.height-793.701)>.01 or page.rotation:raise ValueError('página fora do formato CE fixado')
            try:zones,profile=organizar(chars,number)
            except ValueError as e:zones=[('perfil_retido',list(range(len(chars))))];profile=dict(apto_perfil=False,motivo=str(e))
            glyphs=[dict(id=i,texto=c['text'],bbox=[c['x0'],c['top'],c['x1'],c['bottom']],matriz=list(c['matrix']),fonte=c['fontname'],tamanho=c['size'],cor=c.get('non_stroking_color')) for i,c in enumerate(chars)]
            rec=dict(pagina=number,glifos=glyphs,zonas=[dict(nome=zone,ids=ids) for zone,ids in zones],perfil=profile,imagens=len(page.images));log.write(json.dumps(rec,ensure_ascii=False)+'\n');log.flush()
            htmlparts.append('<section><h2>Página PDF '+str(number)+'</h2>')
            for zone,ids in zones:htmlparts.append('<h3>'+zone+'</h3><pre>'+html.escape(linhas(chars,ids))+'</pre>')
            htmlparts.append('</section>');summary.append(dict(pagina=number,glifos=len(chars),perfil=profile,imagens=len(page.images)));page.close()
    (out/'prototipo-nao-publicavel.html').write_text('\n'.join(htmlparts)+'\n');(out/'recibo.json').write_text(json.dumps(dict(sha256_PDF=PDF_SHA,paginas=200,glifos=count,documentos=summary,novas_normas=0,alteracao_canonica=False,limites='Protótipo diagnóstico sem tachados/estilos ainda. Não publicável: requer prova de fluxo/limites de notas, preservação por caractere e marcações físicas em perfil CE específico. PDF integral preservado fora do protótipo; fontes e anexos não recortados.'),ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(paginas=200,glifos=count,perfis_espaciais_propostos=sum(d['perfil']['apto_perfil'] for d in summary))),flush=True)
if __name__=='__main__':main()
