---
titulo: "PORTARIA Nº 2.176, DE 17 DE JULHO DE 2019"
orgao: "Ministério da Infraestrutura/Agência Nacional de Aviação Civil/Superintendência de Infraestrutura Aeroportuária"
tipo: "Portaria"
numero: "2176"
data: 2019-07-17
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 01/08/2019, seção 1, p. 56"
data_publicacao: 2019-08-01
edicao: "147"
fonte: "https://www.in.gov.br/web/dou/-/portaria-n-2.176-de-17-de-julho-de-2019-208199409"
sha256_html_fonte: c736a48dca66d5d3bc3fe69ebef9f90a0f99219688999c9d96db88a936648c42
baixado_em: 2026-10-21
---
# PORTARIA Nº 2.176, DE 17 DE JULHO DE 2019

PORTARIA Nº 2.176, DE 17 DE JULHO DE 2019

OS SUPERINTENDENTES DE INFRAESTRUTURA AEROPORTUÁRIA E DE REGULAÇÃO ECONÔMICA DE AEROPORTOS, no uso das atribuições que lhes conferem, respectivamente, os arts. 33, incisos III e XII, e 41, incisos IV e XVI, do Regimento Interno, aprovado pela Resolução nº 381, de 14 de junho de 2016, tendo em vista o disposto nos arts. 5º, § 3º, 7º, § 3º, e 10, § 4º, da Resolução nº 464, de 22 de fevereiro de 2018, e considerando o que consta do processo nº 00058.023658/2019-42, resolvem:

**Art. 1º** A Portaria nº 1.017/SRA/SIA, de 26 de março de 2018, publicada no Diário Oficial da União de 29 de março de 2018, Seção 1, páginas 267 a 269, que estabelece a estrutura dos dados e os procedimentos de remessa do Compilado de Movimentação Aeroportuário - CMA, do Resumo de Movimentação Aeroportuária - RMA e do Relatório de Informações de Movimentação Aeroportuária - RIMA, previstos na Resolução nº 464, de 22 de fevereiro de 2018, passa a vigorar com as seguintes alterações:

"Art. 8º O registro dos dados do RIMA deverá conter os seguintes campos, na exata ordem apresentada e delimitados por ";" (ponto e vírgula):

I - Campo 1 - COD\_RIMA: refere-se ao código de operação, que identifica uma determinada operação aeroportuária, desde o momento do toque da aeronave na pista de pouso até a decolagem;

II - Campo 2 - MOVIMENTO\_TIPO: refere-se ao tipo de movimento reportado, pouso ou decolagem. O formato é alfabético de apenas uma letra, com o valor 'P' para pouso ou 'D' para decolagem;

III - Campo 3 - AERONAVE\_MARCAS: refere-se à identificação da aeronave. O formato é alfanumérico e é representado pelas marcas de nacionalidade e de matrícula atribuídas pelo Registro Aeronáutico, brasileiro ou estrangeiro, ou pela identificação correspondente de aeronave militar;

IV - Campo 4 - AERONAVE\_TIPO: refere-se ao modelo da aeronave. O formato é alfanumérico e é representado pelo designador OACI do modelo da aeronave ou equipamento;

V - Campo 5 - AERONAVE\_OPERADOR: refere-se ao operador da aeronave. O formato é alfanumérico e é representado por:

a) designador da empresa de transporte aéreo obtido junto à OACI; ou

b) designação "GERAL", caso não haja o designador OACI;

VI - Campo 6 - VOO\_OUTRO\_AEROPORTO: tem formato é alfanumérico e é representado pelo código OACI designado ao aeroporto definido como:

a) em caso de POUSO, refere-se ao aeroporto anterior, onde ocorreu o último processamento de passageiros, cargas ou correio antes do pouso em questão;

b) em caso de DECOLAGEM, refere-se ao aeroporto posterior, onde ocorreu o primeiro processamento de passageiros, cargas ou correio após a decolagem em questão;

VII - Campo 7 - VOO\_NUMERO: refere-se à identificação do voo da aeronave que tenha pousado no aeroporto (em caso de movimento de POUSO) ou decolado deste (em caso de movimento de DECOLAGEM). O formato é numérico e é representado pelo número do voo. Caso não se aplique, utilizar "0";

