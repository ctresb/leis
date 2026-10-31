---
titulo: "INSTRUÇÃO NORMATIVA - IN ANS Nº 8, DE 30 DE MARÇO DE 2022"
orgao: "Ministério da Saúde/Agência Nacional de Saúde Suplementar"
tipo: "Instrução Normativa"
numero: "8"
data: 2022-03-30
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 04/04/2022, seção 1, p. 109"
data_publicacao: 2022-04-04
edicao: "64"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-in-ans-n-8-de-30-de-marco-de-2022-390370361"
sha256_html_fonte: b514d6252868308ff9bc41ba0cf997026ebfeb60237fc3e5275535cd149e73dd
baixado_em: 2026-10-20
---
# INSTRUÇÃO NORMATIVA - IN ANS Nº 8, DE 30 DE MARÇO DE 2022

INSTRUÇÃO NORMATIVA - IN ANS Nº 8, DE 30 DE MARÇO DE 2022

Dispõe sobre o formato XML (Extensible Markup Language) para a transmissão das informações para o Sistema de Informações de Beneficiários da Agência Nacional de Saúde Suplementar - SIB/ANS; estabelece procedimentos para a geração, validação, transmissão e controle de dados cadastrais de beneficiários do SIB/ANS; e revoga as Instruções Normativas DIDES nº 50, de 25 de setembro de 2012, nº 55, de 03 de dezembro de 2014, nº 57, de 28 de abril de 2015 e nº 69, de 19 de julho de 2019.

A Diretoria Colegiada da Agência Nacional de Saúde Suplementar - ANS, no uso das atribuições que lhe confere o art.24, inciso III, da Resolução Regimental nº 21, de 26 de janeiro de 2022, e considerando a aprovação em reunião realizada em 30 de março de 2022, adotou a seguinte Instrução Normativa e eu, Diretor-Presidente, determino a sua publicação.

#### CAPÍTULO I — DAS DISPOSIÇÕES PRELIMINARES

**Art. 1º** Esta Instrução Normativa dispõe sobre o formato XML (Extensible Markup Language) como padrão para a troca de informações entre as operadoras e o Sistema de Informações de Beneficiários da Agência Nacional de Saúde Suplementar - SIB/ANS; estabelece procedimentos para a geração, validação, transmissão e controle de dados cadastrais de beneficiários do SIB/ANS e revoga as Instruções Normativas DIDES nº 50, de 25 de setembro de 2012, nº 55, de 03 de dezembro de 2014, nº 57, de 28 de abril de 2015 e nº 69, de 19 de julho de 2019.

**Parágrafo único.** As definições de que trata o art. 2º da Resolução Normativa nº 500, de 30 de março de 2022, são aplicadas para fins desta IN.

**Art. 2º** O envio de dados cadastrais de beneficiários para a ANS será efetuado somente por meio do SIB/ANS, em formato XML.

**§ 1º** O envio de dados cadastrais de beneficiários deve atender às especificações de formato, tamanho e domínio dos campos de dados, definidas nos arquivos XSD (XML Schema Definition) previstos nesta norma, sob pena de os arquivos serem rejeitados.

**§ 2º** A rejeição de um arquivo de atualização de dados (SBX) caracteriza o não envio das informações contidas nesse arquivo.

**Art. 3º** As orientações para o envio de dados cadastrais de beneficiário, o aplicativo de transmissão dos arquivos em formato XML e os arquivos XSD encontram-se à disposição no endereço eletrônico da ANS na Internet, na aba SIB da página Aplicativos ANS.

**Art. 4º** O Anexo I desta Instrução Normativa define a obrigatoriedade de preenchimento dos campos de dados para cada procedimento de atualização cadastral previsto nesta norma.

**Art. 5º** O Anexo II desta Instrução Normativa define o calendário de envio e de retirada dos arquivos que compõem o processo de atualização cadastral.

#### CAPÍTULO II — DAS REGRAS DE IDENTIFICAÇÃO DE BENEFICIÁRIO

##### Seção I — Das Disposições Gerais Sobre as Regras de Identificação de Beneficiário

**Art. 6º** Os dados de identificação pessoal, de identificação de endereço e de identificação contratual compõem o registro de vínculo de cada beneficiário na base de dados das operadoras na ANS, da seguinte forma:

I - dados de identificação pessoal:

a) Código de Controle Operacional (CCO);

b) código de identificação do beneficiário na operadora;

c) nome do beneficiário;

d) data de nascimento do beneficiário;

e) código de sexo do beneficiário;

f) número de inscrição no Cadastro de Pessoa Física (CPF) do beneficiário;

