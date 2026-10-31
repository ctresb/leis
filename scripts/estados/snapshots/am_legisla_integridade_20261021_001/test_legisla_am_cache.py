import unittest,gzip,hashlib
from auditar_legisla_am_cache import identidade,auditar,dispositivo_proprio
SHA=lambda b:hashlib.sha256(b).hexdigest()
class CacheAM(unittest.TestCase):
    def test_numero_espacado_sem_truncamento(self):
        self.assertEqual(identidade('LEI N. º 7. 588, DE 18 DE JUNHO DE 2025')['numero'],'7588')
        self.assertEqual(identidade('LEI Nº 4.312 DE 11 DE MARÇO DE 2016')['numero'],'4312')
    def test_complementar_e_citacao_nao_sao_epigrafe(self):
        for s in ('LEI COMPLEMENTAR Nº 273, DE 1 DE JULHO DE 2024','Altera a LEI Nº 273, DE 1 DE JULHO DE 2024'):
            with self.assertRaises(ValueError):identidade(s)
    def row(self,title):
        b=('<main><div class="materia rounded"><p>'+title+'</p><p>FAÇO SABER que a Assembleia decretou e eu sanciono a presente LEI: Art. 1º Fica fixado -100; 0,5%; R$ 0.</p></div></main>').encode();z=gzip.compress(b)
        return dict(http=200,sha256_cache=SHA(z),sha256_fonte=SHA(b),item=dict(titulo=title,numero='604',ano='2024',id_legisla='13659',url='https://legisla.imprensaoficial.am.gov.br/diario_am/12/2024/7/13659')),z
    def test_ano_URL_nao_sobrescreve_epigrafe_e_CSS_pendente(self):
        r,z=self.row('LEI N. º 604, DE 1 DE JULHO DE 1967');q=auditar(r,z);self.assertEqual(q['data'],'1967-07-01');self.assertTrue(q['divergencia_ano_URL']);self.assertFalse(q['publicavel']);self.assertTrue(q['sinais_numericos_iguais'])
    def test_artigo_citado_em_errata_nao_basta(self):
        from auditar_legisla_am_cache import dispositivo_proprio
        with self.assertRaises(ValueError):dispositivo_proprio('LEI Nº 1. RETIFICAÇÃO. Onde se lê no Art. 1º valor100, leia-se valor200.')
        self.assertIn('Art. 1.º',dispositivo_proprio('FAÇO SABER que sanciono a presente L E I: Art. 1.º Fica instituído.'))
    def test_captura_sem_receipt_e_identidade_divergente_retidas(self):
        r,z=self.row('LEI N. º 604, DE 1 DE JULHO DE 1967');r['http']=None
        with self.assertRaises(ValueError):auditar(r,z)
        r['http']=200;r['item']['titulo']='LEI N. º 605, DE 1 DE JULHO DE 1967'
        with self.assertRaises(ValueError):auditar(r,z)
if __name__=='__main__':unittest.main()
