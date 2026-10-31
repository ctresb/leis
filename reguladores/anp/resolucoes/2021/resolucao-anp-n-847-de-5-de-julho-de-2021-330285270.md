---
titulo: "RESOLUÇÃO ANP Nº 847, DE 5 DE JULHO DE 2021"
orgao: "Ministério de Minas e Energia/Agência Nacional do Petróleo, Gás Natural e Biocombustíveis"
tipo: "Resolução"
numero: "847"
data: 2021-07-05
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 06/07/2021, seção 1, p. 64"
data_publicacao: 2021-07-06
edicao: "125"
fonte: "https://www.in.gov.br/web/dou/-/resolucao-anp-n-847-de-5-de-julho-de-2021-330285270"
sha256_html_fonte: 6ee4b98a4d0009fb2b76f1de6c46997b127267754a71c3a7f005e3d8eec557b2
baixado_em: 2026-10-21
---
# RESOLUÇÃO ANP Nº 847, DE 5 DE JULHO DE 2021

RESOLUÇÃO ANP Nº 847, DE 5 DE JULHO DE 2021

Regulamenta a formatação e os procedimentos de entrega obrigatória de dados geofísicos não sísmicos ao Banco de Dados Técnicos de Exploração e Produção vinculado à ANP.

A DIRETORIA DA AGÊNCIA NACIONAL DO PETRÓLEO, GÁS NATURAL E BIOCOMBUSTÍVEIS - ANP, no exercício das atribuições conferidas pelo art. art. 65 do Regimento Interno, aprovado pela Portaria ANP nº 265, de 10 de setembro de 2020, e pelo art. 7º do Anexo I do Decreto nº 2.455, de 14 de janeiro de 1998, tendo em vista o disposto na Lei nº 9.478, de 6 de agosto de 1997, considerando o que consta do Processo nº 48610.001454/2016-11 e as deliberações tomadas na 1.054ª Reunião de Diretoria, realizada em 1º de julho de 2021, resolve:

#### CAPÍTULO I — DISPOSIÇÕES PRELIMINARES

**Art. 1º** Esta Resolução regulamenta as especificidades de formatação, procedimentos e conteúdos obrigatórios, conforme estabelecido pelo Anexo I, para a entrega dos dados geofísicos não sísmicos, seus complementares e documentos associados, aplicáveis aos agentes regulados vinculados às atividades de aquisição ou processamento realizadas nas bacias sedimentares brasileiras nas fases de exploração e produção de petróleo e gás natural.

**Art. 2º** Para os fins desta Resolução ficam estabelecidas as seguintes definições:

I - altitude geométrica: altitude em relação ao elipsoide de referência, determinado matematicamente, correspondendo à altitude medida por um receptor GNSS (Global Navigation Satellite System);

II - altitude ortométrica: distância vertical de um ponto, situado sobre a superfície terrestre, em relação a um geoide de referência.

III - aquisição de dados: atividade de coleta de informações realizada por intermédio de aplicação de métodos geofísicos, podendo ocorrer em ambientes terrestres, aéreos, marítimos ou de transição;

IV - dados batimétricos: dados oriundos de levantamentos marítimos, nos quais ondas sonoras são emitidas e refletidas no fundo oceânico em uma ou mais frequências, utilizando um ou mais feixes;

V - dados eletromagnéticos: dados provenientes da indução de ondas eletromagnéticas naturais ou de fonte controlada, que gera a propagação de correntes elétricas no meio, podendo ser adquiridos, processados e interpretados no domínio do tempo ou da frequência;

VI - dados gamaespectrométricos: dados provenientes da medição da radiação gama local;

VII - dados gravimétricos: dados provenientes da medição do campo de gravidade local, incluindo dados gradiométricos;

VIII - dados não sísmicos: dados provenientes de tecnologias geofísicas distintas do método sísmico, por exemplo, gravimetria, magnetometria, gamaespectrometria;

IX - elipsoide de referência: aproximação matemática da superfície física da Terra;

X - processamento de dados: fluxo de tratamento aplicado a dados preexistentes, em caráter de correção ou atenuação de distorções e eventos indesejáveis, difundido como reprocessamento quando posterior ao seu primeiro processamento; e

XI - programa geofísico não sísmico: conjunto de dados multifísicos relacionados entre si, com nomenclatura única, resultante de campanhas de aquisição, processamento, elaboração de estudos ou ambas, podendo existir uma ou mais versões de processamento.

#### CAPÍTULO II — DA IDENTIFICAÇÃO DO PROGRAMA GEOFÍSICO NÃO SÍSMICO

**Art. 3º** A identificação do programa para aquisição e processamento de dados geofísicos não sísmicos conterá até quarenta e cinco caracteres alfanuméricos em letras maiúsculas, sem acentuação e sem espaços em branco, e será constituída em partes separadas por subtraços ("\_") e correspondentes:

I - ao número de equipe;

II - à tecnologia do programa de aquisição ou processamento; e

III - à livre descrição.

**§ 1º** O número de equipe referido no inciso I do caput será composto por quatro dígitos previamente fornecidos pela ANP.

**§ 2º** A tecnologia do programa referida no inciso II do caput será representada por uma sigla constituída por entre duas à cinco letras na forma estabelecida no Anexo II.

**§ 3º** A descrição referida no inciso III do caput será de livre preenchimento, desde que obedecidas as condicionantes estabelecidas pelo caput.

**Art. 4º** A identificação do levantamento apenas processado deverá ser iniciada com a letra "R", seguido pelas regras de formatação de que trata o art. 3º.

**Art. 5º** As identificações de estação e linha conterão apenas números inteiros, letras e os caracteres hífen ou subtraço.

#### CAPÍTULO III — DA FORMATAÇÃO GERAL DOS ARQUIVOS

**Art. 6º** O nome do diretório raiz deverá ter o mesmo nome do programa geofísico não sísmico.

