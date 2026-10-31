---
titulo: "PORTARIA Nº 18.340, DE 2 DE DEZEMBRO DE 2025"
orgao: "Ministério de Portos e Aeroportos/Agência Nacional de Aviação Civil/Superintendência de Acompanhamento de Serviços Aéreos"
tipo: "Portaria"
numero: "18340"
data: 2025-12-02
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 09/12/2025, seção 1, p. 104"
data_publicacao: 2025-12-09
edicao: "234"
fonte: "https://www.in.gov.br/web/dou/-/portaria-n-18.340-de-2-de-dezembro-de-2025-673956739"
baixado_em: 2026-10-16
sha256_html_fonte: 5d70c2f6cd5556a13a9c2eacd66e4e08aecfc484e1ff366bc6d009a5649b93d6
---
# PORTARIA Nº 18.340, DE 2 DE DEZEMBRO DE 2025

PORTARIA Nº 18.340, DE 2 DE DEZEMBRO DE 2025

O SUPERINTENDENTE DE ACOMPANHAMENTO DE SERVIÇOS AÉREOS, no uso da atribuição que lhe confere o art. 32, inciso V, do Regimento Interno, aprovado pela Resolução nº 381, de 14 de junho de 2016, tendo em vista o disposto no art. 2º da Resolução nº 780, de 16 de outubro de 2025, e considerando o que consta do processo nº 00058.054468/2023-53, resolve:

**Art. 1º** Estabelecer os procedimentos para o registro e a divulgação dos dados de tarifas aéreas comercializadas referentes aos serviços de transporte aéreo doméstico de passageiros com oferta pública de assentos.

**Parágrafo único.** Para os fins desta Portaria, a sigla RDT corresponde ao Registro de Dados das Tarifas Aéreas Domésticas Comercializadas.

#### CAPÍTULO I — DAS DISPOSIÇÕES GERAIS

**Art. 2º** O RDT é obrigatório para os transportadores que ofertem os serviços de transporte aéreo doméstico de passageiros com oferta pública de assentos.

**Parágrafo único.** Ainda que a operação de transporte seja conduzida por terceiros, o registro ficará a cargo do transportador responsável pela comercialização.

**Art. 3º** O RDT tem por objetivo propiciar o acompanhamento da evolução do preço dos serviços de transporte aéreo doméstico de passageiros, com base nos dados das passagens comercializadas.

#### CAPÍTULO II — DO OBJETO DO REGISTRO

**Art. 4º** Constituirá objeto do RDT:

I - dados das tarifas aéreas domésticas comercializadas ao público em geral, exceto se ofertadas com descontos individuais, exclusivos ou diferenciados, não disponíveis a esse público; e

II - quantitativo de passagens aéreas emitidas com condições diferenciadas, ou seja, com descontos individuais, exclusivos ou específicos, não disponíveis ao público em geral, conforme disposto no art. 5º, incisos II ao V.

**§ 1º** A obrigação prevista no caput restringe-se aos dados das passagens aéreas cujos voos necessitam de registro prévio no Sistema de Registro de Operações da ANAC, ou outro que venha a substituí-lo, independentemente do local e dos meios empregados para efetivar a comercialização.

**§ 2º** Não deverão compor o registro:

I - as tarifas aéreas referentes às passagens reemitidas;

II - as tarifas aéreas referentes às etapas domésticas das passagens internacionais comercializadas; e

III - os dados das passagens aéreas que tenham sido comercializadas, porém canceladas.

**Art. 5º** Os dados que constituem objeto do RDT deverão ser classificados nos seguintes grupos:

I - grupo I: tarifas aéreas comercializadas ao público em geral, exceto se ofertadas com descontos individuais, exclusivos ou diferenciados, não disponíveis a esse público;

II - grupo II: quantidade de passagens aéreas emitidas com descontos exclusivos para crianças, acompanhantes, idosos, empregados do transportador ou similares, desde que vinculadas a alguma especificidade intrínseca do passageiro;

