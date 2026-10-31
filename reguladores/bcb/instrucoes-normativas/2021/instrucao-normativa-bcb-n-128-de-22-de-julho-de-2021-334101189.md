---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 128, DE 22 DE JULHO DE 2021"
orgao: "Ministério da Economia/Banco Central do Brasil/Área de Organização do Sistema Financeiro e de Resolução/Departamento de Competição e de Estrutura do Mercado Financeiro"
tipo: "Instrução Normativa"
numero: "128"
data: 2021-07-22
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 26/07/2021, seção 1, p. 86"
data_publicacao: 2021-07-26
edicao: "139"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-128-de-22-de-julho-de-2021-334101189"
sha256_html_fonte: 2f050f1d2858905a2395e0c6026f84d886d6a48f437e2c239eaabfa21bb849ad
baixado_em: 2026-10-21
---
# INSTRUÇÃO NORMATIVA BCB Nº 128, DE 22 DE JULHO DE 2021

INSTRUÇÃO NORMATIVA BCB Nº 128, DE 22 DE JULHO DE 2021

Estabelece os procedimentos necessários para os testes formais de homologação no Diretório de Identificadores de Contas Transacionais (DICT), para a validação de QR Codes e para a validação da prestação de serviço de iniciação de transação de pagamento, no âmbito do Pix.

O Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro (Decem), no uso das atribuições que lhe confere o art. 97-A, inciso X, alínea "b", do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, e tendo em conta o disposto no art. 114 do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020, resolve:

**Art. 1º** Aplica-se o disposto nesta Instrução Normativa às instituições que, no âmbito do Pix estão sujeitas à realização dos testes formais de homologação no Diretório de Identificadores de Contas Transacionais (DICT), à validação de QR Codes e à validação da prestação de serviço de iniciação de transação de pagamento.

#### CAPÍTULO I — DOS TESTES FORMAIS DE HOMOLOGAÇÃO NO DICT

##### Seção I — Dos testes formais de homologação no DICT para os participantes provedores de conta transacional e liquidantes especiais

**Art. 2º** Os testes formais de homologação no DICT para os participantes provedores de conta transacional e liquidantes especiais são compostos das seguintes etapas:

I - preparação da instituição;

II - preparação do Banco Central do Brasil; e

III - execução dos testes.

###### Subseção I — Da Preparação da instituição

**Art. 3º** Para iniciar os testes, a instituição não pode ter nenhuma portabilidade, reivindicação de posse ou notificação de infração pendente de recebimento no ambiente de homologação.

**§ 1º** A preparação da instituição constitui-se em:

I - registrar mil chaves Pix de um determinado tipo; e

II - realizar, no mínimo, cinco transações, em ambiente de homologação, usando o participante virtual indicado pelo Decem no momento do agendamento dos testes.

**§ 2º** As informações sobre o tipo de chave de que trata o inciso I do § 1º e o conteúdo do campo EndToEndId das transações de que trata o inciso II do § 1º devem ser enviadas ao Decem por meio do endereço pix-operacional@bcb.gov.br.

###### Subseção II — Da Preparação do Banco Central do Brasil

**Art. 4º** Antes do início dos testes, o Banco Central do Brasil irá modificar e inserir algumas chaves Pix manualmente, do tipo informado pela instituição, para serem utilizadas no teste de verificação de sincronismo.

**Parágrafo único.** O Banco Central do Brasil criará reivindicações diversas ao longo da execução dos testes de que trata a Seção III deste Capítulo.

###### Subseção III — Da Execução dos testes

**Art. 5º** Todos os testes devem ser realizados dentro de uma janela de uma hora.

**Art. 6º** O horário de início da execução dos testes deve ser agendado por meio do endereço pix-operacional@bcb.gov.br.

**Art. 7º** Os seguintes testes devem ser realizados:

I - registro de chaves: registrar uma chave Pix de cada tipo;

II - consulta a chaves: consultar uma chave Pix de cada tipo (CPF, CNPJ, e-mail, número de telefone celular e chave aleatória);

III - verificação de sincronismo: realizar com sucesso uma verificação de sincronismo;

IV - recebimento de reivindicações: realizar o recebimento de todas as portabilidades e reivindicações de posse geradas pelo Banco Central do Brasil, em que é doador, em até um minuto;

