"""Comparação por caractere, posição e ancestralidade em CommonMark/GFM e HTML5."""
from pathlib import Path
import gzip,hashlib,json,subprocess
import html5lib
from lxml import html
from markdown_it import MarkdownIt
SHA=lambda b:hashlib.sha256(b).hexdigest()
MARKED=Path('/Users/joaodavisn/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/marked/lib/marked.esm.js')
MARKED_SHA='0b4487359ce6b85108708e7a532e1242a27f4718241e7b2de109ac6cd307d2dc'
NODE='/opt/homebrew/bin/node'
STRUCT={'h1','h2','h3','h4','h5','h6','p','strong','b','em','i','a','ul','ol','li','blockquote','pre','code'}

def percorrer(node,ancestry=(),deleted=False):
    if not isinstance(node.tag,str):return
    tag=node.tag.split('}')[-1].lower();deleted=deleted or tag in {'del','s','strike'}
    if tag in STRUCT:ancestry=ancestry+((tag,tuple((k,node.attrib[k]) for k in ['href','title','start','value'] if k in node.attrib)),)
    if node.text:
        for ch in node.text:yield ch,deleted,ancestry
    for child in node:
        yield from percorrer(child,ancestry,deleted)
        if child.tail:
            for ch in child.tail:yield ch,deleted,ancestry

def analisar(source,parser):
    root=html.fromstring('<div>'+source+'</div>') if parser=='lxml' else html5lib.parseFragment(source,treebuilder='etree',namespaceHTMLElements=False)
    return list(percorrer(root))

def comparar(old,new,expected_pairs,controle=None):
    if SHA(MARKED.read_bytes())!=MARKED_SHA:raise ValueError('motor GFM não corresponde à dependência fixada')
    code="import {marked} from '"+str(MARKED)+"';process.stdin.setEncoding('utf8');let t='';for await(const x of process.stdin)t+=x;process.stdout.write(JSON.stringify(JSON.parse(t).map(v=>marked.parse(v,{gfm:true,pedantic:false,breaks:false}))));"
    gfm=json.loads(subprocess.check_output([NODE,'--input-type=module','-e',code],input=json.dumps([old,new],ensure_ascii=False).encode()))
    cm=MarkdownIt('commonmark',{'html':True,'linkify':False,'typographer':False});renderers=dict(CommonMark=[cm.render(old),cm.render(new)],GFM=gfm)
    expected=[tuple(x) for x in expected_pairs];results=[];visible_reference=None
    output=Path(controle) if controle else None
    if output:output.mkdir(parents=True,exist_ok=False)
    for engine,pair in renderers.items():
        if output:
            for label,value in zip(['preimagem','candidato'],pair):(output/(engine+'-'+label+'.html.gz')).write_bytes(gzip.compress(value.encode(),mtime=0))
        for parser in ['lxml','HTML5lib']:
            a=analisar(pair[0],parser);b=analisar(pair[1],parser)
            if ''.join(ch for ch,deleted,ancestors in a)!=''.join(ch for ch,deleted,ancestors in b):raise ValueError(engine+'/'+parser+': texto ou espaços alterados')
            av=[(ch,ancestors) for ch,deleted,ancestors in a if not ch.isspace()];bv=[(ch,ancestors) for ch,deleted,ancestors in b if not ch.isspace()]
            if av!=bv:raise ValueError(engine+'/'+parser+': negrito/link/lista ou caractere alterado')
            if any(deleted for ch,deleted,ancestors in a):raise ValueError('baseline contém tachado já interpretado pelo motor')
            actual=[];rank=0;compact=[]
            for ch,deleted,ancestors in b:
                if ch.isspace():continue
                compact.append(ch)
                if deleted:actual.append((rank,ch))
                rank+=1
            if actual!=expected:raise ValueError(engine+'/'+parser+': escopo de tachado difere por posição/caractere')
            visible=''.join(compact)
            if visible_reference is None:visible_reference=visible
            if visible!=visible_reference:raise ValueError('projeções visíveis dos motores divergem')
            raw=json.dumps(actual,ensure_ascii=False,separators=(',',':')).encode()
            if output:(output/(engine+'-'+parser+'-pares-tachados.json.gz')).write_bytes(gzip.compress(raw,mtime=0))
            results.append(dict(motor=engine,parser_HTML=parser,caracteres_tachados=len(actual),sha256_pares_posicao_caractere=SHA(raw),texto_completo_e_espacos_identicos=True,ancestralidade_negrito_links_listas_identica=True,escopo_tachado_por_caractere_e_posicao_identico=True,sha256_visivel_sem_espacos=SHA(visible.encode())))
    receipt=dict(combinacoes=results,GFM=dict(modulo=str(MARKED),sha256=MARKED_SHA,versao='17.0.5',Node=NODE,Node_versao=subprocess.check_output([NODE,'--version']).decode().strip()),HTML5lib_versao=html5lib.__version__,CommonMark_versao=__import__('importlib.metadata',fromlist=['version']).version('markdown-it-py'),rede=False,comparacao='Todos os caracteres/espaços e ancestralidades antigos/novos comparados; cada caractere tachado compara posição não branca e código Unicode esperado. Nenhuma equivalência decimal, de sinal ou pontuação foi aplicada.')
    if output:(output/'recibo-motores.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    return receipt
