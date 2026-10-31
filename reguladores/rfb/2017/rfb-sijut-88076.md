---
titulo: "Ato Declaratório Executivo Cofis nº 72, de 16 de novembro de 2017"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "72"
data: "2017-11-16"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 22/11/2017, seção 1, página 46"
data_publicacao: "2017-11-22"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/88076/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/88076/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "88076"
sha256_texto: "4548f4d9af6e4235635f62b57e0389f15dda291ba843d8dba784a8ec9451ad3f"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Cofis nº 72, de 16 de novembro de 2017

Dispõe sobre o leiaute do Programa Gerador da Declaração do Imposto sobre a Renda Retido na Fonte (PGD Dirf 2018).

O COORDENADOR-GERAL DE FISCALIZAÇÃO, no uso das atribuições que lhe confere o inciso II do art. 334 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 430, de 9 de outubro de 2017, e tendo em vista o disposto na Instrução Normativa RFB nº 1757, de 10 de novembro de 2017, declara:

**Art. 1º** Fica aprovado o leiaute aplicável aos campos, registros e arquivos da Declaração do Imposto sobre a Renda Retido na Fonte (Dirf 2018), constante no anexo único a este Ato Declaratório.

**Art. 2º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

FLÁVIO VILELA CAMPOS

## ANEXO



## ANEXO

LEIAUTE DO ARQUIVO Declaração do Imposto sobre a Renda Retido na Fonte – Dirf

1. Regras gerais Estas regras devem ser respeitadas em todos os arquivos gerados, quando não excepcionadas por regra específica referente a um dado registro e explicitada em suas observações.

Nº Regra de preenchimento Descrição ALFANUMÉRICO (C): representados por “C” - todos os caracteres, excetuados o caractere “|” (pipe ou barra vertical). 1 Formato dos campos NUMÉRICO (N): representados por “N” – pode conter apenas os valores de zero a nove. 2 Campos numéricos (D) cujo conteúdo representa data Devem ser informados conforme o padrão ano, mês e dia (AAAAMMDD), excluindo-se quaisquer caracteres de separação (tais como “.”, “/”, “-”, etc.); Campos numéricos com número de inscrição ou Os campos numéricos com número de inscrição (CNPJ e CPF) ou códigos de receita deverão ser informados com todos os dígitos, inclusive os zeros à esquerda;

códigos de receita As máscaras (caracteres especiais de formatação, tais como “.”, “/”, “-”, etc.) não devem ser informadas. Devem ser informados com até 13 posições, representando 11 posições inteiras e 2 decimais; Os zeros não significativos não devem ser informados; 4 Campos numéricos referentes a valores Os caracteres ‘.’ (ponto) e ‘,’ (vírgula) não devem ser informados; Todos os valores monetários devem estar expressos em reais. Os campos com conteúdo alfanumérico nos quais se faz necessário registrar números ou códigos de identificação (Exemplo: Número de Identificação Fiscal– NIF) deverão seguir a regra de formação e tamanho definidos pelo respectivo órgão Campos alfanuméricos com números ou códigos de 5 regulador; identificação As máscaras (caracteres especiais de formatação, tais como “.”, “/”, “-”, etc.) não devem ser informadas.

Ao final de cada campo (inclusive o último de cada registro) deve ser inserido o caractere delimitador “|” (pipe ou barra vertical: caractere 124 da Tabela ASCII); O caractere delimitador “|” (barra vertical) não deve ser incluído como parte integrante do conteúdo de quaisquer campos numéricos, datas ou alfanuméricos; 6 Formação dos campos Na ausência de informação, o campo vazio (campo sem conteúdo, nulo e com valor zero) deverá ser iniciado com o caractere “|” (barra vertical) e imediatamente encerrado com o mesmo caractere “|” (barra vertical) delimitador de campo.

7 Formação dos registros Cada registro deve necessariamente ocupar apenas uma linha no arquivo. Preenchimento fixo: o campo deve ser preenchido com o tamanho exato. 8 Preenchimento dos campos Preenchimento variável: o campo pode ter variação de tamanho de preenchimento. Deve ser informado com até 4 posições, representando 3 posições inteiras e 1 decimal; 9 Campo numérico referente a quantidade de meses Os zeros não significativos não devem ser informados; Os caracteres ‘.’ (ponto) e ‘,’ (vírgula) não devem ser informados.

2. Estrutura de arquivo 2.1 Estrutura completa de uma declaração de Pessoa Física

