import unittest
from auditar_rn_retomada_pdf import identidade
class IdentidadeRN(unittest.TestCase):
    def setUp(self):
        self.item={'titulo':'Lei Ordinária 12.931 de 19.10.2026','lista':'leis-ordinarias'}
        self.source='LEI Nº 12.931, DE 19 DE OUTUBRO DE 2026.\nArt. 1º Fica instituído o programa.'
    def test_epigrafe_propria(self):self.assertEqual(identidade(self.source,self.item)['data'],'2026-10-19')
    def test_numero_data_tipo_divergentes(self):
        for a,b in [('12.931','12.930'),('19 DE OUTUBRO','18 DE OUTUBRO'),('LEI Nº','LEI COMPLEMENTAR Nº')]:
            with self.subTest(mudanca=b):
                with self.assertRaises(ValueError):identidade(self.source.replace(a,b),self.item)
    def test_ementa_sem_normativo(self):
        with self.assertRaises(ValueError):identidade(self.source.split('\n')[0],self.item)
if __name__=='__main__':unittest.main()