**Art. 7º** O ambiente de aquisição ou a atividade de reprocessamento deverão ser informados no cabeçalho de todos os arquivos por meio das seguintes siglas:

I - "TERRA", para dados terrestres;

II - "AR", para dados aéreos;

III - "MAR", para dados marítimos;

IV - "TRANS", caso tenha mais de um ambiente na aquisição; ou

V - "REPRO", para casos em que os dados sejam oriundos apenas de reprocessamento.

**Art. 8º** Todos os valores deverão ser acompanhados de suas respectivas unidades.

**Art. 9º** É obrigatória a utilização do Sistema Internacional de Unidades (SI) para todas as unidades.

**Parágrafo único.** Será aceita a utilização dos sistemas CGS e MKS quando a utilização do Sistema Internacional de Unidades (SI) for não razoável ou não usual para o tratamento dos dados.

**Art. 10.** O separador decimal deverá ser o ponto ".".

**Parágrafo único.** A ANP poderá autorizar exceção à regra do caput, mediante comprovação da necessidade.

**Art. 11.** As coordenadas geográficas e projetadas deverão ser configuradas no referencial geodésico SIRGAS 2000.

**Parágrafo único.** Caso as coordenadas tenham sido determinadas em outro referencial geodésico, deverá ser informado o código European Petroleum Survey Group (EPSG) da transformação desse referencial geodésico para o referencial geodésico SIRGAS 2000.

**Art. 12.** As coordenadas projetadas Este e Norte deverão utilizar a projeção UTM ou policônica e seu código EPSG.

**§ 1º** A projeção UTM será acompanhada dos parâmetros que a definem:

I - o meridiano central ou zona/fuso UTM;

II - o falso este, sempre 500.000m; e

III - o falso norte, sendo10.000.000m para o hemisfério sul ou 0m para o hemisfério norte.

**§ 2º** A projeção policônica será acompanhada dos parâmetros que a definem:

I - o meridiano central;

II -a latitude de origem;

III - o falso Este; e

IV - o falso Norte.

**Parágrafo único.** Outras projeções poderão ser aceitas, desde que comprovada a inviabilidade de aplicação daquelas já estabelecidas pelo caput.

**Art. 13.** Além da altitude ortométrica, poderá ser considerada a altitude geométrica, que possui valor positivo para posições acima do elipsoide de referência e valor negativo para posições abaixo dessa superfície.

#### CAPÍTULO IV — DO PROCEDIMENTO DE ENTREGA

**Art. 14.** Compete apenas ao titular do programa geofísico não sísmico a entrega à ANP dos dados obrigatórios associados.

**Art. 15.** Os dados obrigatórios deverão ser enviados fisicamente à ANP ou encaminhados por meio eletrônico, juntamente com o Boletim de Remessa de Dados vinculado ao programa, conforme disposto no sítio eletrônico da Agência.

**Art. 16.** Considerando o envio físico dos dados obrigatórios deverá o responsável pela entrega, realizar consulta a ANP para obter informações sobre tecnologias e limitações de hardware.

**Art. 17.** Somente será permitido o envio de dados obrigatórios por meio eletrônico mediante o prévio aceite e conforme procedimento estipulado no sitio eletrônico da ANP.

**Art. 18.** A entrega de dados obrigatórios corrompidos ou incompletos não será considerada para cumprimento dos prazos estipulado, dada a impossibilidade de cadastro da remessa nos sistemas da ANP.

**Art. 19.** Somente estará apto a realizar a entrega e submissão dos dados para análise o titular cujo programa cadastrado esteja regular quanto às notificações de início e término de atividade.

#### CAPÍTULO V — DISPOSIÇÕES FINAIS E TRANSITÓRIAS

**Art. 20.** A Resolução ANP nº 9, de 24 de fevereiro de 2005, passa a vigorar com a seguinte alteração:

"Art. 1º Fica aprovada a atualização do padrão técnico ANP1B para dados sísmicos, que se encontra disponível no sítio eletrônico da ANP (http://www.gov.br/anp)." (NR)

**Art. 21.** Esta Resolução entra em vigor no dia 1º de agosto de 2021.

RODOLFO HENRIQUE DE SABOIA

Diretor-Geral

## ANEXO I

(a que se refere o art. 1º da Resolução ANP nº 847 de 5 de julho de 2021.)

1\. PARA TODAS AS TECNOLOGIAS

1\. Todos os arquivos em extensão ASCII e TXT devem ser entregues nos formatos a seguir:

1\. As linhas do cabeçalho devem iniciar com "/" (barra).

1\. 1. Os mnemônicos no cabeçalho devem ser seguidos do caractere "=" (igual), sua respectiva descrição, unidade física entre " " (aspas) ou [] colchetes, seguido do caractere ";" (ponto e vírgula).

1\. 1. 3. A primeira linha do corpo do dado deve apresentar os canais formados por todos os mnemônicos separados pelo caractere "," (vírgula).

1\. 1. 4. No corpo do dado, os valores poderão conter colunas separadas pelo caractere "," (vírgula) ou "." (ponto).

1\. 1. 5. O fiducial é um número sequencial inteiro que começa do número 1 (um) e com incremento 1 (um).

1\. 1. 6. A data deve ser representada no formato AAAAMMDD, sendo AAAA para o ano, MM para o mês e DD para o dia.

1\. 1. 7. A hora deve ser representada no formato HHMMSS sendo HH para as horas, MM para os minutos, SS para os segundos. Opcionalmente, o milésimo de segundo pode ser apresentado com 3 caracteres.

1\. 1. 8. As coordenadas geográficas (latitude e longitude) devem ser representadas em graus decimais.

1\. 1. 9. O valor nulo ou dummy quando usado deve ser representado por "\*" (asterisco). O valor deve ser declarado no cabeçalho do arquivo da seguinte forma: "DUMMY=\*;".

