"""Citação de outra norma quebrada na linha do PDF não pode abrir parágrafo novo."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import texto_pdf_para_md


class CitacaoQuebradaNaLinha(unittest.TestCase):
    def test_citacao_apos_preposicao_continua_a_frase(self):
        corpo = texto_pdf_para_md("Art. 6º O Conselho deve ser composto, nos termos da\n"
                                  "Lei nº 16.301, de 13 de outubro de 2022, de 24 conselheiros.\n")
        self.assertEqual(corpo.count("\n\n"), 0)
        self.assertIn("nos termos da Lei nº 16.301", corpo)

    def test_lista_de_leis_com_artigo_no_fim_da_linha(self):
        corpo = texto_pdf_para_md("Art. 1º Ficam revogadas a Lei nº 10.266, de 1999; a\n"
                                  "Lei nº 10.525, de 2000; a Lei nº 10.764, de 2001.\n")
        self.assertNotIn("\n\n", corpo.strip())

    def test_epigrafe_depois_de_ponto_final_abre_bloco(self):
        corpo = texto_pdf_para_md("Art. 2º Esta Lei entra em vigor.\nLEI Nº 5, DE 1 DE JANEIRO DE 2000\nArt. 1º Texto.\n")
        self.assertEqual(corpo.strip().count("\n\n"), 2)

    def test_inciso_terminado_em_e_ainda_abre_novo_bloco(self):
        corpo = texto_pdf_para_md("Art. 3º Compete:\nI - fiscalizar; e\nII - julgar.\n")
        self.assertIn("\n\n", corpo.strip())
        self.assertEqual(corpo.strip().count("\n\n"), 2)


if __name__ == "__main__":
    unittest.main()
