---
titulo: "Ato Declaratório Executivo Cofis nº 77, de 10 de novembro de 2014"
orgao: "Coordenação-Geral de Fiscalização"
tipo: "Ato Declaratório Executivo"
numero: "77"
data: "2014-11-10"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 19/11/2014, seção 1, página 12"
data_publicacao: "2014-11-19"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/58338/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/58338/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "58338"
sha256_texto: "af19f4450b637c98cb6bb2d2864e7a553b6b3b1e753ed5c4f1967907fd307d29"
baixado_em: "2026-10-20"
---
# Ato Declaratório Executivo Cofis nº 77, de 10 de novembro de 2014

Dispõe sobre o leiaute do Programa Gerador da Declaração do Imposto sobre a Renda Retido na Fonte (PGD Dirf 2015).

O COORDENADOR-GERAL DE FISCALIZAÇÃO, no uso das atribuições que lhe confere o inciso III do art. 312 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 203, de 14 de maio de 2012, e tendo em vista o disposto na Instrução Normativa RFB nº 1.503, de 29 de outubro de 2014, declara:

**Art. 1º** Fica aprovado o leiaute aplicável aos campos, registros e arquivos da Declaração do Imposto sobre a Renda Retido na Fonte (Dirf 2015), constante no anexo único a este Ato Declaratório.

**Art. 2º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação no Diário Oficial da União.

KLEBER GIL ZECA

## ANEXO



ANEXO LEIAUTE DO ARQUIVO Declaração do Imposto sobre a Renda Retido na Fonte – Dirf

1. Regras gerais Estas regras devem ser respeitadas em todos os arquivos gerados, quando não excepcionadas por regra específica referente a um dado registro e explicitada em suas observações.

Nº Regra de preenchimento Descrição

ALFANUMÉRICO (C): representados por “C” - todos os caracteres, excetuados o 1 Formato dos campos caractere “|” (pipe ou barra vertical). NUMÉRICO (N): representados por “N” – pode conter apenas os valores de zero a nove.

Campos numéricos (D) Devem ser informados conforme o padrão ano, mês e dia (AAAAMMDD), excluindo-se 2 cujo conteúdo quaisquer caracteres de separação (tais como “.”, “/”, “-”, etc.); representa data

Os campos numéricos com número de inscrição (CNPJ e CPF) ou códigos de receita Campos numéricos com deverão ser informados com todos os dígitos, inclusive os zeros à esquerda; 3 número de inscrição ou códigos de receita As máscaras (caracteres especiais de formatação, tais como “.”, “/”, “-”, etc.) não devem ser informadas.

Devem ser informados com até 13 posições, representando 11 posições inteiras e 2 decimais; Campos numéricos Os zeros não significativos não devem ser informados;

referentes a valores Os caracteres ‘.’ (ponto) e ‘,’ (vírgula) não devem ser informados; Todos os valores monetários devem estar expressos em reais.

Os campos com conteúdo alfanumérico nos quais se faz necessário registrar números ou Campos alfanuméricos códigos de identificação (Exemplo: Número de Identificação Fiscal - NIF) deverão seguir 5 com números ou a regra de formação e tamanho definidos pelo respectivo órgão regulador; códigos de identificação As máscaras (caracteres especiais de formatação, tais como “.”, “/”, “-”, etc.) não devem ser informadas.

Ao final de cada campo (inclusive o último de cada registro) deve ser inserido o caractere delimitador “|” (pipe ou barra vertical: caractere 124 da Tabela ASCII); O caractere delimitador “|” (barra vertical) não deve ser incluído como parte integrante do 6 Formação dos campos conteúdo de quaisquer campos numéricos, datas ou alfanuméricos;

Na ausência de informação, o campo vazio (campo sem conteúdo, nulo e com valor zero) deverá ser iniciado com o caractere “|” (barra vertical) e imediatamente encerrado com o mesmo caractere “|” (barra vertical) delimitador de campo.

7 Formação dos registros Cada registro deve necessariamente ocupar apenas uma linha no arquivo.

Preenchimento dos Preenchimento fixo: o campo deve ser preenchido com o tamanho exato.