Dirf – Declaração do imposto sobre a renda retido na fonte RESPO – Responsável pelo preenchimento DECPF – Declarante pessoa física IDREC – Identificação do código de receita BPFDEC – Beneficiário pessoa física do declarante RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTDP – Rendimentos Tributáveis – Dedução – Dependentes RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte CJAC – Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA – Compensação de Imposto por Decisão Judicial – Anos Anteriores ESRT – Tributação com Exigibilidade Suspensa – Rendimento Tributável ESPO – Tributação com Exigibilidade Suspensa – Dedução – Previdência Oficial ESDP – Tributação com Exigibilidade Suspensa – Dedução – Dependentes ESIR – Tributação com Exigibilidade Suspensa – Imposto sobre a Renda na Fonte ESDJ – Tributação com Exigibilidade Suspensa – Depósito Judicial INFPC – Informações de Previdência Complementar RTPP – Rendimentos Tributáveis – Dedução – Previdência Privada RTFA – Rendimentos Tributáveis – Dedução – FAPI ESPP – Tributação com Exigibilidade Suspensa – Dedução – Previdência Privada ESFA – Tributação com Exigibilidade Suspensa – Dedução – FAPI INFPA – Informações do beneficiário da pensão alimentícia RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia ESPA – Tributação com Exigibilidade Suspensa – Dedução – Pensão Alimentícia RIDAC – Rendimentos Isentos – Diária e Ajuda de Custo RIIRP – Rendimentos Isentos – Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV RIAP – Rendimentos Isentos – Abono Pecuniário RIP65 – Rendimentos Isentos – Parcela Isenta de Aposentadoria para Maiores de 65 anos RIO – Rendimentos Isentos Anuais – Outros BPJDEC – Beneficiário pessoa jurídica do declarante RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte RRA – Rendimentos recebidos acumuladamente IDREC – Identificação do código de receita BPFRRA – Beneficiário pessoa física do rendimento recebido acumuladamente

RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte DAJUD – Despesa com ação judicial QTMESES – Quantidade de meses INFPA – Informações do beneficiário da pensão alimentícia RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia SCP – Informações da sociedade em conta de participação BPFSCP – Beneficiário pessoa física da sociedade em conta de participação RISCP – Lucros e dividendos pagos ao sócio da sociedade em conta de participação BPJSCP – Beneficiário pessoa jurídica da sociedade em conta de participação RISCP – Lucros e dividendos pagos ao sócio da sociedade em conta de participação PSE – Plano privado de assistência à saúde – coletivo empresarial OPSE – Operadora de plano privado de assistência à saúde – coletivo empresarial TPSE – Titular de plano privado de assistência à saúde – coletivo empresarial RTPSE – Reembolso do titular do plano de assistência à saúde – coletivo empresarial DTPSE – Dependente do titular de plano privado de assistência à saúde – coletivo empresarial RDTPSE – Reembolso do dependente do titular do plano de assistência à saúde – coletivo empresarial RPDE – Rendimentos pagos a residentes ou domiciliados no exterior BRPDE – Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE – Valores de rendimentos pagos a residentes ou domiciliados no exterior INF – Informações complementares para o comprovante de rendimentos FIMDirf – Término da declaração

2.2 Estrutura completa de uma declaração de Pessoa Jurídica

Dirf – Declaração do imposto sobre a renda retido na fonte RESPO – Responsável pelo preenchimento DECPJ – Declarante pessoa jurídica IDREC – Identificação do código de receita BPFDEC – Beneficiário pessoa física do declarante RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTDP – Rendimentos Tributáveis – Dedução – Dependentes RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte CJAC – Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA – Compensação de Imposto por Decisão Judicial – Anos Anteriores ESRT – Tributação com Exigibilidade Suspensa – Rendimento Tributável ESPO – Tributação com Exigibilidade Suspensa – Dedução – Previdência Oficial ESDP – Tributação com Exigibilidade Suspensa – Dedução – Dependentes ESIR – Tributação com Exigibilidade Suspensa – Imposto sobre a Renda na Fonte ESDJ – Tributação com Exigibilidade Suspensa – Depósito Judicial INFPC – Informações de Previdência Complementar RTPP – Rendimentos Tributáveis – Dedução – Previdência Privada RTFA – Rendimentos Tributáveis – Dedução – FAPI RTSP – Rendimentos Tributáveis – Dedução – Fundo de Previdência do Servidor Público RTEP – Rendimentos Tributáveis – Dedução – Contribuição do ente público patrocinador ESPP – Tributação com Exigibilidade Suspensa – Dedução – Previdência Privada ESFA – Tributação com Exigibilidade Suspensa – Dedução – FAPI ESSP – Tributação com Exigibilidade Suspensa – Dedução – Fundo de Previdência do Servidor Público ESEP – Tributação com Exigibilidade Suspensa – Dedução – Contribuição do ente público patrocinador INFPA – Informações do beneficiário da pensão alimentícia RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia ESPA – Tributação com Exigibilidade Suspensa – Dedução – Pensão Alimentícia RIDAC – Rendimentos Isentos – Diária e Ajuda de Custo RIIRP – Rendimentos Isentos – Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV RIAP – Rendimentos Isentos – Abono Pecuniário RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave RIP65 – Rendimentos Isentos – Parcela Isenta de Aposentadoria para Maiores de 65 anos RIBMR – Rendimentos Isentos – Bolsa de Estudo Recebida por Médico-residente RICAP – Rendimentos Isentos – Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIL96 – Rendimentos Isentos Anuais – Lucros e dividendos pagos a partir de 1996 RIPTS – Rendimentos Isentos Anuais – Valores pagos a titular ou sócio ou empresa de pequeno porte, exceto pró-labore e aluguéis RIO – Rendimentos Isentos Anuais – Outros BPJDEC – Beneficiário pessoa jurídica do declarante RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte VPEIM – Valores pagos às entidades imunes ou isentas – IN RFB 1.234/2012 RIMUM – Rendimentos Imunes – art. 4º, inciso III RISEN – Rendimentos Isentos – art. 4º, inciso IV FCI – Fundo ou clube de investimento IDREC – Identificação do código de receita BPFFCI – Beneficiário pessoa física do fundo ou clube de investimento RTRT – Rendimentos Tributáveis – Rendimento Tributável

RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte CJAC – Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA – Compensação de Imposto por Decisão Judicial – Anos Anteriores ESRT – Tributação com Exigibilidade Suspensa – Rendimento Tributável ESIR – Tributação com Exigibilidade Suspensa – Imposto sobre a Renda na Fonte ESDJ – Tributação com Exigibilidade Suspensa – Depósito Judicial RIP65 – Rendimentos Isentos – Parcela Isenta de Aposentadoria para Maiores de 65 anos RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave RICAP – Rendimentos Isentos – Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIO – Rendimentos Isentos Anuais – Outros BPJFCI – Beneficiário pessoa jurídica do fundo ou clube de investimento RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte PROC – Processo da justiça do trabalho/federal/estadual/Distrito Federal IDREC – Identificação do código de receita BPFPROC – Beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTDP – Rendimentos Tributáveis – Dedução – Dependentes RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte CJAC – Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA – Compensação de Imposto por Decisão Judicial – Anos Anteriores ESRT – Tributação com Exigibilidade Suspensa – Rendimento Tributável ESPO – Tributação com Exigibilidade Suspensa – Dedução – Previdência Oficial ESDP – Tributação com Exigibilidade Suspensa – Dedução – Dependentes ESIR – Tributação com Exigibilidade Suspensa – Imposto sobre a Renda na Fonte ESDJ – Tributação com Exigibilidade Suspensa – Depósito Judicial RTPP – Rendimentos Tributáveis – Dedução – Previdência Privada RTFA – Rendimentos Tributáveis – Dedução – FAPI RTSP – Rendimentos Tributáveis – Dedução – Fundo de Previdência do Servidor Público ESPP – Tributação com Exigibilidade Suspensa – Dedução – Previdência Privada ESFA – Tributação com Exigibilidade Suspensa – Dedução – FAPI ESSP – Tributação com Exigibilidade Suspensa – Dedução – Fundo de Previdência do Servidor Público RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia ESPA – Tributação com Exigibilidade Suspensa – Dedução – Pensão Alimentícia RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave RIRSR –Rendimentos pagos sem retenção do IR na fonte – Lei nº 10.833/2003 BPJPROC – Beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte RIRSR – Rendimentos pagos sem retenção do IR na fonte – Lei nº 10.833/2003 RRA – Rendimentos recebidos acumuladamente IDREC – Identificação do código de receita BPFRRA – Beneficiário pessoa física do rendimento recebido acumuladamente RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave RIP65 – Rendimentos Isentos – Parcela Isenta de Aposentadoria para Maiores de 65 anos DAJUD – Despesa com ação judicial QTMESES – Quantidade de meses RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia SCP – Informações da sociedade em conta de participação BPFSCP – Beneficiário pessoa física da sociedade em conta de participação RISCP – Lucros e dividendos pagos ao sócio da sociedade em conta de participação BPJSCP – Beneficiário pessoa jurídica da sociedade em conta de participação RISCP – Lucros e dividendos pagos ao sócio da sociedade em conta de participação PSE – Plano privado de assistência à saúde – coletivo empresarial OPSE – Operadora de plano privado de assistência à saúde – coletivo empresarial TPSE – Titular de plano privado de assistência à saúde – coletivo empresarial RTPSE – Reembolso do titular do plano de assistência à saúde – coletivo empresarial DTPSE – Dependente do titular de plano privado de assistência à saúde – coletivo empresarial RDTPSE – Reembolso do dependente do titular do plano de assistência à saúde – coletivo empresarial RPDE – Rendimentos pagos a residentes ou domiciliados no exterior BRPDE – Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE – Valores de rendimentos pagos a residentes ou domiciliados no exterior INF – Informações complementares para o comprovante de rendimentos FIMDirf – Término da declaração

3. Leiaute do arquivo 3.1 Registro de identificação da declaração (identificador Dirf)

- Registro obrigatório no arquivo;

- Deve ser o primeiro registro no arquivo; - Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 4 Dirf Sim 2 Ano referência N Fixo 4 2018 Sim 3 Ano-calendário N Fixo 4 2018 ou 2017 Sim S – Retificadora 4 Indicador de retificadora C Fixo 1 Sim N – Original 5 Número do recibo N Fixo 12 - Não 6 Identificador de estrutura do leiaute C Fixo 7 Q84FV63 Sim

5 Número do recibo O preenchimento será obrigatório se o campo de ordem 4 igual a “S” e declaração transmitida sem o uso de certificação digital.

3.2 Registro do Responsável pelo preenchimento da declaração (identificador RESPO)

- Registro obrigatório no arquivo; - Deve ser o segundo registro no arquivo; - Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 5 RESPO Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 DDD N Fixo 2 - Sim 5 Telefone N Variável 9 - Sim 6 Ramal N Variável 6 - Não 7 Fax N Variável 9 - Não 8 Correio eletrônico C Variável 50 - Não

