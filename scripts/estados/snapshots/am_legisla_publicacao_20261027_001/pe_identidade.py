"""Identidade PE somente da epígrafe no campo normativo; sem ano de publicação."""
import datetime as dt
import re
from zoneinfo import ZoneInfo

from datas import data_do_texto

TIPOS_EPIGRAFE = {
    '13': r'EMENDA\s+CONSTITUCIONAL', '2': r'LEI\s+COMPLEMENTAR',
    '1': r'LEI(?!\s+COMPLEMENTAR)', '11': r'DECRETO\s*[-–]?\s*LEI',
    '6': r'DECRETO(?!\s+LEGISLATIVO)', '4': r'RESOLU[ÇC][ÃA]O',
    '5': r'DECRETO\s+LEGISLATIVO', '8': r'PORTARIA(?:\s+ADMINISTRATIVA)?',
}


def numero_indice(item):
    m = re.search(r'n[°º]\s*([\d.]+(?:-[A-Za-z]+)?)\b', item['nome'], re.I)
    if not m:
        raise ValueError('número do índice não comprovado')
    return m[1].replace('.', '').upper()


def identidade_do_texto(item, corpo):
    numero = numero_indice(item)
    linhas = [re.sub(r'^#{1,6}\s+', '', ln.strip()) for ln in corpo.splitlines() if ln.strip()][:6]
    semzeros = numero.lstrip('0') or '0'
    flex = r'0*' + r'\.?'.join(map(re.escape, semzeros))
    ep = re.compile(r'^\s*\*{0,2}\s*' + TIPOS_EPIGRAFE[item['tipo']] + r'\s+N[º°o.\s]*' + flex + r'\b', re.I)
    proprias = [ln for ln in linhas if ep.search(ln)]
    data = data_do_texto('\n'.join(proprias), numero=semzeros)
    if not data or dt.date.fromisoformat(data) > dt.datetime.now(ZoneInfo('America/Recife')).date():
        raise ValueError('tipo/número/data da epígrafe própria não comprovados')
    return numero, data, proprias[0]
