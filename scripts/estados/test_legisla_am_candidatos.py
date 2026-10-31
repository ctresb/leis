import unittest
from am_legisla_candidatos import revisar,compor
class Candidatos(unittest.TestCase):
 def test_revisao_sha_e_retencoes_exatas(self):
  qa=dict(retencoes=['citação']);r=dict(sha256_fonte='abc',resultado='contexto_completo_com_citacao_ou_tabela_propria',retencoes_automaticas_revisadas=['citação'])
  self.assertEqual(revisar(qa,r,'abc')[0],[])
  with self.assertRaises(ValueError):revisar(qa,r,'def')
  with self.assertRaises(ValueError):revisar(dict(retencoes=['anexo ausente']),r,'abc')
 def test_prova_citacao_nao_dispensa_anexo(self):
  foreign='outra epígrafe completa exige revisão de granularidade/citação';r=dict(sha256_fonte='abc',resultado='contexto_completo_com_citacao_ou_tabela_propria',retencoes_automaticas_revisadas=[foreign]);self.assertEqual(revisar(dict(retencoes=[],citacoes=dict(todas_contextualizadas=True)),r,'abc')[0],[])
  r['retencoes_automaticas_revisadas']=['anexo ausente']
  with self.assertRaises(ValueError):revisar(dict(retencoes=[],citacoes=dict(todas_contextualizadas=True)),r,'abc')
 def test_revisao_ausencia_nao_libera(self):
  r=dict(sha256_fonte='abc',resultado='reter_ausencia_confirmada_no_campo');self.assertEqual(revisar(dict(retencoes=['anexo']),r,'abc')[0],['anexo'])
 def test_composicao_nao_inventa_vigencia_ano_URL_ou_corpo(self):
  r=dict(item=dict(titulo='LEI Nº 604 DE 1 DE JULHO DE 1967',id_legisla='13659',url='https://legisla.imprensaoficial.am.gov.br/diario_am/12/2024/7/13659',numero='604',ano='2024'),capturado_em='2026-10-21T01:00:00-03:00',sha256_fonte='abc');q=dict(tipo='Lei Ordinária',numero='604',data='1967-07-01',sha256_campo='def');field='<div class="materia rounded"><p>Art. 1º -100; 0,5%; R$ 0.</p></div>';raw,meta=compor(r,q,field);self.assertIsNone(meta['revogada']);self.assertEqual(meta['ano'],'1967');self.assertEqual(meta['ano_URL'],'2024');self.assertIn(field.encode(),raw)
if __name__=='__main__':unittest.main()
