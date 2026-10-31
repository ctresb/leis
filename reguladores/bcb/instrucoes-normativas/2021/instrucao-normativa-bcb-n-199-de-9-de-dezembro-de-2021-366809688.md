---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 199, DE 9 DE DEZEMBRO DE 2021"
orgao: "Ministério da Economia/Banco Central do Brasil/Área de Organização do Sistema Financeiro e de Resolução/Departamento de Competição e de Estrutura do Mercado Financeiro"
tipo: "Instrução Normativa"
numero: "199"
data: 2021-12-09
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 13/12/2021, seção 1, p. 54"
data_publicacao: 2021-12-13
edicao: "233"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-199-de-9-de-dezembro-de-2021-366809688"
sha256_html_fonte: bfcf3c37fa55dfb1c16894815011551568710d744536c6922937584eaf3fdfc6
baixado_em: 2026-10-21
---
# INSTRUÇÃO NORMATIVA BCB Nº 199, DE 9 DE DEZEMBRO DE 2021

INSTRUÇÃO NORMATIVA BCB Nº 199, DE 9 DE DEZEMBRO DE 2021

Estabelece os procedimentos operacionais para a cobrança e para a efetuação do ressarcimento de custos operacionais referente a cada Pix com finalidade de saque ou de troco.

O Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro (Decem) e o Chefe do Departamento de Operações Bancárias e de Sistema de Pagamentos (Deban), no uso das atribuições que lhes conferem, respectivamente, o art. 97-A, inciso X, e o art. 111, inciso V, do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, e tendo em conta o disposto no § 6º do art. 96-B do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020, resolvem:

**Art. 1º** A cobrança do ressarcimento de custos operacionais referente a cada Pix com finalidade de saque ou de troco será operacionalizada pelo Banco Central do Brasil a partir das informações contidas nas ordens de pagamentos instantâneos liquidadas no Sistema de Pagamentos Instantâneos (SPI).

**§ 1º** A cobrança de que trata o caput será efetuada mensalmente e considerará todas as transações Pix com finalidade de saque ou de troco liquidadas no SPI e realizadas no mês imediatamente anterior ao mês da cobrança.

**§ 2º** O Banco Central do Brasil disponibilizará até o quinto dia útil de cada mês:

I - arquivo com informações referentes às transações Pix com finalidade de saque ou de troco liquidadas no SPI em que o participante direto do SPI que está requisitando o arquivo atua como:

a) prestador de serviços de pagamento do usuário pagador;

b) prestador de serviços de pagamento do usuário recebedor;

c) facilitador de serviço de saque;

d) liquidante do prestador de serviços de pagamento do usuário pagador;

e) liquidante do prestador de serviços de pagamento do usuário recebedor;

f) liquidante do facilitador de serviço de saque;

II - arquivo com a posição líquida devedora ou credora do participante direto do SPI que está requisitando o arquivo em relação a cada um dos demais participantes diretos do SPI.

**§ 3º** Cada um dos arquivos de que trata o § 2º será disponibilizado apenas para os participantes diretos do SPI, a partir de requisição comandada pelo participante por meio da mensagem camt.060, respondida por meio da mensagem camt.052, observados os formatos, padrões e especificações constantes do Catálogo de Serviços do SFN.

**Art. 2º** Fica o participante direto do SPI responsável por calcular a posição líquida de cada um dos participantes indiretos do SPI para os quais ele presta serviço de liquidação, em relação:

I - a ele próprio;

II - às transações Pix com finalidade de saque ou de troco realizadas com os demais participantes indiretos do SPI para os quais ele presta serviço de liquidação.

**Parágrafo único.** A posição líquida de que trata o caput deve:

I - ser calculada mensalmente;

II - considerar as transações Pix com finalidade de saque ou de troco liquidadas nos sistemas do próprio participante direto do SPI e que envolvam facilitador de serviço de saque que utiliza serviço de liquidação desse participante direto do SPI, liquidadas no mês imediatamente anterior ao mês de cálculo da posição líquida;

III - ser enviada pelo participante direto do SPI para cada um dos participantes indiretos do SPI para os quais ele presta serviço de liquidação até o oitavo dia útil do mês em que o cálculo foi realizado.

**Art. 3º** O pagamento das posições líquidas a que se refere o inciso II do §2 do art. 1º será realizado por meio de Transferência Eletrônica Disponível (TED).

