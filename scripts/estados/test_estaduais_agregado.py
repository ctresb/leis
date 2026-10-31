import unittest
from reexecutar_estaduais_agregado import conferir_diff_status,conferir_head
class ControlesAgregados(unittest.TestCase):
    def test_altera_apenas_campo_e_preserva_literal_no_corpo(self):
        old=b'---\nrevogada: false\ndata: "2026-01-01"\n---\n# Lei\n\nrevogada: false\n';new=old.replace(b'revogada: false',b'revogada: null',1);self.assertTrue(conferir_diff_status(old,new))
    def test_rejeita_corpo_data_e_booleano_indevidos(self):
        old=b'---\nrevogada: false\ndata: "2026-01-01"\n---\n# Lei\n\nArt. 1. Valor -100 e 0,5%.\n';good=old.replace(b'revogada: false',b'revogada: null',1)
        for bad in (good.replace(b'-100',b'100'),good.replace(b'0,5%',b'05%'),good.replace(b'2026-01-01',b'2025-01-01'),old):
            with self.subTest(candidate=bad):
                with self.assertRaises(ValueError):conferir_diff_status(old,bad)
    def test_HEAD_exige_exatamente_preimagens_e_ausencias(self):
        expected={'novo':None,'reparo':'a'*64};conferir_head(expected,dict(expected))
        for observed in ({'novo':None},{'novo':'b'*64,'reparo':'a'*64},{'novo':None,'reparo':'b'*64}):
            with self.assertRaises(ValueError):conferir_head(expected,observed)
if __name__=='__main__':unittest.main()
