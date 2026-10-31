import unittest
from identidade_legis_ac import conferir
from test_representacao_html_ac_legis import FOOT
ITEM=dict(tipo='Lei Ordinária',numero='4838',data='2026-09-09')
def field(title='LEI Nº 4.838, DE 09 DE SETEMBRO DE 2026',fecho='Rio Branco - Acre, 9 de setembro de 2026, 138º da República.'):
 return '<div id="body-law"><blockquote><p>'+title+'</p></blockquote><p>Art. 1º Texto.</p><p>'+fecho+'</p>'+FOOT+'</div>'
class IdentidadeACTest(unittest.TestCase):
 def test_epigrafe_fecho_card(self):self.assertEqual(conferir(field(),ITEM)['numero'],'4838')
 def test_sufixo_nao_e_ignorado(self):
  with self.assertRaises(ValueError):conferir(field(title='LEI Nº 4.838-A, DE 09 DE SETEMBRO DE 2026'),ITEM)
 def test_data_fecho_nao_e_corrigida(self):
  with self.assertRaises(ValueError):conferir(field(fecho='Rio Branco – Acre, 8 de setembro de 2026.'),ITEM)
 def test_card_data_divergente_retem(self):
  with self.assertRaises(ValueError):conferir(field(),dict(ITEM,data='2026-09-08'))
 def test_fecho_citado_distinto_nao_escolhe_um(self):
  s=field().replace(FOOT,'<p>Rio Branco - Acre, 8 de setembro de 2026.</p>'+FOOT)
  with self.assertRaises(ValueError):conferir(s,ITEM)
 def test_ordinal_separado_literal_sem_reescrever(self):
  original=field(fecho='Rio Branco-Acre, 9 º de setembro de 2026.');q=conferir(original,ITEM);self.assertIn('9 º',q['fechos'][0]['trecho'])
 def test_ausencia_de_preposicao_nao_inventa_tokens(self):
  q=conferir(field(fecho='Rio Branco-Acre, 9 setembro de 2026.'),ITEM);self.assertIn('9 setembro',q['fechos'][0]['trecho'])
 def test_preposicao_deslocada_preservada(self):
  q=conferir(field(fecho='Rio Branco, de 9 de setembro de 2026.'),ITEM);self.assertIn(', de 9',q['fechos'][0]['trecho'])
 def test_fecho_sala_sessoes_data_explicita(self):
  q=conferir(field(fecho='Sala das Sessões “Deputado Francisco Cartaxo”, 9 de setembro de 2026'),ITEM);self.assertEqual(q['fechos'][0]['data'],'2026-09-09')
 def test_formato_flexivel_nao_relaxa_data(self):
  with self.assertRaises(ValueError):conferir(field(fecho='Rio Branco-Acre, 8 setembro de 2026.'),ITEM)
 def test_epigrafe_adicional_em_celula_e_alerta_contextual(self):
  from identidade_legis_ac import epigrafes_contextuais
  s=field().replace(FOOT,'<table><tr><td>LEI Nº 93-A, DE 13 DE DEZEMBRO DE 1966 Art. 1º Texto citado.</td></tr></table>'+FOOT);q=epigrafes_contextuais(s);self.assertEqual(q[0]['numero_impresso'],'93-A');self.assertIn('Não prova duplicação',q[0]['nota'])
if __name__=='__main__':unittest.main()
