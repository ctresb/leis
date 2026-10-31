---
titulo: "Ato Declaratório Executivo Coana nº 11, de 10 de outubro de 2018"
orgao: "Coordenação-Geral de Administração Aduaneira"
tipo: "Ato Declaratório Executivo"
numero: "11"
data: "2018-10-10"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 23/10/2018, seção 1, página 19"
data_publicacao: "2018-10-23"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/95908/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/95908/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "95908"
sha256_texto: "016710afbd4e34864e37e19d67770f1359751322f843eda9314694284d0e7642"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Coana nº 11, de 10 de outubro de 2018

Revoga o Ato Declaratório Executivo Coana nº 4, de 19 de março de 2018, e estabelece o novo modelo de dados contendo as informações, especificações e requisitos técnicos necessários à integração dos sistemas próprios das lojas francas com os serviços da Receita Federal do Brasil para as Lojas Francas de Fronteira.

O COORDENADOR-GERAL DE ADMINISTRAÇÃO ADUANEIRA, no uso da atribuição que lhe confere o inciso II do art. 334 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 430, de 9 de outubro de 2017, e tendo em vista o disposto no art. 23 da Portaria MF nº 307, de 17 de julho de 2014, e no artigo 32, inciso III, da Instrução Normativa 1799, de 16 de março de 2018, declara:

**Art. 1º** As informações, especificações e requisitos técnicos necessários para a integração dos sistemas próprios das lojas francas com os serviços da Receita Federal do Brasil para as Lojas Francas de Fronteira são os constantes do anexo único deste Ato Declaratório Executivo.

**Art. 2º** Fica revogado o Ato Declaratório Executivo Coana nº 4, de 19 de março de 2018.

**Art. 3º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

JACKSON ALUIR CORBARI

ANEXO ÚNICO

a

ANEXO ÚNICO

MODELO DE DADOS - LOJA FRANCA

API - Loja Franca de Fronteira

Documentação para o consumo dos serviços das Lojas Francas de Fronteira

Receita Federal do Brasil

Versão 1.0

Introdução

Todos os serviços seguem o mesmo protocolo de acesso, baseado nas instruções de uso e contratação do serviço API Serpro. A API do Loja Franca de Fronteira foi desenvolvida baseada na arquitetura REST. Ela trabalha exclusivamente com o formato JSON.

A API usa o formato UTF-8.

A URL base da API do ambiente de Validação é https://apigateway.serpro.gov.br/loja-franca-hom/api, o endereço da produção é https://apigateway.serpro.gov.br/loja-franca/api (usaremos a tag <url> para referenciá-las).

Autenticação

Para garantir a identificação e a segurança da origem da informação, toda requisição a API deve seguir três processos:

1. Assinar a requisição com o seu conteúdo anexado mediante a utilização do certificado digital A1 e-CNPJ (cadeia ICP Brasil) da contratante;

2. Submeter a mensagem assinada mediante a apresentação da chave de acesso da API gateway válida (gerada a partir das credencias disponibilizadas no portal do cliente para cada CNPJ) e

3.Verificar a assinatura da requisição, checando se o certificado é válido e não revogado.

Assim, a cada requisição realizada, haverá Validação de Origem que realizará o batimento entre o CNPJ Comercial (CNPJ vinculado as credencias do portal do cliente), CNPJ de Autenticidade (CNPJ assinante da requisição) garantido a irretratabilidade (não repúdio) no nível em cada requisição.

Contratação