VIII - Campo 8 - SERVICE\_TYPE: refere-se ao tipo de voo realizado pela aeronave, conforme codificação constante no "APPENDIX C - SERVICE TYPES" do "Standart Schedules Information Manual", publicado pela IATA, ou eventuais códigos que venham a substituí-los, considerando-se ainda as seguintes codificações como padrão:

a) Y, para voos alternados;

b) Z, para voos de retorno;

IX - Campo 9 - NATUREZA: refere-se à natureza da operação realizada pela aeronave. O formato é alfabético e é representado por:

a) D, caso o voo seja doméstico, ou seja, voos realizados por aeronave de matrícula brasileira, em que os pontos de partida, intermediário, se houver, e de destino estão situados no território brasileiro; e

b) I, caso o voo seja internacional, ou seja, voos realizados por aeronave de matrícula estrangeira, em qualquer situação; ou por aeronave de matrícula brasileira, quando procedente ou destinada ao exterior, independente de escalas no território brasileiro, ou ainda, quando executando fretamento em complementação de voo internacional;

X - Campo 10 - PREVISTO\_DATA: refere-se à data prevista, conforme o horário local do aeroporto, para a realização do movimento informado (pouso ou decolagem). O formato é data e é representado por DD/MM/AAAA, onde DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010);

XI - Campo 11 - PREVISTO\_HORARIO: refere-se ao horário local previsto para a realização do movimento informado (pouso ou decolagem). O formato é hora e é representado por HH:MM, onde HH representa a hora (00 - 23) e MM representa os minutos (00 - 59). Ambos devem possuir 2 (dois) caracteres e ser informado no padrão 24 (vinte e quatro) horas;

XII - Campo 12 - CALCO\_DATA: refere-se à data em que ocorreu o movimento informado (pouso ou decolagem), conforme o horário local, apurado pelo critério do calço e descalço, conhecido internacionalmente pelo termo em inglês block-to-block. O formato é data e é representado por DD/MM/AAAA, onde DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010);

XIII - Campo 13 - CALCO\_HORARIO: refere-se ao horário de realização do movimento informado (pouso ou decolagem), conforme o horário local, apurado pelo critério do calço e descalço, conhecido internacionalmente pelo termo em inglês block-to-block. O formato é hora e é representado por HH:MM, onde HH representa a hora (00 - 23) e MM representa os minutos (00 - 59). Ambos devem possuir 2 (dois) caracteres e ser informado no padrão 24 (vinte e quatro) horas;

XIV - Campo 14 - TOQUE\_DATA: refere-se à data em que ocorreu o movimento informado (pouso ou decolagem), conforme horário local, apurada pelo critério do contato da aeronave com o solo, conhecido internacionalmente pelos termos em inglês wheels-on e wheels-off. O formato é data e é representado por DD/MM/AAAA, onde DD representa o dia (01 - 31), MM representa o mês (01 - 12), e AAAA representa o ano (ex. 2010);

XV - Campo 15 - TOQUE\_HORARIO: refere-se ao horário em que ocorreu o movimento informado (pouso ou decolagem), conforme horário local, apurado pelo critério do contato da aeronave com o solo, conhecido internacionalmente pelos termos em inglês wheels-on e wheels-off. O formato é hora e é representado por HH:MM, onde HH representa a hora (00 - 23) e MM representa os minutos (00 - 59). Ambos devem possuir 2 (dois) caracteres e ser informado no padrão 24 (vinte e quatro) horas;

XVI - Campo 16 - CABECEIRA: refere-se à cabeceira de pista por onde ocorreu o movimento informado (pouso ou decolagem). O formato é alfanumérico e é representado pelo identificador da cabeceira de pista;

XVII - Campo 17 - BOX: refere-se à posição de pátio onde ocorreu o desembarque, em caso de pouso, ou o embarque, em caso de decolagem. O formato é alfanumérico e é representado pelo identificador da posição de pátio cadastrada. Preencher com "N/A" caso o movimento em questão não utilize uma posição de pátio cadastrada pela ANAC;

XVIII - Campo 18 - PONTE\_CONECTOR\_REMOTO: refere-se ao tipo de instrumento utilizado para o desembarque dos passageiros, em caso de pouso, ou o embarque de passageiros, em caso de decolagem. O formato é numérico e é representado por:

a) 1, caso tenha sido utilizado ponte de embarque e desembarque de passageiros;