4 DDD O primeiro algarismo deve ser diferente de zero. 5 Telefone Deve ser preenchido com oito ou nove algarismos. 7 Fax Deve ser preenchido com oito ou nove algarismos.

3.3 Registro de identificação do declarante pessoa física (identificador DECPF)

- Registro obrigatório no arquivo para declarante pessoa física; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPJ.

1 Identificador de registro C Fixo 5 DECPF Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim

S – Pagou rendimentos a residentes ou domiciliados no exterior. Indicador de declarante de rendimentos pagos a residentes ou domiciliados no 4 C Fixo 1 Sim exterior N – Não pagou rendimentos a residentes ou domiciliados no exterior.

S – Titular de serviços notariais e de registros. 5 Indicador de Titular de Serviços Notariais e de Registros C Fixo 1 Sim N – Não é titular de serviços notariais e de registros. S – Existe pagamento de valor pelo titular/dependente do plano de saúde. 6 Indicador de plano privado de assistência à saúde – coletivo empresarial C Fixo 1 Sim N – Não existe pagamento de valor pelo titular/dependente do plano de saúde. Indicador de sócio ostensivo responsável por sociedade em conta de participação – S – Sócio ostensivo 7 C Fixo 1 Sim SCP N – Não é sócio ostensivo

S – Encerramento de espólio/saída definitiva do país. 8 Indicador de situação especial da declaração C Fixo 1 Sim N – Não é encerramento de espólio/saída definitiva do país 9 Data do Evento D Fixo 8 - Não 1 – Encerramento de espólio. 10 Tipo de Evento N Fixo 1 Não 2 – Saída definitiva do Brasil.

9 Data do Evento O preenchimento será obrigatório se o campo de ordem 8 igual a “S”. 10 Tipo de Evento O preenchimento será obrigatório se o campo de ordem 8 igual a “S”.

3.4 Registro de identificação do declarante pessoa jurídica (identificador DECPJ)

- Registro obrigatório no arquivo para declarante pessoa jurídica; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPF.

1 Identificador de registro C Fixo 5 DECPJ Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

0 – Pessoa jurídica de direito privado. 1 – Órgãos, autarquias e fundações da administração pública federal.

2 – Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal. 4 Natureza do declarante N Fixo 1 Sim 3 – Empresa pública ou sociedade de economia mista federal.

4 – Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal.

8 – Entidade com alteração de natureza jurídica (uso restrito). 5 CPF responsável perante o CNPJ N Fixo 11 - Sim Indicador de sócio ostensivo responsável por sociedade em conta de participação – S – Sócio ostensivo. 6 C Fixo 1 Sim SCP N – Não é sócio ostensivo. S – Depositário de crédito decorrente de decisão judicial. 7 Indicador de declarante depositário de crédito decorrente de decisão judicial C Fixo 1 Sim N – Não é depositário de crédito decorrente de decisão judicial. S – Instituição administradora ou intermediadora de fundo ou clube de investimento. Indicador de declarante de instituição administradora ou intermediadora de fundo ou 8 C Fixo 1 Sim clube de investimento N – Não é instituição administradora ou intermediadora de fundo ou clube de investimento.

S – Pagou rendimentos a residentes ou domiciliados no exterior. 9 Indicador de declarante de rendimentos pagos a residentes ou domiciliados no exterior C Fixo 1 Sim N – Não pagou rendimentos a residentes ou domiciliados no exterior.

S – Existe pagamento de valor pelo titular/dependente do plano de saúde. 10 Indicador de plano privado de assistência à saúde – coletivo empresarial C Fixo 1 Sim N – Não existe pagamento de valor pelo titular/dependente do plano de saúde. Indicador de pagamentos relacionados aos Jogos Olímpicos de 2016 e aos Jogos S – Existe pagamento relacionado às Olimpíadas. 11 C Fixo 1 Sim Paraolímpicos de 2016 N – Não existe pagamento relacionado às Olimpíadas. Indicador de entidade em que a União detém maioria do capital social sujeito a voto, S – Existe pagamento de valores a entidades imunes/isentas. 12 recebe recursos do Tesouro Nacional e está obrigada a registrar a execução C Fixo 1 Sim N – Não existe pagamento de valores a entidades imunes/isentas. orçamentária no Siafi (IN 1.234/2012, art. 4º, incisos III e IV) S – Declaração de situação especial. 13 Indicador de situação especial da declaração C Fixo 1 Sim N – Não é declaração de situação especial. 14 Data do evento D Fixo 8 - Não

Relativamente à natureza do declarante 8 – Entidade com alteração de natureza jurídica (uso restrito), esclarecemos: 1. Para declarante que alterou sua natureza jurídica em relação ao ano-calendário e que implique em mudança da natureza do declarante na ficha Informações da Dirf; 4 Natureza do declarante 2. Para declarante que mudou sua natureza jurídica de órgão público para privado, ou vice-versa. Aplica-se ainda para mudanças entre as esferas governamentais da federação. Por exemplo: órgão público ou pessoa jurídica de direito privado estadual ou municipal que passou a ser federal, ou vice-versa; 3. A declaração deverá ser entregue na RFB.

