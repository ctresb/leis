"""Retenção conservadora de remissão explícita a anexo da própria norma."""
import re

_REMISSAO = re.compile(
    r'(?:anex[oa]s?\b.{0,100}\b(?:a\s+|d)?(?:este|esta|presente)\s+'
    r'(?:decreto|lei|resolu[çc][aã]o|portaria)|'
    r'tabelas?\s*[IVX\d]*\s*[,;]?\s*(?:em\s+anexo|deste decreto)|'
    r'anex[oa]s?\s+(?:que\s+)?(?:integra[m]?|acompanha[m]?)\s+(?:est[ae]|[oa]\s+presente))',
    re.I,
)


def remissoes_sem_representacao(corpo):
    """Não certifica completude; exige revisão dos casos devolvidos, sem inferir teor."""
    remissoes = [m.group() for m in _REMISSAO.finditer(corpo)
                 if not re.search(r'\b(?:d[oa]|a[oa])\s+(?:decreto|lei|RICMS|RIPVA|regulamento|resolu[çc][aã]o|portaria)\b',
                                  m.group(), re.I)]
    if not remissoes:
        return []
    if re.search(r'(?im)^\s*[#*\s]{0,8}(?:ANEXO|TABELA|QUADRO)\b', corpo):
        return []
    if re.search(r'<table\b|^\s*\|.*\|\s*$', corpo, re.I | re.M):
        return []
    return remissoes
