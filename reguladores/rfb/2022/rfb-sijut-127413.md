---
titulo: "Ato Declaratório Executivo Cofis nº 113, de 21 de novembro de 2022"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "113"
data: "2022-11-21"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 28/11/2022, seção 1, página 33"
data_publicacao: "2022-11-28"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/127413/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/127413/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "127413"
sha256_texto: "f7008bfbeb1bc7fce1f932999a3e5988c769bbed12749e7fec24ad889efafe3a"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Cofis nº 113, de 21 de novembro de 2022

Dispõe sobre o leiaute do Programa Gerador da Declaração do Imposto sobre a Renda Retido na Fonte (PGD Dirf 2023)

O COORDENADOR-GERAL DE FISCALIZAÇÃO, no uso das atribuições que lhe conferem os incisos I e II do art. 121 e inciso II do art. 358 do Regimento Interno da Secretaria Especial da Receita Federal do Brasil, aprovado pela Portaria ME nº 284, de 27 de julho de 2020, e tendo em vista o disposto na Instrução Normativa RFB nº 1.990, de 18 de novembro de 2020, declara:

**Art.1º** Fica aprovado o leiaute aplicável aos campos, registros e arquivos da Declaração do Imposto sobre a Renda Retido na Fonte (Dirf 2023) para apresentação das informações relativas aos anos calendário de 2022, situação normal, e 2023, nos casos de situação especial.

**Art.2º** Para o preenchimento ou importação de dados pelo PGD Dirf 2023 deverá ser observado o leiaute do arquivo constante do Anexo Único deste Ato Declaratório.

**Art.3º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

PAULO EDUARDO NUNES VERÇOSA

Anexo Único

Anexo Único

ANEXO ÚNICO LEIAUTE DO ARQUIVO Declaração do Imposto sobre a Renda Retido na Fonte – Dirf

1. Regras gerais: Esta seção apresenta as regras que devem ser respeitadas em todos os arquivos gerados, quando não excepcionadas por regra específica referente a um dado registro e explicitada em suas observações.

Nº Regra de preenchimento Descrição ALFANUMÉRICO (C): representados por “C” - todos os caracteres, excetuados o caractere “|” (pipe 1 Formato dos campos ou barra vertical). NUMÉRICO (N): representados por “N” – pode conter apenas os valores de zero a nove. Campos numéricos (D) cujo Devem ser informados conforme o padrão ano, mês e dia (AAAAMMDD), excluindo-se quaisquer

conteúdo representa data caracteres de separação (tais como “.”, “/”, “-”, etc.); Os campos numéricos com número de inscrição (CNPJ e CPF) ou códigos de receita deverão ser Campos numéricos com informados com todos os dígitos, inclusive os zeros à esquerda; 3 número de inscrição ou As máscaras (caracteres especiais de formatação, tais como “.”, “/”, “-”, etc.) não devem ser códigos de receita informadas. Devem ser informados com até 13 posições, representando 11 posições inteiras e 2 decimais; Campos numéricos referentes Os zeros não significativos não devem ser informados;

a valores Os caracteres “.” (ponto) e “,” (vírgula) não devem ser informados; Todos os valores monetários devem estar expressos em reais. Os campos com conteúdo alfanumérico nos quais se faz necessário registrar números ou códigos Campos alfanuméricos com de identificação (Exemplo: Número de Identificação Fiscal – N IF) deverão seguir a regra de 5 números ou códigos de formação e tamanho definidos pelo respectivo órgão regulador; identificação As máscaras (caracteres especiais de formatação, tais como “.”, “/”, “-”, etc.) não devem ser informadas. Ao final de cada campo (inclusive o último de cada registro) deve ser inserido o caractere 6 Formação dos campos delimitador “|” (pipe ou barra vertical: caractere 124 da Tabela ASCII); O caractere delimitador “|” (barra vertical) não deve ser incluído como parte integrante do conteúdo de quaisquer campos numéricos, datas ou alfanuméricos; Na ausência de informação, o campo vazio (campo sem conteúdo, nulo e com valor zero) deverá ser iniciado com o caractere “|” (barra vertical) e imediatamente encerrado com o mesmo caractere “|” (barra vertical) delimitador de campo. 7 Formação dos registros Cada registro deve necessariamente ocupar apenas uma linha no arquivo. Preenchimento fixo: o campo deve ser preenchido com o tamanho exato. 8 Preenchimento dos campos Preenchimento variável: o campo pode ter variação de tamanho de preenchimento. Deve ser informado com até 4 posições, representando 3 posições inteiras e 1 decimal; Campo numérico referente a 9 Os zeros não significativos não devem ser informados; quantidade de meses Os caracteres “.” (ponto) e “,” (vírgula) não devem ser informados.

2. Estrutura de arquivo 2.1 Estrutura completa de uma declaração de Pessoa Física

Dirf – Declaração do imposto sobre a renda retido na fonte RESPO – Responsável pelo preenchimento DECPF – Declarante pessoa física IDREC – Identificação do código de receita BPFDEC – Beneficiário pessoa física do declarante RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTDP – Rendimentos Tributáveis – Dedução – Dependentes RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte CJAC – Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA – Compensação de Imposto por Decisão Judicial – Anos Anteriores ESRT – Tributação com Exigibilidade Suspensa – Rendimento Tributável ESPO – Tributação com Exigibilidade Suspensa – Dedução – Previdência Oficial ESDP – Tributação com Exigibilidade Suspensa – Dedução – Dependentes ESIR – Tributação com Exigibilidade Suspensa – Imposto sobre a Renda na Fonte ESDJ – Tributação com Exigibilidade Suspensa – Depósito Judicial INFPC – Informações de Previdência Complementar RTPP – Rendimentos Tributáveis – Dedução – Previdência Privada RTFA – Rendimentos Tributáveis – Dedução – FAPI ESPP – Tributação com Exigibilidade Suspensa – Dedução – Previdência Privada ESFA – Tributação com Exigibilidade Suspensa – Dedução – FAPI INFPA – Informações do beneficiário da pensão alimentícia

RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia ESPA – Tributação com Exigibilidade Suspensa – Dedução – Pensão Alimentícia RIDAC – Rendimentos Isentos – Diária e Ajuda de Custo RIIRP – Rendimentos Isentos – Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV RIAP – Rendimentos Isentos – Abono Pecuniário RIP65 – Rendimentos Isentos – Parcela Isenta de Aposentadoria (65 anos ou mais) RIJMRE – Rendimentos Isentos Anuais – Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função RIO – Rendimentos Isentos Anuais – Outros BPJDEC – Beneficiário pessoa jurídica do declarante RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte RRA – Rendimentos recebidos acumuladamente IDREC – Identificação do código de receita BPFRRA – Beneficiário pessoa física do rendimento recebido acumuladamente RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte DAJUD – Despesa com ação judicial QTMESES – Quantidade de meses RIJMRE – Rendimentos Isentos Anuais – Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função INFPA – Informações do beneficiário da pensão alimentícia RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia SCP – Informações da sociedade em conta de participação BPFSCP – Beneficiário pessoa física da sociedade em conta de participação RISCP – Lucros e dividendos pagos ao sócio da sociedade em conta de participação BPJSCP – Beneficiário pessoa jurídica da sociedade em conta de participação RISCP – Lucros e dividendos pagos ao sócio da sociedade em conta de participação PSE – Plano privado de assistência à saúde – coletivo empresarial OPSE – Operadora de plano privado de assistência à saúde – coletivo empresarial TPSE – Titular de plano privado de assistência à saúde – coletivo empresarial RTPSE – Reembolso do titular do plano de assistência à saúde – coletivo empresarial DTPSE – Dependente do titular de plano privado de assistência à saúde – coletivo empresarial RDTPSE – Reembolso do dependente do titular do plano de assistência à saúde – coletivo empresarial RPDE – Rendimentos pagos a residentes ou domiciliados no exterior BRPDE – Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE – Valores de rendimentos pagos a residentes ou domiciliados no exterior INF – Informações complementares para o comprovante de rendimentos FIMDirf – Término da declaração

2.2 Estrutura completa de uma declaração de Pessoa Jurídica

Dirf – Declaração do imposto sobre a renda retido na fonte RESPO – Responsável pelo preenchimento DECPJ – Declarante pessoa jurídica IDREC – Identificação do código de receita BPFDEC – Beneficiário pessoa física do declarante RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTDP – Rendimentos Tributáveis – Dedução – Dependentes RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte CJAC – Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA – Compensação de Imposto por Decisão Judicial – Anos Anteriores ESRT – Tributação com Exigibilidade Suspensa – Rendimento Tributável ESPO – Tributação com Exigibilidade Suspensa – Dedução – Previdência Oficial ESDP – Tributação com Exigibilidade Suspensa – Dedução – Dependentes ESIR – Tributação com Exigibilidade Suspensa – Imposto sobre a Renda na Fonte ESDJ – Tributação com Exigibilidade Suspensa – Depósito Judicial INFPC – Informações de Previdência Complementar RTPP – Rendimentos Tributáveis – Dedução – Previdência Privada RTFA – Rendimentos Tributáveis – Dedução – FAPI RTSP – Rendimentos Tributáveis – Dedução – Fundo de Previdência do Servidor Público RTEP – Rendimentos Tributáveis – Dedução – Contribuição do ente público patrocinador ESPP – Tributação com Exigibilidade Suspensa – Dedução – Previdência Privada ESFA – Tributação com Exigibilidade Suspensa – Dedução – FAPI ESSP – Tributação com Exigibilidade Suspensa – Dedução – Fundo de Previdência do Servidor Público ESEP – Tributação com Exigibilidade Suspensa – Dedução – Contribuição do ente público patrocinador

