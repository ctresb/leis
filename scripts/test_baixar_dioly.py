import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar_dioly import (
    blocos_emenda, eh_promulgada, data_do_bloco, titulo_do_bloco, gravar_emenda,
    recortar_ato, EPIGRAFE, SALA,
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


if __name__ == "__main__":
    unittest.main()
