import unittest
from contexto_to_pdf import primeira_epigrafe,granularidade,anotacoes,documentos
BASE='LEI Nº 123, DE 1 DE JANEIRO DE 2020.\nFaço saber que a Assembleia decreta e eu sanciono a seguinte Lei:\nArt. 1º Norma própria.\n'
class Contexto(unittest.TestCase):
 def test_epigrafe_inicial(self):self.assertTrue(primeira_epigrafe('  \n'+BASE,3))
 def test_marcador_editorial_preservado(self):self.assertTrue(primeira_epigrafe('*'+BASE,1))
 def test_projeto_nao_e_epigrafe_legal(self):
  with self.assertRaisesRegex(ValueError,'projeto'):primeira_epigrafe('PROJETO DE '+BASE,11)
 def test_citacao_nao_substitui_epigrafe_malformada(self):
  prefix='LEI Nº I.258, DE 1 DE JANEIRO DE 2020.\nAltera a '
  with self.assertRaises(ValueError):primeira_epigrafe(prefix+BASE,len(prefix))
 def test_sem_numero_ordinal_na_segunda_lei(self):
  with self.assertRaisesRegex(ValueError,'secundária'):granularidade(BASE+'\nLEI 124, DE 1 DE JANEIRO DE 2020.\n','Lei Ordinária','123','2020-01-01',['fecho'])
 def test_portaria_titlecase_segunda_coluna(self):
  with self.assertRaisesRegex(ValueError,'outro ato'):granularidade(BASE+'Art. 2º fim.       Portaria nº 3, de 2020.\n','Lei Ordinária','123','2020-01-01',['fecho'])
 def test_duas_promulgacoes_retem(self):
  with self.assertRaisesRegex(ValueError,'promulgação'):granularidade(BASE+BASE,'Lei Ordinária','123','2020-01-01',['fecho'])
 def test_dois_fechos_mesma_data_retem(self):
  with self.assertRaisesRegex(ValueError,'fecho'):granularidade(BASE,'Lei Ordinária','123','2020-01-01',['fecho','fecho'])
 def test_projeto_no_assunto_nao_e_projeto_do_documento(self):self.assertTrue(granularidade(BASE+'Art. 2º Prazos para o Projeto de Lei Orçamentária.','Lei Ordinária','123','2020-01-01',['fecho']))
 def test_notas_fora_parenteses(self):
  for s in ['Revogada pela Lei nº 1471.','*§2º com redação determinada pela Lei nº 1183.','*Declarada Inconstitucional através da ADI.','*Art. 2º-A acrescentado pela Lei Complementar nº 82.']:self.assertTrue(anotacoes(s))
 def test_documento_aprovado_quebra_linha(self):self.assertTrue(documentos('Art.1º Fica aprovado o\nCódigo de Obras.'))
 def test_plural_programas_ratificados(self):self.assertTrue(documentos('Ficam ratificados os\nProgramas Institucionais.'))
 def test_aprovacao_da_propria_lei_no_preambulo(self):self.assertFalse(documentos('Faço saber que a Assembleia aprova e eu sanciono a seguinte Lei: Art.1º Política de ocupação do solo.'))
 def test_licenca_futura_nao_aprova_documento_anexo(self):self.assertFalse(documentos('A localização será aprovada pelo NATURATINS ou mediante convênio, por órgão municipal.'))
 def test_sistema_homologado_nao_homologa_convenio(self):self.assertFalse(documentos('Sistema de gestão ambiental, homologados pelo COEMA e na conformidade de convênio ou instrumento de cooperação.'))
if __name__=='__main__':unittest.main()
