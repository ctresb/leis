import unittest,hashlib,json
from metadados_to_pdf import criar,verificar,data_captura
class MetadadosTO(unittest.TestCase):
 def setUp(self):
  self.row=dict(capturado_em='2026-10-28T01:00:00+00:00',url='https://www.al.to.leg.br/arquivo/999',url_final='https://www.al.to.leg.br/arquivos/999.pdf',sha256_fonte='a'*64,item=dict(id_ALETO='999'));self.body='Página 1\n\n```text\n0\n-100,00 0,5%\n```\n';self.q=dict(sha256_corpo=hashlib.sha256(self.body.encode()).hexdigest(),epigrafe='LEI Nº 123, DE 1 DE JANEIRO DE 2020',tipo='Lei Ordinária',numero='123',data='2020-01-01')
 def meta(self,blob):
  h,b=blob.decode()[4:].split('\n---\n',1);return dict((k,json.loads(v)) for k,v in (l.split(': ',1) for l in h.splitlines())),b
 def test_data_offset(self):self.assertEqual(data_captura(self.row),'2026-10-27')
 def test_captura_sem_offset_falha(self):
  self.row['capturado_em']='2026-10-28T01:00:00'
  with self.assertRaises(ValueError):data_captura(self.row)
 def test_corpo_integral_esquema_nulo(self):
  meta,body=self.meta(criar(self.row,self.q,self.body));self.assertEqual(body,'# '+self.q['epigrafe']+'\n\n'+self.body);self.assertIsNone(meta['revogada']);self.assertIsNone(meta['situacao']);self.assertEqual(meta['baixado_em'],'2026-10-27');self.assertTrue(verificar(meta,self.row));self.assertLess(list(meta).index('versao_texto'),list(meta).index('fonte'))
 def test_corpo_alterado_falha(self):
  with self.assertRaises(ValueError):criar(self.row,self.q,self.body.replace('-100,00','100,00'))
 def test_campo_ausente_falha(self):
  meta,_=self.meta(criar(self.row,self.q,self.body));del meta['versao_texto']
  with self.assertRaises(ValueError):verificar(meta,self.row)
if __name__=='__main__':unittest.main()
