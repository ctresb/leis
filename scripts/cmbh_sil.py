"""Adaptador SIL da Câmara Municipal de Belo Horizonte.

O host interno cmbhsilint.cmbh.mg.gov.br falha TLS. A consulta pública usa o
proxy Drupal `/sites/all/modules/consulta_normas/pesquisar.php` (detalhe em
`proxy.php`). O binário oficial (OLE `.doc`, PDF ou XLS) sai de
cmbhsildownload, o mesmo caminho da Lei Orgânica no PR #23.

Catálogo explícito: números, datas e `idDocDaNorma` vieram da ficha SIL, não
de URL inventada. Anexos do Plano Diretor são binários da mesma norma — não
contam como leis novas. Belo Horizonte não publica tipo Lei Complementar.
"""
import datetime as dt
import hashlib
import html as htmlmod
import json
import os
from pathlib import Path
import re
import sys
import urllib.parse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import Rede, normalizar_chave, slugify, yaml_str

RAIZ = Path(__file__).resolve().parent.parent
PESQUISAR = "https://www.cmbh.mg.gov.br/sites/all/modules/consulta_normas/pesquisar.php"
PROXY = "https://www.cmbh.mg.gov.br/sites/all/modules/consulta_normas/proxy.php"
DOWNLOAD = ("https://cmbhsildownload.cmbh.mg.gov.br/silinternet/servico/download/"
            "documentoDaNorma")
