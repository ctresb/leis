---
titulo: "PORTARIA Nº 2.964, DE 20 DE SETEMBRO DE 2019"
orgao: "Ministério da Infraestrutura/Agência Nacional de Aviação Civil/Superintendência de Regulação Econômica de Aeroportos"
tipo: "Portaria"
numero: "2964"
data: 2019-09-20
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 27/09/2019, seção 1, p. 147"
data_publicacao: 2019-09-27
edicao: "188"
fonte: "https://www.in.gov.br/web/dou/-/portaria-n-2.964-de-20-de-setembro-de-2019-218533779"
sha256_html_fonte: 0e7c37aac63543e23f7d3ae70e539bd34c4d1c2a422e796153c3f2932e896233
baixado_em: 2026-10-27
---
# PORTARIA Nº 2.964, DE 20 DE SETEMBRO DE 2019

PORTARIA Nº 2.964, DE 20 DE SETEMBRO DE 2019

Estabelece a estrutura dos dados e os procedimentos de remessa do Relatório de Remuneração das Tarifas de Embarque e Conexão - RTEC, Relatório de Remuneração das Tarifas de Pouso e Permanência - RTAP e do Relatório de Remuneração das Tarifas de Armazenagem e Capatazia - RTAC, previstas no item 4 do Anexo 4 dos Contratos de Concessão nºs 001/ANAC/2019-Nordeste, 002/ANAC/2019-Centro-Oeste e 003/ANAC/2019-Sudeste.

O SUPERINTENDENTE DE REGULAÇÃO ECONÔMICA DE AEROPORTOS, no uso das atribuição que lhe confere o art. 41, incisos IV, XV e XVI, do Regimento Interno, aprovado pela Resolução nº 381, de 14 de junho de 2016, e tendo em vista o disposto no anexo 4 dos contratos de concessão para ampliação, manutenção e exploração dos aeroportos integrantes dos blocos nordeste, centro-oeste e sudeste, e considerando o que consta do processo 00058.026901/2019-84, resolve:

**Art. 1º** Estabelecer a estrutura dos dados e os procedimentos de remessa do Relatório de Remuneração das Tarifas de Embarque e Conexão - RTEC; Relatório de Remuneração das Tarifas de Pouso e Permanência - RTAP e do Relatório de Remuneração das Tarifas de Armazenagem e Capatazia - RTAC, previstos no anexo 4 dos Contratos de Concessão nºs 001/ANAC/2019-Nordeste, 002/ANAC/2019-Centro-Oeste e 003/ANAC/2019-Sudeste.

#### CAPÍTULO I — DO RELATÓRIO DE REMUNERAÇÃO DAS TARIFAS DE EMBARQUE E CONEXÃO - RTEC

**Art. 2º** O RTEC deve contemplar os dados referentes aos voos cujas receitas associadas à cobrança ou estorno das tarifas de embarque e/ou conexão tenham sido reconhecidas, contabilmente, no mês de referência.

**Art. 3º** O RTEC deverá ser enviado à ANAC em arquivo eletrônico no formato de texto, extensão "csv", por meio do sistema Portal de Arquivos da ANAC, acessado pelo endereço eletrônico sistemas.anac.gov.br/portalarquivos, até o dia 25 do mês subsequente ao mês de referência do arquivo.

**Parágrafo único.** A ANAC poderá autorizar outro meio eletrônico de remessa dos dados distinto do previsto no caput deste artigo.

**Art. 4º** O RTEC será composto por um arquivo nomeado "EEEE-RTEC-AAAAMM", onde "EEEE" representa a sigla do aeroporto junto à OACI, "AAAA" representa os 4 (quatro) dígitos do ano, "MM" representa os 2 (dois) dígitos do mês de referência dos dados e "RTEC" é um rótulo das informações relativas ao Relatório de Remuneração das Tarifas de Embarque e Conexão.

**§ 1º** A primeira linha do conteúdo do arquivo deve ser preenchida pelos nomes dos campos, tais como descritos na coluna "DADO" da tabela presente no Anexo I desta Portaria, separados por ponto e vírgula (;), de forma a configurar o cabeçalho dos dados do arquivo.

