---
titulo: "RESOLUÇÃO NORMATIVA - RN Nº 500, DE 30 DE MARÇO DE 2022"
orgao: "Ministério da Saúde/Agência Nacional de Saúde Suplementar"
tipo: "Resolução"
numero: "500"
data: 2022-03-30
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 01/04/2022, seção 1, p. 338"
data_publicacao: 2022-04-01
edicao: "63"
fonte: "https://www.in.gov.br/web/dou/-/resolucao-normativa-rn-n-500-de-30-de-marco-de-2022-390313494"
sha256_html_fonte: d39cc3869b3079b979721c3107b41bfbc1c97747468b412a2aa42489435277aa
baixado_em: 2026-10-20
---
# RESOLUÇÃO NORMATIVA - RN Nº 500, DE 30 DE MARÇO DE 2022

RESOLUÇÃO NORMATIVA - RN Nº 500, DE 30 DE MARÇO DE 2022

Estabelece normas para a geração, transmissão e controle de dados cadastrais de beneficiários do Sistema de Informações de Beneficiários da Agência Nacional de Saúde Suplementar - SIB/ANS; dispõe sobre o formato XML (Extensible Markup Language) como padrão para a troca de informações entre as operadoras e o SIB/ANS; revoga as Resoluções Normativas nº 295, de 09 de maio de 2012, nº 303, de 31 de agosto de 2012, nº 361, de 03 de dezembro de 2014, nº 376, de 28 de abril de 2015 e nº445 de 19 de julho de 2019; e dá outras providências.

A Diretoria Colegiada da Agência Nacional de Saúde Suplementar ANS, em vista do que dispõe o inciso XXXI do art. 4º e o inciso II do art.10, ambos da Lei nº 9.961, de 28 de janeiro de 2000; o art. 20 da Lei nº 9.656, de 3 de junho de 1998; e do inciso IV do art. 42 da Resolução Regimental nº 21, de 26 de janeiro de 2022, adotou a seguinte Resolução Normativa e eu, Diretor Presidente, determino a sua publicação.

#### CAPÍTULO I — DAS DISPOSIÇÕES PRELIMINARES

**Art. 1º** Esta Resolução estabelece normas para a geração, transmissão e controle de dados cadastrais de beneficiários do Sistema de Informações de Beneficiários da Agência Nacional de Saúde Suplementar - SIB/ANS; dispõe sobre o formato XML (Extensible Markup Language) como padrão para a troca de informações entre as operadoras e o SIB/ANS; revoga as Resoluções Normativas - RN nº 295, de 09 de maio de 2012, nº 303, de 31 de agosto de 2012, nº 361, de 03 de dezembro de 2014, nº 376, de 28 de abril de 2015 e nº445 de 19 de julho de 2019; e dá outras providências.

**Art. 2º** Para fins desta Resolução e do SIB/ANS, considera-se:

I - beneficiário de plano privado de assistência à saúde: é a pessoa natural, titular ou dependente, que possui direitos e deveres definidos em legislação e em contrato assinado com operadora de plano privado de assistência à saúde, para garantia da assistência médico-hospitalar ou odontológica, sendo, no cadastro de beneficiários da operadora na ANS, classificado como:

a) beneficiário titular: é o beneficiário de plano privado de assistência à saúde cujo contrato o caracteriza como detentor principal do vínculo contratual com uma operadora;

b) beneficiário dependente: é o beneficiário de plano privado de assistência à saúde cujo vínculo contratual com a operadora depende da existência de relação de dependência a um beneficiário titular;

c) beneficiário ativo: é o beneficiário de plano privado de assistência à saúde cujo contrato do respectivo plano está em vigor; e

d) beneficiário inativo: é o beneficiário de plano privado de assistência à saúde cujo contrato do respectivo plano não está em vigor;

II - dados cadastrais de beneficiário: é o conjunto de dados de identificação pessoal, de identificação de endereço e de identificação contratual que identificam o beneficiário da operadora e o plano privado de assistência à saúde a ele vinculado;

III - atualização de dados cadastrais de beneficiário: são os procedimentos de inclusão, de retificação, de mudança contratual, de cancelamento e de reativação que visam a atualizar os dados cadastrais na base de dados de beneficiários das operadoras na ANS, que são assim classificados:

a) procedimento de inclusão: refere-se ao envio, pela operadora, de registro de dados de beneficiário que não existia anteriormente no cadastro de beneficiários da operadora na ANS;

b) procedimento de retificação: refere-se à correção, alteração ou complementação de dados cadastrais no cadastro de beneficiários da operadora na ANS, decorrente de erro de informação, mudança de endereço, complementação de informações do registro de dados ou outras alterações dos dados cadastrais; procedimento de mudança contratual: refere-se à alteração de dados contratuais do beneficiário no cadastro de beneficiários da operadora na ANS, decorrente de:

1 - migração de plano (mudança de plano anterior à Lei nº 9.656, de 3 de junho de 1998, para plano posterior à Lei nº 9.656, de 1998);

2 - adaptação de plano contratado até 1º de janeiro de 1999 às regras de plano contratado após 1ºde janeiro de 1999;

3 - mudança de plano contratado após 1º de janeiro de 1999 para outro plano contratado após 1º de janeiro de 1999; e

4 - portabilidade de carência entre planos da mesma operadora, na forma estabelecida pela Resolução Normativa nº 438, de 03 de dezembro de 2018;

c) procedimento de cancelamento de beneficiário: refere-se à mudança da situação do registro de dados do beneficiário de ativo para inativo no cadastro de beneficiários da operadora na ANS, quando a relação contratual entre o beneficiário e a operadora não estiver mais em vigor; e

d) procedimento de reativação de beneficiário: refere-se à mudança da situação do registro de dados do beneficiário de inativo para ativo no cadastro de beneficiários da operadora na ANS.

IV - arquivos de troca de informações: são os arquivos de atualização de dados (SBX), de resultado do processamento (RPX) e de conferência (CNX), gerados no formato .XML, por meio dos quais é feita a troca de informações entre as operadoras e a ANS, relativa aos dados cadastrais de beneficiários; sendo assim definidos:

a) arquivo de atualização de dados (SBX): contém os dados cadastrais de beneficiários que são transmitidos pelas operadoras para atualizar o seu cadastro de beneficiários na ANS;

b) arquivo de resultado do processamento (RPX): contém o Protocolo de Atualização Cadastral (PTC), o resultado do processamento do arquivo SBX e a relação dos Códigos de Controle Operacional (CCO) atribuídos aos beneficiários que foram incluídos naquele processamento;

c) arquivo de conferência (CNX): contém a situação dos dados cadastrais dos beneficiários ativos e inativos de uma determinada operadora, registrada no cadastro de beneficiários da operadora na ANS até a última atualização cadastral;

V - Código de Controle Operacional (CCO): código atribuído pelo SIB/ANS que identifica univocamente os vínculos armazenados na base de dados de beneficiários das operadoras na ANS; e

VI - Sistema de Informações de Beneficiários (SIB/ANS): sistema informatizado que coleta, processa e armazena os dados cadastrais de beneficiários enviados pelas operadoras, composto:

a) pelo padrão de troca de informações entre operadoras e ANS;

b) pelo aplicativo de transmissão;

c) pelo processamento dos arquivos de dados cadastrais; e

d) pela base de dados de beneficiários das operadoras na ANS.

**Parágrafo único.** O arquivo de resultado do processamento (RPX) e o arquivo de conferência (CNX) são disponibilizados pela ANS às operadoras com registro ativo na ANS.

#### CAPÍTULO II — DAS DISPOSIÇÕES GERAIS

##### Seção I — Das Regras Gerais Sobre o Envio de Dados Cadastrais ao SIB/ANS

**Art.3º** As operadoras devem enviar para a ANS os dados cadastrais de todos os seus beneficiários, na forma desta Resolução e do seu Anexo e de regulamentação específica da Diretoria de Desenvolvimento Setorial - DIDES.

**§ 1º** As operadoras são responsáveis por manter os dados cadastrais de beneficiários atualizados, corretos e fidedignos na ANS.

**§ 2º** A ANS poderá, de ofício, adequar os dados cadastrais de beneficiários do Sistema de Informações de Beneficiários da Agência Nacional de Saúde Suplementar - SIB/ANS a partir de outras fontes que julgar cabíveis

**§ 3°** Os dados informados no SIB, pelas operadoras de planos privados de assistência à saúde, deverão ser auditados anualmente por auditor independente.