g) número de inscrição no Programa de Integração Social (PIS) ou no Programa de Formação do Patrimônio do Servidor Público (PASEP) ou Número de Identificação do Trabalhador (NIT);

h) nome da mãe do beneficiário;

i) número do Cartão Nacional de Saúde do beneficiário;

j) número da Declaração de Nascido Vivo para os beneficiários nascidos a partir de 1º de janeiro de 2010; e

k) código de identificação do beneficiário titular na operadora, para beneficiários informados como dependentes (não-titulares);

II - dados de identificação de endereço:

a) indicação de endereço residencial ou profissional;

b) logradouro do beneficiário;

c) número do logradouro;

d) complemento do logradouro;

e) bairro;

f) código do município do logradouro indicado, sem o dígito verificador;

g) Código de Endereçamento Postal (CEP);

h) indicação se a residência do beneficiário é no Brasil ou no exterior; e

i) código do município de residência do beneficiário, caso o endereço informado seja indicado como endereço profissional;

III - dados de identificação contratual:

a) número de registro do plano na ANS (RPS);

b) código do cadastro do plano na ANS (SCPA);

c) número do registro do plano de origem no RPS, nos casos de portabilidade;

d) data de contratação do plano;

e) data de cancelamento do plano;

f) código do motivo do cancelamento do plano;

g) data de reativação do plano;

h) indicação de existência de Cobertura Parcial Temporária (CPT);

i) indicação de existência de itens de procedimentos excluídos da cobertura;

j) número no Cadastro Nacional de Pessoa Jurídica (CNPJ) da pessoa jurídica contratante do plano coletivo empresarial ou do plano coletivo por adesão;

k) número no Cadastro de Atividade Econômica da Pessoa Física - CAEPF do contratante do plano coletivo empresarial ou do plano coletivo por adesão; e

l) relação de dependência.

##### Seção II — Do Preenchimento dos Dados de Identificação Pessoal do Beneficiário

**Art. 7º** A operadora deve preencher os dados de identificação pessoal do beneficiário da seguinte forma:

I - para titulares menores ou maiores de 18 (dezoito) anos:

a) são de preenchimento obrigatório:

1\. CCO;

2\. código de identificação do beneficiário na operadora;

3\. nome do beneficiário;

4\. data de nascimento do beneficiário;

5\. código de sexo do beneficiário;

6\. número do CPF do beneficiário; e

7\. número do Cartão Nacional de Saúde do beneficiário.

b) são de preenchimento restritivo, ou seja, deverá ser preenchido pelo menos um dos campos a seguir, sob pena de rejeição do registro de vínculo do beneficiário:

1\. nome da mãe do beneficiário;

2\. número de inscrição no PIS ou no PASEP ou NIT.

c) é de preenchimento opcional o número da Declaração de Nascido Vivo para os beneficiários nascidos a partir de 1º de janeiro de 2010.

II - para dependentes maiores de 18 (dezoito) anos:

a) são de preenchimento obrigatório:

1\. CCO;

2\. código de identificação do beneficiário na operadora;

3\. nome do beneficiário;

4\. data de nascimento do beneficiário;

5\. código de sexo do beneficiário;

6\. número do CPF do beneficiário;

7\. código de identificação do beneficiário titular na operadora para beneficiários informados como dependentes (não-titulares); e

8\. número do Cartão Nacional de Saúde do beneficiário.

b) são de preenchimento restritivo, ou seja, deverá ser preenchido pelo menos um dos campos a seguir, sob pena de rejeição do registro de vínculo do beneficiário:

1\. nome da mãe do beneficiário;

2\. número de inscrição no PIS ou no PASEP ou NIT.

III - para dependentes menores de 18 (dezoito) anos:

a) são de preenchimento obrigatório:

1\. CCO;

2\. código de identificação do beneficiário na operadora;

3\. nome do beneficiário;

4\. data de nascimento do beneficiário;

5\. código de sexo do beneficiário;

6\. código de identificação do beneficiário titular na operadora para beneficiários informados como dependentes (não-titulares);

7\. número do Cartão Nacional de Saúde do beneficiário.

b) são de preenchimento restritivo, ou seja, deverá ser preenchido pelo menos um dos campos a seguir, sob pena de rejeição do registro de vínculo do beneficiário:

1\. nome da mãe do beneficiário;

2\. número do CPF do beneficiário; e

3\. número de inscrição no PIS ou no PASEP ou NIT.

c) é de preenchimento opcional o número da Declaração de Nascido Vivo para os beneficiários nascidos a partir de 1º de janeiro de 2010.