**§ 2º** As demais linhas do arquivo deverão ser preenchidas pelas informações associadas a cada campo descrito nos incisos do art. 5º desta Portaria, sendo uma linha para cada lançamento contábil realizado no mês de referência dos dados.

**Art. 5º** O registro dos dados do RTEC deverá conter os seguintes campos, na exata ordem apresentada e delimitados por ";" (ponto e vírgula):

I - Campo 1 - COD\_RIMA: refere-se ao código de operação, que identifica uma determinada operação aeroportuária, desde o momento do toque da aeronave na pista de pouso até a decolagem, conforme constante na Portaria nº 1.017/SRA/SIA, de 26 de março de 2018, alterada pela Portaria nº 2176/SRA/SIA, de 17 de julho de 2019;

II - Campo 2 - OPERACAO\_ID: Refere-se ao código da operação, que identifica uma determinada operação aeroportuária, conforme constante no sistema de tarifação de passageiros do aeroporto.

III - Campo 3 - LANCAMENTO\_DESCRICAO: Refere-se à descrição do tipo de lançamento realizado, sendo 'COBRANCA' para novas cobranças ou complementações, ou 'ESTORNO' para estorno de lançamentos anteriores.

IV - Campo 4 - PAX\_TARIFADO\_EMBARQUE\_LOCAL: Refere-se à quantidade de passageiros de incidentes da tarifa de embarque, que iniciaram a viagem aérea neste voo no aeroporto. O formato é inteiro não negativo. Caso não haja passageiros incidentes da tarifa de embarque, utilizar '0';

V - Campo 5 - PAX\_TARIFADO\_CONEXAO\_DOMESTICA: Refere-se à quantidade de passageiros advindos de voos domésticos incidentes da tarifa de embarque ou conexão, que embarcaram no voo no aeroporto. O formato é inteiro não negativo. Caso não haja passageiros tarifados advindos de voos domésticos, utilizar '0';

VI - Campo 6 - PAX\_TARIFADO\_CONEXAO\_INTERNACIONAL: Refere-se à quantidade de passageiros advindos de voos internacionais incidentes da tarifa de embarque ou conexão, que embarcaram no voo no aeroporto. O formato é inteiro não negativo. Caso não haja passageiros tarifados advindos de voos internacionais, utilizar '0';

VII - Campo 7 - RECEITA\_EMBARQUE\_LOCAL: Refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa de embarque, aplicável aos passageiros que iniciam a viagem aérea no aeroporto. O formato é numérico com 2 (duas) casas decimais. Caso não haja passageiros incidentes da tarifa de embarque, utilizar '0';

VIII - Campo 8 - RECEITA\_CONEXAO\_DOMESTICA: Refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa de embarque ou conexão aplicável aos passageiros advindos de voos domésticos. O formato é inteiro não negativo. Caso não haja passageiros tarifados advindos de voos domésticos, utilizar '0';

IX - Campo 9 - RECEITA\_CONEXAO\_INTERNACIONAL: Refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa de embarque ou conexão aplicável aos passageiros advindos de voos internacionais. O formato é inteiro não negativo. Caso não haja passageiros tarifados advindos de voos internacionais, utilizar '0';

X - Campo 10 - COBRANCA\_EMBARQUE\_LOCAL: Refere-se à data de reconhecimento contábil da receita informada no Campo 7. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12) e AAAA representa o ano (ex. 2010);

XI - Campo 11 - COBRANCA\_CONEXAO\_DOMESTICA: Refere-se à data de reconhecimento contábil da receita informada no Campo 8. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12) e AAAA representa o ano (ex. 2010); e

XII - Campo 12 - COBRANCA\_CONEXAO\_INTERNACIONAL: Refere-se à data de reconhecimento contábil da receita informada no Campo 9. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12) e AAAA representa o ano (ex. 2010).

**§ 1º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de embarque, aplicável a passageiros que iniciam a viagem aérea no aeroporto, os campos 4 e 7 deverão ser preenchidos com '0', e o campo 10 deverá ser enviado vazio.

