---
titulo: "Ato Declaratório Executivo Cofis nº 56, de 23 de novembro de 2023"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "56"
data: "2023-11-23"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 28/11/2023, seção 1, página 34"
data_publicacao: "2023-11-28"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/134962/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/134962/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "134962"
sha256_texto: "eefe58034891caf3a767788c9ee2a9c3fadaf590e6d346bfbdb32b73fc914934"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Cofis nº 56, de 23 de novembro de 2023

Dispõe sobre o leiaute do Programa Gerador da Declaração do Imposto sobre a Renda Retido na Fonte (PGD Dirf 2024)

O COORDENADOR-GERAL DE FISCALIZAÇÃO, no uso das atribuições que lhe conferem os incisos I e II do art. 121 e inciso II do art. 358 do Regimento Interno da Secretaria Especial da Receita Federal do Brasil, aprovado pela Portaria ME nº 284, de 27 de julho de 2020, e tendo em vista o disposto na Instrução Normativa RFB nº 1.990, de 18 de novembro de 2020, declara:

**Art.1º** Fica aprovado o leiaute aplicável aos campos, registros e arquivos da Declaração do Imposto sobre a Renda Retido na Fonte (Dirf 2024) para apresentação das informações relativas aos anos calendário de 2023, situação normal, e 2024, nos casos de situação especial.

**Art.2º** Para o preenchimento ou importação de dados pelo PGD Dirf 2024 deverá ser observado o leiaute do arquivo constante do Anexo Único deste Ato Declaratório.

**Art.3º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

RICARDO DE SOUZA MOREIRA

Anexo Único

Anexo Único

ANEXO ÚNICO

LEIAUTE DO ARQUIVO Declaração do Imposto sobre a Renda Retido na Fonte - Dirf 1. Regras gerais Estas regras devem ser respeitadas em todos os arquivos gerados, quando não excepcionadas por regra específica referente a um dado registro e explicitada em suas observações.

Nº Regra de preenchimento Descrição ALFANUMÉRICO (C): representados por "C" - todos os caracteres, excetuados o caractere "|" (pipe ou barra vertical). 1 Formato dos campos NUMÉRICO (N): representados por "N" - pode conter apenas os valores de zero a nove. Campos numéricos (D) Devem ser informados conforme o padrão ano, mês e dia 2 cujo conteúdo representa (AAAAMMDD), excluindo-se quaisquer caracteres de separação data (tais como ".", "/", "-", etc.); Os campos numéricos com número de inscrição (CNPJ e CPF) Campos numéricos com ou códigos de receita deverão ser informados com todos os 3 número de inscrição ou dígitos, inclusive os zeros à esquerda; códigos de receita As máscaras (caracteres especiais de formatação, tais como ".", "/", "-", etc.) não devem ser informadas. Devem ser informados com até 13 posições, representando 11 posições inteiras e 2 decimais; Campos numéricos Os zeros não significativos não devem ser informados;

referentes a valores Os caracteres "." (ponto) e "," (vírgula) não devem ser informados; Todos os valores monetários devem estar expressos em reais. Os campos com conteúdo alfanumérico nos quais se faz necessário registrar números ou códigos de identificação Campos alfanuméricos (Exemplo: Número de Identificação Fiscal - NIF) deverão seguir 5 com números ou códigos a regra de formação e tamanho definidos pelo respectivo órgão de identificação regulador; As máscaras (caracteres especiais de formatação, tais como ".", "/", "-", etc.) não devem ser informadas. Ao final de cada campo (inclusive o último de cada registro) 6 Formação dos campos deve ser inserido o caractere delimitador "|" (pipe ou barra vertical: caractere 124 da Tabela ASCII); O caractere delimitador "|" (barra vertical) não deve ser incluído como parte integrante do conteúdo de quaisquer campos numéricos, datas ou alfanuméricos; Na ausência de informação, o campo vazio (campo sem conteúdo, nulo e com valor zero) deverá ser iniciado com o caractere "|" (barra vertical) e imediatamente encerrado com o mesmo caractere "|" (barra vertical) delimitador de campo. Cada registro deve necessariamente ocupar apenas uma linha 7 Formação dos registros no arquivo. Preenchimento fixo: o campo deve ser preenchido com o Preenchimento dos tamanho exato.

campos Preenchimento variável: o campo pode ter variação de tamanho de preenchimento.

Deve ser informado com até 4 posições, representando 3 Campo numérico posições inteiras e 1 decimal; 9 referente a quantidade Os zeros não significativos não devem ser informados; de meses Os caracteres "." (ponto) e "," (vírgula) não devem ser informados. 2. Estrutura de arquivo 2.1 Estrutura completa de uma declaração de Pessoa Física

