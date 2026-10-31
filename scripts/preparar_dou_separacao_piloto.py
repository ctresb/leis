"""Prepara seis candidatos offline, sem aplicar alterações ao corpus do DOU."""
import argparse
import datetime as dt
import gzip
import hashlib
import html
import importlib.util
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
BASE = RAIZ / 'reguladores/_fonte/auditorias/dou-separacao-piloto-20261016'
CORE = 'bb85371750359042e0636ae0adc206cb0c353c6b6586c8d46e60a5257633ed3c'
ENTRADA = '4a11cda05bf34ce9d7f0b4519eeb592c02d9879887215ba5157d5e21906f3436'
ESPERADOS = {0: [('460', '2025-07-04'), ('461', '2025-07-04')],
             6: [('2404', '2025-06-26'), ('2403', '2025-06-26')],
             324: [('36', '2025-07-21'), ('37', '2025-07-24')]}
MESES = {'junho': 6, 'julho': 7}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def normalizar(s):
    return ' '.join(''.join(c for c in unicodedata.normalize('NFD', s.lower())
                            if not unicodedata.combining(c)).split())


def campos(md):
    cab = md.split('---', 2)[1]
    return {k: json.loads(v) if v.startswith('"') else v
            for k, v in (line.split(': ', 1) for line in cab.strip().splitlines())}


def identidade(titulo, orgao):
    t = normalizar(titulo)
    m = re.fullmatch(r'(resolucao interna anatel|resolucao-re|portaria alf dca) '
                     r'n[º°o]?\s*([\d.]+), de (\d+) de (junho|julho) de (\d{4})', t)
    if not m:
        return None
    tipo, numero, dia, mes, ano = m.groups()
    data = dt.date(int(ano), MESES[mes], int(dia)).isoformat()
    return {'tipo_especifico': tipo, 'orgao': orgao, 'numero': numero.replace('.', ''), 'data': data}


def chave(ident):
    return tuple(ident[k] for k in ('tipo_especifico', 'orgao', 'numero', 'data'))


def span(s, classe):
    m = re.search(r'<span class="' + classe + r'">(.*?)</span>', s, re.S)
    if not m:
        raise ValueError('campo de publicação ausente: ' + classe)
    return html.unescape(re.sub('<[^>]+>', '', m[1])).strip()


def gravar(path, b, auditar):
    if auditar:
        assert path.read_bytes() == b, 'replay divergente: ' + str(path)
    elif path.exists():
        assert path.read_bytes() == b, 'recusada sobrescrita: ' + str(path)
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b)


def gates(fragmento, corpo, ident, publicacao, ato):
    assert ident and ident['data'] <= publicacao, 'identidade/data inválida'
    assert ato.get('preambulo') and ato.get('assinatura') and ato.get('artigos_proprios')
    assert not re.search(r'<(?:img|svg|canvas|object|embed|iframe|math)\b', fragmento, re.I), 'visual pendente'
    assert '\x00' not in corpo and len(corpo.strip()) > 100
    n = normalizar(corpo)
    for m in re.finditer(r'\b(?:integras?|inteiro teor)\b', n):
        assert not re.search(r'dispon|biblioteca|constam|site|consult|encontr',
                             n[max(0, m.start()-80):m.end()+240]), 'íntegra externa'
    assert 'carater reservado' not in n, 'conteúdo reservado'
    assert not re.search(r'\b(?:minuta|consulta publica|sumula|aresto)\b', n), 'tipo/escopo fora do piloto'
    for tag in ('table', 'tr', 'td', 'th'):
        assert len(re.findall(r'<' + tag + r'\b', fragmento, re.I)) == len(re.findall(r'</' + tag + r'>', fragmento, re.I)), 'limite corta tabela'
    assert corpo.count('<table') == len(re.findall(r'<table\b', fragmento, re.I)), 'tabela perdida'
    return {'imagens': 'ausentes', 'integra_externa': 'ausente', 'tipo': 'permitido_no_piloto',
            'data': 'epigrafe_propria_nao_posterior_publicacao', 'tabelas': 'limites_balanceados_e_quantidade_preservada',
            'revogada': None, 'decisao': 'candidato_para_revisao_sem_aplicacao'}