INFPA – Informações do beneficiário da pensão alimentícia RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia ESPA – Tributação com Exigibilidade Suspensa – Dedução – Pensão Alimentícia RIDAC – Rendimentos Isentos – Diária e Ajuda de Custo RIIRP – Rendimentos Isentos – Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV RIAP – Rendimentos Isentos – Abono Pecuniário RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave RIP65 – Rendimentos Isentos – Parcela Isenta de Aposentadoria (65 anos ou mais) RIBMR – Rendimentos Isentos – Bolsa de Estudo Recebida por Médico-residente RICAP – Rendimentos Isentos – Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIRPC – Rendimentos Isentos – Resgate de previdência complementar por portador de moléstia grave RIL96 – Rendimentos Isentos Anuais – Lucros e dividendos pagos a partir de 1996 RIPTS – Rendimentos Isentos Anuais – Valores pagos a titular ou sócio ou empresa de pequeno porte, exceto pró-labore e aluguéis RIJMRE – Rendimentos Isentos Anuais – Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função RIO – Rendimentos Isentos Anuais – Outros BPJDEC – Beneficiário pessoa jurídica do declarante RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte VPEIM – Valores pagos às entidades imunes ou isentas – IN RFB 1.234/2012 RIMUN – Rendimentos Imunes – art. 4º, inciso III RISEN – Rendimentos Isentos – art. 4º, inciso IV FCI – Fundo ou clube de investimento IDREC – Identificação do código de receita BPFFCI – Beneficiário pessoa física do fundo ou clube de investimento RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte CJAC – Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA – Compensação de Imposto por Decisão Judicial – Anos Anteriores ESRT – Tributação com Exigibilidade Suspensa – Rendimento Tributável ESIR – Tributação com Exigibilidade Suspensa – Imposto sobre a Renda na Fonte ESDJ – Tributação com Exigibilidade Suspensa – Depósito Judicial RIP65 – Rendimentos Isentos – Parcela Isenta de Aposentadoria (65 anos ou mais) RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave RICAP – Rendimentos Isentos – Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIO – Rendimentos Isentos Anuais – Outros BPJFCI – Beneficiário pessoa jurídica do fundo ou clube de investimento RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte PROC – Processo da justiça do trabalho/federal/estadual/Distrito Federal IDREC – Identificação do código de receita BPFPROC – Beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial RTDP – Rendimentos Tributáveis – Dedução – Dependentes RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte CJAC – Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA – Compensação de Imposto por Decisão Judicial – Anos Anteriores ESRT – Tributação com Exigibilidade Suspensa – Rendimento Tributável ESPO – Tributação com Exigibilidade Suspensa – Dedução – Previdência Oficial ESDP – Tributação com Exigibilidade Suspensa – Dedução – Dependentes ESIR – Tributação com Exigibilidade Suspensa – Imposto sobre a Renda na Fonte ESDJ – Tributação com Exigibilidade Suspensa – Depósito Judicial RTPP – Rendimentos Tributáveis – Dedução – Previdência Privada RTFA – Rendimentos Tributáveis – Dedução – FAPI RTSP – Rendimentos Tributáveis – Dedução – Fundo de Previdência do Servidor Público ESPP – Tributação com Exigibilidade Suspensa – Dedução – Previdência Privada ESFA – Tributação com Exigibilidade Suspensa – Dedução – FAPI ESSP – Tributação com Exigibilidade Suspensa – Dedução – Fundo de Previdência do Servidor Público RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia ESPA – Tributação com Exigibilidade Suspensa – Dedução – Pensão Alimentícia RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave RIJMRE – Rendimentos Isentos Anuais – Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função RIRSR – Rendimentos pagos sem retenção do IR na fonte – Lei nº 10.833/2003

BPJPROC – Beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT – Rendimentos Tributáveis – Rendimento Tributável RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte RIRSR – Rendimentos pagos sem retenção do IR na fonte – Lei nº 10.833/2003 RRA – Rendimentos recebidos acumuladamente IDREC – Identificação do código de receita BPFRRA – Beneficiário pessoa física do rendimento recebido acumuladamente RTRT – Rendimentos Tributáveis – Rendimento Tributável RTPO – Rendimentos Tributáveis – Dedução – Previdência Oficial INFPA – Informações do beneficiário da pensão alimentícia RTPA – Rendimentos Tributáveis – Dedução – Pensão Alimentícia RTIRF – Rendimentos Tributáveis – Imposto sobre a Renda Retido na Fonte RIMOG – Rendimentos Isentos – Pensão, Aposentadoria ou Reforma por Moléstia Grave RIP65 – Rendimentos Isentos – Parcela Isenta de Aposentadoria (65 anos ou mais) RIJMRE – Rendimentos Isentos Anuais – Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função DAJUD – Despesa com ação judicial QTMESES – Quantidade de meses SCP – Informações da sociedade em conta de participação BPFSCP – Beneficiário pessoa física da sociedade em conta de participação RISCP – Lucros e dividendos pagos ao sócio da sociedade em conta de participação BPJSCP – Beneficiário pessoa jurídica da sociedade em conta de participação RISCP – Lucros e dividendos pagos ao sócio da sociedade em conta de participação PSE – Plano privado de assistência à saúde – coletivo empresarial OPSE – Operadora de plano privado de assistência à saúde – coletivo empresarial TPSE – Titular de plano privado de assistência à saúde – coletivo empresarial RTPSE – Reembolso do titular do plano de assistência à saúde – coletivo empresarial DTPSE – Dependente do titular de plano privado de assistência à saúde – coletivo empresarial RDTPSE – Reembolso do dependente do titular do plano de assistência à saúde – coletivo empresarial RPDE – Rendimentos pagos a residentes ou domiciliados no exterior BRPDE – Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE – Valores de rendimentos pagos a residentes ou domiciliados no exterior INF – Informações complementares para o comprovante de rendimentos FIMDirf – Término da declaração

3. Leiaute do arquivo 3.1 Registro de identificação da declaração (identificador Dirf)

- Registro obrigatório no arquivo; - Deve ser o primeiro registro no arquivo; - Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 4 Dirf Sim 2 Ano referência N Fixo 4 2023 Sim 3 Ano-calendário N Fixo 4 2022 ou 2023 Sim S – Retificadora 4 Indicador de retificadora C Fixo 1 Sim N – Original 5 Número do recibo N Fixo 12 - Não 6 Identificador de estrutura do leiaute C Fixo 7 ARNZRXP Sim

Observações: Ordem Campo Descrição O preenchimento será obrigatório se o campo de ordem 4 igual a “S” e declaração 5 Número do recibo transmitida sem o uso de certificação digital.

3.2 Registro do Responsável pelo preenchimento da declaração (identificador RESPO)