1\. 2. Todos os arquivos em extensão ASCII, TXT e SEGY devem conter obrigatoriamente os mnemônicos descritos na Tabela 1. Os arquivos em outras extensões, quando especificado em seu conteúdo, devem conter os mnemônicos, à exceção do arquivo de relatório.

Tabela 1 - Mnemônicos com suas respectivas descrições e formatos.

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Mnemônico</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Descrição</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Tipo</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Unidade</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Formato</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>NOME</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Nome do levantamento</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>30s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>AMB</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Ambiente ("AR", "TERRA", "MAR", "TRANS" OU "REPRO")</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>5s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>CRS</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Sistema de Coordenada de Referência</p>  			<p>(SIRGAS 2000)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>10s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>EPSG</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Código EPSG</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>6s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>PROJ</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Nome da Projeção</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>20s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>EPSG_PROJ</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Código EPSG da projeção</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>6s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>EPSG_CONV</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Código EPSG da conversão</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>6s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>FUSO</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Fuso utilizado para a projeção UTM</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Integer</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>20s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>HEM</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Hemisfério para a projeção UTM (N ou S)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>1s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>MC</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Meridiano Central para a projeção</p>  			<p>Policônica</p>  			<p>(GG:MM:SS.ss)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Graus, minutos e segundos</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>12i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>LAT_O</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Latitude de Origem para a projeção</p>  			<p>Policônica</p>  			<p>(GG:MM:SS.ss)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Graus, minutos e segundos</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>12i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>FN</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Falso Norte para a projeção Policônica</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>7i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>ALT_TIPO</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Tipo de Altitude - Geométrica (GEOM) ou Ortométrica (ORTO)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>4i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>FE</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Falso Leste para a projeção Policônica</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>8i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>DUMMY</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Valor nulo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>*</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>ALGR</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Algoritmo de interpolação</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>80s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>GX</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Tamanho da célula na direção Leste</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>metros</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9.2f</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>GY</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Tamanho da célula na direção Norte</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>metros</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9.2f</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>NL</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Número de linhas no arquivo de interpolação</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>10i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>NC</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Número de colunas no arquivo de interpolação</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>10i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>FID</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Fiducial</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Long</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>8i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>LINHA</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Linha</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>10s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>EST</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Estação</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>8s</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>DATA</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Data (AAAAMMDD)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>8i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>HORA</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Hora (HHMMSS[.sss])</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Float</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>N/A</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>10.3</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>LAT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Latitude (GG:MM:SS.ss)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Graus, minutos e segundos</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>12i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>LONG</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Longitude (GG:MM:SS.ss)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>String</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Graus, minutos e segundos</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>12i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>X</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Coordenada Leste projetada</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Float</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>metros</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9.2f</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Y</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Coordenada Norte projetada</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Float</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>metros</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>10.2f</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>ALT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Altitude</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Float</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>metros</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>6.1f</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>PROF</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Profundidade estimada por inversão</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Float</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>metros</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>6.1f</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>SP ou IL</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Localização dos<strong>bytes</strong>dos<strong>Shot Points</strong>ou</p>  			<p><strong>Inlines</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>20i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>CDP</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Localização dos<strong>bytes</strong>dos CDPs</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Adimensional</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>20i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>IA</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Intervalo de amostragem</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>metros</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>6i</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>AT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Número de amostras por traço</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Integer</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Amostras/traço</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>10i</p> 			</td> 		</tr> 	</tbody> </table>

1\. 3. Todos os arquivos em extensão EDI deverão seguir o formato MT/EMAP Data Interchange Standard de 1987 da SEG, conforme exemplo mostrado no Quadro 1.

Quadro 1 - Exemplo de arquivo de dados de tensores elétricos e magnéticos extensão EDI.

>HEAD

DATAID="01-113-02"

ACQBY="EMPRESA A"

FILEBY="EMPRESA B"

ACQDATE=2013/01/13

FILEDATE=2014/07/16

COUNTRY="BRASIL"

STATE="RIO DE JANEIRO"

LAT= "GRAUS DECIMAIS"

LONG= "GRAUS DECIMAIS"

ELEV=643

UNITS=M

STDVERS="SEG 1.0"

PROGVERS="Corrector NW 4.98"

PROGDATE=2014/07/16

EMPTY=1.0E+32

>INFO

RUN INFORMATION STATION 1

PROCESSED FROM DFT TIME SERIES STN Number: 01-113-02

SURVEY: RECONCAVO Site Desc; BadR: 0 SatR: 47527 COMPANY: EMPRESA C Lat 23:27:369S Long 050:47:152W

JOB: 01 Elevation: 643 Meters.

Reference Site: RR-4-24

HARDWARE: MTU52 MTU52 Site Permitted by:

START-UP: 2013/01/01 - 01:00:00 Site Layout by:

END-TIME: 2014/04/23 - 13:47:29 SYSTEM INFORMATION

FILE: 1964420B 1967421A MTU-Box Serial Number: U-1964

MTUPROG VERSION: 3100E6 MTU-Box Gains:E`s x 40 H`s x 12

MTU-DFT VERSION: TStoFT.34 MTU-Ref Serial Number: U-1967

MTU-RBS VERSION: R2007-1127-B18 Comp Chan# Sensor Azimuth

Reference Field: Remote H - Ref. Ex1 1 100.0 M 0.0 DGtn

XPR Weighting: RHO Variance. Ey1 2 100.0 M 90.0 DGtn

RBS: 7 COH: 0.85 RHO VAR: 0.75 Hx1 3 COIL1249 0.0 DGtn

CUTOFF: 0.00 COH: 35 % VAR: 25 % Hy1 4 COIL1251 90.0 DGtn

Notch Filters set for 60 Hz. Hz1 5 COIL2290

