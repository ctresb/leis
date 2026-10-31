import unittest,io
from pathlib import Path
from pypdf import PdfReader,PdfWriter
from pypdf.generic import DictionaryObject,NameObject,TextStringObject,DecodedStreamObject,RectangleObject
from visibilidade_pdf_to import conferir
class Visibilidade(unittest.TestCase):
 def fonte(self):return Path('estaduais/TO/_fonte/auditorias/portal-testes-20261027-005/simples.pdf').read_bytes()
 def alterar(self,callback):
  w=PdfWriter();w.clone_document_from_reader(PdfReader(io.BytesIO(self.fonte())));callback(w);out=io.BytesIO();w.write(out);return out.getvalue()
 def marcado(self,w,props):
  stream=DecodedStreamObject();stream.set_data(b'/Span '+props+b' BDC\n'+w.pages[0].get_contents().get_data()+b'\nEMC\n');w.pages[0][NameObject('/Contents')]=stream
 def test_pdf_simples(self):self.assertEqual(conferir(self.fonte())['total_paginas'],1)
 def test_recorte_retem(self):
  raw=self.alterar(lambda w:setattr(w.pages[0],'cropbox',RectangleObject([0,0,100,100])))
  with self.assertRaisesRegex(ValueError,'CropBox'):conferir(raw)
 def test_ocg_retem(self):
  def change(w):w._root_object[NameObject('/OCProperties')]=DictionaryObject({NameObject('/D'):DictionaryObject()})
  with self.assertRaisesRegex(ValueError,'opcionais'):conferir(self.alterar(change))
 def test_actualtext_retem(self):
  with self.assertRaisesRegex(ValueError,'alternativo'):conferir(self.alterar(lambda w:self.marcado(w,b'<< /ActualText (OUTRO) >>')))
 def test_mcid_nao_modifica_texto(self):self.assertTrue(conferir(self.alterar(lambda w:self.marcado(w,b'<< /MCID 0 >>')))['sem_texto_alternativo'])
 def test_alt_retem(self):
  with self.assertRaisesRegex(ValueError,'alternativo'):conferir(self.alterar(lambda w:self.marcado(w,b'<< /Alt (OMISSO) >>')))
if __name__=='__main__':unittest.main()
