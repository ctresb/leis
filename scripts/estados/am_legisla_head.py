"""Dedup offline por HEAD fornecido pelo coordenador; nenhum acesso ao Git."""
import collections,re,urllib.parse

def normalizar(v):return re.sub(r'[.\s]','',str(v)).upper().lstrip('0')
def namespace(url):
    u=urllib.parse.urlparse(url)
    patterns={'legisla.imprensaoficial.am.gov.br':r'/diario_am/\d+/\d{4}/\d{1,2}/(\d+)','sapl.al.am.leg.br':r'/norma/(\d+)/?'}
    if u.netloc not in patterns:return None
    m=re.fullmatch(patterns[u.netloc],u.path)
    return (u.netloc,m[1]) if m else None

def conferir(documentos,inventario,mapa):
    if set(mapa)!={r['destino'] for r in documentos} or any(s is not None for s in mapa.values()):raise ValueError('destinos não são exatamente ausentes em HEAD')
    ids=collections.defaultdict(list);tipos=collections.defaultdict(list);pastas=collections.defaultdict(list)
    for r in inventario['documentos']:
        meta=r['meta'];p=r['path'].split('/');year=str(meta.get('data') or meta.get('ano') or p[3])[:4];num=normalizar(meta.get('numero',''));space=namespace(meta.get('fonte',''))
        if space:ids[space].append(r['path'])
        tipos[(meta.get('tipo'),num,year)].append(r['path']);pastas[(p[2],num,year)].append(r['path'])
    proof=[];internos=set();official=set()
    for r in documentos:
        qa=r['QA'];space=namespace(r['captura']['item']['url']);key=(qa['tipo'],normalizar(qa['numero']),qa['data'][:4])
        if space is None or space[0]!='legisla.imprensaoficial.am.gov.br':raise ValueError('namespace Legisla não comprovado')
        aliases=sorted(set(ids.get(space,[])+tipos.get(key,[])+pastas.get(('leis-ordinarias',key[1],key[2]),[])))
        if aliases:raise ValueError('alias de HEAD: '+r['destino']+' '+str(aliases))
        if key in internos or space in official:raise ValueError('identidade repetida dentro do pacote')
        internos.add(key);official.add(space);proof.append(dict(destino=r['destino'],namespace_fonte=space,numero=qa['numero'],ano=key[2],HEAD_SHA256=None,aliases=[]))
    return proof
