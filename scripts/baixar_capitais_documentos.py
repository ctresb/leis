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
from comum import Rede, normalizar_chave, yaml_str
from baixar_organicas_sapl import corpo_de_fonte

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
    'municipio': 'Porto Alegre', 'uf': 'RS', 'codigo_ibge': '4314902',
    'tipo': 'Lei Orgânica', 'categoria': 'lei-organica', 'numero': '', 'data': '1990-04-03',
    'titulo': 'Lei Orgânica do Município de Porto Alegre, de 3 de abril de 1990',
    'slug': 'lei-organica-porto-alegre-1990', 'cache': 'porto-alegre-organica.pdf',
    'fonte': 'https://legislacao.camarapoa.rs.gov.br/lei-organica/',
    'fonte_texto': 'https://legislacao.camarapoa.rs.gov.br/wp-content/uploads/documents/lei_organica/Lei%20Org%C3%A2nica%20do%20Munic%C3%ADpio%20de%20Porto%20Alegre%20atualizada%20at%C3%A9%20emenda%20n%C2%BA%2049.pdf',
    'versao_texto': 'compilação oficial da Câmara Municipal de Porto Alegre (Diretoria Legislativa), atualizada até a Emenda nº 49, de 12/12/2022; captura Wayback 20240422221213id_ do PDF oficial, porque legislacao.camarapoa.rs.gov.br esgotou conexão no IP do agente (página e PDF da Emenda 51); o Google indexa o nome “atualizada até emenda nº 51”, mas esse PDF não está no Wayback (Save Page Now HTTP 520); a PGM/SAPL só publica compilação até a Emenda 48/2022; o PDF da Prefeitura/SMPS é imagem sem texto nativo; emendas 50 e 51 (28/08/2024) existem no SAPL como atos isolados e não integram esta compilação; não certifica atualização posterior',
    'marcas_obrigatorias': ['LEI ORGÂNICA DO MUNICÍPIO DE PORTO ALEGRE',
                           'Atualizada até Emenda n.º 49, de 12.12.2022',
                           'O Município de Porto Alegre, pessoa jurídica de direito público interno'],
}, {
    'municipio': 'Porto Alegre', 'uf': 'RS', 'codigo_ibge': '4314902',
    'tipo': 'Plano diretor', 'categoria': 'plano-diretor', 'numero': '1075', 'data': '2026-07-14',
    'titulo': 'Lei Complementar municipal nº 1.075, de 14 de julho de 2026',
    'slug': 'plano-diretor-porto-alegre-2026', 'cache': 'porto-alegre-plano-diretor-1075-2026.pdf',
    'fonte': 'https://legislacao.portoalegre.rs.gov.br/norma/51485',
    'fonte_texto': 'http://legislacao.portoalegre.rs.gov.br/media/sapl/public/normajuridica/2026/51485/lc1075_atualizada_ate_24.09.2026.pdf',
    'versao_texto': 'texto integral anexado no SAPL da PGM/Porto Alegre (norma/51485), PDF atualizado até a derrubada de veto de 24/09/2026; não certifica atualização posterior',
    'observacao': 'Plano Diretor Urbano Sustentável; PDF da API em http, capturado por HTTPS 200.',
    'marcas_obrigatorias': ['LEI COMPLEMENTAR Nº 1.075', 'Institui o Plano Diretor Urbano Sustentável',
                           'Município de Porto Alegre'],
}, {
    'municipio': 'Porto Alegre', 'uf': 'RS', 'codigo_ibge': '4314902',
    'tipo': 'Código municipal', 'categoria': 'codigos', 'numero': '284', 'data': '1992-10-27',
    'titulo': 'Lei Complementar municipal nº 284, de 27 de outubro de 1992',
    'slug': 'codigo-edificacoes-porto-alegre-1992', 'cache': 'porto-alegre-codigo-edificacoes-284-1992.pdf',
    'fonte': 'https://legislacao.portoalegre.rs.gov.br/norma/26743',
    'fonte_texto': 'http://legislacao.portoalegre.rs.gov.br/media/sapl/public/normajuridica/sirel/lc%20284.pdf',
    'versao_texto': 'texto integral anexado no SAPL da PGM/Porto Alegre (norma/26743, arquivo SIREL); 5ª edição CORAG de 2001 do Código de Edificações (LC 284/1992); não certifica compilação posterior',
    'observacao': 'Código de Edificações; PDF da API em http, capturado por HTTPS 200.',
    'marcas_obrigatorias': ['CÓDIGO DE EDIFICAÇÕES', 'Porto Alegre'],
}, {
    'municipio': 'Porto Alegre', 'uf': 'RS', 'codigo_ibge': '4314902',
    'tipo': 'Código tributário', 'categoria': 'codigo-tributario', 'numero': '7', 'data': '1973-12-07',
    'titulo': 'Lei Complementar municipal nº 7, de 07 de dezembro de 1973',
    'slug': 'codigo-tributario-porto-alegre-1973', 'cache': 'porto-alegre-codigo-tributario-7-1973.doc',
    'fonte': 'https://legislacao.portoalegre.rs.gov.br/norma/17478',
    'fonte_texto': 'http://legislacao.portoalegre.rs.gov.br/media/sapl/public/normajuridica/sirel/lc%2007.doc',
    'versao_texto': 'texto integral anexado no SAPL da PGM/Porto Alegre (norma/17478, arquivo SIREL .doc); não certifica compilação posterior',
    'observacao': 'Código Tributário Municipal; DOC da API em http, capturado por HTTPS 200.',
    'marcas_obrigatorias': ['LEI COMPLEMENTAR N', 'tributos de competência do Município'],
}, {
    'municipio': 'Porto Alegre', 'uf': 'RS', 'codigo_ibge': '4314902',
    'tipo': 'Código municipal', 'categoria': 'codigos', 'numero': '1060', 'data': '2025-12-22',
    'titulo': 'Lei Complementar municipal nº 1.060, de 22 de dezembro de 2025',
    'slug': 'codigo-limpeza-urbana-porto-alegre-2025', 'cache': 'porto-alegre-codigo-limpeza-urbana-1060-2025.pdf',
    'fonte': 'https://legislacao.portoalegre.rs.gov.br/norma/50791',
    'fonte_texto': 'http://legislacao.portoalegre.rs.gov.br/media/sapl/public/normajuridica/2025/50791/lc_1060.pdf',
    'versao_texto': 'texto integral anexado no SAPL da PGM/Porto Alegre (norma/50791); não certifica atualização posterior',
    'observacao': 'Código Municipal de Limpeza Urbana; PDF da API em http, capturado por HTTPS 200.',
    'marcas_obrigatorias': ['LEI COMPLEMENTAR Nº 1.060', 'Código Municipal de Limpeza Urbana',
                           'Município de Porto Alegre'],
}]


