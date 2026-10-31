import hashlib,unittest
from candidato_legis_ac import criar
from metadados_legis_ac import ler,verificar
class Candidato(unittest.TestCase):
 def setUp(self):
  self.row=dict(item=dict(titulo_indice='Lei nº 1',tipo='Lei Ordinária',numero='1',data='2026-01-01',fonte='https://legis.ac.gov.br/detalhar/1',id_LEGIS='1'),url='https://legis.ac.gov.br/detalhar/1',capturado_em='2026-10-27T20:00:00-03:00');self.body='<div id="body-law">R$ -100,00 0,5%</div>';self.q=dict(sha256_corpo=hashlib.sha256(self.body.encode()).hexdigest(),ementa_indice='E')
 def test_candidato_nasce_com_esquema_e_corpo_fiel(self):
  b=criar(self.row,self.q,self.body,'Detalhada');m,body=ler(b);self.assertTrue(verificar(m,self.row));self.assertEqual(body,('# Lei nº 1\n\n'+self.body).encode())
 def test_nao_aceita_corpo_nao_auditado(self):
  with self.assertRaises(ValueError):criar(self.row,self.q,self.body+'alterado','Detalhada')
 def test_mantem_observacao_contextual(self):
  m,b=ler(criar(self.row,self.q,self.body,'Detalhada','Anexo conferido.'));self.assertEqual(m['observacao_contextual'],'Anexo conferido.');self.assertIsNone(m['revogada'])
if __name__=='__main__':unittest.main()
