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


class CabecalhoDePagina(unittest.TestCase):
    CONTADOR = "CÂMARA MUNICIPAL DE CAMPINAS 2/4"

    def test_contador_removido_e_frase_partida_pela_pagina_reunida(self):
        corpo, _ = limpar_carimbo_campinas("\n\n".join([
            "**Art. 3º** A incidência exigirá a cessão de uso da faixa viária para o", self.CONTADOR,
            "Município e a implantação das ruas."]))
        self.assertEqual(corpo, "**Art. 3º** A incidência exigirá a cessão de uso da faixa viária para o Município e a implantação das ruas.")

    def test_contador_com_total_truncado(self):
        corpo, _ = limpar_carimbo_campinas("\n\n".join(["Texto que segue ao", "CÂMARA MUNICIPAL DE CAMPINAS 10/", "texto da página seguinte."]))
        self.assertEqual(corpo, "Texto que segue ao texto da página seguinte.")

    def test_pagina_que_termina_em_frase_completa_nao_junta(self):
        corpo, _ = limpar_carimbo_campinas("\n\n".join(["Fim da página.", self.CONTADOR, "Início da outra."]))
        self.assertEqual(corpo, "Fim da página.\n\nInício da outra.")

    def test_titulo_sem_pontuacao_no_fim_da_pagina_nao_junta(self):
        corpo, _ = limpar_carimbo_campinas("\n\n".join(["SEÇÃO I Das Disposições Gerais", self.CONTADOR, "o texto seguinte"]))
        self.assertEqual(corpo.count("\n\n"), 1)

    def test_proximo_dispositivo_nunca_e_unido(self):
        corpo, _ = limpar_carimbo_campinas("\n\n".join(["ficam sujeitos ao", self.CONTADOR, "**Art. 6º** Outro artigo."]))
        self.assertEqual(corpo.count("\n\n"), 1)

    def test_retorno_de_carro_solto_vira_quebra_de_linha(self):
        corpo, _ = limpar_carimbo_campinas("sanciono e promulgo a seguinte lei:\r]\r\nArt. 1º Texto.")
        self.assertNotIn("\r", corpo)
        self.assertEqual(corpo, "sanciono e promulgo a seguinte lei:\n]\nArt. 1º Texto.")

    def test_capa_fundida_com_o_aviso_no_mesmo_paragrafo(self):
        fundido = CAPA_2022 + " Texto para consulta, reproduzido conforme a publicação no Diário Oficial do Município em 13 de novembro de 2018"
        corpo, notas = limpar_carimbo_campinas("\n\n".join([fundido, LEI]))
        self.assertEqual(corpo, LEI)
        self.assertEqual(notas, ["cópia de consulta da Câmara, reproduzida conforme a publicação no Diário Oficial do Município"])

    def test_capa_seguida_de_texto_que_nao_e_aviso_preserva_o_texto(self):
        corpo, notas = limpar_carimbo_campinas(CAPA_2022 + " Art. 1º Texto da lei.")
        self.assertEqual(corpo, "Art. 1º Texto da lei.")
        self.assertEqual(notas, [])

    def test_cabecalho_corrente_do_diario_oficial_sai_e_a_frase_se_reune(self):
        for cabecalho in ("Diário Oficial do Município de Campinas 183",
                          "2 Diário Oficial do Município de Campinas Campinas, quinta-feira, 08 de outubro de 2020",
                          "24 Diário Oficial do Município de Campinas PREFETURA MUNICIPAL DE CAMPINAS",
                          "Diário Oficial do Município de Campinas"):
            corpo, _ = limpar_carimbo_campinas("\n\n".join(["Disponível em https://exemplo.org e acessado em", cabecalho, "março de 2017."]))
            self.assertEqual(corpo, "Disponível em https://exemplo.org e acessado em março de 2017.", cabecalho)

    def test_citacao_do_diario_oficial_no_texto_nao_e_cabecalho(self):
        par = "Publicada no Diário Oficial do Município de Campinas em 12/05/2021"
        corpo, _ = limpar_carimbo_campinas("\n\n".join([LEI, par]))
        self.assertIn(par, corpo)

    def test_contador_so_conta_com_o_paragrafo_inteiro(self):
        par = "A CÂMARA MUNICIPAL DE CAMPINAS 2/4 votou a matéria."
        corpo, _ = limpar_carimbo_campinas("\n\n".join([LEI, par]))
        self.assertIn(par, corpo)

    def test_aviso_sem_valor_legal_vira_nota(self):
        corpo, notas = limpar_carimbo_campinas("\n\n".join([LEI, "Texto somente para consulta, sem valor legal."]))
        self.assertEqual(corpo, LEI)
        self.assertEqual(notas, ["cópia de consulta da Câmara, sem valor legal"])

    def test_variantes_do_aviso_de_reproducao(self):
        for aviso in ("Texto para consulta, reproduzido conforme a publicação extra do Diário Oficial do Município em 12 de maio de 2021",
                      "Texto para consulta, reproduzido conforme a publicação do Diário Oficial do Município em 8 de janeiro de 2021",
                      "\u200bTexto para consulta, reproduzido conforme publicação no Diário Oficial do Município em 29 de julho de 2020"):
            corpo, notas = limpar_carimbo_campinas("\n\n".join([aviso, LEI]))
            self.assertEqual(corpo, LEI, aviso)
            self.assertEqual(notas, ["cópia de consulta da Câmara, reproduzida conforme a publicação no Diário Oficial do Município"])

    def test_aviso_do_diario_oficial_da_camara(self):
        corpo, notas = limpar_carimbo_campinas("\n\n".join([
            "Texto somente para consulta. Não substitui o publicado no Diário Oficial da Câmara Municipal de Campinas em 7 de maio de 2025", LEI]))
        self.assertEqual(corpo, LEI)
        self.assertEqual(notas, ["cópia de consulta da Câmara, não substitui o Diário Oficial da Câmara Municipal"])

    def test_cabecalho_sem_contador_e_aviso_sem_ponto_final(self):
        corpo, notas = limpar_carimbo_campinas("\n\n".join(["CÂMARA MUNICIPAL DE CAMPINAS", LEI, "Texto somente para consulta, sem valor legal"]))
        self.assertEqual(corpo, LEI)
        self.assertEqual(notas, ["cópia de consulta da Câmara, sem valor legal"])

    def test_espaco_de_largura_zero_no_corpo_sai(self):
        corpo, _ = limpar_carimbo_campinas("Art. 1º O \u200bcaput\u200b deste artigo vale.")
        self.assertEqual(corpo, "Art. 1º O caput deste artigo vale.")

    def test_capa_com_caracteres_de_largura_zero(self):
        capa = "​CÂMARA MUNICIPAL DE CAMPINAS ​Estado de São Paulo Diretoria de Gestão Documental Coordenadoria de Biblioteca cbib@campinas.sp.leg.br – Ramal 1603"
        corpo, _ = limpar_carimbo_campinas("\n\n".join([capa, LEI]))
        self.assertEqual(corpo, LEI)

    def test_contador_solto_em_sequencia_sai_e_a_frase_se_reune(self):
        # o cabeçalho "CÂMARAMUNICIPAL DE CAMPINAS" saiu como linha repetida e o contador ficou sozinho (LC 80/2014)
        corpo, _ = limpar_carimbo_campinas("\n\n".join([
            "1/3", LEI, "IV - o estabelecimento será lacrado;", "2/3", "V - multa equivalente a", "3/3", "5.000 UFIC's."]))
        self.assertEqual(corpo, "\n\n".join([LEI, "IV - o estabelecimento será lacrado;", "V - multa equivalente a 5.000 UFIC's."]))

    def test_contador_solto_com_folhas_sem_cabecalho(self):
        # LC 76/2014: algumas folhas não trazem o cabeçalho; a sequência segue crescente e com o mesmo total
        corpo, _ = limpar_carimbo_campinas("\n\n".join(["1/19", LEI, "2/19", "Anexo I.", "4/19", "Anexo II."]))
        self.assertEqual(corpo, "\n\n".join([LEI, "Anexo I.", "Anexo II."]))

    def test_fracao_solta_no_texto_nao_e_contador(self):
        for fracoes in (["1/2"], ["1/2", "1/2"], ["2/3", "3/3"], ["1/3", "2/4"], ["1/2", "3/2"]):
            corpo, _ = limpar_carimbo_campinas("\n\n".join([LEI, *fracoes]))
            self.assertEqual(corpo, "\n\n".join([LEI, *fracoes]), fracoes)

    def test_aviso_sem_valor_legal_sob_fio_de_sublinhados(self):
        corpo, notas = limpar_carimbo_campinas("\n\n".join([LEI, "\\_\\_\\_\\_ Texto somente para consulta, sem valor legal."]))
        self.assertEqual(corpo, LEI)
        self.assertEqual(notas, ["cópia de consulta da Câmara, sem valor legal"])

    def test_rodape_com_hifen_no_lugar_do_travessao(self):
        # assim sai do OCR (LC 515/2025)
        corpo, _ = limpar_carimbo_campinas("\n\n".join([
            LEI, "Avenida da Saudade, nº 1.004 - Ponte Preta - CEP: 13041-670 - Campinas - SP - PABX: (19) 3736-1300"]))
        self.assertEqual(corpo, LEI)


