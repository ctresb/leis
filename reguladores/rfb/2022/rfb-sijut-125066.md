---
titulo: "Ato Declaratório Executivo Cofis nº 72, de 14 de julho de 2022"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "72"
data: "2022-07-14"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 20/07/2022, seção 1, página 79"
data_publicacao: "2022-07-20"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/125066/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/125066/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "125066"
sha256_texto: "3afe188a977b262dc796950572e9b1d508fe1ca28154e3f68d37f8f12ab1f96a"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Cofis nº 72, de 14 de julho de 2022

Aprova a versão 1.3 do Programa Gerador da Declaração do Imposto sobre a Renda Retido na Fonte relativa a fatos geradores ocorridos no ano-calendário de 2021, nos casos de situação normal, e no ano-calendário de 2022, nos casos de situação especial (PGD Dirf 2022).

O COORDENADOR-GERAL DE FISCALIZAÇÃO, no uso das atribuições que lhe conferem os incisos I e II do art. 121 e inciso II do art. 358 do Regimento Interno da Secretaria Especial da Receita Federal do Brasil, aprovado pela Portaria ME nº 284, de 27 de julho de 2020, e tendo em vista o disposto na Instrução Normativa RFB nº 1.990, de 18 de novembro de 2020,

DECLARA:

**Art.1º** Fica aprovada a versão 1.3 do Programa Gerador da Declaração do Imposto sobre a Renda Retido na Fonte relativa a fatos geradores ocorridos no ano-calendário de 2021, nos casos de situação normal, e no ano-calendário de 2022, nos casos de situação especial (Dirf 2022), cuja estrutura passa a contemplar as seguintes alterações:

I - Inclusão do registro de rendimento isento anual relativo aos Juros de Mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função, aplicável aos códigos de receita 1889, 1895, 5928 e 5936 informados para beneficiário pessoa física;

II - Inclusão do registro de rendimento isento mensal relativo ao Resgate de Previdência Complementar por portador de moléstia grave, aplicável aos códigos de receita 3223, 3556 e 3579 informados para beneficiário pessoa física;

III - Atualização do modelo de comprovante de rendimentos pagos e de Imposto sobre a Renda Retido na Fonte (IRRF), com base nas alterações trazidas pela Instrução Normativa RFB nº 2060, de 13 de dezembro de 2021.

**Art. 2º** A importação de dados pelo Programa a que se refere o art. 1º deve ser efetuada em observância ao leiaute aplicável aos campos e registros da Dirf 2022, que passa a vigorar conforme a estrutura de arquivo constante do Anexo único deste Ato Declaratório.

**Art.3º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

PAULO EDUARDO NUNES VERÇOSA

## ANEXO

Anexo&nbsp;

ANEXO LEIAUTE DO ARQUIVO

Declaração do Imposto sobre a Renda Retido na Fonte - Dirf

1. Regras gerais

Estas regras devem ser respeitadas em todos os arquivos gerados, quando não excepcionadas por regra específica referente a um dado registro e explicitada em suas observações.

Nº Regra de preenchimento Descrição ALFANUMÉRICO (C): representados por "C" - todos os caracteres, excetuados o caractere "|" (pipe ou barra vertical). 1 Formato dos campos NUMÉRICO (N): representados por "N" - pode conter apenas os valores de zero a nove. Campos numéricos (D) Devem ser informados conforme o padrão ano, mês e dia 2 cujo conteúdo representa (AAAAMMDD), excluindo-se quaisquer caracteres de separação (tais data como ".", "/", "-", etc.); Os campos numéricos com número de inscrição (CNPJ e CPF) ou Campos numéricos com códigos de receita deverão ser informados com todos os dígitos, 3 número de inscrição ou inclusive os zeros à esquerda; códigos de receita As máscaras (caracteres especiais de formatação, tais como ".", "/", "-", etc.) não devem ser informadas. Devem ser informados com até 13 posições, representando 11 posições inteiras e 2 decimais; Campos numéricos 4 Os zeros não significativos não devem ser informados; referentes a valores Os caracteres .(ponto) e ,(vírgula) não devem ser informados; Todos os valores monetários devem estar expressos em reais. Os campos com conteúdo alfanumérico nos quais se faz necessário registrar números ou códigos de identificação (Exemplo: Número de Campos alfanuméricos Identificação Fiscal - N IF) deverão seguir a regra de formação e 5 com números ou códigos tamanho definidos pelo respectivo órgão regulador; de identificação As máscaras (caracteres especiais de formatação, tais como ".", "/", "-", etc.) não devem ser informadas. Ao final de cada campo (inclusive o último de cada registro) deve ser 6 Formação dos campos inserido o caractere delimitador "|" (pipe ou barra vertical: caractere 124 da Tabela ASCII); O caractere delimitador "|" (barra vertical) não deve ser incluído como parte integrante do conteúdo de quaisquer campos numéricos, datas ou alfanuméricos; Na ausência de informação, o campo vazio (campo sem conteúdo, nulo e com valor zero) deverá ser iniciado com o caractere "|" (barra vertical) e imediatamente encerrado com o mesmo caractere "|" (barra vertical) delimitador de campo. Cada registro deve necessariamente ocupar apenas uma linha no 7 Formação dos registros arquivo. Preenchimento fixo: o campo deve ser preenchido com o tamanho Preenchimento dos exato.

