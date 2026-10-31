---
titulo: "Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020"
orgao: "Coordenação-Geral de Arrecadação e Direito Creditório"
tipo: "Ato Declaratório Executivo"
numero: "4"
data: "2020-09-01"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 03/09/2020, seção 1, página 49"
data_publicacao: "2020-09-03"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/112156/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/112156/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "112156"
sha256_texto: "7e44c9170a09d77fd68630d1a0ee085e77b0a6a418775cd79345cb85013d2937"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020

Aprova o Manual de Integração - Modelo padrão de pagamento online.

O COORDENADOR-GERAL DE ARRECADAÇÃO E DIREITO CREDITÓRIO, no exercício da atribuição prevista no inciso II do art. 358 do Regimento Interno da Secretaria Especial da Receita Federal do Brasil, aprovado pela Portaria ME nº 284, de 27 de julho de 2020, declara:

**Art. 1º** Fica aprovado o Manual de Integração - Modelo padrão de pagamento online, a ser observado pelas instituições integrantes da Rede Arrecadadora de Receitas Federais (Rarf) para recepção de documentos de arrecadação com código de barras, padrão Febraban, pela Internet, mediante débito em conta corrente online pré-autorizado nas instituições, por meio de Application Programming Interface (API) entre instituições autorizadas a funcionar pelo Banco Central do Brasil e a Secretaria Especial da Receita Federal do Brasil.

**Art. 2º** Os serviços descritos no "Manual de Integração - Modelo padrão de pagamento online" serão implantados, efetivamente, para os agentes arrecadadores habilitados, a partir de 17 de janeiro de 2021.

**Art. 3º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

MARCUS VINICIUS MARTINS QUARESMA

ANEXO ÚNICO - MANUAL DE INTEGRAÇÃO - MODELO PADRÃO DE PAGAMENTO ONLINE



(Fl. 1 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.)

Manual de Integração Modelo padrão de pagamento online FEBRABAN

Modelo padrão de pagamento online Página 1

(Fl. 2 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) Histórico de Versões

Data Versão Descrição Responsável 29/11/2019 0.1.0 Criação do Documento RFB-SERPRO-FEBRABAN Inclusão de códigos HTTP e de observações da 12/12/2019 0.1.1 RFB-SERPRO-FEBRABAN FEBRABAN 13/12/2019 0.1.2 Atualização da seção “Segurança” RFB-SERPRO-FEBRABAN Alteração no nome dos campos: de “cpfDespachante” para “cpfUsuario” e de 17/12/2019 0.1.2.1 RFB-SERPRO-FEBRABAN “importador” para “contribuinte”, conforme solicitado na reunião com a RFB. - Inclusão do campo referenciaDebito, dataRequisicao e horaRequisicao no objeto da requisição - Alteração do domínio do campo tipo do contribuinte de CPF para 01 e CNPJ para 02 20/12/2019 0.1.3 RFB-SERPRO-FEBRABAN - Adição do campo descricao no objeto resposta na seção códigos erro - Substituição do termo Siscomex para PUCOMEX - Detalhamento do endpoint do serviço - Adição da obrigatoriedade dos campos - Inclusão da proposta inicial para o processo de testes e homologação 23/12/2019 0.1.4 RFB-SERPRO-FEBRABAN - Inclusão do contrato no formato .yaml como um objeto OLE. - Inclusão de dúvida sobre a redação da seção 2. Premissas. - Complementação dos campos do débito na Banco do Brasil 23/12/2019 0.1.5 (Andrea Maria Braga)

seção 4.2. andreab@bb.com.br - Dúvida sobre o campo referenciaDebito

- Inclusão de regra sobre pagamentos realizados em horário próximo das 23h59min59s Bradesco 27/12/2019 0.1.6 - Observação sobre a consistência no código de (Deise Aparecida) barras deise.rodrigues@bradesco.com.br

- Alteração/Remoção da regra de reenvio do débito com o mesmo número de protocolo. Sugere-se usar o método GET a reenviar o mesmo protocolo. Citibank 27/12/2019 0.1.7 (Priscila Duarte) - Inclusão de dúvida/proposta para “travarmos” priscila.duarte@citi.com para ter apenas um código de barras por cada protocolo.

- Inclusão dos campos dataTransacao e horaTransacao e remoção do campo Reunião horaArrecadacao no objeto RespostaDebito. 03/01/2020 0.1.8 RFB-SERPRO-FEBRABAN - Estabelecendo o campo ReferenciaDebito como obrigatório.

Modelo padrão de pagamento online Página 2

