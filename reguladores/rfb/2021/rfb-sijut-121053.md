---
titulo: "Portaria Coana nº 28, de 30 de julho de 2021"
orgao: "Coordenação-Geral de Administração Aduaneira"
tipo: "Portaria"
numero: "28"
data: "2021-07-30"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 18/10/2021, seção 1, página 21"
data_publicacao: "2021-10-18"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/121053/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/121053/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "121053"
sha256_texto: "ca55b932487c5714c4d6a12690c69427a71f045691827ee9e5792ccf1ceff92d"
baixado_em: "2026-10-16"
---
# Portaria Coana nº 28, de 30 de julho de 2021

Altera a Portaria Coana nº 5, de 24 de fevereiro de 2021, que regulamenta a simplificação dos procedimentos de trânsito aduaneiro por meio de gestão de riscos e estabelece os requisitos para monitoramento de veículos terrestres.

O COORDENADOR-GERAL DE ADMINISTRAÇÃO ADUANEIRA, no uso das atribuições que lhe conferem o art. 147 e o inciso II do art. 358 do Regimento Interno da Secretaria Especial da Receita Federal do Brasil, aprovado pela Portaria ME nº 284, de 27 de julho de 2020, e tendo em vista o disposto nos incisos XIII e XIV do art. 81 da Instrução Normativa SRF nº 248, de 25 de novembro de 2002, com redação dada pela Instrução Normativa nº 1980, de 30 de setembro de 2020, resolve:

**Art. 1º** Os artigos 6º e 7º da Portaria Coana nº 5, de 24 de fevereiro de 2021, passam a vigorar com a seguinte redação:

“Art. 6º A simplificação dos procedimentos de trânsito aduaneiro será concedida em caráter precário por meio de Ato Declaratório Executivo (ADE) do Superintendente Regional ou, no caso de dispensa de etapa inter-regional, por ADE conjunto dos Superintendentes das Regiões Fiscais envolvidas.

**§ 1º** É facultado aos ADE de deferimento a vinculação da dispensa de etapas ao uso de determinadas rotas, tipos de veículos, tipos de carrocerias, à existência de sistema de monitoramento, nos termos do Anexo II desta Portaria, e à possibilidade e forma de acesso ao sistema de monitoramento dos veículos em tempo real.

..............................................................................................................................................

**§ 4º** O ADE de deferimento poderá estipular período de testes para avaliar a segurança das operações com dispensa de etapas.

**Art. 7º** Concedida a simplificação do trânsito aduaneiro, o beneficiário deverá, para cada operação, anexar o relatório da rota percorrida, conforme o item 9 do Anexo I desta Portaria, com as modificações do item 7 do Anexo II, se este for exigido, no dossiê de instrução da declaração, em até 24 (vinte e quatro) horas após a chegada do veículo no destino, por meio da funcionalidade “Anexação de Documentos Digitalizados” do Portal Único de Comércio Exterior (Pucomex), autenticado com uso de certificado digital, observada a legislação específica.

**Parágrafo único.** As unidades de origem e destino dos trânsitos rodoviários poderão solicitar ao transportador, sempre que entenderem necessário, informações adicionais da viagem.” (NR)

**Art. 2º** Os Anexos I e II da Portaria Coana nº 5, de 2021, ficam substituídos pelos Anexos I e II desta Portaria.

**Art. 3º** Esta Portaria entra em vigor no dia 1º de novembro de 2021.

JACKSON ALUIR CORBARI

## ANEXO I

Novo segmento

Requisitos mínimos para Sistema de Monitoramento de Veículos

I. Glossário

Para efeitos deste Anexo, entende-se por:

Datas: as datas devem ser armazenadas e exibidas sempre no formato YYYYMMDD, conforme definido pela norma ISO-8601. Por exemplo, o primeiro dia do mês de janeiro do ano de 2015 deve ser representado como 20150101.

Fuso horário: deve sempre corresponder ao fuso oficial de Brasília no sistema UTC, de 3 (três) horas a menos que a hora oficial do meridiano de Greenwich (GMT) ou, nos pontos e períodos em que o horário de verão estiver oficialmente em uso, de 2 (duas) horas a menos que a hora oficial do GMT.

Georreferenciamento de área: é o mapeamento de uma determinada área referenciando os vértices de seu perímetro a um Sistema Geodésico especificado, definindo sua área e sua posição geográfica. Para os fins deste Anexo o Sistema Geodésico será o WGS84.

Georreferenciamento de rota: é o mapeamento de uma determinada rota referenciando os vértices de seus pontos principais a um Sistema Geodésico especificado, definindo sua composição frente ao referencial adotado, de forma a permitir a repetição, a qualquer tempo. Para os fins deste Anexo o Sistema Geodésico será o WGS84.

GMT: sigla para Greenwich Mean Time. É conhecido como o marcador oficial de tempo. O fuso horário é contabilizado a partir do meridiano de Greenwich: para oeste, o fuso é negativo; para leste, positivo.

