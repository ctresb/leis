"""Recupera a data de uma norma a partir da epígrafe do texto.

Algumas fontes não informam a data no índice (SC e PE nas emendas, PA nas leis antigas), mas o
texto abre com a epígrafe oficial — "EMENDA CONSTITUCIONAL Nº 38, DE 16 DE DEZEMBRO DE 2013".
A data é lida só dessa linha: solta, a busca casaria com a data de publicação no Diário Oficial
ou com a primeira lei citada no corpo.
"""
import datetime as dt
import re
from zoneinfo import ZoneInfo

MESES = {m: i + 1 for i, m in enumerate(
    "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split())}
MESES.update({"marco": 3, "setembro": 9})

# os tipos infralegais entraram com o acervo do Diário Oficial: a epígrafe de uma resolução ou
# de uma portaria tem a mesma forma da de uma lei ("RESOLUÇÃO ANM Nº 249, DE 13 DE OUTUBRO DE 2026")
TIPO_EPIGRAFE = re.compile(
    r"\b(LEI|EMENDA|DECRETO|CONSTITUI[ÇC][ÃA]O|ATO|RESOLU[ÇC][ÃA]O|PORTARIA|INSTRU[ÇC][ÃA]O"
    r"|CIRCULAR|DELIBERA[ÇC][ÃA]O|PROVIMENTO|S[ÚU]MULA|PARECER|SOLU[ÇC][ÃA]O"
    r"|CONV[ÊE]NIO|PROTOCOLO|AJUSTE|RECOMENDA[ÇC][ÃA]O)\b", re.I)
# "Nº 38, DE 16 DE DEZEMBRO DE 2013" / "Nº 07, 29 de dezembro de 1993"
POR_EXTENSO = re.compile(
    r"(?:DE\s+)?(\d{1,2})[º°]?\s+DE\s+([A-Za-zÀ-ÿ]+)\s+DE\s+(\d{4})", re.I)
NUMERICA = re.compile(r"\b(\d{1,2})[./](\d{1,2})[./](\d{4})\b")


def _iso(dia, mes, ano):
    # a legislação federal começa em 1821; nada fora disso é data de norma
    if not 1800 <= ano <= dt.datetime.now(ZoneInfo("America/Recife")).year:
        return None
    try:
        return dt.date(ano, mes, dia).isoformat()
    except ValueError:
        return None


def data_do_texto(corpo, numero=None, linhas=6):
    """AAAA-MM-DD a partir da epígrafe, ou None.

    Só considera as primeiras `linhas` linhas úteis do corpo e, entre elas, as que parecem a
    epígrafe da norma (traz o tipo e, se `numero` for dado, o próprio número).
    """
    uteis = [ln.strip() for ln in corpo.split("\n") if ln.strip()]
    uteis = [ln for ln in uteis if not ln.startswith(("#", ">"))][:linhas]
    for ln in uteis:
        if not TIPO_EPIGRAFE.search(ln):
            continue
        if numero:
            # o número pode vir com zeros à esquerda ("Nº 07") ou separador de milhar
            flex = r"0*" + r"\.?".join(re.escape(c) for c in str(numero))
            if not re.search(r"N[º°o.\s]*" + flex + r"\b", ln, re.I):
                continue
        m = POR_EXTENSO.search(ln)
        if m:
            mes = MESES.get(m.group(2).lower())
            if mes:
                d = _iso(int(m.group(1)), mes, int(m.group(3)))
                if d:
                    return d
        m = NUMERICA.search(ln)
        if m:
            d = _iso(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            if d:
                return d
    return None