**§ 4º** Os dados a serem auditados serão definidos por Instrução Normativa a ser publicada pela Diretoria de Desenvolvimento Setorial - DIDES, que estabelecerá a forma e a periodicidade de enviodo parecer de auditoria à ANS.

**§ 5º** A auditoria realizada nos dados a que se refere a Instrução Normativa mencionada no § 4º deverá observar se os dados cadastrais dos beneficiários informados no SIB refletem as informações dos beneficiários constantes da base de dados da operadora, de forma a aferir a sua consistência.

**Art. 4º** O envio mensal de dados cadastrais de beneficiários para a ANS ocorrerá somente por meiode aplicativo do SIB/ANS, em formato XML.

**Art. 5º** A atualização de dados cadastrais de beneficiários é obrigatória para todas as operadoras com registro ativo na ANS.

**§ 1º** O envio dos dados cadastrais de beneficiários da operadora para a ANS, pelo SIB/ANS, é obrigatório até 60 (sessenta) dias após ter sido concedido o registro/cadastro do primeiro produto da operadora pela ANS.

**§ 2º** Nos meses subsequentes, somente as atualizações de dados cadastrais de beneficiários devem ser informadas pelas operadoras.

**§ 3º** As operadoras que solicitarem cancelamento do seu registro na ANS ficam desobrigadas da atualização mensal dos dados para o SIB/ANS a partir da referida solicitação, desde que atendam ao disposto no art.26, inciso II, da Resolução Normativa nº 85, de 7 de dezembro de 2004.

**§ 4º** Não se aplica o disposto no § 3º se a ANS constatar que as informações prestadas pelas operadoras nos termos do art. 26, inciso II da Resolução Normativa nº 85, de 7 de dezembro de 2004, são inverídicas.

**Art. 6º** A periodicidade de atualização de dados cadastrais de beneficiários é mensal.

**§ 1º** No primeiro envio, a operadora deve encaminhar para a ANS arquivos de atualização de dados contendo a totalidade de beneficiários existentes em sua carteira ou a informação de inexistência de beneficiários.

**§ 2º** Nos envios mensais subsequentes, a operadora deve enviar arquivo de atualização de dados contendo as informações de atualização mensal, informando os procedimentos de inclusão, retificação, mudança contratual, cancelamento e reativação de beneficiários ocorridos na respectiva competência mensal ou a informação de inexistência dos mesmos.

**§ 3º** As operadoras que não possuem beneficiários em seu cadastro, respeitado o disposto nas normas de manutenção e cancelamento de registro de produtos emitidas pela ANS, devem informar mensalmente a referida situação por meio do envio de arquivo de atualização de dados.

**§ 4º** As operadoras que possuem beneficiários em seu cadastro, mas que não têm atualizações nos dados cadastrais de seus beneficiários, devem informar mensalmente a referida situação a ANS por meio do envio de arquivo de atualização de dados.

**Art. 7º** Até o dia 5 (cinco) de cada mês, as operadoras devem enviar informações de atualização de dados cadastrais de beneficiários ocorridas até o último dia do mês imediatamente anterior. Art. 8º O envio de arquivos de atualização de dados cadastrais de que trata o artigo anterior ocorrerá durante o período compreendido entre o dia 6 (seis) do mês corrente até o dia 5 (cinco) do mês imediatamente posterior, podendo ser feito diariamente.

##### Seção II — Do Ciclo de Atualização Cadastral do SIB/ANS

**Art. 9º** O ciclo de atualização cadastral do SIB/ANS compreende:

I - o envio mensal pelas operadoras dos arquivos SBX por meio do aplicativo do SIB/ANS, no formato XML;- a geração e divulgação pelo SIB/ANS do protocolo de transmissão dos arquivos SBX enviados pelas operadoras para a ANS;

II - o processamento pelo SIB/ANS dos arquivos SBX enviados pelas operadoras para a ANS;

III - a geração e divulgação pelo SIB/ANS do arquivo RPX, com o protocolo de atualização cadastral, o detalhamento dos erros encontrados nos conteúdos dos arquivos SBX enviados pelas operadoras para a ANS e a cada CCO atribuído ao registro de beneficiário durante os procedimentos de inclusão processados com sucesso; e

IV - a retirada do arquivo RPX.

