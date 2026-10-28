"""Captura documentos estruturantes das capitais em publicações oficiais identificadas.

Catálogo explícito de fontes: não adivinha URLs, datas ou números. Preserva os
binários, o corte da compilação e anexos, sem contar cada anexo como nova norma.
"""
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import Rede, documento_para_md, normalizar_chave, yaml_str

RAIZ = Path(__file__).resolve().parent.parent
CATALOGO = [{
    'municipio': 'Recife', 'uf': 'PE', 'codigo_ibge': '2611606',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-04-04',
    'titulo': 'Lei Orgânica do Município do Recife, de 4 de abril de 1990',
    'slug': 'lei-organica-recife-1990', 'cache': 'recife-organica.pdf',
    'fonte': 'https://transparencia.recife.pe.leg.br/institucional/competencias/lei-organica_atualizada-em-08-04-2024.pdf',
    'fonte_texto': 'https://transparencia.recife.pe.leg.br/institucional/competencias/lei-organica_atualizada-em-08-04-2024.pdf/@@download/file',
    'versao_texto': 'compilação oficial atualizada em 08/04/2024, com emendas anexas; não certifica atualização posterior',
    'marcas_obrigatorias': ['LEI ORGÂNICA DO MUNICÍPIO DO RECIFE', 'Promulgada em 4 de abril de 1990',
                           'Atualizada em 08 de abril de 2024'],
}, {
    'municipio': 'São Paulo', 'uf': 'SP', 'codigo_ibge': '3550308',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-04-04',
    'titulo': 'Lei Orgânica do Município de São Paulo, de 4 de abril de 1990',
    'slug': 'lei-organica-sao-paulo-1990', 'cache': 'sao-paulo-organica.pdf',
    'fonte': 'https://www.saopaulo.sp.leg.br/lei-organica/',
    'fonte_texto': 'https://www.saopaulo.sp.leg.br/wp-content/uploads/2022/09/LOMC.pdf',
    'versao_texto': 'compilação oficial, edição 2026 atualizada até a Emenda 44/25; índice remissivo preservado',
    'marcas_obrigatorias': ['LEI ORGÂNICA DO MUNICÍPIO DE SÃO PAULO', 'Atualizada até a Emenda 44/25',
                           'São Paulo, 4 de abril de 1990'],
}, {
    'municipio': 'Salvador', 'uf': 'BA', 'codigo_ibge': '2927408',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-04-05',
    'titulo': 'Lei Orgânica do Município de Salvador, de 5 de abril de 1990',
    'slug': 'lei-organica-salvador-1990', 'cache': 'salvador-organica.pdf',
    'fonte': 'https://www.cms.ba.gov.br/lei-organica',
    'fonte_texto': 'https://www.cms.ba.gov.br/uploads/3bdae368d1a3e255c81b7f262ba1bbf6_1709038424.pdf',
    'versao_texto': 'compilação oficial da Câmara Municipal de Salvador, edição consolidada até a Emenda nº 41/2024; a edição não imprime a data de promulgação original; não certifica atualização posterior',
    'marcas_obrigatorias': ['Lei Orgânica do Município de Salvador', 'Edição consolidada até a Emenda nº 41',
                           'O Município de Salvador, Capital do Estado da Bahia'],
}]


def main():
    ibge_path = RAIZ / 'municipais/_indice/ibge-municipios.json'
    ibge = {str(x['id']): x for x in json.loads(ibge_path.read_text())}
    rede = Rede(rps=1)
    for item in CATALOGO:
        municipio = ibge[item['codigo_ibge']]
        uf = municipio['regiao-imediata']['regiao-intermediaria']['UF']['sigla']
        if municipio['nome'] != item['municipio'] or uf != item['uf']:
            raise ValueError('identidade IBGE diverge do catálogo')
        slug = normalizar_chave(municipio['nome']).replace(' ', '-')
        destino = RAIZ / 'municipais' / uf / slug / item['categoria'] / item['data'][:4] / (item['slug'] + '.md')
        if destino.exists():
            print('já existente', destino, flush=True)
            continue
        outros = list((destino.parent.parent).glob('**/*.md'))
        if outros:
            raise ValueError('categoria já contém publicação; revisar versão antes de criar duplicata: ' + str(outros))
        pasta = RAIZ / 'municipais/_fonte/capitais' / slug
        pasta.mkdir(parents=True, exist_ok=True)
        fonte = pasta / item['cache']
        if not fonte.exists():
            st, bruto, _ = rede.get(item['fonte_texto'], tentativas=1, timeout=90)
            if st != 200 or not bruto.startswith(b'%PDF'):
                raise ValueError('fonte indisponível ou não é PDF: HTTP ' + str(st))
            with fonte.open('xb') as f:
                f.write(bruto)
        bruto = fonte.read_bytes()
        corpo, motivo = documento_para_md(bruto, item['fonte_texto'])
        if motivo:
            raise ValueError(motivo)
        normal = normalizar_chave(corpo)
        for marca in item['marcas_obrigatorias']:
            if normalizar_chave(marca) not in normal:
                raise ValueError('marca de identidade/data ausente: ' + marca)
        if not re.search(r'Art\.?\s*1[º°]', corpo, re.I):
            raise ValueError('artigo inicial não reconhecido')
        meta = {k: item[k] for k in ('titulo','tipo','numero','data','municipio','uf','codigo_ibge','versao_texto','fonte','fonte_texto')}
        meta.update({'sha256_fonte': hashlib.sha256(bruto).hexdigest(),
                     'sha256_texto': hashlib.sha256(corpo.encode()).hexdigest(), 'baixado_em': dt.date.today().isoformat()})
        texto = '\n'.join(['---'] + [k + ': ' + yaml_str(v) for k,v in meta.items()]
                          + ['revogada: null', '---', '', '# ' + item['titulo'], '', corpo, ''])
        destino.parent.mkdir(parents=True, exist_ok=True)
        with destino.open('x') as f:
            f.write(texto)
        comprovacao = {**item, 'arquivo': str(destino.relative_to(RAIZ)),
                       'sha256': hashlib.sha256(texto.encode()).hexdigest(),
                       'arquivo_fonte': str(fonte.relative_to(RAIZ)), 'sha256_fonte': meta['sha256_fonte'],
                       'sha256_corpo': meta['sha256_texto'], 'ibge_sha256': hashlib.sha256(ibge_path.read_bytes()).hexdigest(),
                       'verificado_em': dt.datetime.now().isoformat(),
                       'observacao': 'Compilação individual oficial; emendas anexas preservadas no mesmo documento, sem aumento artificial da contagem.'}
        with (pasta / (item['slug'] + '.manifesto.json')).open('x') as f:
            json.dump(comprovacao, f, ensure_ascii=False, indent=2)
        print('gravado', destino, flush=True)


if __name__ == '__main__':
    main()
