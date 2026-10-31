"""Retenção conservadora de objeto/suplemento próprio ausente da transcrição.

Rótulos, links e pontilhado não são conteúdo. A aprovação de um documento pode
exigir revisão mesmo sem a palavra ANEXO; referências a outro ato, alterações
atomizadas e objeto efetivamente reproduzido não bastam para reter.
"""
import html
import re
import unicodedata


def normal(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text.lower())
                   if not unicodedata.combining(c))


def _limpar(corpo):
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', corpo)
    text = re.sub(r'<a\b[^>]*>(.*?)</a>', r'\1', text, flags=re.I | re.S)
    # Double escaping occurs in official Word exports and in the transcription.
    for _ in range(3):
        decoded = html.unescape(text)
        if decoded == text:
            break
        text = decoded
    return normal(re.sub(r'[*_`#]', '', text))


def _rotulo_vazio(text):
    text = text.strip(' <>&«»\\[]()-')
    return bool(re.fullmatch(r'(?:anex[oa]s?|tabelas?|quadros?)(?:\s+[ivxlcdm\d .,–-]+)?\.?', text)) or bool(re.fullmatch(r'\\*final do documento\.?|\d+\s*/\s*\d+', text))



def _placeholder_terminal(clean):
    placeholder = re.search(r'(?:<<|«)\s*(?:anexo|tabela|quadro)s?\s*(?:>>|»)(.*)$', clean, re.S)
    if not placeholder:
        return None
    pointer = placeholder[1].strip()
    citation = not pointer or bool(re.fullmatch(r'(?:clbr|colecao das leis)\s*(?:(?:vol(?:ume)?|ano|pag(?:ina)?s?|tabelas?|anexos?|quadros?)[. ]*|\d+[. ,;:/–-]*|a\s+)+', pointer))
    return placeholder if citation else None


def _lacuna_literal_ou_desenho_proprio(clean, blocks):
    """Retém lacuna editorial ou desenho próprio para conferência documental.

    Não toma descrições ou um formulário textual como prova dos desenhos.
    Não afirma inexistência na lei ou em outra publicação.
    """
    for gap in re.finditer(r'\(\s*ilegivel(?:\s+parte\s+rasgada\s+no\s+livro[.]?)?\s*\)', clean):
        before = clean[max(0, gap.start() - 100):gap.start()]
        # Only explicit use/definition of the adjacent label is exempt.
        # A term containing a missing word is not a definition of that label.
        definition = re.search(r'\b(?:usar|empregar|escrever|registrar|lancar|adotar)\s+(?:a|o)\s+(?:expressao|palavra|termo|rubrica|rotulo)\s*[:=]?\s*["“«]?$', before)
        definition = definition or (re.search(r'\b(?:expressao|palavra|termo|rubrica|rotulo)\s*["“«]?$', before) and re.match(r'^["”»]?\s*(?:significa|designa|indica)\b', clean[gap.end():]))
        if not definition:
            return {'motivo': 'Marcador editorial explícito substitui trecho da transcrição; a concordância do Markdown com uma fonte mutilada não comprova integralidade.',
                    'lacuna': gap[0], 'contexto': clean[max(0, gap.start() - 180):gap.end() + 180],
                    'estado': 'revisao_documental_necessaria'}
    for article in blocks:
        if not re.match(r'^art(?:igo)?\.?\s*(?:\d|unico)', article):
            continue
        drawing = re.search(r'\bdesenhos?\s+anexos?\b', article)
        if not drawing:
            continue
        external = re.search(r'desenhos?\s+anexos?\s+(?:ao|aos|do|dos|a|as)\s+(?:decretos?(?:-lei)?|leis?|portarias?|resolucoes?)\s+n', article)
        quotation = re.search(r'passa[m]? a (?:ter|vigorar)|seguinte redacao|nova redacao|fica[m]? assim redigid', article)
        graphic_object = re.search(r'\b(?:medalhas?|insignias?|uniformes?|gola|bordados?|fitas?)\b', article)
        commanded_form = re.search(r'caracteristic|dimens|de acordo com|na forma|obedec|consignad|elucidad', article)
        referred_regulation = re.search(r'desenhos?\s+anexos?\s+(?:ao|a|aos|as)\s+(?:regulamento|regulamentacao)\b', article)
        if referred_regulation:
            tail = article[referred_regulation.end():]
            # Current explicit approval of this very regulation takes precedence
            # over any future ceremony regulation elsewhere in the decree.
            approved_here = re.search(r'^\s*(?:ja\s+)?aprovad[oa]\s+(?:por|pelo|neste|no)\s*(?:este|presente)?\s*decreto', tail)
            future_regulation = re.search(r'^\s*a ser (?:baixad|aprovad)', tail)
            subject = re.match(r'\s+d(?:a|o|as|os)\s+([a-z]+)', tail)
            if subject and not approved_here:
                # A named referent must share its first object noun. An unrelated
                # future regulation cannot discharge the present drawing.
                future_regulation = future_regulation or re.search(
                    r'\b(?:regulamento|regulamentacao)\s+d(?:a|o|as|os)\s+'
                    + re.escape(subject[1])
                    + r'\b(?:(?!\bregulamento\b)[^.\n]){0,180}\b(?:sera|devera)\s+(?:baixad|aprovad)', clean)
            own_approval = approved_here or re.search(r'\b(?:fica[m]?|sao|e)\s+aprovad[oa]s?\b', clean)
            if not approved_here and (future_regulation or not own_approval):
                continue  # This bound regulation is future or indeterminate.
        if graphic_object and commanded_form and not external and not quotation:
            return {'motivo': 'Objeto gráfico próprio referido expressamente como desenhos anexos, sem representação visual no HTML; descrição, outra tabela ou formulário textual não provam esses desenhos. Exige conferência documental individual.',
                    'remissao': article, 'lacuna': drawing[0],
                    'estado': 'revisao_documental_necessaria'}
    return None


