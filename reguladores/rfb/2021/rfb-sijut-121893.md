---
titulo: "Ato Declaratório Executivo Cofis nº 90, de 16 de novembro de 2021"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "90"
data: "2021-11-16"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 02/12/2021, seção 1, página 63"
data_publicacao: "2021-12-02"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/121893/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/121893/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "121893"
sha256_texto: "7b92a1a6797e1806b5aa0b51981fb94bb3ac797e9cf0dfc63dfaf30343793a93"
baixado_em: "2026-10-20"
ocr_pdf: "Vision macOS português; todas as páginas do anexo conferidas quanto à presença de texto"
---
# Ato Declaratório Executivo Cofis nº 90, de 16 de novembro de 2021

> Texto obtido por OCR a partir de PDF escaneado; pode conter erros de reconhecimento.

Republicação parcial

ANEXO ÚNICO

Anexo Único

ANEXO ÚNICO LEIAUTE DO ARQUIVO DA DECLARAÇÃO Declaração de Serviços Médicos e de Saúde - Dmed 1. Regras Gerais 2. Estrutura de Arquivo 2.1. Exemplo de estrutura de declarante Pessoa Jurídica 3. Leiaute 3.1. Registro de informação da declaração (identificador Dmed) 3.2. Registro do responsável pelo preenchimento (identificador RESPO) 3.3. Registro de informação do declarante pessoa jurídica (identificador DECPJ) 3.4. Registro de informação da operadora de plano de assistência à saúde (identificador OPPAS) 3.5. Registro de informação do titular do plano (identificador TOP) 3.6. Registro de informação de reembolso do titular do plano (identificador RTOP) 3.7. Registro de informação de dependente do titular (identificador DTOP) 3.8. Registro de informação de reembolso do dependente (identificador RDTOP) 3.9. Registro de informação do prestador de serviço de saúde (identificador PSS) 3.10. Registro de informação do responsável pelo pagamento ao prestador do serviço de saúde (identificador RPPSS) 3.11. Registro de informação de beneficiário do serviço pago (identificador BRPPSS) 3.12. Registro identificador do término da declaração (identificador FIMDmed) 4. Tabela de relação de dependência 1 - Regras gerais: Esta seção apresenta as regras que devem ser respeitadas em todos os arquivos gerados, quando não excepcionada: por regra específica referente a um dado registro e explicitada em suas observações. Regra de

Nº preenchimento Alfanumérico (C): representados por "C" - todos os caracteres, excetuados o caractere Formato dos

"|" (pipe ou barra vertical, caractere 124 da Tabela ASCII); campos Numérico (N): representados por "N" - pode conter apenas os valores de "0" a "9". Campos Devem ser informados conforme o padrão ano, mês, dia (AAAAMMDD), excluindo-se numéricos (D) quaisquer caracteres de separação, tais como: "" (ponto), "/" (barra inclinada), "" cujo conteúdo (hifen), etc. representa data Campos numéricos (N) Devem ser informados conforme o padrão "ano" (AAAA). З cujo conteúdo representa ano Os campos numéricos com número de inscrição (CNPJ, CPF, CNES e ANS) deverão ser Campos informados com todos os dígitos, inclusive os zeros (0) à esquerda; numéricos com As máscaras (caracteres especiais de formatação, tais como "" (ponto), "/" (barra número de inclinada), "-" (hífen), etc.) não devem ser informadas. inscrição Campos numéricos Devem ser informados com até 9 posições, representando 7 posições inteiras e 2 decimais; Os zeros não significativos não devem ser informados;

referentes a Os caracteres "." (ponto) e "," (vírgula) não devem ser informados. valores monetários

Regra de Nº

preenchimento Os campos com conteúdo alfanumérico nos quais se faz necessário registrar números ou Campos códigos de identificação (Ex.: Cadastro Nacional de Estabelecimentos de Saúde - CNES) alfanuméricos deverão seguir a regra de formação e tamanho definidos pelo respectivo órgão 6 com números ou regulador; códigos de As máscaras (caracteres especiais de formatação, tais como: "." (ponto), "/" (barra identificação inclinada), "." (hífen), etc.) não devem ser informadas.

