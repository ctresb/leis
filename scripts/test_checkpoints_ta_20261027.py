import hashlib,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from auditar_checkpoints_ta_20261027 import validar
class TestCheckpoints(unittest.TestCase):
 def fixture(self,p):
  folder=p/'captura';cache=p/'cache';folder.mkdir();cache.mkdir();raw=b'{"id": 1}';url='https://sapl.a.leg.br/api/1';stem=hashlib.sha256(url.encode()).hexdigest();(cache/(stem+'.json')).write_bytes(raw);meta=cache/(stem+'.meta.json');meta.write_text(json.dumps(dict(sha256=hashlib.sha256(raw).hexdigest(),status=200,url=url)));(folder/'resultados.jsonl').write_text('{"ta_id": 1}\n');(folder/'checkpoint.json').write_text('{"1": {}}');return folder,cache,meta
 def test_cache_valido_e_bloqueio_nao_retomado(self):
  with tempfile.TemporaryDirectory() as t:
   folder,cache,meta=self.fixture(Path(t));self.assertTrue(validar('sapl.a.leg.br',folder,cache)[0]['apto_retomada']);d=json.loads(meta.read_text());d['status']=429;meta.write_text(json.dumps(d));r,_=validar('sapl.a.leg.br',folder,cache);self.assertFalse(r['apto_retomada']);self.assertEqual(len(r['bloqueios']),1)
 def test_orfao_parcial_e_checkpoint_adiante_retidos(self):
  with tempfile.TemporaryDirectory() as t:
   folder,cache,_=self.fixture(Path(t));(cache/'orfao.html').write_text('parcial');self.assertFalse(validar('sapl.a.leg.br',folder,cache)[0]['apto_retomada']);(cache/'orfao.html').unlink();(folder/'resultados.jsonl').write_text('{"ta_id":1}\n{');self.assertFalse(validar('sapl.a.leg.br',folder,cache)[0]['apto_retomada']);(folder/'resultados.jsonl').write_text('{"ta_id":1}\n');(folder/'checkpoint.json').write_text('{"2": {}}');self.assertFalse(validar('sapl.a.leg.br',folder,cache)[0]['apto_retomada'])
if __name__=='__main__':unittest.main()
