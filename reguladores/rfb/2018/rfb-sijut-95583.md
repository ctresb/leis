---
titulo: "Ato Declaratório Executivo Cofis nº 70, de 5 de outubro de 2018"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "70"
data: "2018-10-05"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 09/10/2018, seção 1, página 56"
data_publicacao: "2018-10-09"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/95583/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/95583/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "95583"
sha256_texto: "32502910b070c486b8a1faafc8ff5dad41dc19019947935009f16f2234bc19da"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Cofis nº 70, de 5 de outubro de 2018

Dispõe sobre o leiaute do Programa Gerador da Declaração de Serviços Médicos e de Saúde (PGD Dmed 2019)

O COORDENADOR-GERAL DE FISCALIZAÇÃO, no uso das atribuições que lhe confere o inciso II do art. 334 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 430, de 09 de outubro de 2017, declara:

**Art. 1º** Fica aprovado o leiaute do arquivo de importação de dados para o Programa Gerador da Declaração de Serviços Médicos e de Saúde (PGD Dmed 2019) para apresentação das informações relativas aos anos-calendário de 2013 a 2018, situação normal, e de 2014 a 2019, nos casos de situação especial.

**Art. 2º** No preenchimento ou importação de dados pelo PGD Dmed 2019, deverá ser observado o leiaute do arquivo constante do Anexo Único deste Ato Declaratório.

**Art. 3º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

FLÁVIO VILELA CAMPOS

ANEXO ÚNICO

a

ANEXO ÚNICO

LEIAUTE DO ARQUIVO DA DECLARAÇÃO

Declaração de Serviços Médicos e Saúde – Dmed

1. Regras Gerais.

2. Estrutura de Arquivo:

2.1. Exemplo de estrutura de declarante Pessoa Jurídica.

3. Leiaute:

3.1. Registro de informação da declaração (identificador Dmed);

3.2. Registro do responsável pelo preenchimento (identificador RESPO);

3.3. Registro de informação do declarante pessoa jurídica (identificador DECPJ);

3.4. Registro de informação da operadora de plano privado de assistência à saúde(identificador OPPAS);

3.5. Registro de informação do titular do plano (identificador TOP);

3.6. Registro de informação de reembolso do titular do plano (identificador RTOP);

3.7. Registro de informação de dependente do titular (identificador DTOP);

3.8. Registro de informação de reembolso do dependente (identificador RDTOP);

3.9. Registro de informação do prestador de serviço de saúde (identificador PSS);

3.10. Registro de informação do responsável pelo pagamento ao prestador do serviço de saúde (identificador RPPSS);

3.11. Registro de informação de beneficiário do serviço pago (identificador BRPPSS);

3.12. Registro identificador do término da declaração (identificador FIMDmed);

Tabela de relação de dependência.

1 – Regras gerais:

Esta seção apresenta as regras que devem ser respeitadas em todos os arquivos gerados, quando não excepcionadas por regra específica referente a um dado registro e explicitada em suas observações.

Regra de Nº Descrição preenchimento

Alfanumérico (C): representados por “C” - todos os caracteres, excetuados o caractere “|” Formato dos (pipe ou barra vertical, caractere 124 da Tabela ASCII);

campos Numérico (N): representados por “N” - pode conter apenas os valores de “0” a “9”.

Campos Devem ser informados conforme o padrão ano, mês, dia (AAAAMMDD), excluindo-se numéricos (D) 2 quaisquer caracteres de separação (tais como “.” (ponto), “/” (barra inclinada), “-” (hífen), cujo conteúdo etc.). representa data

Campos numéricos (N) 3 Devem ser informados conforme o padrão “ano” (AAAA). cujo conteúdo representa ano

Campos Os campos numéricos com número de inscrição (CNPJ, CPF, CNES e ANS) deverão ser numéricos com informados com todos os dígitos, inclusive os zeros (0) à esquerda;

número de As máscaras (caracteres especiais de formatação, tais como “.” (ponto), “/” (barra inscrição inclinada), “-” (hífen), etc.) não devem ser informadas.

Campos Devem ser informados com até 9 posições, representando 7 posições inteiras e 2 decimais; numéricos 5 referentes a Os zeros não significativos não devem ser informados; valores Os caracteres ‘.’ (ponto) e ‘,’ (vírgula) não devem ser informados. monetários

Campos Os campos com conteúdo alfanumérico nos quais se faz necessário registrar números ou alfanuméricos códigos de identificação (Ex.: Cadastro Nacional de Estabelecimentos de Saúde – CNES) 6 com números ou deverão seguir a regra de formação e tamanho definidos pelo respectivo órgão regulador; códigos de As máscaras (caracteres especiais de formatação, tais como “.” (ponto), “/” (barra identificação inclinada), “-” (hífen), etc.) não devem ser informadas.

Ao final de cada campo (incluído o último de cada registro) deve ser inserido o caractere delimitador “|” (pipe ou barra vertical: caractere 124 da Tabela ASCII);

