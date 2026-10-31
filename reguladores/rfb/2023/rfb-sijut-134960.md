---
titulo: "Ato Declaratório Executivo Cofis nº 54, de 23 de novembro de 2023"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "54"
data: "2023-11-23"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 28/11/2023, seção 1, página 31"
data_publicacao: "2023-11-28"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/134960/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/134960/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "134960"
sha256_texto: "f5ddd4567ec164c0b537b18f89e9f7f5eafde4dfd34ff07a74f6946a25a41127"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Cofis nº 54, de 23 de novembro de 2023

Dispõe sobre o leiaute do Programa Gerador da Declaração de Serviços Médicos e de Saúde (PGD Dmed 2024).

O COORDENADOR-GERAL DE FISCALIZAÇÃO, no uso das atribuições que lhe conferem os incisos I e II do art. 121 do Regimento Interno da Secretaria Especial da Receita Federal do Brasil, aprovado pela Portaria ME nº 284, de 27 de julho de 2020, e tendo em vista o disposto no art. 122 da referida Portaria, declara:

**Art. 1º** Fica aprovado o leiaute aplicável aos campos, registros e arquivos da Declaração de Serviços Médicos e de Saúde (Dmed) para apresentação das informações relativas aos anos-calendário de 2018 a 2023, situação normal, e de 2018 a 2024, nos casos de situação especial.

**Art. 2º** Para o preenchimento ou importação de dados pelo PGD Dmed 2024 deverá ser observado o leiaute do arquivo constante do Anexo Único deste Ato Declaratório.

**Art. 3º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

RICARDO DE SOUZA MOREIRA

ANEXO ÚNICO

Anexo Único

ANEXO ÚNICO

LEIAUTE DO ARQUIVO DA DECLARAÇÃO Declaração de Serviços Médicos e de Saúde - Dmed 1. Regras Gerais 2. Estrutura de Arquivo 2.1. Exemplo de estrutura de declarante Pessoa Jurídica 3. Leiaute 3.1. Registro de informação da declaração (identificador Dmed) 3.2. Registro do responsável pelo preenchimento (identificador RESPO) 3.3. Registro de informação do declarante pessoa jurídica (identificador DECPJ) 3.4. Registro de informação da operadora de plano de assistência à saúde (identificador OPPAS) 3.5. Registro de informação do titular do plano (identificador TOP) 3.6. Registro de informação de reembolso do titular do plano (identificador RTOP) 3.7. Registro de informação de dependente do titular (identificador DTOP) 3.8. Registro de informação de reembolso do dependente (identificador RDTOP) 3.9. Registro de informação do prestador de serviço de saúde (identificador PSS) 3.10. Registro de informação do responsável pelo pagamento ao prestador do serviço de saúde (identificador RPPSS) 3.11. Registro de informação de beneficiário do serviço pago (identificador BRPPSS) 3.12. Registro identificador do término da declaração (identificador FIMDmed) 4. Tabela de relação de dependência 1 - Regras gerais: Esta seção apresenta as regras que devem ser respeitadas em todos os arquivos gerados, quando não excepcionadas por regra específica referente a um dado registro e explicitada em suas observações.

Regra de Nº Descrição preenchimento Alfanumérico (C): representados por "C" - todos os caracteres, excetuados o caractere "|" (pipe ou barra vertical, caractere 124 1 Formato dos campos da Tabela ASCII); Numérico (N): representados por "N" - pode conter apenas os valores de "0" a "9". Campos numéricos (D) Devem ser informados conforme o padrão ano, mês, dia 2 cujo conteúdo (AAAAMMDD), excluindo-se quaisquer caracteres de separação, representa data tais como: "." (ponto), "/" (barra inclinada), "-" (hífen), etc. Campos numéricos (N) 3 cujo conteúdo Devem ser informados conforme o padrão "ano" (AAAA). representa ano

Os campos numéricos com número de inscrição (CNPJ, CPF, CNES e ANS) deverão ser informados com todos os dígitos, Campos numéricos com inclusive os zeros (0) à esquerda;

