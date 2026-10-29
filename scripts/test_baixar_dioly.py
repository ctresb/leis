import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar_dioly import (
    blocos_emenda, eh_promulgada, data_do_bloco, titulo_do_bloco, gravar_emenda,
    recortar_ato, EPIGRAFE, SALA, blocos_lc, eh_lc_promulgada, data_do_gabinete,
    titulo_lc, caminho_pdf, nota_lc, blocos_lo, lo_contemporanea, titulo_lo, marcar_ilegivel,
)

ELO_2013 = """
ATOS DO PODER LEGISLATIVO

EMENDA Nº 30 À LEI ORGÂNICA
DO MUNICÍPIO DO SALVADOR
Altera dispositivo da Lei Orgânica
do Município de Salvador - LOM.
A Mesa da Câmara Municipal do Salvador faz saber que o
Poder Legislativo Municipal promulga e manda publicar, para
os devidos efeitos, a seguinte Emenda à Lei Orgânica do Município:
Art.1º O § 2º do art. 35 da Lei Orgânica do Município
de Salvador - LOM passa a vigorar com a seguinte redação:
“Art. 35º ................................................................
§ 2º A Câmara elegerá a 02 de janeiro a Mesa Executiva, constituída de 01 (um) Presidente, 03 (três)
Vice-Presidentes, 04 (quatro) Secretários, 01 (um)
Corregedor e 01 (um) Ouvidor, para o mandato de
02 (dois) anos, admitida a reeleição, observando-se:
....................” (NR)
Art. 2º Esta Emenda à LOM entra em vigor na data
de sua publicação, prevalecendo seus efeitos a partir
de 1º de janeiro de 2015.
Sala das Sessões, em 16 de dezembro de 2013.
Paulo Câmara
Presidente
"""

PROJETO = """
PROJETO DE EMENDA À LEI ORGÂNICA Nº 03/2020
Acrescenta, altera e revoga os dispositivos da Lei Orgânica.
A CÂMARA MUNICIPAL DE SALVADOR
DECRETA:
Art. 1º Os incisos XVI, XXIII e XXVII do art. 7° passam a vigorar
com a seguinte redação.
Art. 30. Esta Emenda entra em vigor na data de sua publicação.
Sala da Comissão, 22 de julho de 2020.
"""

BALANCO = """
PRODUÇÃO LEGISLATIVA 2023
EMENDA À LEI ORGÂNICA DO MUNICIPIO PROMULGADA                                      2
LEIS PROMULGADAS                                                                   0
PROJETOS DE EMENDA
"""

ORCAMENTO = """
relativas às emendas individuais (art. 166-A)
01.031.0012.234800      Gestão de Emendas
Lei Orgânica do Município do Salvador (Art. 191)
"""


