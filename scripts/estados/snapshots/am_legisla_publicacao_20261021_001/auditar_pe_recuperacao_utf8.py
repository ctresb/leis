"""Recuperação privada, a partir de cache UTF-8 comprovado, de MD PE com mojibake.

Não toca documentos reais. Cada candidato exige identidade própria, comparação
CommonMark integral, pontuação/sinais e matrizes das tabelas. Casos sem prova ou
com sinais de íntegra pendente permanecem retidos; a conversão não os libera.
"""
import argparse
import collections
import datetime as dt
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from markdown_it import MarkdownIt
from comum import html_para_md
from pe import limites_texto_html, TIPOS
from pe_fidelidade_visivel import texto_visivel_html, _heading_comprovado, assinatura_numerica
from auditar_pe_commonmark_contexto import Counters
from auditar_pe_cache import MONTH, APP, FOREIGN
from integridade_texto import verificar_integridade_texto
from avisos_fonte import avisos_de_omissao
from anexos_fonte import remissoes_sem_representacao
from tabelas_estrutura import _Tabelas

SHA = lambda b: hashlib.sha256(b).hexdigest()
SINAL = re.compile(r'NÂ[º°]|[Aa]rt\.?\s*\d+Â[º°]|ConstituiÃ§Ã£o|aÃ§Ã£o')
TIPO = {'Lei Ordinária': r'LEI(?!\s+COMPLEMENTAR)', 'Lei Complementar': r'LEI\s+COMPLEMENTAR',
        'Decreto-Lei': r'DECRETO\s*[-–]?\s*LEI', 'Emenda Constitucional': r'EMENDA\s+CONSTITUCIONAL'}
MESES_LITERAL = dict(MONTH, **{'agôsto': 8})  # grafia histórica, não correção de OCR
PARSER = MarkdownIt('commonmark', {'html': True}).enable('table')


def metadados(texto):
    out = {}
    for linha in texto.split('\n---\n', 1)[0].splitlines():
        k, sep, v = linha.partition(':')
        if sep:
            try: out[k] = json.loads(v.strip())
            except ValueError: out[k] = v.strip()
    return out


def matrizes(html):
    p = _Tabelas(); p.feed(html); p.close()
    if p.pilha:
        raise ValueError('tabela sem fechamento')
    return [[dict(linha=c['linha'], rowspan=c['rowspan'], colspan=c['colspan'],
                  texto=' '.join(''.join(c['texto']).split())) for c in t['celulas']]
            for t in p.tabelas if t['linha'] > 1]


