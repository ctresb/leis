"""Anotações editoriais delimitadas: preservar como histórico, nunca inferir vigência."""
import re
from contexto_to_pdf import EDITORIAL
EXTRA=re.compile(r'\(\s*(?:Revogad[oa]|Redaç[aã]o dada|Alterad[oa]|Acrescentad[oa])\b',re.I)
INICIO=re.compile(r'^\s*[*“\"\']?\s*\(?\s*(?:Redaç[aã]o|Revogad[oa]s?|Alterad[oa]s?|Acrescentad[oa]s?|Acrescid[oa]s?|Inclu[íi]d[oa]s?|Inserid[oa]s?|Suprimid[oa]s?|Substitu[íi]d[oa]s?|Declarad[oa])\b',re.I)

def conferir_anotacoes(text):
    spans=sorted({(m.start(),m.end()) for pattern in [EDITORIAL,EXTRA] for m in pattern.finditer(text)})
    result=[];seen=set()
    for start,end in spans:
        line_start=text.rfind('\n',0,start)+1
        line_end=text.find('\n',end)
        if line_end<0:line_end=len(text)
        prefix=text[line_start:start]
        if prefix.strip().strip('*“\"\' ('):
            raise ValueError('anotação editorial em dispositivo/citação ou fora do início de linha: exige contexto individual')
        literal=text[line_start:line_end]
        if not INICIO.match(literal):
            raise ValueError('anotação editorial não delimitada: exige contexto individual')
        if line_start in seen:continue
        seen.add(line_start)
        result.append(dict(linha_inicial=text.count('\n',0,line_start)+1,trecho_literal=literal,contexto_literal=text[max(0,line_start-120):min(len(text),line_end+240)]))
    return result