(Fl. 3 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) Pedido do BB para renomear a parte fixa do endpoint do serviço de /v1/debitos para um Banco do Brasil nome mais específico relativo ao DARA. (Pacini) 03/01/2020 0.1.9 Alteração na descrição do campo Citibank (Priscila Duarte) “ReferenciaDebito” - uso do DUIMP no caso do PUCOMEX Alteração do item 4.2.1 • Definição do tempo máximo permitido Alteração do item 4.2.3 • Erro 400: Definição do tempo máximo 27/02/2020 0.1.10 RFB-SERPRO-FEBRABAN permitido • Erro 429: Remoção do limite de requisições (cada banco deverá definir seu limite) Alteração do termo “débito automático” para “débito online”. 05/03/2020 0.1.11 RFB-SERPRO-PUCOMEX Definição do formato do campo referenciaDebito. - Alterações no objeto RequisiçãoDebito: Remoção da lista de códigos de barra com erro. Caso haja algum problema com pelo menos um código de barra, os mesmos deverão ser 20/03/2020 0.1.12 SERPRO-FEBRABAN retornados no objeto ErroDébito, não havendo mais a possibilidade de débito parcial. - Criação do código 08 - Requisição com total de códigos de barra superior a cinco. - Remoção do item “d” das 7. Regras de negócio: “No caso de não convênio do banco 26/03/2020 0.1.13 com determinada Sefaz para recebimento de SERPRO-FEBRABAN GNRE, o banco poderá debitar valores somente para os quais tenha convênio.”

31/03/2020 1.0 Versão final do Modelo de Integração SERPRO-FEBRABAN

Alteração da Versão final após reunião com o Santander que solicitou a inclusão do campo 09/06/2020 1.0.1 “Protocolo” no objeto “ErroDebito”. Houve SERPRO-SANTANDER concordância na alteração por parte do Serpro por ser um pequeno ajuste e necessário. Alteração no item “a” da 7. Regras de negócio: Antes tinha sido definido que “Esse número somente poderá ser utilizado novamente quando não houver resposta da Instituição 24/08/2020 1.0.2 SERPRO Financeira, como por exemplo time out;” Por questão de melhoria na implementação o número de protocolo não poderá ser reutilizado.

Modelo padrão de pagamento online Página 3

(Fl. 4 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) Sumário 1.Introdução .................................................................................................................................. 6

2.Premissas.................................................................................................................................... 7

3.Arquitetura de Integração das Aplicações ................................................................................. 8

3.1Especificações técnicas ....................................................................................................... 8

3.1.1Sistemas ...................................................................................................................... 8

3.1.2Comunicação ............................................................................................................... 9

3.2Segurança ............................................................................................................................ 9

4.Documentação do serviço ........................................................................................................ 10

4.2Efetuar Débito ................................................................................................................... 10

4.2.1Objeto da Requisição - RequisicaoDebito ................................................................. 11

4.2.2Objeto de Resposta ................................................................................................... 12

4.2.2.1Resposta Débito ................................................................................................ 12

4.2.2.2Erro Débito ........................................................................................................ 12

4.2.3Respostas HTTP ......................................................................................................... 13

4.2.4Cenários de uso ......................................................................................................... 13

4.2.4.1Requisição exemplo .......................................................................................... 13

4.2.4.2Resposta: Débito realizado com sucesso .......................................................... 14

4.2.4.3Resposta: Protocolo duplicado ......................................................................... 14

4.2.4.4Resposta: Erros nos dados do débito ................................................................ 15

4.2.4.5Resposta: Erros nos dados do débito e nos códigos de barras ......................... 15

4.2.4.6Resposta: Erros em todos os códigos de barras ............................................... 16

4.3Consultar Débito ............................................................................................................... 17

4.3.1Respostas HTTP ......................................................................................................... 17

4.3.2Cenários de uso ......................................................................................................... 17

4.3.2.1Requisição exemplo .......................................................................................... 17

4.3.2.2Resposta: Débito encontrado ........................................................................... 17

4.3.2.3Resposta: Número do protocolo inválido ......................................................... 18

4.3.2.4Resposta: Número do protocolo inexistente .................................................... 18

Modelo padrão de pagamento online Página 4

(Fl. 5 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) 5.Tabela de mensagens ............................................................................................................... 19

6.Roteiro para Desenvolvimento e Implantação da solução ...................................................... 20

6.1Configuração da comunicação e segurança ...................................................................... 20

7.Regras de Negócio.................................................................................................................... 21

ANEXO I: Contrato no formato OpenAPI..................................................................................... 23

ANEXO II: Arquivo do Contrato no formato OpenAPI ................................................................. 24

Modelo padrão de pagamento online Página 5

(Fl. 6 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) 1. Introdução Este documento tem por objetivo definir as especificações e os critérios técnicos necessários para integração online, por meio de API, entre Instituições autorizadas a funcionar pelo Banco Central do Brasil e a Receita Federal para realização de pagamento de documentos de arrecadação com código de barras, padrão Febraban, pela internet, através de débito online em conta corrente com autorização prévia e única, assim, sem necessidade de autenticação.

