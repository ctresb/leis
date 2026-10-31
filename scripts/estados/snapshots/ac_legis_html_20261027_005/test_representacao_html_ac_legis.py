import unittest
from representacao_html_ac_legis import extrair_campo,representar,MODO
from auditar_spl_html_recente import comparar
FOOT='<span id="texto_publicado_doe">Este texto não substitui o publicado no DOE de 10/09/2026.</span>'
UI='<div style="display:none" class="row"><div><table><thead><tr><th>NOME DO ARQUIVO</th><th>LINK PARA DOWNLOAD</th></tr></thead><tbody></tbody></table></div></div>'
def page(body='Art. 1º Texto.',after=UI):return '<html><body><div id="body-law"><p>'+body+'</p>'+FOOT+'<p>\xa0</p>'+after+'</div></body></html>'
class CampoACTest(unittest.TestCase):
 def test_UI_vazia_e_escopo_explicito(self):
  field,q=extrair_campo(page());self.assertNotIn('NOME DO ARQUIVO',field);self.assertTrue(q['posterior_nao_normativo_comprovado'])
 def test_anexo_apos_rodape_nao_e_descartado(self):
  with self.assertRaisesRegex(ValueError,'material/anexo'):extrair_campo(page(after='<p>ANEXO I: Valores</p>'))
 def test_download_nao_vazio_retem(self):
  with self.assertRaisesRegex(ValueError,'material/anexo'):extrair_campo(page(after=UI.replace('<tbody></tbody>','<tbody><tr><td><a href="anexo.pdf">Anexo</a></td></tr></tbody>')))
 def test_rodape_repetido_retem(self):
  with self.assertRaisesRegex(ValueError,'único'):extrair_campo(page(after=FOOT))
 def test_fragmento_preserva_sinais_CRLF_e_atributos(self):
  source=page(body='R$ 0,5 -100 10%\r\nTexto.');fragment,_=extrair_campo(source);out=representar(fragment,modo=MODO);self.assertNotIn('\r',out);self.assertIn('id="body-law"',out);self.assertTrue(comparar(fragment,out)['sha256_visivel_fonte'])
 def test_ativo_retem(self):
  fragment,_=extrair_campo(page(body='<script>alert(1)</script>Art. 1º'))
  with self.assertRaises(ValueError):representar(fragment,modo=MODO)
 def test_modo_desconhecido_retem(self):
  with self.assertRaises(ValueError):representar('<div>Texto</div>',modo='outro')
if __name__=='__main__':unittest.main()
