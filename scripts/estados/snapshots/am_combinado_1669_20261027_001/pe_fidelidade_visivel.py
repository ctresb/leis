"""Comparação de texto visível que conserva pontuação, moeda e sinais numéricos.

Escopo: Markdown produzido por html2md (ênfase, headings, GFM e HTML nativo).
Não é um renderizador de Markdown de uso geral. Normaliza apenas whitespace e
remove marcadores de apresentação conhecidos, preservando conteúdo escapado,
código inline e dados de HTML nativo. Divergências permanecem para revisão.
"""
import re
from html.parser import HTMLParser


class _Visivel(HTMLParser):
    BLOCK = {'p','div','h1','h2','h3','h4','h5','h6','li','tr','td','th','table','blockquote','pre'}
    SKIP = {'head','style','script','title','xml'}
    VOID = {'br','hr','img','meta','link','input','wbr','col'}

    def __init__(self, protect=None):
        super().__init__(convert_charrefs=True)
        self.stack=[];self.skip=0;self.parts=[];self.protect=protect

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:self.skip+=1
        if not self.skip and (tag in self.BLOCK or tag in {'br','hr'}):self.parts.append(' ')
        if tag not in self.VOID:self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:self.skip-=1
        if not self.skip and tag in self.BLOCK:self.parts.append(' ')
        if tag in self.stack:
            i=len(self.stack)-1-self.stack[::-1].index(tag);del self.stack[i:]

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag,attrs)
        if tag not in self.VOID:self.handle_endtag(tag)

    def handle_data(self, data):
        if self.skip:return
        self.parts.append(self.protect(data) if self.protect and self.stack else data)


def _spaces(text):return ' '.join(text.replace('\ufeff','').split())


def texto_visivel_html(source):
    p=_Visivel();p.feed(source);p.close();return _spaces(''.join(p.parts))


def _split_pipes(line):
    cells=[];current=[];slashes=0
    for char in line:
        if char=='|' and slashes%2==0:
            cells.append(''.join(current));current=[]
        else:current.append(char)
        slashes=slashes+1 if char=='\\' else 0
    cells.append(''.join(current))
    if not cells[0].strip():cells=cells[1:]
    if cells and not cells[-1].strip():cells=cells[:-1]
    return cells


def _sem_estrutura_gfm(text):
    lines=text.splitlines();out=[];i=0
    while i<len(lines):
        if i+1<len(lines) and '|' in lines[i]:
            separator=_split_pipes(lines[i+1])
            if separator and all(re.fullmatch(r'\s*:?-{3,}:?\s*',x) for x in separator):
                out.append(' '.join(_split_pipes(lines[i])));i+=2
                while i<len(lines) and lines[i].lstrip().startswith('|'):
                    out.append(' '.join(_split_pipes(lines[i])));i+=1
                continue
        out.append(lines[i]);i+=1
    return '\n'.join(out)


def _proteger_codigo_e_escapes(text,protect):
    """Escapes/código só fora de HTML nativo; nunca reinterpreta uma célula HTML."""
    punctuation=set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    native=[];out=[];i=0
    tags=re.compile(r'<(/?)([A-Za-z][A-Za-z0-9:-]*)\b[^>]*>')
    ticks=re.compile(r'`+')
    while i<len(text):
        if text.startswith('<!--',i):
            end=text.find('-->',i+4);end=len(text) if end<0 else end+3
            out.append(text[i:end]);i=end;continue
        tag=tags.match(text,i) if text[i]=='<' else None
        if tag:
            name=tag[2].lower()
            if tag[1]:
                if name in native:del native[len(native)-1-native[::-1].index(name):]
            elif name not in _Visivel.VOID and not tag[0].endswith('/>'):native.append(name)
            out.append(tag[0]);i+=len(tag[0]);continue
        if not native and text[i]=='\\' and i+1<len(text) and text[i+1] in punctuation:
            out.append(protect(text[i+1]));i+=2;continue
        if not native and text[i]=='`':
            run=ticks.match(text,i)[0];end=None
            for close in ticks.finditer(text,i+len(run)):
                if close[0]==run:end=close.start();break
            if end is not None:
                content=text[i+len(run):end].replace('\n',' ')
                if content.startswith(' ') and content.endswith(' ') and content.strip():content=content[1:-1]
                out.append(protect(content));i=end+len(run);continue
        out.append(text[i]);i+=1
    return ''.join(out)


