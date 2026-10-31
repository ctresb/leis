"""Sucessor CE: notas por marcadores físicos e objetos BT, sem cortes de artigos."""
import argparse,collections,gzip,json,re
from pathlib import Path
from gerar_prototipo_ce import organizar

def marcadores(glyphs):
    found=[]
    for index,g in enumerate(glyphs):
        if not (re.fullmatch('[0-9]+',g['texto']) and abs(g['bbox'][0]-56.6929)<.03 and 400<g['bbox'][1]<735 and abs(g['tamanho']-8)<.002 and 'AsapCondensed-Light' in g['fonte']):continue
        value=g['texto'];ids=[index];j=index+1
        while j<len(glyphs) and re.fullmatch('[0-9]+',glyphs[j]['texto']) and abs(glyphs[j]['bbox'][1]-g['bbox'][1])<.01:
            value+=glyphs[j]['texto'];ids.append(j);j+=1
        found.append(dict(numero=int(value),impresso=value,ids=ids,top=g['bbox'][1]))
    return found

def fluxo(page,objects):
    glyphs=page['glifos'];raw=[dict(text=g['texto'],x0=g['bbox'][0],top=g['bbox'][1],matrix=g['matriz']) for g in glyphs];oldzones,oldprofile=organizar(raw,page['pagina'])
    if not oldprofile['apto_perfil']:return oldzones,oldprofile,[]
    marks=marcadores(glyphs);wide=[]
    for obj in objects:
        x0,top,x1,bottom=obj['bbox']
        if 400<top<735 and x0<100 and x1>305 and all(glyphs[i]['tamanho']<=8.01 for i in obj['ids']):wide.append(obj)
    candidates=[m['top'] for m in marks]+[obj['bbox'][1] for obj in wide];cut=min(candidates)-3 if candidates else None
    if cut is not None and not marks and page['pagina']!=73:raise ValueError('continuação de nota não revisada')
    groups=collections.defaultdict(list)
    for g in glyphs:
        if g['bbox'][1]>=735:zone='rodape_editorial'
        elif cut is not None and g['bbox'][1]>=cut:zone='notas_largura_total'
        elif g['bbox'][0]<297.638:zone='coluna_esquerda'
        else:zone='coluna_direita'
        groups[zone].append(g['id'])
    noteids=groups.get('notas_largura_total',[])
    if noteids:
        if noteids!=list(range(min(noteids),max(noteids)+1)):raise ValueError('notas não formam bloco contínuo na pintura PDF')
        if any(glyphs[i]['tamanho']>8.01 for i in noteids):raise ValueError('zona de notas absorveu tipografia fora do perfil')
        if not all(set(m['ids'])<=set(noteids) for m in marks):raise ValueError('marcador fora da própria nota')
        if not all(set(obj['ids'])<=set(noteids) for obj in wide):raise ValueError('objeto BT de nota cortado')
    order=['coluna_esquerda','coluna_direita','notas_largura_total','rodape_editorial'];zones=[(name,groups.get(name,[])) for name in order]
    if sorted(i for zone,ids in zones for i in ids)!=list(range(len(glyphs))):raise ValueError('glifo perdido/repetido')
    profile=dict(apto_perfil=True,limite_notas_proposto=cut,limite_anterior_gutter=oldprofile['limite_notas_proposto'],origem_limite='Marcadores físicos ASCII observados e objetos BT largos com tipografia8pt; bloco contínuo de pintura, não regex de artigo.',notas_por_ids_continuos=bool(noteids),objetos_BT_largos=[o['BT'] for o in wide],continuacao_52_paginas_72_73=page['pagina']==73,limite='Perfil espacial ainda sujeito a revisão visual e reconciliação completa antes de canônico.')
    return zones,profile,marks

def main():
    p=argparse.ArgumentParser();p.add_argument('--prova-glifos',required=True);p.add_argument('--objetos-BT',required=True);p.add_argument('--controle',required=True);a=p.parse_args();out=Path(a.controle);out.mkdir(exist_ok=False,parents=True);summary=[];allmarks=[]
    with gzip.open(a.prova_glifos,'rt',encoding='utf8') as source,gzip.open(a.objetos_BT,'rt',encoding='utf8') as bt,gzip.open(out/'glifos-e-ordem.jsonl.gz','wt',encoding='utf8') as target:
        for line in source:
            page=json.loads(line);objects=json.loads(next(bt));assert page['pagina']==objects['pagina'];zones,profile,marks=fluxo(page,objects['objetos_BT']);allmarks.extend(dict(m,pagina=page['pagina']) for m in marks);page['zonas']=[dict(nome=zone,ids=ids) for zone,ids in zones];page['perfil']=profile;page['marcadores_notas']=marks;target.write(json.dumps(page,ensure_ascii=False)+'\n');summary.append(dict(pagina=page['pagina'],perfil=profile,marcadores=marks))
    numbers=[m['numero'] for m in allmarks]
    if numbers!=list(range(1,170)):raise ValueError('notas observadas não reconciliam sequência literal1–169 fixada da edição')
    (out/'recibo.json').write_text(json.dumps(dict(paginas=len(summary),glifos_inalterados=True,sequencia_literal_notas=numbers,documentos=summary,novas_normas=0,alteracao_canonica=False,limite='Sucessor espacial privado; todos os glifos permanecem. Fonte fixada por recibos anteriores. Não infere vigência e não certifica layout/cor/elementos gráficos, preservados pelo PDF integral.'),ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(paginas=len(summary),notas=len(numbers),blocos_notas=sum(d['perfil'].get('notas_por_ids_continuos',False) for d in summary))),flush=True)
if __name__=='__main__':main()