Modelo padrão de pagamento online Página 6

(Fl. 7 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) 2. Premissas Para atender ao serviço que está sendo definido neste manual, será necessário que a conexão Receita Federal com a internet fique estabelecida 24 horas por dia e sete dias por semana.

A Receita Federal e as Instituições Financeiras deverão registrar log de todas as transações para futuras consultas e respostas a questionamentos.

Havendo falha de comunicação entre a Instituição Financeira e a Receita Federal, o processo de contingência será discutido entre as partes em momento futuro.

Tanto no recebimento do DARF Numerado, quanto da GNRE, deverão ser mantidas as consistências atuais, conforme o modelo do documento que estiver sendo criticado.

A utilização desses serviços deve ser precedida da formalização de contrato entre as Instituições e a Receita Federal, onde serão formalizadas as condições negociais de prestação de serviço e a responsabilidade de cada uma das partes quanto ao custeio e desenvolvimento desta solução.

Modelo padrão de pagamento online Página 7

(Fl. 8 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) 3. Arquitetura de Integração das Aplicações O processo de integração das aplicações foi definido pela Febraban em conjunto com a Receita Federal do Brasil e o Serpro, tendo como objetivos principais:

• Padronizar a forma de integração entre os sistemas de informação das entidades envolvidas;

• Fornecer máxima segurança nas operações de pagamento via débito online, garantindo a autenticidade, confidencialidade, integridade e não repúdio;

• Disponibilizar um serviço eletrônico moderno, eficiente e confiável, com bom desempenho e alta disponibilidade.

3.1 Especificações técnicas Esta seção define as especificações técnicas de cada elemento que compõe a arquitetura de integração das aplicações.

3.1.1 Sistemas Os sistemas devem trocar informações no modelo computacional cliente-servidor. O sistema DARA desempenhará o papel de sistema cliente, ou seja, o sistema que solicita o débito, enquanto os sistemas dos bancos realizarão o papel de sistema servidor, ou seja, os sistemas atendem à solicitação de realização de débito online.

O diagrama a seguir ilustra de modo simplificado o modelo de integração:

Este documento especifica a integração entre o sistema DARA/RFB e os sistemas dos bancos conveniados. Vale salientar que a integração entre os sistemas clientes e o DARA ocorre somente no âmbito da RFB/Serpro.

Inicialmente, os sistemas envolvidos na integração são:

Entidade Sistema Descrição Débito Online da Rede Arrecadadora: aplicação Web DARA que realiza o processo de pagamento de documentos RFB de arrecadação via débito online. SISTEMAS Sistemas internos ao ambiente RFB/SERPRO que CLIENTES DO necessitam utilizar os serviços de débito em conta do

Modelo padrão de pagamento online Página 8

(Fl. 9 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) DARA DARA. Aplicações dos bancos conveniados, responsáveis por Bancos Aplicações Web realizar pagamento eletrônico via débito online.

3.1.2 Comunicação Esta seção define os padrões relacionados ao envio e recebimento dos dados.

Diferente do modelo de integração anterior utilizado entre os sistemas clientes do DARA e os sistemas dos bancos, que utilizava a transferência de arquivos texto como estilo de integração padrão, o modelo atual trabalha com chamadas de procedimento remoto. Os dados serão enviados e recebidos via serviços Web e será adotado o estilo arquitetural REST (Representational State Transfer) na construção dos serviços Web.

A tabela abaixo lista os padrões de comunicação definidos para a integração das aplicações:

Componente Especificação Observação Tipo de Comunicação Síncrona Protocolo HTTP v1.1 RFC 2616 Formato dos dados JSON RFC 7159 API do serviço Web OpenAPI v3.0.2

Os serviços Web a serem disponibilizados pelos sistemas dos bancos bem como os dados de entrada e saída estão definidos na seção Documentação do serviço.

3.2 Segurança Para participar da solução, o meio de comunicação deve ser via internet utilizando conexão criptografada via https (HyperText Transfer Protocol Secure). O certificado digital deve ser do tipo A1 para autenticação mútua, a fim de garantir a Confidencialidade1, Integridade2 e Autenticidade3 dos dados trafegados.

O certificado deve ser emitido por Autoridade Certificadora credenciada pela Infraestrutura de Chaves Públicas Brasileira – ICP-Brasil, devendo conter o CNPJ da pessoa jurídica titular do Certificado digital no campo otherName OID=2.16.76.1.3.3 e ter a extensão Extended Key Usage com permissão de “Autenticação Cliente”.

Obs:

• Quanto às mensagens criptografadas, o protocolo TLS 1.2 utilizado pelo HTTPS garante a autenticidade e a criptografia dos dados da mensagem.

• TLS: É obrigatório o uso de TLS 1.2 na comunicação com a API. SSL, TLS 1.0 e 1.1 não são

