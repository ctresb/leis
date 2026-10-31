---
titulo: "PORTARIA Nº 54, DE 8 DE JUNHO DE 2017"
orgao: "Ministério da Fazenda/SECRETARIA DA RECEITA FEDERAL DO BRASIL/SUBSECRETARIA DE GESTÃO CORPORATIVA COORDENAÇÃO-GERAL DE TECNOLOGIA DA INFORMAÇÃO"
tipo: "Portaria"
numero: "54"
data: 2017-06-08
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 22/06/2017, seção 1, p. 21"
data_publicacao: 2017-06-22
edicao: "118"
fonte: "https://www.in.gov.br/web/dou/-/portaria-n-54-de-8-de-junho-de-2017-19129024"
sha256_html_fonte: f75f6301d5c2dd7737c9101a24394a3960469ed4521399d0562d4a4f925161ce
baixado_em: 2026-10-27
---
# PORTARIA Nº 54, DE 8 DE JUNHO DE 2017

PORTARIA Nº 54, DE 8 DE JUNHO DE 2017

Dispõe sobre as formas e critérios de segurançada informação para o acesso a dadosda Secretaria da Receita Federal doBrasil (RFB) por órgãos convenentes oupor órgãos e entidades da AdministraçãoPública Federal direta, autárquica e fundacional.

A COORDENADORA-GERAL DE TECNOLOGIA DA INFORMAÇÃO,no uso da atribuição que lhe confere o inciso III doart. 312 do Regimento Interno da Secretaria da Receita Federal doBrasil, aprovado pela Portaria MF nº 203, de 14 de maio de 2012, etendo em vista o disposto no art. 22, inciso VI, da Portaria SRF nº450, de 28 de abril de 2004, o disposto na Portaria RFB nº 1.384, de09 de setembro de 2016, na Portaria RFB nº 1.639, de 22 de novembrode 2016, e a necessidade de regulamentar as formas e critériosde segurança da informação para acesso a bases de dados daSecretaria da Receita Federal do Brasil por órgãos convenentes ou porórgãos e entidades da Administração Pública Federal direta, autárquicae fundacional, resolve:

DISPOSIÇÕES PRELIMINARES

**Art. 1º** O modelo tecnológico para disponibilização de dadosconstantes de base de dados da Secretaria da Receita Federal doBrasil (RFB) para órgãos convenentes e órgãos e entidades da AdministraçãoPública Federal direta, autárquica e fundacional seguirá odisposto nesta Portaria.

Parágrafo Único. Para efeitos desta Portaria, além do dispostono artigo 2º da Portaria SRF nº 450/2004, entende-se por:

I - Forma de acesso: meio ou tecnologia utilizada para acessaras informações disponibilizadas a convenente ou a órgãos e entidadesda administração pública federal direta, autárquica e fundacional;

II- Web Service/Application Programming Interface (API):Aplicação lógica, programável que torna compatíveis entre si diferentesaplicativos, independentemente do sistema operacional, arquiteturaou protocolo utilizados (REST ou SOAP), permitindo acomunicação e intercâmbio de dados entre diferentes redes e sistemas;

III- Perfil de sistema: conjunto de privilégios ou transaçõesde um sistema atribuído a um usuário;

IV - Perfil de serviço: conjunto de privilégios e informaçõespassíveis de consulta por meio de um serviço atribuído a um órgãoconvenente ou a órgãos e entidades da administração pública federaldireta, autárquica e fundacional;

IV - Transação: conjunto de operações que desempenha umafunção lógica em um sistema;

V - Evento: qualquer interação com o ambiente informatizadoda RFB, com ou sem intervenção do usuário;

VI - Registro de eventos (log): conjunto de informaçõesarmazenadas para permitir o acompanhamento de eventos praticadosno ambiente informatizado; e

VII - Apuração especial: procedimento computacional destinadoa gerar relatório ou arquivo eletrônico especificado pela RFBe executado por um de seus prestadores de serviços.

Das formas de acesso

**Art. 2º** O acesso aos dados da RFB, por órgãos convenentesou por órgãos e entidades da Administração Pública Federal direta,autárquica e fundacional, dar-se-á por consulta via Web Service/API,com o uso de certificado digital.

