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
    'municipio': 'Rio de Janeiro', 'uf': 'RJ', 'codigo_ibge': '3304557',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-04-05',
    'titulo': 'Lei Orgânica do Município do Rio de Janeiro, de 5 de abril de 1990',
    'slug': 'lei-organica-rio-de-janeiro-1990', 'cache': 'rio-de-janeiro-organica.pdf',
    'fonte': 'https://www.camara.rio/atividade-parlamentar/legislacao/lei-organica-do-municipio',
    'fonte_texto': 'https://www.rio.rj.gov.br/dlstatic/10112/4946719/4136646/Lei_Organica_MRJ_comaltdo205_2303.pdf',
    'versao_texto': 'compilação oficial da PGM/Prefeitura do Rio de Janeiro, 2ª edição revista e ampliada (2010), com alterações e revogações assinaladas no texto, atualizada até a Emenda nº 20/2009; o PDF imprime o fecho "Cidade do Rio de Janeiro, 5 de abril de 1990"; Last-Modified 23 Mar 2015; não certifica atualização posterior',
    'marcas_obrigatorias': ['LEI ORGÂNICA DO MUNICÍPIO DO RIO DE JANEIRO',
                           'Texto atualizado até a Emenda n.º 20/2009',
                           'O Município do Rio de Janeiro é a expressão e o instrumento da soberania do povo carioca'],
}, {
    'municipio': 'Rio de Janeiro', 'uf': 'RJ', 'codigo_ibge': '3304557',
    'tipo': 'Plano diretor', 'tipo_na_fonte': 'Lei Complementar',
    'categoria': 'plano-diretor', 'numero': '270', 'data': '2024-01-16',
    'titulo': 'Lei Complementar nº 270, de 16 de janeiro de 2024',
    'slug': 'plano-diretor-270-2024', 'cache': 'lc-270-2024.html', 'formato': 'html',
    'anexos': True,
    'fonte': 'https://aplicnt.camara.rj.gov.br/APL/Legislativos/contlei.nsf/0/0274835DDBC09B5303258AA700487674?OpenDocument',
    'fonte_texto': 'https://aplicnt.camara.rj.gov.br/APL/Legislativos/contlei.nsf/0/0274835DDBC09B5303258AA700487674?OpenDocument',
    'versao_texto': 'texto integral HTML da Câmara Municipal do Rio de Janeiro (Domino/contlei.nsf); republicação após rejeição de vetos parciais na sessão de 14/03/2024; anexos PDF oficiais do mesmo documento preservados à parte, sem contar como normas novas; a fonte declara que o texto não substitui o Diário Oficial',
    'marcas_obrigatorias': ['LEI COMPLEMENTAR Nº 270',
                           'Plano Diretor de Desenvolvimento Urbano Sustentável',
                           'institui a revisão do Plano Diretor'],
}, {
    'municipio': 'Rio de Janeiro', 'uf': 'RJ', 'codigo_ibge': '3304557',
    'tipo': 'Código municipal', 'tipo_na_fonte': 'Lei Complementar',
    'categoria': 'codigos', 'numero': '198', 'data': '2019-01-14',
    'titulo': 'Lei Complementar nº 198, de 14 de janeiro de 2019',
    'slug': 'codigo-obras-edificacoes-198-2019', 'cache': 'lc-198-2019.html', 'formato': 'html',
    'fonte': 'https://aplicnt.camara.rj.gov.br/APL/Legislativos/contlei.nsf/0/B004AA9E75ADFF0483258386005166C9?OpenDocument',
    'fonte_texto': 'https://aplicnt.camara.rj.gov.br/APL/Legislativos/contlei.nsf/0/B004AA9E75ADFF0483258386005166C9?OpenDocument',
    'versao_texto': 'texto integral HTML da Câmara Municipal do Rio de Janeiro (Domino/contlei.nsf); Código de Obras e Edificações Simplificado (COES); a fonte declara que o texto não substitui o Diário Oficial',
    'marcas_obrigatorias': ['LEI COMPLEMENTAR Nº 198',
                           'Código de Obras e Edificações Simplificado',
                           'COES'],
}, {
    'municipio': 'Rio de Janeiro', 'uf': 'RJ', 'codigo_ibge': '3304557',
    'tipo': 'Código municipal', 'tipo_na_fonte': 'Lei Complementar',
    'categoria': 'codigos', 'numero': '197', 'data': '2018-12-27',
    'titulo': 'Lei Complementar nº 197, de 27 de dezembro de 2018',
    'slug': 'codigo-vigilancia-sanitaria-197-2018', 'cache': 'lc-197-2018.html', 'formato': 'html',
    'fonte': 'https://aplicnt.camara.rj.gov.br/APL/Legislativos/contlei.nsf/0/CFDE3DDFD5DA93BC8325837600642FBE?OpenDocument',
    'fonte_texto': 'https://aplicnt.camara.rj.gov.br/APL/Legislativos/contlei.nsf/0/CFDE3DDFD5DA93BC8325837600642FBE?OpenDocument',
    'versao_texto': 'texto integral HTML da Câmara Municipal do Rio de Janeiro (Domino/contlei.nsf); Código de Vigilância Sanitária, Vigilância de Zoonoses e de Inspeção Agropecuária; a fonte declara que o texto não substitui o Diário Oficial',
    'marcas_obrigatorias': ['LEI COMPLEMENTAR Nº 197',
                           'Código de Vigilância Sanitária',
                           'Vigilância de Zoonoses'],
}]