**§ 2º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de embarque ou conexão, aplicável aos passageiros advindos de conexão doméstica, os campos 5 e 8 deverão ser preenchidos com '0', e o campo 11 deverá ser enviado vazio.

**§ 3º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de embarque ou conexão, aplicável aos passageiros advindos de conexão internacional, os campos 6 e 9 deverão ser preenchidos com '0', e o campo 12 deverá ser enviado vazio.

**§ 4º** Nas situações de estorno da cobrança das tarifas de lançamentos ocorridos anteriormente, os valores das receitas, previstas nos Campos 7, 8 e 9 deverão ser negativos ou nulos, e o número de passageiros constante nos Campos 4, 5 e 6 deverão ser positivos ou nulos.

**§ 5º** Caso o aeroporto não possua política tarifária que diferencie os passageiros de embarque local dos passageiros em conexão de natureza distinta, ambos os valores poderão ser reportados como passageiros locais, no que se refere ao número de passageiros e à receita auferida.

#### CAPÍTULO II — DO RELATÓRIO DE REMUNERAÇÃO DAS TARIFAS DE POUSO E PERMANENCIA - RTAP

**Art. 6º** O RTAP deve contemplar os dados referentes aos voos cujas receitas associadas à cobrança ou estorno das tarifas de pouso e/ou permanência tenham sido reconhecidas, contabilmente, no mês de referência.

**Art. 7º** O RTAP deverá ser enviado à ANAC em arquivo eletrônico no formato de texto, extensão "csv", por meio do Sistema Portal de Arquivos da ANAC, acessado pelo endereço eletrônico sistemas.anac.gov.br/portalarquivos, até o dia 25 do mês subsequente ao mês de referência do arquivo.

**Parágrafo único.** A ANAC poderá autorizar outro meio eletrônico de remessa dos dados distinto do previsto no caput deste artigo.

**Art. 8º** O RTAP será composto por um arquivo nomeado "EEEE-RTAP-AAAAMM", onde "EEEE" representa a sigla do aeroporto junto à OACI, "AAAA" representa os 4 (quatro) dígitos do ano, "MM" representa os 2 (dois) dígitos do mês de referência dos dados e "RTAP" é um rótulo das informações relativas ao Relatório de Remuneração das Tarifas de Pouso e Permanência.

**§ 1º** A primeira linha do conteúdo do arquivo deve ser preenchida pelos nomes dos campos, tais como descritos na coluna "DADO" da tabela presente no Anexo II desta Portaria, separados por ponto e vírgula (;), de forma a configurar o cabeçalho dos dados do arquivo.

**§ 2º** As demais linhas do arquivo deverão ser preenchidas pelas informações associadas a cada campo descrito nos incisos do art. 9º desta Portaria, sendo uma linha para cada lançamento contábil realizado no mês de referência dos dados.

**Art. 9º** O registro dos dados do RTAP deverá conter os seguintes campos, na exata ordem apresentada e delimitados por ";" (ponto e vírgula):

I - Campo 1 - COD\_RIMA: refere-se ao código de operação, que identifica uma determinada operação aeroportuária, desde o momento do toque da aeronave na pista de pouso até a decolagem, conforme constante na Portaria nº 1.017/SRA/SIA, de 26 de março de 2018, alterada pela Portaria nº 2176/SRA/SIA, de 17 de julho de 2019;

II - Campo 2 - OPERACAO\_ID: Refere-se ao código da operação, que identifica uma determinada operação aeroportuária, conforme constante no sistema de tarifação de aeronaves do aeroporto.

III - Campo 3 - LANCAMENTO\_DESCRICAO: Refere-se à descrição do tipo de lançamento realizado, sendo 'COBRANCA' para novas cobranças ou complementações, ou 'ESTORNO' para estorno de lançamentos anteriores.

IV - Campo 4 - PMD: refere-se ao Peso Máximo de Decolagem, em toneladas, definido conforme informação constante do Certificado de Aeronavegabilidade da aeronave ou outro documento que o substitua. O formato é numérico com 3 (três) casas decimais.