V - fluxo de reivindicação: criar, confirmar, completar e cancelar pelo menos uma portabilidade ou reivindicação de posse, atuando como reivindicador;

VI - fluxo de notificação de infração: criar, confirmar, completar e cancelar pelo menos uma notificação de infração;

VII - fluxo de solicitação de devolução: criar e completar pelo menos uma solicitação de devolução por falha operacional do prestador de serviços de pagamento do pagador e uma por fundada suspeita de fraude.

**§ 1º** No teste de que trata o inciso II do caput, poderá haver, a critério do Decem, solicitação de consulta a uma ou mais chaves específicas.

**§ 2º** As instituições que prestarão serviço de acesso ao DICT para instituições com acesso indireto devem escolher uma instituição e realizar todos os testes dispostos nos incisos do caput para essa mesma instituição em uma janela de uma hora.

**§ 3º** A janela de tempo de que trata o § 2º deve ser diferente da janela de tempo de que trata o art. 5º e seu horário de início deve ser agendado por meio do endereço pix-operacional@bcb.gov.br.

**§ 4º** Após a realização de todos os testes, a instituição deve agendar, por meio do endereço pix-operacional@bcb.gov.br, o teste de capacidade.

**§ 5º** O teste de capacidade de que trata o § 4º consiste em:

I - consultar, no mínimo, mil chaves diferentes em um intervalo de sessenta segundos e receber resposta do DICT com sucesso, caso a instituição mantenha até um milhão de contas transacionais;

II - consultar, no mínimo, duas mil chaves diferentes em um intervalo de sessenta segundos e receber resposta do DICT com sucesso, caso a instituição mantenha entre um milhão e dez milhões de contas transacionais; ou

III - consultar, no mínimo, quatro mil chaves diferentes em um intervalo de sessenta segundos e receber resposta do DICT com sucesso, caso a instituição mantenha mais de dez milhões de contas transacionais.

**§ 6º** As consultas de que trata o § 5º devem durar dez minutos e devem ser distribuídas de forma homogênea ao longo do tempo, com o total de operações, no mínimo, igual a:

I - dez mil, caso a instituição mantenha até um milhão de contas transacionais;

II - vinte mil, caso a instituição mantenha entre um milhão e dez milhões de contas transacionais; ou

III - quarenta mil, caso a instituição mantenha mais de dez milhões de contas transacionais.

**§ 7º** Para obter aprovação no teste de capacidade, de que tratam os §§ 4º, 5º e 6º, a variação da taxa de consulta por minuto deve ser de até 20%.

##### Seção II — Dos testes formais de homologação no DICT para os participantes iniciadores

**Art. 8º** Os testes formais de homologação no DICT para os participantes iniciadores são compostos das seguintes etapas:

I - execução do teste de consulta de chaves; e

II - execução do teste de capacidade.

**§ 1º** O teste de consulta de chaves de que trata o inciso I do caput:

I - deve ser executado dentro de uma janela de uma hora;

II - deve ter o horário de início da execução agendado por meio do endereço pix-operacional@bcb.gov.br.

III - consiste na consulta de pelo menos uma chave Pix de cada tipo.

**§ 2º** No teste de consulta de que trata o inciso I do caput, poderá haver, a critério do Decem, solicitação de consulta a uma ou mais chaves específicas.

**§ 3º** O teste de capacidade de que trata o inciso II do caput:

I - deve ser efetuado após a aprovação no teste de consulta de que trata o inciso I do caput;

II - deve ser agendado, por meio do endereço pix-operacional@bcb.gov.br;

III - consiste em consultar, no mínimo, mil chaves diferentes em um intervalo de sessenta segundos e receber resposta do DICT com sucesso.

**§ 4º** As consultas de que trata o § 3º, inciso III, devem durar dez minutos e devem ser distribuídas de forma homogênea ao longo do tempo, com o total de operações, no mínimo, igual a dez mil.

**§ 5º** Para obter aprovação no teste de capacidade de que trata o inciso II do caput, a variação da taxa de consulta por minuto deve ser de até 20%.

##### Seção III — Das disposições gerais

**Art. 9º** O Decem pode, a seu exclusivo critério, determinar a repetição ou a complementação dos testes formais de homologação no DICT de que trata este Capítulo.