Confidencialidade: Apenas o destinatário-alvo tem acesso ao seu conteúdo. 2 Integridade: A mensagem é recebida sem modificações. 3 Autenticidade: A origem da mensagem pode ser verificada.

Modelo padrão de pagamento online Página 9

(Fl. 10 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) suportados. Integrações utilizando esses protocolos não poderão realizar transações.

• Restrição de Ips: O consumo dos serviços Web disponibilizados pelos bancos deve estar restrito somente aos IP’s do sistema cliente DARA/RFB.

• Distinguished Name (DN): O consumo dos serviços Web disponibilizados pelos bancos deve estar restrito somente ao certificado cujo DN corresponda ao do Sistema DARA.

• Chave do Certificado: A chave do certificado deverá ser no mínimo de 2048 bits.

O certificado tem por finalidade evitar consequências negativas no âmbito pessoal, financeiro e/ou legal, se os dados forem interceptados e fraudados por terceiros, vindo a serem aceitos como válidos.

As alterações referentes ao certificado de servidor deverão ser previamente comunicadas as Instituições, com antecedência mínima de 30 (trinta) dias úteis. Caberá a Receita Federal e às Instituições Financeiras manterem controle do prazo de vencimento do certificado A1, sua renovação e arcar com os custos envolvidos.

4. Documentação do serviço O serviço “debitoOnline”, para a realização de débitos está documentado por meio do arquivo .yaml (Ain’t Markup Language) onde estão definidas suas operações e mensagens. O arquivo do contrato no formato OpenAPI encontra-se no anexo II deste documento.

4.1 Endpoints dos serviços O endpoint4 proposto para os serviços é:

➢ https://<site\_banco>/rfb/tributos/v<numero\_versao\_servicoBanco>/debitos

onde somente <site\_banco> é a parte variável do endpoint.

Exemplos: https://www.bb.com.br/pbb/rfb/tributos/v1/debitos https://www.itau.com.br/api/servicos/rfb/tributos/v1/debitos https://banco.bradesco/html/classic/rfb/tributos/v1/debitos https://www.santander.com.br/rfb/tributos/v1/debitos https://corporateportal.brazil.citibank.com/rfb/tributos/v1/debitos

4.2 Efetuar Débito O serviço realiza o pagamento de um até 5 (cinco) documentos de arrecadação com código de barras, layout padrão Febraban, através de débito online em conta corrente, com autorização prévia e única, assim, sem necessidade de autenticação.

Neste fluxo, a RFB informará os detalhes do débito: referência do débito (número fornecido pelo sistema cliente do DARA), número de protocolo (número fornecido pelo DARA), código do banco, código da agência, conta corrente, CPF do usuário, CPF/CNPJ do contribuinte, espécie de

4 Endpoint: é a URL onde seu serviço pode ser acessado por uma aplicação cliente.

Modelo padrão de pagamento online Página 10

(Fl. 11 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) débito, data da requisição, hora da requisição e código de barras de 44 posições (layout padrão Febraban versão 5). Esses dados representam o objeto da requisição do item 4.2.1. Neste momento o banco deverá responder à operação com os dados de resposta descritos no objeto “RespostaDebito” conforme item 4.2.2.1. Outros dados podem ser retornados no caso de algum impedimento os quais estão descritos no objeto “ErroDebito” conforme item 4.2.2.2.

Obs. 1.: Na eventualidade de envio pelo sistema de mais de 5 barras, o débito não será efetivado para nenhuma das barras, devendo ser criado um domínio específico com esse código de erro.

Obs. 2.: Em qualquer hipótese, não haverá estorno dos débitos efetivados.

4.2.1 Objeto da Requisição - RequisicaoDebito Objeto da requisição que contém os dados do débito a ser efetuado. Adicionalmente na requisição, deve-se incluir um campo no cabeçalho HTTP contendo um carimbo de data/hora da solicitação em milisegundos. O servidor comparará o registro de data e hora atual com o registro de data e hora da solicitação e só aceitará a solicitação se estiver dentro de um período de tempo permitido de 10 segundos, fazendo-se necessário que os equipamentos envolvidos na comunicação estejam sincronizados com a Hora Legal Brasileira.

Campo Tipo Padrão Descrição protocolo\* String(18) ^\d{18}$ Identificador do protocolo do DARA. codigoBanco\* String(3) ^\d{3}$ Código do banco (CNC). codigoAgencia\* String(4) ^\d{4}$ Código da agência (sem DV). contaCorrente\* String(16) ^\w{2,16}$ Conta corrente para débito (com DV). cpfUsuario\* String(11) ^\d{11}$ CPF do usuário. Ex: despachante aduaneiro representante do importador, contador do contribuinte do imposto de renda, etc. contribuinte\* Object CNPJ ou CPF do contribuinte, contendo os campos tipo e ni, descritos abaixo. • tipo\* Enum 01, 02 Identificador do NI do contribuinte. 01 = CPF 02 = CNPJ • ni\* ^(\d{11}|\d{14})$ NI do contribuinte. especieDebito\* Enum 01 Espécie de débito. 01 = PUCOMEX. ReferenciaDebito String(19) ^\w{19}$ Número de referência do débito \* (único) no sistema de origem. Ex: Para o PUCOMEX , será informado o número da DUIMP\*.

