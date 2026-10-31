import unittest,json
from metadados_legis_ac import montar,verificar,acrescentar,ler,VERSAO
ROW=dict(capturado_em='2026-10-27T20:37:12.123456-03:00')
META=dict(titulo='Lei nº 1',tipo='Lei Ordinária',numero='1',data='2026-01-01',ementa='E',uf='AC',fonte='https://legis.ac.gov.br/detalhar/1',edicao='Detalhada',revogada=None)
def blob(meta=META):return ('---\n'+''.join(k+': '+json.dumps(v,ensure_ascii=False)+'\n' for k,v in meta.items())+'---\n').encode()+'# Lei nº 1\n\nArt. 1º R$ -100,00; 0,5%; João.\n<table><tr><td>0</td></tr></table>\r\n'.encode()
class Esquema(unittest.TestCase):
 def test_apenas_cabecalho_corpo_H1_preservado(self):
  new,p=acrescentar(blob(),ROW);meta,body=ler(new);self.assertEqual(body,ler(blob())[1]);self.assertEqual(p['chaves_adicionadas'],['baixado_em','versao_texto']);self.assertEqual(p['chaves_alteradas'],[]);self.assertEqual(meta['edicao'],'Detalhada');self.assertIsNone(meta['revogada'])
 def test_ordem_canonicamente_apos_adicao(self):
  m=montar(META,ROW);self.assertEqual(list(m)[:5],['titulo','uf','tipo','numero','data']);self.assertLess(list(m).index('versao_texto'),list(m).index('fonte'));self.assertLess(list(m).index('baixado_em'),list(m).index('edicao'));self.assertEqual(m['baixado_em'],'2026-10-27')
 def test_fuso_ausente_retem(self):
  with self.assertRaisesRegex(ValueError,'fuso'):montar(META,dict(capturado_em='2026-10-27T20:37:12'))
 def test_captura_ausente_retem(self):
  with self.assertRaisesRegex(ValueError,'ausente'):montar(META,{})
 def test_captura_UTC_cruza_dia_local(self):
  m=montar(META,dict(capturado_em='2026-10-28T01:00:00+00:00'));self.assertEqual(m['baixado_em'],'2026-10-27')
 def test_captura_local_preserva_data(self):
  m=montar(META,dict(capturado_em='2026-10-28T00:10:00-03:00'));self.assertEqual(m['baixado_em'],'2026-10-28')
 def test_idempotente(self):
  a,p=acrescentar(blob(),ROW);b,q=acrescentar(a,ROW);self.assertEqual(a,b);self.assertEqual(q['chaves_adicionadas'],[])
 def test_nao_sobrescrever_versao_divergente(self):
  with self.assertRaisesRegex(ValueError,'não substituir'):montar(dict(META,versao_texto='vigente presumida'),ROW)
 def test_nao_sobrescrever_captura_divergente(self):
  with self.assertRaisesRegex(ValueError,'não substituir'):montar(dict(META,baixado_em='2026-10-26'),ROW)
 def test_verificar_exige_campo_obrigatorio(self):
  with self.assertRaisesRegex(ValueError,'obrigatório'):verificar(META,ROW)
 def test_verificar_rejeita_ordem_trocada(self):
  m=montar(META,ROW);m=dict(reversed(list(m.items())))
  with self.assertRaisesRegex(ValueError,'ordem'):verificar(m,ROW)
 def test_todos_valores_antigos_preservados(self):
  m=montar(META,ROW)
  for k,v in META.items():self.assertEqual(m[k],v)
if __name__=='__main__':unittest.main()