Ao final de cada campo (incluído o último de cada registro) deve ser inserido o caractere delimitador "|" (pipe ou barra vertical: caractere 124 da Tabela ASCII); O caractere delimitador "|" (pipe) não deve ser incluído como parte integrante do Formação dos conteúdo de quaisquer campos numéricos, datas ou alfanuméricos; campos Na ausência de informação, o campo vazio (campo sem conteúdo; nulo e com valor zero) deverá ser iniciado com caractere "|" e imediatamente encerrado com o mesmo caractere "|" delimitador de campo. 8 Formação dos Cada registro deve necessariamente ocupar apenas uma linha no arquivo. registros

Preenchimento fixo: o campo deve ser preenchido com o tamanho exato; Preenchimento variável: o campo pode ter variação de tamanho de preenchimento. dos campos 2 - Estrutura de arquivo 2.1 - Exemplo de estrutura de declarante Pessoa Jurídica Dmed - Declaração de serviços médicos e de saúde RESPO - Responsável pelo preenchimento DECPJ - Declarante pessoa jurídica OPPAS - Operadora de plano de assistência à saúde TOP - Titular do plano RTOP - Reembolso do titular do plano DTOP - Dependente do titular RDTOP - Reembolso do dependente PSS - Prestador de serviço de saúde RPPSS - Responsável pelo pagamento ao prestador do serviço de saúde BRPPSS - Beneficiário do serviço pago FIMDmed - Término da declaração 3 - Leiaute do arquivo 3.1 - Registro de informação da declaração (identificador Dmed)

- Registro obrigatório no arquivo; - Deve ser o 1° (primeiro) registro no arquivo;

Dmed

Ano referência

2022 2016 a 2022

Ano-calendário S - Retificadora Indicador de retificadora

N - Original

Número do recibo Identificador de estrutura do

leiaute

Se a declaração for original, não preencher; Número do recibo Se a declaração for retificadora, deverá ser preenchido com o número do re-

cibo da última declaração entregue, se declarante não transmitir a declara- ção com assinatura digital. 3.2 - Registro do Responsável pelo preenchimento (identificador RESPO)

- Registro obrigatório no arquivo; - Deve ser o 2° (segundo) registro no arquivo;

RESPO

CPF

З

DDD

Telefone

Ramal

Fax

Correio eletrônico 3.3 - Registro de informação do declarante pessoa jurídica (identificador DECPJ)

- Registro obrigatório no arquivo quando for declarante pessoa juridica; - Deve ser o 3° (terceiro) registro no arquivo; Ocorre somente uma vez no arquivo;

C

DECPJ

CNPJ

Nome empresarial

1 - Prestador de Tipo do declarante serviço de saúde; 2 - Operadora de plano de assistência à saúde; 3 - Prestador de serviço de saúde e Operadora de plano de

assistência à saúde.

Registro ANS

CNES CPF responsável perante o

CNPJ S - Declaração de situação especial; Indicador de situação da

N - Não é

C declaração declaração de situação especial.

DI

Data do evento S - Declarante possui registro na Indicador declarante possui ANS;

N - Declarante registro ANS não possui registro na ANS

Agência Nacional de Saúde Suplementar - ANS; Registro ANS Preenchimento obrigatório se campo de ordem 4 - Tipo do

declarante igual a "2" ou "3"; e campo de ordem 10 - Indicador declarante possui registro ANS igual a "S". CNES Cadastro Nacional de Estabelecimentos de Saúde - CNES. Preenchimento obrigatório se campo de ordem 8 - Indicador de Data do evento situação da declaração igual a "S". Preenchimento obrigatório se campo de ordem 4 - Tipo do

Indicador declarante possui registro ANS declarante igual a "2" ou "3". 3.4 - Registro de informação da operadora de plano de assistência à saúde (identificador OPPAS)

- Ocorre caso o declarante seja operadora de plano de assistência à saúde.

OPPAS C

Preenchimento obrigatório se o campo de ordem 4 - Tipo do Declaran- te, do registro DECPJ igual a "2";

Preenchimento opcional se o campo de ordem 4 - Tipo do Declarante, do registro DECPJ igual a "3", e o declarante não exerceu atividades de Operadora de Plano de Assistência à Saúde no ano-calendário.

3.5 - Registro de informação do titular do plano (identificador TOP)

- Deve estar classificado em ordem crescente por CPF do titular; - Deve estar associado ao registro do tipo OPPAS.

TOP

CPF do titular

Valor pago no ano com o

titular

Valor pago no ano com o ti- Preenchimento obrigatório se não existir registros RTOP e/ou DTOP associa-

