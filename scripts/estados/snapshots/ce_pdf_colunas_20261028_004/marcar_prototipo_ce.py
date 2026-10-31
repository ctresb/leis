"""Marcação física de glifos do protótipo CE; sem classificação de vigência."""
import argparse,collections,gzip,hashlib,html,itertools,json
from pathlib import Path
from gerar_prototipo_ce import nova_linha
SHA=lambda b:hashlib.sha256(b).hexdigest()

def selecionar(page,bands):
    selected=set();profiles=collections.Counter();evidence=[]
    for band in bands:
        x0,top,x1,bottom=band['caixa'];y=(top+bottom)/2;ids=[]
        for glyph in page['glifos']:
            gx0,gtop,gx1,gbottom=glyph['bbox']
            if not glyph['texto'].strip() or gbottom<=gtop:continue
            if .25<=(y-gtop)/(gbottom-gtop)<=.75 and min(x1,gx1)>max(x0,gx0):
                selected.add(glyph['id']);ids.append(glyph['id']);profiles[(str(band['cor']),glyph['fonte'],round(glyph['tamanho'],3),round(bottom-top,5))]+=1
        if len(ids)<3:raise ValueError('faixa deixou de reconciliar com três glifos')
        evidence.append(dict(banda=band,ids=ids))
    return selected,profiles,evidence

def rgb(color):
    if isinstance(color,(int,float)):color=[color]*3
    if not isinstance(color,(list,tuple)) or len(color) not in [3,4]:raise ValueError('cor fora do perfil RGB/cinza/CMYK')
    if any(not 0<=x<=1 for x in color):raise ValueError('componente de cor inválido')
    # Aproximação apenas na camada de leitura privada, nunca altera o PDF primário.
    if len(color)==4:
        c,m,y,k=color;color=[(1-c)*(1-k),(1-m)*(1-k),(1-y)*(1-k)]
    return '#'+''.join(format(round(x*255),'02x') for x in color)

def representar(page,selected):
    chunks=['<section><h2>Página PDF '+str(page['pagina'])+'</h2>'];pairs=[];bodyrank=0;sourcechar=0;record=[]
    for zone in page['zonas']:
        chunks.append('<h3>'+html.escape(zone['nome'])+'</h3><pre>');items=[];previous=None
        for index in zone['ids']:
            g=page['glifos'][index];baseline=g['matriz'][5]
            if previous is not None and nova_linha(previous[0],previous[1],baseline,g['tamanho']):items.append(('\n',(False,False,'#000000',False),None))
            style=('Bold' in g['fonte'] or 'Black' in g['fonte'],'Italic' in g['fonte'] or 'Oblique' in g['fonte'],rgb(g['cor']),index in selected)
            items.append((g['texto'],style,index));previous=(baseline,g['tamanho'])
        for style,group in itertools.groupby(items,key=lambda item:item[1]):
            values=list(group);text=''.join(v[0] for v in values);bold,italic,color,deleted=style;contrast=';background:#333333' if color=='#ffffff' else '';left='<span style="color:'+color+contrast+'">'+('<strong>' if bold else '')+('<em>' if italic else '')+('<del>' if deleted else '');right=('</del>' if deleted else '')+('</em>' if italic else '')+('</strong>' if bold else '')+'</span>';chunks.extend([left,html.escape(text),right])
            for value,flags,index in values:
                if index is None:continue
                record.append(dict(glifo=index,texto=value,tachado=flags[3],zona=zone['nome']))
                sourcechar+=len(value)
        chunks.append('</pre>')
    chunks.append('</section>')
    if sorted(v['glifo'] for v in record)!=list(range(len(page['glifos']))):raise ValueError('glifos não bijetivos')
    return ''.join(chunks),record

def main():
    p=argparse.ArgumentParser();p.add_argument('--prototipo',required=True);p.add_argument('--geometria',required=True);p.add_argument('--controle',required=True);a=p.parse_args();proto=Path(a.prototipo);geom=Path(a.geometria);out=Path(a.controle);out.mkdir(exist_ok=False,parents=True);bands={d['pagina']:d['sinais'] for d in json.loads(geom.read_text())['paginas_com_sinais']};fragments=[];baseline=[];totals=collections.Counter();profiles=collections.Counter()
    with gzip.open(proto/'glifos-e-ordem.jsonl.gz','rt',encoding='utf8') as source,gzip.open(out/'prova-marcacao-fisica.jsonl.gz','wt',encoding='utf8') as log:
        for line in source:
            page=json.loads(line);selected,prof,evidence=selecionar(page,bands.get(page['pagina'],[]));profiles.update(prof);marked,record=representar(page,selected);plain,_=representar(page,set());fragments.append(marked);baseline.append(plain);totals['glifos']+=len(page['glifos']);totals['glifos_tachados']+=len(selected);totals['codepoints_tachados_nao_brancos']+=sum(sum(not c.isspace() for c in page['glifos'][i]['texto']) for i in selected);log.write(json.dumps(dict(pagina=page['pagina'],faixas=evidence,ordem_completa=record,perfil_fluxo=page['perfil']),ensure_ascii=False)+'\n')
    for name,parts in [('prototipo-historico-marcado.html',fragments),('prototipo-baseline-sem-del.html',baseline)]:
        (out/name).write_text('\n'.join(parts)+'\n')
    receipt=dict(totais=dict(totals),perfis=[dict(cor=k[0],fonte=k[1],tamanho=k[2],altura=k[3],ocorrencias=v) for k,v in profiles.items()],novas_normas=0,alteracao_canonica=False,limite='Protótipo privado ainda não qualificado: as marcas são interseções físicas, não classificação jurídica. Exige validação visual dos perfis, leitura de fluxo/notas e quatro motores antes de propor canônico. PDF integral permanece primário; fonte/imagens/apêndices nunca cortados. A camada HTML aproxima CMYK por RGB e acrescenta fundo escuro aos glifos brancos para leitura; não é réplica de cor/layout. Paleta numérica original está no inventário de cada glifo; o PDF integral é a referência visual.')
    (out/'recibo.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt['totais']),flush=True)
if __name__=='__main__':main()