GNSS: sigla para Global Navigation Satellite System. Sistema de posicionamento global por satélite; permite determinar a posição geográfica em um sistema preestabelecido de coordenadas.

Horas: as horas devem ser armazenadas e exibidas sempre associadas a uma data, no formato YYYYMMDDThh:mm:ss-03:00, conforme definido pela norma ISO-8601. Por exemplo, o início do primeiro dia do mês de janeiro do ano de 2015 deve ser representado como 20150101T00:00:00-03:00.

ISO: sigla para International Organization for Standardization ou Organização Internacional de Normalização, com sede em Genebra, na Suíça. Foi criada em 1946 e tem como associados organismos de normalização de cerca de 160 (cento e sessenta) países. A ISO tem como objetivo criar normas que facilitem o comércio e promovam boas práticas de gestão e o avanço tecnológico, além de disseminar conhecimentos.

RASTREADOR: equipamento instalado nos veículos que permite detectar sua posição em um Sistema Geodésico especificado utilizando dados recebidos de algum sistema GNSS. Opcionalmente o RASTREADOR pode coletar dados do veículo, como o estado de portas, tampas, quantidade de combustível ou ainda permitir ações remotas como o destravamento de portas ou mesmo a interrupção de funcionamento.

SMV: sigla para Sistema de Monitoramento de Veículos. Conjunto de equipamentos e softwares necessários para receber os dados enviados pelos RASTREADORES instalados nos veículos e analisá-los em comparação a um sistema predeterminado de mapas e coordenadas.

WGS84: sigla para World Geodetic System 1984, sistema de referência terrestre desenvolvido pelo Departamento de Defesa dos Estados Unidos da América e utilizado, por exemplo, pelo sistema GPS.

Unidades de Transporte:

Recipientes com um volume interior de, pelo menos, 1 (um) metro cúbico, incluindo aqueles de estrutura desmontável;

Veículos rodoviários apropriados ao transporte de mercadorias, incluindo os reboques e semirreboques;

Vagões, incluindo aqueles com a face superior aberta e recoberta por lona ou assemelhados;

Barcaças e outras embarcações; e

Aeronaves.

Sensor: dispositivo capaz de detectar a mudança no estado de um componente do sistema. Por exemplo, os sensores de portas capazes de identificar quando são abertas ou fechadas.

Carroceria tipo baú: compartimento de carga fechado em todos os lados de forma a oferecer proteção física à carga em seu interior. Todas as eventuais aberturas (portas e respiradores) são feitas com material semelhante (em resistência mecânica) ao restante e devem permitir a colocação de trancas, lacres ou cadeados que impeçam sua abertura não intencional.

Latitude: distância em graus de qualquer ponto da superfície terrestre em relação à linha do Equador. A latitude poder ser Norte (N) ou Sul (S) e vai de 0º até 90º. Sempre que solicitado poderá ser informada nos formatos:

Graus, minutos e segundos (DMS, na sigla em inglês): 41°24'12.2"N 2°10'26.5"E

Graus e minutos decimais (DMM, na sigla em inglês): 41 24.2028, 2 10.4418

Graus decimais (DD, na sigla em inglês): 41.40338, 2.17403

Longitude: distância em graus de qualquer ponto da Terra em relação ao meridiano de Greenwich. A longitude pode ser Leste (L) ou Oeste (O) e vai de 0º a 180º. Sempre que solicitado poderá ser informada nos formatos:

Graus, minutos e segundos (DMS, na sigla em inglês): 41°24'12.2"N 2°10'26.5"E

Graus e minutos decimais (DMM, na sigla em inglês): 41 24.2028, 2 10.4418

Graus decimais (DD, na sigla em inglês): 41.40338, 2.17403

II. Generalidades

1\. A utilização de RASTREADORES em conjunto com o SMV pretende:

1.1. Satisfazer os requisitos de segurança exigidos pela RFB para a movimentação de cargas sob controle aduaneiro, detectar mudanças de rotas e aferir o cumprimento dos prazos das operações;

1.2. Permitir o monitoramento ponto a ponto, em períodos e/ou distâncias predeterminados, da posição dos veículos envolvidos em cada operação; e

1.3. Informar as coordenadas geográficas e as ocorrências durante todo seu deslocamento físico e temporal.

2\. A RFB realizará operações de controle e monitoramento dos movimentos das Unidades de Transporte, de acordo com normas, protocolos e regulamentação definidos em cada caso.

III. Do RASTREADOR

3\. O RASTREADOR deve apresentar, pelo menos, estas características:

3.1. Ser capaz de determinar sua posição georreferencial através de informação obtida de algum sistema de posicionamento global por satélite (GNSS);

3.2. Ser capaz de obter data e hora diretamente do sistema GNSS utilizado. Na impossibilidade de obter os dados da rede GNSS, deverá utilizar os dados do relógio interno;

3.3. Ser capaz de armazenar os dados de posicionamento e aqueles gerados pelos sensores durante todo o percurso;

3.4. Ser capaz de transmitir periodicamente os dados armazenados;

3.5. Contar com bateria que permita manter seu funcionamento enquanto não puder obter energia elétrica do veículo onde está instalado; e

