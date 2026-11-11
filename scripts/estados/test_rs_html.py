import unittest
from rs import corpo_html_legis, url_do_arquivo


def pagina(corpo):
    return ('<html><div class="form-mais-info"><table><tr><td><img src="logo.png"></td></tr>'
            '<tr><td valign="TOP" colspan="2">RSM: 759</td></tr>'
            '<tr><td VALIGN="TOP" colspan="2">' + corpo + '</td></tr></table></div></html>')


class CampoNormativoRS(unittest.TestCase):
    def test_exclui_controles_preserva_norma_e_anexos(self):
        corpo = '<p>Art. 1º Texto.</p><table><tr><td rowspan="2">Anexo</td><td>1</td></tr></table>'
        self.assertEqual(corpo_html_legis(pagina(corpo)), corpo)
        self.assertNotIn('logo.png', corpo_html_legis(pagina(corpo)))

    def test_imagem_normativa_nao_e_descartada(self):
        corpo = '<p>Art. 1º Texto.</p><img src="anexo-oficial.png">'
        self.assertEqual(corpo_html_legis(pagina(corpo)), corpo)

    def test_fecho_ausente_rejeitado(self):
        incompleto = '<div class="form-mais-info"><table><tr><td valign="TOP" colspan="2">RSM</td></tr><tr><td valign="TOP" colspan="2"><p>Art. 1º Texto.</p>'
        self.assertIsNone(corpo_html_legis(incompleto))

    def test_template_desconhecido_rejeitado(self):
        self.assertIsNone(corpo_html_legis('<table><td valign="top" colspan="2">Art. 1º</td></table>'))


class UrlDoArquivoRS(unittest.TestCase):
    base = 'https://ww3.al.rs.gov.br/filerepository/repLegis/arquivos/'

    def test_acentos_viram_percent_utf8(self):
        self.assertEqual(url_do_arquivo(self.base + 'LEI%2016.137%20retificação.pdf'),
                         self.base + 'LEI%2016.137%20retifica%C3%A7%C3%A3o.pdf')
        self.assertEqual(url_do_arquivo(self.base + 'Lei nº 08.850.pdf'), self.base + 'Lei%20n%C2%BA%2008.850.pdf')

    def test_nao_codifica_duas_vezes(self):
        ja_codificada = self.base + 'DEC%2058.471.pdf'
        self.assertEqual(url_do_arquivo(ja_codificada), ja_codificada)
        self.assertEqual(url_do_arquivo(url_do_arquivo(self.base + 'a b-republicação.pdf')),
                         self.base + 'a%20b-republica%C3%A7%C3%A3o.pdf')


if __name__ == '__main__':
    unittest.main()