número de inscrição As máscaras (caracteres especiais de formatação, tais como "." (ponto), "/" (barra inclinada), "-" (hífen), etc.) não devem ser informadas. Devem ser informados com até 9 posições, representando 7 Campos numéricos posições inteiras e 2 decimais; 5 referentes a valores Os zeros não significativos não devem ser informados; monetários Os caracteres "." (ponto) e "," (vírgula) não devem ser informados. Os campos com conteúdo alfanumérico nos quais se faz Campos alfanuméricos necessário registrar números ou códigos de identificação (Ex.: 6 com números ou Cadastro Nacional de Estabelecimentos de Saúde - CNES) códigos de identificação deverão seguir a regra de formação e tamanho definidos pelo respectivo órgão regulador. As máscaras (caracteres especiais de formatação, tais como: "." (ponto), "/" (barra inclinada), "-" (hífen), etc.) não devem ser informadas. Ao final de cada campo (incluído o último de cada registro) deve ser inserido o caractere delimitador "|" (pipe ou barra vertical: caractere 124 da Tabela ASCII); 7 Formação dos campos O caractere delimitador "|" (pipe) não deve ser incluído como parte integrante do conteúdo de quaisquer campos numéricos, datas ou alfanuméricos. Na ausência de informação, o campo vazio (campo sem conteúdo; nulo e com valor zero) deverá ser iniciado com caractere "|" e imediatamente encerrado com o mesmo caractere "|" delimitador de campo. Cada registro deve necessariamente ocupar apenas uma linha 8 Formação dos registros no arquivo. Preenchimento fixo: o campo deve ser preenchido com o Preenchimento dos tamanho exato;

campos Preenchimento variável: o campo pode ter variação de tamanho de preenchimento. 2 - Estrutura de arquivo 2.1 - Exemplo de estrutura de declarante Pessoa Jurídica

Dmed - Declaração de serviços médicos e de saúde RESPO - Responsável pelo preenchimento DECPJ - Declarante pessoa jurídica OPPAS - Operadora de plano de assistência à saúde TOP - Titular do plano RTOP - Reembolso do titular do plano DTOP - Dependente do titular RDTOP - Reembolso do dependente PSS - Prestador de serviço de saúde RPPSS - Responsável pelo pagamento ao prestador do serviço de saúde BRPPSS - Beneficiário do serviço pago FIMDmed - Término da declaração

3 - Leiaute do arquivo 3.1 - Registro de informação da declaração (identificador Dmed)

- Registro obrigatório no arquivo; - Deve ser o 1º (primeiro) registro no arquivo; - Ocorre somente uma vez no arquivo.

Identificador 1 C Fixo 4 Dmed Sim de registro Ano 2 N Fixo 4 2024 Sim referência Ano- 3 N Fixo 4 2018 a 2024 Sim calendário S- Indicador de 4 C Fixo 1 Retificadora Sim retificadora N - Original Número do 5 N Fixo 12 - Não recibo Identificador 6 de estrutura C Fixo 6 - Não do leiaute

Se a declaração for original, não preencher; Número do Se a declaração for retificadora, deverá ser preenchido com o número

recibo do recibo da última declaração entregue, se declarante não transmitir a declaração com assinatura digital. 3.2 - Registro do Responsável pelo preenchimento (identificador RESPO)

- Registro obrigatório no arquivo; - Deve ser o 2º (segundo) registro no arquivo; - Ocorre somente uma vez no arquivo.

1 C Fixo 5 RESPO Sim

2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 DDD N Fixo 2 - Sim 5 Telefone N Fixo 9 - Sim 6 Ramal N Variável 6 - Não 7 Fax N Fixo 9 - Não 8 Correio eletrônico C Variável 50 - Não 3.3 - Registro de informação do declarante pessoa jurídica (identificador DECPJ)