III - grupo III: quantidade de passagens aéreas emitidas com descontos exclusivos para grupos de passageiros, acordos corporativos ou similares, não disponíveis ao público em geral;

IV - grupo IV: quantidade de passagens aéreas emitidas com descontos exclusivos vinculados a programas de milhagem, fidelização ou similares, não disponíveis ao público em geral; e

V - grupo V: quantidade de gratuidades.

**§ 1º** Os dados referentes às tarifas aéreas comercializadas ao público em geral, com descontos disponíveis a qualquer usuário do transporte aéreo, deverão ser classificados no grupo I.

**§ 2º** Os dados referentes às tarifas aéreas comercializadas por agências de viagens ou congêneres, atuando como prepostos dos transportadores, deverão ser classificados nos grupos I a V, de acordo com as características de cada passagem emitida.

**Art. 6º** O valor do registro deverá corresponder exclusivamente ao valor referente ao serviço de transporte aéreo do passageiro constante da passagem.

**Parágrafo único.** O valor do registro não deverá considerar outros valores discriminados na passagem aérea, tais como os relativos aos serviços opcionais ofertados pelo transportador, assim como os relativos ao pagamento das taxas governamentais, impostos, tarifas aeroportuárias ou quaisquer valores que apresentem característica de repasse a entes governamentais.

#### CAPÍTULO III — DA ESTRUTURA DO ARQUIVO

**Art. 7º** O arquivo do RDT deverá ser elaborado no formato texto, com codificação ANSI e extensão ".txt".

**Art. 8º** O nome do arquivo deverá ser composto pela sigla "RDT", seguida do designador ICAO de 3 (três) letras do transportador responsável pelo registro, do ano e mês de referência do registro, no formato AAAAMM, e da data de transmissão do arquivo, no formato AAAAMMDD.

**Art. 9º** O arquivo deverá englobar os dados a seguir, delimitados pelo caractere ";" (ponto e vírgula), sem espaços em branco:

I - identificação do transportador responsável pelo registro e do período de referência, a serem reportados na primeira linha do arquivo;

II - dados das tarifas aéreas comercializadas ao público em geral, a serem reportados após os dados do inciso I do caput; e

III - dados das passagens aéreas emitidas com condições diferenciadas, a serem reportados após os dados referentes ao inciso II do caput.

**Art. 10.** Os dados das tarifas aéreas comercializadas ao público em geral deverão englobar as seguintes informações:

I - indicador do grupo da tarifa aérea comercializada ao público em geral, correspondente ao identificador do art. 5º, inciso I;

II - designador ICAO do aeroporto de origem;

III - designador ICAO do aeroporto de destino;

IV - valor da tarifa aérea comercializada; e

V - quantidade de assentos comercializados.

**Parágrafo único.** Cada trecho de origem/destino constante da passagem aérea deverá ser reportado no arquivo, sem considerar as escalas ou conexões realizadas.

**Art. 11.** Os dados das passagens aéreas emitidas com condições diferenciadas deverão englobar as seguintes informações:

I - indicador do grupo da passagem aérea comercializada com condições diferenciadas, correspondente ao art. 5º, incisos II ao V;

II - designador ICAO do aeroporto de origem;

III - designador ICAO do aeroporto de destino; e

IV - quantidade de assentos comercializados.

**Parágrafo único.** Cada trecho de origem/destino constante da passagem aérea deverá ser reportado no arquivo, sem considerar as escalas ou conexões realizadas.

**Art. 12.** A estrutura do arquivo deverá observar as especificações disponibilizadas no Manual de Registro de Dados de Tarifas Aéreas.

#### CAPÍTULO IV — DO ENVIO DO ARQUIVO

**Art. 13.** O arquivo contendo os dados das tarifas aéreas comercializadas no mês de referência deverá ser enviado à ANAC por meio do sistema disponibilizado pela Agência, até o dia 10 (dez) do mês subsequente.

