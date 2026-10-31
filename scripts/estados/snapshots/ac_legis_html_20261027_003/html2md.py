"""Converte o HTML de normas (exportado do Word, como servido pelo normas.leg.br) em Markdown."""
import re
import html
from html.parser import HTMLParser

BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "div", "blockquote"}
SKIP_TAGS = {"head", "style", "script", "title", "xml"}

LABEL = re.compile(
    r"^((?:Art\.|Artigo) ?\d+(?:\.\d+)*\.?[º°o]?(?:-[A-Z]+)?\.?|§ ?\d+\.?[º°]?(?:-[A-Z]+)?\.?|Parágrafo único\.?)(?=\s)"
)
HEADINGS = [
    (re.compile(r"^PARTE (GERAL|ESPECIAL|[IVXLC]+)\b", re.I), 2),
    (re.compile(r"^LIVRO [IVXLC]+(-[A-Z])?\b", re.I), 2),
    (re.compile(r"^LIVRO COMPLEMENTAR\b", re.I), 2),
    (re.compile(r"^TÍTULO [IVXLC]+(-[A-Z])?\b", re.I), 3),
    (re.compile(r"^CAPÍTULO [IVXLC]+(-[A-Z])?\b", re.I), 4),
    (re.compile(r"^SEÇÃO [IVXLC]+(-[A-Z])?\b", re.I), 5),
    (re.compile(r"^SUBSEÇÃO [IVXLC]+(-[A-Z])?\b", re.I), 6),
    (re.compile(r"^ANEXOS?\b(\s+[IVXLC\d]+)?$", re.I), 2),
]


def style_flags(attrs):
    style = (dict(attrs).get("style") or "").replace(" ", "").lower()
    return {
        "b": "font-weight:bold" in style or "font-weight:700" in style,
        "i": "font-style:italic" in style,
        "s": "line-through" in style,
        "center": "text-align:center" in style,
    }


class TableParser(HTMLParser):
    TAGS = {"table", "caption", "colgroup", "col", "thead", "tbody", "tfoot", "tr", "th", "td",
            "p", "div", "br", "ul", "ol", "li", "blockquote", "sup", "sub"}
    VOID = {"br", "col", "img", "hr", "input", "meta", "link", "wbr"}
    VISUAL = {"img", "svg", "object", "embed", "iframe", "canvas", "input", "math"}

    def __init__(self, inherited, exclude_struck=False):
        super().__init__(convert_charrefs=True)
        self.exclude_struck = exclude_struck
        self.root = {"tag": None, "children": [], "flags": inherited, "skip": False}
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        if (tag in self.VISUAL or tag.startswith("v:")) and not self.stack[-1]["skip"]:
            raise ValueError(f"elemento visual não extraído na tabela: {tag}")
        if tag in ("colgroup", "thead", "tbody", "tfoot", "caption"):
            for k in range(len(self.stack) - 1, 0, -1):
                if self.stack[k]["tag"] == "table":
                    del self.stack[k + 1:]
                    break
        if tag == "tr":
            for k in range(len(self.stack) - 1, 0, -1):
                if self.stack[k]["tag"] == "table":
                    break
                if self.stack[k]["tag"] in ("colgroup", "caption"):
                    del self.stack[k:]
                    break
        # Fechamentos opcionais de HTML não podem criar células aninhadas.
        if tag in ("td", "th", "tr", "p"):
            targets = {"td", "th"} if tag in ("td", "th") else {tag}
            for k in range(len(self.stack) - 1, 0, -1):
                if self.stack[k]["tag"] == "table":
                    break
                if self.stack[k]["tag"] in targets:
                    del self.stack[k:]
                    break
        flags = style_flags(attrs)
        flags["b"] |= tag in ("b", "strong")
        flags["i"] |= tag in ("i", "em")
        flags["s"] |= tag in ("s", "strike", "del")
        flags = {k: flags[k] or self.stack[-1]["flags"].get(k, False) for k in ("b", "i", "s")}
        safe = {}
        for key, value in attrs:
            if key in ("rowspan", "colspan", "span") and tag in ("td", "th", "col", "colgroup"):
                if not re.fullmatch(r"[0-9]+", value or ""):
                    raise ValueError(f"{key} inválido na tabela")
                safe[key] = value
            elif key == "scope" and tag == "th" and value in ("row", "col", "rowgroup", "colgroup"):
                safe[key] = value
            elif key in ("id", "headers") and re.fullmatch(r"[\w .:-]+", value or ""):
                safe[key] = value
        node = {"tag": tag, "attrs": safe, "children": [], "flags": flags,
                "skip": self.stack[-1]["skip"] or tag in SKIP_TAGS}
        self.stack[-1]["children"].append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for k in range(len(self.stack) - 1, 0, -1):
            if self.stack[k]["tag"] == tag:
                del self.stack[k:]
                break

    def handle_data(self, data):
        if not self.stack[-1]["skip"]:
            self.stack[-1]["children"].append((data, self.stack[-1]["flags"]))

    def render(self, node=None):
        node = self.root if node is None else node
        if isinstance(node, tuple):
            text, flags = node
            if self.exclude_struck and flags.get("s"):
                return ""
            text = html.escape(text.replace("\r", " ").replace("\n", " "), quote=False)
            if not text.strip():
                return text
            for key, tag in (("i", "em"), ("b", "strong"), ("s", "del")):
                if flags.get(key):
                    text = f"<{tag}>{text}</{tag}>"
            return text
        if node["skip"] or (self.exclude_struck and node["flags"].get("s")):
            return ""
        content = "".join(self.render(child) for child in node["children"])
        tag = node["tag"]
        if tag not in self.TAGS:
            return content
        attrs = "".join(f' {k}="{html.escape(v, quote=True)}"' for k, v in node["attrs"].items())
        return f"<{tag}{attrs}>" if tag in self.VOID else f"<{tag}{attrs}>{content}</{tag}>"