Para consumir a API, é necessário utilizar as credenciais de acesso - Consumer Key e Consumer Secret - disponibilizados no portal do Cliente (https://minhaconta.serpro.gov.br). Esses códigos servem para identificar o contrato.

Exemplos de código:

Consumer Key: djaR21PGoYp1iyK2n2ACOH9RedUb

Consumer Secret: ObRsAJWOL4fv2Tp27D1vd8fB3Ote

Token de Acesso (Bearer)

Para consultar a API, é necessário obter um token de acesso temporário (Bearer). Esse token possui um tempo de validade e sempre que expirado, este passo de requisição de um novo token de acesso deve ser repetido.

Para solicitar o token temporário, é necessário realizar uma requisição HTTP POST para o endpoint Token (https://apigateway.serpro.gov.br/token), informando as credenciais de acesso no formato consumerKey:consumerSecret no HTTP Header Authorization, no formato base64.

Após isso feito, será gerada uma chave hash (Bearer token) que deverá ser passada no header das requisições que serão efetuadas. Este header segue o seguinte formato:

Authorization: Bearer <hash>

Payload

Todo o conteúdo a ser enviado para a API do Loja Franca deverá ser o assinado.

A assinatura da mensagem JSON deve ser feita com o uso de um certificado digital Pessoa Jurídica A1, seguindo o padrão das políticas do ICP-Brasil para assinatura digital com referência básica no formato CMS versão 2.2, com algoritmo SHA256WithRSAEncryption.

Para maiores informações, consulte o documento com os requisitos das políticas de assinatura digital na ICP- Brasil DOC-ICP-15.03.

Antes de enviar o conteúdo assinado, o mesmo deve seguir o Formato de mensagem JSON padrão.

Formato de mensagem JSON padrão

"servico": "// endpoint do serviço a ser chamado",

"dados": {

"// JSON de entrada de cada serviço"

A indicação de qual serviço será disparado se dará através do repasse do endpoint que representa cada serviço.

Exemplo de entrada a assinar

O JSON segue o formato documentado por operação e o mesmo fica encapsulado dentro da propriedade dados.

Por exemplo, para a operação Processa venda de viajante.

"servico": "/venda",

"dados" : {

"valorTotalItensImportados": 10,

"valorTotalItensNacionais": 0,

"valorCotacaoLoja": 3.24,

"viajanteParametro": {

"cpf": "00000000191",

"documento": {

"codigoPaisOrigem": 105,

"codigoTipo": 1,

"numero": "12345"

Exemplo de entrada assinada

Operação Processa venda de viajante.

Exemplo de formato do que deverá ser enviado para a API do Loja Franca.

POST https://apigateway.serpro.gov.br/loja-franca/api

HEADER

Authorization: Bearer 953bae789a1726734005d238e939c978

BODY/PAYLOAD

MIAGCSqGSIb3DQEHAqCAMIACAQExDzANBglghkgBZQMEAgMFADCABgkqhkiG9w0BBwEAAKCAMIIG6jCC BNKgAwIBAg

IDApVmMA0GCSqGSIb3DQEBCwUAMIGVMQswCQYDVQQGEwJCUjETMBEGA1UECgwKSUNQLUJyYXNpb DE7MDkGA1UECwwy

U2VydmljbyBGZWRlcmFsIGRlIFByb2Nlc3NhbWVudG8gZGUgRGFkb3MgLSBTRVJQUk8xNDAyBgNVBAMMK0 F1dG9yaW

RhZGUgQ2VydGlmaWNhZG9yYSBkbyBTRVJQUk8gRmluYWwgdjUwHhcNMTcwODAyMTI0OTA2WhcNMjAwO DAxMTI0OTA2

WjCBoTELMAkGA1UEBhMCQlIxEzARBgNVBAoMCklDUC1CcmFzaWwxGTAXBgNVBAsMEFBlc3NvYSBGaXN pY2EgQTMxET

APBgNVBAsMCEFSU0VSUFJPMSswKQYDVQQLDCJBdXRvcmlkYWRlIENlcnRpZmljYWRvcmEgU0VSUFJPQ UNGMSIwIAYD

VQQDDBlMVUlaIENBUkxPUyBTSUxWRUlSQSBIT1BGMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQ EAi8YM8

VcBZq7DImG6dov33SR

Formatos e tipos

Os seguintes tipos de dados são utilizados pela API do Loja Franca de Fronteira:

Tipo Descrição Formato

string Cadeia de caracteres

string - data String com formato de data yyyy-MM-dd

string - String com formato de data e hora yyyy-MM-ddTHH:mm:ss data/hora

integer Número inteiro que representa códigos e identificadores

number Número inteiro em situações que pode passar do valor 2^31-1

decimal Número fracionado, sempre com duas casas após o decimal, separado por Ex.: 123456789012.22 "." (Exceto cotação do dólar, que pode ter até 3 casas após o decimal).

Tratamento de erros

Erros de negócio

São erros disparados pela API do Loja Franca de Fronteira quando há uma discordância entre os parâmetros enviados e as regras de negócio estabelecidas para as lojas francas.

JSON de Erro

"erros": [

"codigo": integer,

"mensagem": "string"

]

A resposta HTTP será:

Status Code Descrição

422 Erro de negócio do Loja Franca

Atributos da resposta - Status code 422

Nome Descrição Tipo

codigo Código que identifica o erro integer

mensagem Mensagem de erro string

Exemplo de Erro de Negócio

"erros": [

"codigo": 9,

"mensagem": "cnpjLoja <cnpjLoja>00000000000000</cnpjLoja> não existe como Loja."

]

Erros de formatação

São erros disparados pela API do Loja Franca de Fronteira quando há uma discordância na formatação/tipo de dados sugeridos pelos parâmetros enviados.

A resposta HTTP será:

Status Code Descrição

400 Erro de formatação dos parâmetros enviados

Atributos da resposta - Status code 400

Nome Descrição Tipo

codigo Código que identifica o erro integer

mensagem Mensagem de erro string

Exemplo de Erro de Formatação

"erros": [

"codigo": 3,

"mensagem": "<tag>documento</tag> com tamanho ou

formato diferente da definição do serviço."

]

Independentemente do tipo de erro, as mensagens de erro podem conter uma <tag>, que visa facilitar o tratamento do erro caso a aplicação que esteja utilizando a API do Loja Franca de Fronteira queira fazer algum tratamento específico, como por exemplo, uma extração de parâmetros a partir de uma mensagem de erro.

Os erros que a API do Loja Franca de Fronteira dispara pode ser consultada na tabela de erros.

Consulta de cota

Retorna a cota disponível para um determinado viajante.

OBS.: Para Viajante Brasileiro, a identificação pelo número de documento de CPF é sempre obrigatória.

Parâmetros para Viajante (Brasileiro ou Estrangeiro) com CPF

Nome Descrição Tipo Local Detalhes

cpf CPF do Viajante string body Obrigatório

dataNascimento Data de nascimento do Viajante string body Obrigatório formato yyyy- MM-dd

Parâmetros para Viajante Estrangeiro

Nome Descrição Tipo Local Detalhes

documento Documento apresentado pelo documento body Obrigatório Viajante

codigoPaisOrigem Código do país de origem do integer body Obrigatório Viajante tabela de países

codigoTipo Código do tipo de documento integer body Obrigatório apresentado pelo Viajante tabela de tipos de documento

numero Número de identificação do string body Obrigatório

documento apresentado pelo Viajante

dataNascimento Data de nascimento do Viajante string body Obrigatório formato yyyy-MM-dd

nomeNoDocumento Nome do Viajante presente no string body Obrigatório documento apresentado

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

nomeViajante Nome do Viajante cadastrado no Loja Franca string

dataUltimaVenda Data da última Venda string formato yyyy-MM- ddTHH:mm:ss

valorSaldoCota Valor restante do saldo de cota decimal

saldoCotaProduto Saldo de cota de cada produto saldoCotaProduto

codigoProduto Código do produto integer tabela de produtos

quantidade Quantidade de produtos restantes na cota integer

SERVICO /viajante/cota

Exemplo de entrada - Viajante Brasileiro

"cpf": "00000000191",

"dataNascimento": "1980-01-01"

Exemplo de entrada - Viajante Estrangeiro

"documento": {

"codigoPaisOrigem": 1,

"codigoTipo": 1,

"numero": "12345",

"dataNascimento": "1980-01-01",

"nomeNoDocumento": "FULANO DE TAL"

Exemplo de resposta

"nomeViajante": "FULANO DE TAL",

"dataUltimaVenda": "2017-12-08T17:13:55",

"valorSaldoCota": 300.0,

"saldoCotaProduto": [

"codigoProduto": 1,

"quantidade": 10

]

Códigos de erros possíveis

13, 14, 15, 16, 52, 55, 57, 99, -99.

Consulta de viajante

Retorna o nome, a data de nascimento e a data da última venda de um determinado viajante.

Parâmetros para Viajante Brasileiro com CPF

Nome Descrição Tipo Local Detalhes

cpf CPF do Viajante string body Obrigatório

Parâmetros para Viajante Estrangeiro

Nome Descrição Tipo Local Detalhes

documento Documento apresentado pelo documento body Obrigatório Viajante

codigoPaisOrigem Código do país de origem do integer body Obrigatório Viajante tabela de países

codigoTipo Código do tipo de documento integer body Obrigatório apresentado pelo Viajante tabela de tipos de documento

numero Número de identificação do string body Obrigatório documento apresentado pelo Viajante

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

nomeViajante Nome do Viajante cadastrado no Loja Franca string

dataNascimento Data de nascimento do Viajante string formato yyyy-MM-dd

dataUltimaVenda Data da última Venda string formato

yyyy-MM-ddTHH:mm:ss

SERVICO /viajante/consulta

Exemplo de entrada - Viajante Brasileiro

"cpf": "00000000191"

Exemplo de entrada - Viajante Estrangeiro

"documento": {

"codigoPaisOrigem": 105,

"codigoTipo": 1,

"numero": "12345"

Exemplo de resposta

"nomeViajante": "FULANO DE TAL",

"dataUltimaVenda": "2017-12-08T17:13:55.765Z",

"dataNascimento": "1970-01-01"

Códigos de erros possíveis

15, 16, 55, 57, 99.

Consulta cotação do dólar

Retorna a cotação do dólar de uma determinada data.

Parâmetros

Nome Descrição Tipo Local Detalhes

dataCotacao Data da cotação a pesquisar string query Obrigatório formato yyyy-MM-dd

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

data Data da cotação retornada string formato yyyy-MM-dd

valorOficial Valor da cotação do dólar na data retornada decimal

SERVICO /cotacaoDolar?dataCotacao={dataCotacao}

Exemplo de entrada

// não tem parâmetros JSON, apenas por query string. Ver o endpoint acima.

Exemplo de resposta

"data": "2017-12-01",

"valorOficial": 3.1241

Códigos de erros possíveis

Processa venda de viajante

Efetua uma operação de processamento de venda.

OBS.: Para Viajante Brasileiro, a identificação pelo número de documento de CPF é sempre obrigatória. A identificação por documento é sempre obrigatória independentemente se o Viajante for Brasileiro ou Estrangeiro.

Parâmetros

Nome Descrição Tipo Local Detalhes

valorTotalItensImportados Valor total (em US$) decimal body Obrigatório quando de itens importados valorTotalItensNacionais não for na Venda para o informado ou for igual a 0. Viajante

valorTotalItensNacionais Valor total (em US$) decimal body Obrigatório quando de itens nacionais na valorTotalItensImportados não for Venda para o Viajante informado ou for igual a 0.

valorCotacaoLoja Valor da cotação do decimal body Obrigatório dólar oferecido pela loja franca

viajanteParametro Identificação do viajante body Obrigatório Viajante Formato segue os parâmetros da Consulta de viajante. documento é obrigatório para

brasileiros na venda (atributos codigoPaisOrigem, codigoTipo e numero).

produtosControleQuantitativo Representa a produtos body Obrigatório quando é registrada quantidade de uma venda com produtos produtos controlados controlados. presentes na Venda do Viajante

codigoProduto Código do produto integer body Obrigatório quando é registrada uma venda com produtos controlados. tabela de produtos

quantidade Quantidade de integer body Obrigatório quando é registrada produtos controlados uma venda com produtos presente na Venda controlados.

valorTotal Valor total destes decimal body Obrigatório quando é registrada produtos na Venda uma venda com produtos controlados.

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

idVenda Identificação do número da venda gerado pelo sistema string Loja Franca de Fronteira

dataHoraVenda Data do registro da venda string formato yyyy-MM- ddTHH:mm:ss

darf Darf gerado para pagamento do viajante caso exceda a darf Venda exceda a cota

numero Número do Darf gerado number

valor Valor do Darf a ser pago pelo viajante decimal

dataVencimento Data de vencimento do Darf string formato yyyy-MM-dd

codigoReceita Código da receita recolhida integer

pdf PDF do boleto do Darf gerado byte[] String encoded em base-64

SERVICO /venda

Exemplo de entrada - Venda para Viajante Brasileiro, sem produtos controlado

s{

"valorTotalItensImportados": 10,

"valorTotalItensNacionais": 0,

"valorCotacaoLoja": 3.24,

"viajanteParametro": {

"cpf": "00000000191",

"documento": {

"codigoPaisOrigem": 105,

"codigoTipo": 1,

"numero": "12345"

Exemplo de entrada - Venda para Viajante Estrangeiro, sem produtos controlados

"valorTotalItensImportados": 10,

"valorTotalItensNacionais": 50,

"valorCotacaoLoja": 3.24,

"viajanteParametro": {

"documento": {

"codigoPaisOrigem": 1,

"codigoTipo": 1,

"numero": "12345",

"dataNascimento": "1980-01-01",

"nomeNoDocumento": "FULANO DE TAL"

}Exemplo de entrada - Venda para Viajante Brasileiro, com produtos controlados

"valorTotalItensImportados": 10,

"valorTotalItensNacionais": 0,

"valorCotacaoLoja": 3.24,

"viajanteParametro": {

"cpf": "00000000191",

"documento": {

"codigoPaisOrigem": 105,

"codigoTipo": 1,

"numero": "12345"

},

"produtosControleQuantitativo": [{

"codigoProduto": 10,

"quantidade": 2,

"valorTotal": 5.3

},{

"codigoProduto": 1,

"quantidade": 1,

"valorTotal": 4.7

}]

Exemplo de resposta, sem Darf

"idVenda": "2017000000020992652",

"dataHoraVenda": "2017-12-11T17:27:41"

}Exemplo de resposta, com Darf

"idVenda": "2017000000020992653",

"dataHoraVenda": "2017-12-11T17:27:41",

"darf": {

"valor": 31.24,

"codigoReceita": 1258,

"numero": 7011734500514907,

"dataVencimento": "2017-12-12",

"pdf": "Base64EncodedString"

}Códigos de erros possíveis

13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 55, 56, 57.

Entrega venda para viajante

Efetua a operação de entrega de venda.

Parâmetros

Nome Descrição Tipo Local Detalhes

idVenda Identificação do número da venda gerado pelo string query Obrigatório sistema Loja Franca de Fronteira na operação Processa venda de viajante

notaFiscalSaida Número da Nota Fiscal de saída gerado pelo string query Obrigatório sistema gerador de nota fiscal

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

dataHoraEntrega Data e hora da entrega da venda para o string formato yyyy-MM-ddTHH:mm:ss Viajante

SERVICO /venda/entrega?idVenda={idVenda}&amp;notaFiscalSaida={notaFiscalSaida}

Exemplo de entrad

a// não tem parâmetros JSON, apenas por query string. Ver o endpoint acima.

Exemplo de resposta

"dataHoraEntrega": "2017-12-01T16:32:17"

}Códigos de erros possíveis

31, 32, 33, 34, 39, 41, 54.

Cancela venda de viajante

Efetua uma operação de cancelamento de venda.

Parâmetros

Nome Descrição Tipo Local Detalhes

idVenda Identificação do número da venda gerado pelo sistema Loja string query Obrigatório Franca de Fronteira na operação Processa venda de viajante

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

dataHoraCancelamento Data e hora do cancelamento da string formato yyyy-MM-ddTHH:mm:ss venda do Viajante

SERVICO /venda/cancelamento?idVenda={idVenda}

Exemplo de entrad

a// não tem parâmetros JSON, apenas por query string. Ver o endpoint acima.

Exemplo de resposta

"dataHoraCancelamento": "2017-12-01T16:32:17"

}Códigos de erros possíveis

31, 38, 39, 54.

Devolução parcial de venda

Efetua uma operação de devolução parcial de venda.

Parâmetros

Nome Descrição Tipo Local Detalhes

valorTotalItensImportados Valor total (em US$) de decimal body Obrigatório quando itens importados a valorTotalItensNacionais não devolver for informado ou for igual a 0.

valorTotalItensNacionais Valor total (em US$) de decimal body Obrigatório quando itens nacionais a devolver valorTotalItensImportados não for informado ou for igual a 0.

produtosControleQuantitativo Representa a quantidade produtos body Formato segue os parâmetros

de produtos controlados a do Processa venda de viajante devolver

codigoProduto Código do produto integer body Obrigatório quando é registrada uma venda com produtos controlados. tabela de produtos

quantidade Quantidade de produtos integer body Obrigatório quando é registrada controlados presente na uma venda com produtos Venda controlados.

valorTotal Valor total destes produtos decimal body Obrigatório quando é registrada na Venda uma venda com produtos controlados.

venda Representa a Venda a ser venda body Obrigatório devolvida

id Identificação do número string body Obrigatório da venda gerado pelo sistema Loja Franca de Fronteira na operação Processa venda de viajante

notaFiscalEntrada Número da Nota Fiscal de string body Obrigatório entrada gerado pelo sistema gerador de nota fiscal

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

dataHoraDevolucaoParcial Data e hora da devolução string formato yyyy-MM-ddTHH:mm:ss

SERVICO /venda/devolucaoParcial

Exemplo de entrada - Devolução parcial de venda, sem produtos controlado

s{

"valorTotalItensImportados": 9.95,

"valorTotalItensNacionais": 0,

"venda": {

"id": "2017000000020992652",

"numeroNotaFiscalEntrada": "42100484684182000157550010000000020108042108"

Exemplo de entrada - Devolução parcial de venda, com produtos controlados

"valorTotalItensImportados": 5.65,

"valorTotalItensNacionais": 0,

"produtosControleQuantitativo": [{

"codigoProduto": 10,

"quantidade": 1,

"valorTotal": 2.65

}],

"venda": {

"id": "2017000000020992652",

"numeroNotaFiscalEntrada": "42100484684182000157550010000000020108042108"

Exemplo de resposta

"dataHoraDevolucaoParcial": "2017-12-11T17:27:41"

}Códigos de erros possíveis

31, 32, 33, 34, 39, 40, 41, 42, 43, 44, 45, 46, 54, 58, 60, 61, 62, 63.

Devolução total de venda

Efetua uma operação de devolução total de venda.

Parâmetros

Nome Descrição Tipo Local Detalhes

idVenda Identificação do número da venda gerado pelo string query Obrigatório sistema Loja Franca de Fronteira na operação Processa venda de viajante

notaFiscalEntrada Número da Nota Fiscal de entrada gerado pelo string query Obrigatório sistema gerador de nota fiscal

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

dataHoraDevolucaoTotal Data e hora da devolução da string formato yyyy-MM-ddTHH:mm:ss venda

SERVICO /venda/devolucaoTotal?idVenda={idVenda}&amp;notaFiscalEntrada={notaFiscalEntrada}

Exemplo de entrad

a// não tem parâmetros JSON, apenas por query string. Ver o endpoint acima.

Exemplo de resposta

"dataHoraDevolucaoTotal": "2017-12-01T16:32:17"

}Códigos de erros possíveis

31, 32, 33, 34, 39, 40, 41, 54, 58.

Troca item idêntico de venda

Efetua uma operação de troca de item idêntico de uma venda.

Parâmetros

Os parâmetros são exatamente os mesmos da operação Devolução parcial de venda

Atributos da resposta - Status code 200 – OK

Nome Descrição Tipo Detalhes

dataHoraTrocaItemIdentico Data e hora da troca string formato yyyy-MM-ddTHH:mm:ss

SERVICO /venda/trocaItemIdentico

Exemplo de entrada - Troca item idêntico, sem produtos controlado

s{

"valorTotalItensImportados": 10,

"valorTotalItensNacionais": 0,

"venda": {

"id": "2017000000020992652",

"numeroNotaFiscalEntrada": "42100484684182000157550010000000020108042108",

"numeroNotaFiscalSaida": "35160400073132000143550012017000006572827920"

Exemplo de entrada - Devolução parcial de venda, com produtos controlados

"valorTotalItensImportados": 10,

"valorTotalItensNacionais": 0,

"produtosControleQuantitativo": [{

"codigoProduto": 10,

"quantidade": 2,

"valorTotal": 5.3

}],

"venda": {

"id": "2017000000020992652",

"numeroNotaFiscalEntrada": "42100484684182000157550010000000020108042108",

"numeroNotaFiscalSaida": "35160400073132000143550012017000006572827920"

Exemplo de resposta

"dataHoraTrocaItemIdentico": "2017-12-11T17:27:41"

}Códigos de erros possíveis

28, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 54, 58, 60, 61, 62, 63.

Tabela de produtos

Código Descrição

1 Bebida alcóolica

2 Cigarro

3 Fumo

Tabela de tipos de documento

Código Descrição Codigo País País

1 Passaporte TODOS OS PAÍSES

2 Registro de Identidade Civil 105 Brasil

3 Cédula de Identidade AC 105 Brasil

4 Cédula de Identidade AL 105 Brasil

5 Cédula de Identidade AM 105 Brasil

6 Cédula de Identidade AP 105 Brasil

7 Cédula de Identidade BA 105 Brasil

8 Cédula de Identidade CE 105 Brasil

9 Cédula de Identidade DF 105 Brasil

10 Cédula de Identidade ES 105 Brasil

11 Cédula de Identidade GO 105 Brasil

12 Cédula de Identidade MA 105 Brasil

13 Cédula de Identidade MG 105 Brasil

14 Cédula de Identidade MS 105 Brasil

15 Cédula de Identidade MT 105 Brasil

16 Cédula de Identidade PA 105 Brasil

17 Cédula de Identidade PB 105 Brasil

18 Cédula de Identidade PE 105 Brasil

19 Cédula de Identidade PI 105 Brasil

20 Cédula de Identidade PR 105 Brasil

21 Cédula de Identidade RJ 105 Brasil

22 Cédula de Identidade RN 105 Brasil

23 Cédula de Identidade RO 105 Brasil

24 Cédula de Identidade RR 105 Brasil

25 Cédula de Identidade RS 105 Brasil

26 Cédula de Identidade SC 105 Brasil

27 Cédula de Identidade SE 105 Brasil

28 Cédula de Identidade SP 105 Brasil

29 Cédula de Identidade TO 105 Brasil

30 Cédula de Identidade para estrangeiro 105 Brasil

31 Documento Nacional de Identidad 63 Argentina

32 Cédula de Identidad 586 Paraguai

33 Cédula de Identidad 845 Uruguai

34 Cédula de Identidad 850 Venezuela

35 Cédula de Identidad para Nacionales 97 Bolívia

36 Cédula de Identidad para Extranjeros 97 Bolívia

37 Cédula de Identidad 158 Chile

38 Cédula de Ciudadanía 169 Colômbia

39 Tarjeta de Identidad 169 Colômbia

40 Cédula de Extranjería 169 Colômbia

41 Cédula de Ciudadanía 239 Equador

42 Cédula de Identidad para extranjeros 239 Equador

43 Documento Nacional de Identidad 589 Peru

44 Carné de Extranjería 589 Peru

Tabela de países

Ver tabela de países da Receita Federal do Brasil

TABELA DE CÓDIGO DOS PAÍSES

Código País Código País Código País

105 Brasil 271 Finlândia 538 Noruega

013 Afeganistão 161 Formosa (Taiwan) 542 Nova Caledônia

756 África do Sul 275 França 548 Nova Zelândia

017 Albânia, República da 281 Gabão 556 Omã

023 Alemanha 285 Gambia 563 Pacífico, Ilhas do (administ. dos EUA)

037 Andorra 289 Gana 566 Pacífico, Ilhas do (possessão dos EUA) 040 Angola 291 Georgia, República da

041 Anguilla 293 Gibraltar 573 Países Baixos (Holanda)

043 Antigua Barbuda 297 Granada 575 Palau

047 Antilhas Holandesas 301 Grécia 580 Panamá

053 Arábia Saudita 305 Groelândia 545 Papua Nova Guiné

059 Argélia 309 Guadalupe 576 Paquistão

063 Argentina 313 Guam 586 Paraguai

064 Armênia, República da 317 Guatemala 589 Peru

065 Aruba 337 Guiana 593 Pitcairn, Ilha de

073 Arzebaijão, República do 325 Guiana Francesa 599 Polinésia Francesa

069 Austrália 329 Guiné 603 Polônia, República da

072 Áustria 334 Guiné-Bissau 611 Porto Rico

077 Bahamas, Ilhas 331 Guiné-Equatorial 607 Portugal

080 Bahrein, Ilhas 341 Haiti 623 Quênia

081 Bangladesh 345 Honduras 625 Quirguiz, República da

083 Barbados 351 Hong Kong 628 Reino Unido

085 Belarus, República da 355 Hungria, República da 640 República Centro-Africana

087 Bélgica 357 Iemen 647 República Dominicana

088 Belize 361 Índia 660 Reunião, Ilha

229 Benin 365 Indonésia 670 Romênia

090 Bermudas 367 Inglaterra 675 Ruanda

097 Bolívia 372 Irã, República Islâmica do 676 Rússia, Federação da

098 Bósnia-Herzegovina 369 Iraque 685 Saara Ocidental

101 Botsuana 375 Irlanda 677 Salomão, Ilhas 108 Brunei 379 Islândia 690 Samoa

111 Bulgária, República da 383 Israel 691 Samoa Americana

31 Burkina Faso 386 Itália 697 San Marino

115 Burundi 388 Iugoslávia, República 710 Santa Helena Federativa da

119 Butão 391 Jamaica 715 Santa Lúcia

678 Saint Kitts e Nevis

127 Cabo Verde, República de 399 Japão 695 São Cristóvão e Neves, Ilhas

150 Jersey, Ilha do Canal

145 Camarões 396 Johnston, Ilhas 700 São Pedro e Miquelon

141 Camboja 403 Jordânia 720 São Tomé e Príncipe, Ilhas

149 Canadá 411 Kiribati 705 São Vicente e Granadinas

151 Canárias, Ilhas 420 Laos, República Popular 728 Senegal Democrática

153 Casaquistão, República 423 Lebuan, Ilhas 735 Serra Leoa do

737 Servia

154 Catar 426 Lesoto 731 Seychelles

137 Cayman, Ilhas 427 Letônia, República da 744 Síria, República Árabe da

788 Chade 431 Líbano 748 Somália

158 Chile 434 Libéria 750 Sri Lanka

160 China, República Popular 438 Líbia 754 Suazilândia

163 Chipre 440 Liechtenstein 759 Sudão

511 Christmas,Ilhas (Navidad) 442 Lituânia, República da 764 Suécia

741 Cingapura 445 Luxemburgo 767 Suíça

165 Cocos-Keeling, Ilhas 447 Macau 770 Suriname

169 Colômbia 449 Macedônia, 776 Tailândia Ant.Rep.Iugoslava

173 Comores, Ilhas 450 Madagascar 772 Tadjiquistão, República do

452 Madeira, Ilha da

177 Congo 455 Malásia 780 Tanzânia, República Unida da

888 Congo, República Democrática do

183 Cook, Ilhas 458 Malavi 791 Tcheca, República

190 Coréia, República da 461 Maldivas 782 Território Britânico no Oceano Índico

187 Coréia, República Popular 464 Mali 795 Timor Leste Democrática

193 Costa do Marfim 467 Malta 800 Togo

359 Man, Ilha de

196 Costa Rica 472 Marianas do Norte 810 Tonga

198 Coveite 474 Marrocos 805 Toquelau, Ilhas

195 Croácia, República da 476 Marshall, Ilhas 815 Trinidad e Tobago

199 Cuba 477 Martinica 820 Tunísia

998 Delegação Especial da Palestina

232 Dinamarca 485 Maurício 823 Turcas e caicos, Ilhas

783 Djibuti 488 Mauritânia 824 Turcomenistão, República do

235 Dominica, Ilha 493 México 827 Turquia

372 Dubai

237 Dubai 093 Mianmar (Birmânia) 828 Tuvalu

240 Egito 499 Micronésia 831 Ucrânia

687 El salvador 490 Midway, Ilhas 833 Uganda

244 Emirados Árabes Unidos 505 Moçambique 845 Uruguai

243 Eritreia

239 Equador 494 Moldova, República da 847 Uzbequistão, República do

247 Eslovaca, República 495 Mônaco 551 Vanuatu

246 Eslovênia, República da 497 Mongólia 848 Vaticano, Estado da Cidade do

498 Montenegro 873 Wake, Ilha

245 Espanha 501 Montserrat, Ilhas 850 Venezuela

249 Estados Unidos 507 Namíbia 858 Vietnã

251 Estônia, República da 508 Nauru 863 Virgens, Ilhas (Britânicas)

253 Etiópia 517 Nepal 866 Virgens, Ilhas (EUA)

255 Falkland (Ilhas Malvinas) 521 Nicarágua 875 Wallis e Futuna, Ilhas

259 Feroe, Ilhas 525 Niger 888 Zaire

263 Fezzan 528 Nigéria 890 Zâmbia

870 Fidji 531 Niue, Ilha 665 Zimbabue

267 Filipinas 535 Norfolk, Ilha

Tabela de erros

Código Mensagem

1 Estrutura do JSON de entrada diferente da definição do serviço.

2 Chave obrigatória {0} sem conteúdo.

3 {0} com tamanho ou formato diferente da definição do serviço.

4 Certificado não foi informado, não é de Equipamento e/ou não é válido.

9 cnpjLoja {0} não existe como Loja.

10 cnpjLoja diferente do Certificado de Autenticação.

11 cnpjLoja {0} Suspenso.

12 cnpjLoja {0} Cancelado.

13 paisOrigem não localizado na Tabela de Países.

14 tipoDocumento inválido.

15 CPF inválido.

16 Viajante não localizado.

17 CPF obrigatório para brasileiros (paisOrigem = Brasil).

18 CPF diferente do CPF vinculado ao documento {0} através de venda no dia {1}.

19 CPF diferente do CPF vinculado ao documento {0} pela RFB.

20 dataNascimento e nomeNoDocumento obrigatórios para estrangeiro com CPF não informado.

21 Documento não pode ser vinculado ao CPF {0} pois desvinculado desse CPF pela RFB.

22 valorTotalItensImportados ou valorTotalItensNacionais deve ser maior que zero.

23 valorTotalItensNacionais não pode ser maior que saldo de cota: {0}

24 valorCotacaoLoja deve ser maior que zero.

25 produtoControleQuantitativo.codigoProduto {0} não localizado na Tabela de Produtos.

26 produtoControleQuantitativo.codigoProduto {0} já informado na venda.

27 produtoControleQuantitativo.quantidade deve ser maior que zero e não superior ao limite de {0} {1}.

28 produtoControleQuantitativo.valorTotalProdutos deve ser maior que zero.

29 Venda gera imposto inferior ao limite mínimo (R$ {0}) para geração de DARF.

30 Somatório dos produtoControleQuantitativo.valorTotal maior que valorTotalItensImportados + valorTotalItensNacionais.

31 idVenda não localizado.

32 {0} DV inválido.

33 {0} emitida por CNPJ diferente da loja.

34 {0} já informada em outras operações.

35 {0} DV inválido.

36 {0} emitida por CNPJ diferente da loja.

37 {0} já informada em outras operações.

38 Venda foi entregue anteriormente.

39 Venda foi cancelada anteriormente.

40 Venda foi totalmente devolvida anteriormente.

41 Venda não foi entregue anteriormente.

42 produtoControleQuantitativo.codigoProduto {0} não informado na venda.

43 produtoControleQuantitativo.codigoProduto {0} já informado na devolução.

44 produtoControleQuantitativo.quantidade deve ser maior que zero e não superior ao saldo da venda.

45 produtoControleQuantitativo.valorTotal deve ser maior que zero e não superior ao saldo da venda.

46 valorTotalItensImportados + valorTotalItensNacionais maior que saldo da venda.

47 valorTotalItensNacionais maior que saldo da venda da produtos Nacionais.

48 valorTotalItensImportados maior que saldo da venda de produtos Importados.

52 Data de nascimento diferente do {0}.

54 Venda desvinculada do Viajante.

55 CPF não localizado.

56 Data sem cotação do dólar.

57 Situação do CPF inválida.

58 notaFiscalSaida igual a notaFiscalEntrada.

59 notaFiscalSaida não deve ser Informada.

60 Saldo da quantidade do produtoControleQuantitativo.codigoProduto {0} zerado sem zerar o valor total da venda deste produto.

61 Valor total do produtoControleQuantitativo.codigoProduto {0} zerado sem zerar a quantidade total vendida deste produto.

62 Ao zerar os valores totais para produtos Nacionais e Importados, é preciso zerar os produtos controlados da venda.

63 Saldo Final de Produtos Controlados Maior que Saldo Final Total da Venda.

70 Conteúdo do Payload é Invalido.

99 Erro no ambiente {0}. {1}.

-99 Erro na comunicação com algum outro sistema externo que a API do Loja Franca de Fronteira se integra.

Todas as mensagens retornam HTTP Status 422, com exceção das mensagens 1 e 3, que retornam HTTP Status 400.

Todas as mensagens são encapsuladas conforme demonstrado em Tratamento de erros.

As mensagens aqui propostas são sugestões e não necessariamente precisam ser exibidas exatamente da forma como estão no sistema da loja franca que está consumindo a API do Loja Franca de Fronteira, ou seja, elas podem ser customizadas conforme a necessidade.

As mensagens de erro 1, 2, 3, 4, 9, 10, 11, 12, 70 poderão ser disparadas independentemente da operação, pois são mensagens de validação de CNPJ e certificado digital da Loja e mensagens de erros gerais.