**§ 1º** Para dados do Cadastro de Pessoa Física (CPF) e doCadastro Nacional de Pessoa Jurídica (CNPJ), em complemento aodisposto no caput, é facultado o acesso por meio de habilitação emperfis próprios desses sistemas, permitindo acesso aos seguintes dados:

I- CPF:

-Número de inscrição;

-Nome;

-Situação cadastral;

-Indicativo de residente no exterior;

-Nome do país, caso seja residente no exterior;

-Nome da mãe;

-Data de nascimento;

-Sexo;

-Endereço completo (tipo de logradouro, nome do logradouro,número da habitação, CEP, UF e município);

-Telefone;

-Unidade administrativa;

-Ano do óbito;

-Indicativo de estrangeiro;

-Data de inscrição do CPF;

-Naturalidade; e

-Nacionalidade.

II - CNPJ:

-Número de inscrição;

-Indicador de matriz/filial;

-Nome empresarial;

-Nome fantasia;

-Situação cadastral;

-Cidade no exterior, caso o estabelecimento seja domiciliadono exterior;

-Código do país, caso o estabelecimento seja domiciliado noexterior;

-Nome do país, caso o estabelecimento seja domiciliado noexterior;

-Data da situação cadastral;

-Natureza jurídica;

-Data de abertura;

-CNAE - Principal;

-CNAE secundários (até 10);

-Endereço:

-Telefone;

-E-mail;

-Responsável pela PJ, CPF e nome;

-Capital Social da Empresa;

-CPF dos participantes do QSA;

-Qualificação dos participantes no QSA; e

-Porte do estabelecimento.

**§ 2º** A disponibilização de acesso aos dados por meio defornecimento de réplicas, parciais ou totais, das bases de dados doCPF e CNPJ, poderá ser realizada até 31 de dezembro de 2018, nostermos do § 2º do art. 6º da Portaria RFB nº 1639, de 2016.

**§ 3º** O órgão receptor das bases de dados de que trata o art.2º deve garantir a total rastreabilidade das informações ou mídiasfornecidas, em conformidade com os requisitos previstos nesta Portaria.

DOSCRITÉRIOS DE SEGURANÇA PARA ACESSO VIAWEB SERVICES

**Art. 3º** Os Web Services/API utilizados para o fornecimentodos dados deverão conter as seguintes funcionalidades e características:

I- comunicação via HTTPS com uso de certificado digitalICP-Brasil, emitido em nome do órgão receptor dos dados objeto deconvênio ou autorização, do tipo e-Equipamento;

II - filtrar a conexão de origem por conjunto de endereços IPatribuídos aos órgãos receptores dos dados;

III - exigir a identificação (CPF) do usuário que está de fatorealizando a consulta aos dados;

IV - habilitação em perfis de serviços e sistemas de acesso abase por órgãos convenentes ou por órgãos e entidades da AdministraçãoPública Federal direta, autárquica e fundacional, com vias arestringir o acesso apenas aos órgãos/usuários devidamente autorizados;e

V - registro de todos os eventos, com armazenamento e formacomo definidas na Portaria RFB nº 693, de 13 de fevereiro de 2014.

Da habilitação em perfis de sistemas

**Art. 4º** As habilitações de usuários de órgãos convenentes oude órgãos e entidades da Administração Pública Federal direta, autárquicae fundacional, para acesso a sistemas da RFB seguirão o ritoestabelecido na Portaria RFB/Sucor/Cotec nº 73, de 08 de dezembrode 2014, alterada pela Portaria RFB/Sucor/Cotec nº 1, de 11 dejaneiro de 2016.

**§ 1º** As habilitações serão realizadas apenas por necessidadede serviço, as quais, após cessados os motivos que levaram a suaconcessão, deverão ser retiradas por meio de uma solicitação dedesabilitação.

**§ 2º** A qualquer tempo a RFB poderá solicitar aos órgãosconvenentes ou por órgãos e entidades da Administração PúblicaFederal direta, autárquica e fundacional a revisão das habilitaçõesvigentes dos seus usuários.

DA UTILIZAÇÃO E PROTEÇÃO DAS INFORMAÇÕESDISPONIBILIZADAS