**§ 1°** O campo "Código de Controle Operacional - CCO" não deve ser preenchido nos procedimentos de inclusão de beneficiário no SIB/ANS.

**§ 2º** A operadora deve informar o "código de identificação do beneficiário titular" para todos os respectivos dependentes, maiores ou menores de dezoito anos.

##### Seção III — Do Preenchimento dos Dados de Identificação de Endereço do Beneficiário

**Art. 8º** A operadora deve preencher os dados de identificação de endereço do beneficiário da seguinte forma:

I - Indicação se a residência do beneficiário é no Brasil ou no exterior;

II - para residentes no território brasileiro:

a) indicação de endereço residencial ou profissional;

b) logradouro do beneficiário;

c) número do logradouro;

d) complemento do logradouro;

e) bairro;

f) código do município do logradouro indicado, excluído o dígito verificador;

g) CEP; e

h) código do município de residência do beneficiário, excluído o dígito verificar quando o endereço informado for indicado como endereço profissional.

**§ 1º** A informação de código do município deve ser preenchida em conformidade com o constante da tabela de códigos de municípios, elaborada pelo Instituto Brasileiro de Geografia e Estatística (IBGE), excluído o dígito verificador.

**§ 2º** A operadora deve informar o código do município de residência do beneficiário, caso o endereço informado seja o endereço profissional.

##### Seção IV — Do Preenchimento dos Dados de Identificação Contratual do Beneficiário

Art .9º A operadora deve preencher os campos de identificação contratual do beneficiário da seguinte forma:

I - para o tipo de contratação individual/familiar:

a) número do RPS ou SCPA;

b) data de contratação do plano;

c) data de cancelamento do plano;

d) código do motivo do cancelamento do plano;

e) data de reativação do plano;

f) indicação de existência de CPT;

g) indicação de existência de itens de procedimentos excluídos da cobertura;

h) relação de dependência; e

i) número do RPS do plano de origem (nos casos de portabilidade).

II - para o tipo de contratação coletivo empresarial:

a) número do RPS ou código do SCPA;

b) data de contratação do plano;

c) data de cancelamento do plano;

d) código do motivo do cancelamento do plano;

e) data de reativação do plano;

f) indicação de existência de CPT;

g) indicação de existência de itens de procedimentos excluídos da cobertura;

h) número no CNPJ da pessoa jurídica contratante do plano coletivo empresarial;

i) número no CAEPF do contratante do plano coletivo empresarial; e

j) relação de dependência.

III - para o tipo de contratação coletivo por adesão:

a) número do RPS ou SCPA;

b) data de contratação do plano;

c) data de cancelamento do plano;

d) código do motivo do cancelamento do plano;

e) data de reativação do plano;

f) indicação de existência de CPT;

g) indicação de existência de itens de procedimentos excluídos da cobertura;

h) número no CNPJ da pessoa jurídica contratante do plano coletivo por adesão;

i) número no CAEPF do contratante do plano coletivo por adesão;

j) relação de dependência; e

k) número do RPS do plano de origem (nos casos de portabilidade).

**§ 1** º A operadora deve informar o campo "número do registro do plano na ANS - RPS" quando se tratar de plano contratado após 1º de janeiro de 1999, ou informar o campo "Código do cadastro do plano na ANS - SCPA" quando se tratar de plano contratado até 1º de janeiro de 1999.

**§ 2º** O campo "Número do registro do plano origem RPS" deve ser preenchido nos casos de portabilidade de carências estabelecido pela RN nº 438, de 03 de dezembro de 2018.

#### CAPÍTULO III — DA ATUALIZAÇÃO DOS DADOS CADASTRAIS DE BENEFICIÁRIOS

##### Seção I — Das Regras Gerais de Envio de Dados Cadastrais ao SIB/ANS

**Art. 10** O envio de dados cadastrais de beneficiários e as respectivas atualizações mensais observarão o calendário de eventos do Anexo II desta Instrução Normativa, e o que se segue:

I - a periodicidade para o envio de arquivo SBX é mensal;

II - no primeiro envio, a operadora deve encaminhar para a ANS arquivo SBX contendo a totalidade de beneficiários ativos existentes em sua carteira ou a informação de inexistência de beneficiários; e

III - nos envios mensais subsequentes, a operadora deve enviar arquivo SBX contendo as informações de atualização mensal, informando os procedimentos de inclusão, retificação, mudança contratual, cancelamento e reativação de beneficiários ocorridos na respectiva competência mensal ou a informação de inexistência dos mesmos.