Dirf - Declaração do imposto sobre a renda retido na fonte RESPO - Responsável pelo preenchimento DECPF - Declarante pessoa física IDREC - Identificação do código de receita BPFDEC - Beneficiário pessoa física do declarante RTRT - Rendimentos tributáveis - Rendimento tributável RTPO - Rendimentos tributáveis - Dedução - Previdência oficial RTDP - Rendimentos tributáveis - Dedução - Dependentes RTDS - Rendimentos tributáveis - Dedução - Desconto simplificado mensal RTIRF - Rendimentos tributáveis - imposto sobre a renda retido na fonte CJAC - Compensação de imposto por decisão judicial - Ano-calendário CJAA - Compensação de imposto por decisão judicial - Anos anteriores ESRT - Tributação com exigibilidade suspensa - Rendimento tributável ESPO - Tributação com exigibilidade suspensa - Dedução - Previdência oficial ESDP - Tributação com exigibilidade suspensa - Dedução - Dependentes ESDS - Tributação com exigibilidade suspensa - Dedução - Desconto simplificado mensal ESIR - Tributação com exigibilidade suspensa - Imposto sobre a renda na fonte ESDJ - Tributação com exigibilidade suspensa - Depósito judicial INFPC - Informações de previdência complementar RTPP - Rendimentos tributáveis - Dedução - Previdência privada RTFA - Rendimentos tributáveis - Dedução - FAPI ESPP - Tributação com exigibilidade suspensa - Dedução - Previdência privada ESFA - Tributação com exigibilidade suspensa - Dedução - FAPI INFPA - Informações do beneficiário da pensão alimentícia RTPA - Rendimentos tributáveis - Dedução - Pensão alimentícia ESPA - Tributação com exigibilidade suspensa - Dedução - Pensão alimentícia RIDAC - Rendimentos isentos - Diária e Ajuda de custo RIIRP - Rendimentos isentos - Indenizações por rescisão de contrato de trabalho, inclusive a título de PDV RIAP - Rendimentos isentos - Abono pecuniário RIP65 - Rendimentos isentos - Parcela isenta de aposentadoria (65 anos ou mais) RIJMRE - Rendimentos isentos - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função RIO - Rendimentos isentos anuais - Outros BPJDEC - Beneficiário pessoa jurídica do declarante

RTRT - Rendimentos tributáveis - Rendimento tributável RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte RRA - Rendimentos recebidos acumuladamente IDREC - Identificação do código de receita BPFRRA - Beneficiário pessoa física do rendimento recebido acumuladamente RTRT - Rendimentos tributáveis - Rendimento tributável RTPO - Rendimentos tributáveis - Dedução - Previdência oficial RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte DAJUD - Despesa com ação judicial QTMESES - Quantidade de meses RIJMRE - Rendimentos isentos - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função INFPA - Informações do beneficiário da pensão alimentícia RTPA - Rendimentos tributáveis - Dedução - Pensão alimentícia SCP - Informações da sociedade em conta de participação BPFSCP - Beneficiário pessoa física da sociedade em conta de participação RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação BPJSCP - Beneficiário pessoa jurídica da sociedade em conta de participação RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação PSE - Plano privado de assistência à saúde - coletivo empresarial OPSE - Operadora de plano privado de assistência à saúde - coletivo empresarial TPSE - Titular de plano privado de assistência à saúde - coletivo empresarial RTPSE - Reembolso do titular do plano de assistência à saúde - coletivo empresarial DTPSE - Dependente do titular de plano privado de assistência à saúde - coletivo empresarial RDTPSE - Reembolso do dependente do titular do plano de assistência à saúde - coletivo empresarial RPDE - Rendimentos pagos a residentes ou domiciliados no exterior BRPDE - Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE - Valores de rendimentos pagos a residentes ou domiciliados no exterior INF - Informações complementares para o comprovante de rendimentos FIMDirf - Término da declaração 2.2 Estrutura completa de uma declaração de Pessoa Jurídica

Dirf - Declaração do imposto sobre a renda retido na fonte RESPO - Responsável pelo preenchimento DECPJ - Declarante pessoa jurídica IDREC - Identificação do código de receita BPFDEC - Beneficiário pessoa física do declarante RTRT - Rendimentos tributáveis - Rendimento tributável RTPO - Rendimentos tributáveis - Dedução - Previdência oficial RTDP - Rendimentos tributáveis - Dedução - Dependentes

RTDS - Rendimentos tributáveis - Dedução - Desconto simplificado mensal RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte CJAC - Compensação de imposto por decisão judicial - Ano-calendário CJAA - Compensação de imposto por decisão judicial - Anos anteriores ESRT - Tributação com exigibilidade suspensa - Rendimento tributável ESPO - Tributação com exigibilidade suspensa - Dedução - Previdência oficial ESDP - Tributação com exigibilidade suspensa - Dedução - Dependentes ESDS - Tributação com exigibilidade suspensa - Dedução - Desconto simplificado mensal ESIR - Tributação com exigibilidade suspensa - Imposto sobre a renda na fonte ESDJ - Tributação com exigibilidade suspensa - Depósito judicial INFPC - Informações de previdência complementar RTPP - Rendimentos tributáveis - Dedução - Previdência privada RTFA - Rendimentos tributáveis - Dedução - FAPI RTSP - Rendimentos tributáveis - Dedução - Fundo de previdência do servidor público RTEP - Rendimentos tributáveis - Dedução - Contribuição do ente público patrocinador ESPP - Tributação com exigibilidade suspensa - Dedução - Previdência privada ESFA - Tributação com exigibilidade suspensa - Dedução - FAPI ESSP - Tributação com exigibilidade suspensa - Dedução - Fundo de previdência do servidor público ESEP - Tributação com exigibilidade suspensa - Dedução - Contribuição do ente público patrocinador INFPA - Informações do beneficiário da pensão alimentícia RTPA - Rendimentos tributáveis - Dedução - Pensão alimentícia ESPA - Tributação com exigibilidade suspensa - Dedução - Pensão alimentícia RIDAC - Rendimentos isentos - Diária e Ajuda de custo RIIRP - Rendimentos isentos - Indenizações por rescisão de contrato de trabalho, inclusive a título de PDV RIAP - Rendimentos isentos - Abono pecuniário RIMOG - Rendimentos isentos - Pensão, aposentadoria ou reforma por moléstia grave RIP65 - Rendimentos isentos - Parcela isenta de aposentadoria (65 anos ou mais) RIBMR - Rendimentos isentos - Bolsa de estudo recebida por médico-residente RICAP - Rendimentos isentos - Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIRPC - Rendimentos isentos - Resgate de previdência complementar por portador de moléstia grave RIL96 - Rendimentos isentos anuais - Lucros e dividendos pagos a partir de 1996 RIPTS - Rendimentos isentos anuais - Valores pagos a titular ou sócio ou empresa de pequeno porte, exceto pró-labore e aluguéis RIJMRE - Rendimentos isentos - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função RIO - Rendimentos isentos anuais - Outros BPJDEC - Beneficiário pessoa jurídica do declarante

