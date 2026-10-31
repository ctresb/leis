from pathlib import Path
import sys, unittest
from types import SimpleNamespace
sys.path.insert(0,str(Path(__file__).resolve().parent))
from integridade_anexos_decreto import anexo_proprio_ausente as gate

P=SimpleNamespace(visual=[],structure=[])
MAIN='DECRETO Nº 52.677\n\nArtigo único. Fica aprovado o Regimento que com êste baixa.\n\nBrasília, 14 de outubro de 1963; 142º da Independência.\n\nJOÃO GOULART\n\nPaulo de Tarso'
class Anexos(unittest.TestCase):
 def test_somente_assinaturas_ou_nota_retem(self):
  self.assertIsNotNone(gate(MAIN,P))
  self.assertIsNotNone(gate(MAIN+'\n\nO Regimento foi publicado no Diário Oficial de 17 de outubro.',P))
 def test_regimento_presente_nao_retem(self):
  self.assertIsNone(gate(MAIN+'\n\nREGIMENTO DA FACULDADE\n\nArt. 1º A Faculdade...',P))
 def test_citacao_de_outro_decreto_nao_retem(self):
  self.assertIsNone(gate(MAIN.replace('que com êste baixa','anexo ao Decreto nº 1.234 de 1960'),P))
 def test_link_tabela_ou_visual_exige_outra_analise(self):
  self.assertIsNotNone(gate(MAIN+'\n\n[Regimento](https://official/anexo)',P))
  self.assertIsNotNone(gate(MAIN+'\n\n<a href="anexo.pdf">ANEXO</a>',P))
  self.assertIsNotNone(gate(MAIN+'\n\nANEXO',P))
  self.assertIsNone(gate(MAIN+'\n\n[ANEXO](#anexo)\n\nANEXO\n\nArt. 1º Ficam fixados os valores.',P))
  self.assertIsNone(gate(MAIN,SimpleNamespace(visual=[],structure=[('table',())])))
  self.assertIsNone(gate(MAIN,SimpleNamespace(visual=['img'],structure=[])))
 def test_placeholder_escapado_nao_e_conteudo(self):
  for label in ['&lt;&lt;ANEXO&gt;&gt;', '&amp;lt;&amp;lt;ANEXO&amp;gt;&amp;gt;', '«ANEXO»', 'TABELAS.', 'ANEXO I', r'\\\Final do documento.']:
   self.assertIsNotNone(gate(MAIN+'\n\n'+label,P),label)
 def test_aprovacao_na_forma_dos_anexos_retem(self):
  self.assertIsNotNone(gate(MAIN.replace('o Regimento que com êste baixa','o Quadro de Pessoal, na forma dos anexos'),P))
 def test_documento_aprovado_sem_palavra_anexo_exige_revisao(self):
  text=MAIN.replace('o Regimento que com êste baixa','o Manual de Procedimentos do Órgão')
  self.assertEqual(gate(text,P)['estado'],'revisao_documental_necessaria')
 def test_objeto_inline_sem_suplemento_nao_retem(self):
  text=MAIN.replace('o Regimento que com êste baixa','a lotação numérica na forma seguinte:\n\n1 - Oficial de Administração\n\n2 - Escriturários')
  self.assertIsNone(gate(text,P))
 def test_alteracao_atomizada_nao_exige_estatuto_inteiro(self):
  text=MAIN.replace('o Regimento que com êste baixa','a alteração do art. 8º do Estatuto, que passa a ter a seguinte redação:\n\nArt. 8º O capital social é de cem unidades')
  self.assertIsNone(gate(text,P))
 def test_regulamento_antes_do_ultimo_fecho_nao_e_rotulo(self):
  text=MAIN.replace('Brasília, 14','Brasília (DF), 14')+'\n\nREGIMENTO\n\nArt. 1º A Faculdade terá cursos.\n\nArt. 2º Os cursos são gratuitos.\n\nBrasília, 14 de outubro de 1963.\n\nMinistro da Educação'
  self.assertIsNone(gate(text,P))
 def test_aprovacao_futura_nao_e_documento_aprovado_agora(self):
  text=MAIN.replace('Fica aprovado o Regimento que com êste baixa','O Diretor exercerá a competência até que seja instalado o Conselho e aprovado o respectivo Regimento')
  self.assertIsNone(gate(text,P))
 def test_relacao_prometida_substituida_por_pontilhado(self):
  text=MAIN.replace('o Regimento que com êste baixa','o enquadramento dos professores, abrangendo os ocupantes a seguir mencionados, a saber:\n\n..........................................\n\nParágrafo único. Permanecem nas cadeiras')
  self.assertIn('pontilhado',gate(text,P)['motivo'])
 def test_relacao_nominal_reproduzida_nao_retem(self):
  text=MAIN.replace('o Regimento que com êste baixa','o enquadramento dos professores, abrangendo os ocupantes a seguir mencionados, a saber:\n\n1. José da Silva - Química\n\n2. Maria dos Santos - Física')
  self.assertIsNone(gate(text,P))
 def test_tabela_depois_da_aprovacao_pode_ser_objeto(self):
  text=MAIN.replace('o Regimento que com êste baixa','a tabela na forma do anexo\n\n<table><tr><td>Valor</td><td>10</td></tr></table>')
  self.assertIsNone(gate(text,SimpleNamespace(visual=[],structure=[('table',())])))
 def test_tabela_anterior_nao_prova_suplemento_posterior(self):
  text='<table><tr><td>Dado anterior</td></tr></table>\n\n'+MAIN
  self.assertIsNotNone(gate(text,SimpleNamespace(visual=[],structure=[('table',())])))
 def test_rotulos_sem_dados_e_nota_de_publicacao_nao_sao_objeto(self):
  text=MAIN+'\n\nQUADRO DE PESSOAL - PARTE PERMANENTE\n\nCONSELHO NACIONAL DE SERVIÇO SOCIAL\n\nSECRETARIA EXECUTIVA\n\n&lt;&lt;TABELA&gt;&gt;\n\nO anexo foi publicado no D.O. de 4-8-72.'
  self.assertIsNotNone(gate(text,P))
 def test_aprovacao_posterior_e_formas_de_anexo(self):
  for obj in ['o anexo Estatuto da Companhia', 'a tabela em anexo', 'as relações nominais anexas', 'o Regimento, de acordo com o texto anexo']:
   text=MAIN.replace('Artigo único. Fica aprovado o Regimento que com êste baixa','Art. 1º Fica aprovado o valor de dez unidades.\n\nArt. 2º Fica aprovado '+obj)
   self.assertIsNotNone(gate(text,P),obj)
 def test_corpo_curto_de_regimento_sem_artigos_e_conteudo(self):
  self.assertIsNone(gate(MAIN+'\n\nREGIMENTO\n\nA Faculdade terá cursos gratuitos.',P))
 def test_inicial_de_assinatura_nao_e_artigo_gramatical(self):
  self.assertIsNotNone(gate(MAIN.replace('JOÃO GOULART','A. COSTA E SILVA'),P))
 def test_eleicao_depois_de_aprovacao_futura_nao_retem(self):
  text=MAIN.replace('Artigo único. Fica aprovado o Regimento que com êste baixa','Art. 2º A eleição se realizará quinze dias depois e aprovado o novo Regimento do HSE')
  self.assertIsNone(gate(text,P))
 def test_modelo_substituido_com_placeholder_nao_e_integral(self):
  text=MAIN.replace('Fica aprovado o Regimento que com êste baixa',
                    'Fica substituída pelo modêlo anexo denominado Guia de Embarque a atual Guia de Exportação')
  for label in ['<<Anexo>>', '&lt;&lt;Anexo&gt;&gt;', '&lt;&lt;Anexo>>']:
   result=gate(text+'\n\n'+label,P)
   self.assertIsNotNone(result,label)
   self.assertEqual(result['estado'],'ausencia_na_transcricao')
 def test_modelo_de_outra_norma_nao_e_objeto_proprio(self):
  text=MAIN.replace('Fica aprovado o Regimento que com êste baixa',
                    'A repartição utilizará o modelo anexo ao Decreto nº 1.234 de 1960')
  self.assertIsNone(gate(text+'\n\n<<Anexo>>',P))
 def test_modelo_substituido_efetivamente_reproduzido(self):
  text=MAIN.replace('Fica aprovado o Regimento que com êste baixa',
                    'Fica substituída pelo modelo anexo denominado Guia de Embarque a atual Guia')
  self.assertIsNone(gate(text+'\n\nANEXO\n\nGUIA DE EMBARQUE\n\nNome do exportador: ______ Endereço: ______ Quantidade: ______',P))
 def test_anexo_bibliografico_sem_fecho_nao_e_conteudo(self):
  text='DECRETO Nº 34.126\n\nArt. 1º Fica aprovada, na forma da relação anexa, a Tabela Numérica Especial.\n\nArt. 2º Este Decreto entra em vigor na data de sua publicação.'
  for label in ['<<ANEXO>> CLBR Vol. 08 Ano 1953 Pág. 250 Tabela.', '&lt;&lt;ANEXO>>CLBR Vol. 08 Ano 1953 Pág. 250 Tabela.', '&amp;lt;&amp;lt;ANEXO&amp;gt;&amp;gt;']:
   self.assertEqual(gate(text+'\n\n'+label,P)['estado'],'ausencia_na_transcricao')
 def test_anexo_externo_sem_fecho_nao_retem(self):
  text='Art. 1º Fica aprovada a utilização da relação anexa ao Decreto nº 10, de 1950.\n\n<<ANEXO>> CLBR Vol. 08 Ano 1953 Pág. 250 Tabela.'
  self.assertIsNone(gate(text,P))
 def test_tabela_reproduzida_sem_fecho_nao_retem(self):
  text='Art. 1º Fica aprovada a tabela anexa.\n\n<table><tr><td>Cargo</td><td>10</td></tr></table>\n\n<<ANEXO>>'
  self.assertIsNone(gate(text,SimpleNamespace(visual=[],structure=[('table',())])))
 def test_relacao_nominal_alterada_sem_formula_de_aprovacao(self):
  article='Art. 1º Fica alterada, na forma da relação anexa, a Tabela Única de Extranumerários-Mensalistas do Ministério da Aeronáutica.\n\nArt. 2º Este Decreto entra em vigor na data de sua publicação.'
  for fecho in ['', '\n\nRio de Janeiro. em 19 de dezembro de 1950; 129º da Independência.\n\nEurico G. Dutra']:
   text=article+fecho+'\n\n&lt;&lt;ANEXO>>CLBR Vol. 08 Ano 1950 Págs. 389 a 392 Tabelas.'
   self.assertEqual(gate(text,P)['estado'],'ausencia_na_transcricao')
 def test_relacao_nominal_de_outra_norma_nao_e_objeto_proprio(self):
  text='Art. 1º Fica alterada, na forma da relação anexa ao Decreto nº 10, de 1950, a tabela de cargos.\n\n<<ANEXO>>'
  self.assertIsNone(gate(text,P))
 def test_relacao_nominal_efetivamente_representada(self):
  text='Art. 1º Fica alterada, na forma da relação anexa, a Tabela Única de Extranumerários-Mensalistas do Ministério da Aeronáutica.\n\n<table><tr><td>Nome</td><td>Cargo</td></tr><tr><td>João</td><td>Professor</td></tr></table>\n\n<<ANEXO>>'
  self.assertIsNone(gate(text,SimpleNamespace(visual=[],structure=[('table',())])))
  self.assertIsNone(gate(text.split('<table>')[0]+'<<ANEXO>>\n\nNome: João. Cargo: Professor.',P))
 def test_modelos_graficos_apos_regulamento_e_tabelas_exigem_revisao(self):
  text=MAIN.replace('o Regimento que com êste baixa','o novo Regulamento que com êste baixa')+'\n\nREGULAMENTO\n\nArt. 1º Os estabelecimentos são regulados.\n\n<table><tr><td>Outro dado</td></tr></table>\n\nArt. 832. Os carimbos devem obedecer à descrição e aos modelos anexos.\n\n<<ANEXO>>CLBR Vol. 06 Ano 1952 Págs. 486 a 492 Carimbos.'
  self.assertEqual(gate(text,SimpleNamespace(visual=[],structure=[('table',())]))['estado'],'revisao_documental_necessaria')
 def test_figuras_do_proprio_regulamento_exigem_revisao(self):
  text=MAIN+'\n\nREGIMENTO\n\nArt. 1º Os uniformes obedecem às figuras anexas.\n\n&lt;&lt;ANEXO>>CLBR Vol. 08 Ano 1951 Págs. 117 a 140 Figuras.'
  self.assertIsNotNone(gate(text,P))
 def test_figuras_com_representacao_ou_regulamento_externo(self):
  text=MAIN+'\n\n<<ANEXO>>CLBR Vol. 08 Ano 1951 Págs. 117 a 140 Figuras.'
  self.assertIsNone(gate(text,SimpleNamespace(visual=['img'],structure=[])))
  external=text.replace('que com êste baixa','anexo ao Decreto nº 1.234 de 1960')
  self.assertIsNone(gate(external,P))
 def test_anexo_numerado_deste_decreto_sem_representacao(self):
  text=MAIN.replace('Fica aprovado o Regimento que com êste baixa','Ficam extintas as funções constantes do Anexo I dêste decreto')
  self.assertEqual(gate(text,P)['estado'],'ausencia_na_transcricao')
 def test_anexos_numerados_reproduzidos_nao_retem(self):
  text=MAIN.replace('Fica aprovado o Regimento que com êste baixa','Ficam extintas as funções constantes dos Anexos I e II dêste decreto')+'\n\nANEXO I\n\n<table><tr><td>Função</td><td>Professor</td></tr></table>\n\nANEXO II\n\n<table><tr><td>Função</td><td>Secretário</td></tr></table>'
  self.assertIsNone(gate(text,SimpleNamespace(visual=[],structure=[('table',())])))
 def test_anexo_numerado_do_decreto_externo_nao_retem(self):
  text=MAIN.replace('Fica aprovado o Regimento que com êste baixa','Ficam extintas as funções constantes do Anexo I do Decreto nº 1.234 de 1960')
  self.assertIsNone(gate(text,P))
