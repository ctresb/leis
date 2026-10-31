---
titulo: "Ato Declaratório Executivo Cofis nº 90, de 25 de novembro de 2016"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "90"
data: "2016-11-25"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 28/11/2016, seção 1, página 91"
data_publicacao: "2016-11-28"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/78887/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/78887/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "78887"
sha256_texto: "a72b9dde4e0677977c6c327513d862bba92acc82af0611dd3b78eabbc5dd63a1"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Cofis nº 90, de 25 de novembro de 2016

Dispõe sobre o leiaute do Programa Gerador da Declaração do Imposto sobre a Renda Retido na Fonte (PGD Dirf 2017).

O COORDENADOR-GERAL DE FISCALIZAÇÃO SUBSTITUTO, no uso das atribuições que lhe confere o inciso III do art. 312 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 203, de 14 de maio de 2012, e tendo em vista o disposto na Instrução Normativa RFB nº 1.671, de 22 de novembro de 2016, declara:

**Art.1** Fica aprovado o leiaute aplicável aos campos, registros e arquivos da Declaração do Imposto sobre a Renda Retido na Fonte (Dirf 2017), constante no anexo único a este Ato Declaratório.

**Art.2** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

JORDÃO NÓBRIGA DA SILVA JUNIOR

## ANEXO



## ANEXO

LEIAUTE DO ARQUIVO Declaração do Imposto sobre a Renda Retido na Fonte – Dirf

1. Regras gerais Estas regras devem ser respeitadas em todos os arquivos gerados, quando não excepcionadas por regra específica referente a um dado registro e explicitada em suas observações.

Nº Regra de Descrição preenchimento

ALFANUMÉRICO (C): representados por “C” - todos os caracteres, excetuados o caractere “|” (pipe ou barra vertical). 1 Formato dos campos NUMÉRICO (N): representados por “N” – pode conter apenas os valores de zero a nove.

Campos numéricos (D) Devem ser informados conforme o padrão ano, mês e dia (AAAAMMDD), excluindo-se 2 cujo conteúdo quaisquer caracteres de separação (tais como “.”, “/”, “-”, etc.); representa data

Os campos numéricos com número de inscrição (CNPJ e CPF) ou códigos de receita Campos numéricos deverão ser informados com todos os dígitos, inclusive os zeros à esquerda; com número de

inscrição ou códigos de receita As máscaras (caracteres especiais de formatação, tais como “.”, “/”, “-”, etc.) não devem ser informadas.

Devem ser informados com até 13 posições, representando 11 posições inteiras e 2 decimais;

Campos numéricos Os zeros não significativos não devem ser informados;

referentes a valores Os caracteres ‘.’ (ponto) e ‘,’ (vírgula) não devem ser informados;

Todos os valores monetários devem estar expressos em reais.

Os campos com conteúdo alfanumérico nos quais se faz necessário registrar números Campos alfanuméricos ou códigos de identificação (Exemplo: Número de Identificação Fiscal - NIF) deverão com números ou seguir a regra de formação e tamanho definidos pelo respectivo órgão regulador;

códigos de identificação As máscaras (caracteres especiais de formatação, tais como “.”, “/”, “-”, etc.) não devem ser informadas.

Ao final de cada campo (inclusive o último de cada registro) deve ser inserido o caractere delimitador “|” (pipe ou barra vertical: caractere 124 da Tabela ASCII);

O caractere delimitador “|” (barra vertical) não deve ser incluído como parte integrante do 6 Formação dos campos conteúdo de quaisquer campos numéricos, datas ou alfanuméricos;

Na ausência de informação, o campo vazio (campo sem conteúdo, nulo e com valor zero) deverá ser iniciado com o caractere “|” (barra vertical) e imediatamente encerrado com o mesmo caractere “|” (barra vertical) delimitador de campo.

Formação dos 7 Cada registro deve necessariamente ocupar apenas uma linha no arquivo. registros

8 Preenchimento dos Preenchimento fixo: o campo deve ser preenchido com o tamanho exato.

campos Preenchimento variável: o campo pode ter variação de tamanho de preenchimento.

Campo numérico Deve ser informado com até 4 posições, representando 3 posições inteiras e 1 decimal; referente a quantidade 9 de meses Os zeros não significativos não devem ser informados;

Os caracteres ‘.’ (ponto) e ‘,’ (vírgula) não devem ser informados.

2. Estrutura de arquivo 2.1 Estrutura completa de uma declaração de Pessoa Física

Dirf - Declaração do imposto sobre a renda retido na fonte

RESPO - Responsável pelo preenchimento

DECPF - Declarante pessoa física

IDREC - Identificação do código de receita

BPFDEC - Beneficiário pessoa física do declarante

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial

RTDP - Rendimentos Tributáveis - Dedução – Dependentes

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

CJAC - Compensação de Imposto por Decisão Judicial - Ano-calendário

CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores

ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável

ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial

ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes

ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte

ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial

INFPC - Informações de Previdência Complementar

RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada

RTFA - Rendimentos Tributáveis - Dedução - FAPI

ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada

ESFA - Tributação com Exigibilidade Suspensa - Dedução – FAPI

INFPA – Informações do beneficiário da pensão alimentícia

RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia

ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia

RIDAC - Rendimentos Isentos - Diária e Ajuda de Custo

RIIRP - Rendimentos Isentos - Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV

RIAP - Rendimentos Isentos - Abono Pecuniário

RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria para Maiores de 65 anos

RIO - Rendimentos Isentos Anuais – Outros

BPJDEC - Beneficiário pessoa jurídica do declarante

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

RRA - Rendimentos recebidos acumuladamente

IDREC - Identificação do código de receita

BPFRRA - Beneficiário pessoa física do rendimento recebido acumuladamente

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

DAJUD - Despesa com ação judicial

QTMESES - Quantidade de meses

INFPA – Informações do beneficiário da pensão alimentícia

RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia

SCP - Informações da sociedade em conta de participação

BPFSCP - Beneficiário pessoa física da sociedade em conta de participação

RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação

BPJSCP - Beneficiário pessoa jurídica da sociedade em conta de participação

RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação

PSE - Plano privado de assistência à saúde - coletivo empresarial

OPSE - Operadora de plano privado de assistência à saúde - coletivo empresarial

TPSE - Titular de plano privado de assistência à saúde - coletivo empresarial

RTPSE – Reembolso do titular do plano de assistência à saúde - coletivo empresarial

DTPSE - Dependente do titular de plano privado de assistência à saúde - coletivo empresarial

RDTPSE – Reembolso do dependente do titular do plano de assistência à saúde - coletivo empresarial

RPDE - Rendimentos pagos a residentes ou domiciliados no exterior

BRPDE - Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior

VRPDE - Valores de rendimentos pagos a residentes ou domiciliados no exterior

INF - Informações complementares para o comprovante de rendimentos

FIMDirf - Término da declaração

2.2 Estrutura completa de uma declaração de Pessoa Jurídica

Dirf - Declaração do imposto sobre a renda retido na fonte

RESPO - Responsável pelo preenchimento

DECPJ - Declarante pessoa jurídica

IDREC - Identificação do código de receita

BPFDEC - Beneficiário pessoa física do declarante

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial

RTDP - Rendimentos Tributáveis - Dedução - Dependentes

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

CJAC - Compensação de Imposto por Decisão Judicial - Ano-calendário

CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores

ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável

ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial

ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes

ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte

ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial

INFPC - Informações de Previdência Complementar

RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada

RTFA - Rendimentos Tributáveis - Dedução - FAPI

RTSP - Rendimentos Tributáveis - Dedução - Fundo de Previdência do Servidor Público

RTEP - Rendimentos Tributáveis - Dedução - Contribuição do ente público patrocinador

ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada

ESFA - Tributação com Exigibilidade Suspensa - Dedução – FAPI

ESSP - Tributação com Exigibilidade Suspensa - Dedução - Fundo de Previdência do Servidor Público

ESEP - Tributação com Exigibilidade Suspensa - Dedução - Contribuição do ente público patrocinador

INFPA – Informações do beneficiário da pensão alimentícia

RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia

ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia

RIDAC - Rendimentos Isentos - Diária e Ajuda de Custo

RIIRP - Rendimentos Isentos - Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV

RIAP - Rendimentos Isentos - Abono Pecuniário

RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave

RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria para Maiores de 65 anos

RIBMR - Rendimentos Isentos - Bolsa de Estudo Recebida por Médico-Residente

RICAP - Rendimentos Isentos - Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de

1989 a 31 de dezembro de 1995

RIL96 - Rendimentos Isentos Anuais - Lucros e dividendos pagos a partir de 1996

RIPTS - Rendimentos Isentos Anuais - Valores pagos a titular ou sócio ou empresa de pequeno porte, exceto pró-labore e aluguéis

RIO - Rendimentos Isentos Anuais – Outros

BPJDEC - Beneficiário pessoa jurídica do declarante

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

FCI - Fundo ou clube de investimento

IDREC - Identificação do código de receita

BPFFCI - Beneficiário pessoa física do fundo ou clube de investimento

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

CJAC - Compensação de Imposto por Decisão Judicial – Ano-calendário

CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores

ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável

ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte

ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial

RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria para Maiores de 65 anos

RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave

RICAP - Rendimentos Isentos - Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995

RIO - Rendimentos Isentos Anuais - Outros

BPJFCI - Beneficiário pessoa jurídica do fundo ou clube de investimento

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

PROC - Processo da justiça do trabalho/federal/estadual/Distrito Federal

