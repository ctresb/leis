import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from congelar_indice_ta_coerente import paginar
class TestIndice(unittest.TestCase):
 def api(self,pages):
  def fetch(url):
   n=int(url.rsplit('=',1)[1]);return pages[n],{'url':url}
  return fetch
 def test_coerente(self):
  rows,_,total=paginar(self.api({1:{'pagination':{'total_entries':2,'next_page':2},'results':[{'id':1}]},2:{'pagination':{'total_entries':2,'next_page':None},'results':[{'id':2}]}}),'sapl.a.leg.br');self.assertEqual([r['id'] for r in rows],[1,2]);self.assertEqual(total,2)
 def test_total_mudou_antes_dos_corpos(self):
  with self.assertRaisesRegex(ValueError,'Total mudou'):paginar(self.api({1:{'pagination':{'total_entries':5755,'next_page':2},'results':[{'id':4461}]},2:{'pagination':{'total_entries':5758},'results':[{'id':4461}]}}),'sapl.a.leg.br')
 def test_repeticao_e_ciclo(self):
  with self.assertRaisesRegex(ValueError,'ID repetido'):paginar(self.api({1:{'pagination':{'total_entries':2,'next_page':2},'results':[{'id':4461}]},2:{'pagination':{'total_entries':2},'results':[{'id':4461}]}}),'sapl.a.leg.br')
  with self.assertRaisesRegex(ValueError,'ciclica'):paginar(self.api({1:{'pagination':{'total_entries':2,'next_page':1},'results':[]}}),'sapl.a.leg.br')
if __name__=='__main__':unittest.main()