**Art. 10.** O protocolo de atualização cadastral estará disponível às operadoras, por meio dos arquivos RPX, no prazo de cinco dias contado da recepção dos arquivos de atualização enviados pelas operadoras para a ANS.

**Parágrafo único.** O protocolo de atualização cadastral, referente a cada arquivo SBX enviado, será o único comprovante da atualização de dados cadastrais de beneficiários na ANS.

**Art. 11.** No prazo definido pelo caput do art. 10 também estará disponível às operadoras, por meio dos arquivos RPX, o detalhamento dos erros encontrados nos conteúdos dos arquivos de atualização de dados anteriormente enviados.

**Parágrafo único.** Os arquivos RPX ficarão disponíveis por três meses e, findo esse período, serão excluídos da base de dados do SIB/ANS.

**Art. 12.** As operadoras deverão corrigir os erros identificados no relatório do protocolo de atualização cadastral até a atualização mensal subsequente.

**Art. 13.** Os arquivos CNX serão gerados apenas na hipótese de solicitação das operadoras por meio do aplicativo do SIB/ANS.

**Art. 14.** A rejeição de um arquivo de atualização de dados caracteriza o não envio das informações contidas nesse arquivo.

##### Seção III — Das Informações Cadastrais de Beneficiários

**Art. 15.** Os dados cadastrais de beneficiários para o SIB/ANS constam no Anexo desta Resolução Normativa.

**Art. 16.** As operadoras devem enviar para a ANS o nome do beneficiário, o número do seu Cadastro de Pessoas Físicas (CPF) e o nome da sua Mãe.

**§ 1º** As operadoras devem enviar para a ANS a informação do número de inscrição no CPF dos beneficiários titulares, maiores ou menores de dezoito anos, bem como dos beneficiários dependentes maiores de dezoito anos, de planos individuais ou familiares, coletivos empresariais ou coletivos por adesão.

**§ 2º** Para os beneficiários dependentes menores de dezoito anos, o envio da informação do número de inscrição no CPF é opcional.

**Art. 17.** As operadoras devem enviar para a ANS a informação do número do Cartão Nacional de Saúde de todos os seus beneficiários ativos, titulares ou dependentes, maiores ou menores de dezoito anos, de planos individuais ou familiares, coletivos empresariais ou coletivos por adesão.

**Art. 18.** As operadoras podem enviar para a ANS a informação do número da Declaração de Nascido Vivo para os beneficiários ativos nascidos a partir de 1º de janeiro de 2010, titulares ou dependentes, de planos individuais ou familiares, coletivos empresariais ou coletivos por adesão.

**Art. 19.** As operadoras devem informar o código de identificação do beneficiário titular na operadora para todos os dependentes, maiores ou menores de 18 (dezoito) anos.

**Art. 20.** As operadoras devem enviar para a ANS a informação sobre o número de inscrição no Cadastro Nacional de Pessoa Jurídica (CNPJ), ou no Cadastro de Atividade Econômica da Pessoa Física (CAEPF), dos contratantes de planos coletivos empresariais ou de planos coletivos por adesão.

**Art. 21.** O preenchimento do campo relativo ao município de residência do beneficiário deve ser informado em conformidade com o constante da tabela de códigos de municípios (sem o dígito verificador), elaborada pelo Instituto Brasileiro de Geografia e Estatística (IBGE).

##### Seção IV — Das Condições de Intervenção da ANS nos Registros de Dados

###### Subseção I — Da Intervenção nos Registros de Dados nos Casos de Transferência de Carteira

**Art. 22.** A ANS intervirá nos dados de beneficiários, transferindo os beneficiários ativos para a operadora adquirente e cancelando-os na operadora cedente, quando se tratar de transferência de carteira total ou parcial relacionada aos incisos I, II, III, V e VI do art. 8º da Resolução Normativa nº 112, de 28 de setembro de 2005.

**§ 1º** O disposto no caput se aplica aos casos de transferência total de carteira e nas transferências de carteira parcial, em que todos os beneficiários pertencentes a um determinado plano/produto sejam eletivos para a transferência, ressalvada a hipótese estabelecida no inciso IV do art. 8º da Resolução Normativa nº 112, de 28 de setembro de 2005.

**§ 2°** Para fins de envio de informações de beneficiários para o SIB/ANS, as operadoras devem cumprir o disposto nas RN 112, de 2005, quando se tratar de modalidades de transferência de carteira não previstas no caput deste artigo.