def baixar_anexos(rede, html, unid, pasta):
    """Preserva PDFs oficiais do mesmo documento; não cria norma nova."""
    from cmrj import anexos_pdf
    lista = []
    for url, nome in anexos_pdf(html, unid):
        seguro = re.sub(r'[^\w.\- ]+', '_', nome).strip() or 'anexo.pdf'
        destino = pasta / seguro
        pasta.mkdir(parents=True, exist_ok=True)
        if not destino.exists():
            st, bruto, _ = rede.get(url, tentativas=2, timeout=300)
            if st != 200 or not bruto.startswith(b'%PDF'):
                raise ValueError('anexo indisponível ou não é PDF: HTTP ' + str(st) + ' ' + nome)
            with destino.open('xb') as f:
                f.write(bruto)
        bruto = destino.read_bytes()
        lista.append({'arquivo': str(destino.relative_to(RAIZ)), 'nome': nome,
                      'url': url, 'sha256': hashlib.sha256(bruto).hexdigest(), 'bytes': len(bruto)})
        print('anexo', nome, len(bruto), flush=True)
    return lista


def main():
    ibge_path = RAIZ / 'municipais/_indice/ibge-municipios.json'
    ibge = {str(x['id']): x for x in json.loads(ibge_path.read_text())}
    rede = Rede(rps=3)
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
        if item['categoria'] == 'lei-organica':
            outros = list((destino.parent.parent).glob('**/*.md'))
            if outros:
                raise ValueError('categoria já contém publicação; revisar versão antes de criar duplicata: ' + str(outros))
        pasta = RAIZ / 'municipais/_fonte/capitais' / slug
        pasta.mkdir(parents=True, exist_ok=True)
        fonte = pasta / item['cache']
        formato = item.get('formato', 'pdf')
        if not fonte.exists():
            st, bruto, _ = rede.get(item['fonte_texto'], tentativas=1, timeout=180)
            if st != 200:
                raise ValueError('fonte indisponível: HTTP ' + str(st))
            if formato == 'pdf' and not bruto.startswith(b'%PDF'):
                raise ValueError('fonte indisponível ou não é PDF: HTTP ' + str(st))
            with fonte.open('xb') as f:
                f.write(bruto)
        bruto = fonte.read_bytes()
        anexos = []
        if formato == 'html':
            from cmrj import corpo_documento, data_do_documento
            corpo, html = corpo_documento(bruto, 'text/html; charset=UTF-8')
            data_doc = data_do_documento(html, corpo)
            if item['data'] and data_doc and data_doc != item['data']:
                raise ValueError('data do documento ' + data_doc + ' diverge do catálogo ' + item['data'])
            unid = item['fonte_texto'].rstrip('=').rsplit('/', 1)[-1].split('?')[0]
            if item.get('anexos'):
                anexos = baixar_anexos(rede, html, unid, pasta / (item['slug'] + '-anexos'))
                if not anexos:
                    raise ValueError('anexos PDF oficiais não localizados no HTML')
        else:
            corpo, motivo = documento_para_md(bruto, item['fonte_texto'])
            if motivo:
                raise ValueError(motivo)
        normal = normalizar_chave(corpo)
        for marca in item['marcas_obrigatorias']:
            if normalizar_chave(marca) not in normal:
                raise ValueError('marca de identidade/data ausente: ' + marca)
        if not re.search(r'Art\.?\s*1[º°]', corpo, re.I):
            raise ValueError('artigo inicial não reconhecido')
        campos_meta = ('titulo','tipo','numero','data','municipio','uf','codigo_ibge','versao_texto','fonte','fonte_texto')
        meta = {k: item[k] for k in campos_meta}
        if item.get('tipo_na_fonte'):
            meta['tipo_na_fonte'] = item['tipo_na_fonte']
        meta.update({'sha256_fonte': hashlib.sha256(bruto).hexdigest(),
                     'sha256_texto': hashlib.sha256(corpo.encode()).hexdigest(), 'baixado_em': dt.date.today().isoformat()})
        texto = '\n'.join(['---'] + [k + ': ' + yaml_str(v) for k,v in meta.items()]
                          + ['revogada: null', '---', '', '# ' + item['titulo'], '', corpo.rstrip('\n'), ''])
        destino.parent.mkdir(parents=True, exist_ok=True)
        with destino.open('x') as f:
            f.write(texto)
        comprovacao = {**item, 'arquivo': str(destino.relative_to(RAIZ)),
                       'sha256': hashlib.sha256(texto.encode()).hexdigest(),
                       'arquivo_fonte': str(fonte.relative_to(RAIZ)), 'sha256_fonte': meta['sha256_fonte'],
                       'sha256_corpo': meta['sha256_texto'], 'ibge_sha256': hashlib.sha256(ibge_path.read_bytes()).hexdigest(),
                       'verificado_em': dt.datetime.now().isoformat(),
                       'anexos_baixados': anexos,
                       'observacao': ('Compilação individual oficial; anexos PDF do mesmo ato preservados na fonte, '
                                      'sem aumento artificial da contagem.' if anexos else
                                      'Compilação individual oficial; emendas anexas preservadas no mesmo documento, sem aumento artificial da contagem.')}
        with (pasta / (item['slug'] + '.manifesto.json')).open('x') as f:
            json.dump(comprovacao, f, ensure_ascii=False, indent=2)
        print('gravado', destino, flush=True)


if __name__ == '__main__':
    main()