campos Preenchimento variável: o campo pode ter variação de tamanho de preenchimento.

Deve ser informado com até 4 posições, representando 3 posições inteiras e 1 decimal; Campo numérico 9 referente a quantidade Os zeros não significativos não devem ser informados; de meses Os caracteres ‘.’ (ponto) e ‘,’ (vírgula) não devem ser informados.

2. Estrutura de arquivo 2.1 Estrutura completa de uma declaração de Pessoa Física

Dirf - Declaração do imposto sobre a renda retido na fonte RESPO - Responsável pelo preenchimento DECPF - Declarante pessoa física

IDREC - Identificação do código de receita BPFDEC - Beneficiário pessoa física do declarante RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada RTDP - Rendimentos Tributáveis - Dedução - Dependentes RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte CJAC - Compensação de Imposto por Decisão Judicial - Ano-calendário CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial RIDAC - Rendimentos Isentos - Diária e Ajuda de Custo RIIRP - Rendimentos Isentos - Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV RIAP - Rendimentos Isentos - Abono Pecuniário RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria para Maiores de 65 anos RIO - Rendimentos Isentos Anuais - Outros BPJDEC - Beneficiário pessoa jurídica do declarante RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte RRA - Rendimentos recebidos acumuladamente IDREC - Identificação do código de receita BPFRRA - Beneficiário pessoa física do rendimento recebido acumuladamente RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte DAJUD - Despesa com ação judicial QTMESES - Quantidade de meses PSE - Plano privado de assistência à saúde coletivo empresarial OPSE - Operadora de plano privado de assistência à saúde coletivo empresarial TPSE - Titular de plano privado de assistência à saúde coletivo empresarial DTPSE - Dependente do titular de plano privado de assistência à saúde coletivo empresarial RPDE - Rendimentos pagos a residentes ou domiciliados no exterior BRPDE - Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE - Valores de rendimentos pagos a residentes ou domiciliados no exterior INF - Informações complementares para o comprovante de rendimentos FIMDirf - Término da declaração

2.2 Estrutura completa de uma declaração de Pessoa Jurídica

Dirf - Declaração do imposto sobre a renda retido na fonte RESPO - Responsável pelo preenchimento DECPJ - Declarante pessoa jurídica IDREC - Identificação do código de receita BPFDEC - Beneficiário pessoa física do declarante RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada RTDP - Rendimentos Tributáveis - Dedução - Dependentes RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte CJAC - Compensação de Imposto por Decisão Judicial - Ano-calendário CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial RIDAC - Rendimentos Isentos - Diária e Ajuda de Custo RIIRP - Rendimentos Isentos - Indenizações por Rescisão de Contrato de Trabalho, inclusive a título de PDV RIAP - Rendimentos Isentos - Abono Pecuniário RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave RIP65 - Rendimentos Isentos - Parcela Isenta de Aposentadoria para Maiores de 65 anos RIVC - Rendimentos Isentos - Benefícios Indiretos e Reembolso de Despesa - Voluntário da Copa RIBMR - Rendimentos Isentos - Bolsa de Estudo Recebida por Médico-Residente RICAP - Rendimentos Isentos - Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIL96 - Rendimentos Isentos Anuais - Lucros e dividendos pagos a partir de 1996 RIPTS - Rendimentos Isentos Anuais - Valores pagos a titular ou sócio ou empresa de pequeno porte, exceto pró-labore e aluguéis RIO - Rendimentos Isentos Anuais - Outros BPJDEC - Beneficiário pessoa jurídica do declarante RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte FCI - Fundo ou clube de investimento IDREC - Identificação do código de receita BPFFCI - Beneficiário pessoa física do fundo ou clube de investimento RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte CJAC - Compensação de Imposto por Decisão Judicial – Ano-calendário

CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave RICAP - Rendimentos Isentos - Complementação de aposentadoria de previdência complementar correspondente às contribuições efetuadas no período de 1º de janeiro de 1989 a 31 de dezembro de 1995 RIO - Rendimentos Isentos Anuais - Outros BPJFCI - Beneficiário pessoa jurídica do fundo ou clube de investimento RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte PROC - Processo da justiça do trabalho/federal/estadual/Distrito Federal IDREC - Identificação do código de receita BPFPROC - Beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTPP - Rendimentos Tributáveis - Dedução - Previdência Privada RTDP - Rendimentos Tributáveis - Dedução - Dependentes RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte CJAC - Compensação de Imposto por Decisão Judicial – Ano-calendário CJAA - Compensação de Imposto por Decisão Judicial - Anos Anteriores ESRT - Tributação com Exigibilidade Suspensa - Rendimento Tributável ESPO - Tributação com Exigibilidade Suspensa - Dedução - Previdência Oficial ESPP - Tributação com Exigibilidade Suspensa - Dedução - Previdência Privada ESDP - Tributação com Exigibilidade Suspensa - Dedução - Dependentes ESPA - Tributação com Exigibilidade Suspensa - Dedução - Pensão Alimentícia ESIR - Tributação com Exigibilidade Suspensa - Imposto sobre a Renda na Fonte ESDJ - Tributação com Exigibilidade Suspensa - Depósito Judicial RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave BPJPROC - Beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal RTRT - Rendimentos Tributáveis - Rendimento Tributável RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte RRA - Rendimentos recebidos acumuladamente IDREC - Identificação do código de receita BPFRRA - Beneficiário pessoa física do rendimento recebido acumuladamente RTRT - Rendimentos Tributáveis - Rendimento Tributável RTPO - Rendimentos Tributáveis - Dedução - Previdência Oficial RTPA - Rendimentos Tributáveis - Dedução - Pensão Alimentícia RTIRF - Rendimentos Tributáveis - Imposto sobre a Renda Retido na Fonte RIMOG - Rendimentos Isentos - Pensão, Aposentadoria ou Reforma por Moléstia Grave DAJUD - Despesa com ação judicial QTMESES - Quantidade de meses PSE - Plano privado de assistência à saúde - coletivo empresarial

OPSE - Operadora de plano privado de assistência à saúde - coletivo empresarial TPSE - Titular de plano privado de assistência à saúde - coletivo empresarial DTPSE - Dependente do titular de plano privado de assistência à saúde - coletivo empresarial RPDE - Rendimentos pagos a residentes ou domiciliados no exterior BRPDE - Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior VRPDE - Valores de rendimentos pagos a residentes ou domiciliados no exterior INF - Informações complementares para o comprovante de rendimentos FIMDirf - Término da declaração

3. Leiaute do arquivo 3.1 Registro de identificação da declaração (identificador Dirf)

- Registro obrigatório no arquivo; - Deve ser o primeiro registro no arquivo; - Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 4 Dirf Sim

2 Ano referência N Fixo 4 2015 Sim

3 Ano-calendário N Fixo 4 2014 ou 2015 Sim

S - Retificadora 4 Indicador de retificadora C Fixo 1 Sim N - Original

5 Número do recibo N Fixo 12 - Não

Identificador de estrutura do 6 C Fixo 7 M1LB5V2 Sim leiaute

Observações:

Ordem Campo Descrição

O preenchimento será obrigatório se o campo de ordem 4 igual a “S” e 5 Número do recibo declaração transmitida sem o uso de certificação digital.

3.2 Registro do Responsável pelo preenchimento da declaração (identificador RESPO)

- Registro obrigatório no arquivo; - Deve ser o segundo registro no arquivo; - Ocorre somente uma vez no arquivo.

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

- Registro obrigatório no arquivo para declarante pessoa física; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPJ.

1 Identificador de registro C Fixo 5 DECPF Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Indicador de declarante C Fixo 1 S - Pagou Sim de rendimentos pagos a residentes ou rendimentos a residentes ou domiciliados no exterior domiciliados no exterior.

N - Não pagou rendimentos a residentes ou domiciliados no exterior.

5 Indicador de Titular de C Fixo 1 S – Titular de serviços notariais e Sim Serviços Notariais e de de registros. Registros N – Não é titular de serviços notariais e de registros.

6 Indicador de plano C Fixo 1 S – Existe pagamento de valor pelo Sim privado de assistência à titular/dependente do plano de saúde - coletivo saúde. empresarial N – Não existe pagamento de valor pelo titular/dependente do plano de saúde.