**Parágrafo único.** Caso o vencimento do prazo estabelecido no caput ocorra em sábados, domingos ou feriados, considerar-se-á o primeiro dia útil seguinte.

**Art. 14.** Antes do vencimento do prazo estabelecido no art. 13, o transportador responsável pelo registro deverá consultar o resultado do processamento do arquivo e retificar os erros identificados.

**Art. 15.** O arquivo deverá ser enviado à ANAC conforme instruções disponibilizadas no Manual de Registro de Dados de Tarifas Aéreas.

#### CAPÍTULO V — DA FISCALIZAÇÃO

**Art. 16.** Após o recebimento do arquivo, a ANAC iniciará a fiscalização dos dados enviados pelo transportador.

**Parágrafo único.** O transportador será comunicado pela ANAC do resultado da fiscalização a que se refere o caput.

**Art. 17.** O transportador deverá avaliar as críticas formuladas pela fiscalização e apresentar, no prazo de 5 (cinco) dias úteis contados do requerimento da ANAC, o Relatório de Justificativas contendo esclarecimentos que fundamentem a adequabilidade dos dados.

**Parágrafo único.** Os erros apontados pelas críticas, identificados pela análise do transportador, deverão ser retificados dentro do prazo estipulado no caput.

**Art. 18.** Visando à verificação da consistência e da precisão dos dados registrados, a ANAC poderá requisitar documentos, comprovantes de passagens aéreas comercializadas, informações ou esclarecimentos, a serem apresentados no prazo de 3 (três) dias úteis contados do requerimento.

**Art. 19.** Os pedidos de retificação do arquivo requisitados pela ANAC deverão ser atendidos no prazo de 3 (três) dias úteis contados do requerimento.

**Art. 20.** O transportador responsável pelo registro deverá assegurar a disponibilidade das informações de todas as passagens aéreas comercializadas pelo prazo de 5 (cinco) anos, de forma a possibilitar a fiscalização dos dados registrados.

**Art. 21.** O descumprimento do disposto nessa Portaria poderá ensejar a aplicação de providências administrativas, conforme instruções regulamentadas pela ANAC.

**Art. 22.** Os prazos estabelecidos no Capítulo V poderão ser prorrogados, a critério da Gerência responsável pela fiscalização dos dados registrados, mediante solicitação devidamente fundamentada, acompanhada da exposição dos motivos que justifiquem o pedido.

**Art. 23.** Os transportadores deverão observar as instruções relacionadas à fiscalização disponibilizadas no Manual de Registro de Dados de Tarifas Aéreas.

#### CAPÍTULO VI — DA PUBLICAÇÃO

**Art. 24.** As tarifas aéreas registradas na ANAC serão divulgadas na página internet da Agência.

**§ 1º** As tarifas aéreas comercializadas ao público em geral serão estruturadas e publicadas em um painel de dados.

**§ 2º** Os microdados serão disponibilizados em formato bruto.

**Art. 25.** As informações relativas à divulgação dos dados de tarifas aéreas registradas na ANAC estarão disponíveis no Manual de Registro de Dados de Tarifas Aéreas.

#### CAPÍTULO VI — DAS DISPOSIÇÕES FINAIS

**Art. 26.** O manual a que se refere esta Portaria encontra-se disponível na página internet da ANAC, no local destinado às informações sobre Tarifas Aéreas.

**Art. 27.** Ficam revogadas:

I - a Portaria nº 2.923/SAS, de 27 de outubro de 2016, publicada no Diário Oficial da União de 4 de novembro de 2016, Seção 1, página 83; e

II - a Portaria nº 12.719/SAS, de 5 de outubro de 2023, publicada no Boletim de Pessoal e Serviço - BPS v.18, nº 41, de 9 a 13 de outubro de 2023.

**Art. 28.** Esta Portaria entra em vigor em 1º de fevereiro de 2026.

ADRIANO PINTO DE MIRANDA