campos Preenchimento variável: o campo pode ter variação de tamanho de preenchimento. Deve ser informado com até 4 posições, representando 3 posições Campo numérico inteiras e 1 decimal; 9 referente a quantidade de Os zeros não significativos não devem ser informados; meses Os caracteres .(ponto) e ,(vírgula) não devem ser informados.

2. Estrutura de arquivo

2.1 Estrutura completa de uma declaração de Pessoa Física

Dirf - Declaração do imposto sobre a renda retido na fonte RESPO - Responsável pelo preenchimento DECPF - Declarante pessoa física IDREC - Identificação do código de receita BPFDEC - Beneficiário pessoa física do declarante RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTDP - Rendimentos Tributáveis - Dedução - Dependentes RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte CJAC - Compensação de Imposto por Decisão Judicial - Ano-calendário CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial INFPC - Informações de Previdência Complementar RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada RTFA - Rendimentos Tributáveis - Dedução - FAPI ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada ESFA - Tributação com Exigibilidade Suspensa - Dedução - FAPI INFPA - Informações do beneficiário da pensão alimentícia RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia RIDAC - Rendimentos Isentos - Diária e Ajuda de Custo RIIRP - Rendimentos Isentos - Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV RIAP - Rendimentos Isentos - Abono Pecuniário RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria (65 anos ou mais) RIJMRE - Rendimentos Isentos Anuais - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função RIO - Rendimentos Isentos Anuais - Outros BPJDEC - Beneficiário pessoa jurídica do declarante

RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte RRA - Rendimentos recebidos acumuladamente IDREC - Identificação do código de receita BPFRRA - Beneficiário pessoa física do rendimento recebido acumuladamente RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte DAJUD - Despesa com ação judicial QTMESES - Quantidade de meses RIJMRE - Rendimentos Isentos Anuais - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função INFPA - Informações do beneficiário da pensão alimentícia RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia SCP - Informações da sociedade em conta de participação BPFSCP - Beneficiário pessoa física da sociedade em conta de participação RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação BPJSCP - Beneficiário pessoa jurídica da sociedade em conta de participação RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação PSE - Plano privado de assistência à saúde - coletivo empresarial OPSE - Operadora de plano privado de assistência à saúde - coletivo empresarial TPSE - Titular de plano privado de assistência à saúde - coletivo empresarial RTPSE - Reembolso do titular do plano de assistência à saúde - coletivo empresarial DTPSE - Dependente do titular de plano privado de assistência à saúde - coletivo empresarial RDTPSE - Reembolso do dependente do titular do plano de assistência à saúde - coletivo empresarial RPDE - Rendimentos pagos a residentes ou domiciliados no exterior BRPDE - Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE - Valores de rendimentos pagos a residentes ou domiciliados no exterior INF - Informações complementares para o comprovante de rendimentos FIMDirf - Término da declaração 2.2 Estrutura completa de uma declaração de Pessoa Jurídica

Dirf - Declaração do imposto sobre a renda retido na fonte RESPO - Responsável pelo preenchimento DECPJ - Declarante pessoa jurídica IDREC - Identificação do código de receita BPFDEC - Beneficiário pessoa física do declarante

RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTDP - Rendimentos Tributáveis - Dedução - Dependentes RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte CJAC - Compensação de Imposto por Decisão Judicial - Ano-calendário CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial INFPC - Informações de Previdência Complementar RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada RTFA - Rendimentos Tributáveis - Dedução - FAPI RTSP - Rendimentos Tributáveis - Dedução - Fundo de Previdência do Servidor Público RTEP - Rendimentos Tributáveis - Dedução - Contribuição do ente público patrocinador ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada ESFA - Tributação com Exigibilidade Suspensa - Dedução - FAPI ESSP - Tributação com Exigibilidade Suspensa - Dedução - Fundo de Previdência do Servidor Público ESEP - Tributação com Exigibilidade Suspensa - Dedução - Contribuição do ente público patrocinador INFPA - Informações do beneficiário da pensão alimentícia RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia RIDAC - Rendimentos Isentos - Diária e Ajuda de Custo RIIRP - Rendimentos Isentos - Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV RIAP - Rendimentos Isentos - Abono Pecuniário RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria (65 anos ou mais) RIBMR - Rendimentos Isentos - Bolsa de Estudo Recebida por Médico-residente RICAP - Rendimentos Isentos - Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIRPC - Rendimentos Isentos - Resgate de previdência complementar por portador de moléstia grave RIL96 - Rendimentos Isentos Anuais - Lucros e dividendos pagos a partir de 1996 RIPTS - Rendimentos Isentos Anuais - Valores pagos a titular ou sócio ou empresa de pequeno porte, exceto pró-labore e aluguéis RIJMRE - Rendimentos Isentos Anuais - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função

RIO - Rendimentos Isentos Anuais - Outros BPJDEC - Beneficiário pessoa jurídica do declarante RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte VPEIM - Valores pagos às entidades imunes ou isentas - IN RFB 1.234/2012 RIMUN - Rendimentos Imunes - art. 4º, inciso III RISEN - Rendimentos Isentos - art. 4º, inciso IV FCI - Fundo ou clube de investimento IDREC - Identificação do código de receita BPFFCI - Beneficiário pessoa física do fundo ou clube de investimento RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte CJAC - Compensação de Imposto por Decisão Judicial - Ano-calendário CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria (65 anos ou mais) RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave RICAP - Rendimentos Isentos - Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIO - Rendimentos Isentos Anuais - Outros BPJFCI - Beneficiário pessoa jurídica do fundo ou clube de investimento RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte PROC - Processo da justiça do trabalho/federal/estadual/Distrito Federal IDREC - Identificação do código de receita BPFPROC - Beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTDP - Rendimentos Tributáveis - Dedução - Dependentes RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte CJAC - Compensação de Imposto por Decisão Judicial - Ano-calendário CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada RTFA - Rendimentos Tributáveis - Dedução - FAPI

