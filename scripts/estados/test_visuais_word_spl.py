import unittest
from visuais_word_spl import conferir
IMG=[dict(url='https://oficial/logo.png',sha256='a'*64)]
SRC='<html><body><!--[if vml]><v:shape id="X" type="#_x0000_t75"><v:imagedata src="logo.wmz"/></v:shape><![endif]--><img src="logo.png" v:shapes="X"><p>LEI Nº 1</p></body></html>'
class VisualTest(unittest.TestCase):
 def test_cabecalho_associado(self):self.assertEqual(len(conferir(SRC,'https://oficial/doc.html',IMG)['pictures_VML_cabecalho']),1)
 def test_shape_sem_fallback_retido(self):
  with self.assertRaises(ValueError):conferir(SRC.replace('v:shapes="X"','v:shapes="Y"'),'https://oficial/doc.html',IMG)
 def test_textbox_retido(self):
  with self.assertRaises(ValueError):conferir(SRC.replace('<v:imagedata','<v:textbox>Texto</v:textbox><v:imagedata'),'https://oficial/doc.html',IMG)
 def test_matematica_retida(self):
  with self.assertRaises(ValueError):conferir(SRC.replace('<p>','<m:oMath>x</m:oMath><p>'),'https://oficial/doc.html',IMG)
if __name__=='__main__':unittest.main()
