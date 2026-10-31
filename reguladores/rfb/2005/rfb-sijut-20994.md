---
titulo: "Portaria Coana nº 13, de 29 de junho de 2005"
orgao: "Coordenação-Geral de Administração Aduaneira"
tipo: "Portaria"
numero: "13"
data: "2005-06-29"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 04/07/2005, seção 1, página 23"
data_publicacao: "2005-07-04"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/20994/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/20994/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "20994"
sha256_texto: "97d070189e755e902418419fe627a414c70237e45b6ec6ee40922e2d9c6a29b2"
baixado_em: "2026-10-21"
---
# Portaria Coana nº 13, de 29 de junho de 2005

Dispõe sobre a definição e classificação dos perfis de usuários, relativos ao módulo de controle de Ações Fiscais no ambiente Sief - Ação Fiscal Aduaneiro.

O COORDENADOR-GERAL DE ADMINISTRAÇÃO ADUANEIRA, no uso de suas atribuições regimentais e tendo em vista as disposições constantes da Portaria SRF nº 450, de 28 de abril de 2004, e da Portaria SRF/Cotec nº 45, de 27 de maio de 2004, resolve:

**Art.1º** Alterar e aprovar a definição e a classificação dos perfis de usuários, relativos ao controle de acesso lógico do módulo Sief - Ação Fiscal Aduaneiro, conforme Anexo Único.

**Art. 2º** Fica formalmente revogada a Portaria Coana nº 24, de 26 de outubro de 2004.

**Art. 3º** Esta Portaria entra em vigor nesta data.

RONALDO LÁZARO MEDINA

ANEXO ÚNICO



ANEXO ÚNICO SISTEMA AÇÃO FISCAL ADUANEIRO (AFA) Sistema de Controle de Ações Fiscais Aduaneiro OBJETIVO: Controlar e acompanhar de modo padronizado e uniforme as ações fiscais aduaneiras empreendidas pela Secretaria da Receita Federal (SRF), gerando informações e documentos que possibilitem melhor gerenciamento em nível nacional, regional e local, aumentando a eficácia no seu desempenho por meio da otimização da utilização dos recursos humanos. DESCRIÇÃO DOS MÓDULOS E RESPECTIVAS TRANSAÇÕES: 1. PROGRAMAÇÃO: Cadastramento, consulta e exclusão de contribuintes selecionados e passíveis de serem fiscalizados. 2. RPF / MPF: RPF - Registro de Procedimento Fiscal - Documento de caráter interno que registra todas as atividades fiscais desenvolvidas pelos AFRF perante o contribuinte. Para cada procedimento fiscal será emitido um único RPF. MPF - Mandado de Procedimento Fiscal - Documento de caráter externo que instaura e informa os procedimentos de fiscalização e de diligência perante o contribuinte, nos termos da Portaria SRF nº 3.007, de 26 de novembro de 2001. 3. GRUPO: Alocação, exclusão e consulta da mão-de-obra AFRF em Grupos Fiscais. 4. DOSSIÊ: Permite a obtenção de informações consolidadas por contribuinte. 5. RMF: Requisição de Informações sobre Movimentação Financeira - Documento de caráter externo para requisitar informações constantes de documentos, livros e registros de instituições financeiras e de entidades a elas equiparadas, inclusive os referentes a contas de depósitos e de aplicações financeiras. PERFIS

PERFIS 1 - Perfil AFA\_Consulta\_Pleno (REMOTO)

1.1 - Classificação: Gerencial

1.2 - Permitida a habilitação de Não

1.3 - Usuários: Coordenador-Geral da Coana, Coordenador da Coana/Cofin, Chefe da Coana/Cofin/Difia, Superintendentes da Receita Federal, Chefes da Divisão de Administração Aduaneira (Diana), Delegados da Receita Federal, Inspetores da Receita Federal e da Alfândega seus substitutos e/ou servidores por um deles autorizados.

1.4 - Resumo das transações: Transações que permitam consultas

FISCC502 CONSULTA PROGRAMAÇÃO Consulta as programações registradas

FISCC515 CONSULTA AFRF EM GRUPO FISCAL Consulta os grupos fiscais

FISCP501 EMISSÃO RPF/MPF Permite a emissão de RPF/MPF

emissão de Dossiê CAC

FISCR600 DOCUMENTO RPF Consulta Documento RPF

FISCR601 DOCUMENTO Consulta Documento

FISCR602 DOCUMENTO PRORROGAÇÃO MPF Permite consulta ao relatório de prorrogação de MPF

FISCR603 EXTRATO DE PRORROGAÇÕES Consulta extrato de prorrogação

FISCR605 RELATÓRIO DE RPF PENDENTES OU Emite relatório de RPF pendente ou encerrado ENCERRADAS por seqüência de RPF

FISCP525 PARÂMETRO CONSULTA DE RMF Permite informar contribuinte para posterior consulta de RMF

FISCC526 CONSULTA DE RMF Consulta RMF registradas

FISCP521 PARÂMETRO EMISSÃO RMF Permite informar contribuinte para posterior visualização/emissão de RMF

FISCR606 RELATÓRIO RMF Permite a visualização/emissão de RMF

2- Perfil AFA\_Distribui\_MPF (REMOTO)

2.1 - Classificação: Operacional