\*(Ver letra l do item 7.Regras de Negócio)

dataRequisicao\* String(8) ^\d{8}$ Data da requisição (AAAAMMDD). horaRequisicao\* String(6) ^\d{6}$ Hora da requisição (HHMMSS).

Modelo padrão de pagamento online Página 11

(Fl. 12 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) codigosBarra\* Array(1..5) Lista de 1 até 5 códigos de barras (String (44)) de DARFs numerados, GNREs e demais receitas da RFB. \* Campos obrigatórios

4.2.2 Objeto de Resposta 4.2.2.1 Resposta Débito Em resposta à requisição de débito, caso a mesma não apresente nenhum problema que impeça a leitura e processamento do pagamento de todos os códigos de barra enviados na requisição, os serviços de débito providos pelos bancos realizarão o pagamento de todos os documentos e retornarão um objeto RespostaDebito. Esse objeto retornará o mesmo número de protocolo que foi passado previamente para a operação de débito e uma lista representando o resultado da operação contendo todos os documentos/códigos de barras processados.

Segue a definição do formato do objeto RespostaDebito:

Campo Tipo Padrão Descrição protocolo\* String(18) ^\d{18}$ Identificador do protocolo do DARA.

codigosBarraSucesso Array(1..5) Lista de códigos de barra cujo débito ocorreu com sucesso, contendo os campos: codigoBarra, numeroAutenticacao, dataTransacao, horaTransacao e dataArrecadacao.

• codigoBarra\* String(44) ^\d{44}$ Código de barras.

• numeroAutenticacao\* String(23) ^\w{23}$ Número da autenticação. Deverá ser o mesmo número informado no arquivo retorno D+1.

• dataTransacao\* String(8) ^\d{8}$ Data da transação (AAAAMMDD).

• horaTransacao\* String(6) ^\d{6}$ Hora da transação (HHMMSS).

• dataArrecadacao\* String(8) ^\d{8}$ Data da arrecadação (AAAAMMDD). Data do débito na conta. \* Campos obrigatórios

4.2.2.2 Erro Débito Em resposta à requisição de débito, caso a mesma apresente algum problema que impeça a leitura ou processamento de pelo menos um documento enviado, os serviços de débito providos pelos bancos não realizarão o pagamento de nenhum dos documentos enviados e retornarão um objeto ErroDebito. Esse objeto retornará uma lista de erros contendo o campo, o valor, o código e a descrição dos impedimentos retornados pelo banco referente aos problemas encontrados na operação correspondente ao protocolo que foi passado para a operação de débito. Segue a definição do objeto e o formato dos campos que compõem os itens da lista:

Modelo padrão de pagamento online Página 12

(Fl. 13 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.)

Campo Tipo Padrão Descrição protocolo\* String(18) ^\d{18}$ Identificador do protocolo do DARA.

Lista de erros retornados da instituição erros Array(1..n) financeira contendo os campos: “campo”, “valor”, “codigo” e “descrição”. Nome do campo com erro. Os valores devem • campo String respeitar os nomes dos campos existentes no objeto RequisicaoDebito.

• valor String Valor do campo enviado na requisição.

• codigo\* String(2) ^\d{2}$ Código de retorno do erro (Veja tabela 5.1).

• descricao String Descrição do erro.

\* Campos obrigatórios

4.2.3 Respostas HTTP

Código Tipo do retorno Descrição 201 RespostaDebito Requisição de débito processada. 400 - Corpo da requisição inválido (JSON inválido ou inexistente) ou Requisição chegou com atraso acima do permitido – (10 segundos) 401 - Certificado não informado, inválido ou expirado. 422 ErroDebito Erro de processamento do débito. 429 - Número de requisições excedeu o limite. 500 - Erro interno/infraestrutura no servidor.

4.2.4 Cenários de uso Alguns cenários podem ser observados a partir de uma requisição de débito.

4.2.4.1 Requisição exemplo POST /v1/debitos

Headers: Accept application/json

Payload:

