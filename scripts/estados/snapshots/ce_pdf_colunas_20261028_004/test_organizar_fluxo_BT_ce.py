import unittest
from organizar_fluxo_BT_ce import marcadores,fluxo
def glyph(i,text,x,y,size=8,font='Fonte+AsapCondensed-Light'):
    return dict(id=i,texto=text,bbox=[x,y,x+5,y+size],matriz=[1,0,0,1,x,793.701-y],fonte=font,tamanho=size,cor=[0,0,0,1])
class Notes(unittest.TestCase):
    def test_numero_observado_sem_renumeracao(self):
        g=[glyph(0,'0',56.6929,700),glyph(1,'1',61.6929,700)]
        m=marcadores(g);self.assertEqual(m[0]['impresso'],'01');self.assertEqual(m[0]['ids'],[0,1])
    def test_texto_apenas_numerico_nao_basta(self):
        for g in [glyph(0,'1',100,700),glyph(0,'1',56.6929,100),glyph(0,'1',56.6929,700,10),glyph(0,'1',56.6929,700,8,'FonteRegular')]:self.assertEqual(marcadores([g]),[])
    def test_nota_curta_que_nao_cruza_gutter(self):
        g=[glyph(0,'L',80,50,10),glyph(1,'1',56.6929,700),glyph(2,' ',62,700),glyph(3,'nota',74.6929,700),glyph(4,'R',320,50,10),glyph(5,'F',100,747)]
        zones,p,m=fluxo(dict(pagina=26,glifos=g),[])
        self.assertIsNone(p['limite_anterior_gutter']);self.assertEqual(dict(zones)['notas_largura_total'],[1,2,3]);self.assertEqual([i for z,ids in zones for i in ids],[0,4,1,2,3,5])
    def test_continuacao_52_e_marcador_53(self):
        g=[glyph(0,'L',80,50,10),glyph(1,'lei”',56.6929,650),glyph(2,'continua',320,650),glyph(3,'53',56.6929,675),glyph(4,'nota',74.6929,675),glyph(5,'R',320,50,10)]
        bt=[dict(BT=17,bbox=[56.6929,650,438,683],ids=[1,2,3,4])]
        zones,p,m=fluxo(dict(pagina=73,glifos=g),bt)
        self.assertTrue(p['continuacao_52_paginas_72_73']);self.assertEqual(p['limite_notas_proposto'],647);self.assertEqual(dict(zones)['notas_largura_total'],[1,2,3,4])
    def test_nao_absorver_tipografia_do_dispositivo(self):
        g=[glyph(0,'L',80,50,10),glyph(1,'1',56.6929,700),glyph(2,'Artigo',320,705,10)]
        with self.assertRaisesRegex(ValueError,'tipografia'):fluxo(dict(pagina=26,glifos=g),[])
    def test_nota_continua_noutra_pagina_exige_prova(self):
        g=[glyph(0,'L',80,50,10),glyph(1,'nota',56.6929,650),glyph(2,'longa',320,650)]
        with self.assertRaisesRegex(ValueError,'continuação'):fluxo(dict(pagina=74,glifos=g),[dict(BT=1,bbox=[56.6929,650,438,658],ids=[1,2])])
if __name__=='__main__':unittest.main()
