"""Gates somente leitura para lotes de textos articulados SAPL públicos.
Versão 2: aceita também o tipo completo literal cadastrado, sem ignorar divergências anteriores.

Congela um prefixo dos diários de coleta e verifica fonte, identidade literal,
versão selecionada, dispositivos, anexos, mídias e notas. Não publica normas.
"""
import argparse
import datetime as dt
from html.parser import HTMLParser
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from auditar_epigrafes_literais_sapl import numero, normal, MESES
from epigrafe_tipo_literal_ta import analisar
from auditar_anexos_sapl import sinais
from baixar_organicas_sapl import categoria_norma
from converter_organica_fortaleza import converter, tokens
from comum import decodificar
from granularidade_sapl import alertas_outras_publicacoes
ROOT = Path(__file__).resolve().parent.parent


def sha(b):
    return hashlib.sha256(b).hexdigest()


class Contexto(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.title = []
        self.dn = 0
        self.notes = []
        self.alltext = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1' and 'page-header' in a.get('class', '').split():
            self.h1 += 1
        if tag == 'div' and ('dn' in a.get('class', '').split() or self.dn):
            self.dn += 1

    def handle_endtag(self, tag):
        if tag == 'h1' and self.h1:
            self.h1 -= 1
        if tag == 'div' and self.dn:
            self.dn -= 1

    def handle_data(self, text):
        self.alltext.append(text)
        if self.h1:
            self.title.append(text)
        if self.dn:
            self.notes.append(text)


def conferir(row, types, annexes, reference):
    np = row['prova_norma']
    raw = (ROOT / np['arquivo']).read_bytes()
    if sha(raw) != np['sha256'] or json.loads(raw) != row['metadado_norma']:
        raise ValueError('Prova da norma diverge')
    norma = row['metadado_norma']
    if numero(norma['numero']) != numero(row['metadado_ta']['numero']):
        raise ValueError('Sufixo numérico diverge entre norma e TA')
    kind = types[norma['tipo']]['descricao']
    category = categoria_norma(kind, norma)
    if category is None:
        raise ValueError('Tipo oficial não elegível')
    hp = row['prova_frontend']
    source = (ROOT / hp['arquivo']).read_bytes()
    if sha(source) != hp['sha256']:
        raise ValueError('HTML mudou')
    if hp['url_final'].rstrip('/') != f'https://{row["host"]}/ta/{row["ta_id"]}/text':
        raise ValueError('Destino padrão do TA diverge')
    html = decodificar(source, hp['content_type'])
    body, parsed = converter(html)
    candidate = (ROOT / row['transcricao']).read_bytes()
    if sha(candidate) != row['sha256_transcricao'] or candidate.decode() != body:
        raise ValueError('Transcrição candidata diverge')
    context = Contexto()
    context.feed(html)
    title = ' '.join(' '.join(context.title).split())
    identity = analisar({'tipo': kind, 'numero': norma['numero'], 'data': norma['data']}, title)
    if not identity['numero_literal_confirmado'] or not identity['data_literal_confirmada'] or identity['divergencias']:
        raise ValueError('Epígrafe literal não confirma número e data')
    if ''.join(context.notes).strip():
        raise ValueError('Nota fora dos dispositivos requer preservação contextual')
    for block in parsed.ativos:
        if re.search(r'<(?:table|img|svg|canvas|object|iframe|embed|math)\b', block['html'], re.I):
            raise ValueError('Mídia ou tabela ativa requer revisão própria')
        if re.search(r'\bcolor\s*:', block['html'], re.I):
            raise ValueError('Texto colorido ativo requer revisão contextual')
    banners = []
    text = normal(' '.join(' '.join(context.alltext).split()))
    for match in re.finditer(r'VIGENCIA A PARTIR DE (\d{1,2}) DE (\w+) DE (\d{4})', text):
        if match[2] not in MESES:
            raise ValueError('Mês de vigência desconhecido')
        date = dt.date(int(match[3]), MESES[match[2]], int(match[1]))
        if date > reference:
            raise ValueError('Versão padrão marcada com vigência futura')
        banners.append(date.isoformat())
    if annexes['estado'] != 'indice_completo':
        raise ValueError('Relação de anexos não confirmada')
    own = [a for a in annexes['anexos'] if str(a['norma']) == str(norma['id'])]
    alerts, refs = sinais(body)
    if own or alerts or refs or alertas_outras_publicacoes(body):
        raise ValueError('Anexo, remissão própria ou outra publicação exige revisão')
    return {'tipo_oficial': kind, 'categoria': category[0], 'tipo_canonico': category[1], 'titulo_literal': title,
            'tokens_ativos': len(tokens(body)), 'dispositivos_ativos': len(parsed.ativos),
            'historicos_excluidos': len(parsed.historicos), 'cortes_de_vigencia_declarados': banners,
            'anexos_proprios': 0, 'limite': 'Corte declarado é atribuído ao portal. Ausência de corte não certifica atualização nem vigência integral.'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--captura', type=Path, required=True)
    ap.add_argument('--saida', type=Path, required=True)
    ap.add_argument('--tamanho-lote', type=int, default=500)
    ap.add_argument('--referencia', type=dt.date.fromisoformat, default=dt.date.today())
    a = ap.parse_args()
    a.saida.mkdir(exist_ok=False)
    hosts = {}
    evidence = []
    types = {}
    annex = {}
    for journal in sorted(a.captura.glob('*/resultados.jsonl')):
        raw = journal.read_bytes()
        complete = raw[:raw.rfind(b'\n') + 1]
        host = journal.parent.name
        copy = a.saida / (host + '.prefixo.jsonl')
        copy.write_bytes(complete)
        evidence.append({'arquivo': str(copy), 'sha256': sha(complete), 'bytes': len(complete)})
        latest = {r['ta_id']: r for r in map(json.loads, complete.decode().splitlines())}
        hosts[host] = [r for r in latest.values() if r['estado'] == 'candidato_estruturado_para_auditoria']
        url = f'https://{host}/api/norma/tiponormajuridica/?page_size=100&page=1'
        path = ROOT / 'municipais/_indice/organicas-sapl' / host / (sha(url.encode()) + '.json')
        raw = path.read_bytes()
        source = json.loads(raw)
        if source['pagination'].get('next_page'):
            raise ValueError('Tipos oficiais incompletos')
        types[host] = {r['id']: r for r in source['results']}
        copy = a.saida / (host + '.tipos.json')
        copy.write_bytes(raw)
        evidence.append({'arquivo': str(copy), 'url': url, 'sha256': sha(raw)})
        raw = (journal.parent / 'anexos-index.json').read_bytes()
        annex[host] = json.loads(raw)
        copy = a.saida / (host + '.anexos.json')
        copy.write_bytes(raw)
        evidence.append({'arquivo': str(copy), 'sha256': sha(raw)})
    rows = []
    for group in itertools.zip_longest(*(hosts[h] for h in sorted(hosts))):
        for candidate in group:
            if not candidate:
                continue
            row = {**candidate, 'aprovado_nestes_gates': False}
            try:
                row['gates'] = conferir(candidate, types[candidate['host']], annex[candidate['host']], a.referencia)
                row['aprovado_nestes_gates'] = True
            except Exception as err:
                row['pendencia_gate'] = str(err)
            rows.append(row)
            if len(rows) >= a.tamanho_lote:
                break
        if len(rows) >= a.tamanho_lote:
            break
    (a.saida / 'resultados.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))
    receipt = {'criterio': __doc__, 'candidatos': len(rows), 'aprovados_nestes_gates': sum(r['aprovado_nestes_gates'] for r in rows), 'fontes': evidence, 'script_sha256': sha(Path(__file__).read_bytes()), 'limite': 'Não materializa normas; ainda exige prova da API do TA original, colisões e seleção final.'}
    (a.saida / 'manifesto.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2))
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == '__main__':
    main()