class EmendaSemClausulaDeVigencia(unittest.TestCase):
    PROMULGA = ("A Mesa da Câmara Municipal de Campinas, nos termos do § 2º do Artigo 40 da Lei Orgânica, promulga a seguinte emenda "
                "ao seu texto: Fica acrescentado ao artigo 241 o parágrafo único, com a seguinte redação: " + "texto da emenda. " * 40)

    def test_assinatura_de_encerramento_vale_como_fim_do_ato(self):
        corpo = self.PROMULGA + "Campinas, 05 de dezembro de 1996 Romeu Santini Presidente Biléo Soares 1º Secretário"
        self.assertTrue(corpo_integral_reconhecivel(corpo, emenda=True))

    def test_ano_com_ponto_de_milhar(self):
        corpo = self.PROMULGA + "Campinas 27 de dezembro de 1.994. MARCO ABI CHEDID Presidente FRANCISCO SELLIN 1º Secretário"
        self.assertTrue(corpo_integral_reconhecivel(corpo, emenda=True))

    def test_mencao_a_presidente_no_texto_nao_basta(self):
        corpo = self.PROMULGA + "O Presidente da Câmara será eleito entre os vereadores na forma do regimento."
        self.assertFalse(corpo_integral_reconhecivel(corpo, emenda=True))

    def test_so_vale_para_emenda(self):
        corpo = self.PROMULGA + "Campinas, 05 de dezembro de 1996 Romeu Santini Presidente"
        self.assertFalse(corpo_integral_reconhecivel(corpo, emenda=False))

    def test_assinatura_antes_da_promulgacao_nao_vale(self):
        corpo = "Campinas, 05 de dezembro de 1996 Romeu Santini Presidente. " + self.PROMULGA
        self.assertFalse(corpo_integral_reconhecivel(corpo, emenda=True))


class ArtigoUnico(unittest.TestCase):
    def test_artigo_unico_e_reconhecido(self):
        self.assertTrue(corpo_integral_reconhecivel("Artigo único. Acrescentem-se os incisos."))
        self.assertTrue(corpo_integral_reconhecivel("Art. único. Texto."))
        self.assertFalse(corpo_integral_reconhecivel("Sem dispositivos reconhecíveis."))


if __name__ == "__main__":
    unittest.main()
