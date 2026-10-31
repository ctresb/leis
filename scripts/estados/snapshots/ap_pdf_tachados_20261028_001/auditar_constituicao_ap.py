"""Auditoria PDF/Markdown AP por glifo e contexto. Só controles privados, sem promoção."""
from pathlib import Path
import argparse,array,bisect,collections,datetime,gzip,hashlib,io,json,re,string
import pdfplumber
from markdown_it import MarkdownIt
from lxml import html
SHA=lambda b:hashlib.sha256(b).hexdigest()

def projecao_markdown(body):
    parser=MarkdownIt('commonmark',{'html':True});tokens=parser.parse(body)
    kinds=collections.Counter(c.type for t in tokens for c in (t.children or []))
    if set(kinds)-{'text','strong_open','strong_close','softbreak'}:raise ValueError('marcação fora do perfil comprovado: '+str(kinds))
    removed=set()
    for m in re.finditer(r'(?m)^#{1,6} ',body):removed.update(range(m.start(),m.end()))
    for m in re.finditer(r'\*\*[^*\n]+\*\*',body):removed.update([m.start(),m.start()+1,m.end()-2,m.end()-1])
    for i,ch in enumerate(body[:-1]):
        if ch=='\\' and body[i+1] in string.punctuation:removed.add(i)
    positions=array.array('I',(i for i,ch in enumerate(body) if i not in removed and not ch.isspace()))
    compact=''.join(body[i] for i in positions)
    rendered=html.fromstring('<div>'+parser.render(body)+'</div>').text_content()
    if compact!=''.join(ch for ch in rendered if not ch.isspace()):raise ValueError('projeção por offsets diverge do CommonMark')
    anchors={};previous=0
    # O limite de linha precede a remoção de espaços; a página seguinte pode
    # começar com dígitos que não fazem parte do número do rodapé.
    for m in re.finditer(r'(?m)CONSTITUIÇÃO\s+DO\s+ESTADO\s+DO\s+AMAPÁ\s+CONSOLIDADA\s+Página[ \t]+(\d+)[ \t]*$',body,re.I):
        number=int(m[1])
        if number in anchors:raise ValueError('rodapé de página ambíguo')
        start=bisect.bisect_left(positions,m.start());end=bisect.bisect_left(positions,m.end())
        anchors[number]=(previous,start);previous=end
    byte_offsets=array.array('I',[0]);total=0
    for ch in body:total+=len(ch.encode());byte_offsets.append(total)
    return compact,positions,byte_offsets,anchors,dict(kinds)

def intersecoes(rect,chars):
    if not rect.get('fill') or not 0.1<=rect['height']<=1.5 or rect['width']<2:return []
    y=(rect['top']+rect['bottom'])/2;out=[]
    for i,c in enumerate(chars):
        height=c['bottom']-c['top']
        if height<=0:continue
        relative=(y-c['top'])/height
        if 0.25<=relative<=0.75 and rect['x0']-0.05<=(c['x0']+c['x1'])/2<=rect['x1']+0.05:
            out.append((i,relative))
    return out

def black(value):return value in [0,0.0,(0,),(0,0,0),(0,0,0,1)]

def linhas(chars):
    rows=[]
    for i,c in sorted(enumerate(chars),key=lambda pair:(-pair[1]['matrix'][5],pair[1]['x0'],pair[0])):
        baseline=c['matrix'][5]
        if not rows or abs(rows[-1][0]-baseline)>0.8:rows.append((baseline,[]))
        rows[-1][1].append((i,c))
    return [(y,sorted(row,key=lambda pair:(pair[1]['x0'],pair[0]))) for y,row in rows]

