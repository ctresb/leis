"""Confronto literal conservador entre epígrafe e assinatura, sem corrigir datas."""
import datetime,re
from legisla_am_identidade import MESES
MARKER=re.compile(r'(?:GABINETE DO GOVERNADOR|PAL[AÁ]CIO DO GOVERNO|PA[CÇ]O DA ASSEMBL[EÉ]IA)',re.I)
def conferir(text,data_epigrafe):
    matches=list(MARKER.finditer(text))
    if not matches:return dict(status='nao_comparavel',motivo='marcador de assinatura não reconhecido',reter=False)
    seg=text[matches[-1].start():matches[-1].start()+500];m=re.search(r'\bManaus\s*,\s*(\d{1,2})\s+de\s+([A-ZÇ]+)\s+de\s+(\d{4})\b',seg,re.I)
    if not m:return dict(status='nao_comparavel',motivo='data de assinatura não reconhecida literalmente',reter=False)
    try:date=datetime.date(int(m[3]),MESES[m[2].lower()],int(m[1])).isoformat()
    except (KeyError,ValueError):return dict(status='data_assinatura_indeterminada',trecho_literal=m[0],data_epigrafe=data_epigrafe,reter=True)
    return dict(status='conferida' if date==data_epigrafe else 'divergencia_literal',data_epigrafe=data_epigrafe,data_assinatura=date,trecho_literal=m[0],reter=date!=data_epigrafe)