class DiolyEmendasTest(unittest.TestCase):
    def test_promulgada_2013(self):
        achados = blocos_emenda(ELO_2013)
        self.assertEqual(len(achados), 1)
        self.assertEqual(achados[0][0], "30")
        self.assertIn("promulga e manda publicar", achados[0][1])
        self.assertEqual(data_do_bloco(achados[0][1], "30", "2013-12-27"), "2013-12-16")
        self.assertIn("16 de dezembro de 2013", titulo_do_bloco(achados[0][1], "30", "2013-12-16"))
        self.assertNotIn("Câmara vai aos Bairros", achados[0][1])

    def test_corta_jornal_depois_da_sala(self):
        texto = ELO_2013 + "\nCriado pela Lei 4.429 de 19 de novembro de 1991\nCâmara vai aos Bairros\n"
        bloco = blocos_emenda(texto)[0][1]
        self.assertIn("Sala das Sessões, em 16 de dezembro de 2013", bloco)
        self.assertNotIn("Câmara vai aos Bairros", bloco)
        self.assertNotIn("Criado pela Lei", bloco)

    def test_projeto_descartado(self):
        self.assertFalse(eh_promulgada(PROJETO))
        self.assertEqual(blocos_emenda(PROJETO), [])

    def test_estatistica_descartada(self):
        self.assertEqual(blocos_emenda(BALANCO), [])

    def test_promulgada_com_formula_partida(self):
        texto = """EMENDA Nº36 À LEI ORGÂNICA DO MUNICÍPIO DO SALVADOR
Modifica regras relativas ao Regime Próprio.
A Mesa da Câmara Municipal do Salvador faz saber que o
Poder Legislativo Municipal promulga e manda publicar, para os
devidos efeitos, a seguinte
Art. 1º O art. 261 passa a vigorar com a seguinte redação.
Art. 2º Esta Emenda entra em vigor na data da sua publicação.
Sala das Sessões, em 20 de março de 2020.
"""
        achados = blocos_emenda(texto)
        self.assertEqual([n for n, _ in achados], ["36"])

    def test_nao_casa_numero_solto_depois_da_epigrafe(self):
        texto = "Emenda à Lei Orgânica\n                25 de abril de 1990, passa a vigorar"
        self.assertIsNone(EPIGRAFE.search(texto))

    def test_emenda_orcamentaria_descartada(self):
        self.assertEqual(blocos_emenda(ORCAMENTO), [])

    def test_projeto_e_promulgada_na_mesma_edicao(self):
        texto = PROJETO + "\n\n" + ELO_2013
        achados = blocos_emenda(texto)
        self.assertEqual([n for n, _ in achados], ["30"])

    def test_recorta_expediente_depois_das_assinaturas(self):
        texto = ELO_2013 + (
            "\nvereadora Andréa Mendonça, 329 e 330/10 do vereador Téo Senna\n"
            "Terminada a leitura do Expediente, passando à Ordem do Dia\n"
        )
        bloco = recortar_ato(blocos_emenda(texto)[0][1])
        self.assertIn("Paulo Câmara", bloco)
        self.assertNotIn("Expediente", bloco)
        self.assertNotIn("Andréa Mendonça", bloco)

    def test_nao_corta_no_meio_por_cabecalho_de_pagina(self):
        texto = """EMENDA Nº 37 À LEI ORGÂNICA DO MUNICÍPIO DO SALVADOR
Altera dispositivos da Lei Orgânica.
A Mesa da Câmara Municipal do Salvador faz saber que o
Poder Legislativo Municipal promulga e manda publicar, para
os devidos efeitos, a seguinte Emenda à Lei Orgânica do Município:
Art. 1º O art. 10 passa a vigorar com a seguinte redação.
Sexta-feira,
12 de Fevereiro de 2021
Ano XXX
N° 5.899
Art. 2º Esta Emenda entra em vigor na data de sua publicação.
Sala das Sessões, em 22 de dezembro de 2020.
Geraldo Júnior
Presidente
"""
        achados = blocos_emenda(texto)
        self.assertEqual([n for n, _ in achados], ["37"])
        self.assertIn("Art. 2º", achados[0][1])
        self.assertTrue(SALA.search(achados[0][1]))
        self.assertEqual(data_do_bloco(achados[0][1], "37", "2021-02-12"), "2020-12-22")

    def test_data_com_o_no_lugar_do_zero(self):
        texto = ELO_2013.replace("16 de dezembro de 2013", "o5 de agosto de 2015")
        bloco = blocos_emenda(texto)[0][1]
        self.assertEqual(data_do_bloco(bloco, "30", "2015-09-02"), "2015-08-05")

    def test_gravar_campos_obrigatorios(self):
        import tempfile
        from pathlib import Path
        bloco = blocos_emenda(ELO_2013)[0][1]
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "e.md"
            gravar_emenda(dest, {
                "titulo": "Emenda à Lei Orgânica nº 30, de 16 de dezembro de 2013",
                "tipo": "Emenda à Lei Orgânica",
                "numero": "30",
                "data": "2013-12-16",
                "versao_texto": "publicação original",
                "fonte": "https://portal-api.dioly.com.br/uploads/pdfs/x.pdf",
                "baixado_em": "2026-10-28",
            }, bloco + "\n")
            texto = dest.read_text()
            self.assertTrue(texto.startswith("---\n"))
            self.assertIn("# Emenda à Lei Orgânica nº 30", texto)
            from auditar import validar
            import datetime as dt
            erros, avisos = validar(texto, "municipais/BA/salvador/emendas-lei-organica/2013/x.md",
                                    dt.date(2026, 10, 28))
            self.assertEqual(erros, [], avisos)