**Art. 5º** O convenente e órgãos e entidades da AdministraçãoPública Federal direta, autárquica e fundacional são responsáveis pelacorreta utilização dos dados disponibilizados e os mesmos não poderãoser transferidos a terceiros, total ou parcialmente, ou divulgadosde qualquer forma ou a qualquer título.

**Art. 6º** Os dados poderão ser utilizados apenas nas atividadesintrínsecas para as quais foram solicitadas.

**Art. 7º** A utilização dos dados disponibilizados pela RFB emdesconformidade com a legislação pertinente, implicará o imediatocancelamento da disponibilização, sem prejuízo de apurações de responsabilidadena forma prevista em regulamentação específica.

**Art. 8º** Os sistemas de informação de âmbito interno dosórgãos convenentes ou dos órgãos e entidades da Administração PúblicaFederal direta, autárquica e fundacional, que consumirem asinformações disponibilizadas, deverão implementar, no mínimo, osseguintes requisitos:

I - Acesso por meio de certificado digital ICP-Brasil, padrãoA3;

II - Uso de protocolos criptografados para tráfego e armazenamentode dados;

III - Registro de todos os eventos de logs que envolvam osdados objetos do convênio ou autorização, permitindo identificar individualmentea operação efetuada, o usuário, estação de trabalho edata/hora das transações realizadas;

IV - Adoção dos meios necessários para promover criptografiados backups operacionais;

V - Estabelecimento de perfis de acesso com definição deatribuições e responsabilidades dos usuários neles habilitados; e

VI - Acesso regulamentado mediante processos formais paraa solicitação de acesso aos perfis dos sistemas, permitindo verificar,inclusive, os autorizadores que concederam as permissões ao usuário.

**§1º** Os órgãos convenentes ou os órgãos e entidades daAdministração Pública Federal direta, autárquica e fundacional deverãoguardar por período necessário à garantia de responsabilidadedos usuários por eventual uso indevido das informações, observadasas políticas e normas internas, os dados relativos ao controle deacesso e ao acesso a registros de informação, bem como os documentosreferentes à autorização de acesso e utilização dos dadosdisponibilizados pela RFB.

**§ 2º** Deve ser adotado anualmente procedimentos formaispara a revisão das habilitações concedidas.

**§ 3º** Os sistemas de que trata o caput devem ser desenvolvidoscom adesão à práticas e metodologias de desenvolvimentoseguro com vias a mitigar vulnerabilidades e falhas no sistema.

**Art. 9.** As salas, nos órgãos receptores dos dados ou prestadoresde serviço, destinadas aos equipamentos servidores, banco dedados e storages responsáveis pela recepção e guarda dos dadosprovenientes da RFB, deverão implementar, no mínimo, os seguintesrequisitos:

I - utilização de mecanismo eletrônico de identificação econtrole de acesso baseado em, no mínimo, dois fatores de autenticação;

II- todo acesso de pessoas e materiais deve ser autorizado eregistrado por equipamento de monitoramento, 24 horas pelos 7 diasda semana, e mantidas em arquivos de log;

III - infraestrutura protegida com ativos de segurança (Firewall,IDS - Intrusion Detection System e IPS - Intrusion PreventionSystem) e gerenciados e monitorados por Grupo de Resposta a Ataques- GRA; e

IV - manutenção das imagens do sistema de monitoramento,preferencialmente na mesma mídia, pelo período mínimo de umano.

DAS DISPOSIÇÕES finais

**Art. 10.** O convenente ou os órgãos e entidades da AdministraçãoPública Federal direta, autárquica e fundacional devemgarantir a implementação das políticas de segurança da informaçãodispostas nesta Portaria, sendo facultado à RFB solicitar, a qualquermomento, a demonstração do atendimento do disposto nesta Portaria.

**Art.11.** Fica revogada a Portaria RFB/Sucor/Cotec nº 83, de14 de dezembro de 2016.

**Art. 12.** Esta Portaria entra em vigor na data de sua publicaçãono Diário Oficial da União.

CLAUDIA MARIA DE ANDRADE

CLAUDIA MARIA DE ANDRADE

Este conteúdo não substitui o publicado na versão certificada.
