import unittest
from gerar_prototipo_ce import organizar,linhas
def glyph(t,x,y):return dict(text=t,x0=x,top=y,matrix=(1,0,0,1,x,793-y))
class Flow(unittest.TestCase):
    def test_colunas_notas_rodape_sem_perda(self):
        chars=[glyph('F',80,747),glyph('A',80,50),glyph('n',295,690),glyph('B',330,50)]
        zones,profile=organizar(chars,26)
        self.assertTrue(profile['apto_perfil']);self.assertEqual([i for zone,ids in zones for i in ids],[1,3,2,0])
        self.assertEqual(sorted(i for zone,ids in zones for i in ids),list(range(4)))
    def test_texto_largo_nao_inferido_como_nota(self):
        with self.assertRaises(ValueError):organizar([glyph('A',295,200)],26)
    def test_apendice_sem_perfil_preserva_tudo(self):
        zones,profile=organizar([glyph('A',400,300),glyph('B',100,20)],195)
        self.assertFalse(profile['apto_perfil']);self.assertEqual(zones,[('sem_perfil',[0,1])])
    def test_numeros_sinais_e_pontuacao_preservados(self):
        chars=[glyph(c,80+i,50) for i,c in enumerate('R$ -100,00; 0,5%')]
        self.assertEqual(linhas(chars,list(range(len(chars)))),'R$ -100,00; 0,5%')
    def test_matriz_shear_requer_novo_perfil(self):
        c=glyph('A',80,50);c['matrix']=(1,.1,0,1,80,743)
        with self.assertRaises(ValueError):organizar([c],26)
if __name__=='__main__':unittest.main()