- Registro obrigatório no arquivo quando for declarante pessoa jurídica; - Deve ser o 3º (terceiro) registro no arquivo; - Ocorre somente uma vez no arquivo; Ordem Campo Formato Preenchimento Tamanho Valores Válidos Obrigatório Identificador 1 C Fixo 5 DECPJ Sim de registro 2 CNPJ N Fixo 14 - Sim Nome 3 C Variável 150 - Sim empresarial Tipo do 1 - Prestador de 4 N Fixo 1 Sim declarante serviço de saúde; 2 - Operadora de plano de assistência à saúde; 3 - Prestador de serviço de saúde e Operadora de plano de assistência à saúde. 5 Registro ANS N Fixo 6 - Não 6 CNES N Fixo 7 - Não CPF responsável 7 N Fixo 11 - Sim perante o CNPJ S - Declaração de Indicador de situação especial; 8 situação da C Fixo 1 N - Não é Sim declaração declaração de situação especial. Data do 9 D Fixo 8 - Não evento Indicador S - Declarante declarante 10 C Fixo 1 possui registro na Não possui registro ANS; ANS N - Declarante não possui registro na ANS

Agência Nacional de Saúde Suplementar - ANS; Preenchimento obrigatório se campo de ordem 4 - Tipo do 5 Registro ANS declarante igual a "2" ou "3"; e campo de ordem 10 - Indicador declarante possui registro ANS igual a "S". 6 CNES Cadastro Nacional de Estabelecimentos de Saúde - CNES. Preenchimento obrigatório se campo de ordem 8 - Indicador 9 Data do evento de situação da declaração igual a "S". Indicador declarante Preenchimento obrigatório se campo de ordem 4 - Tipo do

possui registro ANS declarante igual a "2" ou "3".

3.4 - Registro de informação da operadora de plano de assistência à saúde (identificador OPPAS)

- Ocorre caso o declarante seja operadora de plano de assistência à saúde. - Ocorre somente uma vez no arquivo.

Identificador 1 C Fixo 5 OPPAS Sim de registro

Preenchimento obrigatório se o campo de ordem 4 - Tipo do Declarante, do registro DECPJ igual a "2"; Identificador 1 Preenchimento opcional se o campo de ordem 4 - Tipo do Declarante, de registro do registro DECPJ igual a "3", e o declarante não exerceu atividades de Operadora de Plano de Assistência à Saúde no ano-calendário. 3.5 - Registro de informação do titular do plano (identificador TOP)

- Deve estar classificado em ordem crescente por CPF do titular; - Deve estar associado ao registro do tipo OPPAS.

1 C Fixo 3 TOP Sim

2 CPF do titular N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Valor pago no ano 4 N Variável 9 - Não com o titular

Valor pago no ano Preenchimento obrigatório se não existir registros RTOP e/ou

com o titular DTOP associados ao TOP. 3.6 - Registro de informação de reembolso do titular do plano (identificador RTOP)

1. Regras de validação do registro: - Deve estar classificado em ordem crescente por CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo TOP; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos- calendário anteriores. Ordem Campo Formato Preenchimento Tamanho Valores Válidos Obrigatório

1 C Fixo 4 RTOP Sim

CPF com 11 CPF/CNPJ do dígitos; 2 prestador de N Variável 14 Sim CNPJ com 14 serviço dígitos.

Nome/Nome Nome da pessoa empresarial do 3 C Variável 150 física até 60 Sim prestador de posições. serviço Nome empresarial da pessoa jurídica até 150 posições. Valor do 4 reembolso do N Variável 9 - Não ano-calendário Valor do 5 reembolso de N Variável 9 - Não anos anteriores

Valor do reembolso do Valores reembolsados no ano-calendário, referentes a

ano-calendário pagamentos de serviços prestados no ano-calendário. Valor do reembolso de Valores reembolsados no ano-calendário referentes a

anos anteriores pagamentos de serviços prestados em anos anteriores. 3.7 - Registro de informação de dependente do titular (identificador DTOP)

- Deve estar classificado em ordem crescente por CPF e Data de nascimento do dependente; - Deve estar associado ao registro do tipo TOP. Ordem Campo Formato Preenchimento Tamanho Valores Válidos Obrigatório

1 C Fixo 4 DTOP Sim

