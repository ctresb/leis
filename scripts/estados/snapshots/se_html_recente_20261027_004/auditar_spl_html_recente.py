"""QA escopado de textos HTML integrais recentes ES/SE; sem promoção canônica."""
import gzip,hashlib,json,re,datetime
from pathlib import Path
from urllib.parse import urljoin
from lxml import html
from markdown_it import MarkdownIt
from tabelas_estrutura import _Tabelas
from css_contexto_campo import ContextoCSS
from integridade_texto import verificar_integridade_texto
from avisos_fonte import avisos_de_omissao
from visuais_word_spl import conferir as conferir_VML
from comum import decodificar
from html2md import convert
from pe_fidelidade_visivel import texto_visivel_html,assinatura_numerica,_heading_comprovado
SHA=lambda b:hashlib.sha256(b).hexdigest()
MESES={m:i for i,m in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split(),1)}
BRASOES_SE=('0d527a9c62cf403eac6c8bf41d3375e5ed4885914b230705b094c39da7878272', '1fc50b2d464855b8e203432dbc746dc99a4ae7fb94c88f662e6d9612a435ab79', '21c18948a2cb9c626eed7064125f63cf6193935dd3967af69e13e8e3a7d5a337', '248763c6729f1f98e184972bbea3aa56eb348cdc323e8658310fc00b7c60ff6e', '31331045fb310ed78bcf3fabf5ae4b4ae0154b54ecc56cf26667a2d134c331e2', '3a4a0ab2a455c12192b77c806e788f3b16bc1387adb63121068d9d81561e1edf', '3b29a77760fddae215aa61466bbe637699e1f87eec3c4f406836c196a5e3e4b4', '4582394917ab173c66f07d9e3aca37ec4f128b708ddc343500da44e3bfbf7b0b', '471f37195a40015442424d1b38468bbf6302005765f4d56e97aae9fb6ce2ded6', '4b02f0dff709b8b5c1633a0968cb6cd7e249f87b8a785a5f9c7e2e963010c78d', '4bddc7e77b20294219ae7ac184c572ca7eedf45a80dd791b6528c7187376e1f2', '6503c3fde229020563b454bb9bc1cf44483d4358b3ca802afbac677fdefdcb47', '9a08f370b5f630eef5b324eb89b080cc212a769f05e7ce84083e44fd2a3a8508', '9cca16065d32c08180f491a16c013dd9b0039e2d892a24e90f9f6f39ad7517e8', 'a47ecfbb705dafef42871b162db4c4623d53589d74379176896afb0c00507896', 'b7f59e45fb2c5b7b2d69df9412183595f531006317b264df15bf23578abfd3d6', 'bbbca2319fb929bd525aa3c1cba7b5e2122b1a46ce03acb641a92504965019a5', 'c43b9bfa3cd3485126c18ad91e69c210dabbcd716e3a76405d0f91f5aa7a0309', 'ccc6d8d71dbde965ca0fd0934772d95e0e62b91362353286f0e3f88a55ead1a4', 'd481a4ef41b4b44a8c02c3988571d8c709e8bbcea4f321d452dc8661c45bf7b2', 'db3ac06a122099e834bb2be6cdc54fe611706db83e97b683e4c6fd1e24322407', 'e28829cca5ca685d2f9462e54c508b5a2800f26803bab460ed7eb9e7f9eb826f', 'f0cf4525ed375c2d9f297f36f743a728445eb8a8c2924e768ed5d60cf20164ac', 'f439cd73ac5864486b805e52ef0db632b8e3a9d80579d499d84b5ee9eb6acd26', 'f6dd75fe77c5ded4dfa9cebd5eea16121e17a6a6280205f0289349b25d9dc4a8')