def preparar(auditar=False):
    entrada = (BASE / 'entrada-revisada.json').read_bytes()
    assert sha(entrada) == ENTRADA
    corepath = BASE / f'html2md-{CORE}.py'
    assert sha(corepath.read_bytes()) == CORE
    spec = importlib.util.spec_from_file_location('dou_core_congelado', corepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    registros = json.loads(entrada)
    assert {r['id'] for r in registros} == set(ESPERADOS)
    candidatos, anteriores = [], []
    for r in registros:
        bruto = gzip.decompress((RAIZ / r['snapshot_fonte']).read_bytes())
        assert sha(bruto) == r['fonte_sha256']
        anterior = gzip.decompress((RAIZ / r['snapshot_md_anterior']).read_bytes())
        assert sha(anterior) == r['sha256_md_atual']
        assert (RAIZ / r['path']).read_bytes() == anterior, 'MD atual mudou; rever delta'
        antigos = campos(anterior.decode())
        s = bruto.decode('utf-8')
        pub = dt.datetime.strptime(span(s, 'publicado-dou-data'), '%d/%m/%Y').date().isoformat()
        orgao = span(s, 'orgao-dou-data')
        assert pub == antigos['data_publicacao'] and orgao == antigos['orgao']
        assert span(s, 'edicao-dou-data') == antigos['edicao']
        assert len(r['atos']) == 2
        anteriores.append({'path': r['path'], 'sha256_md': sha(anterior),
                           'sha256_corpo': sha(anterior.split(b'---', 2)[2]),
                           'snapshot': r['snapshot_md_anterior'], 'acao_proposta': 'substituir_apenas_apos_revisao'})
        for ordem, ato in enumerate(r['atos']):
            ini, fim = ato['html_caracteres_unicode_inicio'], ato['html_caracteres_unicode_fim_exclusivo']
            frag = s[ini:fim]
            assert sha(frag.encode()) == ato['sha256_fragmento_html_utf8']
            ident = identidade(ato['epigrafe'], orgao)
            assert (ident['numero'], ident['data']) == ESPERADOS[r['id']][ordem]
            corpo = mod.convert(frag)
            estado = gates(frag, corpo, ident, pub, ato)
            tipo = 'Portaria' if r['id'] == 324 else 'Resolução'
            meta = {'titulo': ato['epigrafe'], 'orgao': orgao, 'tipo': tipo,
                    'tipo_especifico': ident['tipo_especifico'], 'numero': ident['numero'],
                    'data': ident['data'], 'revogada': None, 'versao_texto': 'publicação original',
                    'publicacao': antigos['publicacao'], 'data_publicacao': pub, 'edicao': antigos['edicao'],
                    'fonte': r['fonte'], 'sha256_html_fonte': r['fonte_sha256'],
                    'sha256_fragmento_html': sha(frag.encode()), 'fonte_caractere_inicio': ini,
                    'fonte_caractere_fim_exclusivo': fim, 'fonte_documento_agregado': r['path'],
                    'sha256_core_html2md': CORE, 'baixado_em': antigos['baixado_em']}
            md = '---\n' + '\n'.join(k + ': ' + json.dumps(v, ensure_ascii=False) for k, v in meta.items())
            md += '\n---\n\n# ' + ato['epigrafe'] + '\n\n' + corpo
            nome = re.sub(r'[^a-z0-9]+', '-', normalizar(ato['epigrafe'])).strip('-') + '.md'
            candidato = BASE / 'candidatos' / nome
            fragmentopath = BASE / 'fragmentos' / (sha(frag.encode()) + '.html')
            gravar(candidato, md.encode(), auditar)
            gravar(fragmentopath, frag.encode(), auditar)
            proposto = r['path'] if ordem == 0 else str(Path(r['path']).parent / nome)
            candidatos.append({'id_fonte_revisada': r['id'], 'identidade': ident, 'meta': meta,
                               'path_candidato': str(candidato.relative_to(RAIZ)), 'path_proposto': proposto,
                               'sha256_md': sha(md.encode()), 'sha256_corpo': sha(md.encode().split(b'---', 2)[2]),
                               'sha256_texto_convertido': sha(corpo.encode()), 'fragmento': str(fragmentopath.relative_to(RAIZ)),
                               'fonte_snapshot': r['snapshot_fonte'], 'limites_revisados': ato, 'gates': estado})
    assert len(candidatos) == 6 and len({chave(c['identidade']) for c in candidatos}) == 6
    alvos = {chave(c['identidade']): c for c in candidatos}
    ocorrencias = []
    paths = [] if auditar else sorted((RAIZ / 'reguladores').glob('*/*/*/*.md'))
    for p in paths:
        with p.open() as f:
            inicio = f.read(16000)
        try:
            meta = campos(inicio)
        except (ValueError, IndexError, json.JSONDecodeError):
            continue
        ident = identidade(meta.get('titulo', ''), meta.get('orgao', ''))
        if not ident or chave(ident) not in alvos:
            continue
        c = alvos[chave(ident)]
        raw = p.read_bytes()
        texto = raw.decode().split('---', 2)[2].lstrip()
        texto = texto.split('\n\n', 1)[1] if texto.startswith('# ') and '\n\n' in texto else texto
        ocorrencias.append({'path': str(p.relative_to(RAIZ)), 'identidade': ident,
                            'sha256_md': sha(raw), 'sha256_texto_convertido': sha(texto.encode()),
                            'mesma_identidade_e_corpo': sha(texto.encode()) == c['sha256_texto_convertido'],
                            'decisao': 'equivalencia_exata' if sha(texto.encode()) == c['sha256_texto_convertido'] else 'mesma_identidade_texto_diferente_preservar'})
    if auditar:
        ocorrencias = json.loads((BASE / 'manifesto.json').read_text())['dedup_identidade_e_corpo']
        for item in ocorrencias:
            assert sha((RAIZ / item['path']).read_bytes()) == item['sha256_md'], 'acervo de dedup mudou'
    resultado = {'estado': 'preparado_sem_aplicar', 'escopo_fechado_ids': [0, 6, 324], 'candidatos': candidatos,
                 'anteriores_preservados': anteriores, 'dedup_identidade_e_corpo': ocorrencias,
                 'dedup_limite': 'Orgão literal da publicação; sem aliases inferidos ou supressão por corpo/URL isolados. Nenhum MD removido.',
                 'delta_proposto': {'fontes_agregadas': 3, 'candidatos': 6, 'saldo_maximo_antes_dedup': 3},
                 'core_sha256': CORE, 'entrada_sha256': ENTRADA, 'http': 0}
    gravar(BASE / 'manifesto.json', (json.dumps(resultado, ensure_ascii=False, indent=2) + '\n').encode(), auditar)
    return resultado


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--auditar', action='store_true', help='replay sem sobrescrever candidatos ou manifesto')
    args = ap.parse_args()
    result = preparar(args.auditar)
    print(json.dumps({'candidatos': len(result['candidatos']), 'aplicados': 0,
                      'http': 0, 'manifesto': str(BASE / 'manifesto.json')}, ensure_ascii=False))
