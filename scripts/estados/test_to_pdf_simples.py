"""Fixtures sintéticos; não são fontes de inclusão legislativa."""
import gzip,hashlib,json,tempfile,unittest
from pathlib import Path
from auditar_to_pdf_simples import auditar
SHA=lambda b:hashlib.sha256(b).hexdigest()
class PDFTO(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.p=Path(self.tmp.name);index='<div>Registros encontrados: 1<div class="row"><div class="col-12"><h4><a href="/arquivo/999">Lei nº 123 de 2020 (ordinária)</a></h4><p><small>Categoria: Legislação Estadual</small><small> | Data: 01/01/2020</small></p></div><div><em><strong>Teste</strong></em></div></div></div>'.encode();z=gzip.compress(index);p=self.p/'index.gz';p.write_bytes(z);self.index=dict(url='https://www.al.to.leg.br/legislacaoEstadual?documento.ano=2020',url_final='https://www.al.to.leg.br/legislacaoEstadual?documento.ano=2020',http=200,cache=str(p),sha256_fonte=SHA(index),sha256_cache=SHA(z))
 def row(self,name):
  b=(Path('estaduais/TO/_fonte/auditorias/portal-testes-20261027-005')/(name+'.pdf')).read_bytes();z=gzip.compress(b);p=self.p/(name+'.gz');p.write_bytes(z);return dict(item=dict(indice=self.index,fonte='https://www.al.to.leg.br/arquivo/999',id_ALETO='999',numero='123',ano_titulo='2020',data_cartao='2020-01-01',tipo='Lei Ordinária',pasta='leis-ordinarias'),url='https://www.al.to.leg.br/arquivo/999',url_final='https://www.al.to.leg.br/arquivos/999.pdf',http=200,cache=str(p),sha256_fonte=SHA(b),sha256_cache=SHA(z))
 def test_preserva_numero_zero_decimal_negativo(self):
  b,q=auditar(self.row('simples'));self.assertIn('\n0\n',b);self.assertIn('-100,00',b);self.assertIn('0,5%',b);self.assertTrue(q['CommonMark_cercas_iguais'])
 def test_vetor_retem(self):
  with self.assertRaisesRegex(ValueError,'raster/vetor'):auditar(self.row('vetor'))
 def test_branco_retem(self):
  with self.assertRaisesRegex(ValueError,'colorido/oculto'):auditar(self.row('branco'))
 def test_compilacao_retem(self):
  with self.assertRaisesRegex(ValueError,'contexto histórico'):auditar(self.row('anotacao_editorial'))
 def test_ato_vizinho_retem(self):
  with self.assertRaisesRegex(ValueError,'ato alheio'):auditar(self.row('ato_vizinho'))
 def test_data_cartao_nao_e_corrigida(self):
  r=self.row('simples');r['item']['data_cartao']='2020-01-02'
  with self.assertRaisesRegex(ValueError,'cartão'):auditar(r)
 def test_sha_divergente_retem(self):
  r=self.row('simples');r['sha256_fonte']='0'*64
  with self.assertRaisesRegex(ValueError,'diverge'):auditar(r)
if __name__=='__main__':unittest.main()
