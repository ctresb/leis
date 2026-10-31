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

class EscopoIdTest(unittest.TestCase):
 def test_marcador_final_nao_remove_DOM_de_seletor_relacional(self):
  s='<html><style>#body-law:has(.ui){display:none}</style><body><div id="body-law"><p>Art. 1º</p><span id="fim">DOE</span><div class="ui">UI</div></div></body></html>'
  q=ContextoCSS([]).conferir(s,id_campo='body-law',id_final_campo='fim');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_UI_posterior_fora_do_escopo_normativo(self):
  s='<html><body><div id="body-law"><p>Art. 1º</p><span id="fim">DOE</span><div style="display:none">UI</div></div></body></html>'
  q=ContextoCSS([]).conferir(s,id_campo='body-law',id_final_campo='fim');self.assertTrue(q['CSS_sem_risco_comprovado'])
 def test_ancestral_real_continua_examinado(self):
  s='<html><body style="opacity:0"><div id="body-law">Art. 1º<span id="fim">DOE</span></div></body></html>'
  q=ContextoCSS([]).conferir(s,id_campo='body-law',id_final_campo='fim');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_marcador_fora_do_campo_falha(self):
  with self.assertRaises(ValueError):ContextoCSS([]).conferir('<html><body><div id="body-law">Texto</div><span id="fim">DOE</span></body></html>',id_campo='body-law',id_final_campo='fim')

class FamiliasFontesTest(unittest.TestCase):
 def test_unicode_symbol_fallback_nao_e_fonte_legacy(self):
  from css_contexto_campo import riscos
  self.assertFalse(riscos('font-family','-apple-system, Arial, "Segoe UI Symbol"'))
 def test_symbol_exato_e_escapado_sao_retidos(self):
  from css_contexto_campo import riscos
  self.assertTrue(riscos('font-family','Arial, Symbol'));self.assertTrue(riscos('font-family','"S\\79mbol"'));self.assertTrue(riscos('font-family','Wingdings 2'))
 def test_import_relativo_resolvido_pela_folha(self):
  import tinycss2
  c=ContextoCSS([]);c._parse(tinycss2.parse_stylesheet('@import url("colors.css");'),'https://legis.ac.gov.br/assets/css/style.css');self.assertEqual(c.imports,['https://legis.ac.gov.br/assets/css/colors.css'])

class RecursosVisuaisCSSTest(unittest.TestCase):
 def test_imagem_de_fundo_aplicada_retem(self):
  q=ContextoCSS([]).conferir('<html><style>p{background-image:url(mapa.png)}</style><body><p>Texto</p></body></html>');self.assertFalse(q['CSS_sem_risco_comprovado'])
 def test_imagem_de_fundo_disjunta_nao_afeta_campo(self):
  q=ContextoCSS([]).conferir('<html><style>.chrome{background-image:url(mapa.png)}</style><body><p>Texto</p></body></html>');self.assertTrue(q['CSS_sem_risco_comprovado'])
 def test_fundo_plano_nao_e_imagem(self):
  from css_contexto_campo import riscos
  self.assertFalse(riscos('background','#fff'));self.assertTrue(riscos('background','linear-gradient(red,blue)'))

class PseudoestadoContextualTest(unittest.TestCase):
 def test_checkbox_indeterminado_disjunto(self):
  s='<html><style>.custom-checkbox .custom-control-input:indeterminate~.custom-control-label::after{background-image:url(check.svg)}</style><body><p>Art. 1º</p></body></html>'
  q=ContextoCSS([]).conferir(s);self.assertTrue(q['CSS_sem_risco_comprovado']);self.assertEqual(q['seletores_nao_suportados_disjuntos'],1)
 def test_checkbox_indeterminado_pode_atingir_campo(self):
  s='<html><style>.custom-checkbox .custom-control-input:indeterminate~.custom-control-label::after{background-image:url(check.svg)}</style><body><div class="custom-checkbox"><input class="custom-control-input"><label class="custom-control-label">Valor</label></div></body></html>'
  q=ContextoCSS([]).conferir(s);self.assertFalse(q['CSS_sem_risco_comprovado'])
if __name__=='__main__':unittest.main()