{

"protocolo": "999000000000000001",

"codigoBanco": "999",

Modelo padrão de pagamento online Página 13

(Fl. 14 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) "codigoAgencia": "9999",

"contaCorrente": "9999999999999999",

"cpfUsuario": "99999999999",

"contribuinte": {

"tipo": "01",

"ni": "99999999999"

},

"especieDebito": "01",

"referenciaDebito": "0000000001",

"dataRequisicao": "20191128",

"horaRequisicao": "153820",

"codigosBarra": [

"11111111111111111111111111111111111111111111",

"22222222222222222222222222222222222222222222",

"33333333333333333333333333333333333333333333",

"44444444444444444444444444444444444444444444",

"55555555555555555555555555555555555555555555"

]

}

4.2.4.2 Resposta: Débito realizado com sucesso Status: 201

Headers: Location /v1/debitos/999000000000000001

Content-Type application/json

date 1508484583259

Payload:

{

"protocolo": "999000000000000001",

"codigosBarraSucesso": [

Modelo padrão de pagamento online Página 14

(Fl. 15 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) {

"codigoBarra": "11111111111111111111111111111111111111111111",

"numeroAutenticacao": "11111111111111111111111",

"dataTransacao": "20191128",

"horaTransacao": "153820",

"dataArrecadacao": "20191128"

},

{

"codigoBarra": "22222222222222222222222222222222222222222222",

"numeroAutenticacao": "22222222222222222222222",

"dataTransacao": "20191128",

"horaTransacao": "153820",

"dataArrecadacao": "20191128"

},

{

"codigoBarra": "33333333333333333333333333333333333333333333",

"numeroAutenticacao": "33333333333333333333333",

"dataTransacao": "20191128",

"horaTransacao": "153820",

"dataArrecadacao": "20191128"

},

{

"codigoBarra": "44444444444444444444444444444444444444444444",

"numeroAutenticacao": "44444444444444444444444",

"dataTransacao": "20191128",

"horaTransacao": "153820",

"dataArrecadacao": "20191128"

},

{

Modelo padrão de pagamento online Página 15

(Fl. 16 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) "codigoBarra": "55555555555555555555555555555555555555555555",

"numeroAutenticacao": "55555555555555555555555",

"dataTransacao": "20191128",

"horaTransacao": "153820",

"dataArrecadacao": "20191128"

}

]

}

4.2.4.3 Resposta: Protocolo duplicado Status: 422 Headers: Content-Type application/json Payload: { "protocolo": "999999999999999999",

"erros": [ {

"campo": "protocolo",

"valor": "999000000000000001",

"codigo": "05",

"descricao": "Número do protocolo duplicado."

}

]

}

4.2.4.4 Resposta: Erros nos dados do débito Status: 422 Headers: Content-Type application/json Payload: { "protocolo": "999999999999999999",

"erros": [ {

"campo": "codigoAgencia",

"valor": "9999",

Modelo padrão de pagamento online Página 16

(Fl. 17 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) "codigo": "02",

"descricao": "Código de agência inexistente."

},

{

"campo": "cpfUsuario",

"valor": "99999999999",

"codigo": "01",

"descricao": "CPF do usuário inválido."

}

]

}

4.2.4.5 Resposta: Erros nos dados do débito e nos códigos de barras Status: 422 Headers: Content-Type application/json Payload: { "protocolo": "999999999999999999",

"erros": [ {

"campo": "cpfUsuario",

"valor": "99999999999",

"codigo": "01",

"descricao": "CPF do usuário inválido."

},

{

"campo": "codigosBarra",

"valor": "33333333333333333333333333333333333333333333",

"codigo": "01",

"descricao": "Código de barras inválido."

},

{

Modelo padrão de pagamento online Página 17

(Fl. 18 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) "campo": "codigosBarra",

"valor": "44444444444444444444444444444444444444444444",

"codigo": "05",

"descricao": "Código de barras duplicado."

}

]

}

4.2.4.6 Resposta: Erros em todos os códigos de barras Status: 422 Headers: Content-Type application/json Payload: { "protocolo": "999999999999999999",

"erros": [ {

"campo": "codigosBarra",

"valor": "11111111111111111111111111111111111111111111",

"codigo": "01",

"descricao": "Código de barras inválido."

},

{

"campo": "codigosBarra",

"valor": "22222222222222222222222222222222222222222222",

"codigo": "05",

"descricao": "Código de barras duplicado."

},

{

"campo": "codigosBarra",

"valor": "33333333333333333333333333333333333333333333",

"codigo": "01",

"descricao": "Código de barras inválido."

Modelo padrão de pagamento online Página 18

(Fl. 19 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) },

{

"campo": "codigosBarra",

"valor": "44444444444444444444444444444444444444444444",

"codigo": "05",

"descricao": "Código de barras duplicado."

},

{

"campo": "codigosBarra",

"valor": "55555555555555555555555555555555555555555555",

"codigo": "05",

"descricao": "Código de barras duplicado."

}

]

}

Modelo padrão de pagamento online Página 19

(Fl. 20 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) 4.3 Consultar Débito Consulta débito online realizado anteriormente através do número do protocolo DARA. O mesmo será passado na própria url de chamada do serviço.

