"""Inventário literal dos candidatos retidos por cor; não qualifica nem materializa.

Lê somente os snapshots indicados. Não deduz vigência, não remove cores e não
consulta folhas externas. As categorias são descritivas do markup, sem dispensar
os gates V7, API, identidade, conteúdo, tabelas ou renderização.
"""
from pathlib import Path
import argparse
import collections
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / 'scripts/bin/qa-20261027/python'),
               str(ROOT / 'scripts/bin/qa-confaz-20261027/python'), str(ROOT / 'scripts')]
from lxml import html
import tinycss2
from converter_organica_fortaleza import Dispositivos


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def inventario(source):
    selected = Dispositivos()
    selected.feed(source)
    selected.close()
    if selected.atual or not selected.ativos:
        raise ValueError('Seleção de dispositivos incompleta')
    document = html.fromstring(source)
    external = [dict(e.attrib) for e in document.iter('link')
                if 'stylesheet' in e.get('rel', '').lower().split()]
    entries = []
    for block in selected.ativos:
        doc = html.fromstring(block['html'])
        for element in doc.iter():
            if not isinstance(element.tag, str):
                continue
            attributes = dict(element.attrib)
            declarations = []
            for declaration in tinycss2.parse_declaration_list(
                    element.get('style', ''), skip_comments=True, skip_whitespace=True):
                if declaration.type == 'error':
                    raise ValueError('Declaração CSS inválida no dispositivo ' + str(block['id']))
                if declaration.type == 'declaration' and 'color' in declaration.lower_name:
                    declarations.append(dict(propriedade=declaration.lower_name,
                                             valor=tinycss2.serialize(declaration.value),
                                             important=declaration.important))
            legacy = {k: v for k, v in attributes.items() if k.lower() in {'color', 'bgcolor'}}
            if declarations or legacy:
                entries.append(dict(dispositivo=block['id'], tag=element.tag,
                                    atributos_literais=attributes,
                                    texto_descendente=''.join(element.itertext()),
                                    declaracoes=declarations, atributos_cor=legacy))
    return dict(ocorrencias=entries, folhas_externas_nao_consultadas=external,
                estilos_embutidos=[e.text or '' for e in document.iter('style')],
                dispositivos_ativos=[b['id'] for b in selected.ativos],
                historicos_desativados=[b['id'] for b in selected.historicos])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--gates', type=Path, required=True)
    ap.add_argument('--saida', type=Path, required=True)
    args = ap.parse_args()
    args.gates = args.gates.resolve()
    args.saida = args.saida.resolve()
    rows = [json.loads(line) for line in args.gates.read_text().splitlines()]
    chosen = [r for r in rows if r.get('pendencia_gate') == 'Texto colorido ativo requer revisão contextual']
    result = []
    for row in chosen:
        proof = row['prova_frontend']
        raw = (ROOT / proof['arquivo']).read_bytes()
        if sha(raw) != proof['sha256']:
            raise ValueError('Fonte alterada: ' + proof['arquivo'])
        details = inventario(raw.decode('utf-8'))
        if not details['ocorrencias']:
            raise ValueError('Predicado anterior sem ocorrência literal reproduzida')
        result.append(dict(host=row['host'], ta_id=row['ta_id'], norma_id=row['norma_id'],
                           codigo_ibge=row['codigo_ibge'], fonte=proof, API=row['prova_norma'],
                           pendencia_original=row['pendencia_gate'], **details))
    properties = collections.Counter()
    for row in result:
        for entry in row['ocorrencias']:
            properties.update((d['propriedade'], d['valor']) for d in entry['declaracoes'])
            properties.update(('atributo:' + k, v) for k, v in entry['atributos_cor'].items())
    args.saida.mkdir(exist_ok=False, parents=True)
    output = args.saida / 'inventario.json'
    output.write_text(json.dumps(dict(normas=len(result),
        propriedades=[dict(propriedade=k[0], valor=k[1], ocorrencias=n) for k, n in properties.most_common()],
        candidatas_qualificadas=0, canonicos_alterados=0, registros=result,
        limite='Inventário literal, sem cascata de cor calculada. Folhas externas não consultadas. '
               'A presença de uma cor, inclusive vermelha, não determina vigência ou revogação. '
               'Preservar atributos é necessário, mas não comprova sua renderização no GitHub.'),
        ensure_ascii=False, indent=2) + '\n')
    files = [args.gates.resolve(), output, Path(__file__).resolve()]
    for row in result:
        files.extend([ROOT / row['fonte']['arquivo'], ROOT / row['API']['arquivo']])
    files = sorted(set(files))
    manifesto = dict(normas=len(result), candidatas_qualificadas=0,
        arquivos=[dict(arquivo=str(p.relative_to(ROOT)), sha256=sha(p.read_bytes()), bytes=p.stat().st_size) for p in files])
    manifest = args.saida / 'manifesto.json'
    manifest.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(normas=len(result), candidatas_qualificadas=0,
                         manifesto=str(manifest.relative_to(ROOT)), sha256=sha(manifest.read_bytes()))))


if __name__ == '__main__':
    main()