def preferir_https(url):
    if url.startswith("http://"):
        return "https://" + url.split("://", 1)[1]
    return url


def documento_oficial(bruto):
    cabeca = bruto.lstrip()[:15].lower()
    return (bruto.startswith(b"%PDF") or bruto.startswith(b"\xd0\xcf\x11\xe0") or bruto[:2] == b"PK"
            or cabeca.startswith(b"<html") or cabeca.startswith(b"<!doctype"))


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
        if item['categoria'] == 'lei-organica':
            outros = list((destino.parent.parent).glob('**/*.md'))
            if outros:
                raise ValueError('categoria já contém publicação; revisar versão antes de criar duplicata: ' + str(outros))
        pasta = RAIZ / 'municipais/_fonte/capitais' / slug
        pasta.mkdir(parents=True, exist_ok=True)
        fonte = pasta / item['cache']
        url_catalogo = item['fonte_texto']
        url_usada = url_catalogo
        if not fonte.exists():
            candidatos = []
            https = preferir_https(url_catalogo)
            if https != url_catalogo:
                candidatos.append(https)
            candidatos.append(url_catalogo)
            bruto, st, url_usada = b'', 0, url_catalogo
            for url in candidatos:
                st, bruto, _ = rede.get(url, tentativas=1, timeout=90)
                if st == 200 and documento_oficial(bruto):
                    url_usada = url
                    break
            else:
                raise ValueError('fonte indisponível ou formato não reconhecido: HTTP ' + str(st) + ' ' + url_catalogo)
            with fonte.open('xb') as f:
                f.write(bruto)
        bruto = fonte.read_bytes()
        if not documento_oficial(bruto):
            raise ValueError('arquivo em cache não é documento oficial reconhecido: ' + str(fonte))
        corpo, motivo = corpo_de_fonte(bruto, url_usada)
        if motivo:
            raise ValueError(motivo)
        normal = normalizar_chave(corpo)
        for marca in item['marcas_obrigatorias']:
            if normalizar_chave(marca) not in normal:
                raise ValueError('marca de identidade/data ausente: ' + marca)
        if not re.search(r'Art\.?\s*1[º°]', corpo, re.I):
            raise ValueError('artigo inicial não reconhecido')
        meta = {k: item[k] for k in ('titulo','tipo','numero','data','municipio','uf','codigo_ibge','versao_texto','fonte')}
        meta['fonte_texto'] = url_usada
        meta.update({'sha256_fonte': hashlib.sha256(bruto).hexdigest(),
                     'sha256_texto': hashlib.sha256(corpo.encode()).hexdigest(), 'baixado_em': dt.date.today().isoformat()})
        texto = '\n'.join(['---'] + [k + ': ' + yaml_str(v) for k,v in meta.items()]
                          + ['revogada: null', '---', '', '# ' + item['titulo'], '', corpo, ''])
        destino.parent.mkdir(parents=True, exist_ok=True)
        with destino.open('x') as f:
            f.write(texto)
        nota = item.get('observacao') or ('Compilação individual oficial; emendas anexas preservadas no mesmo documento, sem aumento artificial da contagem.')
        comprovacao = {**item, 'arquivo': str(destino.relative_to(RAIZ)),
                       'sha256': hashlib.sha256(texto.encode()).hexdigest(),
                       'arquivo_fonte': str(fonte.relative_to(RAIZ)), 'sha256_fonte': meta['sha256_fonte'],
                       'sha256_corpo': meta['sha256_texto'], 'fonte_texto': url_usada,
                       'ibge_sha256': hashlib.sha256(ibge_path.read_bytes()).hexdigest(),
                       'verificado_em': dt.datetime.now().isoformat(),
                       'observacao': nota}
        with (pasta / (item['slug'] + '.manifesto.json')).open('x') as f:
            json.dump(comprovacao, f, ensure_ascii=False, indent=2)
        recibo = pasta / (Path(item['cache']).stem + '.fonte.json')
        if not recibo.exists():
            recibo.write_text(json.dumps({
                'url': url_usada, 'url_catalogo': url_catalogo,
                'sha256': meta['sha256_fonte'], 'http_status': 200,
                'content_length': len(bruto),
                'obtido_em': dt.datetime.now(dt.timezone.utc).isoformat(),
            }, ensure_ascii=False, indent=2) + '\n')
        print('gravado', destino, flush=True)


if __name__ == '__main__':
    main()
