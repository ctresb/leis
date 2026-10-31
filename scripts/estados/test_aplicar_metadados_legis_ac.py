import unittest
from aplicar_metadados_legis_ac import par
from metadados_legis_ac import acrescentar
import json
ROW=dict(capturado_em='2026-10-27T20:37:12.123456-03:00')
def blob():
 meta=dict(titulo='Lei nº 1',tipo='Lei Ordinária',numero='1',data='2026-01-01',uf='AC',fonte='https://legis.ac.gov.br/detalhar/1',edicao='Detalhada')
 return ('---\n'+''.join(k+': '+json.dumps(v,ensure_ascii=False)+'\n' for k,v in meta.items())+'---\n').encode()+'# Lei nº 1\n\nArt. 1º R$ -100,00; João.\n'.encode()
class Patch(unittest.TestCase):
 def test_patch_dois_campos_passa(self):
  old=blob();new,p=acrescentar(old,ROW);self.assertEqual(par(old,new,ROW),p)
 def test_corpo_alterado_falha(self):
  old=blob();new,p=acrescentar(old,ROW)
  with self.assertRaisesRegex(ValueError,'excede'):par(old,new.replace(b'-100,00',b'100,00'),ROW)
 def test_outro_metadado_alterado_falha(self):
  old=blob();new,p=acrescentar(old,ROW)
  with self.assertRaisesRegex(ValueError,'excede'):par(old,new.replace(b'"Detalhada"',b'"Outra"'),ROW)
 def test_h1_alterado_falha(self):
  old=blob();new,p=acrescentar(old,ROW)
  with self.assertRaisesRegex(ValueError,'excede'):par(old,new.replace('Lei nº 1\n\n'.encode(),'Lei nº 2\n\n'.encode()),ROW)
if __name__=='__main__':unittest.main()
