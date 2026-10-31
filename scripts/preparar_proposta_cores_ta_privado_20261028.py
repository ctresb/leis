"""Congela experimento de cores em cópias TXT; nenhum candidato é qualificado."""
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from propor_cores_html_ta_privado_20261028 import propor
from inventariar_cores_ta_privado_20261028 import sha


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--gates', type=Path, required=True)
    ap.add_argument('--saida', type=Path, required=True)
    args = ap.parse_args()
    args.gates = args.gates.resolve()
    out = args.saida.resolve()
    out.mkdir(exist_ok=False)
    files = {}

    def add(path):
        raw = path.read_bytes()
        result = dict(arquivo=str(path.relative_to(ROOT)), sha256=sha(raw), bytes=len(raw))
        files[result['arquivo']] = result
        return result

    add(args.gates)
    rows = [json.loads(x) for x in args.gates.read_text().splitlines()]
    results = []
    for row in rows:
        if row.get('pendencia_gate') != 'Texto colorido ativo requer revisão contextual':
            continue
        proof = row['prova_frontend']
        source_path = ROOT / proof['arquivo']
        source = source_path.read_bytes()
        if sha(source) != proof['sha256']:
            raise ValueError('SHA da fonte diverge')
        add(source_path)
        add(ROOT / row['prova_norma']['arquivo'])
        result = dict(host=row['host'], ta_id=row['ta_id'], norma_id=row['norma_id'],
                      fonte=proof, API=row['prova_norma'], apto_para_publicacao=False)
        try:
            body, replay = propor(source.decode('utf-8'))
            name = out / (row['host'] + '-' + str(row['ta_id']) + '.html.txt')
            with name.open('x') as stream:
                stream.write(body)
            result.update(experimento_reproduzido=True, copia_privada=add(name), prova=replay,
                          pendencia='Representação local comprovada, mas CSS externo/GitHub e gates de materialização não qualificados')
        except ValueError as error:
            result.update(experimento_reproduzido=False, pendencia=str(error))
        results.append(result)
    report = out / 'resultados.json'
    report.write_text(json.dumps(dict(normas=len(results),
        experimentos_reproduzidos=sum(r['experimento_reproduzido'] for r in results),
        candidatas_qualificadas=0, canonicos_alterados=0, resultados=results,
        limite='Experimento local explicitamente não publicável. Mantém todas as retenções originais e não substitui o perfil V7.'),
        ensure_ascii=False, indent=2) + '\n')
    add(report)
    for module in ['preparar_proposta_cores_ta_privado_20261028.py', 'propor_cores_html_ta_privado_20261028.py',
                   'test_propor_cores_html_ta_privado_20261028.py', 'inventariar_cores_ta_privado_20261028.py',
                   'test_inventariar_cores_ta_privado_20261028.py', 'perfil_ta_tachados_preservados_20261027.py',
                   'representacao_html_dou_v2.py', 'representacao_html_dou.py', 'converter_organica_fortaleza.py',
                   'conferir_tabelas_nativas_ta.py', 'auditar_commonmark_ta_v2.py',
                   'diagnosticar_css_glifos_ta_20261027.py', 'estados/pe_fidelidade_visivel.py']:
        add(ROOT / 'scripts' / module)
    manifest = out / 'manifesto.json'
    manifest.write_text(json.dumps(dict(normas=len(results), candidatas_qualificadas=0,
        arquivos=sorted(files.values(), key=lambda r: r['arquivo'])), ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(manifesto=str(manifest.relative_to(ROOT)), sha256=sha(manifest.read_bytes()),
                         normas=len(results), experimentos_reproduzidos=sum(r['experimento_reproduzido'] for r in results),
                         candidatas_qualificadas=0)))


if __name__ == '__main__':
    main()