RTSP - Rendimentos Tributáveis - Dedução - Fundo de Previdência do Servidor Público ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada ESFA - Tributação com Exigibilidade Suspensa - Dedução - FAPI ESSP - Tributação com Exigibilidade Suspensa - Dedução - Fundo de Previdência do Servidor Público RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave RIJMRE - Rendimentos Isentos Anuais - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função RIRSR - Rendimentos pagos sem retenção do IR na fonte - Lei nº 10.833/2003 BPJPROC - Beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte RIRSR - Rendimentos pagos sem retenção do IR na fonte - Lei nº 10.833/2003 RRA - Rendimentos recebidos acumuladamente IDREC - Identificação do código de receita BPFRRA - Beneficiário pessoa física do rendimento recebido acumuladamente RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial INFPA - Informações do beneficiário da pensão alimentícia RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria (65 anos ou mais) RIJMRE - Rendimentos Isentos Anuais - Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função DAJUD - Despesa com ação judicial QTMESES - Quantidade de meses SCP - Informações da sociedade em conta de participação BPFSCP - Beneficiário pessoa física da sociedade em conta de participação RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação BPJSCP - Beneficiário pessoa jurídica da sociedade em conta de participação RISCP - Lucros e dividendos pagos ao sócio da sociedade em conta de participação PSE - Plano privado de assistência à saúde - coletivo empresarial OPSE - Operadora de plano privado de assistência à saúde - coletivo empresarial TPSE - Titular de plano privado de assistência à saúde - coletivo empresarial RTPSE - Reembolso do titular do plano de assistência à saúde - coletivo empresarial DTPSE - Dependente do titular de plano privado de assistência à saúde - coletivo empresarial

RDTPSE - Reembolso do dependente do titular do plano de assistência à saúde - coletivo empresarial RPDE - Rendimentos pagos a residentes ou domiciliados no exterior BRPDE - Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE - Valores de rendimentos pagos a residentes ou domiciliados no exterior INF - Informações complementares para o comprovante de rendimentos FIMDirf - Término da declaração 3. Leiaute do arquivo

3.1 Registro de identificação da declaração (identificador Dirf)

- Registro obrigatório no arquivo; - Deve ser o primeiro registro no arquivo; - Ocorre somente uma vez no arquivo. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 4 Dirf Sim 2 Ano referência N Fixo 4 2022 Sim 3 Ano-calendário N Fixo 4 2021 ou 2022 Sim S- 4 Indicador de retificadora C Fixo 1 Retificadora Sim N - Original 5 Número do recibo N Fixo 12 - Não Identificador de estrutura do 6 C Fixo 7 XJFSFHB Sim leiaute Observações: Ordem Campo Descrição Número do O preenchimento será obrigatório se o campo de ordem 4 igual a "S" e

recibo declaração transmitida sem o uso de certificação digital. 3.2 Registro do Responsável pelo preenchimento da declaração (identificador RESPO)

- Registro obrigatório no arquivo; - Deve ser o segundo registro no arquivo; - Ocorre somente uma vez no arquivo. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 5 RESPO Sim

2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 DDD N Fixo 2 - Sim 5 Telefone N Variável 9 - Sim 6 Ramal N Variável 6 - Não 7 Fax N Variável 9 - Não 8 Correio eletrônico C Variável 50 - Não Observações: Ordem Campo Descrição 4 DDD O primeiro algarismo deve ser diferente de zero.

Telefon Deve ser preenchido com oito ou nove

e algarismos. Deve ser preenchido com oito ou nove 7 Fax algarismos. 3.3 Registro de identificação do declarante pessoa física (identificador DECPF)

- Registro obrigatório no arquivo para declarante pessoa física; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPJ. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 5 DECPF Sim

2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Indicador de S - Pagou declarante de rendimentos a rendimentos pagos a 4 C Fixo 1 residentes ou Sim residentes ou domiciliados no domiciliados no exterior exterior N - Não pagou rendimentos a residentes ou domiciliados no exterior S - Titular de serviços Indicador de Titular notariais e de de Serviços registros 5 C Fixo 1 Sim Notariais e de N - Não é titular de Registros serviços notariais e de registros Indicador de plano S - Existe pagamento privado de de valor pelo 6 C Fixo 1 Sim assistência à saúde - titular/dependente do coletivo empresarial plano de saúde N - Não existe pagamento de valor pelo titular/dependente do plano de saúde Indicador de sócio ostensivo S - Sócio ostensivo responsável por 7 C Fixo 1 N - Não é sócio Sim sociedade em conta ostensivo de participação - SCP S - Encerramento de espólio/saída Indicador de definitiva do país 8 situação especial da C Fixo 1 N - Não é Sim declaração encerramento de espólio/saída definitiva do país 9 Data do Evento D Fixo 8 - Não