7 Indicador de situação C Fixo 1 S - Encerramento de espólio/saída Sim especial da declaração definitiva do país. N - Não é encerramento de espólio/saída definitiva do país

8 Data do Evento D Fixo 8 - Não

9 Tipo de Evento N Fixo 1 1 - Encerramento de espólio. Não 2 - Saída definitiva do Brasil.

Observações:

Ordem Campo Descrição

8 Data do Evento O preenchimento será obrigatório se o campo de ordem 7 igual a “S”.

9 Tipo de Evento O preenchimento será obrigatório se o campo de ordem 7 igual a “S”.

3.4 Registro de identificação do declarante pessoa jurídica (identificador DECPJ)

- Registro obrigatório no arquivo para declarante pessoa jurídica; - Deve ser o terceiro registro no arquivo; - Ocorre somente uma vez no arquivo; - Não pode ser informado se existir o registro tipo DECPF.

1 Identificador de registro C Fixo 5 DECPJ Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

4 Natureza do declarante N Fixo 1 0 - Pessoa jurídica de direito Sim privado. 1 - Órgãos, autarquias e fundações da administração pública federal.

2 - Órgãos, autarquias e fundações da administração pública estadual, municipal ou do Distrito Federal.

3 – Empresa pública ou sociedade de economia mista federal.

4 - Empresa pública ou sociedade de economia mista estadual, municipal ou do Distrito Federal.

8 – Entidade com alteração de natureza jurídica (uso restrito).

5 CPF responsável N Fixo 11 - Sim perante o CNPJ

6 Indicador de sócio C Fixo 1 S - Sócio ostensivo. Sim ostensivo responsável por sociedade em conta N - Não é sócio ostensivo. de participação - SCP

7 Indicador de declarante C Fixo 1 S - Depositário de crédito Sim depositário de crédito decorrente de decisão decorrente de decisão judicial. judicial N – Não é depositário de crédito decorrente de decisão judicial.

8 Indicador de declarante C Fixo 1 S - Instituição administradora Sim de instituição ou intermediadora de fundo administradora ou ou clube de investimento. intermediadora de fundo ou clube de N – Não é instituição investimento administradora ou intermediadora de fundo ou clube de investimento.

9 Indicador de declarante C Fixo 1 S - Pagou rendimentos a Sim de rendimentos pagos residentes ou domiciliados a residentes ou no exterior. domiciliados no exterior N - Não pagou rendimentos a residentes ou domiciliados no exterior.

10 Indicador de plano C Fixo 1 S – Existe pagamento de Sim privado de assistência valor pelo titular/dependente à saúde - coletivo do plano de saúde. empresarial N – Não existe pagamento de valor pelo titular/dependente do plano de saúde.

11 Indicador de C Fixo 1 S - Existe pagamento Sim pagamentos relacionado à Copa relacionados à Copa das Confederações Fifa N - Não existe pagamento 2013 e Copa do Mundo relacionado à Copa Fifa 2014

12 Indicador de situação C Fixo 1 S - Declaração de situação Sim especial da declaração especial. N - Não é declaração de situação especial.

13 Data do evento D Fixo 8 - Não

Observações:

Ordem Campo Descrição

4 Natureza do declarante Relativamente à natureza do declarante 8 – Entidade com alteração de natureza jurídica (uso restrito), esclarecemos: 1. para declarante que alterou sua natureza jurídica em relação ao ano-calendário e que implique em mudança da natureza do declarante na ficha Informações da Dirf;

2. para declarante que mudou sua natureza jurídica de órgão público para privado, ou vice-versa. Aplica-se ainda para mudanças entre as esferas governamentais da federação. Por exemplo: órgão público ou pessoa jurídica de direito privado estadual ou municipal que passou a ser federal, ou vice-versa;

3. a declaração deverá ser entregue na RFB.

12 Data do evento O preenchimento será obrigatório se o campo de ordem 12 igual a “S”.

3.5 Registro de identificação do código de receita (identificador IDREC)

- Deve ser apresentado com os códigos de receita em ordem crescente; - Deve estar associado aos registros do tipo DECPF, DECPJ, FCI, PROC ou RRA.