RTRT - Rendimentos tributáveis - Rendimento tributável RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte VPEIM - Valores pagos às entidades imunes ou isentas - IN RFB 1.234/2012 RIMUN - Rendimentos imunes - art. 4º, inciso III RISEN - Rendimentos isentos - art. 4º, inciso IV FCI - Fundo ou clube de investimento IDREC - Identificação do código de receita BPFFCI - Beneficiário pessoa física do fundo ou clube de investimento RTRT - Rendimentos tributáveis - Rendimento tributável RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte CJAC - Compensação de imposto por decisão judicial - Ano-calendário CJAA - Compensação de imposto por decisão judicial - Anos Anteriores ESRT - Tributação com exigibilidade suspensa - Rendimento tributável ESIR - Tributação com exigibilidade suspensa - Imposto sobre a renda na fonte ESDJ - Tributação com exigibilidade suspensa - Depósito judicial RIP65 - Rendimentos isentos - Parcela isenta de aposentadoria (65 anos ou mais) RIMOG - Rendimentos isentos - Pensão, aposentadoria ou reforma por moléstia grave RICAP - Rendimentos isentos - Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIO - Rendimentos isentos anuais - Outros BPJFCI - Beneficiário pessoa jurídica do fundo ou clube de investimento RTRT - Rendimentos tributáveis - Rendimento tributável RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte PROC - Processo da justiça do trabalho/federal/estadual/Distrito Federal IDREC - Identificação do código de receita BPFPROC - Beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT - Rendimentos tributáveis - Rendimento tributável RTPO - Rendimentos tributáveis - Dedução - Previdência oficial RTDP - Rendimentos tributáveis - Dedução - Dependentes RTDS - Rendimentos tributáveis - Dedução - Desconto simplificado mensal RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte CJAC - Compensação de imposto por decisão judicial - Ano-calendário CJAA - Compensação de imposto por decisão judicial - Anos Anteriores ESRT - Tributação com exigibilidade suspensa - Rendimento tributável ESPO - Tributação com exigibilidade suspensa - Dedução - Previdência oficial ESDP - Tributação com exigibilidade suspensa - Dedução - Dependentes ESDS - Tributação com exigibilidade suspensa - Dedução - Desconto simplificado mensal ESIR - Tributação com exigibilidade suspensa - Imposto sobre a renda na fonte ESDJ - Tributação com exigibilidade suspensa - Depósito judicial RTPP - Rendimentos tributáveis - Dedução - Previdência privada

RTFA - Rendimentos tributáveis - Dedução - FAPI RTSP - Rendimentos tributáveis - Dedução - Fundo de previdência do servidor público ESPP - Tributação com exigibilidade suspensa - Dedução - Previdência privada ESFA - Tributação com exigibilidade suspensa - Dedução - FAPI ESSP - Tributação com exigibilidade suspensa - Dedução - Fundo de previdência do servidor público RTPA - Rendimentos tributáveis - Dedução - Pensão alimentícia ESPA - Tributação com exigibilidade suspensa - Dedução - Pensão alimentícia RIMOG - Rendimentos isentos - Pensão, aposentadoria ou reforma por moléstia grave RIJMRE - Rendimentos isentos- Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função RIRSR - Rendimentos pagos sem retenção do IR na fonte - Lei nº 10.833/2003 BPJPROC - Beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT - Rendimentos tributáveis - Rendimento tributável RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte RIRSR - Rendimentos pagos sem retenção do IR na fonte - Lei nº 10.833/2003 RRA - Rendimentos recebidos acumuladamente IDREC - Identificação do código de receita BPFRRA - Beneficiário pessoa física do rendimento recebido acumuladamente RTRT - Rendimentos tributáveis - Rendimento tributável RTPO - Rendimentos tributáveis - Dedução - Previdência oficial INFPA - Informações do beneficiário da pensão alimentícia RTPA - Rendimentos tributáveis - Dedução - Pensão alimentícia RTIRF - Rendimentos tributáveis - Imposto sobre a renda retido na fonte RIMOG - Rendimentos isentos - Pensão, aposentadoria ou reforma por moléstia grave RIP65 - Rendimentos isentos - Parcela isenta de aposentadoria (65 anos ou mais) RIJMRE - Rendimentos isentos - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função DAJUD - Despesa com ação judicial QTMESES - Quantidade de meses SCP - Informações da sociedade em conta de participação BPFSCP - Beneficiário pessoa física da sociedade em conta de participação RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação BPJSCP - Beneficiário pessoa jurídica da sociedade em conta de participação RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação PSE - Plano privado de assistência à saúde - coletivo empresarial OPSE - Operadora de plano privado de assistência à saúde - coletivo empresarial TPSE - Titular de plano privado de assistência à saúde - coletivo empresarial RTPSE - Reembolso do titular do plano de assistência à saúde - coletivo empresarial

DTPSE - Dependente do titular de plano privado de assistência à saúde - coletivo empresarial RDTPSE - Reembolso do dependente do titular do plano de assistência à saúde - coletivo empresarial RPDE - Rendimentos pagos a residentes ou domiciliados no exterior BRPDE - Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE - Valores de rendimentos pagos a residentes ou domiciliados no exterior INF - Informações complementares para o comprovante de rendimentos FIMDirf - Término da declaração 3. Leiaute do arquivo 3.1 Registro de identificação da declaração (identificador Dirf)

