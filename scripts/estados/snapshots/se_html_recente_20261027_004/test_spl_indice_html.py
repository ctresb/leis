import unittest
from spl_indice_html import ler_indice

URL='https://aleselegis.al.se.leg.br/legislacao/consulta-legislacao.aspx?tipo=4&ano=2026'
CARD='''<div class="kt-widget5__item"><div><a class="kt-widget5__title" href="norma.aspx?id=12630&amp;tipo=4&amp;ano=2026">Lei Ordinária n° 10.056/2026</a><a class="kt-widget5__desc">Altera “a”, b, c; preserva 0,5 e -100.</a><div class="kt-widget5__info"><span>Data:</span><span>07/10/2026</span><span>Situação:</span><span>Em vigor</span></div></div><a href="/Arquivo/Documents/legislacao/html/L100562026.html">TEXTO COMPLETO</a></div>'''
class IndiceTest(unittest.TestCase):
 def parse(self,s):return ler_indice(s.encode(),URL,'SE','4',2026)
 def test_identidade_e_ementa_com_aspas_virgulas_sinais(self):
  a=self.parse(CARD)[0];self.assertEqual(a['id'],'12630');self.assertEqual(a['numero'],'10056');self.assertEqual(a['data'],'2026-10-07');self.assertEqual(a['ementa'],'Altera “a”, b, c; preserva 0,5 e -100.')
 def test_sufixo_literal_preservado(self):self.assertEqual(self.parse(CARD.replace('10.056/2026','10.056-A/2026'))[0]['numero'],'10056-A')
 def test_sem_fallback_de_url_inferida(self):self.assertEqual(self.parse(CARD.replace('href="/Arquivo','href="/fora'))[0]['textos_completos_observados'],[])
 def test_tipo_diferente_falha(self):
  with self.assertRaises(ValueError):self.parse(CARD.replace('Lei Ordinária','Lei Complementar'))
 def test_link_de_outra_origem_falha(self):
  with self.assertRaises(ValueError):self.parse(CARD.replace('href="norma','href="https://exemplo.invalid/norma'))
 def test_id_repetido_falha(self):
  with self.assertRaises(ValueError):self.parse(CARD+CARD)
 def test_schema_alterado_falha(self):
  with self.assertRaises(ValueError):self.parse(CARD.replace('Situação:','Estado:'))
 def test_data_invalida_falha(self):
  with self.assertRaises(ValueError):self.parse(CARD.replace('07/10/2026','31/02/2026'))
if __name__=='__main__':unittest.main()