class Parser(HTMLParser):
    def __init__(self, exclude_struck=False):
        super().__init__(convert_charrefs=True)
        self.exclude_struck = exclude_struck
        self.skip = 0
        self.fmt = []  # pilha de (tag, flags)
        self.runs = []  # [(texto, bold, italic, tachado)]
        self.block_center = False
        self.block_tag = None
        self.blocks = []  # (tipo, conteúdo, centralizado)
        self.source = ""
        self.line_offsets = [0]
        self.table_depth = 0

    def feed(self, data):
        inicio = len(self.source)
        self.line_offsets.extend(inicio + m.end() for m in re.finditer("\n", data))
        self.source += data
        super().feed(data)

    def source_offset(self):
        line, column = self.getpos()
        return self.line_offsets[line - 1] + column

    # --- formatação inline herdada ---
    def cur(self, key):
        return any(f.get(key) for _, f in self.fmt)

    def handle_starttag(self, tag, attrs):
        if self.table_depth:
            self.table_depth += tag == "table"
            return
        if tag == "table" and not self.skip:
            self.flush()
            self.table_depth = 1
            self.table_start = self.source_offset()
            self.table_inherited = {k: self.cur(k) for k in ("b", "i", "s")}
            return
        if tag in SKIP_TAGS:
            self.skip += 1
            return
        if tag in ("br",):
            self.runs.append(("\n", False, False, False))
            return
        if tag == "img":
            return
        flags = style_flags(attrs)
        if tag in ("b", "strong"):
            flags["b"] = True
        if tag in ("i", "em"):
            flags["i"] = True
        if tag in ("s", "strike", "del"):
            flags["s"] = True
        if tag in BLOCK_TAGS:
            self.flush()
            self.block_tag = tag
            self.block_center = flags["center"] or (dict(attrs).get("align") or "").lower() == "center"
        self.fmt.append((tag, flags))

    def handle_endtag(self, tag):
        if self.table_depth:
            if tag == "table":
                self.table_depth -= 1
                if not self.table_depth:
                    end = self.source.find(">", self.source_offset()) + 1
                    parser = TableParser(self.table_inherited, self.exclude_struck)
                    parser.feed(self.source[self.table_start:end])
                    parser.close()
                    self.emitir(("html_table", parser.render(), False))
            return
        if tag in SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
            return
        # desempilha até a tag correspondente
        for k in range(len(self.fmt) - 1, -1, -1):
            if self.fmt[k][0] == tag:
                del self.fmt[k:]
                break
        if tag in BLOCK_TAGS:
            self.flush()

    def handle_data(self, data):
        if self.skip or self.table_depth:
            return
        # quebra de linha no fonte HTML é só espaço; quebras reais vêm de <br>
        data = data.replace("\r", " ").replace("\n", " ")
        self.runs.append((data, self.cur("b"), self.cur("i"), self.cur("s")))

    def emitir(self, bloco):
        self.blocks.append(bloco)

    def flush(self):
        runs = [r for r in self.runs if not r[3]] if self.exclude_struck else self.runs
        text = render_runs(runs)
        self.runs = []
        if text:
            self.emitir((self.block_tag or "p", text, self.block_center))

