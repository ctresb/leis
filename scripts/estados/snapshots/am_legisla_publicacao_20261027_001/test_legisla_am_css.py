import unittest,gzip,hashlib,tempfile
from pathlib import Path
from legisla_am_css import ContextoCSS,riscos
class CSSAM(unittest.TestCase):
 def ctx(self,css):
  d=tempfile.TemporaryDirectory();self.addCleanup(d.cleanup);p=Path(d.name)/'fonte.gz';b=css.encode();p.write_bytes(gzip.compress(b));return ContextoCSS([dict(url='https://official.example/style.css',cache=str(p),http=200,sha256_fonte=hashlib.sha256(b).hexdigest(),sha256_cache=hashlib.sha256(p.read_bytes()).hexdigest())])
 def test_heranca_e_ocultacao(self):
  c=self.ctx('.materia p {text-decoration:line-through}');self.assertFalse(c.conferir('<div class="materia"><p>Art. 1º Texto</p></div>')['CSS_sem_risco_comprovado'])
 def test_css_irrelevante_e_proxy_placeholder(self):
  c=self.ctx('.menu {display:none} .form-control::-webkit-input-placeholder {opacity:0} .materia {font-size:1rem}');p=c.conferir('<div class="materia"><p>Art. 1º Texto</p></div>');self.assertTrue(p['CSS_sem_risco_comprovado']);self.assertEqual(p['seletores_nao_suportados_disjuntos'],1)
 def test_loader_exige_handler_e_ancestral(self):
  c=self.ctx('.m-page--loading .m-page {opacity:0}');s='<body class="m-page--loading"><div class="m-page"><div class="materia">Texto</div></div></body>';self.assertFalse(c.conferir(s)['CSS_sem_risco_comprovado']);self.assertTrue(c.conferir(s+"<script>$(window).on('load', function() { $('body').removeClass('m-page--loading'); });</script>")['CSS_sem_risco_comprovado'])
 def test_CSS_inline_herdado_e_import_pendente(self):
  c=self.ctx('.materia{font-size:1rem}')
  self.assertFalse(c.conferir('<html><head><style>.materia p {text-decoration:line-through}</style></head><body><div class="materia"><p>Antigo</p></div></body></html>')['CSS_sem_risco_comprovado'])
  self.assertFalse(c.conferir('<html><head><style>@import url("https://official.example/nao-capturado.css");</style></head><body><div class="materia">Texto</div></body></html>')['CSS_sem_risco_comprovado'])
 def test_import_pendente_e_sinais(self):
  with self.assertRaises(ValueError):self.ctx('@import url("https://official.example/missing.css");')
  for n,v in [('opacity','.0'),('font-size','0px'),('text-decoration','line-through'),('content','"123"')]:self.assertTrue(riscos(n,v))
if __name__=='__main__':unittest.main()