#### CAPÍTULO II — DA VALIDAÇÃO DE QR CODES

**Art. 10.** A validação de QR Codes para permitir a iniciação de um Pix através de leitura de QR Code estático ou de QR Code dinâmico (jornada do usuário pagador), obrigatória para participantes do Pix que ofertem contas transacionais a usuários finais pessoas naturais, compreende:

I - a leitura de QR Codes estáticos e dinâmicos gerados por ferramenta provida pelo Banco Central do Brasil e o correto envio das respectivas ordens de pagamento; e

II - a leitura de QR Codes estáticos e dinâmicos com erros intencionais gerados por ferramenta provida pelo Banco Central do Brasil e o correto tratamento das inconsistências encontradas.

**Parágrafo único.** A validação de QR Codes de que trata o caput também deve ser executada por participantes do Pix que ofertem contas transacionais exclusivamente a usuários finais pessoas jurídicas e por participantes iniciadores, caso o participante oferte a iniciação de um Pix através de leitura de QR Code estático ou de QR Code dinâmico.

**Art. 11.** A validação de QR Codes para permitir a geração de QR Codes estáticos associados ao Pix Cobrança para pagamentos imediatos (jornada do usuário recebedor), obrigatória para participantes do Pix que ofertem contas transacionais a usuários finais pessoas naturais e facultativa para participantes do Pix que ofertem contas transacionais exclusivamente a usuários finais pessoas jurídicas, compreende a validação com sucesso, em ferramenta provida pelo Banco Central do Brasil, de QR Codes estáticos gerados pelo provedor de conta transacional.

**Art. 12** A validação de QR Codes para permitir a geração de QR Codes dinâmicos associados ao Pix Cobrança para pagamentos imediatos e para pagamentos com vencimento (jornada do usuário recebedor), facultativa para os participantes do Pix, compreende a validação com sucesso, em ferramenta provida pelo Banco Central do Brasil, de QR Codes dinâmicos gerados pelo provedor de conta transacional.

**Art. 13.** Os participantes devem manter documentação que comprove a execução dos testes de validação de QR Codes para eventual análise por parte do Banco Central do Brasil pelo prazo de cinco anos.

**Art. 14.** O Decem pode, a seu exclusivo critério, determinar a repetição ou a complementação da realização dos testes de validação de QR Codes de que trata este Capítulo.

**Art. 15.** Previamente à oferta de produtos e serviços facultativos aos usuários finais, as instituições deverão comunicar seu intento ao Decem, através do Protocolo Digital do Banco Central do Brasil, por meio do envio dos formulários constantes nos Anexos I ou II, a depender da modalidade de participação, e realizar os procedimentos descritos neste Capítulo.

#### CAPÍTULO III — DA VALIDAÇÃO DA PRESTAÇÃO DE SERVIÇO DE INICIAÇÃO DE TRANSAÇÃO DE PAGAMENTO

**Art. 16.** Para o provedor de conta transacional, os testes homologatórios referentes ao serviço de iniciação de transação de pagamento consistem na verificação de sua aptidão para a realização de um Pix após o recebimento de um pedido de iniciação.

**Parágrafo único.** Os testes de que trata o caput compreendem a validação com sucesso, em ferramenta provida pelo Banco Central do Brasil, da realização de um Pix mediante prévio recebimento de pedido de iniciação:

I - com chave Pix;

II - com inserção manual dos dados da conta transacional do usuário recebedor;

III - nos casos em que a instituição que provê o serviço de iniciação detém todas as informações do usuário recebedor; e

IV - com leitura de QR Code.

**Art. 17.** Para o iniciador, os testes homologatórios referentes à prestação do serviço de iniciação de transação de pagamento consistem na verificação de sua aptidão para a emissão de um pedido de iniciação de um Pix para o detentor da conta transacional.

**§ 1º** Os testes de que trata o caput compreendem a validação com sucesso, em ferramenta provida pelo Banco Central do Brasil, da emissão de um pedido de iniciação:

I - com chave Pix;

II - com inserção manual dos dados da conta transacional do usuário recebedor;

III - nos casos em que a instituição que provê o serviço de iniciação detém todas as informações do usuário recebedor; e

IV - com leitura de QR Code.

