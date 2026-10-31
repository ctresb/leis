"""Regressões no pipeline completo, usando captura oficial congelada."""
import copy,gzip,hashlib,json,tempfile,unittest
from pathlib import Path
from auditar_legis_ac import AuditorAC
SHA=lambda b:hashlib.sha256(b).hexdigest()
class Pipeline(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.row=json.loads(Path('scripts/estados/manifestos/ac-legis-fontes-500-20261027-010.json').read_text())['capturas'][0]
  cls.raw=gzip.decompress(Path(cls.row['cache']).read_bytes()).decode('utf-8-sig')
  cls.a=AuditorAC(json.loads(Path('estaduais/AC/_fonte/auditorias/legis-CSS-20261027-008/recibos-normalizados-18.json').read_text()),json.loads(Path('estaduais/AC/_fonte/auditorias/legis-JS-norma-20261027-012/recursos-observados.json').read_text())[0])
 def edit(self,old,new):
  assert old in self.raw
  r=copy.deepcopy(self.row);b=self.raw.replace(old,new).encode();t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);p=Path(t.name)/'fonte.gz';z=gzip.compress(b);p.write_bytes(z);r.update(cache=str(p),sha256_fonte=SHA(b),sha256_cache=SHA(z));return r
 def test_pipeline_real(self):
  body,q=self.a.auditar(self.row);self.assertIsNone(q['revogada']);self.assertEqual(q['sha256_corpo'],SHA(body.encode()))
 def test_sha_fonte(self):
  r=copy.deepcopy(self.row);r['sha256_fonte']='0'*64
  with self.assertRaisesRegex(ValueError,'SHA'):self.a.auditar(r)
 def test_url_fonte(self):
  r=copy.deepcopy(self.row);r['url_final']='https://example.org/'
  with self.assertRaisesRegex(ValueError,'URL'):self.a.auditar(r)
 def test_tachado_js_nao_vigencia(self):
  r=self.edit('name="leis_revogadas_guard" value="0"','name="leis_revogadas_guard" value="1"')
  with self.assertRaisesRegex(ValueError,'tachado total'):self.a.auditar(r)
 def test_incorporacao_posterior_nao_e_versao_original(self):
  r=self.edit('</blockquote>','</blockquote><p>(Incluído pela Lei nº 9.999, de 01/01/2027)</p>')
  with self.assertRaisesRegex(ValueError,'incorporação legislativa posterior'):self.a.auditar(r)
 def test_corpo_igualdade_estrita(self):
  with self.assertRaisesRegex(ValueError,'corpo privado'):self.a.auditar(self.row,'outro texto')
 def test_data_cartao(self):
  r=copy.deepcopy(self.row);r['item']['data']='2026-09-08'
  with self.assertRaisesRegex(ValueError,'cartão'):self.a.auditar(r)
if __name__=='__main__':unittest.main()