**Art. 23.** Nos casos de transferência de carteira autorizada pela Diretoria Colegiada da ANS, a agência intervirá na mudança da condição dos registros de vínculos de beneficiários entre as operadoras cedente e adquirente da seguinte forma:

I - executará rotina de inclusão dos beneficiários ativos, relacionados ao processo de transferência de carteira da operadora cedente, transferindo integralmente os dados cadastrais de beneficiários para o cadastro da operadora adquirente, da mesma maneira em que se encontravam preenchidos pela operadora cedente;

II - executará rotina de cancelamento dos beneficiários ativos, relacionados ao processo de transferência de carteira da operadora cedente, com base nas informações do sistema de Registro de Planos de Saúde - RPS;

III - atribuirá os Códigos de Controle Operacional - CCO correspondentes aos registros de dados cadastrais de beneficiários transferidos;

IV - disponibilizará um arquivo CNX especial para conhecimento da operadora cedente, com os dados cadastrais de beneficiários cancelados em decorrência do processo de transferência de carteira; e

V - disponibilizará um arquivo CNX específico para conhecimento da operadora adquirente, com os dados cadastrais de beneficiários transferidos em decorrência do processo de transferência de carteira.

**§ 1º** Os registros de dados cadastrais de beneficiários, que forem objeto da transferência de carteira mencionada no caput, passarão a integrar o cadastro de beneficiários da operadora adquirente na ANS.

**§ 2º** Após a inclusão dos dados cadastrais de beneficiário, a operadora adquirente passa a ser a responsável por manter os dados atualizados, corretos e fidedignos no SIB/ANS.

**§ 3º** Ao retirar o arquivo CNX especial para transferência de carteira, a operadora adquirente poderá alterar o código de identificação do beneficiário.

###### Subseção II — Da Intervenção nos Registros de Dados nos casos de Cancelamento de Registro a pedido da Operadora

**Art. 24.** Nos casos de cancelamento de registro na ANS, a pedido da própria operadora, a ANS, após deferimento em processo administrativo, realizará o procedimento de cancelamento dos registros de beneficiários ativos, sem, no entanto, modificar o conteúdo dos demais campos de dados referentes ao registro.

**§ 1°** Nos casos mencionados no caput, será gravada na base de dados das operadoras na ANS a data informada pela operadora na declaração de inexistência de beneficiários, de que trata o artigo 26, inciso II, da Resolução Normativa nº 85, de 2004, que corresponda à data efetiva do cancelamento dos beneficiários.

**§ 2°** No caso de não constar a data efetiva do cancelamento de beneficiários na declaração de inexistência de beneficiários citada no parágrafo anterior, a ANS considerará para fins de cancelamento de beneficiários na base de dados das operadoras na ANS, a data de emissão da declaração, sem prejuízo das sanções administrativas cabíveis.

###### Subseção III — Da Intervenção nos Registros de Dados nos casos de Cancelamento Compulsório de Registro da Operadora

**Art. 25.** Nos casos de cancelamento compulsório de registro na ANS, quando houver em processo administrativo, manifestação expressa da Diretoria de Normas e Habilitação de Operadoras - DIOPE, a ANS realizará o procedimento de cancelamento dos registros de beneficiários ativos, sem, no entanto, modificar o conteúdo dos demais campos de dados referentes ao registro.

**Parágrafo único.** Nos casos mencionados no caput, será gravada na base de dados das operadoras na ANS a data informada pela DIOPE, referente à data efetiva do cancelamento dos beneficiários, sem prejuízo das sanções administrativas cabíveis.

#### CAPÍTULO III — DAS DISPOSIÇÕES FINAIS E TRANSITÓRIAS

**Art. 26.** Os dados cadastrais de beneficiários referentes ao campo Cartão Nacional de Saúde deverão ser informados obrigatoriamente pelas operadoras a partir de 1º de janeiro de 2016.

**Art. 27.** O não fornecimento, o fornecimento incompleto, a não atualização dos dados cadastrais ou a omissão das informações de beneficiários nos prazos estabelecidos nesta resolução, bem como o fornecimento de informações falsas ou fraudulentas, constituem infrações previstas na Resolução Normativa nº 489, de 29 de março de 2022.

**Art. 28.** A DIDES fica autorizada a editar regulamentação específica para detalhar a presente Resolução Normativa.