IDREC - Identificação do código de receita

BPFPROC - Beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial

RTDP - Rendimentos Tributáveis - Dedução - Dependentes

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

CJAC - Compensação de Imposto por Decisão Judicial – Ano-calendário

CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores

ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável

ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial

ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes

ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte

ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial

INFPC - Informações de Previdência Complementar

RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada

RTFA - Rendimentos Tributáveis - Dedução - FAPI

RTSP - Rendimentos Tributáveis - Dedução - Fundo de Previdência do Servidor Público

ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada

ESFA - Tributação com Exigibilidade Suspensa - Dedução – FAPI

ESSP - Tributação com Exigibilidade Suspensa - Dedução - Fundo de Previdência do Servidor Público

INFPA – Informações do beneficiário da pensão alimentícia

RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia

ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia

RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave

RIRSR – Rendimentos Isentos Anuais – Rendimentos pagos sem retenção do IR na fonte –

Lei nº 10.833/2003

BPJPROC - Beneficiário pessoa jurídica do processo da justiça do

trabalho/federal/estadual/Distrito Federal

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

RIRSR – Rendimentos Isentos Anuais – Rendimentos pagos sem retenção do IR na fonte –

Lei nº 10.833/2003

RRA - Rendimentos recebidos acumuladamente

IDREC - Identificação do código de receita

BPFRRA - Beneficiário pessoa física do rendimento recebido acumuladamente

RTRT - Rendimentos Tributáveis - Rendimento Tributável

RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial

RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte

RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave

RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria para Maiores de 65 anos

DAJUD - Despesa com ação judicial

QTMESES - Quantidade de meses

INFPA – Informações do beneficiário da pensão alimentícia

RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia

SCP - Informações da sociedade em conta de participação

BPFSCP - Beneficiário pessoa física da sociedade em conta de participação

RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação

BPJSCP - Beneficiário pessoa jurídica da sociedade em conta de participação

RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação

PSE - Plano privado de assistência à saúde - coletivo empresarial

OPSE - Operadora de plano privado de assistência à saúde - coletivo empresarial

TPSE - Titular de plano privado de assistência à saúde - coletivo empresarial

RTPSE – Reembolso do titular do plano de assistência à saúde - coletivo empresarial

DTPSE - Dependente do titular de plano privado de assistência à saúde - coletivo empresarial

RDTPSE – Reembolso do dependente do titular do plano de assistência à saúde - coletivo empresarial

RPDE - Rendimentos pagos a residentes ou domiciliados no exterior

BRPDE - Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior

VRPDE - Valores de rendimentos pagos a residentes ou domiciliados no exterior

INF - Informações complementares para o comprovante de rendimentos

FIMDirf - Término da declaração

3. Leiaute do arquivo 3.1 Registro de identificação da declaração (identificador Dirf)

- Registro obrigatório no arquivo;

- Deve ser o primeiro registro no arquivo;

- Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 4 Dirf Sim

2 Ano referência N Fixo 4 2017 Sim

3 Ano-calendário N Fixo 4 2016 ou 2017 Sim

S - Retificadora 4 Indicador de retificadora C Fixo 1 Sim N – Original

5 Número do recibo N Fixo 12 - Não

Identificador de estrutura do 6 C Fixo 7 P49VS72 Sim leiaute

Observações:

Ordem Campo Descrição

O preenchimento será obrigatório se o campo de ordem 4 igual a “S” e 5 Número do recibo declaração transmitida sem o uso de certificação digital.

3.2 Registro do Responsável pelo preenchimento da declaração (identificador RESPO)

- Registro obrigatório no arquivo;

- Deve ser o segundo registro no arquivo;

- Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 5 RESPO Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 DDD N Fixo 2 - Sim

5 Telefone N Variável 9 - Sim

6 Ramal N Variável 6 - Não

7 Fax N Variável 9 - Não

8 Correio eletrônico C Variável 50 - Não

Observações:

Ordem Campo Descrição

4 DDD O primeiro algarismo deve ser diferente de zero.

5 Telefone Deve ser preenchido com oito ou nove algarismos.

7 Fax Deve ser preenchido com oito ou nove algarismos.

3.3 Registro de identificação do declarante pessoa física (identificador DECPF)

- Registro obrigatório no arquivo para declarante pessoa física;

- Deve ser o terceiro registro no arquivo;

- Ocorre somente uma vez no arquivo;

- Não pode ser informado se existir o registro tipo DECPJ.

1 Identificador de registro C Fixo 5 DECPF Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Indicador de declarante de C Fixo 1 S - Pagou Sim rendimentos pagos a residentes ou domiciliados no exterior rendimentos a residentes ou domiciliados no exterior.

N - Não pagou rendimentos a residentes ou domiciliados no exterior.

5 Indicador de Titular de Serviços C Fixo 1 S – Titular de serviços Sim Notariais e de Registros notariais e de registros.