- Registro obrigatório no arquivo; - Deve ser o primeiro registro no arquivo; - Ocorre somente uma vez no arquivo.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 4 Dirf Sim 2 Ano referência N Fixo 4 2024 Sim 2023 ou 3 Ano-calendário N Fixo 4 Sim 2024 S- Indicador de 4 C Fixo 1 Retificadora Sim retificadora N - Original 5 Número do recibo N Fixo 12 - Não

6 C Fixo 7 B3VH8RQ Sim estrutura do leiaute

Observações: Ordem Campo Descrição Número do O preenchimento será obrigatório se o campo de ordem 4 igual a "S" e

recibo declaração transmitida sem o uso de certificação digital. 3.2 Registro do Responsável pelo preenchimento da declaração (identificador RESPO)

- Registro obrigatório no arquivo; - Deve ser o segundo registro no arquivo; - Ocorre somente uma vez no arquivo.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 5 RESPO Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim 4 DDD N Fixo 2 - Sim 5 Telefone N Variável 9 - Sim 6 Ramal N Variável 6 - Não 7 Fax N Variável 9 - Não 8 Correio eletrônico C Variável 50 - Não Observações: Ordem Campo Descrição 4 DDD O primeiro algarismo deve ser diferente de zero. 5 Telefone Deve ser preenchido com oito ou nove algarismos. 7 Fax Deve ser preenchido com oito ou nove algarismos. 3.3 Registro de identificação do declarante pessoa física (identificador DECPF)

- Registro obrigatório no arquivo para declarante pessoa física; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPJ.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 5 DECPF Sim

2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Indicador de declarante de S - Pagou rendimentos rendimentos a 4 pagos a C Fixo 1 residentes ou Sim residentes ou domiciliados no domiciliados no exterior exterior N - Não pagou rendimentos a residentes ou domiciliados no exterior S - Titular de Indicador de serviços notariais e Titular de de registros 5 Serviços C Fixo 1 Sim N - Não é titular de Notariais e de serviços notariais e Registros de registros Indicador de S - Existe plano privado pagamento de valor 6 de assistência à C Fixo 1 pelo Sim saúde - coletivo titular/dependente empresarial do plano de saúde N - Não existe pagamento de valor

pelo titular/dependente do plano de saúde Indicador de sócio ostensivo responsável por S - Sócio ostensivo 7 sociedade em C Fixo 1 N - Não é sócio Sim conta de ostensivo participação - SCP S - Encerramento de espólio/saída Indicador de definitiva do país situação 8 C Fixo 1 N - Não é Sim especial da encerramento de declaração espólio/saída definitiva do país 9 Data do Evento D Fixo 8 - Não 1 - Encerramento de espólio 10 Tipo de Evento N Fixo 1 Não 2 - Saída definitiva do Brasil S - Declarante Indicador de falecido 11 declarante C Fixo 1 Sim N - Declarante não falecido falecido 12 Data do óbito D Fixo 8 - Não 0 - Sem espólio Situação do 13 N Fixo 1 1 - Espólio não Não espólio encerrado CPF do 14 N Fixo 11 - Não inventariante Nome do 15 C Variável 60 - Não inventariante

Observações: Ordem Campo Descrição O preenchimento será obrigatório se o campo de ordem 8 igual a 9 Data do Evento "S". O preenchimento será obrigatório se o campo de ordem 8 igual a 10 Tipo de Evento "S". Indicador de Deve ser preenchido com "S" se o campo de ordem 8 igual a "S" e 11 declarante campo de ordem 10 igual a 1 falecido Permitido somente para as declarações normais Situação do 13 Para o encerramento de espólio a declaração será sempre de espólio situação especial; Declarante falecido - indicador igual a SIM Situação 1 - sem espólio - Apresentar declaração normal do ano-calendário; - Informar data do óbito e situação do espólio igual a 0;

Observação: não serão aceitas declarações para anos posteriores ao ano da data do óbito sem espólio; Situação 2 - com espólio não encerrado - Apresentar declaração normal do ano-calendário; - Informar data do óbito e situação do espólio igual a 1; Observação: serão aceitas declarações para anos posteriores ao ano da data do óbito até que seja apresentada uma declaração de situação especial - encerramento de espólio; Situação 3 - encerramento de espólio - Apresentar declaração de situação especial do ano-calendário; Observação: os campos 12 a 15 não serão preenchidos; 3.4 Registro de identificação do declarante pessoa jurídica (identificador DECPJ)

- Registro obrigatório no arquivo para declarante pessoa jurídica; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPF.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 5 DECPJ Sim

2 CNPJ N Fixo 14 - Sim Nome 3 C Variável 150 - Sim empresarial Natureza do 0 - Pessoa jurídica 4 N Fixo 1 Sim declarante de direito privado 1 - Órgãos, autarquias e fundações da administração pública federal 2 - Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal 3 - Empresa pública ou sociedade de economia mista federal 4 - Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal 8 - Entidade com alteração de

natureza jurídica (uso restrito) CPF responsável 5 N Fixo 11 - Sim perante o CNPJ Indicador de sócio ostensivo responsável por S - Sócio ostensivo 6 sociedade em C Fixo 1 N - Não é sócio Sim conta de ostensivo participação - SCP S - Depositário de Indicador de crédito decorrente declarante de decisão judicial depositário de 7 C Fixo 1 N - Não é Sim crédito depositário de decorrente de crédito decorrente decisão judicial de decisão judicial Indicador de declarante de instituição S - Instituição administradora administradora ou 8 ou C Fixo 1 intermediadora de Sim intermediadora fundo ou clube de de fundo ou investimento clube de investimento N - Não é instituição administradora ou intermediadora de fundo ou clube de investimento Indicador de declarante de S - Pagou rendimentos rendimentos a 9 pagos a C Fixo 1 residentes ou Sim residentes ou domiciliados no domiciliados no exterior exterior N - Não pagou rendimentos a residentes ou domiciliados no exterior Indicador de S - Existe plano privado de pagamento de valor 10 assistência à C Fixo 1 pelo Sim saúde - coletivo titular/dependente empresarial do plano de saúde N - Não existe pagamento de valor pelo titular/dependente do plano de saúde