**§ 1º** A operadora que não possua beneficiários ativos em seu cadastro deve informar essa situação por meio de arquivo de atualização com o código da mensagem "NAO EXISTEM BENEFICIARIOS CADASTRADOS".

**§ 2º** A operadora que possua beneficiário ativo em seu cadastro, mas que não teve atualizações nos dados cadastrais dos beneficiários, deve informar essa situação por meio de arquivo de atualização com o código da mensagem "NAO HOUVE ATUALIZACAO DE DADOS BENEFICIARIOS NA COMPETENCIA".

**Art. 11** Finalizado o envio do arquivo SBX com êxito, o aplicativo de transmissão disponibilizará protocolo especificando que a operação de transmissão foi realizada.

**§ 1º** O protocolo de transmissão do arquivo SBX certifica apenas a transmissão dos dados da operadora e sua recepção pela ANS.

**§ 2º** Após a recepção do arquivo SBX, estes serão submetidos a um conjunto de críticas, o que pode ocasionar a rejeição, no todo ou em parte, dos registros de dados de um ou mais beneficiários contidos no arquivo.

##### Seção II — Dos Procedimentos Para a Atualização de Dados Cadastrais no SIB/ANS

**Art. 12** Os procedimentos que orientam a atualização dos dados cadastrais de beneficiário pela operadora são:

I - procedimento de inclusão: refere-se ao envio, pela operadora, de registro de dados de beneficiário que não existia anteriormente no cadastro de beneficiários da operadora na ANS;

II - procedimento de retificação: refere-se à correção, alteração ou complementação de dados cadastrais no cadastro de beneficiários da operadora na ANS, decorrente de erro de informação, mudança de endereço, complementação de informações do registro de dados ou outras alterações dos dados cadastrais;

III - procedimento de mudança contratual: refere-se à alteração de dados contratuais do beneficiário no cadastro de beneficiários da operadora na ANS, decorrente de:

a) migração de plano - mudança de plano anterior à Lei nº 9.656, de 3 de junho de 1998, para plano posterior à Lei nº 9.656, de 1998;

b) adaptação de plano - adaptação de plano contratado até 1º de janeiro de 1999 às regras de plano contratado após 1º de janeiro de 1999;

c) mudança de plano - mudança de plano contratado após 1º de janeiro de 1999 para outro plano contratado após 1º de janeiro de 1999; e

d) portabilidade de carência, nos casos de portabilidade entre planos da mesma operadora, na forma estabelecida pela Resolução Normativa nº 438, de 03 de dezembro de 2018.

IV - procedimento de cancelamento de beneficiário: refere-se à mudança da situação do registro de dados do beneficiário de ativo para inativo no cadastro de beneficiários da operadora na ANS, quando a relação contratual entre o beneficiário e a operadora não estiver mais em vigor; e

V - procedimento de reativação de beneficiário: refere-se à mudança da situação do registro de dados do beneficiário de inativo para ativo no cadastro de beneficiários da operadora na ANS.

**§ 1º** No procedimento de inclusão, a chave primária do registro de beneficiário é composta pelos 6 (seis) dígitos do registro da operadora na ANS e pelo código de identificação do beneficiário na operadora, concatenados nessa ordem.

**§ 2º** Nos procedimentos de retificação, mudança contratual, cancelamento e reativação, a chave primária do registro de beneficiário é o CCO.

**§ 3º** Nos procedimentos de retificação, mudança contratual, cancelamento e reativação de registro de beneficiário, a atualização dos dados é feita por meio da sobreposição dos conteúdos de cada campo pelos dados atualizados pela operadora, desde que processados com sucesso.

**§ 4º** Para cada procedimento, a operadora deve respeitar as obrigatoriedades e críticas de preenchimento dos campos definidas nesta Instrução Normativa, em seu Anexo I e no documento "Críticas de campos de dados cadastrais" disponível no endereço eletrônico da ANS.

**§ 5º** Os procedimentos para atualização dos dados cadastrais dos beneficiários serão processados com sucesso desde que os dados de identificação pessoal, de endereço e contratual estejam preenchidos de forma correta e consistente, nos termos desta Instrução Normativa.

**Art. 13** Nos casos de alteração do campo "código de identificação do beneficiário na operadora", a atualização deve ser feita por meio do procedimento de retificação e, no mesmo procedimento, a operadora deve informar o novo código atribuído pela operadora ao beneficiário.

**Art. 14** O campo "data de contratação do plano" deve ser preenchido nos procedimentos de inclusão, retificação ou mudança contratual, nos termos deste artigo:

I - no procedimento de inclusão, o campo "data de contratação do plano" é referente à data de adesão do beneficiário ao plano da operadora;

