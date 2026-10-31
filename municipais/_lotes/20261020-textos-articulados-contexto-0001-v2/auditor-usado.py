"""Detecta texto e mídia normativa fora dos dispositivos contabilizados do TA.

Controle adicional somente leitura. Qualquer conteúdo não contabilizado é
retido, sem presumir que se trata de navegação ou decidir vigência por aparência.
"""
from html.parser import HTMLParser
import argparse
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
ROOT = Path(__file__).resolve().parent.parent
VOID = {'br', 'hr', 'input', 'link', 'meta', 'img', 'wbr', 'col', 'source', 'area', 'base', 'param', 'track'}
MEDIA = {'img', 'svg', 'canvas', 'object', 'iframe', 'embed', 'math', 'table'}


def sha(b):
    return hashlib.sha256(b).hexdigest()


class ContextoCompleto(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.fora = []
        self.media = []

    def classes(self):
        return set().union(*(x[1] for x in self.stack)) if self.stack else set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        c = set(a.get('class', '').split())
        ancestors = self.classes()
        if 'cp' in ancestors and 'desativado' not in ancestors and tag in MEDIA and 'dptt' not in ancestors:
            self.media.append({'tag': tag, 'attrs': a, 'posicao': self.getpos()})
        if tag not in VOID:
            self.stack.append((tag, c))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, text):
        c = self.classes()
        if 'cp' in c and 'desativado' not in c and 'dptt' not in c and not ({'tipo-vigencias', 'cp-linha-vigencias'} & c) and text.strip():
            self.fora.append({'texto': ' '.join(text.split()), 'posicao': self.getpos()})


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--materializados', type=Path, required=True)
    ap.add_argument('--saida', type=Path, required=True)
    a = ap.parse_args()
    a.saida.mkdir(exist_ok=False)
    rows = []
    for row in map(json.loads, (a.materializados / 'resultados.jsonl').read_text().splitlines()):
        if not row['aprovado']:
            continue
        hp = row['prova_frontend']
        raw = (ROOT / hp['arquivo']).read_bytes()
        if sha(raw) != hp['sha256']:
            raise ValueError('HTML mudou')
        p = ContextoCompleto()
        p.feed(raw.decode())
        norma = (ROOT / row['prova_norma']['arquivo']).read_bytes()
        if sha(norma) != row['prova_norma']['sha256']:
            raise ValueError('API da norma mudou')
        observation = json.loads(norma).get('observacao', '')
        result = {'path': row['path'], 'sha256': sha((ROOT / row['path']).read_bytes()), 'sha256_fonte': sha(raw), 'fonte': hp['arquivo'], 'texto_fora_dos_dispositivos': p.fora, 'midia_fora_dos_dispositivos': p.media, 'observacao_api': observation, 'aprovado_neste_gate': not p.fora and not p.media and not observation}
        rows.append(result)
    for name, accepted in [('aprovados', True), ('retidos', False)]:
        (a.saida / (name + '.paths.txt')).write_text(''.join(r['path'] + '\n' for r in rows if r['aprovado_neste_gate'] == accepted))
    result = {'criterio': __doc__, 'aprovados': sum(r['aprovado_neste_gate'] for r in rows), 'retidos': sum(not r['aprovado_neste_gate'] for r in rows), 'script_sha256': sha(Path(__file__).read_bytes()), 'resultados': rows, 'limite': 'Texto fora do bloco pode ser histórico, alterado ou duplicado; retenção é preventiva, sem afirmar omissão antes de revisão. Os controles de seleção de vigência e de tokens por dispositivo continuam necessários.'}
    (a.saida / 'controle.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({'aprovados': result['aprovados'], 'retidos': result['retidos']}))


if __name__ == '__main__':
    main()