LC_075 = """
EXECUTIVO
LEIS COMPLEMENTARES
LEI COMPLEMENTAR Nº 075/2020
Modifica as regras do Regime Próprio de
Previdência Social do Município de Salvador,
promove alterações para implementar o Programa
de Renovação da Previdência e dá outras
providências.
O PREFEITO MUNICIPAL DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º O Regime Próprio de Previdência Social - RPPS do Município de Salvador
fica alterado por meio desta Lei Complementar.
Art. 40. Esta Lei Complementar entra em vigor na data de sua publicação.
GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 30 de março de 2020.
ANTONIO CARLOS PEIXOTO DE MAGALHÃES NETO
Prefeito
DECRETOS FINANCEIROS
DECRETO Nº 32.000 de 30 de março de 2020
Abre crédito.
"""

LC_PROJETO = """
PROJETO DE LEI COMPLEMENTAR Nº 02/16
Dispõe sobre o regime de pessoal na forma que indica e dá outras providências.
O PREFEITO MUNICIPAL DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei Complementar:
Art. 1º Ficam alterados o caput e o § 1º.
Sala das Comissões, 14 de dezembro de 2016.
"""

LC_CITACAO = """
PORTARIA Nº 627/2023
O Secretário, no uso de suas atribuições e com fundamento no
artigo 3º da Lei Complementar nº 075/2020, cabendo à Diretoria de
Previdência a fixação de sua renda mensal na inatividade.
GABINETE DO SECRETÁRIO MUNICIPAL DE GESTÃO.
Em 28 de julho de 2023.
"""

LC_089_ORIG = """
LEI COMPLEMENTAR Nº 089/2025
Modifica a Estrutura Organizacional da Prefeitura
Municipal de Salvador - PMS.
O PREFEITO DO MUNICÍPIO DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º Fica alterada a Estrutura Organizacional.
Art. 2º Esta Lei Complementar entra em vigor na data de sua publicação.
GABINETE DO PREFEITO DO MUNICÍPIO DO SALVADOR, em 01 de janeiro de 2025.
BRUNO SOARES REIS
Prefeito
"""

LC_089_REP = """
LEI COMPLEMENTAR Nº 089/2025
Publicada no DOM de 31/12/2024 a 02/01/2025.
Republicada por ter saído com incorreção.
Modifica a Estrutura Organizacional da Prefeitura
Municipal de Salvador - PMS, altera e acrescenta
dispositivo à Lei Complementar nº 33, de 17 de
julho de 2002, e dá outras providências.
O PREFEITO DO MUNICÍPIO DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º Fica alterada a Estrutura Organizacional da Prefeitura Municipal de Salvador.
Art. 20. Esta Lei Complementar entra em vigor na data de sua publicação.
GABINETE DO PREFEITO DO MUNICÍPIO DO SALVADOR, em 01 de janeiro de 2025.
BRUNO SOARES REIS
Prefeito
"""

LC_DUAS = """
LEI COMPLEMENTAR N° 057/2012
Institui novos critérios para o Prêmio por Desempenho Fazendário e dá outras providências.
O PREFEITO MUNICIPAL DO SALVADOR, CAPITAL DO ESTADO
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º O Prêmio por Desempenho Fazendário fica instituído.
GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 03 de abril de 2012.
João Henrique
Prefeito
LEI COMPLEMENTAR N° 058/2012
Altera os dispositivos que indica da Lei Complementar n° 01, de 15 de março de 1991.
O PREFEITO MUNICIPAL DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º Fica alterado o art. 61.
GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 03 de abril de 2012.
João Henrique
Prefeito
DECRETO Nº 1 de 3 de abril de 2012
"""


