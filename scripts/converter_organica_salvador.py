"""Transcreve a edição oficial de Salvador de 2024, com prova integral por página.

Preserva capa, notas, ADCT, fólios e números. Uma nota (36) fora de posição na
extração é recolocada antes do inciso III conforme prova visual da página 47.
"""
import collections
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import yaml_str
ROOT = Path(__file__).resolve().parent.parent
PDF = Path('municipais/_fonte/capitais/salvador/lei-organica-consolidada-41-2024.pdf')
SOURCE_SHA = 'b98d10caff6d3f9ef053b101622f6d107b4ceda01c3a0cae9f187d3ca85f9598'
VISUAL_PAGES = {2, 39, 47, 64}
VISUAL_SHA = {
    2: 'f10308e7fb7efe58d190202167c93796ba83791f1fd42c0e6cc6a0b33630bb3a',
    39: 'f374157ab536811d159bba894db3d7c005d5a523cc32747deec75f0ce08134ec',
    47: 'caaae3e4764e374853fc8ae087daa23b9e5a14ebe712af84bf7fb32438e40421',
    64: '57ed715765fa7428f6e94c27106f7fe3a35f539bb691b2c24cb962deaaec673a',
}
PREIMAGE_CANDIDATE = 'b204ba9517ded8577db8409451e40723f44357ae6465151fe988b86b8f3a522b'
OLD_MARKER = '         III – aos 61 (sessenta e um) anos de idade, se mulher, e aos 64 (sessenta e\n      (36)\n\nquatro)'
NEW_MARKER = '      (36)\n         III – aos 61 (sessenta e um) anos de idade, se mulher, e aos 64 (sessenta e\nquatro)'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def preparar(layout, bbox):
    chunks = layout.split('\f')
    pages = [p for p in ET.fromstring(bbox).iter() if p.tag.rsplit('}', 1)[-1] == 'page']
    if len(pages) != 89 or len(chunks) != 90 or chunks[-1].strip():
        raise ValueError('Contagem física difere')
    if chunks[46].count(OLD_MARKER) != 1:
        raise ValueError('Preimagem do marcador difere')
    original_page = chunks[46]
    chunks[46] = chunks[46].replace(OLD_MARKER, NEW_MARKER, 1)
    if chunks[46].replace(NEW_MARKER, OLD_MARKER, 1) != original_page:
        raise ValueError('Alteração além do marcador')
    proof = []
    for i, (chunk, page) in enumerate(zip(chunks[:-1], pages), 1):
        words = [w.text or '' for w in page.iter() if w.tag.rsplit('}', 1)[-1] == 'word']
        a = ''.join(chunk.split())
        b = ''.join(''.join(words).split())
        if i in VISUAL_SHA and sha(a.encode()) != VISUAL_SHA[i]:
            raise ValueError('Ordem não corresponde à extração revista visualmente na página ' + str(i))
        if a != b and (i not in VISUAL_PAGES or collections.Counter(a) != collections.Counter(b)):
            raise ValueError('Caracteres não conferidos na página ' + str(i))
        proof.append({'pagina': i, 'sequencia_caracteres_identica': a == b, 'multiconjunto_caracteres_identico': collections.Counter(a) == collections.Counter(b), 'excecao_visual': i in VISUAL_PAGES})
    adjusted = '\f'.join(chunks)
    if collections.Counter(c for c in layout if not c.isspace()) != collections.Counter(c for c in adjusted if not c.isspace()):
        raise ValueError('Caracteres originais não preservados')
    return adjusted, proof