- Registro obrigatório no arquivo; - Deve ser o segundo registro no arquivo; - Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 5 RESPO Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 DDD N Fixo 2 - Sim 5 Telefone N Variável 9 - Sim 6 Ramal N Variável 6 - Não 7 Fax N Variável 9 - Não 8 Correio eletrônico C Variável 50 - Não

Observações: Ordem Campo Descrição 4 DDD O primeiro algarismo deve ser diferente de zero. 5 Telefone Deve ser preenchido com oito ou nove algarismos. 7 Fax Deve ser preenchido com oito ou nove algarismos.

3.3 Registro de identificação do declarante pessoa física (identificador DECPF)

- Registro obrigatório no arquivo para declarante pessoa física; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPJ.

1 Identificador de registro C Fixo 5 DECPF Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Indicador de declarante de rendimentos S – Pagou rendimentos a 4 pagos a residentes ou domiciliados no C Fixo 1 residentes ou domiciliados no Sim exterior exterior N – Não pagou rendimentos a residentes ou domiciliados no exterior Indicador de Titular de Serviços Notariais S – Titular de serviços notariais e 5 C Fixo 1 Sim e de Registros de registros

N – Não é titular de serviços notariais e de registros S – Existe pagamento de valor Indicador de plano privado de assistência 6 C Fixo 1 pelo titular/dependente do Sim à saúde – coletivo empresarial plano de saúde N – Não existe pagamento de valor pelo titular/dependente do plano de saúde Indicador de sócio ostensivo responsável S – Sócio ostensivo 7 por sociedade em conta de participação – C Fixo 1 Sim N – Não é sócio ostensivo SCP S – Encerramento de Indicador de situação especial da espólio/saída definitiva do país 8 C Fixo 1 Sim declaração N – Não é encerramento de espólio/saída definitiva do país 9 Data do Evento D Fixo 8 - Não 1 – Encerramento de espólio 10 Tipo de Evento N Fixo 1 Não 2 – Saída definitiva do Brasil S – Declarante falecido 11 Indicador de declarante falecido C Fixo 1 Sim N – Declarante não falecido 12 Data do óbito D Fixo 8 - Não 0 – Sem espólio 13 Situação do espólio N Fixo 1 Não 1 – Espólio não encerrado 14 CPF do inventariante N Fixo 11 - Não 15 Nome do inventariante C Variável 60 - Não

Observações: Ordem Campo Descrição 9 Data do Evento O preenchimento será obrigatório se o campo de ordem 8 igual a “S”. 10 Tipo de Evento O preenchimento será obrigatório se o campo de ordem 8 igual a “S”. 11 Indicador de declarante falecido Deve ser preenchido com “S” se o campo de ordem 8 igual a “S” e campo de ordem 10 igual a 1 13 Situação do espólio Permitido somente para as declarações normais Para o encerramento de espólio a declaração será sempre de situação especial; Declarante falecido – indicador igual a SIM Situação 1 – sem espólio - Apresentar declaração normal do ano-calendário; - Informar data do óbito e situação do espólio igual a 0; Observação: não serão aceitas declarações para anos posteriores ao ano da data do óbito sem espólio; Situação 2 – com espólio não encerrado - Apresentar declaração normal do ano-calendário; - Informar data do óbito e situação do espólio igual a 1; Observação: serão aceitas declarações para anos posteriores ao ano da data do óbito até que seja apresentada uma declaração de situação especial – encerramento de espólio; Situação 3 – encerramento de espólio - Apresentar declaração de situação especial do ano-calendário; Observação: os campos 12 a 15 não serão preenchidos;

3.4 Registro de identificação do declarante pessoa jurídica (identificador DECPJ)

- Registro obrigatório no arquivo para declarante pessoa jurídica; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPF.

1 Identificador de registro C Fixo 5 DECPJ Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 0 – Pessoa jurídica de direito 4 Natureza do declarante N Fixo 1 Sim privado

1 – Órgãos, autarquias e fundações da administração pública federal 2 – Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal 3 – Empresa pública ou sociedade de economia mista federal 4 – Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal 8 – Entidade com alteração de natureza jurídica (uso restrito) 5 CPF responsável perante o CNPJ N Fixo 11 - Sim Indicador de sócio ostensivo responsável S – Sócio ostensivo 6 por sociedade em conta de participação – C Fixo 1 Sim N – Não é sócio ostensivo SCP S – Depositário de crédito Indicador de declarante depositário de decorrente de decisão judicial 7 C Fixo 1 Sim crédito decorrente de decisão judicial N – Não é depositário de crédito decorrente de decisão judicial Indicador de declarante de instituição S – Instituição administradora ou 8 administradora ou intermediadora de C Fixo 1 intermediadora de fundo ou Sim fundo ou clube de investimento clube de investimento N – Não é instituição administradora ou intermediadora de fundo ou clube de investimento Indicador de declarante de rendimentos S – Pagou rendimentos a 9 pagos a residentes ou domiciliados no C Fixo 1 residentes ou domiciliados no Sim exterior exterior N – Não pagou rendimentos a residentes ou domiciliados no exterior S – Existe pagamento de valor Indicador de plano privado de assistência 10 C Fixo 1 pelo titular/dependente do Sim à saúde – coletivo empresarial plano de saúde N – Não existe pagamento de valor pelo titular/dependente do plano de saúde Indicador de entidade em que a União S – Existe pagamento de valores 11 detém maioria do capital social sujeito a C Fixo 1 Sim a entidades imunes/isentas voto, recebe recursos do Tesouro Nacional e está obrigada a registrar a N – Não existe pagamento de execução orçamentária no Siafi (IN valores a entidades 1.234/2012, art. 4º, incisos III e IV) imunes/isentas S – Fundação pública de direito Indicador de fundação pública de direito privado 12 privado instituída pela União, Estados, C Fixo 1 Sim N – Não é fundação pública de Municípios ou Distrito Federal direito privado S – Declaração de situação Indicador de situação especial da especial 13 C Fixo 1 Sim declaração N – Não é declaração de situação especial 14 Data do evento D Fixo 8 - Não

