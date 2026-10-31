import copy,unittest
from reexecutar_legis_ac import conferir_revisao_contextual
class Revisao(unittest.TestCase):
 def setUp(self):
  self.row=dict(item=dict(id_LEGIS='1',tipo='Lei Ordinária',numero='100',data='2026-01-01'),sha256_fonte='fonte');self.q=dict(sha256_corpo='corpo',fidelidade=dict(sha256_matrizes='matriz'),contextos_objetos=['Anexo Único'],epigrafes_contextuais=[]);self.r=dict(self.row['item'],decisao='apto_contextual',sha256_fonte='fonte',sha256_corpo='corpo',sha256_matrizes='matriz',contextos_objetos=['Anexo Único'],epigrafes_contextuais=[],fundamento='Anexo identificado e presente no campo integral.')
 def test_exige_revisao_explicita(self):
  with self.assertRaisesRegex(ValueError,'ausente'):conferir_revisao_contextual(None,self.row,self.q)
 def test_revisao_apenas_para_mesmos_bytes_contextos(self):
  self.assertTrue(conferir_revisao_contextual(self.r,self.row,self.q));self.r['sha256_fonte']='outra'
  with self.assertRaisesRegex(ValueError,'diverge'):conferir_revisao_contextual(self.r,self.row,self.q)
 def test_identidade_nao_pode_mudar(self):
  self.r['numero']='101'
  with self.assertRaisesRegex(ValueError,'identidade'):conferir_revisao_contextual(self.r,self.row,self.q)
 def test_contexto_nao_pode_mudar(self):
  self.r['contextos_objetos']=['outra referência']
  with self.assertRaisesRegex(ValueError,'contextos'):conferir_revisao_contextual(self.r,self.row,self.q)
 def test_epigrafe_secundaria_nao_e_liberada_por_lista(self):
  self.r['epigrafes_contextuais']=self.q['epigrafes_contextuais']=['outra lei']
  with self.assertRaisesRegex(ValueError,'epígrafes'):conferir_revisao_contextual(self.r,self.row,self.q)
if __name__=='__main__':unittest.main()