RHx2 6 COIL2460 0.0 DGtn

Comp MTU box S/N Temp RHy2 7 COIL2462 90.0 DGtn

Ex & Ey: MTU52 1964 48 C Ebat:11.0V Hbat:11.0V Rbat:11.8V

Hx & Hy: MTU52 1964 48 C Ex Pot Resist: 1.200 Kohms

Hz: MTU52 1964 48 C Ex Voltage:AC=30.5mV, DC=+0.20mV Rx & Ry: MTU52 1967 44 C Ey Pot Resist: 1.350 Kohms

1\. PARA AS TECNOLOGIAS GRAVIMÉTRICAS, MAGNETOMÉTRICAS E GAMAESPECTROMÉTRICAS

1\. 1. Diretório raiz: Deve conter os arquivos de dados medidos e processados, dados fixos, dados interpolados, localização e relatório, conforme ilustrado na Tabela 2.

Tabela 2 - Para as tecnologias eletromagnéticas aéreas, gravimétricas, magnetométricas e gamaespectrométricas.

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Diretório Raiz</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Arquivo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Extensão</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Padrão de nome do arquivo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Exemplos</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Dados medidos e processados</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>ASCII ou TXT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome do</p>  			<p>levantamento&gt;_med_proc.asc</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_GRAV_CAMPOS_med_proc.asc</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Dados fixos</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>ASCII ou TXT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome do</p>  			<p>levantamento&gt;_fix.asc</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_GRAV_CAMPOS_fix.asc</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Dados interpolados</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>ASCII ou TXT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome do</p>  			<p>levantamento&gt;_grid.asc</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_GRAV_CAMPOS_grid.asc</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Localização</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>ASCII ou TXT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome do</p>  			<p>levantamento&gt;_localizacao.asc</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_GRAV_CAMPOS_</p>  			<p>localizacao.asc</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Relatório</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>PDF/A ou</p>  			<p>DOCX ou ODT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome do</p>  			<p>levantamento&gt;_relatorio.docx</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_GRAV_CAMPOS_relatorio.docx</p> 			</td> 		</tr> 	</tbody> </table>

1\. 2. Arquivo de dados medidos e processados: deve conter todos os valores medidos das estações móveis e fixas e processados, incluindo os produtos intermediários resultantes das etapas de processamento, conforme exemplificado no Quadro 2, salvo quando da comprovação da necessidade e posterior anuência desta Agência em casos de excepcionalidades.

2.2.1. Deve ser entregue nas extensões ASCII ou TXT. O nome do arquivo segue o padrão nome do levantamento, seguido pelo caractere "\_" (sublinhado) e a sigla med\_proc, como mostrado na Tabela 2.2.2.2. No cabeçalho do arquivo deve conter as informações: nome do levantamento, ambiente, Sistema de Coordenada de Referência (CRS) em SIRGAS 2000, coordenadas geográficas e projetadas da estação medida, EPGS da coordenada geográfica ou da coordenada projetada, ambiente, descrição dos mnemônicos e do valor nulo.

1\. 2. 1. O arquivo deve ter no corpo os seguintes itens: fiducial, linha, estação, data, hora, coordenadas geográficas, coordenadas projetadas leste e norte, altitude geométrica e anomalias. As informações contidas no arquivo devem ser ordenadas de forma correspondente entre cabeçalhos, mnemônicos e valores medidos.

1\. 2. 2. As colunas correspondentes ao fiducial, linha, estação, data, hora, coordenadas geográficas, coordenadas projetadas leste e norte e altitude geométrica não deverão conter valores nulos.

Quadro 2 - Exemplo de arquivo de dados medidos e processados.

/ NOME = 9999\_MAG\_CAMPOS\_AREA\_AA;

/ DATUM = SIRGAS2000; PROJ = UTM 24S; EPSG= 4674; EPSG\_PROJ= 31984;

/ FID= fiducial; EST= Estacao medida; LINHA = Linhas do Levantamento; AMB=MAR;

/ DATA= Data em formato AAAAMMDD; HORA= Hora em formato HHMMSS.sss;

/ LAT = Latitude "GRAUS DECIMAIS"; LONG = Longitude "GRAUS DECIMAIS";

/ X = Coordenada projetada leste "m"; Y = Coordenada projetada norte "m";

/ ALTG= Atitude Geométrica "m";

/ DECL= declinação "o"; INCL= inclinação "o";

/ MAGB= campo magnetico bruto "nT";

/ MAG\_BASE= Variacao diurna do campo magnetico "nT";

/ MAG\_VAR= Correcao da variacao diurna do campo magnetico "nT";

/ TAN= Campo magnetico "nT";

/ TANS= Campo Magnetico Reduzido e Micronivelado "nT";

/ TANSH= Campo Magnetico Reduzido "nT";

/ TANSH\_LEV= Campo Magnetico Reduzido e Micronivelado "nT";

/ DUMMY = \*;

FID,LINHA,EST,DATA,HORA,LAT,LONG,X,Y,ALT,DECL,INCL,MAGB,MAG\_BASE,MAG\_VAR,TAN,TANS,TANSH,TANSH\_LEV

1,500,120528,20050808,140859.500,-4.00383858,-0.65971000,6038325,9663415,304,-3.78,-

5.02,26226.03,26257.71,31.69,26.84,26.84,28.89,40.02

2.3. Arquivo de dados fixos: deve conter os dados medidos em estações fixas para efeito de correção, como exemplificado no Quadro 3, salvo quando da comprovação da necessidade e posterior anuência desta Agência em casos de excepcionalidades.

2.3.1. Deve ser entregue nas extensões ASCII ou TXT. O nome do arquivo segue o padrão nome do levantamento, seguido pelo caractere "\_" (sublinhado) e a sigla fix (Tabela 2).