def anexo_proprio_ausente(corpo, parsed):
    if parsed.visual:
        return None  # Separate visual gate retains these; this helper proves no absence.
    clean = _limpar(corpo)
    blocks = [re.sub(r'\s+', ' ', b).strip() for b in clean.split('\n\n') if b.strip()]
    explicit_gap = _lacuna_literal_ou_desenho_proprio(clean, blocks)
    if explicit_gap:
        return explicit_gap
    # A bibliographic replacement of drawings is a separate question from a
    # reproduced regulation or its text tables. It must survive the Art.1 shortcut.
    picture_gap = re.search(r'(?:<<|«)\s*(?:anexo|tabela|quadro)s?\s*(?:>>|»)\s*(?:clbr|colecao das leis)[^\n]*(?:carimbos?|figuras?|simbolo|desenhos?)[^\n]*', clean)
    own_regulation = re.search(r'\bfica[m]?\s+aprovad[oa]s?\b.{0,350}que com est[ea] baixa', clean)
    if picture_gap and own_regulation:
        return {'motivo': 'Objeto gráfico do regulamento próprio indicado apenas por placeholder bibliográfico; descrição textual ou outras tabelas não comprovam a reprodução dos desenhos, símbolos, carimbos ou figuras.',
                'lacuna': picture_gap[0], 'estado': 'revisao_documental_necessaria'}
    # A regulation can precede its own final signature when the first presidential
    # date has an unusual layout. A second own Art.1 is actual content, not a label.
    if len(re.findall(r'^\s*art(?:igo)?\.?\s*(?:1[º°o.]?(?!\d)|unico\b)', clean, re.M)) > 1:
        return None
    placeholder = _placeholder_terminal(clean)
    if placeholder and not parsed.structure:
        for article in blocks:
            if not re.match(r'^art(?:igo)?\.?\s*(?:\d|unico)', article):
                continue
            commanded = re.search(r'\bfica[m]?\s+alterad[oa]s?\b.{0,100}\bna forma d[ao] (?:relacao|tabela|quadro)\b.{0,80}\banex[oa]s?\b', article)
            external = re.search(r'anex[oa]s?\s+(?:ao|aos|do|dos)\s+(?:decretos?|leis?)\s+n', article)
            if commanded and not external:
                return {'motivo': 'Relação própria que determina a alteração da tabela pelo presente decreto substituída por placeholder terminal; referência bibliográfica não reproduz os nomes ou dados exigidos pelo comando.',
                        'remissao': article, 'lacuna': placeholder[0],
                        'estado': 'ausencia_na_transcricao'}
    fechamento = next((i for i, b in enumerate(blocks)
                        if re.match(r'^(?:brasilia|rio de janeiro|capital federal)(?:[-,\s]+d\.?f\.?)?[,.;\s]+(?:em\s*)?\d', b)), None)
    if fechamento is None:
        # A terminal literal placeholder with a bibliographic pointer is not the
        # promised own annex, even when the source omits the presidential date.
        if placeholder and not parsed.structure:
            articles = [b for b in blocks if re.match(r'^art(?:igo)?\.?\s*(?:\d|unico)', b)]
            for article in articles:
                own = re.search(r'\b(?:fica[m]?|sao|e)\s+aprovad[oa]s?\b', article) and re.search(r'\banex[oa]s?\b|que com est[ea] baixa', article)
                external = re.search(r'anex[oa]s?\s+(?:ao|aos|do|dos)\s+(?:decretos?|leis?)\s+n', article)
                if own and not external:
                    return {'motivo': 'Aprovação própria com placeholder terminal e nenhuma reprodução do suplemento; a indicação bibliográfica não é o conteúdo do anexo, mesmo sem fecho reconhecível.',
                            'remissao': article, 'lacuna': placeholder[0], 'fecho': None,
                            'estado': 'ausencia_na_transcricao'}
        return None
    principal = '\n'.join(blocks[:fechamento])
    explicit = re.search(r'que com est[ea] baixa[m]?|que a est[ea] acompanha|acompanha (?:este|o presente) decreto|anex[oa]s? a este decreto|anex[oa]s? ao presente decreto|anex[oa]s?(?:\s+[ivxlcdm\d]+(?:\s+e\s+[ivxlcdm\d]+)?)?\s+deste decreto', principal)
    artigos = [(i, b) for i, b in enumerate(blocks[:fechamento])
               if re.match(r'^art(?:igo)?\.?\s*(?:\d|unico)', b)]
    approvals = [(i, b, m) for i, b in artigos
                     for m in [re.search(r'\b(?:fica[m]?|sao|e)\s+aprovad[oa]s?\b', b)]
                     if m and not re.search(r'\b(?:sera|serao|devera|deverao|ate que|depois|apos|uma vez|quando|elaborado e aprovado|posteriormente)\b', b[:m.end()])]
    approval = next((a for a in approvals if re.search(r'\banex[oa]s?\b|acompanha|com est[ea] baixa', a[1])), approvals[0] if approvals else None)
    remissao = explicit
    document_only = False
    if approval:
        bi, artigo, match = approval
        own_annex = re.search(r'\banex[oa]s?\b|que com est[ea] baixa[m]?|acompanha', artigo)
        # Approval in the own article establishes the referent of 'na forma dos
        # anexos'. An annex explicitly belonging to another numbered act does not.
        if own_annex and not re.search(r'anex[oa]s? ao decreto\s+n', artigo):
            remissao = own_annex
        promised = re.search(r'a seguir mencionad[oa]s?|a saber', artigo)
        if promised:
            following = '\n'.join(blocks[bi + 1:fechamento])
            gap = re.match(r'^\.{15,}(?:\s|$)', following)
            if gap:
                return {'motivo': 'Relação prometida pelo comando próprio substituída por pontilhado, sem os nomes/dados na transcrição.',
                        'remissao': artigo, 'lacuna': gap[0].strip(), 'fecho': blocks[fechamento], 'estado': 'ausencia_na_transcricao'}
        after = artigo[match.end():]
        object_match = re.match(r'\s*(?:[,].{0,100}?[,])?\s*(?:(?:o|a|os|as)\s+)?(?:(?:novo|nova|novos|novas)\s+)?(regulamento|regimento|manual|estatuto|programas?|plano|criterios|quadro|tabela|relacao)\b', after)
        inline = re.search(r'seguinte[s]?\b|nos termos deste decreto|consoante o estabelecido no presente decreto|abaixo|constituido d[oa]s?|compreendendo|constituindo programa', artigo)
        # For short approvals without deixis, hold as a documented question rather
        # than claiming an omitted annex: the object may be defined by the own act.
        if not remissao and object_match and len(artigos) <= 5 and not inline and not re.search(r'anex[oa]s? ao decreto\s+n', artigo):
            document_only = True
            remissao = match
    # A substituted model can be an own annex without an approval formula.
    # A literal placeholder is evidence of a label, never of the promised model.
    if not remissao and any(_rotulo_vazio(b) for b in blocks[fechamento + 1:]):
        for _, artigo in artigos:
            model = re.search(r'\bmodelos?\s+anex[oa]s?\b', artigo)
            external = re.search(r'\bmodelos?\s+anex[oa]s?\s+(?:ao|aos|do|dos)\s+decretos?\s+n', artigo)
            if model and not external:
                remissao = re.search(re.escape(artigo), principal)
                break
    if not remissao:
        return None
    # A table after the approval may be the object itself, including a table placed
    # before the presidential date. A table before the approval proves nothing.
    if parsed.structure:
        table = clean.find('<table')
        command = clean.find(approval[1]) if approval else -1
        if table < 0 or command < 0 or table > command:
            return None
    apos = blocks[fechamento + 1:]
    heading = re.compile(r'^(?:anexo|regulamento|regimento|manual|estatuto|tabela|quadro|relacao|convencao|acordo)\b')
    if any(re.match(r'^art(?:igo)?\.?\s*\d', b) for b in apos):
        return None
    tail = [b for b in apos if not _rotulo_vazio(b) and not heading.match(b)
            and not re.search(r'publicad[oa]|diario oficial|\bdou\b|nao substitui', b)]
    if any(len(b) > 130 or re.search(r'\d|[:;!?=]', b) or len(b.split()) > 16 or re.match(r'^(?:o|a|os|as|cada|este|esta|para|compete|cabe)\s', b) for b in tail) or len(' '.join(tail)) > 650:
        return None
    if document_only:
        # Lists or operative details between the approval and the date may be the
        # complete object; neither a separate annex nor a title is then required.
        bi, artigo, match = approval
        material = '\n'.join(blocks[bi + 1:fechamento])
        if re.search(r'(?m)^(?:\d+[).\\]|[ivx]+\s*[-–]|[a-z]\))', material) or '<table' in material:
            return None
        return {'motivo': 'Aprovação própria de documento sem remissão explícita: fonte só traz aprovação/regras administrativas e fecho; exige revisão do objeto, sem afirmar lacuna comprovada.',
                'remissao': artigo, 'fecho': blocks[fechamento], 'apos_fecho': apos,
                'estado': 'revisao_documental_necessaria'}
    return {'motivo': 'Suplemento próprio referido pelo decreto ausente da transcrição: somente fecho, assinaturas, nota ou rótulo/link vazio, sem corpo do objeto.',
            'remissao': approval[1] if approval else principal[max(0, remissao.start() - 120):remissao.end() + 120],
            'fecho': blocks[fechamento], 'apos_fecho': apos, 'estado': 'ausencia_na_transcricao'}