**Art. 29.** As operadoras registradas na ANS como administradoras de benefícios, nos termos da Resolução Normativa nº 196, de 14 de Julho de 2009, são dispensadas do cumprimento das normas estabelecidas nesta Resolução Normativa.

**Art. 30.** Os casos omissos e excepcionais serão decididos pela Diretoria Colegiada - DICOL da ANS.

**Art. 31.** Revogam-se as Resoluções Normativas nº 295, de 09 de maio de 2012, nº 303, de 31 de agosto de 2012, nº 361, de 03 de dezembro de 2014, nº 376, de 28 de abril de 2015 e nº 445 de 19 de julho de 2019.

**Art. 32.** Esta Resolução Normativa - RN entrará em vigor na data de sua publicação.

PAULO ROBERTO REBELLO FILHO

## ANEXO I

Planos individuais ou familiares: São aqueles contratados diretamente pelo beneficiário, com ou sem seu grupo familiar.

Planos de saúde coletivos: Se dividem em empresarial e coletivo por adesão. Os empresarias são contratados em decorrência de vínculo empregatício para seus funcionários. Os coletivos por adesão são contratados por pessoa jurídica de caráter profissional, classista ou setorial para seus vinculados (associados ou sindicalizados, por exemplo).

Tanto os planos individuais quanto os planos coletivos são regulados pela ANS e devem cumprir as exigências do órgão regulador com relação à assistência prestada e à cobertura obrigatória.

Veja as particularidades de cada tipo:

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Plano Individual ou Familiar</p></td>      <td rowspan="1" colspan="1"><p>Plano Coletivo por Adesão</p></td>      <td rowspan="1" colspan="1"><p>Plano Coletivo Empresarial</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Quem pode contratar?</p></td>      <td rowspan="1" colspan="1"><p>Qualquer pessoa</p></td>      <td rowspan="1" colspan="1"><p>Pessoa que mantenha vínculo com determinada pessoa jurídica de caráter profissional, classista ou setorial</p></td>      <td rowspan="1" colspan="1"><p>Grupo de pessoas vinculado à pessoa jurídica por relação empregatícia ou estatutária.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Carência*</p></td>      <td rowspan="1" colspan="1"><p>Até: 24 horas para urgência e emergência; 180 dias para demais casos (por exemplo: procedimentos e internação); e 300 dias para parto a termo.</p></td>      <td rowspan="1" colspan="1"><p>Se o beneficiário ingressar no plano em até trinta dias da celebração do contrato coletivo ou do aniversário, para os novos filiados, não há carência.</p></td>      <td rowspan="1" colspan="1"><p>Se o número de participantes for igual ou superior a trinta beneficiários e o ingresso no plano se dê em até trinta dias da celebração do contrato ou da vinculação à Pessoa Jurídica, não há carência.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Cobertura Parcial Temporária em caso de Doença ou Lesão Preexistente*</p></td>      <td rowspan="1" colspan="1"><p>Pode haver estabelecimento de suspensão da cobertura de Procedimentos de Alta Complexidade (PAC), leitos de alta tecnologia e procedimentos cirúrgicos nos casos de DLP por 24 meses.</p></td>      <td rowspan="1" colspan="1"><p>Pode haver estabelecimento de suspensão da cobertura de Procedimentos de Alta Complexidade (PAC), leitos de alta tecnologia e procedimentos cirúrgicos nos casos de DLP por 24 meses.</p></td>      <td rowspan="1" colspan="1"><p>Desde que o número de participantes seja igual ou superior a trinta beneficiários e que beneficiário ingresse no plano em até trinta dias da celebração do contrato ou da vinculação à Pessoa Jurídica, não pode haver.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Cobrança</p></td>      <td rowspan="1" colspan="1"><p>Diretamente ao beneficiário, pela operadora.</p></td>      <td rowspan="1" colspan="1"><p>À Pessoa Jurídica e esta (ou uma administradora) cobra do beneficiário.**</p></td>      <td rowspan="1" colspan="1"><p>À Pessoa Jurídica e esta (ou uma administradora) cobra do beneficiário.***</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Rescisão Imotivada pela Operadora</p></td>      <td rowspan="1" colspan="1"><p>Só pode por fraude ou não-pagamento da mensalidade por período superior a sessenta dias, consecutivos ou não, nos últimos doze meses de vigência do contrato, desde que o consumidor seja comprovadamente notificado até o qüinquagésimo dia de inadimplência</p></td>      <td rowspan="1" colspan="1"><p>Pode haver desde que haja previsão em contrato e que seja para o contrato coletivo como um todo. A pessoa jurídica deve ser notificada com pelo menos 60 dias de antecedência.</p></td>      <td rowspan="1" colspan="1"><p>Pode haver desde que haja previsão em contrato e que seja para o contrato coletivo como um todo. A pessoa jurídica deve ser notificada com pelo menos 60 dias de antecedência.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Participação de Administradora</p></td>      <td rowspan="1" colspan="1"><p>Não</p></td>      <td rowspan="1" colspan="1"><p>Facultativa</p></td>      <td rowspan="1" colspan="1"><p>Facultativa</p></td>     </tr>    </tbody>   </table>

