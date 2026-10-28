"""Captura documentos estruturantes das capitais em publicações oficiais identificadas.

Catálogo explícito de fontes: não adivinha URLs, datas ou números. Preserva os
binários, o corte da compilação e anexos, sem contar cada anexo como nova norma.
"""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import Rede, documento_para_md, html_para_md, normalizar_chave, texto_pdf_para_md, yaml_str

OLE = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'

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
    'municipio': 'Belo Horizonte', 'uf': 'MG', 'codigo_ibge': '3106200',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-03-21',
    'titulo': 'Lei Orgânica do Município de Belo Horizonte, de 21 de março de 1990',
    'slug': 'lei-organica-belo-horizonte-1990', 'cache': 'belo-horizonte-organica.doc',
    'fonte': 'https://www.cmbh.mg.gov.br/atividade-legislativa/pesquisar-legislacao/lei-organica',
    'fonte_texto': 'https://cmbhsildownload.cmbh.mg.gov.br/silinternet/servico/download/documentoDaNorma?idDocDaNorma=2c907f76a0ee650c01a0fc97127701cf',
    'versao_texto': 'compilação oficial da Câmara Municipal de Belo Horizonte (LOMBH-atual.doc no SIL), atualizada até setembro/2026, inclusive a Emenda nº 45, de 23/9/2026; promulgação 21/03/1990 e publicação 22/03/1990; não certifica atualização posterior',
    'marcas_obrigatorias': ['LEI ORGÂNICA DO MUNICÍPIO DE BELO HORIZONTE',
                           'Belo Horizonte, 21 de março de 1990',
                           'O Município de Belo Horizonte integra, com autonomia político-administrativa',
                           'Atualizada até setembro/2026'],
}]


def ole_doc_para_md(bruto):
    """Converte o .doc OLE oficial (LOMBH-atual.doc) sem inventar PDF derivado."""
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, 'a.doc')
        open(src, 'wb').write(bruto)
        if shutil.which('textutil'):
            r = subprocess.run(['textutil', '-convert', 'html', '-stdout', src],
                               capture_output=True, timeout=300)
            corpo = html_para_md(r.stdout.decode('utf-8', 'replace'))
        elif shutil.which('antiword'):
            r = subprocess.run(['antiword', '-w', '0', src], capture_output=True, timeout=300)
            if r.returncode != 0 or not r.stdout.strip():
                return None, 'antiword não extraiu o DOC oficial'
            corpo = texto_pdf_para_md(r.stdout.decode('utf-8', 'replace'))
        elif shutil.which('catdoc'):
            r = subprocess.run(['catdoc', '-w', src], capture_output=True, timeout=300)
            if r.returncode != 0 or not r.stdout.strip():
                return None, 'catdoc não extraiu o DOC oficial'
            corpo = texto_pdf_para_md(r.stdout.decode('utf-8', 'replace'))
        else:
            return None, 'sem conversor de DOC (textutil, antiword ou catdoc)'
        if len(re.sub(r'\W', '', corpo)) < 80:
            return None, 'DOC sem texto legível'
        return corpo, None


def documento_oficial_para_md(bruto, url):
    if bruto.startswith(OLE):
        return ole_doc_para_md(bruto)
    return documento_para_md(bruto, url)


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
            if st != 200 or not (bruto.startswith(b'%PDF') or bruto.startswith(OLE)):
                raise ValueError('fonte indisponível ou não é PDF/DOC oficial: HTTP ' + str(st))
            with fonte.open('xb') as f:
                f.write(bruto)
        bruto = fonte.read_bytes()
        corpo, motivo = documento_oficial_para_md(bruto, item['fonte_texto'])
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
