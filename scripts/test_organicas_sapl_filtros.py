"""Filtros de categoria/ano e texto oficial apontado na observação do SAPL."""
import unittest

from baixar_organicas_sapl import (
    html_sem_imagens, https_mesmo_host, texto_integral_alternativo, tipo_selecionado,
)


class FiltrosSAPLTest(unittest.TestCase):
    def test_https_so_no_mesmo_host(self):
        self.assertEqual(https_mesmo_host("http://legislacao.portoalegre.rs.gov.br/media/a.pdf",
                                         "legislacao.portoalegre.rs.gov.br"),
                         "https://legislacao.portoalegre.rs.gov.br/media/a.pdf")
        self.assertEqual(https_mesmo_host("http://outro.gov.br/media/a.pdf",
                                         "legislacao.portoalegre.rs.gov.br"),
                         "http://outro.gov.br/media/a.pdf")

    def test_observacao_um_arquivo_oficial(self):
        obs = ('Processo 5420/2009 <a href="http://legislacao.portoalegre.rs.gov.br'
               '/media/sapl/public/normajuridica/sirel/Norma_30_20101208_1.html" '
               'target="_blank">Norma_30_20101208_1.html</a>')
        self.assertEqual(texto_integral_alternativo(obs, "legislacao.portoalegre.rs.gov.br"),
                         "https://legislacao.portoalegre.rs.gov.br/media/sapl/public/normajuridica/sirel/Norma_30_20101208_1.html")

    def test_observacao_dois_arquivos_nao_escolhe(self):
        obs = ('<a href="https://legislacao.portoalegre.rs.gov.br/media/a.html">a</a>'
               '<a href="https://legislacao.portoalegre.rs.gov.br/media/b.pdf">b</a>')
        self.assertIsNone(texto_integral_alternativo(obs, "legislacao.portoalegre.rs.gov.br"))

    def test_observacao_host_alheio_ignorado(self):
        self.assertIsNone(texto_integral_alternativo(
            '<a href="https://exemplo.org/media/a.html">a</a>',
            "legislacao.portoalegre.rs.gov.br"))

    def test_html_remove_img_sem_alterar_texto(self):
        html = '<p>Art. 1º</p><img src="/netahtml/sirel/imagem/logocmpoa.jpg" alt="brasao"><p>Vigor.</p>'
        self.assertEqual(html_sem_imagens(html), "<p>Art. 1º</p><p>Vigor.</p>")

    def test_categorias_restringe_emenda(self):
        self.assertTrue(tipo_selecionado("Emenda à Lei Orgânica", "organicas", ["emendas-lei-organica"]))
        self.assertFalse(tipo_selecionado("Lei Orgânica", "organicas", ["emendas-lei-organica"]))
        self.assertTrue(tipo_selecionado("Lei Orgânica", "organicas", None))
        self.assertFalse(tipo_selecionado("Decreto municipal", "organicas", None))


if __name__ == "__main__":
    unittest.main()
