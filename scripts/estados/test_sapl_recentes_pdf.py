import unittest
from auditar_sapl_recentes_pdf import identidade
class EpigrafeAM(unittest.TestCase):
    def setUp(self):self.item={'numero':'8562','data':'2026-10-14','ano':2026};self.text='LEI Nº 8.562, DE 14 DE OUTUBRO DE 2026.\nArt. 1º Fica instituído o dia.'
    def test_identidade_oficial(self):self.assertEqual(identidade(self.text,self.item)['numero'],'8562')
    def test_divergencias_nao_sao_silenciadas(self):
        for field,val in [('numero','8561'),('data','2026-10-13'),('ano',2025)]:
            with self.subTest(field=field):
                with self.assertRaises(ValueError):identidade(self.text,dict(self.item,**{field:val}))
if __name__=='__main__':unittest.main()
