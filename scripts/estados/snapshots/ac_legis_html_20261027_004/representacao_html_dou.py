"""Representação explícita e fiel de um campo texto-dou em HTML nativo.

Não busca fontes nem decide identidade, íntegra ou vigência. O chamador deve
manter esses gates e a captura original. CSS externo/herdado não fornecido no
fragmento não é certificado por este helper.
"""
from html.parser import HTMLParser
from html import unescape
import re

MODO_HTML_NATIVO = "html-nativo-texto-dou-v1"
_ATIVOS = {"script", "iframe", "object", "embed", "form", "input", "button",
           "select", "textarea", "style", "link", "meta", "base", "frame",
           "frameset", "applet", "audio", "video", "source", "track"}
_VISUAIS = {"img", "svg", "canvas", "math"}
_TACHADOS = {"s", "strike", "del"}
_CSS_RISCO = re.compile(
    r"line-through|display\s*:\s*none\b|visibility\s*:\s*(?:hidden|collapse)\b|"
    r"(?:^|;)\s*opacity\s*:\s*0(?:\.0*)?\s*(?:!important\s*)?(?:;|$)|"
    r"font-size\s*:\s*0(?:\.0*)?(?:[a-z%]+)?\s*(?:!important\s*)?(?:;|$)|"
    r"(?:^|;)\s*color\s*:\s*transparent\b", re.I)
_CLASSE_RISCO = re.compile(r"revogad|tachad|riscad|desativad|deleted|deletion|strike", re.I)


class _Campo(HTMLParser):
    def __init__(self, texto):
        super().__init__(convert_charrefs=False)
        self.texto = texto
        self.inicios = [0] + [m.end() for m in re.finditer("\n", texto)]
        self.textos = []
        self.divs = 0
        self.abriu = False
        self.fechou = False

    def posicao(self):
        linha, coluna = self.getpos()
        return self.inicios[linha - 1] + coluna

    def handle_starttag(self, tag, attrs):
        if len(dict(attrs)) != len(attrs):
            raise ValueError("atributo repetido exige revisão")
        attrs = dict(attrs)
        if self.fechou:
            raise ValueError("elemento fora do campo texto-dou")
        if not self.abriu:
            if tag != "div" or "texto-dou" not in attrs.get("class", "").split():
                raise ValueError("primeiro elemento não é o campo texto-dou")
            self.abriu = True
        if tag in _ATIVOS or any(k.lower().startswith("on") for k in attrs):
            raise ValueError("elemento/atributo ativo exige revisão")
        if tag in _VISUAIS or tag.startswith(("v:", "m:")):
            raise ValueError("elemento visual/fórmula exige revisão")
        if tag in _TACHADOS:
            raise ValueError("redação tachada exige revisão histórica/compilada")
        for key, value in attrs.items():
            value = value or ""
            if key == "hidden" or key == "aria-hidden" and value.lower() == "true":
                raise ValueError("conteúdo oculto exige revisão")
            if key in {"href", "src", "action", "formaction", "xlink:href"}:
                compact = re.sub(r"\s+", "", value).lower()
                if compact.startswith(("javascript:", "vbscript:", "data:")):
                    raise ValueError("URL ativa exige revisão")
            if key == "class" and _CLASSE_RISCO.search(value):
                raise ValueError("classe potencialmente histórica exige contexto CSS")
            if key == "style" and (_CSS_RISCO.search(value) or "\\" in value or "/*" in value):
                raise ValueError("CSS tachado/oculto ou escapado exige revisão")
            if key == "face" and re.search(r"wingdings|webdings|symbol", value, re.I):
                raise ValueError("fonte de símbolos exige revisão visual")
        if tag == "div":
            self.divs += 1

    def handle_startendtag(self, tag, attrs):
        if tag == "div":
            raise ValueError("div autocontida não comprova o campo normativo")
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if self.fechou:
            raise ValueError("fechamento fora do campo texto-dou")
        if tag == "div":
            self.divs -= 1
            if self.divs < 0:
                raise ValueError("fechamento de div sem abertura")
            if not self.divs:
                self.fechou = True

    def handle_data(self, data):
        if not self.abriu or self.fechou:
            if data.strip():
                raise ValueError("texto fora do campo texto-dou")
        inicio = self.posicao()
        self.textos.append((inicio, inicio + len(data)))

    def handle_entityref(self, name):
        if (not self.abriu or self.fechou) and not unescape("&" + name + ";").isspace():
            raise ValueError("entidade fora do campo texto-dou")

    def handle_charref(self, name):
        if (not self.abriu or self.fechou) and not unescape("&#" + name + ";").isspace():
            raise ValueError("entidade fora do campo texto-dou")

    def handle_comment(self, data):
        # Condicionais Word podem esconder recursos ou redações em outro render.
        raise ValueError("comentário HTML exige revisão do contexto")

    def handle_decl(self, decl):
        raise ValueError("declaração HTML fora do fragmento normativo")


def representar_fragmento(fragmento: str, *, modo: str) -> str:
    """Preserva fragmento/atributos, normaliza LF e escapa espaços textuais finais.

    Um espaço final vira &#32; e uma tabulação final vira &#9;, somente quando
    pertencem a um nó textual comprovado. Espaços dentro de tags/atributos não
    são normalizados. O resultado não recebe wrapper ou newline adicional.
    """
    if modo != MODO_HTML_NATIVO:
        raise ValueError("modo de representação HTML desconhecido")
    if not isinstance(fragmento, str):
        raise TypeError("fragmento deve ser texto Unicode")
    texto = fragmento.replace("\r\n", "\n").replace("\r", "\n")
    parser = _Campo(texto)
    parser.feed(texto)
    parser.close()
    if not parser.abriu or not parser.fechou or parser.divs:
        raise ValueError("campo texto-dou sem fechamento comprovado")
    trocas = []
    for match in re.finditer(r"[ \t]+(?=\n|$)", texto):
        if not any(a <= match.start() and match.end() <= b for a, b in parser.textos):
            raise ValueError("whitespace final em tag/atributo exige revisão")
        equivalente = "".join("&#32;" if c == " " else "&#9;" for c in match[0])
        trocas.append((match.start(), match.end(), equivalente))
    for inicio, fim, equivalente in reversed(trocas):
        texto = texto[:inicio] + equivalente + texto[fim:]
    return texto