N – Não é titular de serviços notariais e de registros.

6 Indicador de plano privado de C Fixo 1 S – Existe pagamento de Sim assistência à saúde - coletivo valor pelo empresarial titular/dependente do plano de saúde.

N – Não existe pagamento de valor pelo titular/dependente do plano de saúde.

7 Indicador de sócio ostensivo C Fixo 1 S - Sócio ostensivo. Sim responsável por sociedade em conta de participação - SCP N - Não é sócio ostensivo.

8 Indicador de situação especial da C Fixo 1 S - Encerramento de Sim declaração espólio/saída definitiva do país.

N - Não é encerramento de espólio/saída definitiva do país

9 Data do Evento D Fixo 8 - Não

10 Tipo de Evento N Fixo 1 1 - Encerramento de Não espólio.

2 - Saída definitiva do Brasil.

Observações:

Ordem Campo Descrição

8 Data do Evento O preenchimento será obrigatório se o campo de ordem 7 igual a “S”.

9 Tipo de Evento O preenchimento será obrigatório se o campo de ordem 7 igual a “S”.

3.4 Registro de identificação do declarante pessoa jurídica (identificador DECPJ)

- Registro obrigatório no arquivo para declarante pessoa jurídica;

- Deve ser o terceiro registro no arquivo;

- Ocorre somente uma vez no arquivo;

- Não pode ser informado se existir o registro tipo DECPF.

Orde Campo Formato Preenchimento Tamanho Valores válidos Obrigatório m

1 Identificador de registro C Fixo 5 DECPJ Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

4 Natureza do declarante N Fixo 1 0 - Pessoa jurídica de Sim direito privado.

1 - Órgãos, autarquias e fundações da administração pública federal.

2 - Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal.

3 – Empresa pública ou sociedade de economia mista federal.

4 - Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal.

8 – Entidade com alteração de natureza jurídica (uso restrito).

5 CPF responsável perante o CNPJ N Fixo 11 - Sim

6 Indicador de sócio ostensivo C Fixo 1 S - Sócio ostensivo. Sim responsável por sociedade em conta de participação - SCP N - Não é sócio ostensivo.

7 Indicador de declarante C Fixo 1 S - Depositário de crédito Sim depositário de crédito decorrente decorrente de decisão de decisão judicial judicial.

N – Não é depositário de crédito decorrente de decisão judicial.

8 Indicador de declarante de C Fixo 1 S - Instituição Sim instituição administradora ou administradora ou intermediadora de fundo ou clube intermediadora de fundo de investimento ou clube de investimento.

N – Não é instituição administradora ou intermediadora de fundo ou clube de investimento.

9 Indicador de declarante de C Fixo 1 S - Pagou rendimentos a Sim rendimentos pagos a residentes residentes ou domiciliados ou domiciliados no exterior no exterior.

N - Não pagou rendimentos a residentes ou domiciliados no exterior.

10 Indicador de plano privado de C Fixo 1 S – Existe pagamento de Sim assistência à saúde - coletivo valor pelo empresarial titular/dependente do plano de saúde.

N – Não existe pagamento de valor pelo titular/dependente do plano de saúde.

11 Indicador de pagamentos C Fixo 1 S - Existe pagamento Sim relacionados aos Jogos relacionado às Olimpíadas. Olímpicos de 2016 e aos Jogos Paraolímpicos de 2016 N - Não existe pagamento relacionado às Olimpíadas.

12 Indicador de situação especial da C Fixo 1 S - Declaração de situação Sim declaração especial.

N - Não é declaração de situação especial.

13 Data do evento D Fixo 8 - Não

Observações:

Ordem Campo Descrição

4 Natureza do Relativamente à natureza do declarante 8 – Entidade com alteração de natureza jurídica declarante (uso restrito), esclarecemos:

1. para declarante que alterou sua natureza jurídica em relação ao ano-calendário e que implique em mudança da natureza do declarante na ficha Informações da Dirf;

2. para declarante que mudou sua natureza jurídica de órgão público para privado, ou vice-versa. Aplica-se ainda para mudanças entre as esferas governamentais da federação. Por exemplo: órgão público ou pessoa jurídica de direito privado estadual ou municipal que passou a ser federal, ou vice-versa;

3. a declaração deverá ser entregue na RFB.

13 Data do evento O preenchimento será obrigatório se o campo de ordem 12 igual a “S”.

3.5 Registro de identificação do código de receita (identificador IDREC)

- Deve ser apresentado com os códigos de receita em ordem crescente;

- Deve estar associado aos registros do tipo DECPF, DECPJ, FCI, PROC ou RRA.

1 Identificador de C Fixo 5 IDREC Sim registro

2 Código de receita N Fixo 4 De acordo com a tabela de Sim códigos de receitas constante na IN que dispõe sobre a Dirf.