II - no procedimento de retificação, o campo "data de contratação do plano" é referente à correção ou complementação de data de contratação do plano já informada ao SIB/ANS;

III - no procedimento de mudança contratual, o campo "data de contratação do plano" é referente à data em que o beneficiário realizou uma migração, adaptação de plano, mudança de plano ou portabilidade de carência entre planos da mesma operadora; e

IV - o campo "data de contratação do plano" não se aplica aos procedimentos de cancelamento ou de reativação.

**Art. 15** É permitida a inclusão de beneficiário com tipo de contratação individual/familiar, para planos contratados até 1º de janeiro de 1999, somente nos casos em que se tratar de beneficiário dependente de um beneficiário titular no mesmo plano, inclusão apenas de novo cônjuge e filhos, nos termos do §5º do art. 35 da Lei n° 9.656, de 1998.

**Art. 16** É permitida a inclusão de beneficiário com tipo de contratação coletivo para planos contratados até 1º de janeiro de 1999, somente nos casos de titulares ou dependentes inseridos em planos cujo CNPJ ou CAEPF do contratante do plano estiver devidamente preenchido no SIB/ANS.

##### Seção III — Do aplicativo de transmissão e da formatação dos arquivos

**Art. 17** A troca de informações entre a operadora e a ANS pelo SIB/ANS deve ocorrer por meio de arquivos XML, em formato definido por schemas XSD.

**§ 1º** O arquivo de atualização de dados (SBX), o arquivo de resultado do processamento (RPX) e o arquivo de conferência (CNX) são os arquivos de troca de informações.

**§ 2º** Encontram-se disponíveis no endereço eletrônico da ANS os schemas XSD dos arquivos de troca de informações.

**§ 3º** A geração de arquivos de atualização de dados deve observar as instruções contidas nos schemas XSD e as orientações estabelecidas nesta IN, e seus anexos, e as informações disponíveis no endereço eletrônico da ANS.

**Art. 18** O aplicativo de transmissão deve ser utilizado pela operadora para transmitir o arquivo de atualização para o SIB/ANS.

**§ 1º** Encontra-se disponível no endereço eletrônico da ANS o aplicativo de transmissão do SIB/ANS.

**§ 2º** As operadoras devem acompanhar as mudanças de versão do aplicativo de transmissão e utilizar a versão mais atual disponível no endereço eletrônico da ANS.

##### Seção IV — Da geração, validação e transmissão dos arquivos de dados

**Art. 19** O arquivo SBX é gerado em formato XML, identificado por 24 (vinte e quatro) caracteres no formato XXXXXXAAAAMMDDHHmmSS. SBX, onde XXXXXX corresponde ao número de registro da operadora na ANS, AAAA ao ano de geração do arquivo, MM ao mês, DD ao dia, HH à hora, mm aos minutos e SS aos segundos relativos à data e horário da geração do arquivo e extensão "SBX".

**§ 1º** As operadoras devem encaminhar pelo menos um arquivo SBX por competência, sendo facultado o envio de mais de um arquivo por competência, sem limite máximo de total de arquivos, desde que sejam respeitados os parâmetros estabelecidos nesta Instrução Normativa.

**§ 2º** Os arquivos SBX gerados, validados e transmitidos para a ANS devem ter identificação individualizada sob pena de serem rejeitados e considerados como não envio da informação de atualização cadastral de beneficiários.

**§ 3º** O arquivo SBX não excederá 100.000 (cem mil) procedimentos de atualização cadastral de beneficiários.

**§ 4º** Caso a quantidade de procedimentos de atualização exceda 100.000 (cem mil), a operadora deve gerar tantos arquivos SBX quantos forem necessários para o envio das informações, e obedecendo às disposições desta Instrução Normativa.

**Art. 20.** Os arquivos de atualização de dados de beneficiário são processados à medida que são recepcionados pela ANS.

**Parágrafo único.** O envio de arquivos e o conteúdo de cada arquivo devem obedecer a uma sequência coerente de procedimentos de atualização.

**Art. 21** O preenchimento e a validação dos campos de dados e as respectivas mensagens de erro são definidos no documento "Críticas de campos de dados cadastrais" disponível no endereço eletrônico da ANS.

**Art. 22** A validação dos arquivos de atualização de dados a serem transmitidos para a ANS ocorrerá em duas etapas:

I - antes do envio, o aplicativo de transmissão realizará a validação do nome, da estrutura e do formato do arquivo e do seu conteúdo e, caso não seja validado, o arquivo não será transmitido para a ANS; e

