---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 27, DE 13 DE OUTUBRO DE 2020"
orgao: "Ministério da Economia/Banco Central do Brasil/Área de Política Monetária/Departamento de Operações Bancárias e de Sistema de Pagamentos"
tipo: "Instrução Normativa"
numero: "27"
data: 2020-10-13
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 14/10/2020, seção 1, p. 83"
data_publicacao: 2020-10-14
edicao: "197"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-27-de-13-de-outubro-de-2020-282470683"
sha256_html_fonte: eca5b84941804047eb4ebe76fcdba8c337c23806ae92f9a24851e4d8c38bcff6
baixado_em: 2026-10-21
---
# INSTRUÇÃO NORMATIVA BCB Nº 27, DE 13 DE OUTUBRO DE 2020

INSTRUÇÃO NORMATIVA BCB Nº 27, DE 13 DE OUTUBRO DE 2020

Estabelece procedimentos operacionais relativos à manutenção no Banco Central do Brasil de recursos, em espécie, correspondentes ao valor do saldo das moedas eletrônicas mantidas em conta de pagamento.

O CHEFE DO DEPARTAMENTO DE OPERAÇÕES BANCÁRIAS E DE SISTEMA DE PAGAMENTOS (Deban), no uso das atribuições que lhe confere o art. 111, inciso XIV, e o art. 23, inciso I, alínea "a", do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, com base no art. 12, da Circular nº 3.681, de 4 de novembro de 2013, e na Circular nº 3.704, de 24 de abril de 2014, com as alterações introduzidas pela Circular nº 4.038, de 28 de julho de 2020, resolve:

**Art. 1º** O disposto nesta Instrução Normativa se aplica às instituições emissoras de moeda eletrônica e aos titulares de conta Reservas Bancárias, de Conta de Liquidação e de Conta Pagamentos Instantâneos (Conta PI), exceto câmaras e prestadores de serviços de compensação e de liquidação.

**Art. 2º** Para cumprimento da obrigatoriedade de manutenção, no Banco Central do Brasil, de recursos em espécie correspondentes ao valor do saldo das moedas eletrônicas mantidas em contas de pagamento e em trânsito entre contas de pagamento na mesma instituição de pagamento, de que trata o art. 12 da Circular nº 3.681, de 4 de novembro de 2013, as instituições emissoras de moeda eletrônica devem observar os procedimentos operacionais estabelecidos nesta Instrução Normativa.

#### CAPÍTULO I — DAS DEFINIÇÕES

**Art. 3º** Para efeitos dessa Instrução Normativa, considera-se:

I - instituição emissora de moeda eletrônica (IEME): instituição que gerencia conta de pagamento de usuário final, do tipo pré-paga, e disponibiliza transação de pagamento com base em moeda eletrônica aportada nessa conta;

II - instituição de pagamento: pessoa jurídica integrante do Sistema de Pagamentos Brasileiro (SPB), definida no art. 6º, inciso III, da Lei nº 12.865, de 9 de outubro de 2013;

III - Conta Correspondente a Moeda Eletrônica (CCME): conta específica mantida no Banco Central do Brasil, de titularidade das instituições de pagamento, das instituições financeiras e das demais instituições autorizadas a funcionar pelo Banco Central do Brasil, quando emissoras de moeda eletrônica, destinada exclusivamente à manutenção dos recursos em espécie correspondentes ao valor do saldo das moedas eletrônicas mantidas em conta de pagamento pré-paga por elas gerenciadas, acrescido dos saldos de moedas eletrônicas em trânsito entre contas de pagamento na mesma instituição de pagamento; e

IV - recursos em espécie: saldo em reais mantido em conta no Banco Central do Brasil.

#### CAPÍTULO II — DAS MOVIMENTAÇÕES DE RECURSOS NA CONTA CORRESPONDENTE A MOEDA ELETRÔNICA

##### Seção I — Da utilização dos Grupos de Serviços SME e LPI

**Art. 4º** As movimentações de recursos na CCME são realizadas por meio de mensagens dos Grupos de Serviços SME e LPI, do Catálogo de Serviços do SFN, observado que:

I - o envio das mensagens dos Grupos de Serviços SME e LPI pelas instituições participantes do STR é feito por meio da Rede do Sistema Financeiro Nacional (RSFN) ou pela internet, utilizando o aplicativo STR-Web, conforme a forma de acesso principal ao STR utilizada pelo participante, durante operação em regime normal ou de contingência; e

II - as IEME não participantes do STR utilizam o aplicativo STR-Web para comandar transferências a débito da CCME de sua titularidade e a débito da Conta PI para crédito na CCME, ambas de sua titularidade.

##### Seção II — Da alocação dos recursos

**Art. 5º** A transferência a crédito da CCME é realizada por meio da mensagem "SME0001- IF requisita transferência para depósito em conta específica" ou por meio da mensagem "LPI0004 - PSPI requisita transferência para saque em Conta PI e depósito em CCME", constante do Catálogo de Serviços do SFN.

##### Seção III — Da retirada de recursos

**Art. 6º** A transferência a débito da CCME deve ser comandada exclusivamente pelo titular da referida conta por meio da mensagem "SME0002- IEME requisita transferência para saque em conta específica" ou por meio da mensagem "LPI0002 - IF requisita transferência de conta CCME para depósito em Conta PI", constantes do Catálogo de Serviços do SFN.