**§ 1º** Os participantes diretos do SPI devem ressarcir os custos operacionais de cada um dos demais participantes diretos do SPI, sempre que a sua posição líquida for devedora em relação a cada um deles, no valor correspondente ao discriminado no arquivo de que trata o inciso II do § 2º do art. 1º.

**§ 2º** O ressarcimento de que trata o caput deve ser realizado:

I - até o décimo dia útil de cada mês, referente às transações efetuadas no mês imediatamente anterior;

II - por meio de mensagem do Grupo de Serviços STR, ou do Grupo de Serviços PAG, conforme o caso, instruída com finalidade específica, nos termos do Catálogo de Serviços do SFN, observado o seguinte:

a) quando ambos os participantes diretos do SPI envolvidos no ressarcimento forem participantes do STR, deverá ser utilizada a mensagem STR0004 - IF requisita Transferência para IF;

b) quando o participante direto do SPI que efetuará o ressarcimento for participante do STR, mas o participante direto do SPI que será ressarcido não participar do STR, deverá ser utilizada a mensagem STR0007 - IF requisita Transferência de IF para conta de cliente;

c) quando o participante direto do SPI que efetuará o ressarcimento não for participante do STR, mas o participante direto do SPI que será ressarcido for participante do STR, deverá ser utilizada a mensagem STR0006 - IF requisita Transferência de cliente para IF ou a mensagem PAG0142 - IF requisita Transferência de recursos de cliente para IF por conta de operação de varejo; e

d) quando ambos os participantes diretos do SPI envolvidos no ressarcimento não forem participantes do STR, deverá ser utilizada a mensagem STR0008 - IF requisita Transferência entre contas de clientes ou a mensagem PAG0108 - IF requisita Transferência de recursos entre contas de clientes.

**Art. 4º** O ressarcimento dos custos operacionais referente a cada transação Pix com finalidade de saque ou de troco liquidada nos sistemas dos participantes diretos do SPI e que envolva facilitador de serviço de saque que utiliza serviço de liquidação desse participante direto do SPI deve ser realizado até o décimo dia útil de cada mês, referente às transações efetuadas no mês imediatamente anterior.

**Parágrafo único.** Os procedimentos operacionais para o ressarcimento de que trata o caput devem ser estabelecidos livremente entre as partes no contrato de prestação de serviço de liquidação entre o participante direto do SPI e o participante indireto do SPI.

**Art. 5º** O facilitador de serviço de saque deve distribuir a parcela que cabe ao agente de saque referente à disponibilização do Pix Saque e/ou Pix Troco de que trata o § 5º do art. 96-B do Regulamento anexo à Resolução BCB nº 1 (Regulamento do Pix), de 12 de agosto de 2020, até o décimo quinto dia útil de cada mês, referente às transações Pix com finalidade de saque ou de troco ocorridas no mês imediatamente anterior.

**Parágrafo único.** Os procedimentos operacionais para a distribuição de que trata o caput deve seguir o disposto na relação contratual entre o facilitador de serviço de saque e o agente de saque, conforme previsto no § 1º do art. 11-L do Regulamento do Pix.

**Art. 6º** A não efetivação do ressarcimento de custos operacionais referente a cada transação Pix com finalidade de saque ou de troco nos prazos estabelecidos nos arts. 3º, 4º e 5º acarretará multa de mora de 2% (dois por cento) e juros de mora de 1% (um por cento) ao mês, incidentes sobre as posições devedoras do participante do Pix que deu causa ao atraso.

**§ 1º** A cobrança da não efetivação do ressarcimento dos custos operacionais será de responsabilidade do participante do Pix credor.

**§ 2º** A não efetivação do ressarcimento de custos operacionais em um determinado mês não afeta os procedimentos de cobrança e de pagamento referentes aos meses subsequentes.

**Art. 7º** É facultado ao participante direto do SPI requerer a revisão do valor cobrado, de que trata o § 1º do art. 1º, devendo, para tanto, apresentar pedido fundamentado ao Decem, por meio do endereço estatísticas.spb@bcb.gov.br.

**Art. 8º** Ficam revogadas:

I - a Instrução Normativa BCB nº 151, de 3 de setembro de 2021; e

II - a Instrução Normativa BCB nº 189, de 26 de novembro de 2021.

**Art. 9º** Esta Instrução Normativa entre em vigor na data de sua publicação.

Angelo José Mont Alverne Duarte

Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro

Rogério Antônio Lucca

Chefe do Departamento de Operações Bancárias e de Sistema de Pagamentos