def render_runs(runs):
    # junta runs com mesma formatação e aplica ** / * com espaços por fora dos marcadores
    merged = []
    for text, b, i, strike in runs:
        text = text.replace("﻿", "")
        text = re.sub(r"[ \t\r\f\v\xa0]+", " ", text.replace("\n", " \n "))
        if merged and merged[-1][1:] == [b, i, strike]:
            merged[-1][0] += text
        else:
            merged.append([text, b, i, strike])
    out = []
    previous_strike = False
    for text, b, i, strike in merged:
        core = text.strip(" ")
        if not re.search(r"\w", core) and not (strike and core.strip()):
            # só espaço/pontuação: formatação não acrescenta nada
            out.append(escape_inline(text))
            previous_strike = False
            continue
        lead = " " if text.startswith(" ") else ""
        trail = " " if text.endswith(" ") else ""
        mark = ("~~" if strike else "") + ("**" if b else "") + ("*" if i else "")
        core = escape_inline(core)
        rendered = f"{lead}{mark}{core}{mark[::-1]}{trail}" if mark else f"{lead}{core}{trail}"
        if previous_strike and strike and out[-1].endswith("~~") and rendered.startswith("~~"):
            out[-1] = out[-1][:-2] + rendered[2:]
        else:
            out.append(rendered)
        previous_strike = strike
    s = "".join(out)
    s = re.sub(r" *\n *", "\n", s)
    s = re.sub(r" {2,}", " ", s).strip()
    s = re.sub(r"\*\*\s*\*\*", " ", s)  # negritos vazios / colados
    s = re.sub(r"###[A-Z0-9-]*@@@", "", s)
    s = s.replace("<<Anexo>>", "").replace("<<ANEXO>>", "").replace("<<ANEXOS>>", "")
    return s.strip()


def escape_inline(s):
    return s.replace("\\", "\\\\").replace("*", "\\*").replace("_", "\\_").replace("<", "&lt;")


def strip_md(s):
    return re.sub(r"[*\\]", "", s).strip()


def heading_level(plain):
    for rx, lvl in HEADINGS:
        if rx.match(plain):
            return lvl
    return None


def looks_like_name(plain):
    return (
        0 < len(plain) < 200
        and heading_level(plain) is None
        and not LABEL.match(plain)
        and not re.match(r"^[IVXLC]+ ?[-–—]", plain)
        and not re.match(r"^[a-z]\)", plain)
        and not plain.startswith("(")
        and not re.search(r"[.;:,]$", plain)
    )


def table_md(rows):
    width = max(len(r) for r in rows)
    rows = [[c.replace("|", "\\|").replace("\n", " ") for c in r] + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + " --- |" * width]
    lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(lines)


