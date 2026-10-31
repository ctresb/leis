import unittest
from spl_agape import numero_com_sufixo,conferir_numero_proprio,conferir_tipo_proprio,processar
class SufixoTest(unittest.TestCase):
 def test_sufixo_literal_preservado(self):self.assertEqual(numero_com_sufixo('8.494-A'),'8494-A')
 def test_sem_sufixo_distinto(self):self.assertNotEqual(numero_com_sufixo('8.494'),numero_com_sufixo('8.494-A'))
 def test_epigrafe_propria_nao_descarta_sufixo(self):
  with self.assertRaises(ValueError):conferir_numero_proprio('LEI Nº 8.494-A, DE 28 DE DEZEMBRO DE 2018','8494')
 def test_epigrafe_conferida(self):conferir_numero_proprio('LEI Nº 8.494-A, DE 28 DE DEZEMBRO DE 2018','8494-A')
 def test_indice_deslocado_rejeitado(self):
  with self.assertRaises(ValueError):numero_com_sufixo(' do inciso II')
 def test_id_deslocado_falha_antes_de_rede(self):self.assertEqual(processar({'cod':' do inciso II'})[0],'sem_texto')
 def test_epigrafe_ausente_falha(self):
  with self.assertRaises(ValueError):conferir_numero_proprio('','8494-A')
 def test_lei_ordinaria_nao_e_delegada_mesmo_numero(self):
  with self.assertRaisesRegex(ValueError,'tipo'):
   conferir_tipo_proprio('LEI Nº 4','Lei Delegada')
 def test_tipo_delegada_confere(self):conferir_tipo_proprio('LEI DELEGADA Nº 4','Lei Delegada')
 def test_complementar_nao_e_ordinaria(self):
  with self.assertRaisesRegex(ValueError,'tipo'):
   conferir_tipo_proprio('LEI COMPLEMENTAR Nº 4','Lei Ordinária')
if __name__=='__main__':unittest.main()