Observações: Ordem Campo Descrição Relativamente à natureza do declarante 8 – Entidade com alteração de natureza 4 Natureza do declarante jurídica (uso restrito), esclarecemos: 1. Para declarante que alterou sua natureza jurídica em relação ao ano-calendário e que implique em mudança da natureza do declarante na ficha Informações da Dirf;

2. Para declarante que mudou sua natureza jurídica de órgão público para privado, ou vice-versa. Aplica-se ainda para mudanças entre as esferas governamentais da federação. Por exemplo: órgão público ou pessoa jurídica de direito privado estadual ou municipal que passou a ser federal, ou vice-versa; 3. A declaração deverá ser entregue na RFB. Indicador de entidade em que a União Indicador com a opção “Sim” permitido somente se campo de ordem 4 – Natureza do 11 detém maioria do capital social sujeito a declarante, igual a “0”, “1”, “3” ou “8” voto, recebe recursos do Tesouro Nacional e está obrigada a registrar a execução orçamentária no Siafi (IN 1.234/2012, art. 4º, incisos III e IV) Indicador de fundação pública de direito Indicador com a opção “S” permitido somente se campo de ordem 4 – Natureza do 12 privado instituída pela União, Estados, declarante, igual a “1”, “2” ou “8” Municípios ou Distrito Federal Para as demais naturezas do declarante deve ser igual a “N” 14 Data do evento O preenchimento será obrigatório se o campo de ordem 13 igual a “S”.

3.5 Registro de identificação do código de receita (identificador IDREC)

- Deve ser apresentado com os códigos de receita em ordem crescente; - Deve estar associado aos registros do tipo DECPF, DECPJ, FCI, PROC ou RRA.

1 Identificador de registro C Fixo 5 IDREC Sim De acordo com a tabela de 2 Código de receita N Fixo 4 códigos de receitas constante na Sim IN que dispõe sobre a Dirf