def linhas_por_intersecao(chars):
    groups=[]
    for i,c in sorted(enumerate(chars),key=lambda pair:(pair[1]['top'],pair[1]['x0'],pair[0])):
        target=None
        for group in groups[-3:]:
            ref=group['ref'];overlap=max(0,min(c['bottom'],ref['bottom'])-max(c['top'],ref['top']))
            if overlap>=0.6*min(c['bottom']-c['top'],ref['bottom']-ref['top']):target=group;break
        if target is None:target=dict(ref=c,chars=[]);groups.append(target)
        target['chars'].append((i,c))
        if c['size']>target['ref']['size']:target['ref']=c
    return [(g['ref']['matrix'][5],sorted(g['chars'],key=lambda pair:(pair[1]['x0'],pair[0]))) for g in groups]

def contexto_literal(rows,baseline,compact,bounds,ids=None):
    if ids:center=max(range(len(rows)),key=lambda n:sum(i in ids for i,c in rows[n][1]))
    else:center=min(range(len(rows)),key=lambda n:abs(rows[n][0]-baseline))
    left,right=bounds
    for distance in range(9):
        winners=[]
        for before in range(5):
            after=distance-before
            if not 0<=after<=4:continue
            selected=rows[max(0,center-before):min(len(rows),center+after+1)];mapping=[]
            for _,row in selected:
                for i,c in row:
                    for sub,ch in enumerate(c['text']):
                        if not ch.isspace():mapping.append((i,sub,ch))
            text=''.join(ch for i,sub,ch in mapping);found=[];offset=compact.find(text,left,right)
            while offset>=0:
                found.append(offset);offset=compact.find(text,offset+1,right)
            if len(found)==1:
                signature=tuple((i,sub,found[0]+n) for n,(i,sub,ch) in enumerate(mapping) if not ids or i in ids)
                winners.append((mapping,found,dict(antes=before,depois=after),signature))
        if winners:
            if len({w[3] for w in winners})!=1:return mapping,[],dict(ambiguidade_contextual=True)
            return winners[0][:3]
    return mapping,found,dict(antes=before,depois=after)