CPF do 2 N Fixo 11 - Não dependente Data de 3 D Fixo 8 - Não Nascimento 4 Nome C Variável 60 Sim Conforme Tabela Relação de 5 N Fixo 2 de Relação de Não Dependência Dependência Valor pago no 6 ano com o N Variável 9 - Não dependente

CPF do Preenchimento obrigatório para maiores de 18 anos completos até 31

dependente de dezembro do ano-calendário da declaração. Preenchimento obrigatório para menores de 18 anos completos até Data de 3 31 de dezembro do ano-calendário da declaração, que não tenham nascimento informado o CPF. 3.8. Registro de informação de reembolso do dependente (identificador RDTOP)

- Deve estar classificado em ordem crescente por CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo DTOP; - Só deverá constar o registro se houver valor de reembolso do ano-calendário e de anos- calendário anteriores. Ordem Campo Formato Preenchimento Tamanho Valores Válidos Obrigatório

1 C Fixo 5 RDTOP Sim

CPF com 11 CPF/CNPJ do dígitos; 2 prestador de N Variável 14 Sim CNPJ com 14 serviço dígitos. Nome/Nome Nome da pessoa Empresarial do 3 C Variável 150 física até 60 Sim prestador de posições; serviço Nome empresarial da pessoa jurídica até 150 posições. Valor do 4 reembolso do N Variável 9 - Não ano-calendário Valor do 5 reembolso de N Variável 9 - Não anos anteriores

Valor do Valores reembolsados no ano-calendário, referentes a pagamentos 4 reembolso do de serviços prestados no ano-calendário. ano-calendário Valor do Valores reembolsados no ano-calendário referentes a pagamentos 5 reembolso de de serviços prestados em anos anteriores. anos anteriores 3.9 - Registro de informação do prestador de serviço de saúde (identificador PSS)

- Ocorre caso o declarante seja prestador de serviço de saúde. - Ocorre somente uma vez no arquivo.

Identificador 1 C Fixo 3 PSS Sim de registro

Preenchimento obrigatório se o campo de ordem 4 - Tipo do Declarante, do registro DECPJ igual a "1"; Identificador 1 Preenchimento opcional se o campo de ordem 4 - Tipo do Declarante, de registro do registro DECPJ igual a "3", e o declarante não exerceu atividades de Prestador de Serviços de Saúde no ano-calendário. 3.10 - Registro de informação do responsável pelo pagamento ao prestador do serviço de saúde

(identificador RPPSS)

- Deve estar classificado em ordem crescente por CPF do responsável pelo pagamento; - Deve estar associado ao registro do tipo PSS.

1 Identificador de registro C Fixo 5 RPPSS Sim CPF do responsável 2 N Fixo 11 - Sim pelo pagamento 3 Nome C Variável 60 - Sim Valor pago no ano pelo 4 responsável em N Variável 9 - Não benefício próprio

Valor pago no ano pelo Preenchimento obrigatório se não existir registro BRPPSS 4 responsável em associado ao RPPSS. benefício próprio 3.11 - Registro de informação de beneficiário do serviço pago (identificador BRPPSS)

- Deve estar classificado em ordem crescente por CPF e Data de nascimento do beneficiário; - Deve estar associado ao registro do tipo RPPSS.

1 C Fixo 6 BRPPSS Sim

CPF do 2 N Fixo 11 - Não beneficiário Data de 3 D Fixo 8 - Não nascimento 4 Nome C Variável 60 - Sim Valor pago no 5 ano com o N Variável 9 >0 Sim beneficiário

Data de Preenchimento obrigatório para o beneficiário do serviço de saúde

nascimento que não informar o número do CPF quando da prestação do serviço. 3.12 - Registro identificador do término da declaração (identificador FIMDmed)

- Registro obrigatório no arquivo; - Deve ser o último registro no arquivo; - Ocorre somente uma vez no arquivo.

1 C Fixo 7 FIMDmed Sim

4 - Tabela de relação de dependência

Código Descrição 03 Cônjuge/companheiro 04 Filho/filha 06 Enteado/enteada 08 Pai/mãe 10 Agregado/outros

