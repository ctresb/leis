import re,unittest
from referencias_inline_to import conferir_referencias
HEAD=re.compile(r'LEI Nº \d+, DE \d+ DE JANEIRO DE \d{4}',re.I)
class Referencias(unittest.TestCase):
    def avaliar(self,t):return conferir_referencias(t,list(HEAD.finditer(t)))
    def test_remissao_literal(self):
        t='LEI Nº 1, DE 1 DE JANEIRO DE 2020\nArt. 1º A Lei nº 2, de 2 de janeiro de 2019 passa a vigorar...'
        r=self.avaliar(t);self.assertEqual(len(r),1);self.assertEqual(r[0]['referencia_literal'],'Lei nº 2, de 2 de janeiro de 2019')
    def test_ementa(self):
        self.assertEqual(len(self.avaliar('LEI Nº 1, DE 1 DE JANEIRO DE 2020\nAltera a Lei nº 2, de 2 de janeiro de 2019.')),1)
    def test_cabecalho_vizinho_retem(self):
        with self.assertRaisesRegex(ValueError,'linha/coluna'):self.avaliar('LEI Nº 1, DE 1 DE JANEIRO DE 2020\nLEI Nº 2, DE 2 DE JANEIRO DE 2020')
    def test_coluna_retem(self):
        with self.assertRaisesRegex(ValueError,'linha/coluna'):self.avaliar('LEI Nº 1, DE 1 DE JANEIRO DE 2020\nTexto da   LEI Nº 2, DE 2 DE JANEIRO DE 2020')
    def test_relacao_desconhecida_retem(self):
        with self.assertRaisesRegex(ValueError,'sem relação'):self.avaliar('LEI Nº 1, DE 1 DE JANEIRO DE 2020\nTexto: LEI Nº 2, DE 2 DE JANEIRO DE 2020')
    def test_numero_sinal_literal_preservado(self):
        t='LEI Nº 1, DE 1 DE JANEIRO DE 2020\nArt. 1º O valor -100,00 e 0,5% da LEI Nº 2, DE 2 DE JANEIRO DE 2020'
        r=self.avaliar(t);self.assertIn('-100,00 e 0,5%',r[0]['contexto_literal']);self.assertIn('-100,00 e 0,5%',t)
if __name__=='__main__':unittest.main()