Exemplo: https://<site banco>/rfb/tributos/v<numero\_da\_versao\_servico do banco>/debitos/{protocolo}

4.3.1 Respostas HTTP Caso exista na base algum débito com o número de protocolo passado na requisição seus dados serão retornados conforme abaixo:

Código Tipo do retorno Descrição 200 RespostaDebito Consulta do débito realizada com sucesso. 401 - Certificado não informado, inválido ou expirado. 404 ErroDebito Débito não encontrado para o protocolo especificado. 429 - Número de requisições excedeu o limite. 500 - Erro interno/infraestrutura no servidor.

4.3.2 Cenários de uso Alguns cenários podem ser observados a partir de uma requisição de consulta.

4.3.2.1 Requisição exemplo GET /v1/debitos/999000000000000001

Headers: Accept application/json

4.3.2.2 Resposta: Débito encontrado Status: 200

Headers: Content-Type application/json

Payload:

{

"protocolo": "999000000000000001",

"codigosBarraSucesso": [

{

"codigoBarra": "11111111111111111111111111111111111111111111",

"numeroAutenticacao": "11111111111111111111111",

"dataTransacao": "20191128",

Modelo padrão de pagamento online Página 20

(Fl. 21 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) "horaTransacao": "153820",

"dataArrecadacao": "20191128"

},

{

"codigoBarra": "22222222222222222222222222222222222222222222",

"numeroAutenticacao": "22222222222222222222222",

"dataTransacao": "20191128",

"horaTransacao": "153820",

"dataArrecadacao": "20191128"

},

{

"codigoBarra": "33333333333333333333333333333333333333333333",

"numeroAutenticacao": "33333333333333333333333",

"dataTransacao": "20191128",

"horaTransacao": "153820",

"dataArrecadacao": "20191128"

},

{

"codigoBarra": "44444444444444444444444444444444444444444444",

"numeroAutenticacao": "44444444444444444444444",

"dataTransacao": "20191128",

"horaTransacao": "153820",

"dataArrecadacao": "20191128"

},

{

"codigoBarra": "55555555555555555555555555555555555555555555",

"numeroAutenticacao": "55555555555555555555555",

"dataTransacao": "20191128",

"horaTransacao": "153820",

Modelo padrão de pagamento online Página 21

(Fl. 22 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) "dataArrecadacao": "20191128"

}

]

}

4.3.2.3 Resposta: Número do protocolo inválido Status: 422

Headers: Content-Type application/json

Payload:

{ "protocolo": "999999999999999999",

"erros": [

{

"campo": "protocolo",

"valor": "99999999999999999X",

"codigo": "01",

"descricao": "Número do protocolo inválido."

}

]

}

4.3.2.4 Resposta: Número do protocolo inexistente Status: 422

Headers: Content-Type application/json

Payload:

{ "protocolo": "999999999999999999",

"erros": [

{

"campo": "protocolo",

"valor": "999999999999999999",

"codigo": "02",

"descricao": "Número do protocolo inexistente."

Modelo padrão de pagamento online Página 22

(Fl. 23 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) }

]

}

Modelo padrão de pagamento online Página 23

(Fl. 24 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) 5. Tabela de mensagens As mensagens de erros que serão devolvidas pelo serviço são as definidas pela FEBRABAN junto com as instituições financeiras, constantes na tabela de mensagens.

5.1 Tabela de mensagens - Retorno de erro da operação (ErroDebito) Código Mensagens 01 {campo\*} inválido(a). \*Ex: Banco, Agência, Conta Corrente, CPF do usuário, Tipo Cpf/Cnpj do contribuinte, CPF/CNPJ do contribuinte 02 {campo\*} inexistente. \* Ex: Agência, Conta Corrente 03 {campo\*} não autorizado. \* Ex: CpfUsuario 04 Saldo insuficiente 05 {campo\*} duplicado \* Ex: Código de Barras 06 Convênio não ativo no Banco. 07 Número do protocolo DARA já existente na base de dados\*.

\* No caso de um débito tentar usar um protocolo já utilizado por outra operação 08 Requisição com total de códigos de barra superior a cinco. 99 Outros

Modelo padrão de pagamento online Página 24

(Fl. 25 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) 6. Roteiro para Desenvolvimento e Implantação da solução As Instituições Financeiras e a RFB devem implementar os serviços Web seguindo a especificação da API de Débito Online definido neste documento.

Após o desenvolvimento dos serviços Web, a Instituição Financeira e a RFB definirão a agenda de testes. Nesta fase, a Instituição Financeira deverá informar o endpoint do serviço Web de testes, disponibilizado em um ambiente que simula o ambiente de produção, especialmente criado para testes de integração. Neste ambiente, a RFB deverá executar o plano de testes. A Instituição Financeira também deverá disponibilizar uma massa de testes que possibilite a execução dos diversos cenários de testes necessários para validação da solução.

