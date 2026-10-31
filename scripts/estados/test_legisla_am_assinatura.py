import unittest
from legisla_am_assinatura import conferir
class Assinatura(unittest.TestCase):
 def test_data_confere(self):self.assertFalse(conferir('GABINETE DO GOVERNADOR, em Manaus, 20 de julho de 1978.','1978-07-20')['reter'])
 def test_nao_corrige_epigrafe_divergente(self):
  q=conferir('GABINETE DO GOVERNADOR, em Manaus, 20 de julho de 1978.','1978-06-20');self.assertTrue(q['reter']);self.assertEqual(q['data_epigrafe'],'1978-06-20')
 def test_mes_incorreto_nao_e_inferido(self):self.assertTrue(conferir('GABINETE DO GOVERNADOR, em Manaus, 20 de otubro de 1978.','1978-10-20')['reter'])
 def test_ausencia_de_formula_nao_comprova_defeito(self):self.assertEqual(conferir('GOVERNADOR, assinatura.','1978-01-01')['status'],'nao_comparavel')
if __name__=='__main__':unittest.main()