Indicador de entidade em que a União detém maioria do capital social sujeito a voto, recebe recursos do 12 Indicador com a opção “Sim” permitido somente se campo de ordem 4 – Natureza do declarante, igual a “0”, “1”, “3” ou “8” Tesouro Nacional e está obrigada a registrar a execução orçamentária no Siafi (IN 1.234/2012, art. 4º, incisos III e IV)

14 Data do evento O preenchimento será obrigatório se o campo de ordem 13igual a “S”.

3.5 Registro de identificação do código de receita (identificador IDREC)

- Deve ser apresentado com os códigos de receita em ordem crescente; - Deve estar associado aos registros do tipo DECPF, DECPJ, FCI, PROC ou RRA.

1 Identificador de registro C Fixo 5 IDREC Sim De acordo com a tabela de códigos de receitas constante na IN que dispõe 2 Código de receita N Fixo 4 Sim sobre a Dirf.

3.6 Registro de beneficiário pessoa física do declarante (identificador BPFDEC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFDEC Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Data atribuída pelo laudo da moléstia grave D Fixo 8 - Não S – Existem informações detalhadas do alimentando. Sim 5 Indicador de identificação do alimentando C Fixo 1 N – Não existem informações detalhadas do alimentando. Sim S – Existem informações detalhadas da previdência complementar. 6 Indicador de identificação da previdência complementar C Fixo 1 N – Não existem informações detalhadas da previdência complementar.

Se campo igual a “S” –deverá constar o registro INFPA seguido do registro de valor (RTPA e/ou ESPA) para cada alimentando. 5 Indicador de identificação do alimentando Se campo igual a “N” –não apresentar o registro INFPA; deverão constar os registros de valores (RTPA e/ou ESPA) com o valor total de pensão alimentícia pago a todos os alimentandos do beneficiário. – As informações detalhadas a que se refere o campo são: CPF, data de nascimento, nome e relação de dependência do alimentando (registro INFPA).

Se campo igual a “S” –deverá constar o registro INFPC seguido do registro de valor (RTPP, RTFA, RTSP e/ou ESPP, ESFA, ESSP) para cada entidade de previdência complementar do beneficiário.

6 Indicador de identificação da previdência complementar Se campo igual a “N” –não apresentar o registro INFPC; deverão constar apenas os registros de valores mensais (RTPP, RTFA, RTSP e/ou ESPP, ESFA, ESSP) com o total dos valores de previdência complementar pagos pelo beneficiário. – As informações detalhadas a que se refere o campo são: CNPJ e Nome empresarial da entidade de previdência complementar (registro INFPC).

3.7 Registro de beneficiário pessoa jurídica do declarante (identificador BPJDEC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPJDEC Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.8 Registro de valores pagos às entidades imunes e isentas (identificador VPEIM)

- Serão apresentados todos os CNPJ em ordem crescente; - Registro permitido somente para declarante pessoa jurídica; e se campo 12 do registro DECPJ igual a “S”;

1 Identificador de registro C Fixo 5 VPEIM Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.9 Registro de identificação do fundo ou clube de investimento (identificador FCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Deve estar associado ao registro do tipo DECPJ.

1 Identificador de registro C Fixo 3 FCI Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.10 Registro do beneficiário pessoa física do fundo ou clube de investimento (identificador BPFFCI)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFFCI Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Data atribuída pelo laudo da moléstia grave D Fixo 8 - Não

3.11 Registro do beneficiário pessoa jurídica do fundo ou clube de investimento (identificador BPJFCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPJFCI Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.12 Registro de processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador PROC)

- Deve estar classificado em ordem crescente por: - Tipo de justiça; - Número do processo; - Deve estar associado ao registro do tipo DECPJ.

1 Identificador de registro C Fixo 4 PROC Sim 2 Indicador de Justiça N Fixo 1 1 – Justiça federal Sim

2 – Justiça do trabalho 3 – Justiça estadual/Distrito Federal 3 Número do processo C Variável 20 - Sim 1 – Pessoa física 4 Indicador de tipo de advogado/escritório de advocacia N Fixo 1 Não 2 – Pessoa jurídica CPF com 11 dígitos 5 CPF do advogado/ CNPJ do escritório de advocacia N Variável 14 Não CNPJ com 14 dígitos Nome da pessoa física até 60 posições. 6 Nome do advogado/ Nome empresarial do escritório de advocacia C Variável 150 Não Nome empresarial da pessoa jurídica até 150 posições. 7 Valor pago para o advogado N Variável 13 Valor pago para o advogado Não

3.13 Registro de beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPFPROC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 7 BPFPROC Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Data atribuída pelo laudo da moléstia grave D Fixo 8 - Não

3.14 Registro de beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPJPROC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 7 BPJPROC Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.15 Registro de rendimentos recebidos acumuladamente (identificador RRA)

- Deve estar classificado em ordem crescente por: - Indicador de rendimento recebido acumuladamente; - Número do processo.

1 Identificador de registro C Fixo 3 RRA Sim 1 – Pago pelo declarante 2 Identificador de rendimento recebido acumuladamente N Fixo 1 Sim 2 – Pago pela justiça 3 Número do processo/requerimento C Variável 20 - Não 1 – Pessoa física 4 Indicador de tipo de advogado/escritório de advocacia N Fixo 1 Não 2 – Pessoa jurídica CPF com 11 dígitos 5 CPF do advogado/CNPJ do escritório de advocacia N Variável 14 Não CNPJ com 14 dígitos Nome da pessoa física com até 60 posições. 6 Nome do advogado/Nome empresarial do escritório de advocacia C Variável 150 Não Nome empresarial da pessoa jurídica com até 150 posições. 7 Valor pago para o advogado N Variável 13 Valor pago para o advogado Não

3 Número do processo/requerimento O preenchimento será obrigatório se o campo de ordem 2 igual a 2.

3.16 Registro de beneficiário pessoa física dos rendimentos recebidos acumuladamente (identificador BPFRRA)

- Deve estar classificado em ordem crescente por: - CPF; - Natureza do RRA; - Deve estar associado ao registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFRRA Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Natureza do RRA C Variável 50 - Não 5 Data atribuída pelo laudo da moléstia grave D Fixo 8 - Não S – Existem informações detalhadas do alimentando. 6 Indicador de identificação do alimentando C Fixo 1 Sim N – Não existem informações detalhadas do alimentando.

1. O campo só poderá ser igual a “S” se o campo 2 do registro RRA igual a “1” (Pago pelo declarante); 2. Se campo igual a “S” –deverá constar o registro INFPA e RTPA para cada alimentando; 6 Indicador de identificação do alimentando 3. Se campo igual a “N” –não apresentar o registro INFPA; deverá constar o registro RTPA com o valor de pensão alimentícia pago a todos os alimentandos do beneficiário; 4. As informações detalhadas a que se refere o campo são: CPF, Data de nascimento e Nome do alimentando (registro INFPA).

3.17 Registro de identificação de Previdência Complementar (identificador INFPC)

- Registro permitido somente se campo 6 do registro BPFDEC (Indicador de identificação da previdência complementar) igual a “S”; - Serão apresentados todos os CNPJ em ordem crescente; - Deve estar associado ao registro do tipo BPFDEC; - Deve constar um registro INFPC para cada CNPJ de entidade de previdência complementar.

1 Identificador de registro C Fixo 5 INFPC Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.18 Registro de informações do beneficiário da pensão alimentícia (identificador INFPA)

- Registro permitido somente se Indicador de identificação do alimentando igual a “S” (BPFDEC, campo 5; e BPFRRA, campo 6); - Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo BPFDEC, BPFRRA.

1 Identificador de registro C Fixo 5 INFPA Sim 2 CPF do alimentando N Fixo 11 - Não 3 Data de nascimento D Fixo 8 - Não 4 Nome C Variável 60 - Sim 03 – Cônjuge/ Companheiro(a) 04 – Filho (a) 5 Relação de dependência N Fixo 2 06 – Enteado (a) Não 08 – Pai/Mãe 10 – Agregado/ Outros

2 CPF do alimentando Preenchimento obrigatório para maiores de 18anos completos até 31 de dezembro do ano-calendário da declaração. 3 Data de nascimento Preenchimento obrigatório para menores de 18anos completos até 31 de dezembro do ano-calendário da declaração, que não tenham informado o CPF. - Regra de validação O registro INFPA associado ao BPFRRA será permitido somente quando o Identificador de rendimento recebido acumuladamente igual a “1 – Pago pelo declarante” (campo 2 do registro RRA).

3.19 Registro de valores mensais (identificadores RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTIRF, CJAA, CJAC, ESRT, ESPO, ESPP, ESFA, ESSP, ESEP, ESDP, ESPA, ESIR, ESDJ, RIP65, RIDAC, RIIRP, RIAP, RIMOG, RIVC, RIBMR, RICAP, RISCP, RIMUN, RISEN e DAJUD)

- Deve ocorrer apenas se houver pelo menos um dos valores referente aos meses ou 13º salário; - Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC, BPJDEC, BPFFCI, BPJFCI, BPFPROC, BPJPROC, BPFRRA, BPFSCP, BPJSCP, INFPC, INFPA.

RTRT RTPO RTPP RTFA RTSP RTEP RTDP RTPA RTIRF CJAC CJAA ESRT ESPO ESPP ESFA ESSP 1 Identificador de registro C Variável 5 ESEP Sim ESDP ESPA ESIR ESDJ RIP65 RIDAC RIIRP RIAP RIMOG RIVC RIBMR RICAP RISCP RIMUN RISEN DAJUD 2 Janeiro N Variável 13 - Não 3 Fevereiro N Variável 13 - Não 4 Março N Variável 13 - Não 5 Abril N Variável 13 - Não 6 Maio N Variável 13 - Não 7 Junho N Variável 13 - Não 8 Julho N Variável 13 - Não 9 Agosto N Variável 13 - Não 10 Setembro N Variável 13 - Não 11 Outubro N Variável 13 - Não 12 Novembro N Variável 13 - Não 13 Dezembro N Variável 13 - Não 14 Décimo Terceiro N Variável 13 - Não

3.20 Registro de valores anuais isentos (identificadores RIL96, RIPTS e RIRSR)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC(RIL96 e RIPTS) ou BPFPROC(RIRSR).

RIL96 1 Identificador de registro C Fixo 5 RIPTS Sim RIRSR 2 Valor pago no ano N Variável 13 - Sim

3.21 Registro de valores anuais de rendimentos isentos – outros (identificador RIO)

- Ocorrerá apenas um registro para cada beneficiário; - Deve estar associado ao registro do tipo BPFDEC ou BPFFCI.

1 Identificador de registro C Fixo 3 RIO Sim 2 Valor pago no ano N Variável 13 - Sim 3 Descrição dos rendimentos isentos – outros C Variável 60 - Sim

3.22 Registro de quantidade de meses (identificador QTMESES)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado ao registro do tipo BPFRRA.

1 Identificador de registro C Fixo 7 QTMESES Sim 2 Quantidade meses – janeiro N Variável 4 - Não 3 Quantidade meses – fevereiro N Variável 4 - Não 4 Quantidade meses – março N Variável 4 - Não 5 Quantidade meses – abril N Variável 4 - Não 6 Quantidade meses – maio N Variável 4 - Não 7 Quantidade meses – junho N Variável 4 - Não 8 Quantidade meses – julho N Variável 4 - Não 9 Quantidade meses – agosto N Variável 4 - Não 10 Quantidade meses – setembro N Variável 4 - Não 11 Quantidade meses – outubro N Variável 4 - Não 12 Quantidade meses – novembro N Variável 4 - Não 13 Quantidade meses – dezembro N Variável 4 - Não

3.23 Registro de informações da Sociedade em Conta de Participação (identificador SCP)

- Serão apresentados em ordem crescente de CNPJ. - Deve constar um registro para cada CNPJ de Sociedade em conta de participação

1 Identificador de registro C Fixo 3 SCP Sim 2 CNPJ da Sociedade em Conta de Participação N Fixo 14 - Sim 3 Nome empresarial da Sociedade em Conta de Participação C Variável 150 - Sim

3.24 Registro de beneficiário pessoa física da sociedade em conta de participação (identificador BPFSCP)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJSCP, caso exista o registro; - Deve estar associado a um registro do tipo SCP.

1 Identificador de registro C Fixo 6 BPFSCP Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Percentual de participação na SCP C Variável 4 - Não

3.25 Registro de beneficiário pessoa jurídica da sociedade em conta de participação (identificador BPJSCP)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFSCP, caso exista o registro; - Deve estar associado a um registro do tipo SCP.

1 Identificador de registro C Fixo 6 BPJSCP Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 4 Percentual de participação na SCP C Variável 4 - Não

3.26 Registro de pagamentos a plano privado de assistência à saúde – coletivo empresarial (identificador PSE)

- Ocorre somente uma vez no arquivo, caso exista informação de valores pagos pelo titular/dependente do plano de assistência à saúde.

1 Identificador de registro C Fixo 3 PSE Sim

3.27 Registro de operadora do plano privado de assistência à saúde – coletivo empresarial (identificador OPSE)

- Ocorre caso exista o registro PSE; - Serão apresentados todos os CNPJ em ordem crescente.

1 Identificador de registro C Fixo 4 OPSE Sim 2 CNPJ da operadora de plano privado de assistência à saúde – coletivo empresarial N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 4 Registro ANS N Fixo 6 - Sim

3.28 Registro de titular do plano privado de assistência à saúde – coletivo empresarial (identificador TPSE)

- Serão apresentados todos os CPF em ordem crescente. - Deve estar associado ao registro do tipo OPSE.

1 Identificador de registro C Fixo 4 TPSE Sim 2 CPF do titular N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Valor pago no ano N Variável 13 - Sim

4 Valor pago no ano Preenchimento obrigatório se o titular não possuir dependente cadastrado e nem reembolso informado.

3.29 Registro de informação de reembolso do titular do plano de saúde – coletivo empresarial (identificador RTPSE)

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo TPSE; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos-calendário anteriores.

Ordem Campo Formato Preenchimento Tamanho Valores Válidos Obrigatório 1 Identificador de registro C Fixo 5 RTPSE Sim CPF/CNPJ do prestador de serviço CPF com 11 dígitos; 2 N Variável 14 Sim CNPJ com 14 dígitos. Nome/Nome empresarial do prestador de serviço Nome da pessoa física até 60 posições. 3 C Variável 150 Sim Nome empresarial da pessoa jurídica até 150 posições. 4 Valor do reembolso do ano-calendário N Variável 9 - Não 5 Valor do reembolso de anos anteriores N Variável 9 - Não

4 Valor do reembolso do ano-calendário Valores reembolsados no ano-calendário, referentes a pagamentos de serviços prestados no ano-calendário. 5 Valor do reembolso de anos anteriores Valores reembolsados no ano-calendário referentes a pagamentos de serviços prestados em anos anteriores.

3.30 Registro de dependente do plano privado de assistência à saúde – coletivo empresarial (identificador DTPSE)

- Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo TPSE.

1 Identificador de registro C Fixo 5 DTPSE Sim 2 CPF do dependente N Fixo 11 - Não 3 Data de nascimento D Fixo 8 - Não 4 Nome C Variável 60 - Sim 03 – Cônjuge/ Companheiro(a) 04 – Filho(a) 06 – Enteado(a) 5 Relação de dependência N Fixo 2 08 – Pai/Mãe Não 10 – Agregado/ Outros

6 Valor pago no ano N Variável 13 - Sim

2 CPF do dependente Preenchimento obrigatório para maiores de 18anos completos até 31 de dezembro do ano-calendário da declaração. 3 Data de nascimento Preenchimento obrigatório para menores de 18anos completos até 31 de dezembro do ano-calendário da declaração, que não tenham informado o CPF. 6 Valor pago no ano Preenchimento obrigatório se o dependente não possuir reembolso informado.

3.31 – Registro de informação de reembolso do dependente (identificador RDTPSE):

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo DTPSE; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos-calendário anteriores. Ordem Campo Formato Preenchimento Tamanho Valores Válidos Obrigatório 1 Identificador de registro C Fixo 6 RDTPSE Sim CPF com 11 dígitos; 2 CPF/CNPJ do prestador de serviço N Variável 14 Sim CNPJ com 14 dígitos. Nome da pessoa física até 60 posições; 3 Nome/Nome Empresarial do prestador de serviço C Variável 150 Sim Nome empresarial da pessoa jurídica até 150 posições. 4 Valor do reembolso do ano-calendário N Variável 9 - Não 5 Valor do reembolso de anos anteriores N Variável 9 - Não

4 Valor do reembolso do ano-calendário Valores reembolsados no ano-calendário, referentes a pagamentos de serviços prestados no ano-calendário. 5 Valor do reembolso de anos anteriores Valores reembolsados no ano-calendário referentes a pagamentos de serviços prestados em anos anteriores.

3.32 Registro de rendimentos pagos a residentes ou domiciliados no exterior (identificador RPDE)

- Ocorre somente uma vez no arquivo, caso exista informação de rendimentos pagos a residentes ou domiciliados no exterior

1 Identificador de registro C Fixo 4 RPDE Sim

3.33 Registro de beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior (identificador BRPDE)

- Deve estar classificado em ordem crescente por: - Beneficiário; - Código de país; - Número de identificação fiscal – NIF; - Deve estar associado ao registro do tipo RPDE.

1 Identificador de registro C Fixo 5 BRPDE Sim 1 – Pessoa física 2 Beneficiário N Fixo 1 Sim 2 – Pessoa jurídica De acordo com a tabela de código dos países constante na 3 Código de país N Variável 3 Sim IN que dispõe sobre a Dirf 4 Número de identificação fiscal – NIF C Variável 30 - Não

S – Dispensado do Número de identificação fiscal – NIF 5 Indicador de beneficiário dispensado do Número de Identificação Fiscal – NIF C Fixo 1 Sim N – Não é dispensado do Número de identificação fiscal – NIF

S – Dispensado do Número de identificação fiscal – NIF 6 Indicador de que o país não exige Número de Identificação Fiscal – NIF C Fixo 1 Sim N – Não é dispensado do Número de identificação fiscal – NIF

CPF com 11 dígitos. 7 CPF/CNPJ N Variável 14 Não CNPJ com 14 dígitos. 8 Nome/Nome empresarial C Variável 150 - Sim

De acordo com a tabela de informações sobre os beneficiários dos 9 Relação fonte pagadora pessoa jurídica e beneficiário pessoa jurídica N Fixo 3 Não rendimentos constante na IN que dispõe sobre a Dirf

10 Logradouro C Variável 60 - Não 11 Número C Variável 6 - Não 12 Complemento C Variável 25 - Não 13 Bairro/Distrito C Variável 20 - Não 14 Código postal N Variável 10 - Não 15 Cidade C Variável 40 - Não 16 Estado/Província C Variável 40 - Não 17 Telefone N Variável 15 - Não

9 Relação fonte pagadora pessoa jurídica e beneficiário pessoa jurídica Preenchimento obrigatório se campo de ordem 2 (Beneficiário) igual a 2.

3.34 Registro de valores de rendimentos pagos a residentes ou domiciliados no exterior (identificador VRPDE)

- Deve estar classificado em ordem crescente por: - Data do pagamento; - Código de receita; - Deve estar associado ao registro do tipo BRPDE.

1 Identificador de registro C Fixo 5 VRPDE Sim 2 Data do pagamento D Fixo 8 - Sim 3 Código de receita N Fixo 4 - Sim De acordo com a tabela de informações sobre os rendimentos 4 Tipo de rendimento N Fixo 3 Sim constante na IN que dispõe sobre a Dirf 5 Rendimento pago N Variável 13 - Sim 6 Imposto retido N Variável 13 - Não De acordo com a tabela de informações sobre a forma de tributação 7 Forma de tributação N Fixo 2 Sim constante na IN que dispõe sobre a Dirf

3.35 Registro de informações complementares para o comprovante de rendimento (identificador INF)

- Serão apresentados todos os CPF em ordem crescente; - Deve haver um registro BPFDEC, BPFPROC e/ou BPFRRA correspondente na declaração; - Deve ocorrer apenas um registro para cada beneficiário.

1 Identificador de registro C Fixo 3 INF Sim 2 CPF N Fixo 11 - Sim 3 Informações complementares C Variável 500 - Sim

3.36 Registro identificador do término da declaração (identificador FIMDirf)

- Registro obrigatório no arquivo; - Deve ser o último registro no arquivo; - Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 7 FIMDirf Sim

