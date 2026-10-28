"""Parse da ficha SIL (proxy Drupal) e catálogo explícito de BH — sem rede."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cmbh_sil import (ANEXOS_PLANO_DIRETOR, EMENDAS, cache_anexo, data_por_extenso,
                      parse_pesquisa, url_download, url_ficha)


FICHA = """<div id="resultadoPesquisa_normasInterno"><h2>Lei - 11181/2019</h2><span id='novaUrl' style='display:none'>https://www.cmbh.mg.gov.br/atividade-legislativa/pesquisar-legislacao/lei/11181/2019</span><div class="col-xs-12"><p><strong>Documentos da norma: </strong><ol id='documentos-norma'><li><span>lei11181-atual.doc</span><a href="https://cmbhsildownload.cmbh.mg.gov.br/silinternet/servico/download/documentoDaNorma?idDocDaNorma=2c907f7693d91e4901941d35b6360152" class="btn btn-success btn-fila btn-anexo"></a></li><li><span>lei11181 - Anexo I - Mapa.pdf</span><a href="https://cmbhsildownload.cmbh.mg.gov.br/silinternet/servico/download/documentoDaNorma?idDocDaNorma=abc123" class="btn"></a></li></ol></p><li style='list-style:none'><strong>Responsável pela Promulgação/Publicação: </strong>Prefeito</li><ul><li><strong>Data da promulgação: </strong>08/08/2019</li><li><strong>Data da publicação: </strong>09/08/2019</li></ul><p><strong>Ementa:</strong> Aprova o Plano Diretor do Município de Belo Horizonte e dá outras providências.</p></div>"""


class CmbhSil(unittest.TestCase):
    def test_parse_ficha_e_anexos(self):
        d = parse_pesquisa(FICHA)
        self.assertEqual(d["titulo"], "Lei - 11181/2019")
        self.assertEqual(d["ementa"][:20], "Aprova o Plano Diret")
        self.assertEqual(d["datas"], [("promulgação", "08/08/2019"), ("publicação", "09/08/2019")])
        self.assertEqual(len(d["docs"]), 2)
        self.assertEqual(d["docs"][0]["id"], "2c907f7693d91e4901941d35b6360152")
        self.assertTrue(d["fonte"].endswith("/lei/11181/2019"))

    def test_parse_vazio(self):
        self.assertIsNone(parse_pesquisa("<h1>Resultados da pesquisa:</h1>Nenhum resultado encontrado."))

    def test_catalogo_emendas_1_a_45(self):
        nums = [e[0] for e in EMENDAS]
        self.assertEqual(nums, list(range(1, 46)))
        self.assertEqual(len({e[4] for e in EMENDAS}), 45)
        self.assertEqual(EMENDAS[0][2], "1992-06-30")
        self.assertEqual(EMENDAS[44][2], "2026-09-23")
        self.assertEqual(EMENDAS[15][2], "2000-06-15")  # nº 16, ausente das notas da LO
        self.assertEqual(EMENDAS[28][2], "2016-02-29")  # nº 29
        self.assertEqual(EMENDAS[41][2], "2024-03-06")  # nº 42

    def test_anexos_plano_diretor(self):
        self.assertEqual(len(ANEXOS_PLANO_DIRETOR), 32)
        nomes = [n for n, _ in ANEXOS_PLANO_DIRETOR]
        self.assertTrue(nomes[0].startswith("lei11181 - Anexo I"))
        self.assertTrue(nomes[-1].startswith("lei11181 - Anexo XIX"))
        self.assertEqual(len({i for _, i in ANEXOS_PLANO_DIRETOR}), 32)

    def test_urls_e_cache(self):
        self.assertIn("idDocDaNorma=abc", url_download("abc"))
        self.assertTrue(url_ficha("lei", 11181, 2019).endswith("/lei/11181/2019"))
        self.assertEqual(data_por_extenso("2019-08-08"), "8 de agosto de 2019")
        self.assertTrue(cache_anexo("lei11181 - Anexo I - Mapa.pdf").endswith(".pdf"))
        self.assertNotIn(" ", cache_anexo("lei11181 - Anexo I - Mapa.pdf"))


if __name__ == "__main__":
    unittest.main()