**Parágrafo único.** O sistema verificará, a cada requisição de débito na CCME, o saldo disponível na referida conta do solicitante e rejeitará as requisições no caso de insuficiência de saldo.

##### Seção IV — Das Devoluções de recursos recebidos indevidamente

**Art. 7º** A devolução de transferência envolvendo a CCME deve ser realizada por meio da mensagem "SME0004 - IF ou IEME requisita transferência para devolução de lançamento indevido no SME".

**§1º** A devolução deve ocorrer em comando único e corresponder ao valor total do originalmente recebido.

**§2º** Todas as instituições detentoras de conta Reservas Bancárias devem estar aptas ao envio da mensagem SME0004 - IF ou IEME requisita transferência para devolução de lançamento indevido no SME - para eventual necessidade de devolução de recursos indevidamente creditados em sua conta.

##### Seção V — Da autorização para movimentação financeira na CCME

**Art. 8º** A autorização para uso das mensagens dos Grupos de Serviços SME ou LPI, do Catálogo de Serviços do SFN, e a ativação da CCME são solicitadas por intermédio de expediente encaminhado pela IEME ao Deban, esclarecido que a solicitação deve ser encaminhada por:

I - instituições de pagamento que emitem moeda eletrônica, que optarem por realizar alocações de recursos em espécie: após a expedição, pelo Banco Central do Brasil, da autorização para emitir moeda eletrônica; e

II - instituições financeiras e demais instituições autorizadas a funcionar pelo Banco Central do Brasil prestadoras de serviços de pagamento na modalidade de emissor de moeda eletrônica: a qualquer momento.

**§1º** A solicitação de que trata o caput poderá fazer parte do processo de abertura de conta Reservas Bancárias ou de Conta de Liquidação, ou de participação no Sistema de Pagamentos Instantâneos (SPI), com a respectiva abertura de Conta PI, no Banco Central do Brasil, na forma estabelecida pelo Deban.

**§2º** A liberação para uso das mensagens dos Grupos de Serviços SME ou LPI pela instituição e a ativação da CCME, em ambiente de produção, estão condicionadas à realização de testes estabelecidos pelo Deban.

**Art. 9º** As instituições financeiras titulares de conta Reservas Bancárias não emissoras de moeda eletrônica podem solicitar, a qualquer momento, autorização para utilização da mensagem "SME0001 - IF requisita transferência para depósito em conta específica" para comandar transferências em nome de IEME não participante do STR.

**Parágrafo único.** A liberação de uso da mensagem, na situação mencionada no caput, deve ser objeto de solicitação específica ao Deban, que indicará o teste necessário para o cadastramento.

#### CAPÍTULO III — DA UTILIZAÇÃO DO APLICATIVO STR-WEB PELAS IEME NÃO PARTICIPANTES DO STR

**Art. 10.** A utilização do aplicativo STR-Web pelas IEME não participantes do STR segue os requisitos técnicos e de segurança para acesso ao STR-Web descritos no Manual de Acesso ao STR via Internet, disponível no sítio do Banco Central do Brasil (www.bcb.gov.br).

**Art. 11.** A solicitação de acesso ao STR-Web e de movimentação da CCME deve ser feita por intermédio de expediente encaminhado ao Deban, firmado pelo diretor responsável pelo cumprimento das normas relativas à conta de pagamento, observado que:

**§1º** A solicitação de que trata o caput deve ser encaminhada, conforme o caso, nos momentos descritos no art. 8º, incisos I e II, desta Instrução Normativa.

**§2º** A liberação para uso do STR-Web pela instituição em ambiente de produção está condicionada à realização de testes estabelecidos pelo Deban.

**Art. 12.** As IEME não participantes do STR devem informar e manter atualizado, por meio de registro no portlet "Responsáveis" do STR-Web, o nome, o número de CPF, o número do documento oficial de identificação, o endereço de e-mail e, no mínimo, dois números de telefone em ordem de prioridade para contato:

I - do diretor responsável pelo cumprimento das normas relativas à conta de pagamento, de que trata o art. 5º da Circular nº 3.680, de 4 de novembro de 2013;

II - de, no mínimo, dois responsáveis pelo gerenciamento da Conta Correspondente a Moeda Eletrônica;

III - de, no mínimo, três representantes para as solicitações referentes ao regime de operação em Contingência Telefônica.

**Parágrafo único.** As responsabilidades descritas nos incisos I, II e III podem ser atribuídas de forma acumulada.

**Art. 13.** A instituição emissora de moeda eletrônica não participante do STR deve informar ao Deban, por meio de expediente firmado pelo diretor responsável pelo cumprimento das normas relativas à conta de pagamento, os dados bancários para envio da cobrança da tarifa pela utilização do serviço de contingência de que trata o art. 10 da Circular nº 3.704, de 24 de abril de 2014.

**Art. 14.** As solicitações de ativação e de encerramento da operação em regime de Contingência Telefônica de que trata o art. 9º da Circular nº 3.704, de 2014, são feitas por intermédio de contato telefônico originado de um dos representantes citados no art.12, inciso III, desta Instrução Normativa, com o componente da Divisão de Gestão e Monitoramento dos Sistemas de Transferências de Fundos do BCB (Gemon) ao qual o solicitante estiver vinculado.

**Art. 15.** Fica revogada a Carta Circular nº 3.893, de 7 de agosto de 2018.

**Art. 16.** Esta Instrução Normativa entra em vigor em 3 de novembro de 2020.

FLÁVIO TÚLIO VILELA
