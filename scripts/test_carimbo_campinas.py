"""A limpeza do carimbo da biblioteca da Câmara de Campinas remove só parágrafos inteiros conhecidos."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from baixar_organicas_sapl import corpo_integral_reconhecivel, limpar_carimbo_campinas

CAPA_2022 = ("CÂMARA MUNICIPAL DE CAMPINAS Estado de São Paulo Diretoria de Gestão Documental "
             "Coordenadoria de Biblioteca cbib@campinas.sp.leg.br – Ramal 1603")
CAPA_2024 = "Diretoria de Gestão Documental Coordenadoria de Biblioteca cbib@campinas.sp.leg.br Ramal: 1603"
RODAPE = "Avenida da Saudade, nº 1.004 – Ponte Preta – CEP: 13041-670 – Campinas – SP – PABX: (19) 3736-1300."
LEI = "LEI Nº 1, DE 1 DE JANEIRO DE 2024\n\n**Art. 1º** Texto."


class LimparCarimbo(unittest.TestCase):
    def verificar(self, aviso, nota):
        corpo, notas = limpar_carimbo_campinas("\n\n".join([CAPA_2022, aviso, LEI, RODAPE]))
        self.assertEqual(corpo, LEI)
        self.assertEqual(notas, [nota])

    def test_nao_substitui_com_grafia_errada_e_data_ordinal(self):
        self.verificar("Texto somente para consulta. Não substitui o publicado no Diário Oficial do Municipio de Campinas em 1º de outubro de 2024",
                   "cópia de consulta da Câmara, não substitui o Diário Oficial do Município")

    def test_nao_substitui_com_data_sem_espaco(self):
        self.verificar("Texto somente para consulta. Não substitui o publicado no Diário Oficial do Município de Campinas em 8 de novembrode 2024",
                   "cópia de consulta da Câmara, não substitui o Diário Oficial do Município")

    def test_reproduzido_conforme_publicacao(self):
        self.verificar("Texto para consulta, reproduzido conforme a publicação no Diário Oficial do Município em 17 de março de 2022",
                   "cópia de consulta da Câmara, reproduzida conforme a publicação no Diário Oficial do Município")

    def test_capa_de_2024_e_suplemento(self):
        corpo, notas = limpar_carimbo_campinas("\n\n".join([CAPA_2024, LEI, "OBS.: TABELAS EXPLICATIVAS PUBLICADAS EM SUPLEMENTO ANEXO A ESTA EDIÇÃO."]))
        self.assertEqual(notas, ["tabelas e anexos publicados em suplemento, ausentes do texto integral"])
        self.assertTrue(corpo.startswith("LEI Nº 1"))

    def test_texto_da_lei_parecido_com_carimbo_nao_e_removido(self):
        par = "Art. 2º O Diretoria de Gestão Documental da Câmara fará a consulta."
        corpo, notas = limpar_carimbo_campinas("\n\n".join([LEI, par]))
        self.assertIn(par, corpo)
        self.assertEqual(notas, [])


class ArtigoUnico(unittest.TestCase):
    def test_artigo_unico_e_reconhecido(self):
        self.assertTrue(corpo_integral_reconhecivel("Artigo único. Acrescentem-se os incisos."))
        self.assertTrue(corpo_integral_reconhecivel("Art. único. Texto."))
        self.assertFalse(corpo_integral_reconhecivel("Sem dispositivos reconhecíveis."))


if __name__ == "__main__":
    unittest.main()