CATALOGO_PAGINA = "https://www.cmbh.mg.gov.br/atividade-legislativa/pesquisar-legislacao"
TIPO_LEI = "2c907f78064b443701064b444c020008"
TIPO_EMENDA = "2c907f78064b443701064b444bb80006"
TIPO_ORGANICA = "2c907f7619968b1a011a0179819f12aa"
IBGE_BH = "3106200"
OLE = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"
MESES = ("janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

# (numero, ano, data_promulgacao, data_publicacao, idDocDaNorma, arquivo_sil, ementa)
EMENDAS = [
    [
        1,
        1992,
        "1992-06-30",
        "1992-07-02",
        "2c907f76267b781a0126955fd74d00a9",
        "EMENDA LOMBH-01-atual.doc",
        "Altera o § 1º do art. 63 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        2,
        1992,
        "1992-09-24",
        "1992-09-26",
        "2c907f76267b781a0126956f3a4000b1",
        "EMENDA LOMBH-02-atual.doc",
        "Dispõe sobre o afastamento do Vereador, sem perda do mandato, em casos de gestação e paternidade."
    ],
    [
        3,
        1992,
        "1992-12-01",
        "1992-12-03",
        "2c907f76267b781a01269575c5bd00b7",
        "EMENDA LOMBH-03-atual.doc",
        "Altera o parágrafo único do artigo 219 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        4,
        1993,
        "1993-12-21",
        "1994-02-11",
        "2c907f76267b781a01269a0cb66600f6",
        "EMENDA LOMBH-04-atual.doc",
        "Altera e acrescenta parágrafos ao art. 38 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        5,
        1994,
        "1994-02-22",
        "1994-03-17",
        "2c907f76267b781a01269a067c2d00f2",
        "EMENDA LOMBH-05-atual.doc",
        "Altera o art. 191 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        6,
        1994,
        "1994-12-14",
        "1995-02-23",
        "2c907f76267b781a01269a1417dd010d",
        "EMENDA LOMBH-06-atual.doc",
        "Dá nova redação ao art. 71 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        7,
        1995,
        "1995-01-26",
        "1995-02-14",
        "2c907f76267b781a01269a5a6be2011d",
        "EMENDA LOMBH-07-atual.doc",
        "Altera o § 1º do art. 74 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        8,
        1995,
        "1995-03-08",
        "1995-03-15",
        "2c907f76267b781a01269a5fa1330122",
        "EMENDA LOMBH-08-atual.doc",
        "Altera dispositivos da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        9,
        1995,
        "1995-04-24",
        "1995-05-16",
        "2c907f76267b781a01269a647bc00127",
        "EMENDA LOMBH-09-atual.doc",
        "Dá nova redação ao caput e aos incisos do artigo 80 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        10,
        1995,
        "1995-12-27",
        "1995-12-29",
        "2c907f76267b781a01269a683cb6012c",
        "EMENDA LOMBH-10-atual.doc",
        "Dá nova redação ao inciso III do art. 56 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        11,
        1996,
        "1996-01-02",
        "1996-01-04",
        "2c907f76267b781a0126ae6045360182",
        "EMENDA LOMBH-11-atual.doc",
        "Altera dispositivos da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        12,
        1996,
        "1996-03-12",
        "1996-03-14",
        "2c907f76267b781a0126ae72f6520193",
        "EMENDA LOMBH-12-atual.doc",
        "Acrescenta inciso ao art. 224 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        13,
        1998,
        "1998-09-04",
        "1998-09-24",
        "2c907f76267b781a0126ae769703019a",
        "EMENDA LOMBH-13-atual.doc",
        "Acrescenta inciso ao art. 85 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        14,
        1999,
        "1999-06-16",
        "1999-06-22",
        "2c907f76267b781a0126ae7a7307019f",
        "EMENDA LOMBH-14-atual.doc",
        "Dá nova redação ao art. 52 da Lei Orgânica do Município."
    ],
    [
        15,
        2000,
        "2000-03-22",
        "2000-03-25",
        "2c907f76267b781a0126ae7e0d7301a6",
        "EMENDA LOMBH-15-atual.doc",
        "Altera a redação do art. 164 da Lei Orgânica do Município."
    ],
    [
        16,
        2000,
        "2000-06-15",
        "2000-06-16",
        "2c907f76267b781a0126aef897d401f4",
        "EMENDA LOMBH-16-atual.doc",
        "Acrescenta dispositivo à Lei Orgânica do Município."
    ],
    [
        17,
        2001,
        "2001-09-17",
        "2001-07-11",
        "2c907f76267b781a0126aefb8e1701fb",
        "EMENDA LOMBH-17-atual.doc",
        "Dá nova redação ao art. 107 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        18,
        2004,
        "2004-04-07",
        "2004-04-10",
        "2c907f76267b781a0126af012d460201",
        "EMENDA LOMBH-18-atual.doc",
        "Acrescenta dispositivo ao art. 219 da LOMBH."
    ],
    [
        19,
        2006,
        "2006-01-05",
        "2006-01-05",
        "2c907f7629286aac012936c9448a0039",
        "EMENDA LOMBH-19-atual.doc",
        "Altera os artigos 56 e 87 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        20,
        2007,
        "2007-02-01",
        "2007-02-16",
        "2c907f76267b781a0126af07fc4a020d",
        "EMENDA LOMBH-20-atual.doc",
        "Altera a redação da alínea \"c\", do inciso X do art. 158 da Lei Orgânica do Município de Belo Horizonte - LOMBH - e dá outras providências."
    ],
    [
        21,
        2007,
        "2007-07-17",
        "2007-08-09",
        "2c907f76267b781a0126af0b7d250214",
        "EMENDA LOMBH-21-atual.doc",
        "Dá nova redação a dispositivo do art. 150 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        22,
        2010,
        "2010-06-01",
        "2010-06-02",
        "2c907f7629a36d3f012a0eb38d3d05f4",
        "EMENDA LOMBH-22-atual.doc",
        "Dá nova redação ao caput e ao § 1º do art. 34 da Lei Orgânica do Município de Belo Horizonte - LOMBH."
    ],
    [
        23,
        2011,
        "2011-09-13",
        "2011-09-15",
        "2c907f76324fb36c0132724e369200e2",
        "EMENDA LOMBH-23-atual.doc",
        "Acrescenta artigo à Lei Orgânica do Município, vedando a nomeação ou a designação para os cargos que menciona, daqueles inelegíveis em razão de atos ilícitos, nos termos da legislação federal."
    ],
    [
        24,
        2012,
        "2012-04-18",
        "2012-04-19",
        "2c907f76366547b40136cac2eb2e00b9",
        "EMENDA LOMBH-24-atual.doc",
        "Acrescenta à Lei Orgânica do Município de Belo Horizonte o art. 108-A e parágrafo único aos arts. 125 e 127."
    ],
    [
        25,
        2012,
        "2012-07-09",
        "2012-07-11",
        "2c907f76386dedad01387789a10b004c",
        "EMENDA LOMBH -25-atual.doc",
        "Dá nova redação ao § 2º  do art. 79 e do § 5º do art. 92 da Lei Orgânica do  Município de Belo Horizonte."
    ],
    [
        26,
        2012,
        "2012-12-28",
        "2012-12-29",
        "2c907f7691b2137a0191dd091010003a",
        "EMENDA LOMBH - 26-atual.doc",
        "Dá nova redação ao art. 160 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        27,
        2012,
        "2012-12-28",
        "2012-12-29",
        "2c907f763c002e8a013c06f38ad6002e",
        "EMENDA LOMBH - 27-atual.doc",
        "Dá nova redação ao § 2º do art. 219 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        28,
        2015,
        "2015-03-12",
        "2015-03-14",
        "2c907f764bc6de7f014c227f87a301d7",
        "emendalombh28.doc",
        "Dá nova redação ao art. 199 da Lei Orgânica do Município de Belo Horizonte - Lombh."
    ],
    [
        29,
        2016,
        "2016-02-29",
        "2016-03-02",
        "2c907f7653013875015337b808b30120",
        "EMLO-29-2016.doc",
        "Altera dispositivos do Capítulo XI do Título VI da Lei Orgânica do Município de Belo Horizonte, que dispõe sobre a Política Urbana."
    ],
    [
        30,
        2016,
        "2016-05-30",
        "2016-06-01",
        "2c907f7654cfab6201550cd4fa1500ab",
        "EMLO-30-2016.doc",
        "Acrescenta o § 1º-A ao art. 105 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        31,
        2018,
        "2018-12-27",
        "2018-12-28",
        "2c907f7667c5d0dc0168141897e40160",
        "EMLO-31-2018.doc",
        "Altera o inciso II do artigo 13; parágrafo único do artigo 20; inciso I do artigo 22; artigo 52; artigo 144; artigo 157; artigo 159; artigo 173; artigo 175; Capítulo IX, Seção II; artigo 177; artigo 181 e 229 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        32,
        2020,
        "2020-08-26",
        "2020-08-27",
        "2c907f767378fa0d01742fc2eace0185",
        "EMLO-32-2020.doc",
        "Altera o art. 80 da LOMBH, para incluir a licença-maternidade e a licença-paternidade, em razão de nascimento de filho ou de adoção."
    ],
    [
        33,
        2020,
        "2020-12-30",
        "2020-12-31",
        "2c907f76766722210176b93776c00136",
        "EMLO-33-2020.doc",
        "Acrescenta artigo ao Ato das Disposições Transitórias da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        34,
        2021,
        "2021-07-22",
        "2021-07-23",
        "2c907f767a80bf78017ad39b10d700d2",
        "EMLO-34-2021.doc",
        "Acrescenta os §§ 4º-A a 4º-J ao art. 132 da Lei Orgânica do Município de Belo Horizonte e acrescenta o art. 31-C ao Ato das Disposições Transitórias dessa lei."
    ],
    [
        35,
        2022,
        "2022-12-01",
        "2022-12-02",
        "2c907f76849a71d20184d299a8c400e6",
        "EMLO-35-2022.doc",
        "Acrescenta o art. 130-A à Lei Orgânica do Município de Belo Horizonte, altera a redação dos §§ 4°-A, 4°-C, 4°-G, 4°-H, 4°-I e 4°-J do seu art. 132 e acrescenta a esse artigo os §§ 4°-K, 4°-L, 4°-M e 4°-N."
    ],
    [
        36,
        2023,
        "2023-04-27",
        "2023-04-28",
        "2c907f7687b99fa20187c5d80725002f",
        "EMLO-36-2023.doc",
        "Acrescenta os §§ 5º, 6º e 7º ao art. 193 da LOMBH."
    ],
    [
        37,
        2023,
        "2023-06-07",
        "2023-06-08",
        "2c907f768895e6220188af426e760027",
        "EMLO-37-2023.doc",
        "Dá nova redação ao art. 70 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        38,
        2023,
        "2023-07-26",
        "2023-07-27",
        "2c907f7689557b920189970f6e1d0107",
        "EMLO-38-2023.doc",
        "Dá nova redação ao inciso IV e ao § 1º do art. 80 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        39,
        2023,
        "2023-08-02",
        "2023-08-03",
        "2c907f7689994ddc0189bb5a211600b4",
        "EMLO-39-2023.doc",
        "Altera o art. 110 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        40,
        2023,
        "2023-08-28",
        "2023-08-30",
        "2c907f768a41e43e018a46011efe0018",
        "EMLO-40-2023.doc",
        "Altera a redação dos §§ 4º-I e 4º-J do art. 132 da LOMBH."
    ],
    [
        41,
        2023,
        "2023-10-11",
        "2023-10-12",
        "2c907f768b13df8f018b255724d60053",
        "EMLO-41-2023.doc",
        "Dá nova redação ao art. 70 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        42,
        2024,
        "2024-03-06",
        "2024-03-07",
        "2c907f768dec5bbe018e187e91380079",
        "EMLO-42-2024.doc",
        "Altera o art. 193 da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        43,
        2025,
        "2025-03-10",
        "2025-03-11",
        "2c907f769543c08e01958a2eb4c300ac",
        "EMLO-43-2025-atual.doc",
        "Dá nova redação aos §§ 1° e 2° do art. 130-A da LOMBH."
    ],
    [
        44,
        2026,
        "2026-02-09",
        "2026-02-10",
        "2c907f769c2dea6c019c476b2f170033",
        "EMLO-44-2026.doc",
        "Acrescenta o § 10 ao art. 4° da Lei Orgânica do Município de Belo Horizonte."
    ],
    [
        45,
        2026,
        "2026-09-23",
        "2026-09-24",
        "2c907f76a0d2ca8c01a0d34e2a190003",
        "EMLO-45-2026.doc",
        "Acrescenta o § 5° ao art. 159 da Lei Orgânica do Município de Belo Horizonte."
    ]
]

# (nome oficial SIL, idDocDaNorma) — Anexos I a XIX da Lei 11.181/2019
ANEXOS_PLANO_DIRETOR = [
    [
        "lei11181 - Anexo I - Mapa de Estrutura Urbana Zoneamento.pdf",
        "2c907f766f673d3101701535698d01b9"
    ],
    [
        "lei11181 - Anexo II - Mapa de Estrutura Ambiental.pdf",
        "2c907f766f673d31017015358e0f01bb"
    ],
    [
        "lei11181 - Anexo III - Mapa de Áreas de Diretrizes Especiais.pdf",
        "2c907f766f673d3101701535b5c401bd"
    ],
    [
        "lei11181 - Anexo IV - Mapa de Projetos Estratégicos.pdf",
        "2c907f766f673d3101701535ddfe01bf"
    ],
    [
        "lei11181 - Anexo V - Mapa de Hierarquização do Sistema Viário.pdf",
        "2c907f766f673d31017015360d7c01c1"
    ],
    [
        "lei11181 - Anexo VI - Mapa Hierarquização do Sistema Viário - Permissividade - atual.pdf",
        "2c907f769543c08e0195950fca7a00c1"
    ],
    [
        "lei11181 - Anexo VII - 1 - ADE Bacia da Pampulha - Setores.pdf",
        "2c907f766f673d3101701536701b01c5"
    ],
    [
        "lei11181 - Anexo VII - 2 - ADE - Belvedere - Belvedere III uso - atual.pdf",
        "2c907f7693d91e490193da74ed4b0031"
    ],
    [
        "lei11181 - Anexo VII - 3 - ADE Mangabeiras uso.pdf",
        "2c907f766f673d31017015369dd701c9"
    ],
    [
        "lei11181 - Anexo VII - 4 - ADE São Bento - Setores usos - atual.pdf",
        "2c907f7693d91e490193da75143b0033"
    ],
    [
        "lei11181 - Anexo VII - 5 - ADE Buritis - Setores.pdf",
        "2c907f766f673d3101701536c58d01cd"
    ],
    [
        "lei11181 - Anexo VII - 6 - ADE Mirantes - Setores.pdf",
        "2c907f766f673d3101701536e70901cf"
    ],
    [
        "lei11181 - Anexo VII - 7 - ADE Contorno - Setores e ADEs.pdf",
        "2c907f766f673d3101701537024001d1"
    ],
    [
        "lei11181 - Anexo VII - 8 - ADE Distrito da moda - Setores.pdf",
        "2c907f766f673d31017015371ac801d3"
    ],
    [
        "lei11181 - Anexo VII - 9a - ADE Pampulha - Usos - atual.pdf",
        "2c907f7693d91e490193da75479d0035"
    ],
    [
        "lei11181 - Anexo VII - 9b - ADE  Pampulha - Setor Lagoa da Pampulha.pdf",
        "2c907f766f673d31017015374e1e01d7"
    ],
    [
        "lei11181 - Anexo VII - 10 - ADE Santa Tereza - Setores usos.pdf",
        "2c907f766f673d310170153764a501d9"
    ],
    [
        "lei11181 - Anexo VII - 11 - ADE Região da Lagoinha - Setores - atual.pdf",
        "2c907f7693d91e490193da755ecd0037"
    ],
    [
        "lei11181 - Anexo VII - 12 - ADE Cidade Jardim uso.pdf",
        "2c907f766f673d310170153797f901dd"
    ],
    [
        "lei11181 - Anexo VII - 13 - ADE Venda Nova - Setores.pdf",
        "2c907f766f673d3101701537c34401df"
    ],
    [
        "lei11181 - Anexo VIII - Mapa Classificação de calçadas.pdf",
        "2c907f766f673d3101701537e0e001e1"
    ],
    [
        "lei11181 - Anexo IX - Rede Cicloviária.pdf",
        "2c907f766f673d3101701537f95e01e3"
    ],
    [
        "lei11181 - Anexo X - Mapa da Rede Estruturante de Transporte Coletivo.pdf",
        "2c907f766f673d31017015381a1401e5"
    ],
    [
        "lei11181 - Anexo XI - Glossário.pdf",
        "2c907f766f673d31017015384fcd01e7"
    ],
    [
        "lei11181 - Anexo XII - Parâmetros urbanísticos-atual.doc",
        "2c907f7693d91e4901941d3a5af00154"
    ],
    [
        "lei11181 - Anexo XIII - Classificação das Atividades - atual.pdf",
        "2c907f7693d91e490193df87f7290053"
    ],
    [
        "lei11181 - Anexo XIV - Localização dos usos.pdf",
        "2c907f766f673d3101701538a90401ed"
    ],
    [
        "lei11181 - Anexo XV - Atividades Vedadas.xls",
        "2c907f766f673d3101701538fd0901ef"
    ],
    [
        "lei11181 - Anexo XVI - Penalidades - atual.doc",
        "2c907f76701a303001701a420f68000d"
    ],
    [
        "lei11181 - Anexo XVII - Coeficientes de Aproveitamento - Básico de Transição.pdf",
        "2c907f766f673d3101701539459f01f3"
    ],
    [
        "lei11181 - Anexo XVIII - Operação Urbana Simplificada Vila Monte São José.pdf",
        "2c907f766f673d3101701539a33101f5"
    ],
    [
        "lei11181 - Anexo XIX - Parâmetros Urbanísticos da Operação Urbana Vila Monte São José.doc",
        "2c907f766f673d3101701539d0ef01f7"
    ]
]


def url_download(id_doc):
    return DOWNLOAD + "?idDocDaNorma=" + id_doc


def url_ficha(tipo_slug, numero, ano):
    return f"{CATALOGO_PAGINA}/{tipo_slug}/{numero}/{ano}"


def data_por_extenso(iso):
    ano, mes, dia = (int(p) for p in iso.split("-"))
    return f"{dia} de {MESES[mes - 1]} de {ano}"


def cache_anexo(nome):
    raiz, ext = os.path.splitext(nome)
    return slugify(normalizar_chave(raiz).replace(" ", "-")) + ext.lower()


def parse_pesquisa(html):
    """Extrai ficha SIL devolvida por pesquisar.php (via proxy Drupal)."""
    if re.search(r"Nenhum resultado encontrado|não retornou uma legislação válida", html, re.I):
        return None
    h2 = re.search(r"<h2>(.*?)</h2>", html)
    if not h2:
        return None
    docs = []
    for m in re.finditer(
            r'<li><span>(.*?)</span><a href="(https://cmbhsildownload[^"]+idDocDaNorma=([^"&]+))"',
            html):
        docs.append({"nome": htmlmod.unescape(m.group(1)), "url": m.group(2), "id": m.group(3)})
    ementa = re.search(r"<strong>Ementa:</strong>\s*(.*?)</p>", html, re.S)
    datas = [(k, htmlmod.unescape(v).strip())
             for k, v in re.findall(r"<strong>Data da (promulgação|publicação): </strong>(.*?)</li>", html)]
    nova = re.search(r"<span id='novaUrl'[^>]*>(.*?)</span>", html)
    return {
        "titulo": htmlmod.unescape(h2.group(1)),
        "ementa": htmlmod.unescape(re.sub("<[^>]+>", "", ementa.group(1))).strip() if ementa else None,
        "datas": datas,
        "docs": docs,
        "fonte": htmlmod.unescape(nova.group(1)).strip() if nova else None,
    }


def campos_pesquisa(tipo, numero, ano):
    return {
        "metodo": "", "paginaRequerida": "1", "urlNorma": "", "idNorma": "",
        "buscarEmendas": "", "buscaViaUrl": "1", "mobile": "0",
        "tipoDeNorma": tipo, "numero": str(numero), "ano": str(ano),
        "assunto": "", "assunto2": "", "autoria": "", "tema": "",
    }


def pesquisar(rede, tipo, numero, ano):
    body = urllib.parse.urlencode(campos_pesquisa(tipo, numero, ano)).encode()
    req_headers = {**rede.headers, "Content-Type": "application/x-www-form-urlencoded",
                   "Referer": CATALOGO_PAGINA}
    from urllib.request import Request, urlopen
    rede.limite.esperar()
    req = Request(PESQUISAR, data=body, headers=req_headers)
    with urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", "replace")
    return parse_pesquisa(html)


def binario_oficial(bruto):
    return bruto.startswith(OLE) or bruto.startswith(b"%PDF")


def baixar(rede, url, destino, timeout=180):
    if destino.exists() and destino.stat().st_size > 32:
        return destino.read_bytes()
    st, bruto, _ = rede.get(url, tentativas=2, timeout=timeout)
    if st != 200 or not binario_oficial(bruto):
        raise ValueError(f"fonte indisponível ou não é PDF/DOC/XLS oficial: HTTP {st} {url}")
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("xb") as f:
        f.write(bruto)
    return bruto


def converter_oficial(bruto, url):
    from baixar_capitais_documentos import documento_oficial_para_md
    return documento_oficial_para_md(bruto, url)


def corpo_emenda_reconhecivel(corpo):
    if re.search(r"art(?:igo)?\.?\s*1(?:[º°o]|\b)", corpo, re.I):
        return True
    return bool(len(corpo) > 400
                and re.search(r"\bpromulg(?:o|a|am|amos)\b", corpo, re.I)
                and re.search(r"vigorar|vigor|Lei Orgânica", corpo, re.I))


def gravar_md(destino, meta, corpo):
    texto = "\n".join(["---"] + [k + ": " + yaml_str(v) for k, v in meta.items()]
                      + ["revogada: null", "---", "", "# " + meta["titulo"], "", corpo, ""])
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("x") as f:
        f.write(texto)
    return texto


def materializar_emendas(rede=None):
    ibge_path = RAIZ / "municipais/_indice/ibge-municipios.json"
    ibge = {str(x["id"]): x for x in json.loads(ibge_path.read_text())}
    municipio = ibge[IBGE_BH]
    uf = municipio["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]
    if municipio["nome"] != "Belo Horizonte" or uf != "MG":
        raise ValueError("identidade IBGE diverge do município de Belo Horizonte")
    slug = normalizar_chave(municipio["nome"]).replace(" ", "-")
    pasta = RAIZ / "municipais/_fonte/capitais" / slug / "emendas-lei-organica"
    pasta.mkdir(parents=True, exist_ok=True)
    rede = rede or Rede(rps=3, headers={"Referer": CATALOGO_PAGINA})
    gravados = pulados = 0
    for numero, ano, data, publicacao, id_doc, arquivo, ementa in EMENDAS:
        slug_md = f"emendas-lei-organica-{numero}-{ano}"
        destino = (RAIZ / "municipais" / uf / slug / "emendas-lei-organica" / str(ano)
                   / (slug_md + ".md"))
        if destino.exists():
            print("já existente", destino, flush=True)
            pulados += 1
            continue
        fonte_texto = url_download(id_doc)
        fonte = url_ficha("emenda-a-lei-organica", numero, ano)
        cache = pasta / f"{slug_md}.doc"
        bruto = baixar(rede, fonte_texto, cache)
        corpo, motivo = converter_oficial(bruto, fonte_texto)
        if motivo:
            raise ValueError(f"emenda {numero}/{ano}: {motivo}")
        if not corpo_emenda_reconhecivel(corpo):
            raise ValueError(f"emenda {numero}/{ano}: corpo sem artigo inicial nem cláusula de vigência")
        titulo = (f"Emenda à Lei Orgânica nº {numero}, de {data_por_extenso(data)}")
        meta = {
            "titulo": titulo,
            "tipo": "Emenda à Lei Orgânica",
            "tipo_na_fonte": "Emenda à Lei Orgânica",
            "numero": str(numero),
            "data": data,
            "data_publicacao": publicacao,
            "municipio": "Belo Horizonte",
            "uf": "MG",
            "codigo_ibge": IBGE_BH,
            "versao_texto": (f"texto integral oficial do SIL da CMBH ({arquivo}); "
                             f"promulgação {data} e publicação {publicacao}; "
                             "não certifica atualização posterior"),
            "fonte": fonte,
            "fonte_texto": fonte_texto,
            "sha256_fonte": hashlib.sha256(bruto).hexdigest(),
            "sha256_texto": hashlib.sha256(corpo.encode()).hexdigest(),
            "baixado_em": dt.date.today().isoformat(),
        }
        texto = gravar_md(destino, meta, corpo)
        comprovacao = {
            "municipio": "Belo Horizonte", "uf": "MG", "codigo_ibge": IBGE_BH,
            "tipo": "Emenda à Lei Orgânica", "categoria": "emendas-lei-organica",
            "numero": str(numero), "data": data, "data_publicacao": publicacao,
            "titulo": titulo, "slug": slug_md, "arquivo_sil": arquivo,
            "ementa_sil": ementa, "fonte": fonte, "fonte_texto": fonte_texto,
            "sil_id_doc_da_norma": id_doc, "sil_tipo_id": TIPO_EMENDA,
            "arquivo": str(destino.relative_to(RAIZ)),
            "sha256": hashlib.sha256(texto.encode()).hexdigest(),
            "arquivo_fonte": str(cache.relative_to(RAIZ)),
            "sha256_fonte": meta["sha256_fonte"], "sha256_corpo": meta["sha256_texto"],
            "ibge_sha256": hashlib.sha256(ibge_path.read_bytes()).hexdigest(),
            "verificado_em": dt.datetime.now().isoformat(),
            "observacao": "Série 1–45 do SIL; datas da ficha oficial, não das notas da compilação da LO.",
        }
        with (pasta / (slug_md + ".manifesto.json")).open("x") as f:
            json.dump(comprovacao, f, ensure_ascii=False, indent=2)
        print("gravado", destino, flush=True)
        gravados += 1
    return {"gravados": gravados, "pulados": pulados, "catalogo": len(EMENDAS)}


def main():
    print(json.dumps(materializar_emendas(), ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