II- após o envio, ao ser processado pela ANS, ocorrerá a validação da consistência e da coerência das informações contidas no arquivo e os procedimentos com informações inconsistentes ou incoerentes serão rejeitados.

**Parágrafo único.** No cabeçalho do arquivo, o campo "de origem" deve ser preenchido com o número de registro da operadora, e o campo "de destino" deve ser preenchido com o número do CNPJ da ANS, sob pena de o arquivo não ser validado.

##### Seção V — Do Controle do Processamento do SIB/ANS

**Art. 23** O controle da atualização das informações do SIB/ANS é efetuado pelas críticas do processamento do arquivo SBX, pelo arquivo RPX e pelo arquivo CNX.

**Art. 24** O arquivo RPX de que trata o art. 2°, inciso IV, alínea "b", da Resolução Normativa nº 295, de 9 de maio de 2012, deve ser analisado obrigatoriamente pelas operadoras. (REFERÊNCIA CRUZADA - CORRIGIR COM O NOVO Nº DA RN 295)

**Art. 25** O arquivo RPX será gerado pela ANS em formato XML identificado por 24 (vinte e quatro) caracteres no formato XXXXXXAAAAMMDDHHmmSS.RPX, onde XXXXXX corresponderá ao número de registro da operadora na ANS, AAAA ao ano, MM ao mês, DD ao dia, HH à hora, mm aos minutos e SS aos segundos relativos à data/horário da geração do arquivo e a extensão ".RPX".

**Art. 26** O arquivo RPX é composto por quatro partes, a seguir descritas:

I - a primeira parte, que representa o Protocolo de Atualização Cadastral (PTC), contém o cabeçalho do arquivo e o número identificador do processamento do arquivo SBX;

II - a segunda parte contém os procedimentos de atualização que apresentam incorreções e suas respectivas mensagens de erro;

III - a terceira parte contém os procedimentos de inclusão que foram processados com sucesso, acrescidos dos respectivos CCO atribuídos pelo SIB/ANS para cada registro de vínculo de beneficiário; e

IV - a quarta parte contém o consolidado dos procedimentos de atualização enviados, processados e rejeitados, agrupados por procedimento de atualização.

**§ 1º** O download do arquivo RPX será realizado pela operadora por meio do aplicativo Protocolo de Transmissão de Arquivos (PTA) em até 5 (cinco) dias após a recepção do arquivo SBX pela ANS.

**§ 2º** Caso o arquivo SBX não obedeça à formatação definida no schema XSD, o arquivo será rejeitado e será gerado o arquivo RPX correspondente, informando a não conformidade.

**§ 3º** Os erros identificados no processamento dos arquivos de atualização e registrados nos arquivos RPX correspondentes devem ser corrigidos e enviados pelo SIB/ANS, até a competência subsequente.

**§ 4°** A rejeição de um procedimento implica a não atualização da informação desse procedimento no SIB/ANS.

**Art. 27** A operadora poderá solicitar, pelo endereço eletrônico da ANS, o Arquivo de Conferência (CNX) que indicará a situação atualizada de todos os dados cadastrais de beneficiários da operadora, ativos e inativos, processados com sucesso pela ANS.

**§ 1º** A geração do arquivo CNX, nos termos do caput, ocorrerá em até 20 (vinte) dias a partir da solicitação da operadora, limitando-se a uma solicitação de arquivo CNX por competência mensal.

**§ 2º** O arquivo CNX será gerado com tamanho máximo de 500.000 (quinhentos mil) registros de vínculos de beneficiários.

**§ 3º** O arquivo CNX será identificado por 27 caracteres no formato ArqConfXXXXXXMMAAAAYYZZ.CNX, onde XXXXXX corresponderá ao número de registro da operadora na ANS, MM ao mês e AAAA ao ano relativos à geração do arquivo, YY à quantidade total de arquivos gerados e ZZ ao número sequencial do arquivo e a extensão ".CNX".

**§ 4º** O download do arquivo CNX será realizado pela operadora, por meio do aplicativo PTA.

**Art. 28.** As operadoras identificarão no arquivo CNX os campos de dados que necessitam ser preenchidos, corrigidos ou complementados para se adequarem a esta norma.

##### Seção VI — Do Código de Controle Operacional (CCO)

**Art. 29.** O Código de Controle Operacional (CCO) identifica univocamente cada registro de vínculo de beneficiário no SIB/ANS.

**Art. 30.** O CCO é atribuído pelo SIB/ANS a todos os registros de vínculos de beneficiários incluídos no Cadastro de Beneficiários do SIB/ANS.

**§ 1°** O CCO será disponibilizado para as operadoras por meio do arquivo RPX.