def candidato(raw, fonte):
    """Bytes finais e provas. Charset não é inferido por substituição de nomes."""
    antigo = raw.decode('utf-8'); meta = metadados(antigo)
    if not SINAL.search(antigo):
        raise ValueError('sem sinal explícito de dupla decodificação')
    pagina = fonte.decode('utf-8', 'strict')
    if '\ufffd' in pagina:
        raise ValueError('cache já contém caractere de substituição')
    limites = limites_texto_html(pagina, fragmento='id="divTexto"' not in pagina)
    if not limites:
        raise ValueError('campo normativo sem limite')
    field = pagina[limites[0]:limites[1]]
    # Caches antigos são fragmentos Word: a representação UTF-8 do cache não
    # deve ser reinterpretada pela declaração windows-1252 interna do Word.
    if 'id="divTexto"' not in pagina and not re.search(r'</body\s*>.*?</html\s*>', field, re.I | re.S):
        raise ValueError('fragmento Word sem body/html fechados')
    if re.search(r'<(?:img|svg|canvas|object|embed|iframe|script|s|strike|del|math|v:\w+|m:oMath)\b|\bon\w+\s*=|javascript\s*:|line-through|display\s*:\s*none|visibility\s*:\s*hidden|mso-hide\s*:\s*all|opacity\s*:\s*0(?:[;\s\"\']|$)|font-size\s*:\s*0(?:px|pt|em|rem|[;\s])|color\s*:\s*transparent|\bhidden(?:\s|=|>)|Wingdings|Webdings|class\s*=\s*["\'][^"\']*(?:tachad|revogad|riscad|desativad|deleted)', field, re.I):
        raise ValueError('visual/ativo/tachado/ocultação exige contexto')
    if re.search(r'line-through|display\s*:\s*none|visibility\s*:\s*hidden|mso-hide\s*:\s*all|opacity\s*:\s*0(?:[;\s\"\']|$)|font-size\s*:\s*0(?:px|pt|em|rem|[;\s])|color\s*:\s*transparent|Wingdings|Webdings', pagina, re.I):
        raise ValueError('regra CSS potencialmente histórica/oculta exige contexto')
    if re.search(r'<(?:ol|ul)\b', field, re.I):
        raise ValueError('lista HTML nativa exige associação contextual')
    source = texto_visivel_html(field)
    typ = TIPO.get(meta.get('tipo'))
    if not typ:
        raise ValueError('tipo fora do escopo')
    ep = re.match(typ + r'\s+N[º°o.\s]*([\d.]+(?:\s*-\s*[A-Za-z]+)?)\s*,?\s*DE\s+(\d{1,2})[º°o]?\s+DE\s+(\w+)\s+DE\s+(\d{4})\b', source, re.I)
    if not ep:
        raise ValueError('epígrafe própria não comprovada')
    normal = lambda n: re.sub(r'[.\s]', '', str(n)).lstrip('0').upper()
    if normal(ep[1]) != normal(meta['numero']):
        raise ValueError('número da epígrafe diverge; não renumerar silenciosamente')
    data = dt.date(int(ep[4]), MESES_LITERAL[ep[3].lower()], int(ep[2])).isoformat()
    if data > dt.datetime.now(ZoneInfo('America/Recife')).date().isoformat() or (meta.get('ano') not in (None, '', 'sem-ano') and str(meta['ano']) != data[:4]):
        raise ValueError('data/ano não comprovados')
    if meta.get('data') and meta['data'] != data:
        raise ValueError('data antiga diverge da epígrafe')
    body = html_para_md(field)
    issue, dispositivo = verificar_integridade_texto(body)
    if issue:
        raise ValueError(issue)
    if avisos_de_omissao(body) or remissoes_sem_representacao(body):
        raise ValueError('aviso/remissão própria não representada exige contexto')
    if re.search(r'\banex[oa]s?\s+(?:[úu]nic[oa]s?\s+|[IVXLC0-9]+\s+)?(?:desta|deste|a\s+esta|a\s+este|[àa]\s+presente)\b', source, re.I) and not re.search(r'(?im)^\s*[#*\s]*ANEXO\b', body):
        raise ValueError('anexo próprio sem título representado exige contexto')
    if APP.search(source) and not re.search(r'(?im)^\s*[#*\s]*(?:ANEXO|REGULAMENTO|REGIMENTO|ESTATUTO|PLANO|MANUAL)\b', body):
        raise ValueError('objeto aprovado próprio exige contexto')
    if any(normal(m[2]) != normal(meta['numero']) for m in FOREIGN.finditer(body.replace('*', ''))):
        raise ValueError('outra epígrafe exige revisão de granularidade')
    tokens = PARSER.parse(body); lists = [dict(start=t.attrGet('start') or 1, markup=t.markup, linhas=t.map) for t in tokens if t.type == 'ordered_list_open']
    rendered = PARSER.render(body); counters = Counters(lists); counters.feed(rendered)
    visible, headings = _heading_comprovado(texto_visivel_html(''.join(counters.out)), body, source)
    if visible != source or assinatura_numerica(visible) != assinatura_numerica(source):
        raise ValueError('CommonMark integral/sinais não confere')
    tables = matrizes(field)
    if tables != matrizes(rendered):
        raise ValueError('células/ordem/spans/textos de tabela não conferem')
    pre, priorbody = antigo.split('\n---\n', 1); h1 = next(l for l in priorbody.splitlines() if l.startswith('# '))
    pre = re.sub(r'(?m)^data:.*$', 'data: '+json.dumps(data), pre)
    if re.search(r'(?m)^ano:', pre):
        pre = re.sub(r'(?m)^ano:.*$', 'ano: '+json.dumps(data[:4]), pre)
    else:
        pre += '\nano: '+json.dumps(data[:4])
    new = (pre+'\n---\n'+h1+'\n\n'+body.strip()+'\n').encode('utf-8')
    if re.search(rb'(?m)^[<=>]{7}(?: |$)|[\t ]+$', new) or b'\r' in new:
        raise ValueError('formatação Markdown exige representação separada')
    return new, dict(epigrafe_literal=ep[0], data=data, sha256_campo=SHA(field.encode()),
                     dispositivo_proprio=dispositivo, igualdade_visivel_CommonMark=True,
                     assinatura_numerica_sinais=True, tabelas_multilinhas=len(tables),
                     normalizacoes_heading=headings, listas=counters.proofs,
                     encoding='Cache UTF-8 estrito, sem substituições; declaração Word interna não muda os bytes da representação preservada.',
                     limites_campo=limites)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inventario', required=True); ap.add_argument('--lote', required=True)
    ap.add_argument('--limite', type=int, default=1000); ap.add_argument('--anterior', action='append', default=[])
    args = ap.parse_args()
    if not 1 <= args.limite <= 2000 or not re.fullmatch(r'\d{8}-\d{3}', args.lote):
        ap.error('lote AAAAMMDD-NNN e limite 1–2000')
    root = Path(__file__).resolve().parents[2]
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    tree = subprocess.check_output(['git', 'ls-tree', '-r', head, '--', 'estaduais/PE/emendas-constitucionais', 'estaduais/PE/leis-complementares', 'estaduais/PE/decretos-lei', 'estaduais/PE/leis-ordinarias'], text=True)
    blobs = {l.split('\t')[1]: l.split()[2] for l in tree.splitlines()}
    prior = set()
    for p in args.anterior:
        prior.update(r['path'] for r in json.loads(Path(p).read_text())['selecionados'])
    catalog = {r['id']: r for r in json.loads((root/'estaduais/PE/_indice/lista.json').read_text())}
    order = {'emendas-constitucionais': 0, 'leis-complementares': 1, 'decretos-lei': 2, 'leis-ordinarias': 3}
    rows = [r for r in json.loads(Path(args.inventario).read_text())['documentos'] if r['path'] not in prior and r['path'] in blobs and not r['path'].endswith(('-id74626.md', '-id76757.md'))]
    rows.sort(key=lambda r: (order[r['path'].split('/')[2]], r['path']))
    rows = rows[:args.limite]; selected = []; accepted = []; held = []; reasons = collections.Counter()
    name = 'pe-recuperacao-utf8-'+args.lote; base = root/'estaduais/PE/_fonte/auditorias'/name
    manifest = root/'scripts/estados/manifestos'/(name+'.json')
    if base.exists() or manifest.exists():
        raise FileExistsError('lote já existe')
    base.mkdir(parents=True)
    for i, row in enumerate(rows, 1):
        path = row['path']; r = dict(path=path, sha256_MD_inventario=row['sha256_md']); selected.append(r)
        try:
            raw = (root/path).read_bytes(); assert SHA(raw) == row['sha256_md'], 'MD mudou desde inventário'
            assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == blobs[path], 'worktree diverge HEAD'
            meta = metadados(raw.decode()); ident = re.search(r'[?&]id=(\d+)', meta['fonte'])[1]; item = catalog[ident]
            num = re.search(r'n[°º]\s*([\d.]+(?:-[A-Za-z]+)?)', item['nome'])[1]
            assert re.sub(r'[.\s]', '', num).upper() == re.sub(r'[.\s]', '', meta['numero']).upper(), 'número índice diverge'
            assert TIPOS[item['tipo']][1] == meta['tipo'], 'tipo índice diverge'
            assert not item.get('ano') or item['ano'] == meta.get('ano'), 'ano índice diverge'
            z = (root/row['cache']).read_bytes(); fonte = gzip.decompress(z); new, proof = candidato(raw, fonte)
            backup = base/'HEAD-preimagem'/Path(path+'.gz'); backup.parent.mkdir(parents=True, exist_ok=True); backup.write_bytes(gzip.compress(raw))
            body = raw.decode().split('\n---\n', 1)[1].encode(); bodybackup = base/'body-preimagem'/Path(path+'.gz'); bodybackup.parent.mkdir(parents=True, exist_ok=True); bodybackup.write_bytes(gzip.compress(body))
            year = proof['data'][:4]
            destino = path.replace('/sem-ano/', '/'+year+'/').replace('-sem-ano-', '-'+year+'-')
            if destino != path:
                assert destino not in blobs and not (root/destino).exists(), 'destino canônico já existe'
            dest = base/'candidatos'/Path(destino+'.gz'); dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(gzip.compress(new))
            r.update(destino_canonico=destino, exige_rename_atomico=destino != path, sha256_HEAD=SHA(raw), git_blob_HEAD=blobs[path], fonte=meta['fonte'], id_oficial=ident,
                     cache=row['cache'], sha256_cache=SHA(z), sha256_fonte=SHA(fonte), backup=str(backup.relative_to(root)),
                     sha256_backup=SHA(backup.read_bytes()), body_preimagem=str(bodybackup.relative_to(root)), sha256_body_preimagem=SHA(body),
                     candidato_privado=str(dest.relative_to(root)), sha256_candidato=SHA(new), sha256_candidato_gz=SHA(dest.read_bytes()), QA=proof)
            accepted.append(r)
        except Exception as e:
            r['motivo'] = type(e).__name__+': '+str(e); held.append(r); reasons[r['motivo']] += 1
        if i % 100 == 0:
            print('PROGRESSO', i, 'aceitos', len(accepted), 'retidos', len(held), flush=True)
    obj = dict(auditado_em=dt.datetime.now(ZoneInfo('America/Recife')).isoformat(), HEAD_commit=head,
               sha256_arvore_HEAD=SHA(tree.encode()), codigo_auditor=str(Path(__file__).relative_to(root)), sha256_codigo_auditor=SHA(Path(__file__).read_bytes()), rede=0, MD_reais_modificados=0, total_selecionado=len(rows),
               total_candidatos_privados=len(accepted), total_retido=len(held), selecionados=selected,
               candidatos=accepted, retidos=held, motivos=dict(reasons),
               criterio='Reparos privados de publicados com prova de bytes UTF-8 da fonte/cache e preimagem HEAD. Identidade índice/epígrafe/data/tipo, íntegra/visuais/tachados/objetos conservadores, CommonMark e sinais integrais, matrizes de tabelas. Data/ano antes vazios são preenchidos somente pela epígrafe comprovada; paths sem-ano têm destino privado explícito para rename atômico; resto do metadata/H1 preservado, corpo reextraído da mesma fonte. Não modifica MD reais nem presume vigência.')
    manifest.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
    Path('/tmp/'+name+'-paths.txt').write_text(str(manifest.relative_to(root))+'\n')
    Path('/tmp/'+name+'-hashes.json').write_text(json.dumps({str(manifest.relative_to(root)): SHA(manifest.read_bytes())}, indent=2)+'\n')
    print('FINAL', len(rows), len(accepted), len(held), dict(reasons), flush=True)


if __name__ == '__main__':
    main()
