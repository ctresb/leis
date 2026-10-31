import unittest
from css_contexto_campo import ContextoCSS
class CSSTest(unittest.TestCase):
 def test_tachado_herdado(self):
  q=ContextoCSS([]).conferir('<html><head><style>.old {text-decoration:line-through}</style></head><body class="old"><p>Art. 1º</p></body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_regra_disjunta(self):
  q=ContextoCSS([]).conferir('<html><style>.old{display:none}</style><body><p>Art. 1º</p></body></html>');self.assertTrue(q['CSS_sem_risco_comprovado'])
 def test_campo_classe_ancestral(self):
  q=ContextoCSS([]).conferir('<html><body style="opacity:0"><div class="norma">Art. 1º</div></body></html>',classe_campo='norma');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_import_nao_capturado(self):
  q=ContextoCSS([]).conferir('<html><head><style>@import url("a.css");</style></head><body>Art. 1º</body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_pseudo_conteudo(self):
  q=ContextoCSS([]).conferir('<html><style>p:before{content:"1."}</style><body><p>Texto</p></body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_sem_excecao_am_loader(self):
  q=ContextoCSS([]).conferir('<html><style>.m-page{opacity:0}</style><body class="m-page">Texto</body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])

class SeletorSemRiscoTest(unittest.TestCase):
 def test_seletor_nao_suportado_propriedades_neutras(self):
  q=ContextoCSS([]).conferir('<html><style>span.05Artigo{font-family:Verdana;font-size:13pt}</style><body>Art. 1º</body></html>');self.assertTrue(q['CSS_sem_risco_comprovado']);self.assertTrue(q['seletores_nao_suportados_sem_risco_nas_propriedades_examinadas'])
 def test_seletor_nao_suportado_risco_retido(self):
  q=ContextoCSS([]).conferir('<html><style>span.05Artigo{display:none}</style><body>Art. 1º</body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])

class MSOHideTest(unittest.TestCase):
 def test_hide_mso_herdado_retido(self):
  q=ContextoCSS([]).conferir('<html><style>.oculto{mso-hide:all}</style><body class="oculto">Texto</body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])

class SpanBrancoVazioTest(unittest.TestCase):
 def test_nbsp_folha_literal_e_comprovado(self):
  q=ContextoCSS([]).conferir('<html><body><span style="color:white">&#160;</span></body></html>');self.assertTrue(q['CSS_sem_risco_comprovado']);self.assertEqual(q['spans_brancos_vazios_comprovados'][0]['texto_literal'],'\xa0')
 def test_texto_branco_permanece_retido(self):
  q=ContextoCSS([]).conferir('<html><body><span style="color:white">Art. 1º</span></body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_filho_visual_permanece_retido(self):
  q=ContextoCSS([]).conferir('<html><body><span style="color:white"><img src="tabela.png"></span></body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_pseudo_gerado_permanece_retido(self):
  q=ContextoCSS([]).conferir('<html><style>span:before{content:"100"}</style><body><span style="color:white">&#160;</span></body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])
if __name__=='__main__':unittest.main()