2.3.2. O cabeçalho do arquivo deve conter o nome do levantamento, ambiente, CRS, EPGS da coordenada geográfica ou da coordenada projetada, ambiente e descrição dos mnemônicos.

2.3.3. O corpo do dado deverá conter os seguintes itens: nome da estação, coordenadas geográficas, altitude, data, hora e anomalias. As informações contidas no arquivo devem ser ordenadas de forma correspondente entre cabeçalhos, mnemônicos e valores medidos.

2.3.4. Esse arquivo não pode conter valores nulos.

Quadro 3 - Exemplo de arquivo de dados fixos.

/ NOME = 9999\_MAG\_CAMPOS\_AREA\_AA;

/ DATUM = SIRGAS 2000; EPSG= 4674; AMB=MAR;

/ EST = Nome da Estação;

/ LAT = Latitude "GRAUS"; LONG = Longitude "GRAUS";

/ ALTG= Atitude Geométrica "m";

/ DATA= data no formato AAAAMMDD;

/ HORA= hora no formato HHMMSS.sss;

/ MAG = campo magnetico "nT";

EST,LAT,LONG, HALT,DATA,HORA, MAG

L879,-4.00383858,-40.65971000, 325,20060306,083027.000,25874.320

L877,-4.15283858,-40.75971222, 502,20060306,184712.000,25875.580

2.4. Arquivo com dados interpolados:

2.4.1. Deve conter todas as anomalias oriundas de processamento 1D e 2D, como ilustrado no Quadro 4, salvo quando da comprovação da necessidade e posterior anuência desta Agência em casos de excepcionalidades. No caso de interpolação com tamanhos de células diferentes, cada tamanho corresponderá a um arquivo com dados interpolados.

2.4.2. Deve ser entregue nas extensões ASCII ou TXT. O nome do arquivo segue o padrão nome do levantamento, seguido pelo caractere "\_" (sublinhado) e a sigla grid (Tabela 2).

2.4.3. O cabeçalho do arquivo deve conter nome do levantamento, ambiente, algoritmo, Sistema de Coordenada de Referência (CRS) em SIRGAS 2000, coordenadas geográficas e projetadas da estação medida, EPGS da coordenada geográfica ou da coordenada projetada, ambiente, descrição dos mnemônicos e do valor nulo. Deve conter ainda os valores do tamanho da célula utilizada para fazer a interpolação na direção Leste e Norte, número de linhas e de colunas.

2.4.4. No corpo do arquivo deverão estar contidos os seguintes itens: coordenadas geográficas ou projetadas e os valores das anomalias. As informações contidas no arquivo devem ser ordenadas de forma correspondente entre cabeçalhos, mnemônicos e valores medidos.

2.4.5. As colunas com coordenadas geográficas ou projetadas não podem conter valores nulos.

Quadro 4 - Exemplo de arquivo de dados de interpolação.

/ NOME = 9999\_MAG\_CAMPOS\_AREA\_AA; AMB=MAR

/ ALGR: Mínima Curvatura;

/ DATUM = SIRGAS 2000; PROJ = UTM Zona 24S;

/ EPSG= 4674; EPSG\_PROJ= 31984;

/ GX= 7000; GY= 6500;

/ NL= 143; NC= 142;

/ X = Coordenada projetada leste "m"; Y = Coordenada projetada norte "m";

/ MAG= dado bruto "nT";

/ TAN= Campo magnético simples "nT";

/ TANS= Campo magnético sem a variação diurna "nT";

/ TANSH= Campo magnético com filtragem do modelo IGRF "nT";

/ TAN\_LEV= Campo magnético com filtragem do movimento da aeronave "nT"; / DUMMY = \*;

X,Y,MAG,TAN,TANS,TANSH,TANSH\_LEV

140000.00,8701000.00,24230.18,24.88,24.88,27.43,38.59

1\. PARA AS TECNOLOGIAS ELETROMAGNÉTICAS

1\. 1. Diretório raiz: Deve conter um subdiretório com os dados medidos e processados, denominado med\_proc, e outro com as estações remotas; arquivos de localização e relatório, conforme mostrado na Tabela 3.

Tabela 3 - Para as tecnologias eletromagnéticas terrestres e marítimas.

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Diretório</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Exemplo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Subdiretório</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Exemplo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Subdiretório</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Nome de arquivo</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Diretório raiz</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_MT_CAMPOS</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>med_proc (Dados medidos e processados)</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_MT_CAMPOS_med_proc</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>medidos</strong><br> 			<strong>(Dados medidos)</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Séries temporais medidas e calibração</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="9"> 			<p> </p> 			</td> 			<td colspan="1" rowspan="9"> 			<p> </p> 			</td> 			<td colspan="1" rowspan="6"> 			<p> </p> 			</td> 			<td colspan="1" rowspan="6"> 			<p> </p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="6"> 			<p><strong>processados</strong><br><strong>(Dados processados)</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Curvas dos tensores elétricos e magnéticos</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Inversão 1D</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Inversão 2D</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Inversão 2.5D</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Inversão 3D</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>remotas</strong></p>  			<p><strong>(Séries temporais das estações remotas)</strong></p> 			</td> 			<td colspan="2" rowspan="1"> 			<p>9999_MT_CAMPOS_remotas</p>  			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Séries temporais e calibração</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="3" rowspan="2"> 			<p> </p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Localização</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Relatório</strong></p> 			</td> 		</tr> 	</tbody> </table>

1\. 2. Subdiretório de dados medidos e processados (med\_proc): O nome do diretório segue o padrão nome do levantamento, seguido pelo caractere "\_" (sublinhado) e a sigla med\_proc. O subdiretório med\_proc deve conter dois subdiretórios denominados "medidos" e "processados".

1\. 3. Subdiretório medidos: Deve conter os dados medidos, incluindo séries temporais dos receptores, transmissores e respectivas calibrações.

