"""Detecta recursos visuais que o conversor textual não representa.

O chamador deve delimitar antes o campo normativo, excluindo controles do portal.
Não decide que uma remissão a anexo é da própria norma; registra a evidência visual.
"""
from html.parser import HTMLParser


class _Imagens(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imagens = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "img":
            self.imagens.append(dict(attrs))

    handle_startendtag = handle_starttag


def imagens_html(fragmento):
    parser = _Imagens()
    parser.feed(fragmento)
    return parser.imagens


def exigir_sem_imagem_omitida(fragmento):
    imagens = imagens_html(fragmento)
    if imagens:
        recursos = ", ".join(im.get("src", "(sem src)") for im in imagens)
        raise ValueError("imagem normativa exige preservação/conferência visual: " + recursos)
