import unittest
from am_legisla import itens_lista
class ListaOficialAM(unittest.TestCase):
    def setUp(self):self.source='<li class="item-li"><h5>(*) LEI N. º 8.227, DE 07 DE MAIO DE 2026</h5><p>Publicada em 07 de maio de 2026</p><a href="/diario_am/12/2026/5/19985?modo=lista">Texto integral</a></li><a rel="next" href="/diario_am/12?modo=lista&amp;page=2">Próxima</a>'
    def test_id_numero_e_paginacao_oficiais(self):
        rows,nxt=itens_lista(self.source);self.assertEqual(rows[0]['numero'],'8227');self.assertEqual(rows[0]['id_legisla'],'19985');self.assertIn('&page=2',nxt)
    def test_outra_especie_em_categoria_LO_fica_explicita(self):
        rows,_=itens_lista(self.source.replace('LEI N. º 8.227','LEI COMPLEMENTAR N.º 273'));self.assertEqual(rows[0]['tipo_indice'],'Lei Complementar');self.assertIsNone(rows[0]['numero'])
    def test_sufixo_preservado(self):self.assertEqual(itens_lista(self.source.replace('8.227','8.227-A'))[0][0]['numero'],'8227-A')
    def test_espacos_do_numero_e_ano_URL_divergente(self):
        rows,_=itens_lista(self.source.replace('8.227','7. 588').replace('2026</h5>','2025</h5>'))
        self.assertEqual(rows[0]['numero'],'7588');self.assertEqual(rows[0]['ano'],'2025');self.assertEqual(rows[0]['ano_URL'],'2026')
    def test_nao_reclassifica_outra_categoria(self):
        with self.assertRaises(ValueError):itens_lista(self.source.replace('/diario_am/12/2026','/diario_am/11/2026'))
    def test_titulo_ausente_falha_com_diagnostico(self):
        with self.assertRaises(ValueError):itens_lista(self.source.replace('<h5>','<div>').replace('</h5>','</div>'))
if __name__=='__main__':unittest.main()
