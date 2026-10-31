import hashlib,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from preparar_reparo_alvorada4238 import preparar,conferir_replay,BASE,ROOT
from auditar_municipal import metadados
class TestReparo(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.candidate,cls.native,cls.proof=preparar()
 def test_ato_inteiro_identidade_data_e_limites(self):
  self.assertEqual(self.proof['caracteres_nao_brancos'],2498);self.assertEqual(self.proof['codigo_ibge'],'4300604');self.assertIn('PREFEITURA MUNICIPAL DE ALVORADA',self.proof['fonte_cabecalho'])
  for token in ['Art. 1º.','Art. 2º.','Art. 3º.','Art. 4º. Esta lei entra em vigor na data da sua publicação.','ANEXO I','VIII -Executar outras tarefas correlatas.','Código Identificador:6D5C2FBB']:
   self.assertIn(token,self.native)
  self.assertNotIn('4.239',self.native);self.assertNotIn('306D4F67',self.native);meta=metadados(self.candidate);self.assertEqual(meta['data'],'2026-02-02');self.assertEqual(meta['baixado_em'],'2026-10-15')
 def test_perda_de_artigo_numero_e_troca_de_ordem_rejeitadas(self):
  body=self.candidate.split('\n---\n',1)[1].lstrip('\n').split('\n\n',1)[1].removesuffix('\n')
  self.assertTrue(conferir_replay(body,self.native))
  for bad in [body.replace('Esta lei entra em vigor na data da sua publicação.',''),body.replace('3.990,00','3.990,01'),body.replace('I -01 (um)','I -02 (um)')]:
   with self.assertRaises(ValueError):conferir_replay(bad,self.native)
 def test_enfases_provadas_e_canoniconao_escrito(self):
  self.assertIn('<em>',self.candidate);self.assertIn('<strong>',self.candidate);path=ROOT/'municipais/RS/alvorada/leis-ordinarias/2026/lei-ordinaria-4238-2026-6d5c2fbb.md';before=path.read_bytes();preparar();self.assertEqual(path.read_bytes(),before);self.assertEqual(hashlib.sha256((BASE/'preimagem-head.md').read_bytes()).hexdigest(),self.proof['sha256_preimagem'])
if __name__=='__main__':unittest.main()
