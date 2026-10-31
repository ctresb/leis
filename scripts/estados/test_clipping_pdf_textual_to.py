"""Fixtures gráficos somente em memória, sem documentos candidatos ou rede."""
import io,unittest
from pathlib import Path
from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject,DecodedStreamObject,RectangleObject,NumberObject,ArrayObject
from clipping_pdf_textual_to import conferir,concat
class Clipping(unittest.TestCase):
 def pdf(self,content,change=None):
  reader=PdfReader(io.BytesIO(Path('estaduais/TO/_fonte/auditorias/portal-testes-clipping-20261028-012/fonte-original.pdf').read_bytes()));w=PdfWriter();w.add_page(reader.pages[0]);p=w.pages[0];s=DecodedStreamObject();s.set_data(content);p[NameObject('/Contents')]=w._add_object(s)
  if change:change(p)
  out=io.BytesIO();w.write(out);return out.getvalue()
 def text(self,x=100,y=100):return f'BT /R13 12 Tf 1 0 0 1 {x} {y} Tm (A) Tj ET\n'.encode()
 def test_fonte_original(self):
  q=conferir(Path('estaduais/TO/_fonte/auditorias/portal-testes-clipping-20261028-012/fonte-original.pdf').read_bytes());self.assertEqual(q['total_recortes'],1);self.assertGreater(q['paginas'][0]['glifos'],100)
 def test_retangulo_pagina(self):self.assertEqual(conferir(self.pdf(b'0 0 612 1008 re W n\n'+self.text()))['total_recortes'],1)
 def test_glifo_recortado_retem(self):
  with self.assertRaisesRegex(ValueError,'glifo'):conferir(self.pdf(b'0 0 50 50 re W n\n'+self.text()))
 def test_bbox_programa_amplia_extrator(self):
  # Origem/advance aproximados ficam dentro, mas a caixa de TODOS os contornos
  # da fonte ultrapassa x=99,5 e deve reter conservadoramente.
  with self.assertRaisesRegex(ValueError,'glifo'):conferir(self.pdf(b'99.5 0 512.5 1008 re W n\n'+self.text()))
 def test_fontbbox_declarado_errado_nao_aperta_programa(self):
  def change(p):p['/Resources']['/Font']['/R13']['/FontDescriptor'][NameObject('/FontBBox')]=ArrayObject([NumberObject(0),NumberObject(0),NumberObject(1),NumberObject(1)])
  with self.assertRaisesRegex(ValueError,'glifo'):conferir(self.pdf(b'99.5 0 512.5 1008 re W n\n'+self.text(),change))
 def test_ctm_escala(self):
  q=conferir(self.pdf(b'q .1 0 0 .1 0 0 cm 0 0 6120 10080 re W n BT /R13 120 Tf 1 0 0 1 1000 1000 Tm (A) Tj ET Q\n'));self.assertEqual(q['paginas'][0]['recortes'][0]['retangulo'],[0,0,612,1008])
 def test_ctm_translacao_composicao(self):self.assertEqual(concat((.1,0,0,.1,0,0),(1,0,0,1,120,120)),(.1,0,0,.1,12,12))
 def test_save_restore_matriz(self):
  q=conferir(self.pdf(b'q 2 0 0 2 0 0 cm Q\n'+self.text()));self.assertLess(q['paginas'][0]['caixa_glifos'][2],120)
 def test_intersecao_mantida(self):
  q=conferir(self.pdf(b'0 0 612 1008 re W n 20 20 560 900 re W n\n'+self.text()));self.assertEqual(q['paginas'][0]['recortes'][1]['intersecao_ativa'],[20,20,580,920])
 def test_intersecao_vazia_retem(self):
  with self.assertRaisesRegex(ValueError,'vazia'):conferir(self.pdf(b'0 0 50 50 re W n 100 100 50 50 re W n\n'+self.text()))
 def test_restore_recorte_prova_mais_conservadora(self):
  # Mesmo restaurado antes do texto, o retângulo estreito é retido; não usamos
  # esse teste como licença para ignorar glifos fora de algum recorte observado.
  with self.assertRaisesRegex(ValueError,'glifo'):conferir(self.pdf(b'q 0 0 50 50 re W n Q\n'+self.text()))
 def test_rotacao_pagina_retem(self):
  with self.assertRaisesRegex(ValueError,'rotação'):conferir(self.pdf(self.text(),lambda p:p.__setitem__(NameObject('/Rotate'),NumberObject(90))))
 def test_shear_retem(self):
  with self.assertRaisesRegex(ValueError,'shear'):conferir(self.pdf(b'q 1 .1 0 1 0 0 cm 0 0 612 1008 re W n\n'+self.text()+b'Q'))
 def test_poligono_cruzado_retem(self):
  with self.assertRaises(ValueError):conferir(self.pdf(b'0 0 m 612 1008 l 0 1008 l 612 0 l h W n\n'+self.text()))
 def test_rotacao_diamante_retem(self):
  with self.assertRaises(ValueError):conferir(self.pdf(b'q .707 .707 -.707 .707 0 0 cm 0 0 612 1008 re W n\n'+self.text()+b'Q'))
 def test_fontsize_escala_rise(self):
  q=conferir(self.pdf(b'BT /R13 12 Tf 200 Tz 15 Ts 1 0 0 1 100 100 Tm (A) Tj ET'));b=q['paginas'][0]['caixa_glifos'];self.assertGreater(b[2],115);self.assertGreater(b[1],110)
 def test_pintura_retem(self):
  with self.assertRaisesRegex(ValueError,'pintura'):conferir(self.pdf(b'0 0 612 1008 re f\n'+self.text()))
 def test_save_sem_restore_retem(self):
  with self.assertRaisesRegex(ValueError,'encerrado'):conferir(self.pdf(b'q\n'+self.text()))
 def test_restore_sem_save_retem(self):
  with self.assertRaisesRegex(ValueError,'restore'):conferir(self.pdf(b'Q\n'+self.text()))
 def test_multiplos_subcaminhos_retem(self):
  with self.assertRaisesRegex(ValueError,'subcaminhos'):conferir(self.pdf(b'0 0 m 612 0 l 612 1008 l 0 1008 l h 10 10 m 20 20 l W n\n'+self.text()))
 def test_origem_nao_zero_retem(self):
  with self.assertRaisesRegex(ValueError,'origem'):conferir(self.pdf(self.text(),lambda p:setattr(p,'mediabox',RectangleObject([10,10,612,1008]))))
 def test_userunit_retem(self):
  with self.assertRaisesRegex(ValueError,'UserUnit'):conferir(self.pdf(self.text(),lambda p:p.__setitem__(NameObject('/UserUnit'),NumberObject(2))))
 def test_texto_rotacionado_caixa_transformada(self):
  q=conferir(self.pdf(b'BT /R13 12 Tf 0 1 -1 0 100 100 Tm (A) Tj ET'));b=q['paginas'][0]['caixa_glifos'];self.assertLess(b[0],100);self.assertGreater(b[3],108)
 def test_texto_shear_caixa_transformada(self):
  q=conferir(self.pdf(b'BT /R13 12 Tf 1 .2 .3 1 100 100 Tm (A) Tj ET'));b=q['paginas'][0]['caixa_glifos'];self.assertGreater(b[2],111);self.assertGreater(b[3],110)
 def test_sem_programa_fonte_retem(self):
  def change(p):del p['/Resources']['/Font']['/R13']['/FontDescriptor']['/FontFile3']
  with self.assertRaisesRegex(ValueError,'programa incorporado'):conferir(self.pdf(self.text(),change))
 def test_truetype_unidades_e_contornos(self):
  from fontTools.fontBuilder import FontBuilder
  from fontTools.pens.ttGlyphPen import TTGlyphPen
  from pypdf.generic import DictionaryObject
  fb=FontBuilder(2048,isTTF=True);fb.setupGlyphOrder(['.notdef','A']);glyphs={}
  for name,points in [('.notdef',[(0,0),(100,0),(100,100),(0,100)]),('A',[(-128,0),(128,1800),(1400,0)])]:
   pen=TTGlyphPen(None);pen.moveTo(points[0])
   for point in points[1:]:pen.lineTo(point)
   pen.closePath();glyphs[name]=pen.glyph()
  fb.setupGlyf(glyphs);fb.setupHorizontalMetrics({'.notdef':(2048,0),'A':(2048,-128)});fb.setupHorizontalHeader(ascent=1800,descent=-200);fb.setupCharacterMap({65:'A'});fb.setupNameTable(dict(familyName='QAClip',styleName='Regular',uniqueFontIdentifier='QAClip',fullName='QAClip',psName='QAClip'));fb.setupOS2(sTypoAscender=1800,sTypoDescender=-200,usWinAscent=1800,usWinDescent=200);fb.setupPost();fb.setupMaxp();program=io.BytesIO();fb.save(program)
  reader=PdfReader(io.BytesIO(self.pdf(self.text())));w=PdfWriter();w.add_page(reader.pages[0]);p=w.pages[0];stream=DecodedStreamObject();stream.set_data(program.getvalue());descriptor=DictionaryObject({NameObject('/Type'):NameObject('/FontDescriptor'),NameObject('/FontName'):NameObject('/QAClip'),NameObject('/FontBBox'):ArrayObject([NumberObject(0),NumberObject(0),NumberObject(1),NumberObject(1)]),NameObject('/Ascent'):NumberObject(1800),NameObject('/Descent'):NumberObject(-200),NameObject('/Flags'):NumberObject(32),NameObject('/FontFile2'):w._add_object(stream)});font=DictionaryObject({NameObject('/Type'):NameObject('/Font'),NameObject('/Subtype'):NameObject('/TrueType'),NameObject('/BaseFont'):NameObject('/QAClip'),NameObject('/Encoding'):NameObject('/WinAnsiEncoding'),NameObject('/FontDescriptor'):w._add_object(descriptor),NameObject('/FirstChar'):NumberObject(65),NameObject('/LastChar'):NumberObject(65),NameObject('/Widths'):ArrayObject([NumberObject(1000)])});p['/Resources']['/Font'][NameObject('/R13')]=w._add_object(font);out=io.BytesIO();w.write(out);q=conferir(out.getvalue());proof=q['paginas'][0]['fontes'][0];self.assertEqual(proof['tipo_programa'],'TrueType');self.assertEqual(proof['caixa_programa_conservadora'],[-62.5,0,683.59375,878.90625]);self.assertLess(q['paginas'][0]['caixa_glifos'][0],100)
if __name__=='__main__':unittest.main()