b) 2, caso tenha sido utilizado o modo conector remoto acessível para embarque e desembarque de passageiros, excluído a opção descrita na alínea 'a'. Conector remoto acessível - equipamento utilizado para o embarque ou desembarque de passageiros, com o fluxo direto dos passageiros entre o terminal e a aeronave, de forma abrigada de sol, chuva, vento, gases, risco de chama, que seja climatizado e sem desníveis ao longo do trajeto, ou com elevador e/ou rampa para superação de desnível junto à aeronave, quando houver;

c) 3, caso tenha sido realizado o modo remoto para o embarque ou desembarque de passageiros, quando o passageiro se desloca entre o terminal e a aeronave andando, sem usufruir de qualquer facilitação, ou por meio de veículo dedicado ao transporte terrestre dos passageiros, tais como ônibus e vans, ou quando não enquadrado nas opções descritas nas alíneas 'a' ou 'b'; ou

d) 4, caso o movimento em questão não apresente pessoas embarcadas ou desembarcadas por meio do terminal de passageiros;

XIX - Campo 19 - TERMINAL: refere-se ao terminal de passageiros utilizado para o desembarque, em caso de pouso, ou o embarque, em caso de decolagem. O formato é alfanumérico e é representado pelo número ou letra que identifica o terminal utilizado. Preencher com "N/A" caso não se aplique;

XX - Campo 20 - PAX\_LOCAL: tem formato numérico e deve ser entendido como se segue:

a) em caso de POUSO, refere-se ao número de passageiros que desembarcaram de uma aeronave, e finalizaram a sua viagem no aeroporto;

b) em caso de DECOLAGEM, refere-se ao número de passageiros que embarcaram em uma aeronave com a finalidade de iniciar um voo, e que inicia a sua viagem no aeroporto;

c) preencher com caractere 0 (zero) caso o voo não possua passageiros que se enquadrem nas condições das alíneas a ou b desse inciso;

XXI - Campo 21 - PAX\_CONEXAO\_DOMESTICO: representa à quantidade de passageiros que desembarcaram para reembarcar no mesmo aeroporto, na mesma aeronave ou em outra, em prosseguimento à mesma viagem, independente de mudança de companhia aérea, desde que constante do mesmo contrato de transporte. Tem formato numérico e deve ser entendido como se segue:

a) em caso de POUSO, refere-se a quantidade de passageiros que desembarcaram neste aeroporto para reembarcar em conexão em um voo doméstico;

b) em caso de DECOLAGEM, refere-se a quantidade de passageiros que embarcaram em conexão neste aeroporto, provenientes de um voo doméstico;

c) preencher com caractere 0 (zero) caso o voo não possua passageiros que se enquadrem nas condições das alíneas a ou b desse inciso;

XXII - Campo 22 - PAX\_CONEXAO\_INTERNACIONAL: representa à quantidade de passageiros que desembarcaram para reembarcar no mesmo aeroporto, na mesma aeronave ou em outra, em prosseguimento à mesma viagem, independente de mudança de companhia aérea, desde que constante do mesmo contrato de transporte. Tem formato numérico e deve ser entendido como se segue:

a) em caso de POUSO, refere-se à quantidade de passageiros que desembarcaram neste aeroporto para reembarcar em conexão em um voo internacional;

b) em caso de DECOLAGEM, refere-se à quantidade de passageiros que embarcaram em conexão neste aeroporto, provenientes de um voo internacional;

c) preencher com caractere 0 (zero) caso o voo não possua passageiros que se enquadrem nas condições das alíneas a ou b desse inciso;

XXIII - Campo 23 - CORREIO: refere-se à quantidade de correspondências e outros objetos confiados pelas administrações postais à empresa aérea, expresso em quilogramas, que tenha desembarcado da aeronave, em caso de pouso, ou embarcado na aeronave, em caso de decolagem. O formato é numérico. Preencher com caractere 0 (zero) caso não tenha desembarcado ou embarcado da aeronave no aeroporto correspondências e outros objetos;

XXIV - Campo 24 - CARGA: refere-se à quantidade de todos bens transportados na aeronave, expressa em quilogramas, que tenha desembarcado da aeronave, em caso de pouso, ou embarcado na aeronave, em caso de decolagem, excluindo correio, provisões de bordo, bagagens de mão e bagagens despachadas. O formato é numérico. Preencher com caractere 0 (zero) caso não tenha embarcado ou desembarcado carga da aeronave no aeroporto;