dos ao TOP. tular 3.6 - Registro de informação de reembolso do titular do plano (identificador RTOP)

- Deve estar classificado em ordem crescente por CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo TOP; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos-calendário anteriores.

RTOP

C CPF com 11 CPF/CNPJ do prestador de dígitos; serviço

CNPJ com 14 dígitos. Nome da pessoa Nome/Nome empresarial física até 60 do prestador de serviço | posições.

Nome empresarial da pessoa jurídica até 150 posições. Valor do reembolso do

ano-calendário Valor do reembolso de

anos anteriores

Valores reembolsados no ano-calendário, referentes a Valor do reembolso do ano-calendário

pagamentos de serviços prestados no ano-calendário. Valores reembolsados no ano-calendário referentes Valor do reembolso de anos anteriores

pagamentos de serviços prestados em anos anteriores.

3.7 - Registro de informação de dependente do titular (identificador DTOP)

- Deve estar classificado em ordem crescente por CPF e Data de nascimento do dependente; - Deve estar associado ao registro do tipo TOP.

DTOP

CI

CPF do dependente

Data de Nascimento

DI

Conforme Tabela Relação de Dependência

de Relação de Dependência Valor pago no ano com o

dependente

CPF do dependente Preenchimento obrigatório para maiores de 18 anos completos até 31 de dezembro

do ano-calendário da declaração. Preenchimento obrigatório para menores de 18 anos completos até 31 de dezembro Data de nascimento do ano-calendário da declaração, que não tenham informado o CPF. 3.8. Registro de informação de reembolso do dependente (identificador RDTOP)

- Deve estar classificado em ordem crescente por CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo DTOP; - Só deverá constar o registro se houver valor de reembolso do ano-calendário e de anos-calendário anteriores.

RDTOP

CPF com 11 CPF/CNPJ do prestador de dígitos; serviço

CNPJ com 14 dígitos. Nome da pessoa Nome/Nome Empresarial do física até 60 prestador de serviço posições;

Nome empresarial da pessoa jurídica até 150 posições. Valor do reembolso do ano-

calendário Valor do reembolso de anos

anteriores

Valor do reembolso do ano- Valores reembolsados no ano-calendário, referentes a pagamentos de

calendário serviços prestados no ano-calendário. Valores reembolsados no ano-calendário referentes a pagamentos de Valor do reembolso de anos

anteriores serviços prestados em anos anteriores. 3.9 - Registro de informação do prestador de serviço de saúde (identificador PSS)

- Ocorre caso o declarante seja prestador de serviço de saúde.

З

PSS

Preenchimento obrigatório se o campo de ordem 4 - Tipo do Decla- rante, do registro DECPJ igual a "1"; Preenchimento opcional se o campo de ordem 4 - Tipo do Declarante, do registro DECPJ igual a "3", e o declarante não exerceu atividades de Prestador de Serviços de Saúde no ano-calendário. 3.10 - Registro de informação do responsável pelo pagamento ao prestador do serviço de saúde (identificador RPPSS)

- Deve estar classificado em ordem crescente por CPF do responsável pelo pagamento; - Deve estar associado ao registro do tipo PSS.

RPPSS CPF do responsável pelo

pagamento

Valor pago no ano pelo

responsável em benefício próprio

Valor pago no ano pelo Preenchimento obrigatório se não existir registro BRPPSS associado ao

responsável em benefício RPPSS. próprio 3.11 - Registro de informação de beneficiário do serviço pago (identificador BRPPSS)

- Deve estar classificado em ordem crescente por CPF e Data de nascimento do beneficiário; • Deve estar associado ao registro do tipo RPPSS.

BRPPSS

CPF do beneficiário

D

Data de nascimento

Valor pago no ano com o

>0 beneficiário

Preenchimento obrigatório para o beneficiário do serviço de saúde que não Data de nascimento З informar o número do CPF quando da prestação do serviço. 3.12 - Registro identificador do término da declaração (identificador FIMDmed)

- Registro obrigatório no arquivo; - Deve ser o último registro no arquivo;

Tamanho Valores Válidos

FIMDmed

4 - Tabela de relação de dependência

Código Cônjuge/companheiro

Filho/filha

Enteado/enteada

Pai/mãe

Agregado/outros


Nota: Republicado em parte por ter saído no DOU de 18/11/2021, seção 1, página 51 a 53, com incorreção do original.