3.6 Registro de beneficiário pessoa física do declarante (identificador BPFDEC)

- Serão apresentados todos os CPF em ordem crescente;

- Devem ser apresentados antes dos registros com identificador BPJDEC, caso exista o registro;

- Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFDEC Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Data atribuída pelo laudo da D Fixo 8 - Não moléstia grave

3.7 Registro de beneficiário pessoa jurídica do declarante (identificador BPJDEC)

- Serão apresentados todos os CNPJ em ordem crescente;

- Devem ser apresentados depois dos registros com identificador BPFDEC, caso exista o registro;

- Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPJDEC Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

3.8 Registro de identificação do fundo ou clube de investimento (identificador FCI)

- Serão apresentados todos os CNPJ em ordem crescente;

- Deve estar associado ao registro do tipo DECPJ.

1 Identificador de registro C Fixo 3 FCI Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

3.9 Registro do beneficiário pessoa física do fundo ou clube de investimento (identificador BPFFCI)

- Serão apresentados todos os CPF em ordem crescente;

- Devem ser apresentados antes dos registros com identificador BPJFCI, caso exista o registro;

- Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFFCI Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Data atribuída pelo laudo da D Fixo 8 - Não moléstia grave

3.10 Registro do beneficiário pessoa jurídica do fundo ou clube de investimento (identificador BPJFCI)

- Serão apresentados todos os CNPJ em ordem crescente;

- Devem ser apresentados depois dos registros com identificador BPFFCI, caso exista o registro;

- Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPJFCI Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

3.11 Registro de processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador PROC)

- Deve estar classificado em ordem crescente por:

- Tipo de justiça;

- Número do processo;

- Deve estar associado ao registro do tipo DECPJ.

Orde Tamanh Campo Formato Preenchimento Valores válidos Obrigatório m o

1 Identificador de registro C Fixo 4 PROC Sim

2 Indicador de Justiça N Fixo 1 1 - Justiça federal Sim

2 - Justiça do trabalho

3 - Justiça estadual/Distrito Federal

3 Número do processo C Variável 20 - Sim

4 Indicador de tipo de N Fixo 1 1 - Pessoa física Não advogado/escritório de advocacia 2 - Pessoa jurídica

5 CPF do advogado/ CNPJ do N Variável 14 CPF com 11 dígitos Não escritório de advocacia CNPJ com 14 dígitos

6 Nome do advogado/ Nome C Variável 150 Nome da pessoa física Não empresarial do escritório de até 60 posições. advocacia Nome empresarial da pessoa jurídica até 150 posições.

7 Valor pago para o advogado N Variável 13 Valor pago para o Não advogado

3.12 Registro de beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPFPROC)

- Serão apresentados todos os CPF em ordem crescente;

- Devem ser apresentados antes dos registros com identificador BPJPROC, caso exista o registro;

- Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 7 BPFPROC Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Data atribuída pelo laudo da D Fixo 8 - Não

moléstia grave

3.13 Registro de beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPJPROC)

- Serão apresentados todos os CNPJ em ordem crescente;

- Devem ser apresentados depois dos registros com identificador BPFPROC, caso exista o registro;

- Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 7 BPJPROC Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

3.14 Registro de rendimentos recebidos acumuladamente (identificador RRA)

- Deve estar classificado em ordem crescente por:

- Indicador de rendimento recebido acumuladamente;

- Número do processo.

Orde Tamanh Campo Formato Preenchimento Valores válidos Obrigatório m o

1 Identificador de registro C Fixo 3 RRA Sim

2 Identificador de rendimento recebido N Fixo 1 1 - Pago pelo declarante Sim acumuladamente 2 - Pago pela justiça

3 Número do processo/requerimento C Variável 20 - Não

4 Indicador de tipo de N Fixo 1 1 - Pessoa física Não advogado/escritório de advocacia 2 - Pessoa jurídica

5 CPF do advogado/CNPJ do N Variável 14 CPF com 11 dígitos Não escritório de advocacia

CNPJ com 14 dígitos

6 Nome do advogado/Nome C Variável 150 Nome da pessoa física Não empresarial do escritório de com até 60 posições. advocacia Nome empresarial da pessoa jurídica com até 150 posições.

7 Valor pago para o advogado N Variável 13 Valor pago para o Não advogado

Observações:

Ordem Campo Descrição

3 Número do processo/requerimento O preenchimento será obrigatório se o campo de ordem 2 igual a 2.

3.15 Registro de beneficiário pessoa física dos rendimentos recebidos acumuladamente (identificador BPFRRA)

- Deve estar classificado em ordem crescente por:

- CPF;

- Natureza do RRA;

- Deve estar associado ao registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFRRA Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Natureza do RRA C Variável 50 - Não

5 Data atribuída pelo laudo da D Fixo 8 - Não moléstia grave

3.16 Registro de identificação de Previdência Complementar (identificador INFPC)