V - Campo 5 - AERONAVE\_GRUPO: refere-se ao Grupo da aeronave ao pousar no aeroporto. O formato é numérico e é representado por:

a) 1, para operações do Grupo I;

b) 2, para operações do Grupo II.

VI - Campo 6 - NMIN\_MANOBRAS: refere-se ao número de minutos tarifados relativos à permanência em pátio de manobras. O formato é numérico e é representado por número inteiro não negativo. Caso não se aplique, utilizar '0';

VII - Campo 7 - NMIN\_ESTADIA: refere-se ao número de minutos tarifados relativos à permanência em pátio de estadia. O formato é numérico e é representado por número inteiro não negativo. Caso não se aplique, utilizar '0';

VIII - Campo 8 - RPO: refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa de pouso de aeronave do Grupo I que pousou no aeroporto. O formato é numérico com 2 (duas) casas decimais. Caso o voo seja de aeronave do Grupo II, utilizar '0';

IX - Campo 9 - RU: refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa unificada de embarque e pouso de aeronave do Grupo II que pousou no aeroporto. O formato é numérico com 2 (duas) casas decimais. Caso o voo seja de aeronave do Grupo I, utilizar '0';

X - Campo 10 - RPM\_GRUPO\_I: refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa de permanência em pátio de manobra de aeronave do Grupo I que pousou no aeroporto. O formato é numérico com 2 (duas) casas decimais. Caso o voo seja de aeronave do Grupo II, utilizar '0';

XI - Campo 11 - RPE\_GRUPO\_I: refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa de permanência em pátio de estadia de aeronave do Grupo I que pousou no aeroporto. O formato é numérico com 2 (duas) casas decimais. Caso o voo seja de aeronave do Grupo II, utilizar '0';

XII - Campo 12 - RPM\_GRUPO\_II: refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa de permanência em pátio de manobra de aeronave do Grupo II que pousou no aeroporto. O formato é numérico com 2 (duas) casas decimais. Caso o voo seja de aeronave do Grupo I, utilizar '0';

XIII - Campo 13 - RPE\_GRUPO\_II: refere-se ao valor, em R$ (reais), correspondente à receita reconhecida, contabilmente, em função da cobrança da tarifa de permanência em pátio de estadia de aeronave do Grupo II que pousou no aeroporto. O formato é numérico com 2 (duas) casas decimais. Caso o voo seja de aeronave do Grupo I, utilizar '0';

XIV - Campo 14 - POUSO\_COBRANCA\_DATA: refere-se à data de reconhecimento, contábil, da receita da tarifa de pouso de aeronave do Grupo I ou da tarifa unificada de embarque e pouso de aeronave do Grupo II. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010);

XV - Campo 15 - PERMANENCIA\_COBRANCA\_DATA: refere-se à data de reconhecimento, contábil, da receita da tarifa de permanência, de aeronaves do Grupo I ou Grupo II, em pátio de manobras ou em pátio de estadia. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010); e

XVI - Campo 16 - ISENCAO\_POUSO: refere-se à informação sobre a existência de isenção legal à cobrança de tarifa de pouso na operação aeroportuária, devendo ser preenchido com a seguinte codificação:

a) 1, ou vazio, se houver isenção na tarifa de pouso, aplicável a operações do Grupo I, ou na tarifa unificada de embarque e pouso, aplicável a operações do Grupo II; e

b) 0, caso não haja isenção na tarifa de pouso, aplicável a operações do Grupo I, ou na tarifa unificada de embarque e pouso, aplicável a operações do Grupo II.

**§ 1º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de pouso do Grupo I, o campo 8 deverá ser preenchido com '0'.

**§ 2º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa unificada de embarque e pouso do Grupo II, o campo 9 deverá ser preenchido com '0'.

**§ 3º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de pouso de Grupo I ou da tarifa unificada de embarque e pouso do Grupo II, o campo 14 deverá ser informado vazio.

**§ 4º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de permanência em pátio de manobra de aeronave do Grupo I, o campo 10 deverá ser informado vazio.

