import unittest
from am_legisla_head import conferir,namespace
class HeadAM(unittest.TestCase):
 def doc(self):return dict(destino='novo.md',QA=dict(tipo='Lei Ordinária',numero='100',data='2026-01-01'),captura=dict(item=dict(url='https://legisla.imprensaoficial.am.gov.br/diario_am/12/2026/1/7')))
 def old(self,n='200',tipo='Lei Ordinária',fonte='https://sapl.al.am.leg.br/norma/7'):return dict(path='estaduais/AM/leis-ordinarias/2026/old.md',meta=dict(tipo=tipo,numero=n,data='2026-01-01',fonte=fonte))
 def test_SAPL_ID_igual_nao_e_alias_Legisla(self):self.assertEqual(len(conferir([self.doc()],dict(documentos=[self.old()]),{'novo.md':None})),1)
 def test_mesmo_numero_entre_fontes_e_alias(self):
  with self.assertRaises(ValueError):conferir([self.doc()],dict(documentos=[self.old(n='100')]),{'novo.md':None})
 def test_pasta_protege_tipo_variado_e_ID_proprio(self):
  with self.assertRaises(ValueError):conferir([self.doc()],dict(documentos=[self.old(n='100',tipo='Lei')]),{'novo.md':None})
  with self.assertRaises(ValueError):conferir([self.doc()],dict(documentos=[self.old(fonte=self.doc()['captura']['item']['url'])]),{'novo.md':None})
 def test_destino_presente_ou_faltante_falha(self):
  for mapa in ({},{'novo.md':'abc'}):
   with self.assertRaises(ValueError):conferir([self.doc()],dict(documentos=[]),mapa)
if __name__=='__main__':unittest.main()