def auditar(cache,preimagem,output,paginas=None):
    output.mkdir(parents=True,exist_ok=False);packed=cache.read_bytes();raw=gzip.decompress(packed)
    if not raw.startswith(b'%PDF'):raise ValueError('cache não é PDF')
    md=preimagem.read_bytes();header,bodybytes=md.split(b'\n---\n',1);body=bodybytes.decode('utf-8')
    compact,positions,byte_offsets,anchors,kinds=projecao_markdown(body)
    results=[];totals=collections.Counter()
    with pdfplumber.open(io.BytesIO(raw)) as document, gzip.open(output/'prova-caracteres.jsonl.gz','xt',encoding='utf-8') as log:
        for page_index,page in enumerate(document.pages,1):
            if paginas and page_index not in paginas:continue
            chars=page.chars
            rows=linhas(chars)
            physical_rows=None
            char_data=[dict(id=i,texto=c['text'],caixa=[c['x0'],c['top'],c['x1'],c['bottom']],fonte=c['fontname'],tamanho=c['size'],matriz=list(c['matrix']),mcid=c.get('mcid'),tag=c.get('tag')) for i,c in enumerate(chars)]
            row=dict(pagina=page_index,MediaBox=list(page.mediabox),CropBox=list(page.cropbox),rotacao=page.rotation,caracteres=len(chars),sha256_caracteres=SHA(json.dumps(char_data,ensure_ascii=False,sort_keys=True).encode()),retangulos_intersectantes=[])
            for rect_index,rect in enumerate(page.rects):
                hits=intersecoes(rect,chars)
                if not hits:continue
                chosen=[chars[i] for i,_ in hits];baseline=sorted(c['matrix'][5] for c in chosen)[len(chosen)//2]
                line=sorted([(i,c) for i,c in enumerate(chars) if abs(c['matrix'][5]-baseline)<=0.8],key=lambda pair:(pair[1]['x0'],pair[0]))
                found=[];glyph_map=[];margin=0;mode='baseline_matriz'
                if page_index in anchors:
                    glyph_map,found,margin=contexto_literal(rows,baseline,compact,anchors[page_index],{i for i,f in hits})
                    if len(found)!=1:
                        if physical_rows is None:physical_rows=linhas_por_intersecao(chars)
                        glyph_map,found,margin=contexto_literal(physical_rows,baseline,compact,anchors[page_index],{i for i,f in hits});mode='intersecao_vertical_com_sobrescrito'
                known=black(rect.get('non_stroking_color')) and rect.get('tag')=='Span' and page.rotation==0
                item=dict(id_retangulo=rect_index,caixa=[rect['x0'],rect['top'],rect['x1'],rect['bottom']],cor=rect.get('non_stroking_color'),mcid=rect.get('mcid'),tag=rect.get('tag'),texto_linha=''.join(c['text'] for _,c in line),perfil_preto_Span=known,ocorrencias_linha_MD=len(found),margem_contexto_linhas=margin,modo_contexto=mode,glifos=[])
                by_index=collections.defaultdict(list)
                for n,(i,sub,ch) in enumerate(glyph_map):by_index[i].append((n,sub,ch))
                for i,relative in hits:
                    c=chars[i];width=c['x1']-c['x0'];coverage=max(0,min(rect['x1'],c['x1'])-max(rect['x0'],c['x0']))/width if width>0 else 0
                    proof=dict(char_data[i],fracao_vertical_rect=relative,fracao_horizontal_glifo=coverage)
                    if len(found)==1 and i in by_index:
                        codepoints=[]
                        for n,sub,ch in by_index[i]:
                            at=found[0]+n;raw_at=positions[at]
                            if compact[at]!=ch or body[raw_at]!=ch:raise ValueError('caractere PDF/MD divergiu')
                            codepoints.append(dict(indice_no_glifo=sub,caractere=ch,MD_corpo_offset_unicode=raw_at,MD_corpo_offset_bytes=byte_offsets[raw_at]))
                        raw_at=codepoints[0]['MD_corpo_offset_unicode']
                        proof.update(MD_caracteres=codepoints,MD_contexto=body[max(0,raw_at-80):raw_at+100],comparacao_literal=True)
                    item['glifos'].append(proof)
                item['todos_glifos_nao_brancos_mapeados']=all('MD_caracteres' in g for g in item['glifos'] if not g['texto'].isspace())
                totals['retangulos_intersectantes']+=1
                if known:totals['perfil_preto_Span']+=1
                if not item['todos_glifos_nao_brancos_mapeados']:totals['intersecoes_com_contexto_nao_resolvido']+=1
                row['retangulos_intersectantes'].append(item)
            log.write(json.dumps(row,ensure_ascii=False)+'\n');log.flush();results.append(dict(pagina=page_index,caracteres=len(chars),retangulos_intersectantes=len(row['retangulos_intersectantes'])));page.close()
    receipt=dict(preparado_em=datetime.datetime.now().astimezone().isoformat(),cache=str(cache),sha256_cache=SHA(packed),sha256_pdf=SHA(raw),preimagem=str(preimagem),sha256_preimagem=SHA(md),sha256_corpo=SHA(bodybytes),projecao_CommonMark_exata=True,tipos_tokens=kinds,rodapes_unicos=len(anchors),paginas=results,totais=dict(totals),limite='Interseções geométricas são candidatos de marcação, não classificação jurídica automática. Somente páginas efetivamente vistas podem confirmar o aspecto visual. Retângulos coloridos/sem Span, contexto ambíguo ou glifo não mapeado permanecem para revisão. Nenhum conteúdo foi apagado ou marcado no canônico; apêndices permanecem integrais.',novas_normas=0,sem_rede=True,sem_escrita_canonica=True)
    (output/'recibo.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');return receipt

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--cache',required=True);p.add_argument('--preimagem',required=True);p.add_argument('--controle',required=True);p.add_argument('--paginas');a=p.parse_args();pages={int(x) for x in a.paginas.split(',')} if a.paginas else None
    r=auditar(Path(a.cache),Path(a.preimagem),Path(a.controle),pages);print(json.dumps(dict(paginas=len(r['paginas']),totais=r['totais'])))
if __name__=='__main__':main()