Após a realização de testes e homologação da solução e, estando validados todos os aspectos inerentes a estrutura de comunicação e a segurança, a Instituição Financeira em conjunto com a RFB definirão a data para implantação da solução em ambiente de produção.

6.1 Configuração da comunicação e segurança O padrão de segurança e comunicação entre as Instituições Financeiras e a Receita Federal foi definido no item 3 deste documento.

Para a configuração da infraestrutura de comunicação dos ambientes de testes e produção, a RFB e as Instituições Financeiras deverão informar os dados de IP e porta para o devido cadastramento das regras de firewall em ambos os lados da integração.

Para a configuração da segurança via certificado digital no ambiente produtivo, a RFB e as Instituições Financeiras deverão disponibilizar as chaves públicas e informar o Distinguished Name (DN) para devida configuração de segurança em ambos os lados da integração. No ambiente de homologação, a RFB e as Instituições Financeiras deverão utilizar certificados digitais de homologação emitidos por uma CA credenciada ao ICP-BRASIL. No ambiente de testes, é possível também a utilização de certificados digitais auto-assindados desde que atendam aos requisitos dispostos no item 3.2.

Modelo padrão de pagamento online Página 25

(Fl. 26 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) 7. Regras de Negócio

a) Análise do número do protocolo: No caso de não haver resposta da Instituição Financeira numa operação de débito (time out), esse número não poderá ser utilizado novamente pelo sistema cliente. Nesse caso o sistema cliente deverá reenviar as mesmas informações, porém o protocolo deverá ser um novo e não o mesmo;

b) A validação do convênio, a ser realizada pelo Banco, deverá preceder a consulta do saldo.

c) O novo sistema, de início, contemplará o DARF numerado. O recebimento de GNRE ocorrerá de acordo com a implantação do sistema por cada Secretaria de Fazenda Estadual - Sefaz.

d) No caso de insuficiência de saldo, o banco não efetuará qualquer débito, retornando como insuficiência de saldo.

e) Bancos entendem que deve ser mantido o envio do arquivo consolidado da arrecadação à Receita Federal, sendo que poderá ter acréscimo, mas não estorno. O consolidado será o arquivo que baseará o repasse financeiro pelas Instituições Financeiras para a Receita Federal. Somente constará o registro G e sem os insucessos.

f) No caso de pagamento de DARF, a Instituição Financeira efetua o repasse financeiro à Receita Federal dentro dos prazos estabelecidos em contrato.

g) No caso de pagamento de GNRE, a Instituição Financeira presta contas de informação e repasse financeiro de acordo com o contrato com cada Estado.

h) Neste modelo de integração não haverá estorno em qualquer hipótese.

i) Espera-se que o tempo médio de resposta de uma requisição seja de 2 a 3 segundos. Caso não haja retorno algum após 10 segundos será considera uma situação de timeout.

j) Para se evitar erros no acolhimento do DARF numerado, que o pagamento seja efetuado após o fechamento da arrecadação do dia no banco, a data de limite de acolhimento (data de arrecadação) poderá ser um dia útil anterior ou um dia útil seguinte à data da operação.

k) As consistências que hoje, já são realizadas no campo livre da barra, continuarão sendo realizados normalmente. No caso das barras de DARFs Numerados, a barra inteira é consistida.

l) Deverá ser considerado o campo referenciaDebito para composição do extrato do cliente. No caso da DUIMP, o valor do campo referenciaDebito terá o formato: AABRSSSSSSSSSSDNNNN, onde a parte referente ao sequencial SSSSSSSSSS que possui tamanho de 10 caracteres é o mínimo a ser utilizado na composição do extrato no caso de limitação da instituição financeira em exibir os 19 caracteres. Também pode ser mostrado o dígito verificador D e o sequencial que representa a versão do documento NNNN.

m) A barra será considerada duplicada quando já estiver sido paga por outro protocolo:

Modelo padrão de pagamento online Página 26

(Fl. 27 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.) ⚫ Primeira tentativa o Banco recolheu, tentou responder, porém ocorreu timeout; ⚫ Caso ocorra nova tentativa com protocolo diferente e mesma barra, o Banco responde como “barra duplicada”.

Modelo padrão de pagamento online Página 27

(Fl. 28 do Anexo Único ao Ato Declaratório Executivo Codar nº 4, de 1º de setembro de 2020.)

ANEXO I: Arquivo do Contrato no formato OpenAPI O arquivo que define o contrato está anexado abaixo como um objeto OLE. Para visualização completa do arquivo é necessário clicar e entrar no objeto OLE.

openapi: 3.0.2 info: title: Débito Online description: |-

Modelo padrão de arrecadação online via webservice Página 28