def identidade(text,item):
    m=re.search(r'\b(LEI(?: COMPLEMENTAR)?)\s+N[º°.]*(?:\s+)([\d.]+(?:-[A-Za-z]+)?),?\s+DE\s+(\d{1,2})[º°]?\s+DE\s+([A-ZÇ]+)\s+DE\s+(\d{4})',text[:900],re.I)
    if not m:raise ValueError('epígrafe própria ausente')
    tipo='Lei Complementar' if m[1].upper()=='LEI COMPLEMENTAR' else 'Lei Ordinária';date=f'{m[5]}-{MESES[m[4].lower()]:02d}-{int(m[3]):02d}'
    if (tipo,m[2].replace('.','').upper(),date)!=(item['tipo'],item['numero'],item['data']):raise ValueError('identidade própria diverge do cartão')
    if not re.search(r'\bArt[.]\s*1[º°.]?\s',text):raise ValueError('artigo próprio inicial ausente')
    f=re.search(r'\bAracaju,\s*(\d{1,2})[º°]?\s+de\s+([a-zç]+)\s+de\s+(\d{4})',text,re.I)
    if not f or f'{f[3]}-{MESES[f[2].lower()]:02d}-{int(f[1]):02d}'!=date:raise ValueError('data do fecho diverge')
    return dict(epigrafe=m[0],fecho=f[0],data=date,numero=m[2].replace('.','').upper(),tipo=tipo)

def identidade_html(source,item):
    doc=html.fromstring(source)
    rx=re.compile(r'^LEI(?: COMPLEMENTAR)?\s+N[º°.]*(?:\s+)[\d.]+(?:-[A-Za-z]+)?,?\s+DE\s+\d{1,2}[º°]?\s+DE\s+[A-ZÇ]+\s+DE\s+\d{4}[.]?$',re.I)
    blocks=[' '.join(e.text_content().split()) for e in doc.xpath('//p|//h1|//h2|//h3|//div')]
    heads=[text for text in blocks if rx.fullmatch(text)]
    if len(heads)!=1:raise ValueError('bloco de epígrafe própria não único')
    return identidade(heads[0]+' '+texto_visivel_html(source),item)

def cronologia_rodape(source,data):
    """Retém dúvida cronológica literal; não escolhe data nem invalida articulado."""
    text=texto_visivel_html(source);rows=[]
    for m in re.finditer(r'Este texto não substitui.{0,180}?(?=(?:ANEXO\b|$))',text,re.I):
        trecho=m[0]
        for d in re.finditer(r'\b(\d{2})[.](\d{2})[.](\d{4})\b',trecho):
            try:date=datetime.date(int(d[3]),int(d[2]),int(d[1])).isoformat()
            except ValueError:raise ValueError('data literal inválida no rodapé de publicação')
            rows.append(dict(trecho=trecho,data_rodape=date,data_epigrafe=data))
            if date<data:raise ValueError('dúvida cronológica: rodapé DOE anterior à epígrafe/fecho; revisão individual necessária')
    return rows

def matrizes_normativas(source):
    parser=_Tabelas();parser.feed(source)
    if parser.pilha:raise ValueError('tabela não fechada')
    out=[]
    for t in parser.tabelas:
        cells=[dict(linha=c['linha'],rowspan=c['rowspan'],colspan=c['colspan'],texto=' '.join(''.join(c['texto']).split())) for c in t['celulas']]
        txt=' '.join(c['texto'] for c in cells)
        for label in ['Estado de Sergipe','Assembleia Legislativa','Secretaria-Geral da Mesa Diretora']:txt=txt.replace(label,'')
        # Exclusão escopada das tabelas de cabeçalho cujos únicos textos são estes três rótulos.
        if not txt.strip():continue
        out.append(cells)
    return out

def comparar(source,body):
    parser=MarkdownIt('commonmark',{'html':True}).enable('table');tokens=parser.parse(body)
    if any(t.type=='ordered_list_open' for t in tokens):raise ValueError('contadores CommonMark exigem revisão contextual')
    v=texto_visivel_html(parser.render(body));s=texto_visivel_html(source)
    original_tables=matrizes_normativas(source);rendered_tables=matrizes_normativas(parser.render(body))
    if original_tables!=rendered_tables:raise ValueError('células/linhas/spans de tabela divergem')
    normalized,headings=_heading_comprovado(v,body,s)
    if s!=normalized or assinatura_numerica(s)!=assinatura_numerica(normalized):raise ValueError('texto visível/sinais divergem da fonte integral')
    return dict(tabelas_normativas=len(original_tables),sha256_matrizes=SHA(json.dumps(original_tables,ensure_ascii=False,sort_keys=True).encode()),normalizacoes_de_heading_comprovadas=headings,sha256_visivel_normalizado=SHA(normalized.encode()),sha256_visivel_fonte=SHA(s.encode()),sha256_visivel_commonmark=SHA(v.encode()),sha256_html_renderizado=SHA(parser.render(body).encode()),caracteres_visiveis=len(s))