Indicador de entidade em que a União detém S - Existe maioria do pagamento de 11 C Fixo 1 Sim capital social valores a entidades sujeito a voto, imunes/isentas recebe recursos do Tesouro Nacional e está obrigada a registrar a N - Não existe execução pagamento de orçamentária no valores a entidades Siafi (IN imunes/isentas 1.234/2012, art. 4º, incisos III e IV) Indicador de S - Fundação fundação pública pública de direito de direito privado privado 12 instituída pela C Fixo 1 Sim N - Não é fundação União, Estados, pública de direito Municípios ou privado Distrito Federal S - Declaração de Indicador de situação especial 13 situação especial C Fixo 1 N - Não é Sim da declaração declaração de situação especial 14 Data do evento D Fixo 8 - Não

Observações: Ordem Campo Descrição Relativamente à natureza do declarante 8 - Entidade com 4 Natureza do declarante alteração de natureza jurídica (uso restrito), esclarecemos: 1. Para declarante que alterou sua natureza jurídica em relação ao ano-calendário e que implique em mudança da natureza do declarante na ficha Informações da Dirf; 2. Para declarante que mudou sua natureza jurídica de órgão público para privado, ou vice-versa. Aplica-se ainda para mudanças entre as esferas governamentais da federação. Por exemplo: órgão público ou pessoa jurídica de direito privado estadual ou municipal que passou a ser federal, ou vice-versa; 3. A declaração deverá ser entregue na RFB. Indicador de entidade em que a União detém maioria Indicador com a opção "Sim" permitido somente se 11 do capital social sujeito a campo de ordem 4 - Natureza do declarante, igual a "0", voto, recebe recursos do "1", "3" ou "8" Tesouro Nacional e está obrigada a registrar a execução orçamentária no Siafi (IN

1.234/2012, art. 4º, incisos III e IV) Indicador de fundação Indicador com a opção "S" permitido somente se campo pública de direito privado de ordem 4 - Natureza do declarante, igual a "1", "2" ou 12 instituída pela União, "8" Estados, Municípios ou Para as demais naturezas do declarante deve ser igual a Distrito Federal "N" O preenchimento será obrigatório se o campo de ordem 14 Data do evento 13 igual a "S". 3.5 Registro de identificação do código de receita (identificador IDREC)