class LacunasGraficasEEditoriais(unittest.TestCase):
 def test_parte_rasgada_no_dispositivo_retem(self):
  self.assertEqual(gate('Art. 2º As subcomissões prestarão seu concurso (**Ilegível** parte rasgada no livro.).',P)['estado'],'revisao_documental_necessaria')
 def test_lacunas_nomes_objeto_e_alinea_retem(self):
  for text in ['Art. 1º Vagos em virtude da aposentadoria de Francisco, (ilegível) Marcos Pinheiro.', 'Art. 3º XVI – Recuperação e consertos de peças e móveis (ilegivel).', 'Art. 4º Candidatos sem observância do nº(ilegível).', 'Art. 6º Diploma a que se refere a alínea (ilegivel) do art. 23.']:
   self.assertIsNotNone(gate(text,P),text)
 def test_ilegivel_legitimo_no_servico_postal_nao_retem(self):
  self.assertIsNone(gate('Art. 1º Não será aceita remessa que traga ilegível o nome do destinatário.',P))
 def test_ilegivel_legitimo_no_cancelamento_nao_retem(self):
  self.assertIsNone(gate('Art. 1º A nota é riscada em cruz sem a tornar ilegível; quando a praça fôr desligada, a nota será tornada ilegível.',P))
 def test_definicao_explicita_de_rotulo_nao_retem(self):
  self.assertIsNone(gate('Art. 1º Usar a expressão (ilegível) para classificar documentos sem leitura possível.',P))
 def test_desenhos_medalha_propria_com_placeholder_retem(self):
  text='Art. 1º A Medalha tem as seguintes características, elucidadas nos desenhos anexos.\n\nRio de Janeiro, 22 de outubro de 1947.\n\nAssinatura\n\n&lt;&lt;ANEXO>> CLBR Vol. 08 Ano 1947 Pág. 91 Desenhos.'
  self.assertIn('desenhos anexos',gate(text,P)['remissao'])
 def test_formulario_de_proposta_nao_prova_desenhos_insignias(self):
  text=MAIN+'\n\nREGULAMENTO\n\nArt. 1º A Ordem possui cinco graus.\n\nArt. 3º As insígnias terão as dimensões e características consignadas nas explicações e desenhos anexos.\n\nArt. 29. As propostas seguirão o anexo.\n\nANEXO\n\nNome do candidato ....\n\nGrau ....'
  self.assertIn('art. 3',gate(text,P)['remissao'])
 def test_descricao_uniforme_sem_desenhos_retem(self):
  self.assertIsNotNone(gate('Art. 13. Para a distinção de categorias, serão colocados na gola do uniforme bordados dourados de acordo com os desenhos anexos.',P))
 def test_desenhos_de_norma_externa_nao_retem(self):
  self.assertIsNone(gate('Art. 1º A medalha obedecerá às características dos desenhos anexos ao Decreto nº 123 de 1930.',P))
 def test_alteracao_citada_sem_novo_desenho_nao_retem(self):
  self.assertIsNone(gate('Art. 1º O art. 3º do Decreto nº 123 passa a vigorar com a seguinte redação: As insígnias obedecem às características dos desenhos anexos.',P))
 def test_visual_presente_nao_e_declarado_ausente(self):
  self.assertIsNone(gate('Art. 3º As insígnias terão as dimensões consignadas nos desenhos anexos.',SimpleNamespace(visual=['svg'],structure=[])))

