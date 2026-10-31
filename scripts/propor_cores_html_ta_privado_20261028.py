"""Experimento privado de preservação literal de cores; nunca libera publicação.

Mantém os dispositivos selecionados em HTML, incluindo atributos e tachados.
Compara texto, números, máscara e atributos contextuais pelo replay V3 existente,
além do inventário literal de cor. Folhas externas e renderização GitHub seguem
pendentes: este módulo não substitui gates V7/API/M/identidade/anexos/CSS.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / 'scripts/bin/qa-20261027/python'), str(ROOT / 'scripts')]
from converter_organica_fortaleza import Dispositivos
from inventariar_cores_ta_privado_20261028 import inventario
from perfil_ta_tachados_preservados_20261027 import comparar
from representacao_html_dou_v2 import assinatura_dom
from markdown_it import MarkdownIt


class TextoSeguro(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.starts = [0] + [m.end() for m in re.finditer('\n', source)]
        self.texts = []

    def handle_starttag(self, tag, attrs):
        if tag in {'pre', 'textarea', 'xmp', 'plaintext', 'listing', 'script', 'style', 'link',
                   'iframe', 'object', 'embed', 'form', 'input', 'button', 'select',
                   'img', 'svg', 'canvas', 'math', 'audio', 'video'}:
            raise ValueError('Elemento sensível/ativo/visual exige revisão própria')
        if len(dict(attrs)) != len(attrs):
            raise ValueError('Atributo duplicado')
        for key, value in attrs:
            if key.startswith('on') or key == 'hidden' or key == 'aria-hidden' and value == 'true':
                raise ValueError('Comportamento ou ocultação exige revisão própria')
            if key in {'href', 'src', 'action'} and re.sub(r'\s+', '', value or '').lower().startswith(('javascript:', 'data:', 'vbscript:')):
                raise ValueError('URL ativa')
            if key == 'style':
                if re.search(r'white-space|display\s*:|visibility\s*:|opacity\s*:|font-size\s*:\s*0|color\s*:\s*transparent', value or '', re.I):
                    raise ValueError('CSS sensível/oculto exige revisão própria')
                if '\\' in value or '/*' in value:
                    raise ValueError('CSS escapado ou comentado exige revisão própria')

    handle_startendtag = handle_starttag

    def handle_data(self, data):
        line, col = self.getpos()
        start = self.starts[line - 1] + col
        self.texts.append((start, start + len(data)))


def propor(source):
    parsed = Dispositivos()
    parsed.feed(source)
    parsed.close()
    if parsed.atual or not parsed.ativos:
        raise ValueError('Seleção incompleta')
    selected = '\n\n'.join(block['html'] for block in parsed.ativos)
    control = TextoSeguro(selected)
    control.feed(selected)
    control.close()
    output = selected
    for match in reversed(list(re.finditer(r'(?m)^[ \t]*\n', selected))):
        pos = match.end() - 1
        if not any(a <= pos < b for a, b in control.texts):
            raise ValueError('Linha vazia em atributo/tag exige revisão')
        output = output[:pos] + '&#10;' + output[pos + 1:]
    if assinatura_dom(selected) != assinatura_dom(output):
        raise ValueError('DOM textual ou atributos alterados')
    engine = MarkdownIt('commonmark', {'html': True}).enable('table').enable('strikethrough')
    rendered = engine.render(output)
    before = inventario(source)
    after = inventario(rendered)
    if before['ocorrencias'] != after['ocorrencias']:
        raise ValueError('Cor/atributos/texto de contexto divergiram na renderização CommonMark')
    proof = comparar(source, output)
    if not proof['aprovado']:
        raise ValueError('Replay V3 não aprovado')
    return output, dict(replay_V3=proof, inventario_cor_confere=True,
        DOM_textual_da_selecao_confere=True, apto_para_publicacao=False,
        folhas_externas_nao_consultadas=before['folhas_externas_nao_consultadas'],
        limite='Experimento de representação, sem gates de materialização/API/identidade. '
               'Atributos literais preservados em CommonMark local; GitHub e CSS externo não verificados. '
               'Não certifica aparência, atualização ou vigência e não autoriza promoção.')