3.6 Registro de beneficiário pessoa física do declarante (identificador BPFDEC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFDEC Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Data atribuída pelo laudo da moléstia Não 4 D Fixo 8 - grave Indicador de identificação do S – Existem informações Sim 5 C Fixo 1 alimentando detalhadas do alimentando N – Não existem informações detalhadas do alimentando S – Existem informações Sim Indicador de identificação da previdência 6 C Fixo 1 detalhadas da previdência complementar complementar N – Não existem informações detalhadas da previdência complementar

Observações: Ordem Campo Descrição Indicador de identificação do Se campo igual a “S” – deverá constar o registro INFPA seguido do registro de valor

alimentando (RTPA e/ou ESPA) para cada alimentando. Se campo igual a “N” – não apresentar o registro INFPA; deverão constar os registros de valores (RTPA e/ou ESPA) com o valor total de pensão alimentícia pago a todos os alimentandos do beneficiário. – As informações detalhadas a que se refere o campo são: CPF, data de nascimento, nome e relação de dependência do alimentando (registro INFPA). Se campo igual a “S” – deverá constar o registro INFPC seguido do registro de valor Indicador de identificação da previdência 6 (RTPP, RTFA, RTSP e/ou ESPP, ESFA, ESSP) para cada entidade de previdência complementar complementar do beneficiário. Se campo igual a “N” – não apresentar o registro INFPC; deverão constar apenas os

registros de valores mensais (RTPP, RTFA, RTSP e/ou ESPP, ESFA, ESSP) com o total dos valores de previdência complementar pagos pelo beneficiário. – As informações detalhadas a que se refere o campo são: CNPJ e Nome empresarial da entidade de previdência complementar (registro INFPC).

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

1 Identificador de registro C Fixo 6 BPFFCI Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Data atribuída pelo laudo da moléstia D Fixo 8 - Não grave

3.11 Registro do beneficiário pessoa jurídica do fundo ou clube de investimento (identificador BPJFCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPJFCI Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.12 Registro de processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador PROC)

- Deve estar classificado em ordem crescente por: - Tipo de justiça; - Número do processo; - Deve estar associado ao registro do tipo DECPJ.

1 Identificador de registro C Fixo 4 PROC Sim 1 – Justiça federal 2 – Justiça do trabalho 2 Indicador de Justiça N Fixo 1 Sim 3 – Justiça estadual/Distrito Federal 3 Número do processo C Variável 20 - Sim Indicador de tipo de advogado/escritório 1 – Pessoa física 4 N Fixo 1 Não de advocacia 2 – Pessoa jurídica CPF do advogado/ CNPJ do escritório de CPF com 11 dígitos 5 N Variável 14 Não advocacia CNPJ com 14 dígitos Nome da pessoa física até 60 Nome do advogado/ Nome empresarial posições 6 C Variável 150 Não do escritório de advocacia Nome empresarial da pessoa jurídica até 150 posições 7 Valor pago para o advogado N Variável 13 Valor pago para o advogado Não

3.13 Registro de beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPFPROC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 7 BPFPROC Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Data atribuída pelo laudo da moléstia D Fixo 8 - Não grave

3.14 Registro de beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPJPROC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 7 BPJPROC Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.15 Registro de rendimentos recebidos acumuladamente (identificador RRA)

- Deve estar classificado em ordem crescente por: - Identificador de rendimento recebido acumuladamente; - Número do processo/requerimento.

1 Identificador de registro C Fixo 3 RRA Sim Identificador de rendimento recebido 1 – Pago pelo declarante 2 N Fixo 1 Sim acumuladamente 2 – Pago pela justiça 3 Número do processo/requerimento C Variável 20 - Não Indicador de tipo de advogado/escritório 1 – Pessoa física 4 N Fixo 1 Não de advocacia 2 – Pessoa jurídica CPF do advogado/CNPJ do escritório de CPF com 11 dígitos 5 N Variável 14 Não advocacia CNPJ com 14 dígitos Nome da pessoa física com até Nome do advogado/Nome empresarial 60 posições 6 C Variável 150 Não do escritório de advocacia Nome empresarial da pessoa jurídica com até 150 posições 7 Valor pago para o advogado N Variável 13 Valor pago para o advogado Não

Observações: Ordem Campo Descrição 3 Número do processo/requerimento O preenchimento será obrigatório se o campo de ordem 2 igual a 2.

3.16 Registro de beneficiário pessoa física dos rendimentos recebidos acumuladamente (identificador BPFRRA)

- Deve estar classificado em ordem crescente por: - CPF; - Natureza do RRA; - Deve estar associado ao registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFRRA Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Natureza do RRA C Variável 50 - Não Data atribuída pelo laudo da moléstia 5 D Fixo 8 - Não grave Indicador de identificação do S – Existem informações 6 C Fixo 1 Sim alimentando detalhadas do alimentando N – Não existem informações detalhadas do alimentando

Observações: Ordem Campo Descrição Indicador de identificação do 1. O campo só poderá ser igual a “S” se o campo 2 do registro RRA igual a “1” (Pago

alimentando pelo declarante); 2. Se campo igual a “S” – deverá constar o registro INFPA e RTPA para cada alimentando; 3. Se campo igual a “N” – não apresentar o registro INFPA; deverá constar o registro RTPA com o valor de pensão alimentícia pago a todos os alimentandos do beneficiário; 4. As informações detalhadas a que se refere o campo são: CPF, Data de nascimento e Nome do alimentando (registro INFPA).

3.17 Registro de identificação de Previdência Complementar (identificador INFPC)

- Registro permitido somente se campo 6 do registro BPFDEC (Indicador de identificação da previdência complementar) igual a “S”; - Serão apresentados todos os CNPJ em ordem crescente; - Deve estar associado ao registro do tipo BPFDEC; - Deve constar um registro INFPC para cada CNPJ de entidade de previdência complementar.

1 Identificador de registro C Fixo 5 INFPC Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim

3.18 Registro de informações do beneficiário da pensão alimentícia (identificador INFPA)

- Registro permitido somente se Indicador de identificação do alimentando igual a “S” (BPFDEC, campo 5; e BPFRRA, campo 6); - Registro INFPA associado ao BPFRRA será permitido somente quando o identificador de rendimento recebido acumuladamente igual a “1 – Pago pelo declarante” (campo 2 do registro RRA); - Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo BPFDEC, BPFRRA.

1 Identificador de registro C Fixo 5 INFPA Sim 2 CPF do alimentando N Fixo 11 - Não 3 Data de nascimento D Fixo 8 - Não 4 Nome C Variável 60 - Sim 5 Relação de dependência N Fixo 2 03 – Cônjuge/ Companheiro (a) Não 04 – Filho (a) 06 – Enteado (a) 08 – Pai/Mãe 10 – Agregado/Outros

Observações: Ordem Campo Descrição Preenchimento obrigatório para maiores de 18 anos completos até 31 de dezembro 2 CPF do alimentando do ano-calendário da declaração. Preenchimento obrigatório para menores de 18 anos completos até 31 de dezembro 3 Data de nascimento do ano-calendário da declaração, que não tenham informado o CPF.

3.19 Registro de valores mensais (identificadores RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTIRF, CJAA, CJAC, ESRT, ESPO, ESPP, ESFA, ESSP, ESEP, ESDP, ESPA, ESIR, ESDJ, RIP65, RIDAC, RIIRP, RIAP, RIMOG, RIRPC, RIBMR, RICAP, RISCP, RIMUN, RISEN e DAJUD)

- Deve ocorrer apenas se houver pelo menos um dos valores referentes aos meses ou 13º salário; - Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC, BPJDEC, BPFFCI, BPJFCI, BPFPROC, BPJPROC, BPFRRA, BPFSCP, BPJSCP, INFPC, INFPA, VPEIM.

RTRT RTPO 1 Identificador de registro C Variável 5 RTPP Sim RTFA RTSP RTEP RTDP RTPA RTIRF CJAC CJAA ESRT ESPO ESPP ESFA ESSP ESEP ESDP ESPA

ESIR ESDJ RIP65 RIDAC RIIRP RIAP RIMOG RIRPC RIBMR RICAP RISCP RIMUN RISEN DAJUD 2 Janeiro N Variável 13 - Não 3 Fevereiro N Variável 13 - Não 4 Março N Variável 13 - Não 5 Abril N Variável 13 - Não 6 Maio N Variável 13 - Não 7 Junho N Variável 13 - Não 8 Julho N Variável 13 - Não 9 Agosto N Variável 13 - Não 10 Setembro N Variável 13 - Não 11 Outubro N Variável 13 - Não 12 Novembro N Variável 13 - Não 13 Dezembro N Variável 13 - Não 14 Décimo Terceiro N Variável 13 - Não

3.20 Registro de valores anuais isentos/não tributáveis/sem retenção (identificadores RIL96, RIPTS, RIJMRE e RIRSR)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC (RIL96, RIPTS e RIJMRE), BPFPROC/BPJPROC (RIRSR); - Registro RIRSR permitido somente se “indicador de justiça” do registro PROC igual a 1 (Justiça Federal).

RIL96 RIPTS 1 Identificador de registro C Variável 6 Sim RIJMRE RIRSR 2 Valor pago no ano N Variável 13 - Sim

3.21 Registro de valores anuais de rendimentos isentos – outros (identificador RIO)

- Ocorrerá apenas um registro para cada beneficiário; - Deve estar associado ao registro do tipo BPFDEC ou BPFFCI.

1 Identificador de registro C Fixo 3 RIO Sim 2 Valor pago no ano N Variável 13 - Sim 3 Descrição dos rendimentos isentos – C Variável 60 - Sim outros

3.22 Registro de quantidade de meses (identificador QTMESES)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado ao registro do tipo BPFRRA.

1 Identificador de registro C Fixo 7 QTMESES Sim

2 Quantidade meses – janeiro N Variável 4 - Não 3 Quantidade meses – fevereiro N Variável 4 - Não 4 Quantidade meses – março N Variável 4 - Não 5 Quantidade meses – abril N Variável 4 - Não 6 Quantidade meses – maio N Variável 4 - Não 7 Quantidade meses – junho N Variável 4 - Não 8 Quantidade meses – julho N Variável 4 - Não 9 Quantidade meses – agosto N Variável 4 - Não 10 Quantidade meses – setembro N Variável 4 - Não 11 Quantidade meses – outubro N Variável 4 - Não 12 Quantidade meses – novembro N Variável 4 - Não 13 Quantidade meses – dezembro N Variável 4 - Não

3.23 Registro de informações da Sociedade em Conta de Participação (identificador SCP)

- Serão apresentados em ordem crescente de CNPJ. - Deve constar um registro para cada CNPJ de Sociedade em conta de participação

1 Identificador de registro C Fixo 3 SCP Sim 2 CNPJ da Sociedade em Conta de N Fixo 14 - Sim Participação 3 Nome empresarial da Sociedade em C Variável 150 - Sim Conta de Participação

3.24 Registro de beneficiário pessoa física da sociedade em conta de participação (identificador BPFSCP)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJSCP, caso exista o registro; - Deve estar associado a um registro do tipo SCP.

1 Identificador de registro C Fixo 6 BPFSCP Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Percentual de participação na SCP N Variável 4 - Não

3.25 Registro de beneficiário pessoa jurídica da sociedade em conta de participação (identificador BPJSCP)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFSCP, caso exista o registro; - Deve estar associado a um registro do tipo SCP.

1 Identificador de registro C Fixo 6 BPJSCP Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 4 Percentual de participação na SCP C Variável 4 - Não

3.26 Registro de pagamentos a plano privado de assistência à saúde – coletivo empresarial (identificador PSE)

- Ocorre somente uma vez no arquivo, caso exista informação de valores pagos pelo titular/dependente do plano de assistência à saúde.

1 Identificador de registro C Fixo 3 PSE Sim

3.27 Registro de operadora do plano privado de assistência à saúde – coletivo empresarial (identificador OPSE)

- Ocorre caso exista o registro PSE; - Serão apresentados todos os CNPJ em ordem crescente.

1 Identificador de registro C Fixo 4 OPSE Sim CNPJ da operadora de plano privado de 2 N Fixo 14 - Sim assistência à saúde – coletivo empresarial 3 Nome empresarial C Variável 150 - Sim 4 Registro ANS N Fixo 6 - Não

3.28 Registro de titular do plano privado de assistência à saúde – coletivo empresarial (identificador TPSE)

- Serão apresentados todos os CPF em ordem crescente. - Deve estar associado ao registro do tipo OPSE.

1 Identificador de registro C Fixo 4 TPSE Sim 2 CPF do titular N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Valor pago no ano N Variável 9 - Sim

Observações: Ordem Campo Descrição Preenchimento obrigatório se o titular não possuir dependente cadastrado e nem 4 Valor pago no ano reembolso informado.

3.29 Registro de informação de reembolso do titular do plano de saúde – coletivo empresarial (identificador RTPSE)

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo TPSE; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos-calendário anteriores.

1 Identificador de registro C Fixo 5 RTPSE Sim CPF com 11 dígitos 2 CPF/CNPJ do prestador de serviço N Variável 14 Sim CNPJ com 14 dígitos Nome da pessoa física até 60 Nome/Nome empresarial do prestador posições 3 C Variável 150 Sim de serviço Nome empresarial da pessoa jurídica até 150 posições 4 Valor do reembolso do ano-calendário N Variável 9 - Não 5 Valor do reembolso de anos anteriores N Variável 9 - Não

Observações: Ordem Campo Descrição Valores reembolsados no ano-calendário, referentes a pagamentos de serviços 4 Valor do reembolso do ano-calendário prestados no ano-calendário. Valores reembolsados no ano-calendário referentes a pagamentos de serviços 5 Valor do reembolso de anos anteriores prestados em anos anteriores.

3.30 Registro de dependente do plano privado de assistência à saúde – coletivo empresarial (identificador DTPSE)

- Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo TPSE.

1 Identificador de registro C Fixo 5 DTPSE Sim 2 CPF do dependente N Fixo 11 - Não 3 Data de nascimento D Fixo 8 - Não 4 Nome C Variável 60 - Sim 03 – Cônjuge/ Companheiro(a) 04 – Filho(a) 5 Relação de dependência N Fixo 2 06 – Enteado(a) Não 08 – Pai/Mãe 10 – Agregado/ Outros 6 Valor pago no ano N Variável 9 - Sim

Observações: Ordem Campo Descrição CPF do dependente Preenchimento obrigatório para maiores de 18 anos completos até 31 de dezembro

do ano-calendário da declaração. Data de nascimento Preenchimento obrigatório para menores de 18 anos completos até 31 de dezembro

do ano-calendário da declaração, que não tenham informado o CPF. 6 Valor pago no ano Preenchimento obrigatório se o dependente não possuir reembolso informado.

3.31 – Registro de informação de reembolso do dependente (identificador RDTPSE):

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo DTPSE; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos-calendário anteriores.

1 Identificador de registro C Fixo 6 RDTPSE Sim CPF com 11 dígitos 2 CPF/CNPJ do prestador de serviço N Variável 14 Sim CNPJ com 14 dígitos Nome da pessoa física até 60 Nome/Nome Empresarial do prestador posições 3 C Variável 150 Sim de serviço Nome empresarial da pessoa jurídica até 150 posições 4 Valor do reembolso do ano-calendário N Variável 9 - Não 5 Valor do reembolso de anos anteriores N Variável 9 - Não

Observações: Ordem Campo Descrição Valor do reembolso do ano-calendário Valores reembolsados no ano-calendário, referentes a pagamentos de serviços

prestados no ano-calendário Valor do reembolso de anos anteriores Valores reembolsados no ano-calendário referentes a pagamentos de serviços

prestados em anos anteriores

3.32 Registro de rendimentos pagos a residentes ou domiciliados no exterior (identificador RPDE)

- Ocorre somente uma vez no arquivo, caso exista informação de rendimentos pagos a residentes ou domiciliados no exterior

1 Identificador de registro C Fixo 4 RPDE Sim

3.33 Registro de beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior (identificador BRPDE)

- Deve estar classificado em ordem crescente por: - Beneficiário; - Código de país;

- Número de identificação fiscal – NIF; - Deve estar associado ao registro do tipo RPDE.

1 Identificador de registro C Fixo 5 BRPDE Sim 1 – Pessoa física 2 Beneficiário N Fixo 1 Sim 2 – Pessoa jurídica De acordo com a tabela de 3 Código de país N Variável 3 código dos países constante na Sim IN que dispõe sobre a Dirf 4 Número de identificação fiscal – NIF C Variável 30 - Não S – Dispensado do Número de identificação fiscal – NIF Indicador de beneficiário dispensado do 5 C Fixo 1 N – Não é dispensado do Sim Número de Identificação Fiscal – NIF Número de identificação fiscal – NIF S – Dispensado do Número de identificação fiscal – NIF Indicador de que o país não exige 6 C Fixo 1 N – Não é dispensado do Sim Número de Identificação Fiscal – NIF Número de identificação fiscal – NIF CPF com 11 dígitos 7 CPF/CNPJ N Variável 14 Não CNPJ com 14 dígitos 8 Nome/Nome empresarial C Variável 150 - Sim De acordo com a tabela de informações sobre os Relação fonte pagadora pessoa jurídica e 9 N Fixo 3 beneficiários dos rendimentos Não beneficiário pessoa jurídica constante na IN que dispõe sobre a Dirf 10 Logradouro C Variável 60 - Não 11 Número C Variável 6 - Não 12 Complemento C Variável 25 - Não 13 Bairro/Distrito C Variável 20 - Não 14 Código postal N Variável 10 - Não 15 Cidade C Variável 40 - Não 16 Estado/Província C Variável 40 - Não 17 Telefone N Variável 15 - Não

Observações: Ordem Campo Descrição Relação fonte pagadora pessoa jurídica e Preenchimento obrigatório se campo de ordem 2 (Beneficiário) igual a 2.

beneficiário pessoa jurídica

3.34 Registro de valores de rendimentos pagos a residentes ou domiciliados no exterior (identificador VRPDE)

- Deve estar classificado em ordem crescente por: - Data do pagamento; - Código de receita; - Deve estar associado ao registro do tipo BRPDE.

1 Identificador de registro C Fixo 5 VRPDE Sim 2 Data do pagamento D Fixo 8 - Sim 3 Código de receita N Fixo 4 - Sim De acordo com a tabela de informações sobre os 4 Tipo de rendimento N Fixo 3 Sim rendimentos constante na IN que dispõe sobre a Dirf 5 Rendimento pago N Variável 13 - Sim 6 Imposto retido N Variável 13 - Não De acordo com a tabela de 7 Forma de tributação N Fixo 2 informações sobre a forma de Sim tributação constante na IN que

dispõe sobre a Dirf

3.35 Registro de informações complementares para o comprovante de rendimento (identificador INF)

- Serão apresentados todos os CPF em ordem crescente; - Deve haver um registro BPFDEC, BPFPROC e/ou BPFRRA correspondente na declaração; - Deve ocorrer apenas um registro para cada beneficiário.

1 Identificador de registro C Fixo 3 INF Sim 2 CPF N Fixo 11 - Sim 3 Informações complementares C Variável 500 - Sim

3.36 Registro identificador do término da declaração (identificador FIMDirf)

- Registro obrigatório no arquivo; - Deve ser o último registro no arquivo; - Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 7 FIMDirf Sim