1\. 4. Arquivos de séries temporais: devem ser entregues nas extensões HDF5, ASCII ou TXT ou AS2/AS3/AS4/AS5. Devem seguir a seguinte nomenclatura nome da linha, seguido pelo caractere "\_" (sublinhado), a sigla Rx para receptor ou Tx para transmissor e o nome da estação, mostrado na Tabela 4.

1\. 4. 1. Os arquivos nas extensões ASCII, TXT ou AS2/AS3/AS4/AS5 devem ser organizados para que cada estação medida tenha um subdiretório com o nome da estação, contém todos os arquivos medidos e as calibrações.

1\. 4. 2. Caso as séries temporais sejam entregues em HDF5, os dados de calibração devem estar contidos nesses arquivos.

1\. 4. 3. Os dados de séries temporais em extensão ASCII ou TXT ou AS2/AS3/AS4/AS5 devem conter cabeçalho com as seguintes informações: nome do levantamento, ambiente, Sistema de Coordenada de Referência (CRS) em SIRGAS 2000, coordenadas geográficas, EPGS da coordenada geográfica, altitude geométrica, tipo de altitude ("ALT" para altitudes e "BAT" para batimetrias) e a descrição dos mnemônicos.

1\. 4. 4. No corpo deve conter os valores das séries temporais de cada bobina.

Tabela 4 - Subdiretório med\_proc.

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p> </p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Nome de arquivo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Extensão</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Padrão de nome do arquivo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Exemplo</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Séries temporais medidas e calibração</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>HDF5,</p>  			<p>ASCII, TXT ou</p>  			<p>AS2/AS3/A</p>  			<p>S4/AS5</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome da linha&gt;_&lt;Rx ou</p>  			<p>Tx&gt;&lt;estação&gt;.&lt;extensão&gt; (Rx para receptore Tx para transmissor)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>999_Rx2587.h5 (receptor)</p>  			<p>999_Tx02358.h5 (transmissor)</p>  			<p>0215-9999-0001_Rx125.asc</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Curvas dos tensores elétricos e magnéticos</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>EDI ou</p>  			<p>NetCDF</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome da linha&gt;_&lt;Rx ou</p>  			<p>x&gt;&lt;estação&gt;.&lt;extensão&gt; (Rx para receptor e Tx para transmissor)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999-0001_R125.edi</p>  			<p>9999-0001_R125.nc</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Inversão 1D</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>ASCII ou</p>  			<p>SEGY</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Estação&gt;_INV1D.&lt;extensão&gt;</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Estação&gt;_INV1D.sgy</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Inversão 2D</strong></p> 			</td> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>&lt;linha&gt;_INV2D. &lt;extensão&gt;</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;linha&gt;_INV2D.asc</p>  			<p>&lt;linha&gt;_INV2D.sgy</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Inversão 2.5D</strong></p> 			</td> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>&lt;linha&gt;_ INV2.5D.&lt;extensão&gt;</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;linha&gt;_ INV2.5D.asc</p>  			<p>&lt;linha&gt;_ INV2.5D.sgy</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p><strong>Inversão 3D</strong></p> 			</td> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>&lt;nome do</p>  			<p>levantamento&gt;_INV3D.&lt;extensão&gt;</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_MT_CAMPOS_INV3D.asc</p>  			<p>9999_MT_CAMPOS_INV3D.sgy</p> 			</td> 		</tr> 	</tbody> </table>

1\. 5. Subdiretório processados: Deve conter todas as curvas dos tensores e as inversões.

1\. 6. Arquivos de curvas dos tensores elétricos e magnéticos: devem ser entregues na extensão EDI ou NetCDF. Os nomes das curvas devem seguir o padrão nome da linha, seguido pelo caractere "\_" (sublinhado), a sigla Rx para receptor ou Tx para transmissor e o nome da estação (Tabela 4).

1\. 6. 1. Os arquivos de curvas de tensores elétricos e magnéticos devem conter no cabeçalho o nome da estação, coordenadas geográficas e projetadas, EPGS da coordenada geográfica ou da coordenada projetada, altitude geométrica do receptor (vide Quadro 1) e o tipo de altitude ("ALT" para altitudes e "BAT" para batimetrias).

1\. 7. Arquivos de inversão 1D, 2D, 2.5D e 3D: devem ser entregues em ASCII ou SEGY. Os nomes dos arquivos devem seguir o padrão estação para 1D ou linha para 2D e 2,5D ou nome do levantamento para 3D, seguido pelo caractere "\_" (sublinhado) e a respectiva sigla INV1D, INV2D, INV2.5D e INV3D (Tabela 4).

3.7.1Os dados de inversão 1D em extensão ASCII devem conter no cabeçalho o nome do levantamento, ambiente, nome da estação, Sistema de Coordenada de Referência (CRS) em SIRGAS 2000, coordenadas geográficas e projetadas da estação medida, EPGS da coordenada geográfica ou da coordenada projetada, nível de referência, tipo de altitude ("ALT" para altitudes e "BAT" para batimetrias) e a descrição dos mnemônicos. No corpo deve conter profundidades estimadas e resistividades (ohm.m), como ilustrado no exemplo no Quadro 5.

9\. 1. 1. Os arquivos das inversões 2D, 2.5D e 3D em arquivo ASCII devem conter no cabeçalho o nome do levantamento, ambiente, nome da linha (2D e 2.5D), Sistema de Coordenada de Referência (CRS) em SIRGAS 2000, coordenadas geográficas e projetadas da estação medida, EPGS da coordenada geográfica ou da coordenada projetada, nível de referência, tipo de altitude ("ALT" para altitudes e "BAT" para batimetrias) e a descrição dos mnemônicos. No corpo deve conter nomes de linhas, estações medidas, coordenadas geográficas e projetadas, profundidades estimadas e resistividades (ohm.m) como ilustrado no exemplo no Quadro 5.