\* A regra citada neste documento para carência e cobertura parcial temporária de doenças e lesões pré-existentes (CPT) é a prevista na legislação em vigor. O contrato poderá conter cláusula reduzindo ou isentando o cumprimento de carência ou CPT.

\*\* ressalvadas as operadoras na modalidade de autogestão.

\*\*\*ressalvadas as hipóteses previstas nos artigos 30 e 31 da Lei nº 9.656, de 1998 (aposentados e demitidos), das operadoras na modalidade de autogestão e dos entes da administração pública direta ou indireta.

## ANEXO II

Os dados cadastrais de beneficiários que constituem as informações básicas e complementares do registro de beneficiários do SIB/ANS são os seguintes:

I. Dados de identificação pessoal:

a) Código de Controle Operacional - CCO;

b) código de identificação do beneficiário na operadora;

c) nome do beneficiário;

d) data de nascimento do beneficiário;

e) código de sexo do beneficiário;

f) nome da mãe do beneficiário;

g) código de identificação do beneficiário titular na operadora, para beneficiários informados como dependentes (não titulares);

h) número de inscrição no Cadastro de Pessoa Física - CPF do beneficiário;

i) número de inscrição no Programa de Integração Social - PIS ou no Programa de Formação do Patrimônio do Servidor Público - PASEP ou Número de Identificação do Trabalhador - NIT;

j) número do Cartão Nacional de Saúde do beneficiário (obrigatório para todos os beneficiários a partir de 1º/01/2016);

k) número da Declaração de Nascido Vivo para os nascidos a partir de 1º de janeiro de 2010; (Opcional);

l) número do Registro de Identidade Civil - RIC;

m) número da cédula de alistamento eleitoral - Título de Eleitor;

n) número da carteira de identidade do beneficiário;

o) órgão emissor da carteira de identidade do beneficiário;

p) código do país emissor da carteira de identidade do beneficiário;

q) indicação da relação entre o beneficiário dependente e o beneficiário titular.

II. Dados de identificação de endereço:

a) indicação se o endereço do beneficiário é no Brasil ou no exterior

b) indicação de endereço residencial ou profissional;

c) logradouro do beneficiário;

d) número logradouro do beneficiário;

e) Complemento do logradouro;

f) bairro;

g) código do município - IBGE do logradouro; informado (sem o dígito verificador);

h) Código de Endereçamento Postal - CEP para o endereço informado; i) indicação de logradouro situado no exterior;

i) código do município - IBGE de residência do beneficiário (sem o dígito verificador), caso o endereço informado seja indicado como endereço profissional.

III. Campos de identificação do plano privados de assistência à saúde:

a) número do registro do plano na ANS - RPS;

b) código do cadastro do plano na ANS - SCPA

c) data de adesão do beneficiário ao plano;

d) data de cancelamento do vínculo do beneficiário ao plano;

e) código do motivo do cancelamento do plano;

f) data de reativação do plano;

g) indicação de existência de Cobertura Parcial Temporária - CPT;

h) indicação de existência de itens de procedimentos excluídos da cobertura;

i) número no Cadastro Nacional de Pessoa Jurídica - CNPJ da pessoa jurídica contratante do plano coletivo empresarial ou do plano coletivo por adesão;

j) número no Cadastro de Atividade Econômica da Pessoa Física - CAEPF do contratante do plano coletivo empresarial ou do plano coletivo por adesão; e

k) relação de dependência.
