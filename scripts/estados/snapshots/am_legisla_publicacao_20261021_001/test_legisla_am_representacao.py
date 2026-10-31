import unittest
from representacao_html_legisla_am import extrair_campo,representar,MODO
class LegislaHTML(unittest.TestCase):
    def test_limite_nao_inclui_navegacao_ou_rodape(self):
        s='<div>Menu</div><div class="materia rounded"><div><p>Lei</p></div></div><footer>Outro ato</footer>';f,(a,b)=extrair_campo(s);self.assertEqual(f,s[a:b]);self.assertNotIn('Outro ato',f)
    def test_semantica_sinais_atributos_e_linhas(self):
        s='<div class="materia rounded"><p style="margin:1rem">-100; 0,5%; R$ 0\n\n---\n*literal*</p><table><tr><td rowspan="2">0</td></tr><tr><td>10,00</td></tr></table></div>';out=representar(s,modo=MODO);self.assertIn('&#10;',out);self.assertIn('rowspan="2"',out);self.assertIn('-100; 0,5%; R$ 0',out);self.assertEqual(representar(out,modo=MODO),out)
    def test_tachado_oculto_visual_ativo_rejeitados(self):
        for t in ('<s>Antigo</s>','<p style="display:none">Antigo</p>','<img src="tabela.png">','<script>ativo</script>','<p class="MsoNormal">classe não contextualizada</p>'):
            with self.subTest(t=t):
                with self.assertRaises(ValueError):representar('<div class="materia rounded">'+t+'</div>',modo=MODO)
    def test_modo_e_campo_duplicado_falham(self):
        with self.assertRaises(ValueError):representar('<div class="materia rounded">Lei</div>',modo='desconhecido')
        with self.assertRaises(ValueError):extrair_campo('<div class="materia">a</div><div class="materia">b</div>')
if __name__=='__main__':unittest.main()