Quadro 5 - Exemplo de arquivos de inversão em ASCII.

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p> </p>  			<p><em>Exemplo de arquivo de dados de inversão 1D em extensão ASCII.</em></p>  			<p> </p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>/ NOME = Levantamento 9999_MT_RECONCAVO_8;</p>  			<p>/ EST = 4527T-10; AMB=TERRA;</p>  			<p>/ DATUM = SIRGAS 2000; EPSG= 4674; PROJ = UTM24S;</p>  			<p>/ EPSG= 4674; EPSG_PROJ= 31984;</p>  			<p>/ LAT = Latitude "GRAUS"; LONG = Longitude "GRAUS";</p>  			<p>/ X = Coordenada projetada leste "m"; Y = Coordenada projetada norte "m";</p>  			<p>/ ALTG= Atitude Geométrica "m";</p>  			<p>/ PROF= profundidade estimada "m";</p>  			<p>/ RES= resistividade "ohm.m";</p>  			<p>LAT,LONG,X,Y,PROF,RES</p>  			<p>-4.00383858,-40.65971000,6038325,9663415,758,250.85</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p> </p>  			<p><em>Exemplo de arquivo de dados inversão 2D em extensão ASCII.</em></p>  			<p> </p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>/ NOME = Levantamento 9999_MT_RECONCAVO_8; AMB=TERRA;</p>  			<p>/ DATUM = SIRGAS 2000; EPSG= 4674;</p>  			<p>/ PROJ = UTM24S; EPSG= 4674; EPSG_PROJ= 31984;</p>  			<p>/ LINHA= linha; EST= estação medida;</p>  			<p>/ ALTG= Atitude Geométrica "m";</p>  			<p>/ LAT = Latitude "GRAUS"; LONG = Longitude "GRAUS";</p>  			<p>/ X = Coordenada projetada leste "m"; Y = Coordenada projetada norte "m";</p>  			<p>/ PROF= profundidade estimada "m";</p>  			<p>/ RES= resistividade "ohm.m";</p>  			<p>LINHA, EST, LAT, LONG, X, Y, prof,RES</p>  			<p>0258-6523, 5248T, -4.00383858,-40.65971000, 6038325,9663415,758,250.85</p> 			</td> 		</tr> 	</tbody> </table>

9\. 1. 2. Os dados de inversão em formato SEGY devem conter no cabeçalho EBCDIC as informações da Tabela 5. As informações devem ser precedidas de seu respectivo mnemônico separado por espaço.

Tabela 5 - Informações necessárias no cabeçalho do EBCDIC de arquivo SEGY.

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Cartão</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Informação</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Bytes</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C1</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Nome da EAD</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>5-20</p> 			</td> 		</tr> 	</tbody> </table>

<table> 	<tbody> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Ambiente</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>30-40</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Nome da Operadora</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>50-80</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C2</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Número da linha (Levantamentos 2D e 2.5D)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>5-30</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Cartão</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Informação</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>Bytes</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Nome do Levantamento</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>40-60</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C3</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Nome da estação</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>45-55</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C5</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Localização dos<strong>bytes</strong>dos<strong>Shot Points</strong>ou<strong>Inlines</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>5-30</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Localização dos<strong>bytes</strong>dos CDPs</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>40-80</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C6</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Intervalo de amostragem</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>20-30</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Número de amostras por traço.</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>40-50</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C16</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Nível de referência vertical</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>5-30</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C16</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>AMBIENTE ("ALT", "TERRA"ou "AR")</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>40-43</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C38</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Zona UTM ou Meridiano Central</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>5-25</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Latitude de Origem (caso houver)</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>35-45</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Falso Leste</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>50-60</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Falso Norte</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>65-75</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>C39</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Sistema de Coordenada de Referência (CRS) em SIRGAS 2000</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>5-30</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Código EPSG do CRS</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>40-45</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Nome da projeção utilizada</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>50-70</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> </td> 			<td colspan="1" rowspan="1"> 			<p>Código EPSG da projeção</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>75-80</p> 			</td> 		</tr> 	</tbody> </table>

9\. 1. 3. As posições dos bytes obrigatórios dos dados em SEGY seguirão o descrito na Tabela 6.

Tabela 6 - Bytes para arquivos referentes.

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Descrição</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Byte</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Traço</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>1-4</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Amostragem por traço</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>115-116</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Intervalo de amostragem</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>117-118</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>UTMX</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>181-184</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>UTMY</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>185-188</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Linha ou<strong>Inline</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>221-224</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Estação medida ou<strong>Crossline</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>225-228</p> 			</td> 		</tr> 	</tbody> </table>

1\. 8. Diretório com as séries temporais das estações remotas: deve conter as séries temporais e as calibrações das estações remotas.

9\. 1. 1. As séries temporais das estações remotas devem ser entregues nas extensões HDF5, ASCII ou TXT ou AS2/AS3/AS4/AS5. Devem seguir a nomenclatura nome da linha, seguido pelo caractere "\_" (sublinhado), a sigla Rmt e o nome da estação, ilustrada na Tabela 7.

9\. 1. 2. Os arquivos nas extensões ASCII, TXT ou AS2/AS3/AS4/AS5 devem ser organizados para que cada estação medida tenha um subdiretório com o nome da estação, contém todos os arquivos medidos e as calibrações.

9\. 1. 3. Caso as séries temporais sejam entregues em HDF5, os dados de calibração devem constar nesses arquivos.