LC_EMENTA_QUEBRA = """
LEI COMPLEMENTAR Nº 082/2022
Dispõe sobre a avaliação prevista nos artigos 34
da Lei nº 7.867, de 12 de julho de 2010, e 48 da
Lei nº 8.629, de 14 de julho de 2014, e dá outras
providências.
O PREFEITO DO MUNICÍPIO DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º A Administração Municipal promoverá a avaliação.
Art. 2º Esta Lei Complementar entra em vigor na data de sua publicação.
GABINETE DO PREFEITO DO MUNICÍPIO DO SALVADOR, em 20 de julho de 2022.
BRUNO SOARES REIS
Prefeito
DECRETO Nº 35.000 de 21 de julho de 2022
Abre crédito.
"""


LO_9831 = """
EXECUTIVO
LEIS
LEI Nº 9.831/2025
Confere ao advogado constituído prerrogativas.
O PREFEITO DO MUNICÍPIO DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º Esta Lei dispõe sobre a juntada de documentos por advogados.
Art. 2º Esta Lei entra em vigor na data de sua publicação.
GABINETE DO PREFEITO DO MUNICÍPIO DO SALVADOR, em 11 de março de 2025.
BRUNO SOARES REIS
Prefeito
LEI COMPLEMENTAR Nº 090/2025
Altera a Lei Complementar nº 36.
O PREFEITO DO MUNICÍPIO DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º Fica alterado.
GABINETE DO PREFEITO DO MUNICÍPIO DO SALVADOR, em 11 de março de 2025.
DECRETOS FINANCEIROS
DECRETO Nº 39.918 de 11 de março de 2025
Abre crédito. Conforme LEI Nº 7.186/2006 e Lei nº 9.640, de 19 de maio de 2022.
"""

LO_EDITAL_ANTIGA = """
ANEXO XI - EDITAL DE CREDENCIAMENTO Nº. 001/2024
LEI Nº. 9283/2017
Regula e disciplina o SETAX.
O PREFEITO MUNICIPAL DO SALVADOR, CAPITAL DO ESTADO DA BAHIA, Faço saber
que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º Esta Lei disciplina o SETAX.
GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 21 de novembro de 2017.
"""


