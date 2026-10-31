"""Epígrafe literal Legisla.AM; não usa ano da URL como data da norma."""
import datetime,re
MESES={s:i for i,s in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split(),1)}
EP=re.compile(r'^\s*(?:\(\*\)\s*)?LEI\s+N[.º°o\s]*([0-9][0-9.\s]*(?:-[A-Z]+)?)\s*,?\s+DE\s+(\d{1,2})\s+DE\s+([A-ZÇ]+)\s+DE\s+(\d{4})\b',re.I)
def identidade(s):
    m=EP.search(s)
    if not m:raise ValueError('epígrafe própria de lei ordinária não comprovada')
    number=re.sub(r'[.\s]','',m[1]).lstrip('0') or '0';date=datetime.date(int(m[4]),MESES[m[3].lower()],int(m[2])).isoformat()
    return dict(tipo='Lei Ordinária',numero=number,data=date,epigrafe=m[0].strip())