O caractere delimitador “|” (pipe) não deve ser incluído como parte integrante do conteúdo Formação dos 7 de quaisquer campos numéricos, datas ou alfanuméricos; campos Na ausência de informação, o campo vazio (campo sem conteúdo; nulo e com valor zero) deverá ser iniciado com caractere “|” e imediatamente encerrado com o mesmo caractere “|” delimitador de campo.

Formação dos 8 Cada registro deve necessariamente ocupar apenas uma linha no arquivo. registros

Preenchimento Preenchimento fixo: o campo deve ser preenchido com o tamanho exato;

dos campos Preenchimento variável: o campo pode ter variação de tamanho de preenchimento.

2 – Estrutura de arquivo:

2.1 – Exemplo de estrutura de declarante Pessoa Jurídica:

Dmed – Declaração de serviços médicos e de saúde;

RESPO – Responsável pelo preenchimento;

DECPJ – Declarante pessoa jurídica;

OPPAS – Operadora de plano privado de assistência à saúde;

TOP – Titular do plano;

RTOP – Reembolso do titular do plano;

DTOP – Dependente do titular;

RDTOP – Re mbolso do dependente;

PSS – Prestador de serviço de saúde;

RPPSS – Responsável pelo pagamento ao prestador do serviço de saúde;

BRPPSS – Beneficiário do serviço pago;

FIMDmed – Término da declaração.

3 – Leiaute do arquivo:

3.1 – Registro de informação da declaração (identificador Dmed):

- Registro obrigatório no arquivo;

- Deve ser o 1º (primeiro) registro no arquivo;

- Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 4 Dmed Sim

2 Ano referência N Fixo 4 2019 Sim

3 Ano-calendário N Fixo 4 2013 a 2019 Sim

Indicador de retificadora S – Retificadora 4 C Fixo 1 Sim N – Original

5 Número do recibo N Fixo 12 - Não

Identificador de estrutura do 6 C Fixo 6 - Não leiaute

Número do recibo Se a declaração for original, não preencher;

5 Se a declaração for retificadora, deverá ser preenchido com o número do recibo da última declaração entregue, se declarante não transmitir a declaração com assinatura digital.

3.2 – Registro do Responsável pelo preenchimento (identificador RESPO):

- Registro obrigatório no arquivo;

- Deve ser o 2º (segundo) registro no arquivo;

- Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 5 RESPO Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 DDD N Fixo 2 - Sim

5 Telefone N Fixo 9 - Sim

6 Ramal N Variável 6 - Não

7 Fax N Fixo 9 - Não

8 Correio eletrônico C Variável 50 - Não

3.3 – Registro de informação do declarante pessoa jurídica (identificador DECPJ):

- Registro obrigatório no arquivo quando for declarante pessoa jurídica;

- Deve ser o 3º (terceiro) registro no arquivo;

- Ocorre somente uma vez no arquivo;

Preenchi Tamanh Obrigatóri Ordem Campo Formato Valores Válidos mento o o

1 Identificador de registro C Fixo 5 DECPJ Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

1 – Prestador de serviço de saúde;

2 – Operadora de plano privado de assistência à 4 Tipo do declarante N Fixo 1 saúde; Sim

3 – Prestador de serviço de saúde e Operadora de plano privado de assistência a saúde.

5 Registro ANS N Fixo 6 - Não

6 CNES N Fixo 7 - Não

CPF responsável perante o 7 N Fixo 11 - Sim CNPJ

Indicador de situação da S – Declaração de situação declaração especial; 8 C Fixo 1 Sim N – Não é declaração de situação especial.

9 Data do evento D Fixo 8 - Não

Registro ANS Agência Nacional de Saúde Suplementar – ANS; 5 Preenchimento obrigatório se campo de ordem 4 – Tipo do declarante igual a “2” ou “3”.

6 CNES Cadastro Nacional de Estabelecimentos de Saúde – CNES.

Data do evento Preenchimento obrigatório se campo de ordem 8 – Indicador de

situação da declaração igual a “S”.

3.4 – Registro de informação da operadora de plano privado de assistência à saúde (identificador OPPAS):

- Ocorre caso o declarante seja operadora de plano privado de assistência à saúde.

- Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 5 OPPAS Sim

Identificador de registro Preenchimento obrigatório se o campo de ordem 4 – Tipo do Declarante, do registro DECPJ igual a “2”; 1 Preenchimento opcional se o campo de ordem 4 – Tipo do Declarante, do registro DECPJ igual a “3”, e o declarante não exerceu atividades de Operadora de Plano Privado de Assistência à Saúde no ano-calendário.

3.5 – Registro de informação do titular do plano (identificador TOP):

- Deve estar classificado em ordem crescente por CPF do titular;

- Deve estar associado ao registro do tipo OPPAS.

1 Identificador de registro C Fixo 3 TOP Sim

2 CPF do titular N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

Valor pago no ano com o 4 N Variável 9 - Não titular

Valor pago no ano com o Preenchimento obrigatório se não existir registros RTOP e/ou DTOP

titular associados ao TOP.

3.6 – Registro de informação de reembolso do titular do plano (identificador RTOP):

- Deve estar classificado em ordem crescente por CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ);

- Deve estar associado ao registro do tipo TOP;

- Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos-calendário anteriores.

1 Identificador de registro C Fixo 4 RTOP Sim

CPF/CNPJ do prestador CPF com 11 de serviço dígitos; 2 N Variável 14 Sim CNPJ com 14 dígitos.

Nome/Nome empresarial Nome da pessoa do prestador de serviço física até 60 posições. 3 C Variável 150 Sim Nome empresarial da pessoa jurídica até 150 posições.

Valor do reembolso do - 4 N Variável 9 Não ano-calendário

Valor do reembolso de - 5 N Variável 9 Não anos anteriores

Valor do reembolso do ano-calendário Valores reembolsados no ano-calendário, referentes a

pagamentos de serviços prestados no ano-calendário.

Valor do reembolso de anos anteriores Valores reembolsados no ano-calendário referentes a

pagamentos de serviços prestados em anos anteriores.

3.7 – Registro de informação de dependente do titular (identificador DTOP):

- Deve estar classificado em ordem crescente por CPF e Data de nascimento do dependente;

- Deve estar associado ao registro do tipo TOP.

1 Identificador de registro C Fixo 4 DTOP Sim

2 CPF do dependente N Fixo 11 - Não

3 Data de Nascimento D Fixo 8 - Não

4 Nome C Variável 60 Sim

Relação de Dependência Conforme Tabela 5 N Fixo 2 de Relação de Não Dependência

Valor pago no ano com o 6 N Variável 9 - Não dependente

CPF do dependente Preenchimento obrigatório para maiores de 18 anos completos até 31 de dezembro do

ano-calendário da declaração.

Data de nascimento Preenchimento obrigatório para menores de 18 anos completos até 31 de dezembro do

ano-calendário da declaração, que não tenham informado o CPF.

3.8. Registro de informação de reembolso do dependente (identificador RDTOP):

- Deve estar classificado em ordem crescente por CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ);

- Deve estar associado ao registro do tipo DTOP;

- Só deverá constar o registro se houver valor de reembolso do ano-calendário e de anos-calendário anteriores.

1 Identificador de registro C Fixo 5 RDTOP Sim

CPF/CNPJ do prestador de CPF com 11 serviço dígitos; 2 N Variável 14 Sim CNPJ com 14 dígitos.

3 Nome/Nome Empresarial do C Variável 150 Nome da pessoa Sim prestador de serviço física até 60 posições;

Nome empresarial da pessoa jurídica

até 150 posições.

Valor do reembolso do ano- 4 N Variável 9 - Não calendário

Valor do reembolso de anos 5 N Variável 9 - Não anteriores

Valor do reembolso do ano- Valores reembolsados no ano-calendário, referentes a pagamentos de

calendário serviços prestados no ano-calendário.

Valor do reembolso de anos Valores reembolsados no ano-calendário referentes a pagamentos de

anteriores serviços prestados em anos anteriores.

3.9 – Registro de informação do prestador de serviço de saúde (identificador PSS):

- Ocorre caso o declarante seja prestador de serviço de saúde.

- Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 3 PSS Sim

Identificador de registro Preenchimento obrigatório se o campo de ordem 4 – Tipo do Declarante, do registro DECPJ igual a “1”; 1 Preenchimento opcional se o campo de ordem 4 – Tipo do Declarante, do registro DECPJ igual a “3”, e o declarante não exerceu atividades de Prestador de Serviços de Saúde no ano-calendário.

3.10 – Registro de informação do responsável pelo pagamento ao prestador do serviço de saúde (identificador RPPSS):

- Deve estar classificado em ordem crescente por CPF do responsável pelo pagamento;

- Deve estar associado ao registro do tipo PSS.

1 Identificador de registro C Fixo 5 RPPSS Sim

CPF do responsável pelo 2 N Fixo 11 - Sim pagamento

3 Nome C Variável 60 - Sim

Valor pago no ano pelo 4 responsável em benefício N Variável 9 - Não próprio

Valor pago no ano pelo Preenchimento obrigatório se não existir registro BRPPSS associado ao 4 responsável em benefício RPPSS. próprio

3.11 – Registro de informação de beneficiário do serviço pago (identificador BRPPSS):

- Deve estar classificado em ordem crescente por CPF e Data de nascimento do beneficiário;

- Deve estar associado ao registro do tipo RPPSS.

1 Identificador de registro C Fixo 6 BRPPSS Sim

2 CPF do beneficiário N Fixo 11 - Não

3 Data de nascimento D Fixo 8 - Não

4 Nome C Variável 60 - Sim

Valor pago no ano com o 5 N Variável 9 >0 Sim beneficiário

Data de nascimento Preenchimento obrigatório para o beneficiário do serviço de saúde que não

informar o número do CPF quando da prestação do serviço.

3.12 – Registro identificador do término da declaração (identificador FIMDmed):

- Registro obrigatório no arquivo;

- Deve ser o último registro no arquivo;

- Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 7 FIMDmed Sim

4 – Tabela de relação de dependência:

Código Descrição

03 Cônjuge/companheiro

04 Filho/filha

06 Enteado/enteada

08 Pai/mãe

10 Agregado/outros