class DiolyLeisComplementaresTest(unittest.TestCase):
    def test_nao_corta_ementa_que_cita_lei_ordinaria(self):
        achados = blocos_lc(LC_EMENTA_QUEBRA)
        self.assertEqual([(n, a) for n, a, _ in achados], [("82", "2022")])
        self.assertIn("Art. 1º", achados[0][2])
        self.assertIn("GABINETE DO PREFEITO", achados[0][2])
        self.assertNotIn("DECRETO Nº 35.000", achados[0][2])

    def test_lc_promulgada_2020(self):
        achados = blocos_lc(LC_075)
        self.assertEqual([(n, a) for n, a, _ in achados], [("75", "2020")])
        self.assertIn("sanciono a seguinte Lei", achados[0][2])
        self.assertIn("Art. 1º", achados[0][2])
        self.assertNotIn("DECRETOS FINANCEIROS", achados[0][2])
        self.assertEqual(data_do_gabinete(achados[0][2], "2020-03-30"), "2020-03-30")
        self.assertIn("30 de março de 2020", titulo_lc("75", "2020-03-30"))

    def test_projeto_lc_descartado(self):
        self.assertEqual(blocos_lc(LC_PROJETO), [])
        self.assertFalse(eh_lc_promulgada(LC_PROJETO))

    def test_citacao_descartada(self):
        self.assertEqual(blocos_lc(LC_CITACAO), [])

    def test_duas_lc_na_mesma_edicao(self):
        achados = blocos_lc(LC_DUAS)
        self.assertEqual([(n, a) for n, a, _ in achados], [("57", "2012"), ("58", "2012")])
        self.assertIn("Prêmio por Desempenho", achados[0][2])
        self.assertNotIn("LEI COMPLEMENTAR N° 058", achados[0][2])

    def test_republicada_vence_original(self):
        self.assertGreater(nota_lc(LC_089_REP), nota_lc(LC_089_ORIG))
        achados = blocos_lc(LC_089_REP)
        self.assertEqual(achados[0][0], "89")
        self.assertIn("Republicada", achados[0][2])

    def test_gabinete_com_ocr_salvador(self):
        texto = LC_075.replace(
            "GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 30 de março de 2020.",
            "GABINETE DO PREFEITO DO MUNICÍPIO DO SALVBADOR, em 30 de março de 2020.",
        )
        achados = blocos_lc(texto)
        self.assertEqual([(n, a) for n, a, _ in achados], [("75", "2020")])

    def test_caminho_pdf_usa_tipo(self):
        from pathlib import Path
        dom = caminho_pdf(Path("/tmp"), {"data_publicacao": "2020-03-30", "tipo": "DOM", "numero": 7611, "id": 1})
        dol = caminho_pdf(Path("/tmp"), {"data_publicacao": "2013-12-27", "tipo": "DOL", "numero": 4211, "id": 2})
        self.assertEqual(dom.name, "2020-03-30-DOM-7611.pdf")
        self.assertEqual(dol.name, "2013-12-27-DOL-4211.pdf")

    def test_gravar_lc_passa_auditoria(self):
        import tempfile
        import datetime as dt
        from pathlib import Path
        from auditar import validar
        bloco = blocos_lc(LC_075)[0][2]
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "lc.md"
            gravar_emenda(dest, {
                "titulo": titulo_lc("75", "2020-03-30"),
                "tipo": "Lei Complementar",
                "numero": "75",
                "data": "2020-03-30",
                "versao_texto": "publicação original no Diário Oficial do Município (CMS/Dioly)",
                "fonte": "https://portal-api.dioly.com.br/uploads/pdfs/x.pdf",
                "baixado_em": "2026-10-28",
            }, bloco + "\n")
            erros, avisos = validar(dest.read_text(),
                                    "municipais/BA/salvador/leis-complementares/2020/x.md",
                                    dt.date(2026, 10, 28))
            self.assertEqual(erros, [], avisos)


class DiolyLeisOrdinariasTest(unittest.TestCase):
    def test_lo_sancionada_sem_lc_nem_decreto(self):
        achados = blocos_lo(LO_9831)
        self.assertEqual([(n, a) for n, a, _ in achados], [("9831", "2025")])
        bloco = achados[0][2]
        self.assertIn("Art. 1º", bloco)
        self.assertNotIn("COMPLEMENTAR", bloco)
        self.assertNotIn("DECRETO", bloco)
        self.assertEqual(lo_contemporanea(bloco, "2025", "2025-03-12"), "2025-03-11")
        self.assertEqual(titulo_lo("9831", "2025-03-11"), "Lei nº 9831, de 11 de março de 2025")

    def test_glifo_sem_unicode_vira_marcador(self):
        saida = marcar_ilegivel("Art. 1º Texto.\nŶĞǆŽy͗'ƌĂƵĚĞƉůŝĐĂĕĆŽ\nƐƉĞĐŝĂůŝƐƚĂ\nFim.")
        self.assertEqual(saida.splitlines(),
                         ["Art. 1º Texto.", "[trecho ilegível no PDF: fonte sem mapa Unicode]", "Fim."])

    def test_lei_antiga_em_edital_descartada(self):
        achados = blocos_lo(LO_EDITAL_ANTIGA)
        self.assertEqual([(n, a) for n, a, _ in achados], [("9283", "2017")])
        self.assertEqual(lo_contemporanea(achados[0][2], "2017", "2024-01-05"), "")


from baixar_dioly import blocos_mesa, data_sala, titulo_mesa, recortar_mesa  # noqa: E402

