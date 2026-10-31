import unittest
from pe_identidade_ct import comprovar_ct
class CTPE(unittest.TestCase):
    def setUp(self):self.item={'tipo':'8','nome':'Portaria Administrativa da Alepe n° 51-C','id':'90017'};self.body='**PORTARIA Nº 051 - CT, DE 21 DE SETEMBRO DE 2026.**\n\nRESOLVE: designar.'
    def test_divergencia_explicita_sem_mutacao(self):
        adjusted,p=comprovar_ct(self.item,self.body);self.assertEqual(p['numero'],'51-CT');self.assertEqual(p['data'],'2026-09-21');self.assertTrue(self.item['nome'].endswith('51-C'));self.assertTrue(adjusted['nome'].endswith('51-CT'));self.assertIn('051 - CT',p['epigrafe_literal'])
    def test_numero_sufixo_tipo_errados_falham(self):
        for body in (self.body.replace('051','052'),self.body.replace(' - CT','-C'),self.body.replace('PORTARIA','LEI')):
            with self.subTest(body=body):
                with self.assertRaises(ValueError):comprovar_ct(self.item,body)
    def test_citacao_no_corpo_nao_substitui_epigrafe(self):
        with self.assertRaises(ValueError):comprovar_ct(self.item,'EMENTA\n'+('\n'.join(['Um parágrafo']*7))+'\n'+self.body)
if __name__=='__main__':unittest.main()
