"""Variantes literais comprovadas nas fontes TO, sem editar números ou nomes."""
import re
FECHO=re.compile(r'Pal[áa]cio\s+(?:Araguaia|Deputado\s+João\s+D[’\']Abreu)\s*,?\s+em\s+Palmas\s*,?\s+aos?\s+(\d{1,2})[º°o]?\s+dias?\s+do\s+m[eê]s\s+de\s+([a-zç]+)\s+de\s+(\d{4})',re.I)
ART=re.compile(r'^\s*Art[.]\s*1(?:[.]?[º°o])?[.]?\s',re.I)
SECTION=re.compile(r'^\s*(?:CAP[ÍI]TULO\s+I\s*\n\s*(?:Das?\s+)?Disposiç(?:ão|ões)\s+(?:Gerais|Preliminares?)\s*\n|Disposição\s+Preliminar\s*\n)',re.I)

def artigo_inicial(text):
    if ART.match(text):return True
    section=SECTION.match(text)
    return bool(section and ART.match(text[section.end():]))

def cargo_assinatura(text,closing):
    rest=text[closing.end():]
    if re.search(r'Governador\s+do\s+Estado|Presidente\s+da\s+Assembl[eé]ia',rest,re.I):return True
    legislature=bool(re.match(r'Pal[áa]cio\s+Deputado\s+João\s+D[’\']Abreu',closing[0],re.I))
    announced=re.search(r'Presidente\s+(?:desta\s+Casa|da\s+Assembl[eé]ia\s+Legislativa)',text[:closing.start()],re.I)
    signed=re.search(r'(?m)^\s*(?:Deputad[oa]\s+)?[A-ZÁÀÃÂÉÊÍÓÔÕÚÇ][A-ZÁÀÃÂÉÊÍÓÔÕÚÇ ]+\n\s*Presidente\s*(?:\n|$)',rest)
    return bool(legislature and announced and signed)