RES_2026 = """ATOS DO PODER LEGISLATIVO
RESOLUÇÃO Nº 3.622/2026
Concede a Medalha Tomé de Souza à Sra. Suzana Mamede.
A Mesa da Câmara Municipal do Salvador faz saber que o Poder Legislativo Municipal
promulga e manda publicar, para os devidos efeitos, a seguinte Resolução:
Art. 1º Fica concedida a Medalha Tomé de Souza à Sra. Suzana Mamede, em reconhecimen-
to aos relevantes serviços prestados ao Município de Salvador.
Art. 4º Esta Resolução entra em vigor na data de sua publicação.
Sala das Sessões, em 06 de outubro de 2026.
CARLOS MUNIZ
Presidente
Cláudio Tinoco \t\t\t RICARDO ALMEIDA
1º Secretário \t\t\t\t 2º Secretário
ATOS DO PRESIDENTE
ATO Nº 821/2026
O PRESIDENTE DA CÂMARA MUNICIPAL DE SALVADOR, no uso de suas atribuições
RESOLVE:
Art. 1º Fica renovado o reconhecimento de utilidade pública municipal
"""

RES_2010 = """Resolução nº 1.971/2010
Institui a Frente Parlamentar em Defesa da Vida.
A MESA DA CÂMARA MUNICIPAL DO SALVADOR faz saber que o Poder
Legislativo Municipal promulga e manda publicar, para os devidos efeitos, a
seguinte RESOLUÇÃO:
Art. 1º Fica instituída a Frente Parlamentar.
Art. 8º Esta Resolução entra em vigor na data de sua publicação.
Sala das Sessões, em 03 de fevereiro de 2010.
Alan Sanches
Presidente
Sidelvan Nóbrega Vânia Galvão
1º Secretário 2ª Secretária
Resolução nº 1.972/2010
Institui a Frente Parlamentar de Prevenção.
A MESA DA CÂMARA MUNICIPAL DO SALVADOR faz saber que o Poder
Legislativo Municipal promulga e manda publicar, para os devidos efeitos, a
seguinte RESOLUÇÃO:
Art. 1º Fica instituída a Frente Parlamentar de Prevenção.
Sala das Sessões, em 03 de fevereiro de 2010.
Alan Sanches
Presidente
"""

DL_2026 = """ATOS DO PODER LEGISLATIVO
DECRETO LEGISLATIVO Nº 990/2026
Altera o Decreto Legislativo nº 811, de 31 de outubro de
1996.
A MESA DA CÂMARA MUNICIPAL DO SALVADOR faz saber que o Poder Legislati-
vo Municipal promulga e manda publicar, para os devidos efeitos, o seguinte DECRETO
LEGISLATIVO:
Art. 1º O Art. 4° do Decreto Legislativo nº 811, de 31 de outubro de 1996, passa a vigorar
com a seguinte redação:
Art. 3º. Este Decreto Legislativo entra em vigor Lei na data de sua publicação.
Sala das Sessões, em 13 de maio de 2026.
CARLOS MUNIZ
Presidente
ATO Nº 813/2026
"""

RUIDO_MESA = """Projeto de Decreto Legislativo n. 1/25. Subiu à Tribuna, para Parecer.
Na sequência, foi promulgado o Decreto Legislativo n. 989/25. Em co-
Foram promulgadas as Resoluções n.s 3.563 a 3.567/26.
PROJETO DE RESOLUÇÃO Nº 45/2026
Altera o Regimento.
Art. 1º Fica alterado.
Sala das Sessões, em 13 de maio de 2026.
buições e de conformidade com o Decreto Legislativo n.º 811/96, RESOLVE:
PRODUÇÃO LEGISLATIVA - JANEIRO A DEZEMBRO 2024
PROJETOS DE
DECRETO LEGISLATIVO
"""


