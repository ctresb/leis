"""Repara textos Intermediate antigos sem apagar a publicação substituída.

Prepara candidatos e fontes imutáveis; --aplicar só troca arquivos cuja preimagem
continua idêntica. Não afirma atualização quando a API só oferece Original.
O renderizador deve receber Markdown em stdin e devolver HTML em stdout.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime as dt
import gzip
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import urllib.parse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import baixar_federal as federal
from integridade_html_federal import Visivel

ROOT = Path(__file__).resolve().parent.parent
VERSION = 'republicação/retificação'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def metadados(raw):
    text = raw.decode('utf-8')
    head, rest = text.split('\n---\n', 1)
    meta = {}
    for line in head.splitlines():
        if ': ' in line:
            k, v = line.split(': ', 1)
            try:
                meta[k] = json.loads(v)
            except ValueError:
                meta[k] = v
    return meta, head, rest


def texto_visivel(html):
    parser = Visivel()
    parser.feed(html)
    return re.sub(r'\s+', '', ''.join(parser.data).lstrip('\ufeff')), parser


def texto_tachado(html):
    class Tachados(HTMLParser):
        def __init__(self):
            super().__init__()
            self.stack = []
            self.text = []

        def handle_starttag(self, tag, attrs):
            if tag in {'br', 'hr', 'meta', 'link', 'img', 'input', 'wbr', 'col'}:
                return
            style = dict(attrs).get('style') or ''
            active = (bool(self.stack and self.stack[-1][1]) or tag in {'s', 'strike', 'del'}
                      or 'line-through' in style.lower())
            self.stack.append((tag, active))

        def handle_endtag(self, tag):
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break

        def handle_data(self, data):
            if self.stack and self.stack[-1][1]:
                self.text.append(data)
    parser = Tachados()
    parser.feed(html)
    return re.sub(r'\s+', '', ''.join(parser.text))


def validar(meta, api, enc, html, markdown, rendered):
    if api.get('legislationIdentifier') != meta.get('urn'):
        raise ValueError('URN dos metadados diverge do documento')
    if enc.get('version') not in {'Current', 'Original'}:
        raise ValueError('fonte só oferece publicação intermediária')
    visible, parser = texto_visivel(html)
    if parser.visual:
        raise ValueError('conteúdo visual exige revisão: ' + str(parser.visual))
    if re.search(r'<style\b[^>]*>.*?(?:line-through|display\s*:\s*none|Wingdings|Symbol)', html, re.I | re.S):
        raise ValueError('CSS com semântica exige revisão específica')
    rendered_text, rendered_parser = texto_visivel(rendered)
    if visible != rendered_text:
        raise ValueError('texto/pontuação divergem entre HTML oficial e Markdown renderizado')
    if parser.structure != rendered_parser.structure:
        raise ValueError('estrutura das tabelas diverge da fonte')
    if texto_tachado(html) != texto_tachado(rendered):
        raise ValueError('tachados divergem da fonte')
    plain = re.sub(r'[*_`\\]', '', markdown)
    article = re.search(r'^\s*(?:Art\.?|Artigo)\s*1(?:[º°o.]|\s)', plain, re.I | re.M)
    if not article:
        raise ValueError('sem artigo 1 próprio reconhecível')
    prefix = plain[:article.start()]
    if re.search(r'partes\s+vetadas|^\s*RETIFICA[ÇC][ÃA]O\s*$', prefix, re.I | re.M):
        raise ValueError('retificação ou promulgação de partes vetadas avulsa')
    epigraph = re.search(r'\bLEI\s+(?:COMPLEMENTAR\s+)?N[º°o.\s]*([\d.]+)', prefix, re.I)
    if not epigraph or epigraph[1].rstrip('.').replace('.', '') != str(meta['numero']).replace('.', ''):
        raise ValueError('número da epígrafe própria diverge')


def guardar(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != raw:
            raise ValueError('artefato imutável já existe com outros bytes: ' + str(path))
    else:
        path.write_bytes(raw)


def preparar(path, output, renderer, cache=None):
    raw = path.read_bytes()
    meta, head, rest = metadados(raw)
    if meta.get('versao_texto') != VERSION:
        return {'arquivo': str(path.relative_to(ROOT)), 'status': 'pulado'}
    body = rest.lstrip('\n').split('\n\n', 1)[1]
    if federal.motivo_texto_parcial_norma('LEI-n', body) is None:
        return {'arquivo': str(path.relative_to(ROOT)), 'status': 'pulado',
                'motivo': 'artigo inicial próprio reconhecido; rótulo Intermediate não prova erro'}
    identity = sha(meta['urn'].encode())
    folder = output / identity
    guardar(folder / 'anterior.md', raw)
    api_url = federal.API_NORMA.format(urllib.parse.quote(meta['urn'], safe=':;@!~$-.'))
    cached = cache / identity if cache else None
    if cached and (cached / 'metadados.json').exists():
        status, api_raw = 200, (cached / 'metadados.json').read_bytes()
    else:
        status, api_raw = federal.http_get(api_url, 'application/json', tentativas=2)
    if status != 200:
        raise ValueError('HTTP dos metadados: ' + str(status))
    guardar(folder / 'metadados.json', api_raw)
    api = json.loads(api_raw)
    enc = federal.escolher_texto(api)
    if not enc or enc.get('version') not in {'Current', 'Original'}:
        raise ValueError('sem versão Current ou Original')
    url = enc['contentUrl'].replace('/api/binario/', '/api/public/binario/')
    if cached and (cached / 'fonte.html.gz').exists():
        status, html_raw = 200, gzip.decompress((cached / 'fonte.html.gz').read_bytes())
    else:
        status, html_raw = federal.http_get(url, 'text/html', tentativas=2)
    if status != 200 or html_raw.startswith(b'%PDF'):
        raise ValueError('texto não é HTML disponível: HTTP ' + str(status))
    guardar(folder / 'fonte.html.gz', gzip.compress(html_raw, mtime=0))
    html = html_raw.decode('utf-8-sig')
    body = federal.convert(html, preserve_heading_punctuation=True)
    # O conversor geral remove o identificador técnico do Senado. Nesta revisão
    # ele é mantido literalmente para permitir comparação sem mascarar caracteres.
    code = re.match(r'\s*(###[A-Z0-9-]+@@@)', ''.join(texto_visivel(html)[1].data).lstrip('\ufeff'))
    if code:
        body = '\\#\\#\\#' + code[1][3:] + '\n\n' + body
    rendered = subprocess.run(renderer, input=body, text=True, capture_output=True, check=True).stdout
    validar(meta, api, enc, html, body, rendered)
    version = {'Current': 'compilada (texto vigente)', 'Original': 'original'}[enc['version']]
    head = re.sub(r'^versao_texto:.*$', 'versao_texto: ' + json.dumps(version), head, flags=re.M)
    # O status jurídico anterior não foi revalidado por esta operação.
    head = re.sub(r'^revogada:.*$', 'revogada: null', head, flags=re.M)
    extras = {
        'fonte_texto': url,
        'sha256_fonte': sha(html_raw),
        'fonte_metadados': api_url,
        'sha256_metadados_fonte': sha(api_raw),
        'texto_reparado_em': dt.date.today().isoformat(),
        'publicacao_intermediaria_preservada': str((folder / 'anterior.md').relative_to(ROOT)),
        'observacao_edicao': ('Versão original integral; alterações, retificações e partes vetadas posteriores não foram incorporadas. '
                             'A publicação intermediária anterior permanece preservada para consulta.' if version == 'original'
                             else 'Publicação intermediária anterior preservada separadamente para consulta.'),
    }
    for key, value in extras.items():
        line = key + ': ' + json.dumps(value, ensure_ascii=False)
        if re.search(r'^' + key + ':', head, re.M):
            head = re.sub(r'^' + key + ':.*$', lambda _: line, head, flags=re.M)
        else:
            head += '\n' + line
    title = rest.lstrip('\n').split('\n\n', 1)[0]
    new = (head + '\n---\n' + title + '\n\n' + body.rstrip() + '\n').encode()
    guardar(folder / 'candidato.md', new)
    return {'arquivo': str(path.relative_to(ROOT)), 'status': 'preparado', 'versao': version,
            'sha256_anterior': sha(raw), 'sha256_novo': sha(new), 'sha256_fonte': sha(html_raw),
            'pasta': str(folder.relative_to(ROOT))}


def aplicar(rows):
    prepared = []
    for row in rows:
        if row['status'] != 'preparado':
            continue
        path = ROOT / row['arquivo']
        folder = ROOT / row['pasta']
        new = (folder / 'candidato.md').read_bytes()
        if sha(path.read_bytes()) != row['sha256_anterior'] or sha(new) != row['sha256_novo']:
            raise ValueError('preimagem ou candidato mudou: ' + row['arquivo'])
        if sha((folder / 'anterior.md').read_bytes()) != row['sha256_anterior']:
            raise ValueError('backup diverge')
        prepared.append((path, new))
    for path, new in prepared:
        temp = path.with_suffix('.md.reparo.tmp')
        temp.write_bytes(new)
        temp.replace(path)
    return len(prepared)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--lista', type=Path)
    ap.add_argument('--saida', type=Path, required=True)
    ap.add_argument('--renderizador', nargs='+')
    ap.add_argument('--aplicar', action='store_true')
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--rps', type=float, default=4)
    ap.add_argument('--cache', type=Path, help='reutiliza as capturas imutáveis de uma preparação anterior')
    args = ap.parse_args()
    manifest = args.saida / 'manifesto.json'
    if args.aplicar:
        rows = json.loads(manifest.read_text())['documentos']
        n = aplicar(rows)
        guardar(args.saida / 'aplicacao.json', json.dumps({'aplicados': n, 'manifesto_sha256': sha(manifest.read_bytes())}, indent=2).encode())
        print('Aplicados:', n)
        return
    if not args.lista or not args.renderizador:
        ap.error('preparação exige --lista e --renderizador')
    args.saida.mkdir(parents=True, exist_ok=False)
    federal.LIMITE = federal.Limitador(args.rps)
    paths = [ROOT / p for p in args.lista.read_text().splitlines() if p]
    rows = []
    with ThreadPoolExecutor(args.workers) as pool:
        futures = {pool.submit(preparar, p, args.saida, args.renderizador, args.cache): p for p in paths}
        for future in as_completed(futures):
            try:
                row = future.result()
            except Exception as error:
                row = {'arquivo': str(futures[future].relative_to(ROOT)), 'status': 'retido', 'motivo': str(error)}
            rows.append(row)
            manifest.write_text(json.dumps({'documentos': sorted(rows, key=lambda r: r['arquivo'])}, ensure_ascii=False, indent=2))
            if len(rows) % 25 == 0 or len(rows) == len(paths):
                print(json.dumps({'processados': len(rows), 'total': len(paths), 'preparados': sum(r['status'] == 'preparado' for r in rows)}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