XXV - Campo 25 - RETORNO\_ALTERNADO: Este campo refere-se à informação se o voo é de retorno ou alternado, sendo de envio opcional para os aeroportos que optem por seguir o padrão de reporte de voos de retorno e alternados sugerido para o Campo SERVICE\_TYPE. O formato é alfabético e é representado por:

a) R, para voos de retorno;

b) A, para voos alternados;

c) N, ou vazio, para os casos em que o voo não seja de retorno ou alternado;

XXVI - Campo 26 - CONTESTACAO: Este campo é de envio opcional e se refere à informação de se as informações do voo foram recebidas pelo aeroporto e carregadas no sistema que gera o RIMA. O formato é alfabético e é representado por:

a) NE, para voos cujas informações não foram enviadas pelo operador aéreo;

b) NC, para voos cujas informações foram enviadas pelo operador aéreo, entretanto, por motivos sistêmicos, não foi possível realizar a carga das informações no sistema aeroportuário responsável pela geração do RIMA;

c) CO, para voos cujas informações, embora fornecidas pelo operador aéreo e carregadas no sistema responsável pela criação do RIMA, foram contestadas e estão pendentes de resposta por parte do operador aéreo;

d) DV, para voos cujas informações, embora fornecidas pelo operador aéreo e carregadas no sistema responsável pela criação do RIMA, foram contestadas e respondidas, permanecendo a divergência de atendimento dos dados apresentados;

e) Vazio, para os casos em que o voo contenha as informações enviadas pelo operador aéreo e não haja contestação pendente;

**§ 1º** Para fins de apresentação do RIMA à ANAC, considera-se:

I - pouso realizado no mês de referência dos dados: pouso em que a data de calço da aeronave ocorreu durante o mês de referência; e

II - decolagem realizada no mês de referência dos dados: decolagem em que a data de descalço da aeronave ocorreu durante o mês de referência.

**§ 2º** Quando o pouso ou a decolagem estiver associada à operação de aeronaves do Grupo II, exceto táxi-aéreo, o campo previsto no inciso VIII deverá estar preenchido com o código referente à aviação geral e os campos previstos nos incisos XX a XXV poderão não ser preenchidos quando as informações não estiverem disponíveis.

**§ 3º** Quando o pouso ou a decolagem estiver associada à operação de uma aeronave militar, o campo previsto no inciso VIII deverá estar preenchido com o código referente à operação militar e os campos definidos nos incisos V a VII, IX a XIII e XVII a XXV poderão não ser preenchidos quando as informações não estiverem disponíveis.

**§ 4º** O envio do Campo 25, incluindo as informações do cabeçalho, é opcional para os aeroportos que sigam a padronização sugerida no Campo 8 - SERVICE\_TYPE para os códigos 'Y' e 'Z'.

**§ 5º** O padrão disposto nas alíneas "a" e "b" do inciso VIII do caput não é obrigatório caso o aeroporto opte por enviar as informações do campo 25 - RETORNO\_ALTERNADO." (NR)

"Art. 9º-A O administrador aeroportuário deverá apresentar, na data de envio do RIMA, lista em formato eletrônico que seja possível identificar sistemicamente o movimento constante no RIMA enviado, contendo os movimentos cujo envio da informação não foi efetuado pela empresa aérea ou que a carga das informações no banco de dados do aeroporto tenha sido inviabilizada, casos existam tais movimentos.

**Parágrafo único.** O envio da lista contida no caput deste artigo é opcional aos aeroportos que optem por realizar o envio do Campo 26 do RIMA." (NR)

"Art. 9º-B O operador aeroportuário apresentará, na data de envio do RIMA, comprovantes das contestações efetuadas às empresas aéreas, que não tenham sido sanadas, caso existam.

**Parágrafo único.** Isenta-se desta comprovação o administrador aeroportuário que disponibilizar às empresas aéreas as informações passíveis de contestação em plataforma informatizada de verificação em tempo real - on-line." (NR)

**§ 1º** Ficam suprimidas as alíneas "a" e "b" do inciso IV, "a" a "j" do inciso V, "c" a "e" do inciso VIII, "a" a "d" do inciso XVII, e "a" a "c" do inciso XIX do art. 8º da Portaria nº 1.017/SRA/SIA, de 26 de 2018.

**§ 2º** O Anexo III da Portaria 1.017/SRA/SIA, de 26 de março de 2018, passa a vigorar na forma do Anexo desta Portaria.

