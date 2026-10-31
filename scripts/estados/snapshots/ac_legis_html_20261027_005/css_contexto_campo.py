"""Matching CSS conservador de campo HTML explícito e ancestrais.

Derivado do matcher Legisla.AM; sem exceção de loader ou fontes presumidas.
Não consulta rede, não reescreve fonte e não certifica seletores desconhecidos.
"""
import gzip,hashlib,json,re
from pathlib import Path
from urllib.parse import urljoin
import tinycss2,cssselect2
from lxml import html
SHA=lambda b:hashlib.sha256(b).hexdigest()
PROP={'mso-hide','display','visibility','opacity','text-decoration','text-decoration-line','content','clip','clip-path','overflow','overflow-x','overflow-y','height','max-height','font-size','font-family','color','text-indent','transform','filter','background','background-image','list-style-image','border-image-source','mask-image','-webkit-mask-image'}

def riscos(name,value):
    v=value.strip().lower()
    if 'var(' in v:return True
    if name in ('background-image','list-style-image','border-image-source','mask-image','-webkit-mask-image'):return v not in ('none','initial','inherit','unset')
    if name=='background':return bool(re.search(r'url\s*\(|gradient\s*\(|image(?:-set)?\s*\(|element\s*\(|paint\s*\(',v))
    if name=='mso-hide':return v=='all'
    if name=='display':return v=='none'
    if name=='visibility':return v in ('hidden','collapse')
    if name=='opacity':
        try:return float(v)==0
        except ValueError:return True
    if name.startswith('text-decoration'):return 'line-through' in v
    if name=='content':return v not in ('none','normal','""',"''",'" "',"' '")
    if name in ('clip','clip-path'):return v not in ('none','auto')
    if name in ('height','max-height','font-size'):return bool(re.fullmatch(r'[+\-]?0*(?:\.0*)?(?:[a-z%]+)?',v))
    if name=='font-family':
        # Nomes completos de famílias, não a palavra Symbol dentro de um nome
        # Unicode legítimo como Segoe UI Symbol. tinycss2 resolve escapes CSS.
        families=[];part=[]
        for token in tinycss2.parse_component_value_list(value):
            if token.type=='literal' and token.value==',':
                families.append(' '.join(part).strip().lower());part=[]
            elif token.type in ('ident','string'):part.append(token.value)
            elif token.type!='whitespace':return True
        families.append(' '.join(part).strip().lower())
        return any(re.fullmatch(r'symbol|wingdings(?:\s*[23])?|webdings',f) for f in families)
    if name=='color':return v in ('transparent','white','#fff','#ffffff') or bool(re.search(r'(?:rgba|hsla)\([^)]*,\s*0(?:\.0*)?\s*\)',v)) or bool(re.fullmatch(r'#(?:[0-9a-f]{3}0|[0-9a-f]{6}00)',v))
    if name=='text-indent':return v.startswith('-')
    if name=='transform':return v!='none'
    if name=='filter':return 'opacity(0)' in v or 'opacity(0%)' in v
    # overflow é registrado; ocultação por geometria exige contexto, mesmo sem altura explícita.
    if name.startswith('overflow'):return v in ('hidden','clip')
    return False

def declaracoes(content):
    return {d.lower_name:tinycss2.serialize(d.value).strip() for d in tinycss2.parse_declaration_list(content,skip_comments=True,skip_whitespace=True) if d.type=='declaration' and d.lower_name in PROP}