**§ 2º** O participante provedor de conta transacional que pretenda ofertar o serviço de iniciação de transação de pagamento deverá submeter-se à prévia realização dos testes de que trata o § 1º .

**§ 3º** Os testes de que trata o § 1º deverão ser realizados de acordo com os serviços de iniciação de transação de pagamento que o participante pretenda ofertar.

**§ 4º** Previamente à realização dos testes de que trata o § 1º, o participante deverá manter atualizadas as informações constantes dos Anexos I e II.

**§ 5º** As atualizações de que trata o § 4º devem ser encaminhadas ao Decem exclusivamente por meio do Protocolo Digital do Banco Central do Brasil (Protocolo Digital).

**Art. 18.** O Decem pode, a seu exclusivo critério, determinar a repetição ou a complementação da realização dos testes de validação da prestação de serviço de iniciação de transação de pagamento de que trata este Capítulo.

#### CAPÍTULO IV — DAS DISPOSIÇÕES TRANSITÓRIAS

**Art. 19.** O teste de que trata o art. 7º, inciso VII, deverá ser obrigatoriamente realizado até 5 de novembro de 2021 por todas as instituições ativas em ambiente de produção do Pix com acesso direto ao DICT.

**Parágrafo único.** A partir de 6 de novembro de 2021, o teste de que trata o caput deverá ser obrigatoriamente realizado por todas as demais instituições que tenham optado pelo acesso direto ao DICT no âmbito do processo de adesão ao Pix.

**Art. 20.** A validação da prestação de serviço de iniciação de transação de pagamento de que trata o art. 16 deverá ser obrigatoriamente realizada por todas as instituições ativas em ambiente de produção do Pix que participem do Pix na modalidade provedor de conta transacional e que possuam autorização para funcionamento emitida pelo Banco Central do Brasil até:

I - 23 de agosto de 2021, para os testes de que tratam os incisos I e II do parágrafo único do art. 16;

II - 23 de setembro de 2021, para o teste de que trata o inciso III do parágrafo único do art. 16; e

III - 22 de outubro de 2021, para o teste de que trata o inciso IV do parágrafo único do art. 16.

**§ 1º** A partir de 24 de agosto de 2021, a validação dos testes de que trata o inciso I do caput deverá ser obrigatoriamente realizada por todas as demais instituições que tenham optado por participar do Pix na modalidade provedor de conta transacional e que possuam autorização para funcionamento emitida pelo Banco Central do Brasil, no âmbito do processo de adesão ao Pix.

**§ 2º** A partir de 24 de setembro de 2021, a validação do teste de que trata o inciso II do caput deverá ser obrigatoriamente realizada por todas as demais instituições que tenham optado por participar do Pix na modalidade provedor de conta transacional e que possuam autorização para funcionamento emitida pelo Banco Central do Brasil, no âmbito do processo de adesão ao Pix.

**§ 3º** A partir de 23 de outubro de 2021, a validação do teste de que trata o inciso III do caput deverá ser obrigatoriamente realizada por todas as demais instituições que tenham optado por participar do Pix na modalidade provedor de conta transacional e que possuam autorização para funcionamento emitida pelo Banco Central do Brasil, no âmbito do processo de adesão ao Pix.

**§ 4º** A validação da prestação de serviço de iniciação de transação de pagamento não se aplica à cooperativa singular de crédito, filiada à cooperativa central de crédito, e que tenha como liquidante no SPI entidade do sistema cooperativo organizado de dois ou três níveis.

#### CAPÍTULO V — DAS DISPOSIÇÕES GERAIS

**Art. 21.** Esta Instrução Normativa entra em vigor em 2 de agosto de 2021.

Angelo JOSÉ MONT ALVERNE DUARTE

## ANEXO I

