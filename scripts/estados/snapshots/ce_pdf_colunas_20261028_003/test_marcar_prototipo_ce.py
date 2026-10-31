import unittest
from gerar_prototipo_ce import nova_linha
from marcar_prototipo_ce import representar,selecionar,rgb
class Physical(unittest.TestCase):
    def glyph(self,i,text,x,top):return dict(id=i,texto=text,bbox=[x,top,x+5,top+10],matriz=[1,0,0,1,x,793-top],fonte='FonteRegular',tamanho=10,cor=[0,0,0,1])
    def test_sobrescrito_nao_cria_quebra(self):
        self.assertFalse(nova_linha(100,10,104,6));self.assertTrue(nova_linha(100,10,86,10))
    def test_subtexto_fisico_e_sem_normalizacao(self):
        page=dict(pagina=26,glifos=[self.glyph(i,c,i*5,10) for i,c in enumerate('-0,5%')]);band=dict(caixa=[0,15,15,15],cor=[0,0,0,1]);selected,profiles,proof=selecionar(page,[band]);self.assertEqual(selected,{0,1,2});self.assertEqual(''.join(page['glifos'][i]['texto'] for i in sorted(selected)),'-0,')
    def test_escapar_html_e_preservar_todos_glifos(self):
        page=dict(pagina=26,glifos=[self.glyph(i,c,i*5,10) for i,c in enumerate('<&>')],zonas=[dict(nome='coluna_esquerda',ids=[0,1,2])]);markup,record=representar(page,{1});self.assertIn('&lt;',markup);self.assertIn('&amp;',markup);self.assertIn('<del>',markup);self.assertEqual(''.join(g['texto'] for g in record),'<&>')
    def test_glifo_duplicado_falha(self):
        page=dict(pagina=26,glifos=[self.glyph(0,'A',10,10)],zonas=[dict(nome='x',ids=[0,0])]);
        with self.assertRaises(ValueError):representar(page,set())
    def test_CMYK_aproximacao_explicita_e_cor_invalida(self):
        self.assertEqual(rgb([0,0,0,1]),'#000000');self.assertEqual(rgb([0,1,1,0]),'#ff0000')
        with self.assertRaises(ValueError):rgb([2,0,0,0])
if __name__=='__main__':unittest.main()
