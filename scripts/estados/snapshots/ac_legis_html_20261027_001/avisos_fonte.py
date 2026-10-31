"""Avisos explícitos de material não reproduzido na transcrição oficial."""
import re

_OMISSAO = re.compile(
    r'n[aã]o\b.{0,45}\b(?:reproduzid[oa]s?|transcrit[oa]s?|digitad[oa]s?|implantad[oa]s?|inclu[íi]d[oa]s?)\b',
    re.I,
)
_ASSUNTO = re.compile(r'anexo|imagem|formul[áa]rio|quadro|planta|mapa|conv[êe]nio|protocolo|ajuste|tabela|rela[çc][aã]o', re.I)
_OBSERVACAO = re.compile(r'\bOBS[.:]|OBSERVA[ÇC][ÃÕA]O', re.I)
_TECNICA = re.compile(r'impossibilidade\s+t[ée]cnica', re.I)


def avisos_de_omissao(corpo):
    """Devolve indício textual explícito; não afirma que falte no veículo impresso."""
    plano = ' '.join(corpo.split())
    avisos = [m.group() for m in re.finditer(r'\bOs?\s+anexos?\s+consta(?:m)?\s+no\s+DODF\b', plano, re.I)]
    for m in _OMISSAO.finditer(plano):
        antes = plano[max(0, m.start() - 180):m.start()]
        depois = plano[m.end():m.end() + 100]
        if not _ASSUNTO.search(antes[-120:]):
            continue
        if not (_OBSERVACAO.search(antes) or _TECNICA.search(depois)):
            continue
        trecho = plano[max(0, m.start() - 180):m.end() + 100]
        if trecho not in avisos:
            avisos.append(trecho)
    return avisos