**§ 2°** Nos procedimentos de retificação, mudança contratual, cancelamento ou reativação, a operadora deverá informar o CCO do registro de vínculo de beneficiário.

**§ 3º** O Arquivo de Conferência contém a informação do CCO de cada registro de vínculo de beneficiário.

#### CAPÍTULO IV — DAS DISPOSIÇÕES FINAIS E TRANSITÓRIAS

**Art. 31.** O histórico de versões do SIB/ANS é o instrumento utilizado para registrar, orientar e comunicar as mudanças relacionadas ao aplicativo do SIB.

**Art. 32.** Os Anexos I e II desta Instrução Normativa estarão disponíveis no endereço eletrônico da ANS, na área da legislação.

**Art. 33.** Ficam revogadas as Instruções Normativas DIDES nº 50, de 25 de setembro de 2012, nº 55, de 03 de dezembro de 2014, nº 57, de 28 de abril de 2015 e nº 69, de 19 de julho de 2019.

**Art. 34.** Esta Instrução Normativa entrará em vigor na data de sua publicação.

PAULO ROBERTO REBELLO FILHO

## ANEXO I — Obrigatoriedade de preenchimento dos campos de dados para realização dos procedimentos de atualização cadastral do SIB/ANS

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p><strong>Código do campo de dado no SIB</strong></p></td>      <td rowspan="1" colspan="1"><p>Campos de dados</p></td>      <td rowspan="1" colspan="16"><p>Obrigatoriedade de preenchimento dos campos de dados - PROCEDIMENTOS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="3"><p>Inclusão</p></td>      <td rowspan="1" colspan="3"><p>Retificacão</p></td>      <td rowspan="1" colspan="3"><p>Mudança Contratual</p></td>      <td rowspan="1" colspan="3"><p>Cancelamento</p></td>      <td rowspan="1" colspan="3"><p>Reativação</p></td>      <td rowspan="1" colspan="1"><p>Sem Movi- mento</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>     </tr>    </tbody>   </table>

Identificação Pessoal

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>30</p></td>      <td rowspan="1" colspan="1"><p>CCO - Código de Controle Operacional</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>8</p></td>      <td rowspan="1" colspan="1"><p>Código de Identificação do Beneficiário na operadora</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>1</p></td>      <td rowspan="1" colspan="1"><p>Nome do beneficiário</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>2</p></td>      <td rowspan="1" colspan="1"><p>Data de nascimento do beneficiário</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>3</p></td>      <td rowspan="1" colspan="1"><p>Código de sexo do beneficiário</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>4</p></td>      <td rowspan="1" colspan="1"><p>Número no CPF do beneficiário</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>5</p></td>      <td rowspan="1" colspan="1"><p>Número no PIS/PASEP do beneficiário ou Número de Identificação do Trabalhador - NIT</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>6</p></td>      <td rowspan="1" colspan="1"><p>Nome da mãe do beneficiário</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>36</p></td>      <td rowspan="1" colspan="1"><p>Número da Declaração de Nascido Vivo</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>7</p></td>      <td rowspan="1" colspan="1"><p>Número do Cartão Nacional de Saúde</p></td>      <td rowspan="1" colspan="1"><p>O(*)</p></td>      <td rowspan="1" colspan="1"><p>O(*)</p></td>      <td rowspan="1" colspan="1"><p>O(*)</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>18</p></td>      <td rowspan="1" colspan="1"><p>Código de identificação do beneficiário titular na operadora para beneficiários informados como dependentes (não-titulares)</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>    </tbody>   </table>

Identificação de Endereço

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>21</p></td>      <td rowspan="1" colspan="1"><p>Indicação de endereço residencial ou profissional</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>22</p></td>      <td rowspan="1" colspan="1"><p>Logradouro do beneficiário</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>33</p></td>      <td rowspan="1" colspan="1"><p>Número do logradouro</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>34</p></td>      <td rowspan="1" colspan="1"><p>Complemento do logradouro</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>35</p></td>      <td rowspan="1" colspan="1"><p>Bairro</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>26</p></td>      <td rowspan="1" colspan="1"><p>Código do município do logradouro indicado</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>27</p></td>      <td rowspan="1" colspan="1"><p>CEP</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>28</p></td>      <td rowspan="1" colspan="1"><p>Indicação se a residência do beneficiário é no Brasil ou no exterior</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>29</p></td>      <td rowspan="1" colspan="1"><p>Código do município de residência do beneficiário, caso o endereço informado seja indicado como endereço profissional</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>    </tbody>   </table>

