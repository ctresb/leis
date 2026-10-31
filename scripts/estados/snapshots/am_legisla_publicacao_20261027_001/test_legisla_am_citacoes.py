import unittest
from legisla_am_citacoes import conferir_citacoes
class Citacoes(unittest.TestCase):
 own=dict(numero='100',data='1979-01-01')
 def test_referencia_inline_e_comprovada(self):
  q=conferir_citacoes('<div><p>Art. 1º O art. 3º da Lei nº 86, de 4 de dezembro de 1963 passa a vigorar.</p></div>',self.own);self.assertTrue(q['todas_contextualizadas']);self.assertEqual(q['total_referencias'],1)
 def test_epigrafe_alheia_isolada_falha(self):
  self.assertFalse(conferir_citacoes('<div><p>Art. 1º Norma própria.</p><p>LEI Nº 86, DE 4 DE DEZEMBRO DE 1963</p><p>Art. 1º Outro ato.</p></div>',self.own)['todas_contextualizadas'])
 def test_segunda_ocorrencia_nao_citada_falha(self):
  self.assertFalse(conferir_citacoes('<div><p>Art. 1º Revoga a Lei nº 86, de 4 de dezembro de 1963.</p><p>LEI Nº 86, DE 4 DE DEZEMBRO DE 1963</p></div>',self.own)['todas_contextualizadas'])
 def test_texto_fora_paragrafo_e_prova_incompleta(self):
  self.assertFalse(conferir_citacoes('<div>Altera a Lei nº 86, de 4 de dezembro de 1963.</div>',self.own)['todas_contextualizadas'])
if __name__=='__main__':unittest.main()