def texto_visivel_markdown(markdown):
    protected=[]
    def protect(text):
        protected.append(text);return '\ue000'+str(len(protected)-1)+'\ue001'
    text=_sem_estrutura_gfm(markdown)
    text=_proteger_codigo_e_escapes(text,protect)
    parser=_Visivel(protect);parser.feed(text);parser.close();text=''.join(parser.parts)
    text=re.sub(r'(?m)^\s{0,3}#{1,6}\s+','',text)
    # Formatação balanceada fora de HTML nativo; literal escapado está protegido.
    for mark in ('***','**','~~','*','___','__','_'):
        char=mark[0];edge=re.escape(char)
        before=r'(?<!\w)' if char=='_' else ''
        after=r'(?!\w)' if char=='_' else ''
        rx=re.compile(before+r'(?<!'+edge+r')'+re.escape(mark)+r'(?!'+edge+r')(?=\S)(.+?)(?<=\S)(?<!'+edge+r')'+re.escape(mark)+r'(?!'+edge+r')'+after,re.S)
        while True:
            new=rx.sub(r'\1',text)
            if new==text:break
            text=new
    # Restaura até o nível final, pois dados HTML podem conter código protegido.
    token=re.compile('\ue000([0-9]+)\ue001')
    while token.search(text):text=token.sub(lambda m:protected[int(m[1])],text)
    return _spaces(text)


def assinatura_numerica(visible):
    """Conserva decimais, separadores, sinal, moeda, percentual e parênteses."""
    pattern=r'US\$|R\$|[€£$%‰()\[\]{}]|(?<!\w)[+−-]|[–—](?=\s*\d)|\d+(?:[.,:/-]\d+)*'
    return re.findall(pattern,visible)


def _heading_comprovado(visible,markdown,source):
    changes=[]
    for line in markdown.splitlines():
        if not re.match(r'^#{2,6} ',line):continue
        title=texto_visivel_markdown(line)
        if ' — ' not in title:continue
        prefix,name=title.split(' — ',1)
        if not re.fullmatch(r'(?:PARTE (?:GERAL|ESPECIAL|[IVXLC]+)|(?:LIVRO|TÍTULO|CAPÍTULO|SEÇÃO|SUBSEÇÃO|ANEXOS?) (?:COMPLEMENTAR|[IVXLC0-9]+(?: [IVXLC0-9]+)*(?:-[A-Z]+)?))',prefix,re.I):continue
        original=prefix+' '+name
        # Não descarta travessão literal da fonte nem qualquer sinal de valor.
        if original in source and title not in source and title in visible:
            visible=visible.replace(title,original,1)
            changes.append({'markdown':title,'fonte':original,'prova':'Prefixo e título literalmente adjacentes na fonte. Separador editorial inserido pela regra explícita HEADINGS de html2md, sem alteração de palavras/números.'})
    return visible,changes


def comparar_fidelidade(source_html, expected_md, actual_md):
    source=texto_visivel_html(source_html);expected=texto_visivel_markdown(expected_md);actual=texto_visivel_markdown(actual_md)
    normalized,headings=_heading_comprovado(actual,actual_md,source)
    return {'texto_visivel_md_igual_reconversao':actual==expected,
            'texto_visivel_md_igual_html_fonte':actual==source,
            'texto_visivel_md_igual_fonte_apos_formato_heading_comprovado':normalized==source,
            'numeros_sinais_moedas_percentuais_iguais_fonte':assinatura_numerica(normalized)==assinatura_numerica(source),
            'normalizacoes_de_apresentacao':headings,
            'visivel_fonte':source,'visivel_reconversao':expected,'visivel_md':actual,'visivel_md_apos_heading_comprovado':normalized}