class RegulamentosFuturos(unittest.TestCase):
 def test_desenhos_da_regulamentacao_a_ser_baixada_nao_retem(self):
  for text in ['Art. 2º A Ordem constará de quatro graus, cujas insígnias obedecerão a desenhos anexos à regulamentação a ser baixada pelo Ministro.', 'Art. 2º As insígnias da Ordem obedecerão a desenhos anexos ao regulamento a ser baixado.']:
   self.assertIsNone(gate(text,P))
 def test_futuro_expresso_em_outro_artigo_da_mesma_ordem_nao_retem(self):
  text='Art. 2º As insígnias obedecerão aos desenhos anexos ao regulamento da ordem.\n\nArt. 7º O Regulamento da Ordem Nacional será aprovado pelo Presidente, mediante proposta do Conselho.'
  self.assertIsNone(gate(text,P))
 def test_regulamento_futuro_de_outro_objeto_nao_apaga_desenho_proprio(self):
  text='Art. 1º A Medalha terá as características indicadas nos desenhos anexos.\n\nArt. 3º O regulamento das cerimônias será aprovado posteriormente.'
  self.assertIsNotNone(gate(text,P))


class PrecisaoDeReferentes(unittest.TestCase):
 def test_termo_com_lacuna_nao_e_definicao(self):
  self.assertIsNotNone(gate('Art. 1º O termo de (ilegível) será lavrado.',P))
 def test_rubrica_com_lacuna_nao_e_definicao(self):
  self.assertIsNotNone(gate('Art. 2º A rubrica do (ilegível) figurará no certificado.',P))
 def test_definicao_com_significado_explicito_nao_retem(self):
  self.assertIsNone(gate('Art. 1º A expressão (ilegível) significa documento sem leitura possível.',P))
 def test_rotulo_legitimo_nao_oculta_segunda_lacuna(self):
  self.assertIsNotNone(gate('Art. 1º Usar a expressão (ilegível) para classificação.\n\nArt. 2º O termo de (ilegível) será lavrado.',P))
 def test_aprovacao_propria_nao_e_dispensada_por_cerimonias_futuras(self):
  text='Art. 2º As insígnias obedecerão às características dos desenhos anexos ao regulamento aprovado por este decreto.\n\nArt. 7º O regulamento das cerimônias será aprovado posteriormente.'
  self.assertIsNotNone(gate(text,P))
 def test_regulamento_nomeado_atual_nao_e_dispensado_por_outro_futuro(self):
  text='Art. 1º Fica aprovado o Regulamento da Ordem.\n\nArt. 2º As insígnias obedecerão às características dos desenhos anexos ao regulamento da ordem.\n\nArt. 7º O regulamento das cerimônias será aprovado posteriormente.'
  self.assertIsNotNone(gate(text,P))
 def test_regulamento_futuro_no_mesmo_artigo_de_outro_objeto_nao_dispensa(self):
  text='Art. 2º As insígnias obedecerão às características dos desenhos anexos ao regulamento aprovado por este decreto; o regulamento das cerimônias será aprovado posteriormente.'
  self.assertIsNotNone(gate(text,P))

if __name__=='__main__':unittest.main()
