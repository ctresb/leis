"""Triagem conservadora de íntegra: dispositivo próprio e retificações.

Não certifica completude jurídica. O chamador deve confrontar identidade oficial,
edição e corpo com a fonte; os resultados negativos exigem revisão da fonte.
Notas ou anexos de retificação posteriores ao dispositivo não o invalidam.
"""
import re
article = re.compile(r'(?im)^\s*Art(?:igo)?\.?\s*[-–—]?\s*(?:1(?:\b|[º°o])|[uú]nico\b)')
command = re.compile(r'(?im)^\s*(?:D\s*E\s*C\s*R\s*E\s*T\s*A|R\s*E\s*S\s*O\s*L\s*V\s*E(?:M)?)\s*[:.]?\s*$')
inline = re.compile(r'(?is)(?:eu\s*promulgo|Assemb(?:l[eé]ia|leia).{0,180}?\baprova\s*:|(?:D\s*E\s*C\s*R\s*E\s*T\s*A|R\s*E\s*S\s*O\s*L\s*V\s*E(?:M)?)\s*:).{0,900}?\bArt(?:igo)?\.?\s*[-–—]?\s*1(?:[º°o]|\b)')
heading = re.compile(r'(?im)^\s*(?:\(?\s*)?(?:RETIFICA[ÇC](?:[AÃ]O|[OÕ]ES)|ERRATA|RETIFICANDO|REPUBLICA[ÇC][AÃ]O)\b')
quoted = re.compile(r'(?i)\b(?:onde se l[eê]|leia-se|l[eê]-se)\b')

def verificar_integridade_texto(body):
    plain=body.replace('*','').replace('#','').replace('~~','')
    own=[m for rx in (article,inline,command) if (m:=rx.search(plain))]
    if not own:return 'sem dispositivo inicial próprio nem promulgação/comando normativo com contexto comprovado',None
    first=min(own,key=lambda m:m.start())
    before=plain[:first.start()]
    if heading.search(before):return 'epígrafe de retificação/errata antes do dispositivo próprio; revisão da íntegra necessária',None
    if quoted.search(before) and re.search(r'(?i)retific|errata',before):return 'retificação com onde-se-lê/leia-se antes de dispositivo próprio',None
    return None,plain[max(0,first.start()-80):min(len(plain),first.end()+180)]

def motivo_retencao(body):
    return verificar_integridade_texto(body)[0]