2.2 - Permitida a habilitação de Não

2.3 - Usuários: Coordenador-Geral da Coana, Coordenador da Coana/Cofin, Chefe da Coana/Cofin/Difia, Superintendentes da Receita Federal, Chefes da Divisão de Administração Aduaneira (Diana), Delegados da Receita Federal, Inspetores da Receita Federal e da Alfândega, chefes de setor, serviço ou seção de fiscalização aduaneira, seus substitutos e/ou servidores autorizados pelos respectivos titulares das unidades administrativas.

2.4 - Resumo das transações: Todas as transações do sistema

FISCC502 CONSULTA PROGRAMAÇÃO Consulta programação de RPF/MPF

FISCT503 RETIFICAÇÃO PROGRAMAÇÃO Permite retificação de programação de RPF/MPF

FISCP504 CANCELAMENTO PROGRAMAÇÃO Permite o cancelamento de programação de fiscalização

FISCT500 CADASTRAMENTO PROGRAMAÇÃO Permite cadastrar programação de fiscalização

FISCT505 DISTRIBUIÇÃO RPF Permite distribuição de RPF a algum AFRF de

um grupo fiscal

FISCP501 EMISSÃO RPF/MPF Permite a emissão de RPF/MPF

FISCT508 RETIFICAÇÃO RPF Permite retificação de RPF

FISCP510 ENCERRAMENTO MANUAL Permite encerramento não eletrônico de RPF/MPF

FISCP518 PRORROGAÇÃO MPF Permite prorrogação de MPF

FISCR601 DOCUMENTO MPF Consulta documento MPF

FISCR600 DOCUMENTO RPF Consulta documento RPF

FISCR602 DOCUMENTO PRORROGAÇÃO MPF Permite consulta ao relatório de prorrogação de MPF

FISCR603 EXTRATO DE PRORROGAÇÕES Consulta extrato de prorrogações

FISCT511 CONVERSÃO DE AÇÃO FISCAL Permite conversão/transformação de MPF

FISCT512 ENCERRAMENTO COM EXAME Permite o encerramento com exame de RPF/MPF

FISCT513 ENCERRAMENTO SEM EXAME Permite o encerramento sem exame de RPF/MPF

FISCT514 ENCERRAMENTO POR CANCELAMENTO Permite o encerramento por cancelamento de RPF/MPF

FISCC515 CONSULTA AFRF EM GRUPO FISCAL Consulta os grupos fiscais

FISCT516 CADASTRAMENTO AFRF EM GRUPO FISCAL Permite cadastramento e manutenção de AFRF em grupo fiscal

emissão de dossiê CAC

FISCR605 RELATÓRIO DE RPF PENDENTES OU Emite relatório de RPF pendente ou encerrado ENCERRADAS por seqüência de RPF

FISCP525 PARÂMETRO CONSULTA DE RMF Permite informar contribuinte para posterior consulta de RMF

FISCC526 CONSULTA DE RMF Consulta RMF registradas

FISCP521 PARÂMETRO EMISSÃO RMF Permite informar contribuinte para posterior visualização/emissão de RMF

FISCR606 RELATÓRIO RMF Permite a visualização/emissão de RMF

FISCP520 IMPORTAÇÃO DE RMF PROVISÓRIO Permite a importação de arquivo de integração

FISCP522 PARÂMETRO GERAR RMF Permite informar contribuinte para posterior geração de RMF

FISCT523 GERAR RMF Permite a geração de RMF a partir da RMF provisória

FISCP524 PARÂMETRO CANCELAMENTO DE RMF Permite o cancelamento de RMF

FISCP527 PARÂMETRO PARA SELEÇÃO DE RPF A Permite selecionar os RPF a serem exportados SEREM EXPORTADOS PARA O SISTEMA para o sistema Safira SAFIRA

FISCR607 RELATÓRIO DE RPF REJEITADOS NA Demonstrativo dos RPF rejeitados na EXPORTAÇÃO PARA O SISTEMA SAFIRA exportação para o sistema Safira

FISCP528 PARÂMETRO PARA SELEÇÃO DE RPF A Permite selecionar os RPF a serem importados SEREM IMPORTADOS DO SISTEMA SAFIRA do sistema Safira

FISCR608 RELATÓRIO DE RPF REJEITADOS NA Demonstrativo de RPF rejeitados na importação IMPORTAÇÃO DO ARQUIVO DO SISTEMA do arquivo do sistema Safira SAFIRA

FISCR609 RELATÓRIO DE RPF IMPORTADOS NA Demonstrativo de RPF importados na INTEGRAÇÃO COM O SISTEMA SAFIRA integração com o sistema Safira

3 - Perfil AFA\_Dossie\_CAC (REMOTO)

3.1 - Classificação: Gerencial

3.2 - Permitida a habilitação de Não

3.3 - Usuários: Servidores lotados nas Alfândegas, Delegacias, Inspetorias e Agências da Receita Federal responsáveis pelo atendimento a contribuintes e servidores do serviço de atendimento telefônico automático (Receitafone), servidores lotados na Coordenação-Geral de Pesquisa e Investigação, no Escritório de Pesquisa Investigação, autorizados pelos respectivos titulares das unidades administrativas.

3.4 - Resumo das transações: Transações que permitam consultas

emissão de Dossiê CAC

