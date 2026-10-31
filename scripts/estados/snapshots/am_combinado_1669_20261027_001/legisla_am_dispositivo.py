import re

def dispositivo_proprio(visible):
    m=re.search(r'(?:presente|seguinte)\s+L\s*E\s*I\s*[:.]?\s*(?:(?-i:CAP[IÍ]TULO|T[IÍ]TULO|SE[CÇ][AÃ]O|LIVRO|PARTE)\b(?-i:[A-ZÀ-Ý0-9\s,/()–-]){0,300})?(Art[.]\s*1\s*[.º°o]*\s)',visible,re.I)
    first=re.search(r'\bArt[.]\s*1\s*[.º°o]*\s',visible)
    if not m or not first or first.start()!=m.start(1):raise ValueError('artigo inicial próprio após promulgação/sanção não comprovado')
    before=visible[max(0,m.start()-400):m.start()]
    if not re.search(r'\b(?:sanciono|promulgo|promulga)\b',before,re.I):raise ValueError('sanção/promulgação própria não comprovada')
    return visible[max(0,m.start()-80):m.end()+100]