**§ 5º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de permanência em pátio de estadia de aeronave do Grupo I, o campo 11 deverá ser informado vazio.

**§ 6º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de permanência em pátio de manobra de aeronave do Grupo II, o campo 12 deverá ser informado vazio.

**§ 7º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente à tarifa de permanência em pátio de estadia de aeronave do Grupo II, o campo 13 deverá ser informado vazio.

**§ 8º** Caso o lançamento informado não reporte uma nova cobrança, estorno ou complementação da receita correspondente às tarifas de permanência, o campo 15 deverá ser informado vazio.

**Art. 10.** O administrador aeroportuário deverá seguir sistemática de estorno que possibilite a identificação objetiva e automática dos valores de PMD e da diferenciação entre desconto e isenção legal existente na tarifa de pouso para cada operação aeroportuária.

**Parágrafo único.** Recomenda-se que nas situações de estorno da cobrança da tarifa de pouso, ou da tarifa unificada de embarque e pouso, ou das tarifas de permanência, de aeronaves do Grupo I ou Grupo II, em pátio de manobras e/ou em pátio de estadia, de lançamentos ocorridos anteriormente, os valores das receitas, previstas nos Campos 8 a 13, respectivamente, sejam negativos e, em módulo, iguais aos valores das receitas do lançamento anterior; e o valor do PMD, previsto no Campo 4, e do identificador da isenção de pouso, previsto no Campo 16, sejam iguais ao do lançamento estornado

#### CAPÍTULO III — DO RELATÓRIO DE REMUNERAÇÃO DAS TARIFAS DE ARMAZENAGEM E CAPATAZIA - RTAC

**Art. 11.** O RTAC deve contemplar os dados referentes às cargas cuja saída do TECA tenha ocorrido no mês de referência.

**Art. 12.** O RTAC deve ser enviado à ANAC em arquivo eletrônico no formato de texto, extensão "csv", por meio do Sistema Portal de Arquivos da ANAC, acessado pelo endereço eletrônico https://sistemas.anac.gov.br/PortalArquivos, em até 5 dias úteis de solicitação realizada pela ANAC, salvo expressa disposição em contrário.

**Parágrafo único.** A ANAC poderá autorizar outro meio eletrônico de remessa dos dados distinto do previsto no caput deste artigo.

**Art. 13.** O nome do arquivo eletrônico do RTAC será composto por "EEEE-RTAC-AAAAMM", onde "EEEE" representa a sigla do aeroporto junto à OACI, "AAAA" representa os 4 (quatro) dígitos do ano, "MM" representa os 2 (dois) dígitos do mês de referência das informações e "RTAC" é um rótulo das informações relativas ao Relatório de Remuneração das Tarifas de Armazenagem e Capatazia.

**§ 1º** A primeira linha do conteúdo do arquivo deve ser preenchida pelos nomes dos campos, tais como descritos na coluna "DADO" da tabela presente no Anexo III desta Portaria, separados por ponto e vírgula (;), de forma a configurar o cabeçalho dos dados do arquivo.

**§ 2º** As demais linhas do arquivo deverão ser preenchidas pelas informações associadas a cada campo descrito nos incisos do art. 14 desta Portaria, sendo uma linha para cada carga retirada do TECA no mês de referência dos dados.

**Art. 14.** O registro dos dados do RTAC deverá conter os seguintes campos, na exata ordem apresentada e delimitados por ";" (ponto e vírgula):

I - Campo 1 - CARGA\_ID: refere-se ao código identificador da carga, que deverá ser único para cada carga.

II - Campo 2 - CARGA\_TIPO: representa a classificação tarifária da carga, devendo ser preenchido com o número da tabela relativa às Tarifas de Armazenagem e Capatazia do anexo de Tarifas do Contrato de Concessão, para as Concessionárias cujos contratos possuam essa classificação por tabelas, ou, caso contrário, a codificação constante no sistema aeroportuário, que deverá separar as cargas importadas e exportadas em trânsito das demais modalidades de cargas.

III - Campo 3 - PESO\_BRUTO: representa o peso bruto, em quilogramas, da carga. O formato é numérico, com até 3 (três) casas decimais;

