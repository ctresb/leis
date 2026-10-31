"""Separar referências legais explícitas de cabeçalhos, sem cortar conteúdo."""
import re
RELACAO=re.compile(r'\b(?:a|à|da|do|na|no|pela|pelo|esta|desta)\s+$',re.I)
def conferir_referencias(text,headings):
    out=[]
    for h in headings[1:]:
        start=text.rfind('\n',0,h.start())+1
        prefix=text[start:h.start()]
        if not prefix.strip() or re.search(r'[ \t]{3,}$',prefix):
            raise ValueError('epígrafe secundária em linha/coluna: exige contexto individual')
        if not RELACAO.search(prefix):
            raise ValueError('referência secundária sem relação gramatical explícita: exige contexto individual')
        out.append(dict(offset=h.start(),referencia_literal=h[0],contexto_literal=text[max(0,h.start()-180):h.end()+180]))
    return out