1 - Encerramento de espólio 10 Tipo de Evento N Fixo 1 Não 2 - Saída definitiva do Brasil S - Declarante Indicador de falecido 11 C Fixo 1 Sim declarante falecido N - Declarante não falecido 12 Data do óbito D Fixo 8 - Não 0 - Sem espólio 13 Situação do espólio N Fixo 1 1 - Espólio não Não encerrado 14 CPF do inventariante N Fixo 11 - Não Nome do 15 C Variável 60 - Não inventariante Observações: Ordem Campo Descrição 9 Data do Evento O preenchimento será obrigatório se o campo de ordem 8 igual a "S". 10 Tipo de Evento O preenchimento será obrigatório se o campo de ordem 8 igual a "S". Indicador de Deve ser preenchido com "S" se o campo de ordem 8 igual a "S" e 11 declarante campo de ordem 10 igual a 1 falecido Permitido somente para as declarações normais Situação do 13 Para o encerramento de espólio a declaração será sempre de situação espólio especial; Declarante falecido - indicador igual a SIM Situação 1 - sem espólio - Apresentar declaração normal do ano-calendário; - Informar data do óbito e situação do espólio igual a 0; Observação: não serão aceitas declarações para anos posteriores ao ano da data do óbito sem espólio; Situação 2 - com espólio não encerrado - Apresentar declaração normal do ano-calendário; - Informar data do óbito e situação do espólio igual a 1; Observação: serão aceitas declarações para anos posteriores ao ano da data do óbito até que seja apresentada uma declaração de situação especial - encerramento de espólio; Situação 3 - encerramento de espólio - Apresentar declaração de situação especial do ano-calendário; Observação: os campos 12 a 15 não serão preenchidos; 3.4 Registro de identificação do declarante pessoa jurídica (identificador DECPJ)

- Registro obrigatório no arquivo para declarante pessoa jurídica; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPF. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 5 DECPJ Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim Natureza do 0 - Pessoa jurídica 4 N Fixo 1 Sim declarante de direito privado

1 - Órgãos, autarquias e fundações da administração pública federal 2 - Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal 3 - Empresa pública ou sociedade de economia mista federal 4 - Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal 8 - Entidade com alteração de natureza jurídica (uso restrito) CPF responsável 5 N Fixo 11 - Sim perante o CNPJ Indicador de sócio ostensivo S - Sócio ostensivo 6 responsável por C Fixo 1 N - Não é sócio Sim sociedade em conta ostensivo de participação - SCP S - Depositário de Indicador de crédito decorrente declarante de decisão judicial 7 depositário de crédito C Fixo 1 N - Não é depositário Sim decorrente de de crédito decisão judicial decorrente de decisão judicial Indicador de declarante de S - Instituição instituição administradora ou 8 administradora ou C Fixo 1 intermediadora de Sim intermediadora de fundo ou clube de fundo ou clube de investimento investimento N - Não é instituição administradora ou intermediadora de fundo ou clube de investimento Indicador de S - Pagou declarante de rendimentos a rendimentos pagos a 9 C Fixo 1 residentes ou Sim residentes ou domiciliados no domiciliados no exterior exterior N - Não pagou

rendimentos a residentes ou domiciliados no exterior Indicador de plano S - Existe pagamento privado de de valor pelo 10 C Fixo 1 Sim assistência à saúde - titular/dependente do coletivo empresarial plano de saúde N - Não existe pagamento de valor pelo titular/dependente do plano de saúde Indicador de entidade em que a União S - Existe pagamento detém maioria do de valores a 11 C Fixo 1 Sim capital social sujeito entidades a voto, recebe imunes/isentas recursos do Tesouro Nacional e está obrigada a registrar a N - Não existe execução pagamento de orçamentária no Siafi valores a entidades (IN 1.234/2012, art. 4º, imunes/isentas incisos III e IV) Indicador de S - Fundação pública fundação pública de de direito privado direito privado 12 C Fixo 1 N - Não é fundação Sim instituída pela União, pública de direito Estados, Municípios privado ou Distrito Federal S - Declaração de Indicador de situação situação especial 13 especial da C Fixo 1 Sim N - Não é declaração declaração de situação especial 14 Data do evento D Fixo 8 - Não Observações: Ordem Campo Descrição Relativamente à natureza do declarante 8 - Entidade com 4 Natureza do declarante alteração de natureza jurídica (uso restrito), esclarecemos: 1. Para declarante que alterou sua natureza jurídica em relação ao ano-calendário e que implique em mudança da natureza do declarante na ficha Informações da Dirf; 2. Para declarante que mudou sua natureza jurídica de órgão público para privado, ou vice-versa. Aplica-se ainda para mudanças entre as esferas governamentais da federação. Por exemplo: órgão público ou pessoa jurídica de direito privado estadual ou municipal que passou a ser federal, ou vice-versa; 3. A declaração deverá ser entregue na RFB. Indicador de entidade em que a União detém maioria Indicador com a opção "Sim" permitido somente se campo de 11 do capital social sujeito a ordem 4 - Natureza do declarante, igual a "0", "1", "3" ou "8" voto, recebe recursos do Tesouro Nacional e está obrigada a registrar a execução orçamentária no Siafi (IN 1.234/2012, art. 4º, incisos III

e IV) Indicador de fundação pública de direito privado Indicador com a opção "S" permitido somente se campo de 12 instituída pela União, ordem 4 - Natureza do declarante, igual a "1", "2" ou "8" Estados, Municípios ou Para as demais naturezas do declarante deve ser igual a "N" Distrito Federal O preenchimento será obrigatório se o campo de ordem 13 14 Data do evento igual a "S". 3.5 Registro de identificação do código de receita (identificador IDREC)