IV - Campo 4 - PESO\_LIQUIDO: representa o peso líquido, em quilogramas, da carga. O formato é numérico, com até 3 (três) casas decimais;

V - Campo 5 - CIF: representa o valor CIF da carga. O formato é numérico, com até 2 (duas) casas decimais;

VI - Campo 6 - FOB: representa o valor FOB da carga. O formato é numérico, com até 2 (duas) casas decimais;

VII - Campo 7 - DT\_ENTRADA: representa a data de admissão da carga no TECA. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010);

VIII - Campo 8 - HH\_ENTRADA: representa o horário de admissão da carga no TECA, conforme horário local do aeroporto. O formato é hora e é representado por HH:MM, onde HH representa a hora (00 - 23) e MM representa os minutos (00 - 59). Ambos devem possuir 2 (dois) caracteres e ser informados no padrão 24 (vinte e quatro) horas;

IX - Campo 9 - DT\_SAIDA: representa a data de remoção da carga do TECA. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010);

X - Campo 10 - HH\_SAIDA: representa o horário de remoção da carga do TECA, conforme horário local do aeroporto. O formato é hora e é representado por HH:MM, onde HH representa a hora (00 - 23) e MM representa os minutos (00 - 59). Ambos devem possuir 2 (dois) caracteres e ser informados no padrão 24 (vinte e quatro) horas;

XI - Campo 11 - DIAS\_ARMAZENAGEM: representa o número de dias considerados para o cálculo da remuneração da tarifa de armazenagem. O formato é inteiro não negativo. Caso não haja cobrança da tarifa de armazenagem, utilizar '0';

XII - Campo 12 - REMUNERACAO\_ARMAZENAGEM: representa o valor reconhecido contabilmente em função da tarifa de armazenagem. O formato é numérico, com até 2 (duas) casas decimais;

XIII - Campo 13 - REMUNERACAO\_CAPATAZIA: representa o valor reconhecido contabilmente em função da tarifa de capatazia. O formato é numérico, com até 2 (duas) casas decimais;

XIV - Campo 14 - ARMAZENAGEM\_COBRANCA\_DATA: representa a data de reconhecimento contábil da tarifa de armazenagem. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010);

XV - Campo 15 - CAPATAZIA\_COBRANCA\_DATA: representa a data de reconhecimento contábil da tarifa de capatazia. O formato é data e é representado por DD/MM/AAAA, no qual DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010); e

XVI - Campo 16 - DRAWBACK\_RECOF - indica se a carga se enquadra nos casos de: (i) cargas importadas com o benefício de "Drawback"; ou (ii) cargas importadas liberadas na modalidade de Regime Aduaneiro Especial de Entreposto Industrial sob Controle Informatizado (RECOF). Deve ser preenchido com '1' caso verdadeiro, e '0' caso falso.

**§ 1º** Nas situações em que não haja cobrança de tarifa de armazenagem, o Campo 12 deverá ser preenchido com '0' (zero) e o Campo 14 deverá ser enviado vazio.

**§ 2º** Nas situações em que não haja cobrança de tarifa de capatazia, o Campo 13 deverá ser preenchido com '0' (zero) e o Campo 15 deverá ser enviado vazio.

#### CAPÍTULO IV — DAS DISPOSIÇÕES FINAIS

**Art. 15.** Situações não previstas nesta Portaria deverão ser objeto de consulta à Gerência de Informações e Contabilidade - GEIC da Superintendência de Regulação Econômica de Aeroportos - SRA.

**Art. 16.** Os Anexos desta Portaria encontram-se disponíveis no Boletim de Pessoal e Serviço - BPS desta Agência (endereço eletrônico https://www.anac.gov.br/assuntos/legislacao/legislacao-1/boletim-de-pessoal/) e igualmente disponíveis em sua página "Legislação" (endereço eletrônico https://www.anac.gov.br/assuntos/legislacao).

**Art. 17.** Esta Portaria entra em vigor na data de sua publicação.

TIAGO SOUSA PEREIRA