Obrigatoriedade de preenchimento dos campos de dados para realização dos procedimentos de atualização cadastral do SIB/ANS (continuação)

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Código do campo de dado no SIB</p></td>      <td rowspan="1" colspan="1"><p>Campos de dados</p></td>      <td rowspan="1" colspan="16"><p>Obrigatoriedade de preenchimento dos campos de dados - PROCEDIMENTOS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="3"><p>Inclusão</p></td>      <td rowspan="1" colspan="3"><p>Retificacão</p></td>      <td rowspan="1" colspan="3"><p>Mudança Contratual</p></td>      <td rowspan="1" colspan="3"><p>Cancelamento</p></td>      <td rowspan="1" colspan="3"><p>Reativação</p></td>      <td rowspan="1" colspan="1"><p>Sem Movi- mento</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Titular</p></td>      <td rowspan="1" colspan="1"><p>Dep. Maior de 18 anos</p></td>      <td rowspan="1" colspan="1"><p>Dep. Menor de 18 anos</p></td>     </tr>    </tbody>   </table>

Identificação Contratual

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>9</p></td>      <td rowspan="1" colspan="1"><p>Número do registro do plano na ANS (RPS)</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>10</p></td>      <td rowspan="1" colspan="1"><p>Código do cadastro do plano na ANS (SCPA)</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>11</p></td>      <td rowspan="1" colspan="1"><p>Número do plano origem RPS (portabilidade)</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>12</p></td>      <td rowspan="1" colspan="1"><p>Data de contratação do plano</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>31</p></td>      <td rowspan="1" colspan="1"><p>Data de cancelamento do plano</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>32</p></td>      <td rowspan="1" colspan="1"><p>Código do motivo do cancelamento do plano</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>20</p></td>      <td rowspan="1" colspan="1"><p>Data de reativação do plano</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>14</p></td>      <td rowspan="1" colspan="1"><p>Indicação de existência de Cobertura Parcial Temporária</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>15</p></td>      <td rowspan="1" colspan="1"><p>Indicação de itens de procedimentos excluídos da cobertura</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>16</p></td>      <td rowspan="1" colspan="1"><p>Número no CNPJ da pessoa jurídica contratante do plano coletivo</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>42</p></td>      <td rowspan="1" colspan="1"><p>Número no CAEPF do contratante do plano coletivo</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>R</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>13</p></td>      <td rowspan="1" colspan="1"><p>Relação de Dependência</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>Op</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>O</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>    </tbody>   </table>

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>19</p></td>      <td rowspan="1" colspan="1"><p>Reservado à ANS</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>      <td rowspan="1" colspan="1"><p>N</p></td>     </tr>    </tbody>   </table>

Legenda:

O - preenchimento obrigatório do campo;

O(\*) - preenchimento obrigatório do campo "Número do Cartão Nacional de Saúde" a partir de 1º de janeiro de 2016;

N - preenchimento do campo não se aplica; R - preenchimento restritivo do campo; Op - preenchimento opcional do campo.

## ANEXO II

Calendário de envio e retirada dos arquivos que compõem o processo de atualização cadastral.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>EVENTOS</p></td>      <td rowspan="1" colspan="1"><p>PRAZO</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>1. Primeiro encaminhamento do arquivo de atualização, quando da concessão do Registro da Operadora pela ANS.</p></td>      <td rowspan="1" colspan="1"><p>Até 60 dias depois de concedido o primeiro registro de planos posteriores à 1º janeiro de 1.999 ou o primeiro cadastro de planos contratados até 1º de janeiro de 1999 (SCPA).</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>2. Envio mensal de Arquivos de Atualização Cadastral - SBX referentes aos procedimentos de atualização ocorridos até o último dia do mês imediatamente anterior.</p></td>      <td rowspan="1" colspan="1"><p>Até o dia 05 de cada mês, considerando o horário de Brasília/DF.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>3. Retirada do Arquivo do Resultado do Processamento - RPX.</p><p>Nota: Ficarão disponíveis para as operadoras os arquivos RPX referentes aos três últimos meses.</p></td>      <td rowspan="1" colspan="1"><p>Em até 05 (cinco) dias a partir da recepção dos arquivos de atualização enviados pelas operadoras para a ANS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>4. Solicitação e Retirada do Arquivo de Conferência - CNX.</p><p><strong>Nota:</strong>Limitando-se a 01 (uma) solicitação de arquivo de conferência por operadora, por competência<strong>.</strong></p></td>      <td rowspan="1" colspan="1"><p>Solicitação: a qualquer momento.</p><p>Retirada: em até 20 (vinte) dias a partir da solicitação.</p></td>     </tr>    </tbody>   </table>
