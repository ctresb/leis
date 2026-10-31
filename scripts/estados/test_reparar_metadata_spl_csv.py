import unittest,json
from reparar_metadata_spl_csv import candidato,ementa_original
SOURCE='<html><body><h1>LEI Nº 8.886, DE 31 DE AGOSTO DE 2021</h1><h2>Altera o § 1º e mantém “f^’”, 0,5 e -100.</h2><p>O GOVERNADOR DO ESTADO DE SERGIPE,</p><p>Art. 1º texto.</p></body></html>'.encode()
class MetadataTest(unittest.TestCase):
 def test_corpo_integral_preservado_e_literal(self):
  meta={'fonte':'https://oficial/norma.aspx?id="b"','revogada':False,'situacao':'"h"','ementa':'Altera o § 1º'};raw=('---\n'+''.join(k+': '+json.dumps(v,ensure_ascii=False)+'\n' for k,v in meta.items())+'---\n# Lei\n\n**Art. 1º** 0,5 -100.\n').encode();new,q=candidato(raw,SOURCE,'https://oficial/L88862021.html','8886','2021');self.assertEqual(new.split(b'\n---\n',1)[1],raw.split(b'\n---\n',1)[1]);self.assertIn('“f^’”, 0,5 e -100.',new.decode());self.assertEqual(len(q['alteracoes']),4)
 def test_epigrafe_errada_falha(self):
  with self.assertRaises(ValueError):ementa_original(SOURCE,'8885','2021')
 def test_ementa_ausente_nao_inventada(self):
  with self.assertRaises(ValueError):ementa_original(SOURCE.replace(b'<h2>',b'<p>Art. 1').replace(b'</h2>',b'</p>'),'8886','2021')
if __name__=='__main__':unittest.main()