Formulário de produtos e serviços ofertados por participantes provedores de conta transacional.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>I</p></td>      <td rowspan="1" colspan="1"><p>Inscrição no CNPJ</p></td>      <td rowspan="1" colspan="1"><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>II</p></td>      <td rowspan="1" colspan="1"><p>Razão Social</p></td>      <td rowspan="1" colspan="1"></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>III</p></td>      <td rowspan="1" colspan="1"><p>Oferta contas transacionais a usuários finais:</p></td>      <td rowspan="1" colspan="1"><p>( ) pessoas jurídicas</p><p>( ) pessoas naturais</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IV</p></td>      <td rowspan="1" colspan="1"><p>Produtos e serviços obrigatórios ofertados a pessoas naturais</p></td>      <td rowspan="1" colspan="1"><p>Iniciação de Pix - Chave Pix</p><p>Iniciação de Pix - Leitura de QR Code estático</p><p>Iniciação de Pix - Leitura de QR Code dinâmico</p><p>Pix Cobrança para pagamentos imediatos - geração de QR Code estático</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>V</p></td>      <td rowspan="1" colspan="1"><p>Produtos e serviços facultativos ofertados a pessoas naturais</p></td>      <td rowspan="1" colspan="1"><p>( ) Pix Agendado</p><p>( ) Pix Cobrança para pagamentos imediatos - geração de QR Code dinâmico</p><p>( ) Pix Cobrança para pagamentos com vencimento - geração de QR Code dinâmico</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>VI</p></td>      <td rowspan="1" colspan="1"><p>Produtos e serviços facultativos ofertados a pessoas jurídicas</p></td>      <td rowspan="1" colspan="1"><p>( ) Iniciação de Pix - Chave Pix<strong>*</strong></p><p>( ) Iniciação de Pix - Leitura de QR Code estático<strong>*</strong></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>( ) Iniciação de Pix - Leitura de QR Code dinâmico<strong>*</strong></p><p>( ) Pix Agendado</p><p>( ) Pix Cobrança para pagamentos imediatos - geração de QR Code estático</p><p>( ) Pix Cobrança para pagamentos imediatos - geração de QR Code dinâmico</p><p>( ) Pix Cobrança para pagamentos com vencimento - geração de QR Code dinâmico</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>VII</p></td>      <td rowspan="1" colspan="1"><p>Produtos facultativos ofertados por meio de serviço de iniciação de transação de pagamento (disponíveis apenas aos participantes autorizados a funcionar pelo BC)**</p></td>      <td rowspan="1" colspan="1"><p>( ) Iniciação de Pix - Inserção manual de dados da conta transacional do usuário recebedor</p><p>( ) Iniciação de Pix - Chave Pix</p><p>( ) Iniciação de Pix - INIC***</p><p>( ) Iniciação de Pix - leitura de QR code</p><p>( ) Pix Agendado</p></td>     </tr>    </tbody>   </table>

\*A instituição que disponibilize contas transacionais exclusivamente a usuários pessoas jurídicas deverá disponibilizar, no mínimo, uma das três modalidades de iniciação de um Pix.

\*\* A prestação de serviço de iniciação de transação de pagamento é facultativa aos participantes provedores de conta transacional e disponível apenas mediante prévia:

I - autorização para exercício da atividade, concedida pelo BC, ressalvados os casos de dispensa previstos no art. 16 da Resolução BCB nº 80, de 25 de março de 2021; e

II - obtenção do certificado de segurança do Open Banking Brasil.

\*\*\* Corresponde aos casos em que o provedor de conta transacional prestador do serviço de iniciação detém as informações do usuário recebedor.

Anexo II - Formulário de produtos e serviços facultativos ofertados por participantes iniciadores.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>I</p></td>      <td rowspan="1" colspan="1"><p>Inscrição no CNPJ</p></td>      <td rowspan="1" colspan="1"></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>II</p></td>      <td rowspan="1" colspan="1"><p>Razão Social</p></td>      <td rowspan="1" colspan="1"></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>III</p></td>      <td rowspan="1" colspan="1"><p>Produtos facultativos ofertados por meio de serviço de iniciação<strong>*</strong></p></td>      <td rowspan="1" colspan="1"><p>( ) Iniciação de Pix - Inserção manual de dados da conta transacional do usuário recebedor</p><p>( ) Iniciação de Pix - Chave Pix</p><p>( ) Iniciação de Pix - INIC**</p><p>( ) Iniciação de Pix - leitura de QR code</p><p>( ) Pix Agendado</p></td>     </tr>    </tbody>   </table>

\* O iniciador deverá disponibilizar, no mínimo, uma das modalidades de iniciação de um Pix.

\*\* Corresponde aos casos em que o participante iniciador detém as informações do usuário recebedor.