- Deve ser apresentado com os códigos de receita em ordem crescente; - Deve estar associado aos registros do tipo DECPF, DECPJ, FCI, PROC ou RRA.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório Identificador 1 C Fixo 5 IDREC Sim de registro De acordo com a tabela de códigos de Código de 2 N Fixo 4 receitas constante na Sim receita IN que dispõe sobre a Dirf 3.6 Registro de beneficiário pessoa física do declarante (identificador BPFDEC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 6 BPFDEC Sim

2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Data atribuída 4 pelo laudo da D Fixo 8 - Não moléstia grave S - Existem Indicador de informações 5 identificação do C Fixo 1 Sim detalhadas do alimentando alimentando N - Não existem informações detalhadas do alimentando Indicador de S - Existem identificação da 6 C Fixo 1 informações Sim previdência detalhadas da complementar

previdência complementar N - Não existem informações detalhadas da previdência complementar

Observações: Ordem Campo Descrição Indicador de Se campo igual a "S" - deverá constar o registro INFPA 5 identificação do seguido do registro de valor (RTPA e/ou ESPA) para cada alimentando alimentando. Se campo igual a "N" - não apresentar o registro INFPA; deverão constar os registros de valores (RTPA e/ou ESPA) com o valor total de pensão alimentícia pago a todos os alimentandos do beneficiário. - As informações detalhadas a que se refere o campo são: CPF, data de nascimento, nome e relação de dependência do alimentando (registro INFPA). Indicador de Se campo igual a "S" - deverá constar o registro INFPC identificação da seguido do registro de valor (RTPP, RTFA, RTSP e/ou ESPP,

previdência ESFA, ESSP) para cada entidade de previdência complementar complementar do beneficiário. Se campo igual a "N" - não apresentar o registro INFPC; deverão constar apenas os registros de valores mensais (RTPP, RTFA, RTSP e/ou ESPP, ESFA, ESSP) com o total dos valores de previdência complementar pagos pelo beneficiário. - As informações detalhadas a que se refere o campo são: CNPJ e Nome empresarial da entidade de previdência complementar (registro INFPC). 3.7 Registro de beneficiário pessoa jurídica do declarante (identificador BPJDEC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 6 BPJDEC Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.8 Registro de valores pagos às entidades imunes e isentas (identificador VPEIM)

- Serão apresentados todos os CNPJ em ordem crescente;

- Registro permitido somente para declarante pessoa jurídica; e se campo 12 do registro DECPJ igual a "S";

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 5 VPEIM Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.9 Registro de identificação do fundo ou clube de investimento (identificador FCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Deve estar associado ao registro do tipo DECPJ.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 3 FCI Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.10 Registro do beneficiário pessoa física do fundo ou clube de investimento (identificador BPFFCI)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 6 BPFFCI Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Data atribuída pelo laudo 4 D Fixo 8 - Não da moléstia grave 3.11 Registro do beneficiário pessoa jurídica do fundo ou clube de investimento (identificador BPJFCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 6 BPJFCI Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.12 Registro de processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador PROC)

- Deve estar classificado em ordem crescente por: - Tipo de justiça; - Número do processo; - Deve estar associado ao registro do tipo DECPJ.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 4 PROC Sim

1 - Justiça federal 2 - Justiça do 2 Indicador de Justiça N Fixo 1 trabalho Sim 3 - Justiça estadual/Distrito Federal Número do 3 C Variável 20 - Sim processo Indicador de tipo de 1 - Pessoa física 4 advogado/escritório N Fixo 1 2 - Pessoa Não de advocacia jurídica CPF com 11 CPF do advogado/ dígitos 5 CNPJ do escritório N Variável 14 Não CNPJ com 14 de advocacia dígitos Nome da pessoa física até Nome do advogado/ 60 posições Nome empresarial Nome 6 C Variável 150 Não do escritório de empresarial da advocacia pessoa jurídica até 150 posições Valor pago para o Valor pago para 7 N Variável 13 Não advogado o advogado 3.13 Registro de beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPFPROC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 7 BPFPROC Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Data atribuída pelo 4 D Fixo 8 - Não laudo da moléstia grave 3.14 Registro de beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPJPROC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 7 BPJPROC Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.15 Registro de rendimentos recebidos acumuladamente (identificador RRA)

- Deve estar classificado em ordem crescente por: - Identificador de rendimento recebido acumuladamente; - Número do processo/requerimento.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 3 RRA Sim 1 - Pago Identificador de pelo 2 rendimento recebido N Fixo 1 declarante Sim acumuladamente 2 - Pago pela justiça Número do 3 C Variável 20 - Não processo/requerimento 1 - Pessoa Indicador de tipo de física 4 advogado/escritório de N Fixo 1 Não 2 - Pessoa advocacia jurídica CPF com 11 CPF do dígitos 5 advogado/CNPJ do N Variável 14 Não CNPJ com escritório de advocacia 14 dígitos Nome do Nome da 6 C Variável 150 Não advogado/Nome pessoa física

empresarial do com até 60 escritório de advocacia posições Nome empresarial da pessoa jurídica com até 150 posições Valor pago Valor pago para o 7 N Variável 13 para o Não advogado advogado

Observações: Ordem Campo Descrição Número do O preenchimento será obrigatório se o campo de

processo/requerimento ordem 2 igual a 2. 3.16 Registro de beneficiário pessoa física dos rendimentos recebidos acumuladamente (identificador BPFRRA)

- Deve estar classificado em ordem crescente por: - CPF; - Natureza do RRA; - Deve estar associado ao registro do tipo IDREC.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 6 BPFRRA Sim

2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Natureza do RRA C Variável 50 - Não Data atribuída 5 pelo laudo da D Fixo 8 - Não moléstia grave S - Existem Indicador de informações 6 identificação do C Fixo 1 Sim detalhadas do alimentando alimentando N - Não existem informações detalhadas do alimentando

Observações: Ordem Campo Descrição Indicador de 1. O campo só poderá ser igual a "S" se o campo 2 do registro 6 identificação do RRA igual a "1" (Pago pelo declarante); alimentando 2. Se campo igual a "S" - deverá constar o registro INFPA e RTPA para cada alimentando;

3. Se campo igual a "N" - não apresentar o registro INFPA; deverá constar o registro RTPA com o valor de pensão alimentícia pago a todos os alimentandos do beneficiário; 4. As informações detalhadas a que se refere o campo são: CPF, Data de nascimento e Nome do alimentando (registro INFPA). 3.17 Registro de identificação de Previdência Complementar (identificador INFPC)

- Registro permitido somente se campo 6 do registro BPFDEC (Indicador de identificação da previdência complementar) igual a "S"; - Serão apresentados todos os CNPJ em ordem crescente; - Deve estar associado ao registro do tipo BPFDEC; - Deve constar um registro INFPC para cada CNPJ de entidade de previdência complementar.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 5 INFPC Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.18 Registro de informações do beneficiário da pensão alimentícia (identificador INFPA)

- Registro permitido somente se Indicador de identificação do alimentando igual a "S" (BPFDEC, campo 5; e BPFRRA, campo 6); - Registro INFPA associado ao BPFRRA será permitido somente quando o identificador de rendimento recebido acumuladamente igual a "1 - Pago pelo declarante" (campo 2 do registro RRA); - Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo BPFDEC, BPFRRA.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 5 INFPA Sim

CPF do 2 N Fixo 11 - Não alimentando Data de 3 D Fixo 8 - Não nascimento 4 Nome C Variável 60 - Sim 03 - Cônjuge/ Companheiro (a) 04 - Filho (a) Relação de 5 N Fixo 2 06 - Enteado (a) Não dependência 08 - Pai/Mãe 10 - Agregado/Outros

Observações:

Ordem Campo Descrição CPF do Preenchimento obrigatório para maiores de 18 anos completos até 31

alimentando de dezembro do ano-calendário da declaração. Preenchimento obrigatório para menores de 18 anos completos até Data de 3 31 de dezembro do ano-calendário da declaração, que não tenham nascimento informado o CPF. 3.19 Registro de valores mensais (identificadores RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTDS, RTIRF, CJAA, CJAC, ESRT, ESPO, ESPP, ESFA, ESSP, ESEP, ESDP, ESPA, ESDS, ESIR, ESDJ, RIP65, RIDAC, RIIRP, RIAP, RIMOG, RIRPC, RIBMR, RICAP, RIJMRE, RISCP, RIMUN, RISEN e DAJUD)

- Deve ocorrer apenas se houver pelo menos um dos valores referentes aos meses ou 13º salário; - Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC, BPJDEC, BPFFCI, BPJFCI, BPFPROC, BPJPROC, BPFRRA, BPFSCP, BPJSCP, INFPC, INFPA, VPEIM.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos RTRT RTPO

1 C Variável 5 RTPP Sim

RTFA RTSP RTEP RTDP RTPA RTDS RTIRF CJAC CJAA ESRT ESPO ESPP ESFA ESSP ESEP ESDP ESPA ESDS ESIR ESDJ RIP65 RIDAC RIIRP RIAP RIMOG RIRPC RIBMR RICAP RIJMRE RISCP

RIMUN RISEN DAJUD 2 Janeiro N Variável 13 - Não 3 Fevereiro N Variável 13 - Não 4 Março N Variável 13 - Não 5 Abril N Variável 13 - Não 6 Maio N Variável 13 - Não 7 Junho N Variável 13 - Não 8 Julho N Variável 13 - Não 9 Agosto N Variável 13 - Não 10 Setembro N Variável 13 - Não 11 Outubro N Variável 13 - Não 12 Novembro N Variável 13 - Não 13 Dezembro N Variável 13 - Não 14 Décimo Terceiro N Variável 13 - Não 3.20 Registro de valores anuais isentos/não tributáveis/sem retenção (identificadores RIL96, RIPTS,e RIRSR)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC (RIL96, RIPTS), BPFPROC/BPJPROC (RIRSR); - Registro RIRSR permitido somente se "indicador de justiça" do registro PROC igual a 1 (Justiça Federal).

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos RIL96

1 C Variável 6 RIPTS Sim

RIRSR 2 Valor pago no ano N Variável 13 - Sim 3.21 Registro de valores anuais de rendimentos isentos - outros (identificador RIO)

- Ocorrerá apenas um registro para cada beneficiário; - Deve estar associado ao registro do tipo BPFDEC ou BPFFCI.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 3 RIO Sim 2 Valor pago no ano N Variável 13 - Sim Descrição dos 3 rendimentos isentos - C Variável 60 - Sim outros 3.22 Registro de quantidade de meses (identificador QTMESES)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado ao registro do tipo BPFRRA.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 7 QTMESES Sim Quantidade meses - 2 N Variável 4 - Não janeiro Quantidade meses - 3 N Variável 4 - Não fevereiro Quantidade meses - 4 N Variável 4 - Não março Quantidade meses - 5 N Variável 4 - Não abril Quantidade meses - 6 N Variável 4 - Não maio Quantidade meses - 7 N Variável 4 - Não junho Quantidade meses - 8 N Variável 4 - Não julho Quantidade meses - 9 N Variável 4 - Não agosto Quantidade meses - 10 N Variável 4 - Não setembro Quantidade meses - 11 N Variável 4 - Não outubro Quantidade meses - 12 N Variável 4 - Não novembro Quantidade meses - 13 N Variável 4 - Não dezembro 3.23 Registro de informações da Sociedade em Conta de Participação (identificador SCP)

- Serão apresentados em ordem crescente de CNPJ. - Deve constar um registro para cada CNPJ de Sociedade em conta de participação

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 3 SCP Sim CNPJ da Sociedade em 2 N Fixo 14 - Sim Conta de Participação Nome empresarial da 3 Sociedade em Conta de C Variável 150 - Sim Participação 3.24 Registro de beneficiário pessoa física da sociedade em conta de participação (identificador BPFSCP)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJSCP, caso exista o registro; - Deve estar associado a um registro do tipo SCP.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 6 BPFSCP Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Percentual de 4 N Variável 4 - Não participação na SCP 3.25 Registro de beneficiário pessoa jurídica da sociedade em conta de participação (identificador BPJSCP)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFSCP, caso exista o registro; - Deve estar associado a um registro do tipo SCP.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 6 BPJSCP Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim Percentual de 4 C Variável 4 - Não participação na SCP 3.26 Registro de pagamentos a plano privado de assistência à saúde - coletivo empresarial (identificador PSE)

- Ocorre somente uma vez no arquivo, caso exista informação de valores pagos pelo titular/dependente do plano de assistência à saúde.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 3 PSE Sim

3.27 Registro de operadora do plano privado de assistência à saúde - coletivo empresarial (identificador OPSE)

- Ocorre caso exista o registro PSE; - Serão apresentados todos os CNPJ em ordem crescente.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 4 OPSE Sim CNPJ da operadora de plano privado de 2 N Fixo 14 - Sim assistência à saúde - coletivo empresarial 3 Nome empresarial C Variável 150 - Sim 4 Registro ANS N Fixo 6 - Não 3.28 Registro de titular do plano privado de assistência à saúde - coletivo empresarial (identificador TPSE)

- Serão apresentados todos os CPF em ordem crescente. - Deve estar associado ao registro do tipo OPSE.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 4 TPSE Sim

2 CPF do titular N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Valor pago no ano N Variável 9 - Sim

Observações: Ordem Campo Descrição Valor pago no Preenchimento obrigatório se o titular não possuir dependente

ano cadastrado e nem reembolso informado. 3.29 Registro de informação de reembolso do titular do plano de saúde - coletivo empresarial (identificador RTPSE)

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo TPSE; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos- calendário anteriores.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 5 RTPSE Sim

CPF com 11 CPF/CNPJ do dígitos 2 prestador de N Variável 14 Sim CNPJ com 14 serviço dígitos Nome/Nome Nome da pessoa empresarial do 3 C Variável 150 física até 60 Sim prestador de posições serviço

Nome empresarial da pessoa jurídica até 150 posições Valor do 4 reembolso do N Variável 9 - Não ano-calendário Valor do 5 reembolso de N Variável 9 - Não anos anteriores

Observações: Ordem Campo Descrição Valor do reembolso do Valores reembolsados no ano-calendário, referentes a

ano-calendário pagamentos de serviços prestados no ano-calendário. Valor do reembolso de Valores reembolsados no ano-calendário referentes a

anos anteriores pagamentos de serviços prestados em anos anteriores. 3.30 Registro de dependente do plano privado de assistência à saúde - coletivo empresarial (identificador DTPSE)

- Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo TPSE.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 5 DTPSE Sim

CPF do 2 N Fixo 11 - Não dependente Data de 3 D Fixo 8 - Não nascimento 4 Nome C Variável 60 - Sim 03 - Cônjuge/ Companheiro(a) 04 - Filho(a) Relação de 5 N Fixo 2 06 - Enteado(a) Não dependência 08 - Pai/Mãe 10 - Agregado/ Outros Valor pago no 6 N Variável 9 - Sim ano

Observações: Ordem Campo Descrição CPF do Preenchimento obrigatório para maiores de 18 anos completos até 31

dependente de dezembro do ano-calendário da declaração. Preenchimento obrigatório para menores de 18 anos completos até 31 Data de 3 de dezembro do ano-calendário da declaração, que não tenham nascimento informado o CPF. Valor pago no Preenchimento obrigatório se o dependente não possuir reembolso

ano informado.

3.31 - Registro de informação de reembolso do dependente (identificador RDTPSE):

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo DTPSE; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos- calendário anteriores.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 6 RDTPSE Sim

CPF com 11 CPF/CNPJ do dígitos 2 prestador de N Variável 14 Sim CNPJ com 14 serviço dígitos Nome da pessoa Nome/Nome física até 60 Empresarial do posições 3 C Variável 150 Sim prestador de Nome empresarial serviço da pessoa jurídica até 150 posições Valor do 4 reembolso do N Variável 9 - Não ano-calendário Valor do 5 reembolso de N Variável 9 - Não anos anteriores

Observações: Ordem Campo Descrição Valor do reembolso do Valores reembolsados no ano-calendário, referentes a

ano-calendário pagamentos de serviços prestados no ano-calendário Valor do reembolso de Valores reembolsados no ano-calendário referentes a

anos anteriores pagamentos de serviços prestados em anos anteriores 3.32 Registro de rendimentos pagos a residentes ou domiciliados no exterior (identificador RPDE)

- Ocorre somente uma vez no arquivo, caso exista informação de rendimentos pagos a residentes ou domiciliados no exterior

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 4 RPDE Sim

3.33 Registro de beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior (identificador BRPDE)

- Deve estar classificado em ordem crescente por: - Beneficiário; - Código de país; - Número de identificação fiscal - NIF; - Deve estar associado ao registro do tipo RPDE.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório

1 C Fixo 5 BRPDE Sim

1 - Pessoa física 2 Beneficiário N Fixo 1 2 - Pessoa Sim jurídica De acordo com a tabela de código dos países 3 Código de país N Variável 3 Sim constante na IN que dispõe sobre a Dirf Número de 4 identificação fiscal - C Variável 30 - Não NIF S - Dispensado do Número de Indicador de identificação beneficiário fiscal - NIF dispensado do 5 C Fixo 1 N - Não é Sim Número de dispensado do Identificação Fiscal Número de - NIF identificação fiscal - NIF S - Dispensado do Número de Indicador de que o identificação país não exige fiscal - NIF 6 Número de C Fixo 1 N - Não é Sim Identificação Fiscal dispensado do - NIF Número de identificação fiscal - NIF CPF com 11 dígitos 7 CPF/CNPJ N Variável 14 Não CNPJ com 14 dígitos Nome/Nome 8 C Variável 150 - Sim empresarial De acordo com a tabela de Relação fonte informações pagadora pessoa sobre os 9 jurídica e N Fixo 3 beneficiários dos Não beneficiário pessoa rendimentos jurídica constante na IN que dispõe sobre a Dirf

10 Logradouro C Variável 60 - Não 11 Número C Variável 6 - Não 12 Complemento C Variável 25 - Não 13 Bairro/Distrito C Variável 20 - Não 14 Código postal N Variável 10 - Não 15 Cidade C Variável 40 - Não 16 Estado/Província C Variável 40 - Não 17 Telefone N Variável 15 - Não

Observações: Ordem Campo Descrição Relação fonte pagadora pessoa jurídica Preenchimento obrigatório se campo de

e beneficiário pessoa jurídica ordem 2 (Beneficiário) igual a 2. 3.34 Registro de valores de rendimentos pagos a residentes ou domiciliados no exterior (identificador VRPDE)

- Deve estar classificado em ordem crescente por: - Data do pagamento; - Código de receita; - Deve estar associado ao registro do tipo BRPDE.

Ordem Campo Formato Preenchimento Tamanho Valores válidos Obrigatório Identificador 1 C Fixo 5 VRPDE Sim de registro Data do 2 D Fixo 8 - Sim pagamento Código de 3 N Fixo 4 - Sim receita De acordo com a tabela de informações sobre Tipo de 4 N Fixo 3 os rendimentos Sim rendimento constante na IN que dispõe sobre a Dirf Rendimento 5 N Variável 13 - Sim pago Imposto 6 N Variável 13 - Não retido De acordo com a tabela de informações sobre a Forma de 7 N Fixo 2 forma de tributação Sim tributação constante na IN que dispõe sobre a Dirf 3.35 Registro de informações complementares para o comprovante de rendimento (identificador INF)

- Serão apresentados todos os CPF em ordem crescente;

- Deve haver um registro BPFDEC, BPFPROC e/ou BPFRRA correspondente na declaração; - Deve ocorrer apenas um registro para cada beneficiário.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos 1 Identificador de registro C Fixo 3 INF Sim 2 CPF N Fixo 11 - Sim Informações 3 C Variável 500 - Sim complementares 3.36 Registro identificador do término da declaração (identificador FIMDirf)

- Registro obrigatório no arquivo; - Deve ser o último registro no arquivo; - Ocorre somente uma vez no arquivo.

Valores Ordem Campo Formato Preenchimento Tamanho Obrigatório válidos

1 C Fixo 7 FIMDirf Sim

