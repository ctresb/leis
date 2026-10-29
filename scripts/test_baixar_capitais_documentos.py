import datetime as dt
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar_capitais_documentos import (
    CATALOGO, PULAR, gravar_markdown, limpar_chrome_dom, limpar_chrome_md,
    numero_epigrafe, recortar_lei_dom,
)
from auditar import validar

PDDU = """SALVADOR • BAHIA • QUINTA-FEIRA,
30 DE JUNHO DE 2016
ANO XXIX | N º 6.620
EXECUTIVO
LEIS
LEI Nº 9.069/2016
Dispõe sobre o Plano Diretor de Desenvolvimento
Urbano do Município de Salvador - PDDU 2016 e dá
outras providências.
O PREFEITO MUNICIPAL DO SALVADOR, CAPITAL DO ESTADO DA BAHIA,
Faço saber que a Câmara Municipal decreta e eu sanciono a seguinte Lei:
Art. 1º O Plano Diretor de Desenvolvimento Urbano (PDDU) tem como base os
fundamentos expressos na Constituição Federal.
§4º A equidade racial, social e territorial implica o reconhecimento e o respeito a
pessoas e grupos sociais e a orientação de políticas públicas, no sentido da inclusão social de grupos
DIÁRIO OFICIAL DO
Criado pelo art. 82 da Lei nº 3.601, de 18 de fevereiro de 1986
Ouvidoria Geral do Município - Para registrar reclamações, denúncias,
sugestões ou elogios, acesse: www.ouvidoria.salvador.ba.gov.br
CEP: 40.020-000 - Tel.: 3202-6261/6262
Coordenador de Tecnologia
Chefe de Gabinete do Prefeito, em exercício
E
D
I
Ç
Ã
O
\f
DIÁRIO OFICIAL DO
SALVADOR-BAHIA
QUINTA-FEIRA
30 DE JUNHO DE 2016
ANO XXIX | N º 6.620
2
historicamente em situação de desvantagem.
Art. 411. Esta Lei entrará em vigor na data de sua publicação, revogadas as
disposições em contrário.
GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 30 de junho de 2016.
ANTONIO CARLOS PEIXOTO DE MAGALHÃES NETO
Prefeito
ANEXO 01
Quadro 01
Criado pelo art. 82 da Lei nº 3.601, de 18 de fevereiro de 1986
Ouvidoria Geral do Município - Para registrar reclamações, denúncias,
CEP: 40.020-000 - Tel.: 3202-6261/6262
Coordenador de Tecnologia
Chefe de Gabinete do Prefeito, em exercício
"""

LOUOS = """EXECUTIVO
LEIS
LEI Nº 9.148/2016
Dispõe sobre o Ordenamento do Uso e da
Ocupação do Solo do Município de Salvador.
Art. 1º Esta Lei dispõe sobre o ordenamento urbano.
Art. 190. Esta Lei entrará em vigor 120 dias após a data de sua publicação.
GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 08 de setembro de 2016.
ANTONIO CARLOS PEIXOTO DE MAGALHÃES NETO
Prefeito
Criado pelo art. 82 da Lei nº 3.601, de 18 de fevereiro de 1986
"""


class CapitaisSalvadorTest(unittest.TestCase):
    def test_numero_epigrafe(self):
        self.assertEqual(numero_epigrafe("9069"), "9.069")
        self.assertEqual(numero_epigrafe("9148"), "9.148")
        self.assertEqual(numero_epigrafe("9.069"), "9.069")

    def test_recorta_pddu_sem_cortar_colofao_precoce(self):
        corpo = recortar_lei_dom(PDDU, "9069", "2016")
        self.assertTrue(corpo.startswith("LEI Nº 9.069/2016"))
        self.assertIn("Art. 1º", corpo)
        self.assertIn("Art. 411", corpo)
        self.assertIn("GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 30 de junho de 2016", corpo)
        self.assertIn("ANEXO 01", corpo)
        self.assertIn("historicamente em situação de desvantagem", corpo.split("Art. 411")[0])
        self.assertLess(corpo.find("Criado pelo art. 82 da Lei nº 3.601"), corpo.find("Art. 411"))
        self.assertGreater(corpo.find("ANEXO 01"), corpo.find("Art. 411"))
        self.assertLess(corpo.rfind("Criado pelo art. 82"), corpo.find("ANEXO 01"))

    def test_recorta_louos_ate_colofao_final(self):
        corpo = recortar_lei_dom(LOUOS, "9148", "2016")
        self.assertIn("LEI Nº 9.148/2016", corpo)
        self.assertIn("Art. 190", corpo)
        self.assertNotIn("Criado pelo art. 82", corpo)

    def test_epigrafe_ausente(self):
        with self.assertRaisesRegex(ValueError, "epígrafe"):
            recortar_lei_dom(LOUOS, "9069", "2016")

    def test_limpa_chrome_preserva_gabinete(self):
        limpo = limpar_chrome_dom(recortar_lei_dom(PDDU, "9069", "2016"))
        self.assertIn("inclusão social de grupos", limpo)
        self.assertIn("historicamente em situação de desvantagem", limpo)
        self.assertIn("GABINETE DO PREFEITO MUNICIPAL DO SALVADOR, em 30 de junho de 2016", limpo)
        self.assertNotIn("Criado pelo art. 82", limpo)
        self.assertNotIn("SALVADOR-BAHIA", limpo)
        self.assertNotRegex(limpo, r"(?m)^E$")

    def test_limpa_chrome_md_glued_headers(self):
        bruto = "texto\nDIÁRIO OFICIAL DO SALVADOR-BAHIA ANO XXX | N º 6.672 13 V = volume\nANO XXIX | N º 6.620 decisão"
        limpo = limpar_chrome_md(bruto)
        self.assertNotIn("DIÁRIO OFICIAL", limpo)
        self.assertNotIn("ANO XXX", limpo)
        self.assertNotIn("N º 6.672", limpo)
        self.assertIn("V = volume", limpo)
        self.assertIn("decisão", limpo)

    def test_catalogo_dioly_https_e_numeros(self):
        pddu = next(x for x in CATALOGO if x["slug"] == "plano-diretor-9069-2016")
        louos = next(x for x in CATALOGO if x["slug"] == "louos-9148-2016")
        self.assertTrue(pddu["fonte_texto"].startswith("https://portal-api.dioly.com.br/"))
        self.assertTrue(louos["fonte_texto"].startswith("https://portal-api.dioly.com.br/"))
        self.assertEqual(pddu["numero"], "9069")
        self.assertEqual(louos["numero"], "9148")
        self.assertEqual(pddu["categoria"], "plano-diretor")
        self.assertEqual(louos["categoria"], "codigos")
        self.assertEqual(pddu["extrator"], "dioly-raw-v2")
        self.assertNotIn("cmsba.dyndns.org", pddu["fonte"])
        self.assertNotIn("leismunicipais", louos["fonte"])
        self.assertEqual(PULAR[0]["numero"], "7186")
        self.assertEqual(PULAR[0]["status"], "sem_fonte_https")

    def test_gravar_passa_auditoria(self):
        item = next(x for x in CATALOGO if x["slug"] == "plano-diretor-9069-2016")
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "p.md"
            texto = gravar_markdown(dest, item, "**Art. 1º** O PDDU.\n", "abc", "2026-10-28")
            erros, _avisos = validar(texto, "municipais/BA/salvador/plano-diretor/2016/x.md",
                                     dt.date(2026, 10, 28))
            self.assertEqual(erros, [])


if __name__ == "__main__":
    unittest.main()