- Deve ser apresentado com os códigos de receita em ordem crescente; - Deve estar associado aos registros do tipo DECPF, DECPJ, FCI, PROC ou RRA. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o Identificador 1 C Fixo 5 IDREC Sim de registro De acordo com a tabela de Código de códigos de receitas 2 N Fixo 4 Sim receita constante na IN que dispõe sobre a Dirf 3.6 Registro de beneficiário pessoa física do declarante (identificador BPFDEC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 6 BPFDEC Sim

2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Data atribuída pelo 4 laudo da moléstia D Fixo 8 - Não grave S - Existem Indicador de informações 5 identificação do C Fixo 1 Sim detalhadas do alimentando alimentando N - Não existem informações detalhadas do alimentando S - Existem Indicador de informações identificação da 6 C Fixo 1 detalhadas da Sim previdência previdência complementar complementar N - Não existem informações detalhadas da previdência complementar Observações: Ordem Campo Descrição

Indicador de Se campo igual a "S" - deverá constar o registro INFPA seguido do 5 identificação do registro de valor (RTPA e/ou ESPA) para cada alimentando. alimentando Se campo igual a "N" - não apresentar o registro INFPA; deverão constar os registros de valores (RTPA e/ou ESPA) com o valor total de pensão alimentícia pago a todos os alimentandos do beneficiário. - As informações detalhadas a que se refere o campo são: CPF, data de nascimento, nome e relação de dependência do alimentando (registro INFPA). Indicador de Se campo igual a "S" - deverá constar o registro INFPC seguido do identificação da 6 registro de valor (RTPP, RTFA, RTSP e/ou ESPP, ESFA, ESSP) para previdência cada entidade de previdência complementar do beneficiário. complementar Se campo igual a "N" - não apresentar o registro INFPC; deverão constar apenas os registros de valores mensais (RTPP, RTFA, RTSP e/ou ESPP, ESFA, ESSP) com o total dos valores de previdência complementar pagos pelo beneficiário. - As informações detalhadas a que se refere o campo são: CNPJ e Nome empresarial da entidade de previdência complementar (registro INFPC). 3.7 Registro de beneficiário pessoa jurídica do declarante (identificador BPJDEC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 6 BPJDEC Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.8 Registro de valores pagos às entidades imunes e isentas (identificador VPEIM)

- Serão apresentados todos os CNPJ em ordem crescente; - Registro permitido somente para declarante pessoa jurídica; e se campo 12 do registro DECPJ igual a "S"; Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 5 VPEIM Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.9 Registro de identificação do fundo ou clube de investimento (identificador FCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Deve estar associado ao registro do tipo DECPJ. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 3 FCI Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim 3.10 Registro do beneficiário pessoa física do fundo ou clube de investimento (identificador BPFFCI)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 6 BPFFCI Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Data atribuída pelo laudo da 4 D Fixo 8 - Não moléstia grave 3.11 Registro do beneficiário pessoa jurídica do fundo ou clube de investimento (identificador BPJFCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 6 BPJFCI Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.12 Registro de processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador PROC)

- Deve estar classificado em ordem crescente por: - Tipo de justiça; - Número do processo; - Deve estar associado ao registro do tipo DECPJ. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 4 PROC Sim

1 - Justiça federal 2 - Justiça do trabalho 2 Indicador de Justiça N Fixo 1 Sim 3 - Justiça estadual/Distrito Federal 3 Número do processo C Variável 20 - Sim Indicador de tipo de 1 - Pessoa física 4 advogado/escritório de N Fixo 1 Não 2 - Pessoa jurídica advocacia CPF do advogado/ CPF com 11 dígitos 5 N Variável 14 Não CNPJ do escritório de CNPJ com 14

advocacia dígitos Nome da pessoa Nome do advogado/ física até 60 Nome empresarial do posições 6 C Variável 150 Não escritório de Nome empresarial advocacia da pessoa jurídica até 150 posições Valor pago para o Valor pago para o 7 N Variável 13 Não advogado advogado 3.13 Registro de beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPFPROC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 7 BPFPROC Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Data atribuída pelo laudo da 4 D Fixo 8 - Não moléstia grave 3.14 Registro de beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPJPROC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 7 BPJPROC Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.15 Registro de rendimentos recebidos acumuladamente (identificador RRA)

- Deve estar classificado em ordem crescente por: - Identificador de rendimento recebido acumuladamente; - Número do processo/requerimento. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o 1 Identificador de registro C Fixo 3 RRA Sim 1 - Pago pelo

declarante 2 rendimento recebido N Fixo 1 Sim 2 - Pago pela acumuladamente justiça Número do 3 C Variável 20 - Não processo/requerimento 4 Indicador de tipo de N Fixo 1 1 - Pessoa física Não

advogado/escritório de 2 - Pessoa jurídica advocacia CPF com 11 CPF do advogado/CNPJ dígitos 5 do escritório de N Variável 14 Não CNPJ com 14 advocacia dígitos Nome da pessoa física com até 60 Nome do posições advogado/Nome 6 C Variável 150 Nome empresarial Não empresarial do da pessoa jurídica escritório de advocacia com até 150 posições Valor pago para o Valor pago para o 7 N Variável 13 Não advogado advogado Observações: Ordem Campo Descrição Número do O preenchimento será obrigatório se o campo de ordem 2

processo/requerimento igual a 2. 3.16 Registro de beneficiário pessoa física dos rendimentos recebidos acumuladamente (identificador BPFRRA)

- Deve estar classificado em ordem crescente por: - CPF; - Natureza do RRA; - Deve estar associado ao registro do tipo IDREC. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 6 BPFRRA Sim

2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Natureza do RRA C Variável 50 - Não Data atribuída pelo 5 laudo da moléstia D Fixo 8 - Não grave S - Existem Indicador de informações 6 identificação do C Fixo 1 Sim detalhadas do alimentando alimentando N - Não existem informações detalhadas do alimentando Observações: Ordem Campo Descrição Indicador de 1. O campo só poderá ser igual a "S" se o campo 2 do registro RRA 6 identificação do igual a "1" (Pago pelo declarante); alimentando 2. Se campo igual a "S" - deverá constar o registro INFPA e RTPA para cada alimentando; 3. Se campo igual a "N" - não apresentar o registro INFPA; deverá constar o registro RTPA com o valor de pensão alimentícia pago a todos os alimentandos do beneficiário;

4. As informações detalhadas a que se refere o campo são: CPF, Data de nascimento e Nome do alimentando (registro INFPA). 3.17 Registro de identificação de Previdência Complementar (identificador INFPC)

- Registro permitido somente se campo 6 do registro BPFDEC (Indicador de identificação da previdência complementar) igual a "S"; - Serão apresentados todos os CNPJ em ordem crescente; - Deve estar associado ao registro do tipo BPFDEC; - Deve constar um registro INFPC para cada CNPJ de entidade de previdência complementar. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 5 INFPC Sim

2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim 3.18 Registro de informações do beneficiário da pensão alimentícia (identificador INFPA)

- Registro permitido somente se Indicador de identificação do alimentando igual a "S" (BPFDEC, campo 5; e BPFRRA, campo 6); - Registro INFPA associado ao BPFRRA será permitido somente quando o identificador de rendimento recebido acumuladamente igual a "1 - Pago pelo declarante" (campo 2 do registro RRA); - Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo BPFDEC, BPFRRA. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 5 INFPA Sim

CPF do 2 N Fixo 11 - Não alimentando 3 Data de nascimento D Fixo 8 - Não 4 Nome C Variável 60 - Sim 03 - Cônjuge/ Companheiro (a) Relação de 04 - Filho (a) 5 N Fixo 2 Não dependência 06 - Enteado (a) 08 - Pai/Mãe 10 - Agregado/Outros Observações: Ordem Campo Descrição CPF do Preenchimento obrigatório para maiores de 18 anos completos até 31 de

alimentando dezembro do ano-calendário da declaração. Preenchimento obrigatório para menores de 18 anos completos até 31 de Data de 3 dezembro do ano-calendário da declaração, que não tenham informado o nascimento CPF. 3.19 Registro de valores mensais (identificadores RTRT, RTPO, RTPP, RTFA, RTSP, RTEP, RTDP, RTPA, RTIRF, CJAA, CJAC, ESRT, ESPO, ESPP, ESFA, ESSP, ESEP, ESDP, ESPA, ESIR, ESDJ, RIP65, RIDAC, RIIRP, RIAP, RIMOG, RIRPC, RIBMR, RICAP, RISCP, RIMUN, RISEN e DAJUD)

- Deve ocorrer apenas se houver pelo menos um dos valores referentes aos meses ou 13º salário; - Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC, BPJDEC, BPFFCI, BPJFCI, BPFPROC, BPJPROC, BPFRRA, BPFSCP, BPJSCP, INFPC, INFPA, VPEIM. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos RTRT RTPO

1 C Variável 5 RTPP Sim

RTFA RTSP RTEP RTDP RTPA RTIRF CJAC CJAA ESRT ESPO ESPP ESFA ESSP ESEP ESDP ESPA ESIR ESDJ RIP65 RIDAC RIIRP RIAP RIMOG RIRPC RIBMR RICAP RISCP RIMUN RISEN DAJUD 2 Janeiro N Variável 13 - Não 3 Fevereiro N Variável 13 - Não 4 Março N Variável 13 - Não 5 Abril N Variável 13 - Não 6 Maio N Variável 13 - Não 7 Junho N Variável 13 - Não 8 Julho N Variável 13 - Não 9 Agosto N Variável 13 - Não 10 Setembro N Variável 13 - Não 11 Outubro N Variável 13 - Não 12 Novembro N Variável 13 - Não 13 Dezembro N Variável 13 - Não 14 Décimo Terceiro N Variável 13 - Não 3.20 Registro de valores anuais isentos/não tributáveis/sem retenção (identificadores RIL96, RIPTS, RIJMRE e RIRSR)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC (RIL96, RIPTS e RIJMRE), BPFPROC/BPJPROC (RIRSR); - Registro RIRSR permitido somente se "indicador de justiça" do registro PROC igual a 1 (Justiça Federal). Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos RIL96 Identificador de RIPTS 1 C Variável 6 Sim registro RIJMRE RIRSR 2 Valor pago no ano N Variável 13 - Sim 3.21 Registro de valores anuais de rendimentos isentos - outros (identificador RIO)

- Ocorrerá apenas um registro para cada beneficiário; - Deve estar associado ao registro do tipo BPFDEC ou BPFFCI. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 3 RIO Sim 2 Valor pago no ano N Variável 13 - Sim Descrição dos rendimentos 3 C Variável 60 - Sim isentos - outros 3.22 Registro de quantidade de meses (identificador QTMESES)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado ao registro do tipo BPFRRA. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 7 QTMESES Sim 2 Quantidade meses - janeiro N Variável 4 - Não Quantidade meses - 3 N Variável 4 - Não fevereiro 4 Quantidade meses - março N Variável 4 - Não 5 Quantidade meses - abril N Variável 4 - Não 6 Quantidade meses - maio N Variável 4 - Não 7 Quantidade meses - junho N Variável 4 - Não 8 Quantidade meses - julho N Variável 4 - Não 9 Quantidade meses - agosto N Variável 4 - Não Quantidade meses - 10 N Variável 4 - Não setembro 11 Quantidade meses - outubro N Variável 4 - Não Quantidade meses - 12 N Variável 4 - Não novembro Quantidade meses - 13 N Variável 4 - Não dezembro 3.23 Registro de informações da Sociedade em Conta de Participação (identificador SCP)

- Serão apresentados em ordem crescente de CNPJ. - Deve constar um registro para cada CNPJ de Sociedade em conta de participação Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 3 SCP Sim CNPJ da Sociedade em Conta 2 N Fixo 14 - Sim de Participação Nome empresarial da Sociedade 3 C Variável 150 - Sim em Conta de Participação 3.24 Registro de beneficiário pessoa física da sociedade em conta de participação (identificador BPFSCP)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJSCP, caso exista o registro; - Deve estar associado a um registro do tipo SCP. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 6 BPFSCP Sim 2 CPF N Fixo 11 - Sim 3 Nome C Variável 60 - Sim Percentual de participação na 4 N Variável 4 - Não SCP 3.25 Registro de beneficiário pessoa jurídica da sociedade em conta de participação (identificador BPJSCP)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFSCP, caso exista o registro; - Deve estar associado a um registro do tipo SCP. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 6 BPJSCP Sim 2 CNPJ N Fixo 14 - Sim 3 Nome empresarial C Variável 150 - Sim Percentual de participação na 4 C Variável 4 - Não SCP 3.26 Registro de pagamentos a plano privado de assistência à saúde - coletivo empresarial (identificador PSE)

- Ocorre somente uma vez no arquivo, caso exista informação de valores pagos pelo titular/dependente do plano de assistência à saúde. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 3 PSE Sim

3.27 Registro de operadora do plano privado de assistência à saúde - coletivo empresarial (identificador OPSE)

- Ocorre caso exista o registro PSE; - Serão apresentados todos os CNPJ em ordem crescente. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 4 OPSE Sim CNPJ da operadora de plano 2 privado de assistência à saúde - N Fixo 14 - Sim coletivo empresarial 3 Nome empresarial C Variável 150 - Sim 4 Registro ANS N Fixo 6 - Não 3.28 Registro de titular do plano privado de assistência à saúde - coletivo empresarial (identificador TPSE)

- Serão apresentados todos os CPF em ordem crescente. - Deve estar associado ao registro do tipo OPSE. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 4 TPSE Sim

2 CPF do titular N Fixo 11 - Sim 3 Nome C Variável 60 - Sim 4 Valor pago no ano N Variável 9 - Sim Observações: Ordem Campo Descrição Valor pago no Preenchimento obrigatório se o titular não possuir dependente cadastrado e

ano nem reembolso informado. 3.29 Registro de informação de reembolso do titular do plano de saúde - coletivo empresarial (identificador RTPSE)

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo TPSE; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos- calendário anteriores. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 5 RTPSE Sim

CPF/CNPJ do CPF com 11 dígitos 2 N Variável 14 Sim prestador de serviço CNPJ com 14 dígitos Nome da pessoa física até 60 Nome/Nome posições 3 empresarial do C Variável 150 Sim Nome empresarial prestador de serviço da pessoa jurídica até 150 posições Valor do reembolso 4 N Variável 9 - Não do ano-calendário Valor do reembolso 5 N Variável 9 - Não de anos anteriores Observações:

Ordem Campo Descrição Valor do reembolso do Valores reembolsados no ano-calendário, referentes a

ano-calendário pagamentos de serviços prestados no ano-calendário. Valor do reembolso de Valores reembolsados no ano-calendário referentes a

anos anteriores pagamentos de serviços prestados em anos anteriores. 3.30 Registro de dependente do plano privado de assistência à saúde - coletivo empresarial (identificador DTPSE)

- Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo TPSE. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 5 DTPSE Sim

2 CPF do dependente N Fixo 11 - Não 3 Data de nascimento D Fixo 8 - Não 4 Nome C Variável 60 - Sim 03 - Cônjuge/ Companheiro(a) Relação de 04 - Filho(a) 5 N Fixo 2 Não dependência 06 - Enteado(a) 08 - Pai/Mãe 10 - Agregado/ Outros 6 Valor pago no ano N Variável 9 - Sim Observações: Ordem Campo Descrição CPF do Preenchimento obrigatório para maiores de 18 anos completos até 31 de

dependente dezembro do ano-calendário da declaração. Preenchimento obrigatório para menores de 18 anos completos até 31 de Data de 3 dezembro do ano-calendário da declaração, que não tenham informado o nascimento CPF. Valor pago no Preenchimento obrigatório se o dependente não possuir reembolso

ano informado. 3.31 - Registro de informação de reembolso do dependente (identificador RDTPSE):

- Deve estar classificado em ordem crescente de CPF/CNPJ do prestador de serviço (primeiro os CPF e depois os CNPJ); - Deve estar associado ao registro do tipo DTPSE; - Só deverá constar o registro se houver valor de reembolso do ano-calendário ou de anos- calendário anteriores. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 6 RDTPSE Sim

CPF/CNPJ do CPF com 11 dígitos 2 N Variável 14 Sim prestador de serviço CNPJ com 14 dígitos Nome da pessoa física até 60 Nome/Nome posições 3 Empresarial do C Variável 150 Sim Nome empresarial prestador de serviço da pessoa jurídica até 150 posições

Valor do reembolso 4 N Variável 9 - Não do ano-calendário Valor do reembolso 5 N Variável 9 - Não de anos anteriores Observações: Ordem Campo Descrição Valor do reembolso do Valores reembolsados no ano-calendário, referentes a

ano-calendário pagamentos de serviços prestados no ano-calendário Valor do reembolso de Valores reembolsados no ano-calendário referentes a

anos anteriores pagamentos de serviços prestados em anos anteriores 3.32 Registro de rendimentos pagos a residentes ou domiciliados no exterior (identificador RPDE)

- Ocorre somente uma vez no arquivo, caso exista informação de rendimentos pagos a residentes ou domiciliados no exterior Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 4 RPDE Sim

3.33 Registro de beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior (identificador BRPDE)

- Deve estar classificado em ordem crescente por: - Beneficiário; - Código de país; - Número de identificação fiscal - NIF; - Deve estar associado ao registro do tipo RPDE. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o

1 C Fixo 5 BRPDE Sim

1 - Pessoa física 2 Beneficiário N Fixo 1 Sim 2 - Pessoa jurídica De acordo com a tabela de código dos países 3 Código de país N Variável 3 Sim constante na IN que dispõe sobre a Dirf Número de 4 identificação fiscal C Variável 30 - Não - NIF S - Dispensado do Indicador de Número de beneficiário identificação fiscal - dispensado do NIF 5 C Fixo 1 Sim Número de N - Não é dispensado Identificação Fiscal do Número de - NIF identificação fiscal - NIF Indicador de que o S - Dispensado do país não exige Número de 6 Número de C Fixo 1 identificação fiscal - Sim Identificação Fiscal NIF - NIF N - Não é dispensado

do Número de identificação fiscal - NIF CPF com 11 dígitos 7 CPF/CNPJ N Variável 14 Não CNPJ com 14 dígitos Nome/Nome 8 C Variável 150 - Sim empresarial De acordo com a tabela Relação fonte de informações sobre pagadora pessoa os beneficiários dos 9 jurídica e N Fixo 3 Não rendimentos constante beneficiário pessoa na IN que dispõe sobre jurídica a Dirf 10 Logradouro C Variável 60 - Não 11 Número C Variável 6 - Não 12 Complemento C Variável 25 - Não 13 Bairro/Distrito C Variável 20 - Não 14 Código postal N Variável 10 - Não 15 Cidade C Variável 40 - Não 16 Estado/Província C Variável 40 - Não 17 Telefone N Variável 15 - Não Observações: Ordem Campo Descrição Relação fonte pagadora pessoa jurídica e Preenchimento obrigatório se campo de ordem

beneficiário pessoa jurídica 2 (Beneficiário) igual a 2. 3.34 Registro de valores de rendimentos pagos a residentes ou domiciliados no exterior (identificador VRPDE)

- Deve estar classificado em ordem crescente por: - Data do pagamento; - Código de receita; - Deve estar associado ao registro do tipo BRPDE. Preenchiment Ordem Campo Formato Tamanho Valores válidos Obrigatório o Identificador 1 C Fixo 5 VRPDE Sim de registro Data do 2 D Fixo 8 - Sim pagamento Código de 3 N Fixo 4 - Sim receita De acordo com a tabela de Tipo de informações sobre os 4 N Fixo 3 Sim rendimento rendimentos constante na IN que dispõe sobre a Dirf Rendimento 5 N Variável 13 - Sim pago Imposto 6 N Variável 13 - Não retido De acordo com a tabela de Forma de informações sobre a forma 7 N Fixo 2 Sim tributação de tributação constante na IN que dispõe sobre a Dirf

3.35 Registro de informações complementares para o comprovante de rendimento (identificador INF)

- Serão apresentados todos os CPF em ordem crescente; - Deve haver um registro BPFDEC, BPFPROC e/ou BPFRRA correspondente na declaração; - Deve ocorrer apenas um registro para cada beneficiário. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos 1 Identificador de registro C Fixo 3 INF Sim 2 CPF N Fixo 11 - Sim Informações 3 C Variável 500 - Sim complementares 3.36 Registro identificador do término da declaração (identificador FIMDirf)

- Registro obrigatório no arquivo; - Deve ser o último registro no arquivo; - Ocorre somente uma vez no arquivo. Preenchiment Valores Ordem Campo Formato Tamanho Obrigatório o válidos

1 C Fixo 7 FIMDirf Sim

