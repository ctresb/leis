import unittest
from auditar_spl_html_recente import comparar,identidade
class TextoTest(unittest.TestCase):
 def test_literal_valores(self):self.assertTrue(comparar('<p>R$ 0,5 -100 10%</p>','R$ 0,5 -100 10%')['sha256_visivel_fonte'])
 def test_decimal_perdido(self):
  with self.assertRaises(ValueError):comparar('<p>0,5</p>','05')
 def test_sinal_perdido(self):
  with self.assertRaises(ValueError):comparar('<p>-100</p>','100')
 def test_percentual_perdido(self):
  with self.assertRaises(ValueError):comparar('<p>10%</p>','10')
 def test_lista_nao_pode_renumerar(self):
  with self.assertRaises(ValueError):comparar('<p>3. três</p>','3. três')
 def test_epigrafe_fecho_divergentes(self):
  with self.assertRaises(ValueError):identidade('LEI Nº 10.056, DE 07 DE OUTUBRO DE 2026 Art. 1º texto. Aracaju, 08 de outubro de 2026',dict(tipo='Lei Ordinária',numero='10056',data='2026-10-07'))

class BlocoEpigrafeTest(unittest.TestCase):
 def test_nota_revogacao_nao_e_epigrafe(self):
  from auditar_spl_html_recente import identidade_html
  s='<html><body><p>Revogada pela Lei nº 9.238, de 17 de julho de 2023</p><p><b>LEI Nº 8.825, DE 1º DE ABRIL DE 2021</b></p><p>Art. 1º Texto.</p><p>Aracaju, 1º de abril de 2021.</p></body></html>'
  q=identidade_html(s,dict(tipo='Lei Ordinária',numero='8825',data='2021-04-01'));self.assertEqual(q['data'],'2021-04-01')
 def test_citacao_no_corpo_nao_substitui_epigrafe(self):
  from auditar_spl_html_recente import identidade_html
  s='<html><body><p>LEI Nº 8.901, DE 28 DE SETEMBRO DE 2021</p><p>Art. 1º Altera Lei nº 8.901, de 28 de agosto de 2021.</p><p>Aracaju, 28 de setembro de 2021.</p></body></html>'
  with self.assertRaises(ValueError):identidade_html(s,dict(tipo='Lei Ordinária',numero='8901',data='2021-08-28'))
 def test_fecho_real_divergente(self):
  from auditar_spl_html_recente import identidade_html
  s='<html><body><p>LEI Nº 8.848, DE 04 DE JUNHO DE 2021</p><p>Art. 1º Texto.</p><p>Aracaju, 1º de junho de 2021.</p></body></html>'
  with self.assertRaises(ValueError):identidade_html(s,dict(tipo='Lei Ordinária',numero='8848',data='2021-06-04'))


class RodapeTest(unittest.TestCase):
 def test_doe_anterior_e_duvida(self):
  from auditar_spl_html_recente import cronologia_rodape
  with self.assertRaisesRegex(ValueError,'dúvida cronológica'):cronologia_rodape('<p>Este texto não substitui o publicado no D.O.E de 27.10.2020.</p>','2020-11-06')
 def test_republicacao_posterior(self):
  from auditar_spl_html_recente import cronologia_rodape
  self.assertEqual(len(cronologia_rodape('<p>Este texto não substitui o publicado no D.O.E. de 17.01.2024 e republicada no D.O.E. de 04.03.2024.</p>','2024-01-16')),2)
 def test_mencao_alheia_nao_e_rodape(self):
  from auditar_spl_html_recente import cronologia_rodape
  self.assertEqual(cronologia_rodape('<p>Altera a Lei publicada no D.O.E de 27.10.2020.</p>','2020-11-06'),[])

class EstruturaTest(unittest.TestCase):
 def test_tabela_transposta_falha(self):
  with self.assertRaises(ValueError):comparar('<table><tr><td>0,5</td><td>-100</td></tr><tr><td>10%</td><td>2</td></tr></table>','| 0,5 | 10% |\n| --- | --- |\n| -100 | 2 |')
 def test_celulas_iguais_nao_autorizam_fusao(self):
  with self.assertRaises(ValueError):comparar('<table><tr><td>A</td><td>B</td></tr></table>','| A B |\n| --- |')
 def test_heading_separador_explicito_com_prova(self):
  q=comparar('<p>CAPÍTULO I</p><p>DISPOSIÇÕES GERAIS</p>','## CAPÍTULO I — DISPOSIÇÕES GERAIS');self.assertEqual(len(q['normalizacoes_de_heading_comprovadas']),1)
if __name__=='__main__':unittest.main()