3.6. Ser capaz de obter alimentação (de energia elétrica) diretamente do veículo onde está instalado, de forma a recarregar a bateria interna e manter o dispositivo funcionando plenamente por tempo indeterminado.

4\. O RASTREADOR deve ter a capacidade de enviar pacotes de mensagens, cada mensagem contendo pelo menos a informação georreferencial de sua posição.

4.1. A transmissão dos pacotes de mensagens deve ser feita através de um sistema de comunicação celular, satelital ou outro disponível adequado a tal fim.

5\. O intervalo máximo para a coleta dos dados de posicionamento do veículo (georeferenciamento) pelo RASTREADOR é de 10 (dez) minutos.

6\. O intervalo máximo entre as transmissões de mensagens será de 20 (vinte) quilômetros ou 30 (trinta) minutos.

7\. Diante de qualquer motivo técnico que impeça a conexão entre o RASTREADOR e o SMV, uma vez restabelecida a comunicação, toda a informação não enviada deverá ser transmitida imediatamente, em ordem cronológica, sem duplicações ou faltas.

IV. Do SMV

8\. O SMV deve ser capaz de tratar os dados recebidos dos RASTREADORES, incluindo os eventos de desvios de rota e paradas não previstas.

8.1. Independentemente de outras funcionalidades, o SMV deverá possuir as seguintes características:

8.1.1. Exigir cadastro prévio e senha para acesso;

8.1.2. Gerar e manter arquivo “de log” com os acessos de cada usuário;

8.1.3. Montar cercas virtuais e identificar os RASTREADORES que desrespeitarem as cercas a eles atribuídas;

8.1.4. Estabelecer um tempo máximo para a rota a ser percorrida pelo RASTREADOR e controlar o seu cumprimento;

8.1.5. Localizar e exibir um RASTREADOR usando como argumento de pesquisa:

• Placa do veículo motorizado (cavalo);

• Placa do reboque;

• Origem da movimentação; e

• Destino da movimentação;

8.1.6. Emitir alertas sempre que o sistema identificar que um RASTREADOR tiver excedido o tempo máximo estipulado para a rota prevista;

8.1.7. Emitir alertas sempre que o sistema identificar que um RASTREADOR estiver em deslocamento fora da rota prevista;

8.1.8. Permitir o envio de e-mails, mensagens de texto (SMS) ou outra forma de comunicação eletrônica, para diversos destinatários, sempre que algum alerta for emitido; e

8.1.9. Permitir acesso remoto, através da internet e usando qualquer navegador (browser) disponível no mercado, sem exigir a instalação de qualquer componente adicional, proprietário ou não.

8.1.9.1. O acesso remoto ao SMV deve apresentar o mesmo nível de segurança do acesso “local”, obedecendo, inclusive, ao disposto nos itens 8.1.1 e 8.1.2 deste Anexo.

V. Do Relatório

9\. Para cada viagem, o SMV deverá gerar relatório da rota percorrida.

9.1. O relatório deve ser entregue à RFB em formato texto, sem figuras ou outros elementos.

9.2. Cada linha do relatório deve apresentar o horário e as coordenadas dos pontos em que o RASTREADOR aferiu a posição.

## ANEXO II

Novo segmento

Requisitos adicionais para Sistema de Monitoramento de Veículos

I. Objetivo

Este Anexo complementa o Anexo I, adicionando características ao RASTREADOR e ao SMV para permitir o monitoramento das portas do compartimento de carga mediante o uso de sensores.

II. Generalidades

1\. A adição de sensores aos RASTREADORES em conjunto com as alterações no SMV pretende possibilitar o monitoramento do estado de determinados pontos, especialmente as portas do compartimento de carga, além de fornecer relatórios sobre estes estados durante as operações.

2\. As características abaixo devem ser acrescidas àquelas descritas no Anexo I.

III. Do RASTREADOR

3\. O RASTREADOR deve ser capaz de conectar-se com tantos sensores quantos necessários para monitorar o estado de todas as aberturas do compartimento de carga.

3.1. Cada sensor conectado deve receber um código único para que suas informações possam ser monitoradas de forma individualizada.

3.2. Cada sensor conectado deve receber uma descrição indicando qual ponto do compartimento de carga está sendo monitorado.

4\. A instalação do RASTREADOR em veículo com carroceria do tipo baú deve garantir que todas as aberturas do compartimento de carga sejam dotadas de sensores monitorados.

5\. Os pacotes de mensagens enviados pelo RASTREADOR devem conter informações sobre o estado de todos os sensores monitorados.

5.1. Sempre que houver mudança de estado em qualquer sensor monitorado um pacote de mensagem deve ser enviado, independente do tempo decorrido desde a última transmissão.

IV. Do SMV

6\. O SMV deve ser capaz de emitir alertas sempre que um RASTREADOR indicar alteração em seus sensores (por exemplo, abertura de portas do baú).

V. Do Relatório

7\. O item 9.2 do relatório especificado no Anexo I passa a ser acrescido das informações do estado dos sensores.