def main():
    raw = (ROOT / PDF).read_bytes()
    if sha(raw) != SOURCE_SHA:
        raise ValueError('Fonte mudou')
    layout = subprocess.check_output(['/opt/homebrew/bin/pdftotext', '-layout', '-enc', 'UTF-8', str(ROOT / PDF), '-']).decode()
    bbox = subprocess.check_output(['/opt/homebrew/bin/pdftotext', '-bbox-layout', '-enc', 'UTF-8', str(ROOT / PDF), '-'])
    adjusted, proof = preparar(layout, bbox)
    if not all(s in layout for s in ['Edição consolidada até a Emenda nº 41', 'Salvador –2024.', 'Art. 1º O Município de Salvador']):
        raise ValueError('Identidade ou edição não conferida')
    date_reference = ROOT / 'municipais/_lotes/20261020-salvador-inspecao/referencia-data-pagina-117.txt'
    if 'Lei Orgânica do Município do Salvador, de 05 abril de 1990' not in ' '.join(date_reference.read_text().split()):
        raise ValueError('Referência oficial à data não confirmada')
    ibge = next(c for c in json.loads((ROOT / 'municipais/_indice/ibge-municipios.json').read_text()) if str(c['id']) == '2927408')
    if ibge['nome'] != 'Salvador' or ibge['regiao-imediata']['regiao-intermediaria']['UF']['sigla'] != 'BA':
        raise ValueError('IBGE diverge')
    target = ROOT / 'municipais/BA/salvador/lei-organica/1990/lei-organica-salvador-1990.md'
    if not target.exists() or sha(target.read_bytes()) != PREIMAGE_CANDIDATE:
        raise ValueError('Candidato privado anterior mudou; revisar sem substituir')
    if set(target.parent.parent.glob('**/*.md')) - {target}:
        raise ValueError('LO já existente exige conciliação')
    title = 'Lei Orgânica do Município de Salvador — edição consolidada de 2024'
    note = ('Nota de transcrição: edição oficial de 2024, consolidada até a Emenda nº 41. Todas as 89 páginas físicas, notas, fólios e valores foram mantidos. '
            'Na página física 47, o marcador de emenda “(36)” foi recolocado antes do inciso III, conforme sua posição visual; nenhuma palavra ou número foi excluído. '
            'A fonte contém pequenas marcas vermelhas: um ponto no art. 154, a letra “o” no art. 229 e espaços, com sinal gráfico junto ao inciso I do art. 178. '
            'O [mapa visual da edição](../../../../_lotes/20261020-salvador-inspecao/recortes-cores/catalogo.json) preserva essas distinções, sem atribuir efeito jurídico à cor. A grafia “(03Art. 151” consta na própria fonte e foi mantida.\n\n')
    body = note + '```text\n' + adjusted.replace('\f', '\n\n').rstrip('\n') + '\n```'
    metadata = {'titulo': title, 'tipo': 'Lei Orgânica', 'numero': '', 'data': '1990-04-05', 'municipio': 'Salvador', 'uf': 'BA', 'codigo_ibge': '2927408',
                'origem_data': 'referência literal à LO de 05 abril de 1990 no Projeto de Lei 128/09, página física 117 da Ordem do Dia oficial de 19/11/2014; a edição consolidada de 2024 não repete a data de promulgação',
                'versao_texto': 'edição oficial de 2024, consolidada até a Emenda nº 41; transcrição integral da camada nativa, com notas, ADCT, fólios, valores e distinções visuais documentadas; sem certificação de atualização posterior ou vigência integral',
                'fonte': 'https://www.cms.ba.gov.br/lei-organica', 'fonte_texto': 'https://www.cms.ba.gov.br/uploads/3bdae368d1a3e255c81b7f262ba1bbf6_1709038424.pdf', 'sha256_fonte': SOURCE_SHA, 'sha256_texto': sha(body.encode()), 'baixado_em': '2026-10-20'}
    result = '\n'.join(['---'] + [k + ': ' + yaml_str(v) for k, v in metadata.items()] + ['revogada: null', '---', '', '# ' + title, '', body, ''])
    out = ROOT / 'municipais/_lotes/20261020-salvador-lo-v2'
    out.mkdir(exist_ok=False)
    (out / 'preimagem-candidato-v1.md').write_bytes(target.read_bytes())
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('w') as f:
        f.write(result)
    with (out / 'extracao-integral.json.gz').open('xb') as f:
        f.write(gzip.compress(json.dumps({'layout_original': layout, 'bbox': bbox.decode(), 'layout_com_marcador_reposicionado': adjusted}, ensure_ascii=False).encode(), mtime=0))
    (out / 'prova-paginas.json').write_text(json.dumps(proof, ensure_ascii=False, indent=2))
    (out / 'normas.paths.txt').write_text(str(target.relative_to(ROOT)) + '\n')
    receipt = {'documento': str(target.relative_to(ROOT)), 'sha256': sha(target.read_bytes()), 'pdf': str(PDF), 'sha256_fonte': SOURCE_SHA, 'paginas': 89, 'tokens_nativos_preservados': len(re.findall(r'\w+', layout)), 'sequencia_caracteres_identica_layout_bbox': 85, 'paginas_com_ordem_conferida_visualmente': sorted(VISUAL_PAGES), 'cores': '22 caracteres coloridos registrados, sendo 20 espaços, um ponto e a letra o; 19 recortes vistos. Distinções documentadas sem decidir vigência pela cor.', 'marcador_reposicionado': {'pagina': 47, 'preimagem': OLD_MARKER, 'posimagem': NEW_MARKER}, 'criterio': 'Todos os caracteres não brancos conferidos por página. Nas quatro páginas com diferença de fluxo, multiconjunto integral idêntico e ordem confirmada visualmente. Somente o marcador (36) foi reposicionado, com reversão exata. Nas demais páginas, sequência de caracteres idêntica, incluindo pontuação e números, independentemente da separação de palavras pelo bbox.', 'script_sha256': sha(Path(__file__).read_bytes()), 'limite': 'Edição e corte são os da fonte oficial de 2024. A data da LO é atribuída à referência oficial auxiliar. Não certifica atualização posterior ou vigência integral.'}
    (out / 'manifesto.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2))
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == '__main__':
    main()