def convert(html_text, *, exclude_struck=False):
    """Converte preservando o histórico por padrão.

    exclude_struck omite apenas texto marcado como tachado no HTML (tags e
    estilos inline); não certifica vigência, eficácia nem datas de aplicação.
    Notas de revogação, vigência e decisões judiciais continuam no resultado.
    """
    p = Parser(exclude_struck=exclude_struck)
    p.feed(html_text)
    p.close()
    if p.table_depth:
        raise ValueError("tabela HTML sem fechamento")
    p.flush()
    blocks = p.blocks
    # parágrafos com vários dispositivos separados só por <br>: cada dispositivo vira um parágrafo
    inicio_dispositivo = re.compile(
        r"(?=^(?:\*\*)?(?:Art\.? ?\d|Artigo \d|§ ?\d|Parágrafo único|[IVXLC]+ ?[-–—]|[a-z]\) |"
        r"(?:TÍTULO|CAPÍTULO|SEÇÃO|SUBSEÇÃO|LIVRO) [IVXLC]))",
        re.M,
    )
    expandidos = []
    for b in blocks:
        if b[0] not in ("table", "html_table") and "\n" in b[1]:
            partes = [p.strip() for p in inicio_dispositivo.split(b[1]) if p.strip()]
            expandidos += [(b[0], p, b[2]) for p in partes]
        else:
            expandidos.append(b)
    blocks = expandidos
    # cabeçalho institucional da compilação da Câmara
    while blocks and blocks[0][0] != "table" and strip_md(blocks[0][1]) in (
        "CÂMARA DOS DEPUTADOS",
        "Centro de Documentação e Informação",
    ):
        blocks = blocks[1:]

    out = []
    i = 0
    while i < len(blocks):
        kind, content, center = blocks[i]
        if kind in ("table", "html_table"):
            out.append(content if kind == "html_table" else table_md(content))
            i += 1
            continue
        plain = strip_md(content)
        lvl = heading_level(plain)
        if lvl and len(plain) < 250:
            # "CAPÍTULO I<br>DAS DISPOSIÇÕES" -> "CAPÍTULO I — DAS DISPOSIÇÕES"
            plain = re.sub(r"\s*\n\s*", " — ", plain)
            title = plain
            if re.fullmatch(r"\S+( \S+)? [IVXLC]+(-[A-Z])?|PARTE (GERAL|ESPECIAL)", plain, re.I) and i + 1 < len(blocks):
                nk, nc, _ = blocks[i + 1]
                if nk != "table" and looks_like_name(strip_md(nc)):
                    title = f"{plain} — {strip_md(nc)}"
                    i += 1
            out.append(f"{'#' * lvl} {title}")
        else:
            # "**Art.** 1.807." -> "**Art. 1.807.**"
            content = re.sub(
                r"^([“\"]?)\*\*(Art\.|§)\*\* ?(\d[\d.]*[º°o]?(?:-[A-Z]+)?\.?)(?=\s)", r"\1**\2 \3**", content
            )
            m = LABEL.match(plain)
            if m and not content.startswith("**"):
                # negrita o rótulo (Art. 1º, § 2º, Parágrafo único) quando ele vier sem formatação
                lab = m.group(1)
                if content.startswith(lab):
                    content = f"**{lab}**{content[len(lab):]}"
            if re.match(r"^\d+\. ", content):
                content = re.sub(r"^(\d+)\.", r"\1\\.", content)
            elif re.match(r"^[#>+\-] ", content):
                content = "\\" + content
            out.append(content.replace("\n", "  \n"))
        i += 1
    return "\n\n".join(out).strip() + "\n"


def convert_file(path, *, exclude_struck=False):
    with open(path, encoding="utf-8", errors="replace") as f:
        return convert(f.read(), exclude_struck=exclude_struck)


if __name__ == "__main__":
    import sys

    sys.stdout.write(convert_file(sys.argv[1]))