class TestMesa(unittest.TestCase):
    def test_resolucao_caixa_alta_corta_no_ato_seguinte(self):
        achados, desc = blocos_mesa(RES_2026, "resolucoes")
        self.assertEqual([(n, a) for n, a, _ in achados], [("3622", "2026")])
        bloco = achados[0][2]
        self.assertTrue(bloco.startswith("RESOLUÇÃO Nº 3.622/2026"))
        self.assertIn("2º Secretário", bloco)
        self.assertNotIn("ATOS DO PRESIDENTE", bloco)
        self.assertNotIn("utilidade pública", bloco)
        self.assertEqual(desc, [])

    def test_resolucao_2010_titulo_misto(self):
        achados, _ = blocos_mesa(RES_2010, "resolucoes")
        self.assertEqual([(n, a) for n, a, _ in achados], [("1971", "2010"), ("1972", "2010")])
        self.assertNotIn("1.972", achados[0][2])

    def test_decreto_legislativo(self):
        achados, _ = blocos_mesa(DL_2026, "decretos-legislativos")
        self.assertEqual([(n, a) for n, a, _ in achados], [("990", "2026")])
        self.assertNotIn("ATO Nº 813", achados[0][2])
        self.assertEqual(blocos_mesa(DL_2026, "resolucoes")[0], [])

    def test_ruido_nao_entra(self):
        for serie in ("resolucoes", "decretos-legislativos"):
            self.assertEqual(blocos_mesa(RUIDO_MESA, serie)[0], [])

    def test_data_sala_no_ano(self):
        bloco = blocos_mesa(RES_2026, "resolucoes")[0][0][2]
        self.assertEqual(data_sala(bloco, "2026", "2026-10-08"), "2026-10-06")
        self.assertEqual(data_sala(bloco, "2025", "2026-10-08"), "")
        self.assertEqual(data_sala(bloco, "2026", "2028-10-08"), "")

    def test_titulo(self):
        self.assertEqual(titulo_mesa("Decreto Legislativo", "990", "2026-05-13"),
                         "Decreto Legislativo nº 990, de 13 de maio de 2026")

    def test_ata_no_meio_descarta(self):
        txt = ("RESOLUÇÃO Nº 3.151/2022\nConcede o Título.\nA Mesa da Câmara Municipal do Salvador faz "
               "saber que o Poder Legislativo Municipal\npromulga e manda publicar a seguinte Resolução:\n"
               "Art. 1º Fica concedido o Título.\nArt. 4º Esta Resolução entra em vigor.\n"
               "28 de Dezembro de 2022\nCÂMARA MUNICIPAL\nATA 24ª SESSÃO ORDINÁRIA\n"
               + "Compareceram os senhores vereadores e demais presentes.\n" * 40
               + "Sala das Sessões, em 21 de dezembro de 2022.\n")
        achados, desc = blocos_mesa(txt, "resolucoes")
        self.assertEqual(achados, [])
        self.assertTrue(desc)

    def test_cabecalho_de_pagina_sai(self):
        txt = RES_2026.replace("Art. 4º", "Quinta e Sexta-feira, 8 e 9 de Dezembro de 2022\n"
                               "8 de Outubro de 2026\nCÂMARA MUNICIPAL\nArt. 4º")
        bloco = blocos_mesa(txt, "resolucoes")[0][0][2]
        self.assertNotIn("Outubro de 2026", bloco)
        self.assertNotIn("CÂMARA MUNICIPAL\n", bloco)
        self.assertNotIn("Sexta-feira", bloco)

    def test_edicao_dol_usa_numero_da_api(self):
        from baixar_dioly import edicao_dol
        item = {"id": 1, "numero": 6695, "pdf_url": "https://x/u_DOL-2024-04-30-66951.pdf.pdf"}
        self.assertEqual(edicao_dol(item), 6695)

    def test_assinatura_para_em_legenda(self):
        txt = ("Sala das Sessões, em 06 de outubro de 2026.\nCARLOS MUNIZ\nPresidente\n"
               "Vereadores da bancada de governo acompanham os discursos dos colegas\n")
        self.assertNotIn("Vereadores", recortar_mesa("RESOLUÇÃO Nº 1/2026\n" + txt))


if __name__ == "__main__":
    unittest.main()
