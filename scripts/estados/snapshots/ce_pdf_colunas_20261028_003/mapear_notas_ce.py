"""Referências/notas observadas: posição física, glifos e texto literal, sem renumerar."""
import argparse,gzip,json,re,hashlib
from pathlib import Path
from organizar_fluxo_BT_ce import marcadores
PDF_SHA='f0e84e410d6a07bf076497ba55c56b9d0685ccc3e6eb6e7029fda0598c3740aa'

def referencias(page):
    glyphs=page['glifos'];allowed=set(i for zone in page['zonas'] if zone['nome'] in ['coluna_esquerda','coluna_direita'] for i in zone['ids']);found=[];skip=set()
    for i,g in enumerate(glyphs):
        if i in skip or i not in allowed or not re.fullmatch('[0-9]+',g['texto']) or g['tamanho']>=7.99:continue
        value=g['texto'];ids=[i];j=i+1
        while j<len(glyphs) and j in allowed and re.fullmatch('[0-9]+',glyphs[j]['texto']) and abs(glyphs[j]['matriz'][5]-g['matriz'][5])<.01 and abs(glyphs[j]['tamanho']-g['tamanho'])<.01:
            value+=glyphs[j]['texto'];ids.append(j);skip.add(j);j+=1
        found.append(dict(numero=int(value),impresso=value,ids=ids,tamanho=g['tamanho']))
    return found

def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',required=True);p.add_argument('--fluxo',required=True);p.add_argument('--controle',required=True);a=p.parse_args();assert hashlib.sha256(Path(a.pdf).read_bytes()).hexdigest()==PDF_SHA;out=Path(a.controle);out.mkdir(exist_ok=False,parents=True);pages=[];refs={};marks={};notes={};previous=None;continuations=[]
    with gzip.open(a.fluxo,'rt',encoding='utf8') as f:
        for line in f:
            page=json.loads(line);number=page['pagina'];glyphs=page['glifos']
            if not page['perfil']['apto_perfil']:continue
            ms=marcadores(glyphs);rs=referencias(page)
            for values,target in [(ms,marks),(rs,refs)]:
                for item in values:
                    n=item['numero']
                    if n in target:raise ValueError('referência/marcador duplicado')
                    target[n]=dict(item,pagina=number)
            noteids=next(zone['ids'] for zone in page['zonas'] if zone['nome']=='notas_largura_total');starts={m['ids'][0]:m for m in ms};fragments=[];current=None;ids=[]
            for index in noteids:
                if index in starts:
                    if ids:fragments.append((current,ids))
                    current=starts[index]['numero'];ids=[]
                ids.append(index)
            if ids:fragments.append((current,ids))
            for note,ids in fragments:
                if note is None:
                    if number!=73 or previous!=52:raise ValueError('continuação sem prova específica')
                    note=52;continuations.append(dict(numero=52,paginas=[72,73],texto_anterior_final=notes[52][-1]['texto'][-100:],texto_continuacao_inicio=''.join(glyphs[i]['texto'] for i in ids)[:180]))
                fragment=dict(pagina=number,ids=ids,texto=''.join(glyphs[i]['texto'] for i in ids));notes.setdefault(note,[]).append(fragment);previous=note
            pages.append(dict(pagina=number,referencias=rs,marcadores=ms))
    if sorted(refs)!=list(range(1,170)) or sorted(marks)!=list(range(1,170)) or sorted(notes)!=list(range(1,170)):raise ValueError('conjunto de notas incompleto')
    for n in refs:
        if refs[n]['impresso']!=marks[n]['impresso'] or refs[n]['pagina']!=marks[n]['pagina']:raise ValueError('par referência/marcador não é literal/mesma página')
    if len(continuations)!=1 or not continuations[0]['texto_anterior_final'].endswith('na forma da ') or not continuations[0]['texto_continuacao_inicio'].startswith('lei”'):raise ValueError('continuidade52 não reconciliada literalmente')
    receipt=dict(sha256_PDF=PDF_SHA,total_notas=169,referencias_e_marcadores_literais=True,documentos=pages,notas=[dict(numero=n,referencia=refs[n],marcador=marks[n],fragmentos=notes[n]) for n in sorted(notes)],continuacoes=continuations,limite='Números foram lidos dos glifos impressos e reconciliados, não inferidos ou renumerados. Fonte/bytes fixados. A ligação é editorial; texto de todas as notas permanece literal, inclusive52 multipágina. Sem inferência de vigência.')
    (out/'notas-mapeadas.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(notas=169,referencias=169,marcadores=169,continuacoes=len(continuations))),flush=True)
if __name__=='__main__':main()