9\. 1. 4. Os dados de séries temporais em formatos ASCII ou TXT ou AS2/AS3/AS4/AS5 (Tabela 7) devem conter cabeçalho com as seguintes informações: nome do levantamento, ambiente, Sistema de Coordenada de Referência (CRS) em SIRGAS 2000, coordenadas geográficas e projetadas da estação medida, EPGS da coordenada geográfica ou da coordenada projetada, nível de referência, altitude geométrica, ambiente e a descrição dos mnemônicos. O corpo deve conter os valores das séries temporais de cada bobina com valores de amplitude em relação ao tempo. As colunas devem ter a seguinte ordem: Ex, Ey, Hx, Hy e Hz (se houver).

Tabela 7 - Séries temporais e calibração, arquivos de localização e relatórios.

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>Nome de Arquivo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Extensão</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Padrão de nome do arquivo</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Exemplo</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Séries temporais e calibração</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>HDF5,</p>  			<p>ASCII, TXT ou</p>  			<p>AS2/AS3/A S4/AS5</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome da linha&gt;_&lt;Rmt&gt;&lt;estação&gt;.&lt;extensão&gt;</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>0001_Rmt03251.asc ou</p>  			<p>0001_Rmt03251.h5</p>  			<p> </p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Localização</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>UKOOA</p>  			<p>P1/90,</p>  			<p>UKOOA</p>  			<p>P2/94, OGP</p>  			<p>P1/11, TXT ou ASCII</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome do levantamento&gt;_localizacao.&lt;extensão&gt;</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_MT_CAMPOS_localizac ao.asc</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>Relatório</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>PDF/A ou</p>  			<p>DOCX ou ODT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>&lt;Nome do levantamento&gt;_relatorio.&lt;extensão&gt;</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>9999_MT_CAMPOS_relatorio. docx</p> 			</td> 		</tr> 	</tbody> </table>

2\. PARA AS TECNOLOGIAS BATIMETRIA DE MULTIFEIXE E MEDIDA DE FLUXO DE CALOR

2\. 1. O diretório raiz deve conter um subdiretório com dados medidos e processados, denominado med\_proc, e os arquivos de localização e relatório, cabendo observar a estrutura e os exemplos desses itens apresentados nas tabelas Tabela 4 e Tabela 7.

2\. 2. Para a tecnologia batimetria multifeixe, o subdiretório med\_proc deve conter dois diretórios denominados "medidos" e "processados".

3\. DADOS PROCESSADOS

3\. 1. Os dados oriundos de processamento devem conter o arquivo relatório, arquivo de localização dos dados brutos e os dados especificados abaixo.

9\. 1. 5. Para as tecnologias eletromagnéticas aéreas, gravimétricas, magnetométricas e gamaespectrométricas, deve ser entregue o arquivo de dados interpolados.

9\. 1. 6. Para as tecnologias eletromagnéticas terrestres e marítimas, devem ser entregues arquivos de inversões 1D, 2D, 2.5D ou 3D.

4\. ARQUIVO DE LOCALIZAÇÃO

9\. 1. Deve conter todas as localizações das estações medidas.

9\. 2. O arquivo deve ser entregue em extensão UKOOA P1/90, UKOOA P2/94, OGP P1/11, TXT ou ASCII. O nome do arquivo segue o padrão nome do levantamento, seguido pelo caractere "\_" (sublinhado) e a palavra localização (Tabela 7).

9\. 3. No cabeçalho do arquivo deve conter as informações: nome do levantamento, ambiente, Sistema de Coordenada de Referência (CRS) em SIRGAS 2000, coordenadas geográficas e projetadas da estação medida, EPGS da coordenada geográfica ou da coordenada projetada, nível de referência, nível de referência, ambiente e descrição dos mnemônicos.

9\. 4. O corpo do arquivo deve conter as informações na seguinte ordem: linha, estação, coordenadas geográficas ou coordenadas projetadas e as altitudes geométricas.

9\. 5. Para cotas batimétricas, o Nível Médio do Mar (NMM) poderá ser adotado como referência.

5\. ARQUIVO DE RELATÓRIO (COMUM A TODAS AS TECNOLOGIAS)

7.1.O arquivo deve ser entregue em extensão ODT ou PDF/A ou DOCX e deve conter as informações sobre a aquisição e processamento. O nome do arquivo segue o padrão nome do levantamento, seguido pelo caractere "\_" (sublinhado) e a palavra "relatório" (Tabela 7).

7.2.O relatório final deve conter as seguintes informações sobre o levantamento: nome do levantamento, datas da aquisição e do processamento, equipamentos utilizados, parametrização, quilometragem linear ou área e descrição do processamento.

## ANEXO II

(a que se refere o § 2º do art. 3º da Resolução ANP nº 847 de 5 de julho de 2021.)

1\. SIGLAS REFERENTES ÀS TECNOLOGIAS

<table> 	<tbody> 		<tr> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p><strong>SIGLA</strong></p> 			</td> 			<td colspan="1" rowspan="1"> 			<p><strong>TECNOLOGIA</strong></p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>AMT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Audiomagnetotelúrico</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>MBE</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Batimetria de Multifeixe</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>CSAMT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Eletromagnético Audiomagnetotelúrico com Fonte Controlada</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>CSEM</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Eletromagnético de Fonte Controlada</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>CSMT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Eletromagnético Magnetotelúrico com Fonte Controlada</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>GAMA</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Gamaespectrometria</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>GRD</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Gradiometria Gravimétrica-AGG</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>FTG</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Gradiometria Gravimétrica-FTG</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>GMAGG</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Gradiometria Magnética AGG</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>GMFTG</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Gradiometria Magnética FTG</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>GRAV</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Gravimetria</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>MAG</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Magnetometria</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>MT</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Magnetotelúrico</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>HFLOW</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Medida de fluxo de calor</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>SBP</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Perfilagem de Subfundo</p> 			</td> 		</tr> 		<tr> 			<td colspan="1" rowspan="1"> 			<p>TEM</p> 			</td> 			<td colspan="1" rowspan="1"> 			<p>Transiente Eletromagnético</p> 			</td> 		</tr> 	</tbody> </table>
