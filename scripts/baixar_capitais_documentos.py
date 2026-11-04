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
from cmbh_sil import ANEXOS_PLANO_DIRETOR, cache_anexo, url_download, url_ficha

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
}, {
    'municipio': 'Belo Horizonte', 'uf': 'MG', 'codigo_ibge': '3106200',
    'tipo': 'Plano diretor', 'categoria': 'plano-diretor', 'numero': '11181', 'data': '2019-08-08',
    'data_publicacao': '2019-08-09',
    'titulo': 'Lei nº 11.181, de 8 de agosto de 2019',
    'slug': 'plano-diretor-11181-2019', 'cache': 'lei11181-atual.doc',
    'fonte': url_ficha('lei', 11181, 2019),
    'fonte_texto': url_download('2c907f7693d91e4901941d35b6360152'),
    'sil_id_doc_da_norma': '2c907f7693d91e4901941d35b6360152',
    'versao_texto': 'compilação oficial da CMBH (lei11181-atual.doc no SIL), promulgação 08/08/2019 e publicação 09/08/2019; 32 anexos oficiais (mapas I–X e VII.1–VII.13, glossário XI, parâmetros XII, classificação XIII–XVI, coeficientes XVII, OUS XVIII–XIX) preservados como binários da mesma norma, sem contar cada anexo como lei nova; não certifica atualização posterior',
    'marcas_obrigatorias': ['LEI Nº 11.181, DE 8 DE AGOSTO DE 2019',
                           'Aprova o Plano Diretor do Município de Belo Horizonte',
                           'Belo Horizonte, 8 de agosto de 2019'],
    'anexos': [{'nome': n, 'cache': cache_anexo(n), 'fonte_texto': url_download(i),
               'sil_id_doc_da_norma': i} for n, i in ANEXOS_PLANO_DIRETOR],
}, {
    'municipio': 'Belo Horizonte', 'uf': 'MG', 'codigo_ibge': '3106200',
    'tipo': 'Código municipal', 'categoria': 'codigos', 'numero': '8616', 'data': '2003-07-14',
    'data_publicacao': '2003-07-15',
    'titulo': 'Lei nº 8.616, de 14 de julho de 2003',
    'slug': 'codigos-8616-2003', 'cache': 'lei8616-atual.doc',
    'fonte': url_ficha('lei', 8616, 2003),
    'fonte_texto': url_download('2c907f76a10b73fb01a163fc57c401e0'),
    'sil_id_doc_da_norma': '2c907f76a10b73fb01a163fc57c401e0',
    'versao_texto': 'compilação oficial da CMBH (lei8616-atual.doc no SIL); promulgação 14/07/2003 e publicação 15/07/2003 pelo Prefeito; republicação pela Presidência da CMBH em 26/09/2003 (publicação 30/09/2003); não certifica atualização posterior',
    'marcas_obrigatorias': ['LEI Nº 8.616, DE 14 DE JULHO DE 2003',
                           'Contém o Código de Posturas do Município de Belo Horizonte',
                           'Este Código contém as posturas destinadas a promover a harmonia'],
}, {
    'municipio': 'Belo Horizonte', 'uf': 'MG', 'codigo_ibge': '3106200',
    'tipo': 'Código tributário', 'categoria': 'codigo-tributario', 'numero': '1310', 'data': '1966-12-31',
    'data_publicacao': '1967-01-03',
    'titulo': 'Lei nº 1.310, de 31 de dezembro de 1966',
    'slug': 'codigo-tributario-1310-1966', 'cache': 'lei1310-atual.doc',
    'fonte': url_ficha('lei', 1310, 1966),
    'fonte_texto': url_download('2c907f767c5f60f7017c79ac98120097'),
    'sil_id_doc_da_norma': '2c907f767c5f60f7017c79ac98120097',
    'versao_texto': 'compilação oficial da CMBH (lei1310-atual.doc no SIL), promulgação 31/12/1966 e publicação 03/01/1967; não certifica atualização posterior',
    'marcas_obrigatorias': ['LEI Nº 1.310, DE 31 DE DEZEMBRO DE 1966',
                           'Institui o Código Tributário do Município de Belo Horizonte',
                           'Belo Horizonte, 31 de dezembro de 1966'],
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


def baixar_oficial(rede, url, destino, timeout=180):
    if destino.exists() and destino.stat().st_size > 32:
        return destino.read_bytes()
    st, bruto, _ = rede.get(url, tentativas=2, timeout=timeout)
    if st != 200 or not (bruto.startswith(b'%PDF') or bruto.startswith(OLE)):
        raise ValueError('fonte indisponível ou não é PDF/DOC/XLS oficial: HTTP ' + str(st) + ' ' + url)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open('xb') as f:
        f.write(bruto)
    return bruto


def main():
    ibge_path = RAIZ / 'municipais/_indice/ibge-municipios.json'
    ibge = {str(x['id']): x for x in json.loads(ibge_path.read_text())}
    rede = Rede(rps=3, headers={'Referer': 'https://www.cmbh.mg.gov.br/atividade-legislativa/pesquisar-legislacao'})
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
        bruto = baixar_oficial(rede, item['fonte_texto'], fonte)
        anexos_gravados = []
        for anexo in item.get('anexos') or []:
            arq = pasta / anexo['cache']
            binario = baixar_oficial(rede, anexo['fonte_texto'], arq, timeout=300)
            anexos_gravados.append({**anexo, 'arquivo_fonte': str(arq.relative_to(RAIZ)),
                                    'sha256_fonte': hashlib.sha256(binario).hexdigest(),
                                    'bytes': len(binario)})
            print('anexo', arq.name, len(binario), flush=True)
        corpo, motivo = documento_oficial_para_md(bruto, item['fonte_texto'])
        if motivo:
            raise ValueError(motivo)
        normal = normalizar_chave(corpo)
        for marca in item['marcas_obrigatorias']:
            if normalizar_chave(marca) not in normal:
                raise ValueError('marca de identidade/data ausente: ' + marca)
        if not re.search(r'Art\.?\s*1[º°]', corpo, re.I):
            raise ValueError('artigo inicial não reconhecido')
        campos = ('titulo', 'tipo', 'numero', 'data', 'municipio', 'uf', 'codigo_ibge',
                  'versao_texto', 'fonte', 'fonte_texto')
        meta = {k: item[k] for k in campos}
        if item.get('data_publicacao'):
            meta['data_publicacao'] = item['data_publicacao']
        meta.update({'sha256_fonte': hashlib.sha256(bruto).hexdigest(),
                     'sha256_texto': hashlib.sha256(corpo.encode()).hexdigest(),
                     'baixado_em': dt.date.today().isoformat()})
        texto = '\n'.join(['---'] + [k + ': ' + yaml_str(v) for k, v in meta.items()]
                          + ['revogada: null', '---', '', '# ' + item['titulo'], '', corpo, ''])
        destino.parent.mkdir(parents=True, exist_ok=True)
        with destino.open('x') as f:
            f.write(texto)
        observacao = ('Compilação individual oficial; emendas anexas preservadas no mesmo documento, '
                      'sem aumento artificial da contagem.')
        if anexos_gravados:
            observacao = (f'{len(anexos_gravados)} anexos oficiais do SIL preservados como binários '
                          'da mesma norma, sem contar cada anexo como lei nova.')
        comprovacao = {k: item[k] for k in item if k != 'anexos'}
        comprovacao.update({'arquivo': str(destino.relative_to(RAIZ)),
                            'sha256': hashlib.sha256(texto.encode()).hexdigest(),
                            'arquivo_fonte': str(fonte.relative_to(RAIZ)),
                            'sha256_fonte': meta['sha256_fonte'],
                            'sha256_corpo': meta['sha256_texto'],
                            'ibge_sha256': hashlib.sha256(ibge_path.read_bytes()).hexdigest(),
                            'verificado_em': dt.datetime.now().isoformat(),
                            'anexos': anexos_gravados, 'observacao': observacao})
        with (pasta / (item['slug'] + '.manifesto.json')).open('x') as f:
            json.dump(comprovacao, f, ensure_ascii=False, indent=2)
        captura = {'url': item['fonte_texto'], 'filename': item['cache'],
                   'sha256': meta['sha256_fonte'], 'http_status': 200,
                   'content_length': len(bruto),
                   'formato': 'application/msword (OLE Compound File)' if bruto.startswith(OLE) else 'application/pdf',
                   'pagina_catalogo': item['fonte'],
                   'sil_id_doc_da_norma': item.get('sil_id_doc_da_norma'),
                   'captura': 'download oficial HTTP 200 em cmbhsildownload.cmbh.mg.gov.br via catálogo SIL/proxy.php; sem Wayback'}
        with (pasta / (Path(item['cache']).stem + '.fonte.json')).open('x') as f:
            json.dump(captura, f, ensure_ascii=False, indent=2)
        print('gravado', destino, flush=True)


if __name__ == '__main__':
    main()