class ContextoCSS:
    def __init__(self,receipts):
        self.matcher=cssselect2.Matcher();self.falhas=[];self.fontes=[];self.imports=[]
        for row in receipts:
            packed=Path(row['cache']).read_bytes();raw=gzip.decompress(packed)
            if row['http']!=200 or SHA(raw)!=row['sha256_fonte'] or SHA(packed)!=row['sha256_cache']:raise ValueError('captura CSS divergente')
            self.fontes.append(dict(url=row['url'],sha256_fonte=SHA(raw)));self._parse(tinycss2.parse_stylesheet(raw.decode('utf8'),skip_comments=True,skip_whitespace=True),row['url'])
        known={r['url'] for r in self.fontes}
        if any(url not in known for url in self.imports):raise ValueError('@import sem fonte capturada')
    def _parse(self,nodes,url,cond=''):
        for n in nodes:
            if n.type=='error':raise ValueError('CSS com erro de parsing exige revisão')
            if n.type=='at-rule':
                if n.lower_at_keyword=='import':
                    p=tinycss2.serialize(n.prelude);m=re.search(r'url\(["\x27]?([^"\x27)]+)',p)
                    if not m:raise ValueError('@import não reconhecido')
                    self.imports.append(urljoin(url,m[1]))
                elif n.content and n.lower_at_keyword in ('media','supports','layer','document'):self._parse(tinycss2.parse_rule_list(n.content,skip_comments=True,skip_whitespace=True),url,cond+' @'+n.lower_at_keyword+' '+tinycss2.serialize(n.prelude))
            elif n.type=='qualified-rule':
                ds=declaracoes(n.content)
                if not ds:continue
                # Tokens de função são atômicos: vírgulas dentro de :not/:is não separam seletores.
                parts=[[]]
                for t in n.prelude:
                    if t.type=='literal' and t.value==',':parts.append([])
                    else:parts[-1].append(t)
                for part in parts:
                    s=tinycss2.serialize(part).strip();proof=dict(url=url,linha=n.source_line,seletor=s,condicao=cond,declaracoes=ds)
                    try:compiled=cssselect2.compile_selector_list(s)
                    except cssselect2.SelectorError:
                        # Remover pseudoestados produz um superconjunto conservador.
                        # Retirar um pseudoestado positivo cria superconjunto.
                        # Dentro de funções lógicas/estruturais não presumir essa
                        # propriedade: manter retenção se o seletor não compilar.
                        proxy=None if re.search(r':[\w-]+\s*\(',s) else re.sub(r'::?-(?:webkit|moz|ms)-[\w-]+|:(?:valid|invalid|indeterminate)\b','',s)
                        if proxy is not None:
                            try:proxy=cssselect2.compile_selector_list(proxy)
                            except cssselect2.SelectorError:proxy=None
                        self.falhas.append((proof,proxy));continue
                    for c in compiled:self.matcher.add_selector(c,proof)
    def conferir(self,source,tag_campo="body",classe_campo=None,id_campo=None,id_final_campo=None):
        root=cssselect2.ElementWrapper.from_html_root(html.document_fromstring(source));fields=[e for e in root.iter_subtree() if (e.id==id_campo if id_campo else classe_campo in e.classes if classe_campo else e.local_name==tag_campo)]
        if len(fields)!=1:raise ValueError('campo CSS não é único')
        field=fields[0];descendants=list(field.iter_subtree())
        if id_final_campo:
            ends=[e for e in root.iter_subtree() if e.id==id_final_campo]
            positions=[i for i,e in enumerate(descendants) if len(ends)==1 and e.etree_element is ends[0].etree_element]
            if len(positions)!=1:raise ValueError('marcador final CSS não é único ou não pertence ao campo')
            descendants=descendants[:positions[0]+len(list(ends[0].iter_subtree()))]
        # O DOM inteiro permanece intacto para seletores relacionais (:has etc.).
        # Só o conjunto normativo examinado termina no marcador explícito; o
        # chamador deve provar que o material posterior é interface/fora do texto.
        targets=descendants+list(field.ancestors);matched=[];holds=[];ignored=0;unsupported_neutral=[];empty_white=[]
        inline=ContextoCSS([])
        for i,node in enumerate(root.etree_element.iter('style')):
            css=node.text or '';url='inline:'+SHA(source.encode())+'#style'+str(i+1)
            inline.fontes.append(dict(url=url,sha256_fonte=SHA(css.encode())))
            inline._parse(tinycss2.parse_stylesheet(css,skip_comments=True,skip_whitespace=True),url)
        known={r['url'] for r in self.fontes}
        for url in inline.imports:
            if url not in known:holds.append(dict(motivo='@import em CSS inline sem fonte capturada',url=url))
        for proof,proxy in self.falhas+inline.falhas:
            if not any(riscos(k,v) for k,v in proof['declaracoes'].items()):
                unsupported_neutral.append(proof);continue
            if proxy is None or any(c.test(e) for c in proxy for e in targets):holds.append(dict(motivo='seletor não suportado pode atingir o campo',regra=proof))
            else:ignored+=1
        seen=set()
        for e in targets:
            for _,_,pseudo,p in self.matcher.match(e)+inline.matcher.match(e):
                key=(p['url'],p['linha'],p['seletor'],pseudo)
                if key in seen:continue
                seen.add(key);q=dict(**p,pseudo=pseudo);matched.append(q)
                for name,v in p['declaracoes'].items():
                    if not riscos(name,v):continue
                    holds.append(dict(motivo='regra potencialmente oculta/tachada/gerada exige contexto',regra=q,propriedade=name,valor=v))
            if e.local_name=='font' and riscos('color',e.etree_element.get('color','')):holds.append(dict(motivo='cor de font potencialmente oculta exige contexto',tag='font',valor=e.etree_element.get('color')))
            for name,v in declaracoes(e.etree_element.get('style','')).items():
                if not riscos(name,v):continue
                node=e.etree_element
                # Caso literal observado em fontes SE: span folha que contém só
                # NBSP/whitespace e cujo único atributo/propriedade é color:white.
                # Nada é removido da fonte ou do corpo. Texto, filhos, outros
                # atributos e conteúdo gerado por CSS continuam sendo retidos.
                if (name=='color' and e.local_name=='span' and len(node)==0
                    and not (node.text or '').strip() and set(node.attrib)=={'style'}
                    and re.fullmatch(r'\s*color\s*:\s*white\s*;?\s*',node.get('style',''),re.I)):
                    empty_white.append(dict(tag='span',texto_literal=node.text,style_literal=node.get('style'),prova='Folha sem filhos, somente whitespace/NBSP; único atributo e propriedade é color:white. Fonte e corpo preservados.'));continue
                holds.append(dict(motivo='style inline potencialmente oculto/tachado',tag=e.local_name,propriedade=name,valor=v))
        return dict(sha256_HTML=SHA(source.encode()),fontes_CSS=self.fontes+inline.fontes,classes_internas=sorted(set(c for e in descendants for c in e.classes)),IDs_internos=sorted(set(e.id for e in descendants if e.id)),escopo=dict(tag=tag_campo,classe=classe_campo,id=id_campo,id_final=id_final_campo),regras=matched,seletores_nao_suportados_disjuntos=ignored,seletores_nao_suportados_sem_risco_nas_propriedades_examinadas=unsupported_neutral,spans_brancos_vazios_comprovados=empty_white,retencoes=holds,CSS_sem_risco_comprovado=not holds)