1 Identificador de registro C Fixo 5 IDREC Sim

2 Código de receita N Fixo 4 De acordo com a tabela Sim de códigos de receitas constante na IN que dispõe sobre a Dirf.

3.6 Registro de beneficiário pessoa física do declarante (identificador BPFDEC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFDEC Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Data atribuída pelo laudo da D Fixo 8 - Não moléstia grave

3.7 Registro de beneficiário pessoa jurídica do declarante (identificador BPJDEC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFDEC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPJDEC Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

3.8 Registro de identificação do fundo ou clube de investimento (identificador FCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Deve estar associado ao registro do tipo DECPJ.

1 Identificador de registro C Fixo 3 FCI Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

3.9 Registro do beneficiário pessoa física do fundo ou clube de investimento (identificador BPFFCI)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFFCI Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Data atribuída pelo laudo da D Fixo 8 - Não moléstia grave

3.10 Registro do beneficiário pessoa jurídica do fundo ou clube de investimento (identificador BPJFCI)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFFCI, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPJFCI Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

3.11 Registro de processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador PROC)

- Deve estar classificado em ordem crescente por: - Tipo de justiça; - Número do processo;

- Deve estar associado ao registro do tipo DECPJ.

1 Identificador de registro C Fixo 4 PROC Sim

2 Indicador de Justiça N Fixo 1 1 - Justiça federal Sim 2 - Justiça do trabalho 3 - Justiça estadual/Distrito Federal

3 Número do processo C Variável 20 - Sim

4 Indicador de tipo de N Fixo 1 1 - Pessoa física Não advogado/escritório de advocacia 2 - Pessoa jurídica

5 CPF do advogado/ CNPJ N Variável 14 CPF com 11 dígitos Não do escritório de advocacia CNPJ com 14 dígitos

6 Nome do advogado/ C Variável 150 Nome da pessoa física até Não Nome empresarial do 60 posições. escritório de advocacia Nome empresarial da pessoa jurídica até 150 posições.

3.12 Registro de beneficiário pessoa física do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPFPROC)

- Serão apresentados todos os CPF em ordem crescente; - Devem ser apresentados antes dos registros com identificador BPJPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 7 BPFPROC Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Data atribuída pelo laudo da D Fixo 8 - Não moléstia grave

3.13 Registro de beneficiário pessoa jurídica do processo da justiça do trabalho/federal/estadual/Distrito Federal (identificador BPJPROC)

- Serão apresentados todos os CNPJ em ordem crescente; - Devem ser apresentados depois dos registros com identificador BPFPROC, caso exista o registro; - Deve estar associado a um registro do tipo IDREC.

1 Identificador de registro C Fixo 7 BPJPROC Sim

2 CNPJ N Fixo 14 - Sim

3 Nome empresarial C Variável 150 - Sim

3.14 Registro de rendimentos recebidos acumuladamente (identificador RRA)

- Deve estar classificado em ordem crescente por: - Indicador de rendimento recebido acumuladamente; - Número do processo.

1 Identificador de registro C Fixo 3 RRA Sim

2 Identificador de N Fixo 1 1 - Pago pelo declarante Sim rendimento recebido acumuladamente 2 - Pago pela justiça

3 Número do C Variável 20 - Não processo/requerimento

4 Indicador de tipo de N Fixo 1 1 - Pessoa física Não advogado/escritório de advocacia 2 - Pessoa jurídica

5 CPF do advogado/CNPJ N Variável 14 CPF com 11 dígitos Não do escritório de advocacia CNPJ com 14 dígitos

6 Nome do advogado/Nome C Variável 150 Nome da pessoa física com até Não empresarial do escritório 60 posições. de advocacia Nome empresarial da pessoa jurídica com até 150 posições.

Observações:

Ordem Campo Descrição

3 Número do processo/requerimento O preenchimento será obrigatório se o campo de ordem 2 igual a 2.

3.15 Registro de beneficiário pessoa física dos rendimentos recebidos acumuladamente (identificador BPFRRA)

- Deve estar classificado em ordem crescente por: - CPF; - Natureza do RRA; - Deve estar associado ao registro do tipo IDREC.

1 Identificador de registro C Fixo 6 BPFRRA Sim

2 CPF N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Natureza do RRA C Variável 50 - Não

5 Data atribuída pelo laudo da D Fixo 8 - Não moléstia grave

3.16 Registro de valores mensais (identificadores RTRT, RTPO, RTPP, RTDP, RTPA, RTIRF, CJAA, CJAC, ESRT, ESPO, ESPP, ESDP, ESPA, ESIR, ESDJ, RIP65, RIDAC, RIIRP, RIAP, RIMOG, RIVC, RIBMR, RICAP e DAJUD)

- Deve ocorrer apenas se houver pelo menos um dos valores referente aos meses ou 13º salário; - Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado aos registros dos tipos BPFDEC, BPJDEC, BPFFCI, BPJFCI, BPFPROC, BPJPROC ou BPFRRA.

RTRT RTPO RTPP RTDP RTPA

RTIRF CJAC CJAA ESRT ESPO

ESPP ESDP 1 Identificador de registro C Variável 5 Sim ESPA ESIR ESDJ

RIP65 RIDAC RIIRP RIAP RIMOG

RIVC RIBMR RICAP DAJUD

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

3.17 Registro de valores anuais isentos (identificadores RIL96 e RIPTS)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado ao registro do tipo BPFDEC.

RIL96 1 Identificador de registro C Fixo Sim RIPTS

2 Valor pago no ano N Variável 13 - Sim

3.18 Registro de valores anuais de rendimentos isentos - outros (identificador RIO)

- Ocorrerá apenas um registro para cada beneficiário; - Deve estar associado ao registro do tipo BPFDEC ou BPFFCI.

1 Identificador de registro C Fixo 3 RIO Sim

2 Valor pago no ano N Variável 13 - Sim

3 Descrição dos rendimentos C Variável 60 - Sim isentos - outros

3.19 Registro de quantidade de meses (identificador QTMESES)

- Deve ocorrer apenas um registro de cada identificador para o mesmo beneficiário; - Deve estar associado ao registro do tipo BPFRRA.

1 Identificador de registro C Fixo 7 QTMESES Sim

2 Quantidade meses - Janeiro N Variável 4 - Não

3 Quantidade meses - Fevereiro N Variável 4 - Não

4 Quantidade meses - Março N Variável 4 - Não

5 Quantidade meses - Abril N Variável 4 - Não

6 Quantidade meses - Maio N Variável 4 - Não

7 Quantidade meses - Junho N Variável 4 - Não

8 Quantidade meses - Julho N Variável 4 - Não

9 Quantidade meses - Agosto N Variável 4 - Não

10 Quantidade meses - Setembro N Variável 4 - Não

11 Quantidade meses - Outubro N Variável 4 - Não

12 Quantidade meses - Novembro N Variável 4 - Não

13 Quantidade meses - Dezembro N Variável 4 - Não

3.20 Registro de pagamentos a plano privado de assistência à saúde - coletivo empresarial (identificador PSE)

- Ocorre somente uma vez no arquivo, caso exista informação de valores pagos pelo titular/dependente do plano de assistência à saúde.

1 Identificador de registro C Fixo 3 PSE Sim

3.21 Registro de operadora do plano privado de assistência à saúde - coletivo empresarial (identificador OPSE)

- Ocorre caso exista o registro PSE; - Serão apresentados todos os CNPJ em ordem crescente.

1 Identificador de registro C Fixo 4 OPSE Sim

CNPJ da operadora de plano 2 privado de assistência à saúde - N Fixo 14 - Sim coletivo empresarial

3 Nome empresarial C Variável 150 - Sim

4 Registro ANS N Fixo 6 - Sim

3.22 Registro de titular do plano privado de assistência à saúde - coletivo empresarial (identificador TPSE)

- Serão apresentados todos os CPF em ordem crescente.

- Deve estar associado ao registro do tipo OPSE.

1 Identificador de registro C Fixo 4 TPSE Sim

2 CPF do titular N Fixo 11 - Sim

3 Nome C Variável 60 - Sim

4 Valor pago no ano N Variável 13 - Sim

3.23 Registro de dependente do plano privado de assistência à saúde - coletivo empresarial (identificador DTPSE)

- Deve estar classificado em ordem crescente de CPF e data de nascimento; - Deve estar associado ao registro do tipo TPSE.

1 Identificador de registro C Fixo 5 DTPSE Sim

2 CPF do dependente N Fixo 11 - Não

3 Data de nascimento D Fixo 8 - Não

4 Nome C Variável 60 - Sim

03 - Cônjuge/ Companheiro(a) 04 - Filho(a) 5 Relação de dependência N Fixo 2 Não 06 - Enteado(a) 08 - Pai/Mãe 10 - Agregado/ Outros

6 Valor pago no ano N Variável 13 - Sim

3.24 Registro de rendimentos pagos a residentes ou domiciliados no exterior (identificador RPDE)

- Ocorre somente uma vez no arquivo, caso exista informação de rendimentos pagos a residentes ou domiciliados no exterior

1 Identificador de registro C Fixo 4 RPDE Sim

3.25 Registro de beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior (identificador BRPDE)

- Deve estar classificado em ordem crescente por: - Beneficiário;

- Código de país; - Número de identificação fiscal - NIF; - Deve estar associado ao registro do tipo RPDE.

Identificador de 1 C Fixo 5 BRPDE Sim registro

1 - Pessoa física 2 Beneficiário N Fixo 1 Sim 2 - Pessoa jurídica

De acordo com a tabela de 3 Código de país N Variável 3 código dos países constante Sim na IN que dispõe sobre a Dirf

Número de 4 identificação fiscal - C Variável 30 - Não NIF

Indicador de S - Dispensado do Número beneficiário de identificação fiscal - NIF dispensado do 5 C Fixo 1 N - Não é dispensado do Sim Número de Identificação Fiscal - Número de identificação NIF fiscal - NIF

Indicador de que o S - Dispensado do Número país não exige de identificação fiscal - NIF 6 Número de C Fixo 1 N - Não é dispensado do Sim Identificação Fiscal - Número de identificação NIF fiscal - NIF

CPF com 11 dígitos. 7 CPF/CNPJ N Variável 14 Não CNPJ com 14 dígitos.

Nome/Nome 8 C Variável 150 - Sim empresarial

De acordo com a tabela de Relação fonte informações sobre os pagadora pessoa 9 N Fixo 3 beneficiários dos Não jurídica e beneficiário rendimentos constante na IN pessoa jurídica que dispõe sobre a Dirf

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

Relação fonte pagadora pessoa Preenchimento obrigatório se campo de ordem 2 (Beneficiário) igual a 2.

jurídica e beneficiário pessoa jurídica

3.26 Registro de valores de rendimentos pagos a residentes ou domiciliados no exterior (identificador VRPDE)

- Deve estar classificado em ordem crescente por: - Data do pagamento; - Código de receita; - Deve estar associado ao registro do tipo BRPDE.

1 Identificador de registro C Fixo 5 VRPDE Sim

2 Data do pagamento D Fixo 8 - Sim

3 Código de receita N Fixo 4 - Sim

De acordo com a tabela de informações sobre os 4 Tipo de rendimento N Fixo 3 Sim rendimentos constante na IN que dispõe sobre a Dirf

5 Rendimento pago N Variável 13 - Sim

6 Imposto retido N Variável 13 - Não

De acordo com a tabela de informações sobre a forma de 7 Forma de tributação N Fixo 2 Sim tributação constante na IN que dispõe sobre a Dirf

3.27 Registro de informações complementares para o comprovante de rendimento (identificador INF)

- Serão apresentados todos os CPF em ordem crescente; - Deve haver um registro BPFDEC, BPFPROC e/ou BPFRRA correspondente na declaração; - Deve ocorrer apenas um registro para cada beneficiário.

1 Identificador de registro C Fixo 3 INF Sim

2 CPF N Fixo 11 - Sim

3 Informações complementares C Variável 200 - Sim

3.28 Registro identificador do término da declaração (identificador FIMDirf)

- Registro obrigatório no arquivo; - Deve ser o último registro no arquivo; - Ocorre somente uma vez no arquivo.

1 Identificador de registro C Fixo 7 FIMDirf Sim

