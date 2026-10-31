import unittest
from formulas_to_pdf import FECHO,artigo_inicial,cargo_assinatura
class Formulas(unittest.TestCase):
    def test_ordinal_no_fecho(self):
        m=FECHO.search('Palácio Araguaia , em Palmas, ao 1º dia do mês de fevereiro de 2000;')
        self.assertIsNotNone(m);self.assertEqual(m.groups(),('1','fevereiro','2000'))
    def test_pontuacao_artigo(self):
        for x in ['Art. 1º. Valor -100,00','Art. 1.º Valor -100,00','Art. 1o Valor -100,00','Art. 1. Valor -100,00']:self.assertTrue(artigo_inicial(x),x)
        self.assertFalse(artigo_inicial('Art. 10. Não é o primeiro artigo.'))
    def test_capitulo_sem_apagar(self):
        self.assertTrue(artigo_inicial('\n CAPÍTULO I\n Das Disposições Gerais\n Art. 1º A receita...'))
        self.assertTrue(artigo_inicial('Disposição Preliminar\nArt. 1.º Regra'))
    def test_prefixo_desconhecido_falha(self):
        for x in ['AVISO\nArt. 1º Regra','CAPÍTULO II\nDas Disposições Gerais\nArt. 1º Regra','CAPÍTULO I\nArt. 2º Regra\nArt. 1º Regra']:
            self.assertFalse(artigo_inicial(x))
    def test_presidente_com_prova(self):
        t='Faço saber: eu, Marcelo Miranda, Presidente desta Casa, promulgo...\nPalácio Deputado João D’Abreu, em Palmas, aos 04 dias do mês de outubro de 2000;\nDeputado MARCELO MIRANDA\nPresidente\n'
        m=FECHO.search(t);self.assertTrue(cargo_assinatura(t,m))
        t=t.replace('Presidente desta Casa','autoridade não identificada');self.assertFalse(cargo_assinatura(t,FECHO.search(t)))
    def test_governador_sem_adivinhar_nome(self):
        t='Palácio Araguaia, em Palmas, aos 10 dias do mês de maio de 2000;\nNOME LITERAL\nGovernador do Estado\n';self.assertTrue(cargo_assinatura(t,FECHO.search(t)))
if __name__=='__main__':unittest.main()