- Serão apresentados todos os CNPJ em ordem crescente;

- Deve estar associado ao registro do tipo BPFDEC ou BPFPROC;

- Deve constar um registro INFPC para cada CNPJ de entidade de previdência complementar.

1 Identificador de registro C Fixo 5 INFPC Sim

2 CNPJ N Fixo 14 - Não

3 Nome empresarial C Variável 150 - Não

3.17 Registro de informações do beneficiário da pensão alimentícia (identificador INFPA)

- Deve estar classificado em ordem crescente de CPF e data de nascimento;

- Deve estar associado ao registro do tipo BPFDEC, BPFPROC, BPFRRA.

1 Identificador de registro C Fixo 5 INFPA Sim

2 CPF do alimentando N Fixo 11 - Não

3 Data de nascimento D Fixo 8 - Não

4 Nome C Variável 60 - Sim

03 – Cônjuge/ Companheiro (a)

04 – Filho (a)

5 Relação de dependência N Fixo 2 Não 06 – Enteado (a)

08 – Pai/Mãe

10 – Agregado/ Outros

Observações:

Ordem Campo Descrição

CPF do alimentando Preenchimento obrigatório para maiores de 18 anos completos até 31 de dezembro

do ano-calendário da declaração.

3 Data de nascimento Preenchimento obrigatório para menores de 18 anos completos até 31 de dezembro

do ano-calendário da declaração, que não tenham informado o CPF.

3.18 Registro de valores mensais (identificadores RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTIRF, CJAA, CJAC, ESRT, ESPO, ESPP, ESFA, ESSP, ESEP, ESDP, ESPA, ESIR, ESDJ, RIP65, RIDAC, RIIRP, RIAP, RIMOG, RIVC, RIBMR, RICAP, RISCP e DAJUD)

- Deve ocorrer apenas se houver pelo menos um dos valores referente aos meses ou 13º salário;

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário;

- Deve estar associado aos registros dos tipos BPFDEC, BPJDEC, BPFFCI, BPJFCI, BPFPROC, BPJPROC, BPFRRA, BPFSCP, BPJSCP, INFPC, INFPA.

1 Identificador de registro C Variável 5 RTRT Sim

RTPO

RTPP

RTFA

RTSP

RTEP

RTDP

RTPA

RTIRF

CJAC

CJAA

ESRT

ESPO

ESPP

ESFA

ESSP

ESEP

ESDP

ESPA

ESIR

ESDJ

RIP65

RIDAC

RIIRP

RIAP

RIMOG

RIVC

RIBMR

RICAP

RISCP

DAJUD

2 Janeiro N Variável 13 - Não

3 Fevereiro N Variável 13 - Não

4 Março N Variável 13 - Não

5 Abril N Variável 13 - Não

6 Maio N Variável 13 - Não

7 Junho N Variável 13 - Não

8 Julho N Variável 13 - Não

9 Agosto N Variável 13 - Não

10 Setembro N Variável 13 - Não

11 Outubro N Variável 13 - Não

12 Novembro N Variável 13 - Não

13 Dezembro N Variável 13 - Não

14 Décimo Terceiro N Variável 13 - Não

3.19 Registro de valores anuais isentos (identificadores RIL96, RIPTS e RIRSR)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário;

- Deve estar associado aos registros dos tipos BPFDEC ou BPFPROC.

RIL96

1 Identificador de registro C Fixo 5 RIPTS Sim

RIRSR

2 Valor pago no ano N Variável 13 - Sim

3.20 Registro de valores anuais de rendimentos isentos - outros (identificador RIO)

- Ocorrerá apenas um registro para cada beneficiário;

- Deve estar associado ao registro do tipo BPFDEC ou BPFFCI.

1 Identificador de registro C Fixo 3 RIO Sim

2 Valor pago no ano N Variável 13 - Sim

3 Descrição dos rendimentos C Variável 60 - Sim isentos - outros

3.21 Registro de quantidade de meses (identificador QTMESES)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário;

- Deve estar associado ao registro do tipo BPFRRA.

1 Identificador de registro C Fixo 7 QTMESES Sim

2 Quantidade meses – janeiro N Variável 4 - Não

3 Quantidade meses – fevereiro N Variável 4 - Não

4 Quantidade meses – março N Variável 4 - Não

5 Quantidade meses – abril N Variável 4 - Não

6 Quantidade meses – maio N Variável 4 - Não

7 Quantidade meses – junho N Variável 4 - Não

8 Quantidade meses – julho N Variável 4 - Não

9 Quantidade meses – agosto N Variável 4 - Não

10 Quantidade meses – setembro N Variável 4 - Não

11 Quantidade meses – outubro N Variável 4 - Não

12 Quantidade meses – novembro N Variável 4 - Não

13 Quantidade meses – dezembro N Variável 4 - Não

