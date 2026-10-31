"""Confere células, linhas e spans das tabelas HTML complexas antes da publicação."""
from html.parser import HTMLParser
import re


class _Tabelas(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pilha = []
        self.tabelas = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'table':
            if self.pilha:
                self.pilha[-1]['aninhada'] = True
            table = {'linha': 0, 'celulas': [], 'ativa': None, 'aninhada': False}
            self.pilha.append(table)
            self.tabelas.append(table)
        elif self.pilha and tag == 'tr':
            self.pilha[-1]['linha'] += 1
        elif self.pilha and tag in ('td', 'th'):
            table = self.pilha[-1]
            rowspan = int(attrs.get('rowspan', '1'))
            colspan = int(attrs.get('colspan', '1'))
            if rowspan < 1 or colspan < 1:
                raise ValueError('span não positivo exige revisão')
            cell = {'linha': table['linha'], 'tag': tag, 'rowspan': rowspan,
                    'colspan': colspan, 'texto': []}
            table['celulas'].append(cell)
            table['ativa'] = cell
        elif self.pilha and tag == 'br':
            self.handle_data(' ')

    def handle_endtag(self, tag):
        if tag == 'table' and self.pilha:
            self.pilha.pop()
        elif self.pilha and tag in ('td', 'th'):
            self.pilha[-1]['ativa'] = None

    def handle_data(self, data):
        for table in self.pilha:
            if table['ativa'] is not None:
                table['ativa']['texto'].append(data)


def tabelas_complexas(texto):
    parser = _Tabelas()
    parser.feed(texto)
    if parser.pilha:
        raise ValueError('tabela sem fechamento')
    out = []
    for table in parser.tabelas:
        cells = table['celulas']
        if not table['aninhada'] and all(c['rowspan'] == c['colspan'] == 1 for c in cells):
            continue
        out.append([dict(c, texto=re.sub(r'\s+', ' ', ''.join(c['texto'])).strip()) for c in cells])
    return out


def conferir_tabelas_complexas(fonte_html, convertido):
    original = tabelas_complexas(fonte_html)
    resultado = tabelas_complexas(convertido)
    if original != resultado:
        raise ValueError('células, linhas, textos ou spans de tabela complexa divergem da fonte')
    return original