**Art. 2º** Os administradores aeroportuários deverão adequar o formato e conteúdo do RIMA a ser enviado à ANAC até 2 de outubro de 2019, devendo o envio do arquivo subsequente a esta data ser enviado no formato disposto nesta Portaria.

**Parágrafo único.** Durante o período de adequação, o administrador aeroportuário poderá enviar o conteúdo do Campo 1 ("COD\_RIMA") vazio.

**Art. 3º** Esta Portaria entra em vigor na data de sua publicação.

TIAGO SOUSA PEREIRA

Superintendente de Regulação Econômica de Aeroportos

RAFAEL JOSÉ BOTELHO FARIA

Superintendente de Infraestrutura Aeroportuária

## ANEXO

ANEXO III DA PORTARIA 1.017/SRA/SIA, DE 26 DE MARÇO DE 2018.

RELATÓRIO DE INFORMAÇÕES DE MOVIMENTAÇÃO AEROPORTUÁRIA

<table><tr></tr><tr><td><p>CAMPO</p></td><td><p>DADO</p></td><td><p>DESCRIÇÃO</p></td><td><p>FORMATO</p></td><td><p>FORMATO/ DOMÍNIO</p></td><td><p>Exemplo de Resposta</p></td></tr><tr><td><p>1</p></td><td><p>COD_RIMA</p></td><td><p>Código do próprio aeroporto que identifique a operação aeroportuária como única, sendo igual no pouso e na decolagem</p></td><td><p>Alfanumérico</p></td><td><p></p></td><td><p>1</p></td></tr><tr><td><p>2</p></td><td><p>MOVIMENTO_TIPO</p></td><td><p>Tipo de movimento reportado: pouso ou decolagem.</p></td><td><p>Alfabético</p></td><td><p>P / D</p></td><td><p>P</p></td></tr><tr><td><p>3</p></td><td><p>AERONAVE_MARCAS</p></td><td><p>Marcas de Nacionalidade e Matrícula da Aeronave.</p></td><td><p>Alfanumérico</p></td><td><p></p></td><td><p>PTMDB</p></td></tr><tr><td><p>4</p></td><td><p>AERONAVE_TIPO</p></td><td><p>Designador OACI do Modelo da Aeronave ou Equipamento.</p></td><td><p>Alfanumérico</p></td><td><p>XXXX</p></td><td><p>A320</p></td></tr><tr><td><p>5</p></td><td><p>AERONAVE_OPERADOR</p></td><td><p>Designador OACI da Empresa Aérea (ou GERAL caso não exista esse designador).</p></td><td><p>Alfanumérico</p></td><td><p></p></td><td><p>VRG</p></td></tr><tr><td><p>6</p></td><td><p>VOO_OUTRO_AEROPORTO</p></td><td><p>Designador OACI do Aeroporto de anterior (em caso de pouso) ou posterior (caso de decolagem).</p></td><td><p>Alfanumérico</p></td><td><p>XXXX</p></td><td><p>SBMK</p></td></tr><tr><td><p>7</p></td><td><p>VOO_NUMERO</p></td><td><p>Número do voo de pouso ou decolagem.</p></td><td><p>Numérico</p></td><td><p>Nº inteiro não negativo</p></td><td><p>4243</p></td></tr><tr><td><p>8</p></td><td><p>SERVICE_TYPE</p></td><td><p>Tipo de Voo realizado pela aeronave conforme APPENDIX C - SERVICE TYPES do SSIM/IATA</p></td><td><p>Alfabético</p></td><td><p></p></td><td><p>J</p></td></tr><tr><td><p>9</p></td><td><p>NATUREZA</p></td><td><p>Natureza da operação realizada pela aeronave</p></td><td><p>Alfabético</p></td><td><p>D, I</p></td><td><p>D</p></td></tr><tr><td><p>10</p></td><td><p>PREVISTO_DATA</p></td><td><p>Dia, mês e ano previsto para o pouso ou decolagem, conforme horário local (do aeroporto).</p></td><td><p>Data</p></td><td><p>dd/mm/aaaa</p></td><td><p>08/03/2013</p></td></tr><tr><td><p>11</p></td><td><p>PREVISTO_HORARIO</p></td><td><p>Hora e minuto previsto para o pouso ou decolagem, conforme horário local (do aeroporto).</p></td><td><p>Hora</p></td><td><p>hh:mm</p></td><td><p>17:50</p></td></tr><tr><td><p>12</p></td><td><p>CALCO_DATA</p></td><td><p>Dia, mês e ano da realização da operação de calço dentro ou calço fora, conforme horário local (do aeroporto).</p></td><td><p>Data</p></td><td><p>dd/mm/aaaa</p></td><td><p>08/03/2013</p></td></tr><tr><td><p>13</p></td><td><p>CALCO_HORARIO</p></td><td><p>Hora e minuto da realização do calço dentro ou calço fora, conforme horário local (do aeroporto).</p></td><td><p>Hora</p></td><td><p>hh:mm</p></td><td><p>17:50</p></td></tr><tr><td><p>14</p></td><td><p>TOQUE_DATA</p></td><td><p>Dia, mês e ano de realização de toque de pista, conforme horário local (do aeroporto).</p></td><td><p>Data</p></td><td><p>dd/mm/aaaa</p></td><td><p>08/03/2013</p></td></tr><tr><td><p>15</p></td><td><p>TOQUE_HORARIO</p></td><td><p>Hora e minuto da realização do toque de pista, conforme horário local (do aeroporto).</p></td><td><p>Hora</p></td><td><p>hh:mm</p></td><td><p>17:50</p></td></tr><tr><td><p>16</p></td><td><p>CABECEIRA</p></td><td><p>Identificador da cabeceira onde ocorreu o pouso ou decolagem.</p></td><td><p>Alfanumérico</p></td><td><p></p></td><td><p>44R</p></td></tr><tr><td><p>17</p></td><td><p>BOX</p></td><td><p>Identificador da posição de pátio onde ocorreu o embarque ou desembarque.</p></td><td><p>Alfanumérico</p></td><td><p></p></td><td><p>34L</p></td></tr><tr><td><p>18</p></td><td><p>PONTE_CONECTOR_REMOTA</p></td><td><p>Instrumento utilizado para o embarque ou desembarque dos passageiros.</p></td><td><p>Numérico</p></td><td><p>1, 2, 3 ou 4</p></td><td><p>2</p></td></tr><tr><td><p>19</p></td><td><p>TERMINAL</p></td><td><p>Identificador do terminal de embarque ou desembarque.</p></td><td><p>Alfanumérico</p></td><td><p></p></td><td><p>2</p></td></tr><tr><td><p>20</p></td><td><p>PAX_LOCAL</p></td><td><p>Passageiros embarcados de origem ou passageiros desembarcados de destino (não fizeram conexão de voo).</p></td><td><p>Numérico</p></td><td><p>Nº inteiro não negativo</p></td><td><p>22</p></td></tr><tr><td><p>21</p></td><td><p>PAX_CONEXAO_DOMESTICO</p></td><td><p>Passageiros embarcados ou desembarcados que fizeram conexão em voo doméstico.</p></td><td><p>Numérico</p></td><td><p>Nº inteiro não negativo</p></td><td><p>33</p></td></tr><tr><td><p>22</p></td><td><p>PAX_CONEXAO_INTERNACIONAL</p></td><td><p>Passageiros embarcados ou desembarcados que fizeram conexão em voo internacional.</p></td><td><p>Numérico</p></td><td><p>Nº inteiro não negativo</p></td><td><p>0</p></td></tr><tr><td><p>23</p></td><td><p>CORREIO</p></td><td><p>Mala postal embarcada ou desembarcada nesse aeroporto (Kg).</p></td><td><p>Numérico</p></td><td><p>Nº inteiro não negativo</p></td><td><p>44</p></td></tr><tr><td><p>24</p></td><td><p>CARGA</p></td><td><p>Carga embarcada ou desembarcada nesse aeroporto (Kg), exceto bagagens, provisões de bordo e correio.</p></td><td><p>Numérico</p></td><td><p>Nº inteiro não negativo</p></td><td><p>123</p></td></tr><tr><td><p>25</p></td><td><p>RETORNO_ALTERNADO</p></td><td><p>Identificador da Operação como Retorno ou Alternado (Campo opcional caso seja seguido o padrão sugerido para o Campo 8)</p></td><td><p>Alfabético</p></td><td><p>R, A, N, ou vazio</p></td><td><p>R</p></td></tr><tr><td><p>26</p></td><td><p>CONTESTACAO</p></td><td><p>Campo Opcional que identifica a presença de contestação no voo informado</p></td><td><p>Alfabético</p></td><td><p>NE, NC, CO, DV, ou vazio</p></td><td><p>NE</p></td></tr></table>
