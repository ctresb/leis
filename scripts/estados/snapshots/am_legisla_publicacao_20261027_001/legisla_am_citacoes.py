"""Prova conservadora de referências inline, sem reescrever ou fundir atos.

Epígrafes estrangeiras só deixam de ser suspeitas quando cada ocorrência está
no interior de um parágrafo e introduzida por preposição explícita. Cabeçalhos
isolados e ocorrências fora desses blocos continuam exigindo revisão contextual.
"""
import collections,hashlib,re
from lxml import html
from pe_fidelidade_visivel import texto_visivel_html
from legisla_am_identidade import identidade
FOREIGN=re.compile(r'\bLEI\s+N[.º°o\s]*[0-9][0-9.\s]*(?:-[A-Z]+)?\s*,?\s+DE\s+\d{1,2}\s+DE\s+[A-ZÇ]+\s+DE\s+\d{4}\b',re.I)
SHA=lambda b:hashlib.sha256(b).hexdigest()
def conferir_citacoes(field,own):
    visible=texto_visivel_html(field);expected=collections.Counter();proof=[];found=collections.Counter()
    def key(m):
        p=identidade(m[0]);return (p['numero'],p['data'])
    ours=(own['numero'],own['data'])
    for m in FOREIGN.finditer(visible):
        k=key(m)
        if k!=ours:expected[k]+=1
    root=html.fragment_fromstring(field,create_parent='div')
    for p in root.iter('p'):
        # Parágrafos aninhados/malformados não constituem prova independente.
        if any(a.tag=='p' for a in p.iterancestors()):continue
        text=texto_visivel_html(html.tostring(p,encoding='unicode'))
        for m in FOREIGN.finditer(text):
            k=key(m)
            if k==ours:continue
            prefix=text[:m.start()]
            if not re.search(r'\b(?:da|de|pela|na|à|a)\s+$',prefix,re.I):continue
            # A preposição deve pertencer ao texto do próprio parágrafo, não a um título vazio.
            if not prefix.strip():continue
            found[k]+=1;proof.append(dict(numero_citado=k[0],data_citada=k[1],referencia_literal=m[0],prefixo_literal=prefix[-140:],sufixo_literal=text[m.end():m.end()+140],sha256_paragrafo=SHA(text.encode())))
    return dict(total_referencias=sum(expected.values()),referencias_comprovadas=sum(found.values()),todas_contextualizadas=found==expected,provas=proof,sem_alteracao_de_texto=True)
