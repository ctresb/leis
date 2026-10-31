"""Candidatos privados mínimos por captura original; não adivinha ID/data nem muda corpo."""
import gzip,hashlib,json,re
from pathlib import Path
from lxml import html
from comum import decodificar
SHA=lambda b:hashlib.sha256(b).hexdigest()
BLOCKS={'p','h1','h2','h3','h4','div','td','th'}

def ementa_original(raw,numero,ano):
    source=decodificar(raw)
    if '\ufffd' in source:raise ValueError('decodificação ambígua')
    doc=html.fromstring(source);blocks=[e for e in doc.iter() if e.tag in BLOCKS and not any(c.tag in BLOCKS for c in e.iterdescendants()) and e.text_content().strip()];texts=[' '.join(e.text_content().split()) for e in blocks];heads=[i for i,t in enumerate(texts) if re.fullmatch(r'LEI\s+N[º°.]*(?:\s+)[\d.]+,?\s+DE\s+\d{1,2}[º°]?\s+DE\s+[A-ZÇ]+\s+DE\s+\d{4}[.]?',t,re.I)]
    if len(heads)!=1:raise ValueError('epígrafe não única')
    i=heads[0];n=re.search(r'N[º°.]*(?:\s+)([\d.]+)',texts[i],re.I)
    if n[1].replace('.','')!=str(numero).replace('.','') or not texts[i].rstrip('.').endswith(str(ano)):raise ValueError('identidade original diverge')
    text=texts[i+1];node=blocks[i+1]
    if not re.match(r'^(?:Autoriza|Reconhece|Altera|Dispõe|Inclui|Institui|Declara|Revalida)\b',text,re.I):raise ValueError('ementa não identificada inequivocamente')
    nexts=texts[i+2:i+5]
    if not any(re.match(r'^O GOVERNADOR DO ESTADO',s,re.I) for s in nexts):raise ValueError('fim da ementa sem autoridade próxima')
    return text,dict(epigrafe_literal=texts[i],ementa_literal=text,tag=node.tag,sha256_no_ementa_serializado=SHA(html.tostring(node,encoding='utf8')),criterio='Bloco textual único imediatamente após epígrafe própria e antes de autoridade/nota editorial; nenhuma reconstrução de palavras ou aspas.')

def candidato(raw_md,raw_source,url_arquivo,numero,ano):
    text=raw_md.decode();head,body=text.split('\n---\n',1);lines=head.splitlines();out=[];changes=[];em,proof=ementa_original(raw_source,numero,ano)
    replacements={'fonte':url_arquivo,'revogada':None,'situacao':None,'ementa':em}
    for line in lines:
        if ': ' not in line:out.append(line);continue
        key,value=line.split(': ',1)
        if key not in replacements:out.append(line);continue
        new=key+': '+json.dumps(replacements[key],ensure_ascii=False)
        if new!=line:changes.append(dict(campo=key,antes=line,depois=new))
        out.append(new)
    if {x['campo'] for x in changes}!={'fonte','revogada','situacao','ementa'}:raise ValueError('alterações diferentes das quatro permitidas')
    result=('\n'.join(out)+'\n---\n'+body).encode();assert result.decode().split('\n---\n',1)[1]==body
    return result,dict(ementa=proof,alteracoes=changes,sha256_corpo_incluindo_H1=SHA(body.encode()),limite='Corpo inteiro inclusive H1 preservado; sem certificação de edição compilada, tipografia ou equivalência DOE. Datas/números/títulos mantidos, sem inferência de IDs.')