def auditar(captura,imagens,body_atual=None):
    r=captura;it=r['item'];z=Path(r['cache']).read_bytes();b=gzip.decompress(z)
    if r['http']!=200 or SHA(z)!=r['sha256_cache'] or SHA(b)!=r['sha256_fonte']:raise ValueError('fonte/captura diverge')
    if r['url'] not in it['textos_completos_observados'] or r['url_final']!=r['url']:raise ValueError('link integral não observado/redirect inesperado')
    source=decodificar(b)
    if re.search(r'\bTexto\s+compilado\b',texto_visivel_html(source),re.I):raise ValueError('compilação explícita exige revisão de edição/tachados')
    if '\ufffd' in source:raise ValueError('decodificação contém substituição')
    doc=html.fromstring(source);bodies=doc.xpath('//body')
    if len(bodies)!=1:raise ValueError('body não único')
    if any(k.lower().startswith('on') for e in doc.iter() for k in e.attrib):raise ValueError('evento ativo exige revisão')
    if any(re.match(r'\s*(javascript|vbscript):',v,re.I) for e in doc.iter() for k,v in e.attrib.items() if k.lower() in ('href','src')):raise ValueError('URL ativa exige revisão')
    if re.search(r'@import\b',source,re.I):raise ValueError('CSS importado exige captura/contexto')
    if doc.xpath('//script|//iframe|//object|//embed|//svg|//canvas|//del|//strike|//s'):raise ValueError('ativo, visual ou tachado exige revisão')
    if doc.xpath('//link[translate(@rel,"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz")="stylesheet"]'):raise ValueError('CSS externo não capturado')
    if doc.xpath('//*[@hidden or translate(@aria-hidden,"TRUE","true")="true"]'):raise ValueError('atributo de ocultação exige revisão')
    if bodies[0].xpath('.//ol|.//ul'):raise ValueError('listas HTML exigem prova de contadores')
    proof=[]
    for node in doc.xpath('//img'):
        url=urljoin(r['url_final'],node.get('src',''));m=[x for x in imagens if x.get('url')==url and x.get('id')==it['id']]
        if len(m)!=1 or m[0]['http']!=200 or m[0]['sha256'] not in BRASOES_SE or SHA(Path(m[0]['arquivo']).read_bytes())!=m[0]['sha256']:raise ValueError('imagem sem prova literal do brasão revisto')
        proof.append(dict(url=url,sha256=m[0]['sha256'],arquivo=m[0]['arquivo'],revisao='Brasão oficial de Sergipe examinado visualmente; apenas decorativo.'))
    if len(proof)!=1:raise ValueError('esperado exatamente um brasão no escopo revisto')
    # Só a tag raster cujo recurso foi conferido é omitida da apresentação textual.
    filtered=re.sub(r'<img\b[^>]*>','',source,flags=re.I);body=convert(filtered)
    issue,dispositivo=verificar_integridade_texto(body)
    if issue:raise ValueError(issue)
    if avisos_de_omissao(body):raise ValueError('aviso explícito de material não representado')
    css=ContextoCSS([]).conferir(source)
    if css['retencoes']:raise ValueError('CSS exige revisão contextual')
    vml=conferir_VML(source,r['url_final'],proof)
    q=identidade_html(source,it);q.update(rodapes_publicacao=cronologia_rodape(source,q['data']));q.update(comparar(source,body));q.update(CSS=css,dispositivo_proprio=dispositivo,VML=vml);q.update(imagens=proof,total_tabelas=len(doc.xpath('//table')),sha256_corpo=SHA(body.encode()),sha256_fonte=SHA(b),codificacao='UTF-16 com BOM' if b.startswith((b'\xff\xfe',b'\xfe\xff')) else 'charset/meta e decodificação estrita sem U+FFFD',limite='Fidelidade ao HTML integral publicado pela ALESE; não certifica igualdade à edição DOE. Alinhamento, fonte e CSS de apresentação não são reproduzidos integralmente pelo Markdown.')
    if body_atual is not None and body_atual!=body:raise ValueError('corpo privado diverge da reconversão')
    return body,q