3.22 Registro de informações da Sociedade em Conta de Participação (identificador SCP)

- Serão apresentados em ordem crescente de CNPJ.

- Deve constar um registro para cada CNPJ de Sociedade em conta de participação

1 Identificador de registro C Fixo 3 SCP Sim

2 CNPJ da Sociedade em Conta N Fixo 14 - Sim de Participação

3 Nome empresarial da Sociedade C Variável 150 - Sim em Conta de Participação

3.23 Registro de beneficiário pessoa física da sociedade em conta de participação (identificador BPFSCP)

- Serão apresentados todos os CPF em ordem crescente;

- Devem ser apresentados antes dos registros com identificador BPJSCP, caso exista o registro;

- Deve estar associado a um registro do tipo SCP.

1 Identificador de registro C Fixo 6 BPFSCP Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Percentual de participação na C Variável 4 - Não SCP

3.24 Registro de beneficiário pessoa jurídica da sociedade em conta de participação (identificador BPJSCP)

- Serão apresentados todos os CNPJ em ordem crescente;

- Devem ser apresentados depois dos registros com identificador BPFSCP, caso exista o registro;

- Deve estar associado a um registro do tipo SCP.

1 Identificador de registro C Fixo 6 BPJSCP Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

4 Percentual de participação na C Variável 4 - Não SCP

3.25 Registro de pagamentos a plano privado de assistência à saúde - coletivo empresarial (identificador PSE)

- Ocorre somente uma vez no arquivo, caso exista informação de valores pagos pelo titular/dependente do plano de assistência à saúde.

1 Identificador de registro C Fixo 3 PSE Sim

3.26 Registro de operadora do plano privado de assistência à saúde - coletivo empresarial (identificador OPSE)

- Ocorre caso exista o registro PSE;

- Serão apresentados todos os CNPJ em ordem crescente.

1 Identificador de registro C Fixo 4 OPSE Sim

CNPJ da operadora de plano 2 privado de assistência à saúde - N Fixo 14 - Sim coletivo empresarial

3 Nome empresarial C Variável 150 - Sim

4 Registro ANS N Fixo 6 - Sim

3.27 Registro de titular do plano privado de assistência à saúde - coletivo empresarial (identificador TPSE)

- Serão apresentados todos os CPF em ordem crescente.

- Deve estar associado ao registro do tipo OPSE.

1 Identificador de registro C Fixo 4 TPSE Sim

2 CPF do titular N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Valor pago no ano N Variável 13 - Sim

3.28 Registro de informação de reembolso do titular do plano de saúde – coletivo empresarial (identificador RTPSE)

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ);

- Deve estar associado ao registro do tipo TPSE;

- Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos-calendário anteriores.

Ordem Campo Formato Preenchimento Tamanho Valores Válidos Obrigatório

1 Identificador de registro C Fixo 5 RTPSE Sim

CPF/CNPJ do prestador de CPF com 11 dígitos; 2 serviço N Variável 14 Sim CNPJ com 14 dígitos.

Nome/Nome empresarial Nome da pessoa física do prestador de serviço até 60 posições. 3 C Variável 150 Sim Nome empresarial da pessoa jurídica até 150 posições.

Valor do reembolso do ano- - 4 N Variável 9 Não calendário

Valor do reembolso de - 5 N Variável 9 Não anos anteriores

Observações:

Ordem Campo Descrição

Valor do reembolso do ano-calendário Valores reembolsados no ano-calendário, referentes a pagamentos

de serviços prestados no ano-calendário.

Valor do reembolso de anos Valores reembolsados no ano-calendário referentes a pagamentos

anteriores de serviços prestados em anos anteriores.

3.29 Registro de dependente do plano privado de assistência à saúde - coletivo empresarial (identificador DTPSE)

- Deve estar classificado em ordem crescente de CPF e data de nascimento;

- Deve estar associado ao registro do tipo TPSE.

1 Identificador de registro C Fixo 5 DTPSE Sim

2 CPF do dependente N Fixo 11 - Não

3 Data de nascimento D Fixo 8 - Não

4 Nome C Variável 60 - Sim

03 - Cônjuge/ Companheiro(a) 5 Relação de dependência N Fixo 2 Não 04 - Filho(a)

06 - Enteado(a)

08 - Pai/Mãe

10 - Agregado/ Outros

6 Valor pago no ano N Variável 13 - Sim

Observações:

Ordem Campo Descrição

CPF do dependente Preenchimento obrigatório para maiores de 18 anos completos até 31 de dezembro

do ano-calendário da declaração.

Data de nascimento Preenchimento obrigatório para menores de 18 anos completos até 31 de dezembro

do ano-calendário da declaração, que não tenham informado o CPF.

3.30 - Registro de informação de reembolso do dependente (identificador RDTPSE):

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ);

- Deve estar associado ao registro do tipo DTPSE;

- Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos-calendário anteriores.

Ordem Campo Formato Preenchimento Tamanho Valores Válidos Obrigatório

1 Identificador de registro C Fixo 6 RDTPSE Sim

CPF/CNPJ do prestador de CPF com 11 dígitos; 2 serviço N Variável 14 Sim CNPJ com 14 dígitos.

Nome/Nome Empresarial do Nome da pessoa física prestador de serviço até 60 posições; 3 C Variável 150 Sim Nome empresarial da pessoa jurídica até 150 posições.

Valor do reembolso do ano- 4 N Variável 9 - Não calendário

Valor do reembolso de anos 5 N Variável 9 - Não anteriores

Observações:

Ordem Campo Descrição

4 Valor do reembolso do ano- Valores reembolsados no ano-calendário, referentes a pagamentos de serviços

calendário prestados no ano-calendário.

Valor do reembolso de anos Valores reembolsados no ano-calendário referentes a pagamentos de serviços

anteriores prestados em anos anteriores.

3.31 Registro de rendimentos pagos a residentes ou domiciliados no exterior (identificador RPDE)

- Ocorre somente uma vez no arquivo, caso exista informação de rendimentos pagos a residentes ou domiciliados no exterior

1 Identificador de registro C Fixo 4 RPDE Sim

3.32 Registro de beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior (identificador BRPDE)

- Deve estar classificado em ordem crescente por:

- Beneficiário;

- Código de país;

- Número de identificação fiscal - NIF;

- Deve estar associado ao registro do tipo RPDE.

1 Identificador de registro C Fixo 5 BRPDE Sim

1 - Pessoa física 2 Beneficiário N Fixo 1 Sim 2 - Pessoa jurídica

De acordo com a tabela de código dos 3 Código de país N Variável 3 países constante na Sim IN que dispõe sobre a Dirf

Número de identificação fiscal 4 C Variável 30 - Não – NIF

5 Indicador de beneficiário C Fixo 1 S - Dispensado do Sim dispensado do Número de Número de identificação fiscal - NIF

N - Não é dispensado do Número de Identificação Fiscal - NIF identificação fiscal - NIF

S - Dispensado do Número de identificação fiscal - Indicador de que o país não NIF 6 exige Número de Identificação C Fixo 1 Sim Fiscal - NIF N - Não é dispensado do Número de identificação fiscal - NIF

CPF com 11 dígitos. 7 CPF/CNPJ N Variável 14 Não CNPJ com 14 dígitos.

8 Nome/Nome empresarial C Variável 150 - Sim

De acordo com a tabela de informações Relação fonte pagadora sobre os beneficiários 9 pessoa jurídica e beneficiário N Fixo 3 Não dos rendimentos pessoa jurídica constante na IN que dispõe sobre a Dirf

10 Logradouro C Variável 60 - Não

11 Número C Variável 6 - Não

12 Complemento C Variável 25 - Não

13 Bairro/Distrito C Variável 20 - Não

14 Código postal N Variável 10 - Não

15 Cidade C Variável 40 - Não

16 Estado/Província C Variável 40 - Não

17 Telefone N Variável 15 - Não

Observações:

Ordem Campo Descrição

Relação fonte pagadora pessoa jurídica e Preenchimento obrigatório se campo de ordem 2 (Beneficiário)

beneficiário pessoa jurídica igual a 2.

3.33 Registro de valores de rendimentos pagos a residentes ou domiciliados no exterior (identificador VRPDE)

- Deve estar classificado em ordem crescente por:

- Data do pagamento;

- Código de receita;

- Deve estar associado ao registro do tipo BRPDE.

Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 Identificador de registro C Fixo 5 VRPDE Sim

2 Data do pagamento D Fixo 8 - Sim

3 Código de receita N Fixo 4 - Sim

De acordo com a tabela de informações sobre os 4 Tipo de rendimento N Fixo 3 Sim rendimentos constante na IN que dispõe sobre a Dirf

5 Rendimento pago N Variável 13 - Sim

6 Imposto retido N Variável 13 - Não

De acordo com a tabela de informações sobre a forma de 7 Forma de tributação N Fixo 2 Sim tributação constante na IN que dispõe sobre a Dirf

3.34 Registro de informações complementares para o comprovante de rendimento (identificador INF)

- Serão apresentados todos os CPF em ordem crescente;

- Deve haver um registro BPFDEC, BPFPROC e/ou BPFRRA correspondente na declaração;

- Deve ocorrer apenas um registro para cada beneficiário.

1 Identificador de registro C Fixo 3 INF Sim

2 CPF N Fixo 11 - Sim

Informações 3 C Variável 500 - Sim complementares

3.35 Registro identificador do término da declaração (identificador FIMDirf)

- Registro obrigatório no arquivo;

- Deve ser o último registro no arquivo;

- Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 7 FIMDirf Sim

