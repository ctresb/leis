---
titulo: "INSTRUÇÃO NORMATIVA ITI Nº 18, DE 11 DE NOVEMBRO DE 2020"
orgao: "Presidência da República/Casa Civil/Instituto Nacional de Tecnologia da Informação"
tipo: "Instrução Normativa"
numero: "18"
data: 2020-11-11
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 25/11/2020, seção 1, p. 59"
data_publicacao: 2020-11-25
edicao: "225"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-iti-n-18-de-11-de-novembro-de-2020-290042286"
sha256_html_fonte: b3462c1564cb9b606c9965301c9f7c1b26cceb8bdb44e9d3dc2d9cdd3b7a976c
baixado_em: 2026-10-21
---
# INSTRUÇÃO NORMATIVA ITI Nº 18, DE 11 DE NOVEMBRO DE 2020

**INSTRUÇÃO NORMATIVA ITI Nº 18, DE 11 DE NOVEMBRO DE 2020**

Aprova a versão revisada e consolidada do documento Procedimentos para Gerenciamento da Chave Simétrica para Geração do IDN DOC-ICP-05.04.

**O DIRETOR-PRESIDENTE DO INSTITUTO NACIONAL DE TECNOLOGIA DA INFORMAÇÃO**, no uso das atribuições que lhe foram conferidas pelo inciso VI do art. 9º do anexo I do Decreto nº 8.985, de 8 de fevereiro de 2017, pelo art. 1º da Resolução nº 33 do Comitê Gestor da ICP-Brasil, de 21 de outubro de 2004, e pelo art. 2º da Resolução nº 163 do Comitê Gestor da ICP-Brasil, de 17 de abril de 2020,

CONSIDERANDO a determinação estabelecida pelo Decreto nº 10.139, de 28 de novembro de 2019, para revisão e consolidação dos atos normativos inferiores a decreto, editados por órgãos e entidades da administração pública federal direta, autárquica e fundacional, resolve:

**Art. 1º** Esta Instrução Normativa aprova a versão revisada e consolidada do documento Procedimentos para Gerenciamento da Chave Simétrica para Geração do IDN DOC-ICP-05.04.

**Art. 2º** Fica aprovada a versão 3.0 do documento DOC-ICP-05.04 - Procedimentos para Gerenciamento da Chave Simétrica para Geração do IDN.

**Art. 3º** Ficam revogadas.

I - a Instrução Normativa nº 08, de 10 de dezembro de 2015; e

II - a Instrução Normativa nº 13, de 21 de novembro de 2016.

**Art. 4º** Esta Instrução Normativa entra em vigor em 1° de dezembro de 2020.

CARLOS ROBERTO FORTNER

PROCEDIMENTOS PARA GERENCIAMENTO DA CHAVE SIMÉTRICA PARA GERAÇÃO DO IDN

DOC-ICP-05.04

Versão 3.0

23 de novembro de 2020

CONTROLE DE ALTERAÇÕES

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução ou IN que aprovou a alteração</p></td>      <td rowspan="1" colspan="1"><p>Item alterado</p></td>      <td rowspan="1" colspan="1"><p>Descrição da alteração</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IN ITI nº 18, de 23/11/2020</p><p>Versão 3.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Revisão e consolidação, conforme Decreto nº 10.139, de 28 de novembro de 2019.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução nº 123,</p><p>de 06.07.2017</p><p>Versão 2.1</p></td>      <td rowspan="1" colspan="1"><p>1.2.3</p></td>      <td rowspan="1" colspan="1"><p>Inclui a opção de certificação INMETRO para a importação da cópia da chave criptográfica simétrica gerada.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IN nº 13, de 21.11.2016</p><p>Versão 2.0</p></td>      <td rowspan="1" colspan="1"><p>1, 3, 4 e 5.</p></td>      <td rowspan="1" colspan="1"><p>Aprova a versão 2.0 - atualiza os procedimentos de geração, armazenamento, distribuição, proteção, validade e substituição de chaves utilizadas no IDN.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IN nº 08, de 10.12.2015</p><p>Versão 1.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Aprova a versão 1.0 do Documento Procedimentos para Gerenciamento da Chave Simétrica para geração do IDN.</p></td>     </tr>    </tbody>   </table>

LISTA DE ACRÔNIMOS

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>SIGLA</p></td>      <td rowspan="1" colspan="1"><p>DESCRIÇÃO</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AC</p></td>      <td rowspan="1" colspan="1"><p>Autoridade Certificadora</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AC RAIZ</p></td>      <td rowspan="1" colspan="1"><p>Autoridade Certificadora Raiz da ICP-BRASIL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>DOC-ICP</p></td>      <td rowspan="1" colspan="1"><p>Documentos Principais da ICP-BRASIL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ICP-Brasil</p></td>      <td rowspan="1" colspan="1"><p>Infraestrutura de Chaves Públicas Brasileira</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IDN</p></td>      <td rowspan="1" colspan="1"><p>Identificador de Registro Biométrico</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>INMETRO</p></td>      <td rowspan="1" colspan="1"><p>Instituto Nacional de Metrologia, Qualidade e Tecnologia</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ITI</p></td>      <td rowspan="1" colspan="1"><p>Instituto Nacional de Tecnologia da Informação</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>MSC</p></td>      <td rowspan="1" colspan="1"><p>Módulo de Segurança Criptográfico</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PSBio</p></td>      <td rowspan="1" colspan="1"><p>Prestador de Serviço Biométrico</p></td>     </tr>    </tbody>   </table>

1 GERAÇÃO, ARMAZENAMENTO E DISTRIBUIÇÃO DA CHAVE

1.1 Geração e armazenamento da chave

1.1.1 As chaves criptográficas simétricas serão geradas e armazenadas pela AC Raiz, em hardware seguro com atributos específicos que permitam o gerenciamento do seu ciclo de vida.

1.1.2 O algorítmo e o tamanho das chaves criptográficas simétricas geradas pela AC Raiz e utilizadas para geração do IDN pelas ACs estão definidos no documento PADRÕES E ALGORITMOS CRIPTOGRÁFICOS DA ICP-BRASIL[1].

1.2 Distribuição de chave

1.2.1 Recebimento de certificado digital da entidade

1.2.1.1 As entidades interessadas, devidamente credenciadas no âmbito da ICP-Brasil, deverão gerar certificado digital, sendo a chave privada correspondente gerada e armazenada em MSC próprio da entidade.

1.2.1.2 Este certificado deverá ser enviado ao ITI por correio eletrônico, assinado digitalmente pelo representante legal da entidade.

1.2.2 Exportação da Chave Criptográfica Simétrica

1.2.2.1 Após o recebimento do certificado digital encaminhado pela entidade, o ITI agendará cerimônia interna de extração da correspondente chave pública, que servirá para cifragem e exportação da chave criptográfica simétrica.

1.2.3 Importação da Chave Criptográfica Simétrica pela Entidade

1.2.3.1 A cópia da chave criptográfica simétrica gerada será importada em MSC homologado ou com certificação INMETRO, pertencente à entidade, seguindo formato definido no documento PADRÕES E ALGORITMOS CRIPTOGRÁFICOS DA ICP-BRASIL[1].

1.2.3.2 A importação da chave criptográfica simétrica será feita na presença de um representante legalmente constituído da entidade, acompanhado por representante da AC Raiz, em cerimônia específica, com data e hora previamente estabelecidas.

1.2.3.3 Para fins de auditoria, essa cerimônia deverá produzir evidências que a chave criptográfica importada não poderá ser exportada. Caberá ainda ao representante legal da entidade assinar termo específico de importação de chave criptográfica produzida na AC Raiz da ICP-Brasil.

1.2.4 Prazo para distribuição da chave criptográfica simétrica

O ITI deverá providenciar a distribuição da chave criptográfica simétrica em no máximo 30(trinta) dias úteis, contados a partir do recebimento do certificado digital da entidade.

2\. PROTEÇÃO DA CHAVE

2.1 As chaves criptográficas simétricas da AC Raiz, ao serem exportadas, serão cifradas com a chave pública da entidade, que deverá manter a chave privada equivalente em MSC, para abrir o envelope digital seguindo as regras do esquema de cifragem.

2.2 Compete à AC Raiz acompanhar a evolução tecnológica para, quando necessário, atualizar os padrões e algoritmos criptográficos utilizados na ICP-Brasil, com a atualização do documento PADRÕES E ALGORITMOS CRIPTOGRÁFICOS DA ICP-BRASIL[1].

3 PRAZO DE VALIDADE

3.1 Toda chave simétrica gerada pela AC Raiz terá validade de 2 (dois) anos, podendo ser prorrogada por meio de ato normativo do ITI.

3.2 Para geração e distribuição de nova chave criptográfica simétrica deverão ser observadas as regras e procedimentos estabelecidos no item 1 deste documento.

4 SUBSTITUIÇÃO DA CHAVE SIMÉTRICA

4.1 A AC Raiz pode, a qualquer momento, gerar uma nova chave criptográfica simétrica para geração dos IDNs da ICP-Brasil, observando as regras e procedimentos do item 1 do presente documento.

4.2 Assim que as entidades receberem da AC Raiz uma nova chave criptográfica simétrica, os indexadores IDN usados por entidades e PSBios deverão ser recalculados. Caso necessário, poderão ser mantidos os IDNs antigos até a completa reindexação de todas as bases de dados.

4.3 O procedimento de substituição da chave criptográfica simétrica, incluindo a reindexação das bases de dados com IDNs recalculados, deve ser executado num prazo máximo de 15 (quinze) dias úteis, contados a partir da importação da chave simétrica pelas entidades, de maneira sincronizada entre entidades e PSBios, de forma a não causar indisponibilidades no sistema. No caso de comprometimento da chave criptográfica simétrica, esses procedimentos devem ocorrer em no máximo 2 (dois) dias úteis.

4.4 Após a reindexação das bases de dados, os PSBios deverão excluir permanentemente qualquer informação indexada pelo IDN gerado a partir da chave criptográfica simétrica anterior, devendo as entidades manter em seus registros a associação entre IDN antigo e o novo.

5 CÓPIA DE SEGURANÇA DE CHAVE

5.1 Cabe à AC Raiz realizar cópias de segurança de todas as chaves criptográficas simétricas geradas, de forma a garantir a sua preservação, bem como a contingência do sistema de geração e distribuição das chaves.

6 DOCUMENTOS REFERENCIADOS

6.1 Os documentos abaixo são aprovados por Instrução Normativa da AC Raiz, podendo ser alterados, quando necessário, pelo mesmo tipo de dispositivo legal. O sítio http://www.iti.gov.br publica a versão mais atualizada desses documentos e as Instruções Normativas que os aprovaram.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p><em>Ref.</em></p></td>      <td rowspan="1" colspan="1"><p><em>Nome do documento</em></p></td>      <td rowspan="1" colspan="1"><p><em>Código</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[1]</p></td>      <td rowspan="1" colspan="1"><p>PADRÕES E ALGORITMOS CRIPTOGRÁFICOS DA ICP-BRASIL.</p><p>Aprovado pela Instrução Normativa nº 04, de 18 de maio de 2006</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-01.01</p></td>     </tr>    </tbody>   </table>

**INSTRUÇÃO NORMATIVA ITI Nº 19, DE 23 DE NOVEMBRO DE 2020**

Aprova a versão revisada e consolidada do documento Procedimentos para Obtenção da Hora UTC na ICP-Brasil DOC-ICP-07.01.

**O DIRETOR-PRESIDENTE DO INSTITUTO NACIONAL DE TECNOLOGIA DA INFORMAÇÃO**, no uso das atribuições que lhe foram conferidas pelo inciso VI do art. 9º do anexo I do Decreto nº 8.985, de 8 de fevereiro de 2017, pelo art. 1º da Resolução nº 33 do Comitê Gestor da ICP-Brasil, de 21 de outubro de 2004, e pelo art. 2º da Resolução nº 163 do Comitê Gestor da ICP-Brasil, de 17 de abril de 2020,

CONSIDERANDO a determinação estabelecida pelo Decreto nº 10.139, de 28 de novembro de 2019, para revisão e consolidação dos atos normativos inferiores a decreto, editados por órgãos e entidades da administração pública federal direta, autárquica e fundacional, resolve:

**Art. 1º** Esta Instrução Normativa aprova a versão revisada e consolidada do documento Procedimentos para Obtenção da Hora UTC na ICP-Brasil DOC-ICP-07.01.

**Art. 2º** Fica aprovada a versão 2.0 do documento DOC-ICP-07.01 - Procedimentos para Obtenção da Hora UTC na ICP-Brasil, anexa a esta Instrução Normativa.

**Art. 3º** Esta Instrução Normativa entra em vigor em 1° de dezembro de 2020.

CARLOS ROBERTO FORTNER

PROCEDIMENTOS PARA OBTENÇÃO DA HORA UTC NA ICP-BRASIL

DOC-ICP-07.01

Versão 2.0

23 de novembro de 2020

CONTROLE DE ALTERAÇÕES

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução ou IN que aprovou a alteração</p></td>      <td rowspan="1" colspan="1"><p>Item alterado</p></td>      <td rowspan="1" colspan="1"><p>Descrição da alteração</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa ITI nº 19, de 23/11/2020</p><p>Versão 2.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Revisão e consolidação conforme Decreto nº 10.139, de 28 de novembro de 2019.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa nº 09,</p><p>de 07/12/2015</p><p>Versão 1.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Aprova a versão 1.0 do DOC-ICP-07.01.</p></td>     </tr>    </tbody>   </table>

LISTA DE SIGLAS E ACRÔNIMOS

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>SIGLA</p></td>      <td rowspan="1" colspan="1"><p>DESCRIÇÃO</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AC</p></td>      <td rowspan="1" colspan="1"><p>Autoridade Certificadora</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AC-RAIZ</p></td>      <td rowspan="1" colspan="1"><p>Autoridade Certificadora Raiz da ICP-BRASIL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>DOC-ICP</p></td>      <td rowspan="1" colspan="1"><p>Documentos Principais da ICP-BRASIL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>FCT</p></td>      <td rowspan="1" colspan="1"><p>Fonte Confiável do Tempo</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ITI</p></td>      <td rowspan="1" colspan="1"><p>Instituto Nacional de Tecnologia da Informação</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ICP-Brasil</p></td>      <td rowspan="1" colspan="1"><p>Infraestrutura de Chaves Públicas Brasileira</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>NTP</p></td>      <td rowspan="1" colspan="1"><p><em>Network Time Protocol</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PSS</p></td>      <td rowspan="1" colspan="1"><p>Prestador de Serviço de Suporte</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PSBio</p></td>      <td rowspan="1" colspan="1"><p>Prestadores de Serviço Biométrico</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>RFC</p></td>      <td rowspan="1" colspan="1"><p>Request for Comments</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>UTC</p></td>      <td rowspan="1" colspan="1"><p><em>Universal Time Coordinated</em></p></td>     </tr>    </tbody>   </table>

1 DISPOSIÇÕES GERAIS

1.1 A hora utilizada pelas entidades integrantes da Infraestrutura de Chaves Públicas Brasileira - ICP-Brasil, será fornecida pela AC RAIZ às Autoridades Certificadoras de primeiro nível e Prestadores de Serviço Biométrico-PSBio, por meio do serviço Network Time Protocol - NTP, descrito pela RFC 5905.

1.2 O serviço provido pelo ITI utiliza equipamentos sincronizados com a Fonte Confiável do Tempo - FCT, sendo os registros de suas operações mantidos pelo prazo estabelecido nos normativos da ICP-Brasil, a fim de prover a rastreabilidade e auditoria da infraestrutura.

2 SERVIÇO DE SINCRONISMO DO TEMPO

2.1 Operação de Sincronismo

2.1.1 As operações de sincronismo das ACs devem ser realizadas com sucesso ao mínimo uma vez a cada 24 (vinte e quatro) horas.

2.1.2 As ACs de primeiro nível e os PSBIO devem obter a hora UTC (Universal Time Coordinated - UTC) do serviço disponibilizado pelo ITI em 3 (três) servidores, nas URL ntp1.icpbrasil.gov.br, ntp2.icpbrasil.gov.br e ntp3.icpbrasil.gov.br. Para sincronização do relógio de seu(s) servidor(es) de tempo, as ACs devem utilizar como referência os três servidores do ITI simultaneamente.

2.1.3 A partir do sincronismo dos relógios dos servidores de tempo das ACs, estes devem disciplinar a hora UTC de todos os computadores e equipamentos de rede da sua infraestrutura, conforme legislação vigente.

2.1.4 As ACs de primeiro nível e os PSBIOs devem propagar, quando for o caso, a hora UTC para as ACs ou PSBIOs sob sua vinculação.

2.2 Acesso ao Serviço

2.2.1 Para ter acesso ao serviço de sincronismo do tempo, as ACs de primeiro nível ou seus Prestadores de Serviço de Suporte (PSS) devem encaminhar mensagem de correio eletrônico, assinada digitalmente pelo respectivo representante, com certificado padrão ICP-Brasil, para o endereço cgope@iti.gov.br com as seguintes informações:

a) endereço(s) IP(s) dos servidores de tempo da AC, a partir do(s) qual(is) será(ão) realizados os acessos aos serviços disponibilizados pelo ITI;

b) informações da AC ou PSS: Nome, telefone e endereço de correio eletrônico do(s) responsável(is) ou o contato (s) técnico(s).

2.2.2 No caso de alteração de quaisquer dos dados acima, a AC ou seu PSS deverá retificá-la através do mesmo endereço eletrônico.

2.3 Comunicação

2.3.1 Qualquer alteração no serviço de sincronismo do tempo disponibilizado pelo ITI será comunicada através de mensagens de correio eletrônico, assinadas digitalmente com certificado padrão ICP-Brasil, para os endereços informados pelas ACs.

2.3.2 Em caso de problema de acesso aos serviços disponibilizados pelo ITI, a AC ou PSS deverá comunicar o ocorrido por meio de mensagem de correio eletrônico para o endereço informado acima, assinada digitalmente pelo respectivo representante com certificado padrão ICP-Brasil.

2.3.3 Mensagens recebidas em não conformidade com as especificações acima serão descartadas automaticamente.

3 REFERÊNCIAS

RFC 5905, IETF -*Network Time Protocol Version 4: Protocol and Algorithms Specification,june*2010.

INSTRUÇÃO NORMATIVA ITI Nº 20, DE 23 DE NOVEMBRO DE 2020

Aprova a versão revisada e consolidada do documento Procedimentos Operacionais Mínimos para os Prestadores de Serviço de Confiança da ICP-Brasil DOC-ICP-17.01.

**O DIRETOR-PRESIDENTE DO INSTITUTO NACIONAL DE TECNOLOGIA DA INFORMAÇÃO**, no uso das atribuições que lhe foram conferidas pelo inciso VI do art. 9º do anexo I do Decreto nº 8.985, de 8 de fevereiro de 2017, pelo art. 1º da Resolução nº 33 do Comitê Gestor da ICP-Brasil, de 21 de outubro de 2004, e pelo art. 2º da Resolução nº 163 do Comitê Gestor da ICP-Brasil, de 17 de abril de 2020,

CONSIDERANDO a determinação estabelecida pelo Decreto nº 10.139, de 28 de novembro de 2019, para revisão e consolidação dos atos normativos inferiores a decreto, editados por órgãos e entidades da administração pública federal direta, autárquica e fundacional, resolve:

**Art. 1º** Esta Instrução Normativa aprova a versão revisada e consolidada do documento Procedimentos Operacionais Mínimos para os Prestadores de Serviço de Confiança da ICP-Brasil DOC-ICP-17.01.

**Art. 2º** Fica aprovada a versão 3.0 do documento DOC-ICP-17.01 - Procedimentos Operacionais Mínimos para os Prestadores de Serviço de Confiança, anexa a esta Instrução Normativa.

**Art. 3º** Ficam revogadas:

I - a Instrução Normativa nº 10, de 15 de dezembro de 2017;

II - a Instrução Normativa nº 06, de 16 de abril de 2018;

III - a Instrução Normativa nº 02, de 12 de março de 2019;

IV - a Instrução Normativa nº 03, de 04 de abril de 2019;

V - a Instrução Normativa nº 07, de 30 de outubro de 2019; e

VI - a Instrução Normativa nº 07, de 29 de maio de 2020.

**Art. 4º** Esta Instrução Normativa entra em vigor em 1° de dezembro de 2020.

CARLOS ROBERTO FORTNER

PROCEDIMENTOS OPERACIONAIS MÍNIMOS PARA OS PRESTADORES DE SERVIÇO

DE CONFIANÇA DA ICP-BRASIL

DOC-ICP-17.01

Versão 3.0

23 de novembro de 2020

CONTROLE DE ALTERAÇÕES

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução ou IN que aprovou a alteração</p></td>      <td rowspan="1" colspan="1"><p>Item alterado</p></td>      <td rowspan="1" colspan="1"><p>Descrição da alteração</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa ITI nº 20, de 23.11.2020</p><p>Versão 3.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Revisão e consolidação, conforme o Decreto nº 10.139, de 28 de novembro de 2019.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa nº 07,</p><p>de 29.05.2020</p><p>Versão 2.3</p></td>      <td rowspan="1" colspan="1"><p>4.g e 12</p></td>      <td rowspan="1" colspan="1"><p>Altera o tempo de armazenamento dos logs, trilhas de auditorias e imagens.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa nº 07,</p><p>de 30.10.2019</p><p>Versão 2.2</p></td>      <td rowspan="1" colspan="1"><p>6.4 e 6.5.7</p></td>      <td rowspan="1" colspan="1"><p>Corrige endereço do serviço de recuperação do certificado e inclui previsão de serviço de autenticação do titular sem uso de chave. Corrige numeração dos subitens do item 6.4.5.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa nº 03,</p><p>de 04.04.2019</p><p>Versão 2.1</p></td>      <td rowspan="1" colspan="1"><p>6.4.5.2, 6.4.5.6 e 6.4.6.2.1</p></td>      <td rowspan="1" colspan="1"><p>Inclusão do parâmetro<em>hash_algorithm</em>.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa nº 02,</p><p>de 12.03.2019</p><p>Versão 2.0</p></td>      <td rowspan="1" colspan="1"><p>6.4 e 6.5</p></td>      <td rowspan="1" colspan="1"><p>Atualização dos requisitos para serviços de confiança de uso de chaves privadas.</p><p>Inclusão da definição da Lista de Prestadores de Serviço de Confiança - LPSC.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa nº 06,</p><p>de 16.04.2018</p><p>Versão 1.1</p></td>      <td rowspan="1" colspan="1"><p>6.4</p></td>      <td rowspan="1" colspan="1"><p>Item incluído - Requisitos para serviços de confiança de uso de chaves privadas.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa nº 10,</p><p>de 15.12.2017</p><p>Versão 1.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Criação do DOC-ICP-17.01.</p></td>     </tr>    </tbody>   </table>

LISTA DE ACRÎNIMOS

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>SIGLA</p></td>      <td rowspan="1" colspan="1"><p>DESCRIÇÃO</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AC</p></td>      <td rowspan="1" colspan="1"><p>Autoridade Certificadora</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AC RAIZ</p></td>      <td rowspan="1" colspan="1"><p>Autoridade Certificadora Raiz da ICP-Brasil</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ACT</p></td>      <td rowspan="1" colspan="1"><p>Autoridade de Carimbo do Tempo</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AES</p></td>      <td rowspan="1" colspan="1"><p><em>Advanced Encryption Standard</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>APF</p></td>      <td rowspan="1" colspan="1"><p>Administração Pública Federal</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>API</p></td>      <td rowspan="1" colspan="1"><p>Application Programming Interface</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>CAdES</p></td>      <td rowspan="1" colspan="1"><p>CMS Advanced Electronic Signature</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>CTR</p></td>      <td rowspan="1" colspan="1"><p>Counter Mode</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>DPPSC</p></td>      <td rowspan="1" colspan="1"><p>Declaração de Prática do Prestador de Serviço de Confiança</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>EAT</p></td>      <td rowspan="1" colspan="1"><p>Entidade de Auditoria do Tempo - ICP-Brasil</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ETSI</p></td>      <td rowspan="1" colspan="1"><p>European Telecommunications Standards Institute</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>HMAC</p></td>      <td rowspan="1" colspan="1"><p>Hash-based Message Authentication Code</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>HOTP</p></td>      <td rowspan="1" colspan="1"><p>HMAC-Based One-Time Password</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>HSM</p></td>      <td rowspan="1" colspan="1"><p>Hardware Security Module</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>HTTPS</p></td>      <td rowspan="1" colspan="1"><p>Hyper Text Transfer Protocol Secure</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ICP-BRASIL</p></td>      <td rowspan="1" colspan="1"><p>Infraestrutura de Chaves Públicas Brasileira</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IETF</p></td>      <td rowspan="1" colspan="1"><p>Internet Engineering Task Force</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ITI</p></td>      <td rowspan="1" colspan="1"><p>Instituto Nacional de Tecnologia da Informação</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>JSON</p></td>      <td rowspan="1" colspan="1"><p>JavaScript Object Notation</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>KMIP</p></td>      <td rowspan="1" colspan="1"><p>Key Management Interoperability Protocol</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>LPA</p></td>      <td rowspan="1" colspan="1"><p>Lista de Políticas de Assinatura Aprovadas</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>LPSC</p></td>      <td rowspan="1" colspan="1"><p>Lista de Prestadores de Serviço de Confiança</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>OATH</p></td>      <td rowspan="1" colspan="1"><p>Open Authentication</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PAdES</p></td>      <td rowspan="1" colspan="1"><p>PDF Advanced Electronic Signature</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PCO</p></td>      <td rowspan="1" colspan="1"><p>Planejamento de Capacidade Operacional</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PIN</p></td>      <td rowspan="1" colspan="1"><p>Personal Identification Number</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PSBio</p></td>      <td rowspan="1" colspan="1"><p>Prestador de Serviço Biométrico</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PSC</p></td>      <td rowspan="1" colspan="1"><p>Prestador de Serviço de Confiança</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PKCS</p></td>      <td rowspan="1" colspan="1"><p>Public Key Cryptography Standards</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PUK</p></td>      <td rowspan="1" colspan="1"><p>PIN Unlock</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>RFC</p></td>      <td rowspan="1" colspan="1"><p>Request for Comments</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>SSL</p></td>      <td rowspan="1" colspan="1"><p>Secure Sockets Layer</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>TLS</p></td>      <td rowspan="1" colspan="1"><p>Transport Layer Security</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>TOTP</p></td>      <td rowspan="1" colspan="1"><p>Time-based One-Time Password algorithm</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>TRC</p></td>      <td rowspan="1" colspan="1"><p>Teorema do Resto Chinês</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>TTLV</p></td>      <td rowspan="1" colspan="1"><p>Tag, type, length, value</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>XAdES</p></td>      <td rowspan="1" colspan="1"><p>XML Advanced Electronic Signatures</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>XML</p></td>      <td rowspan="1" colspan="1"><p>eXtensible Markup Language</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>XMPP</p></td>      <td rowspan="1" colspan="1"><p>Extensible Messaging and Presence Protocol</p></td>     </tr>    </tbody>   </table>

1 DISPOSIÇÕES GERAIS

1.1. Este documento tem por finalidade regulamentar os requisitos mínimos de segurança e os procedimentos operacionais a serem adotados pelos Prestadores de Serviço de Confiança (PSC) de Assinatura Digital e/ou Armazenamento de Chaves Criptográficas da ICP-Brasil.

1.2. Suplementa, para essas entidades, os regulamentos contidos nos documentos DOC-ICP-03 [1], DOC-ICP-04 [2], DOC-ICP-08 [3] e DOC-ICP-09 [4], tomando como base também a Política de Segurança da ICP-Brasil - DOC-ICP-02 [5].

1.3 Os requisitos contidos neste documento deverão ser apresentados quando do credenciamento do PSC para armazenamento de chaves privadas dos usuários finais ou serviços de assinaturas digitais, verificação de assinaturas digitais, se for o caso, ou ambos e mantidos atualizados durante seu funcionamento enquanto a entidade estiver credenciada na ICP-Brasil.

1.4. O PSC deverá ter uma Política de Segurança da Informação composta por diretrizes, normas e procedimentos que descrevem os controles de segurança que devem ser seguidos em suas dependências e atividades, em consonância com o DOC-ICP-02 [5].

1.5. Deverá existir um exemplar da Política de Segurança da Informação, no formato impresso, disponível para consulta no Nível 1 (vide regulamento no item 3) de segurança do PSC.

1.6. A Política de Segurança da Informação deverá ser seguida por todo pessoal envolvido nas atividades realizadas pelo PSC, do seu próprio quadro ou contratado.

1.7. Este documento define normas operacionais e de segurança que deverão ser aplicadas nas áreas internas ao PSC, assim como no trânsito de informações e materiais com entidades externas, armazenamento de chaves privadas, serviços de assinatura digital e verificação de assinatura digital.

1.8. A seguir são informados os requisitos que devem ser observados quanto a segurança de pessoal, segurança física, segurança lógica, segurança de rede, requisitos mínimos para armazenamento de chaves privadas, serviços de assinatura digital e verificação de assinatura digital, classificação da informação, salvaguarda de ativos da informação, gerenciamento de riscos, plano de continuidade de negócios, análise de registros de eventos e plano de capacidade operacional.

2 SEGURANÇA PESSOAL

2.1. O PSC deverá ter uma Política de Gestão de Pessoas que disponha sobre os processos de contratação, demissão, descrição de cargos, avaliação de desempenho e capacitação.

2.2. A comprovação da capacidade técnica do pessoal envolvido nos serviços prestados pelo PSC deverá estar à disposição para eventuais auditorias e fiscalizações.

2.3. Todo pessoal envolvido nas atividades realizadas pelo PSC, do próprio quadro ou contratado, deverá assinar um termo, com garantias jurídicas, que garanta o sigilo das informações internas e de terceiros, mesmo após a demissão ou o término do contrato.

2.4. O termo de sigilo da informação deverá conter cláusula explícita de responsabilização nos casos de quebra de regras ou regulamentos da ICP-Brasil.

2.5. Aplicar-se-á o termo de sigilo de informações a quaisquer outras entidades que porventura tenham acesso às informações internas e de terceiros originárias dos projetos coordenados pelo PSC.

2.6. O PSC deverá ter procedimentos formais de apuração e responsabilização em caso de descumprimento das regras estabelecidas pelas suas políticas ou pelas normas da ICP-Brasil.

2.7. O quadro de pessoal do PSC e contratados deverão possuir um dossiê contendo os seguintes documentos:

a) contrato de trabalho ou cópia das páginas da carteira de trabalho onde conste o registro da contratação, termo de posse de servidor ou comprovante de situação funcional;

b) comprovante da verificação de antecedentes criminais;

c) comprovante da verificação de situação de crédito;

d) comprovante da verificação de histórico de empregos anteriores;

e)comprovação de residência;

f) comprovação de capacidade técnica;

g) resultado da entrevista inicial, com a assinatura do entrevistador;

h) declaração em que afirma conhecer as suas atribuições e em que assume o dever de cumprir as regras aplicáveis da ICP-Brasil;

i) termo de sigilo.

3 SEGURANÇA FÍSICA

3.1. Disposições Gerais de Segurança Física

3.1.1. Níveis de acesso

3.1.1.1. São definidos pelo menos 4 (quatro) níveis de acesso físico aos diversos ambientes do PSC.

3.1.1.1.1. O primeiro nível - ou nível 1 - deverá situar-se após a primeira barreira de acesso às instalações do PSC. O ambiente de nível 1 do PSC na ICP-Brasil desempenha a função de interface com cliente ou fornecedores que necessita comparecer ao PSC.

3.1.1.1.2. O segundo nível - ou nível 2 - será interno ao primeiro e deverá requerer a identificação individual das pessoas que nele entram. Esse será o nível mínimo de segurança requerido para a execução de qualquer processo operacional ou administrativo do PSC. A passagem do primeiro para o segundo nível deverá exigir identificação por meio eletrônico e o uso de crachá.

a) o ambiente de nível 2 deverá ser separado do nível 1 por paredes divisórias de escritório, alvenaria ou pré-moldadas de gesso acartonado. Não deverá haver janelas ou outro tipo qualquer de abertura para o exterior, exceto a porta de acesso;

b) o acesso a este nível deverá ser permitido apenas a pessoas que trabalhem diretamente com as atividades de serviços de armazenamento dos certificados para usuários finais e serviços de assinatura digital e verificação da assinatura digital ou ao pessoal responsável pela manutenção de sistemas e equipamentos do PSC, como administradores de rede e técnicos de suporte de informática. Demais funcionários do PSC ou do possível ambiente que esta compartilhe não deverão acessar este nível;

c) preferentemente, nobreaks, geradores e outros componentes da infraestrutura física deverão estar abrigados neste nível, para evitar acessos ao ambiente de nível 3 por parte de prestadores de serviços de manutenção;

d) excetuados os casos previstos em lei, o porte de armas não será admitido nas instalações do PSC, a partir do nível 2. A partir desse nível, equipamentos de gravação, fotografia, vídeo, som ou similares, bem como computadores portáteis, terão sua entrada controlada e somente poderão ser utilizados mediante autorização formal e sob supervisão.

3.1.1.1.3. O terceiro nível - ou nível 3 - deverá situar-se dentro do segundo e será o primeiro nível a abrigar material e atividades sensíveis da operação do PSC. Qualquer atividade relativa ao armazenamento de certificados digitais dos usuários e serviços de assinatura digital e verificação da assinatura digital deverá ser realizada nesse nível. Somente pessoas autorizadas poderão permanecer nesse nível.

a) no terceiro nível deverão ser controladas tanto as entradas quanto as saídas de cada pessoa autorizada. Dois tipos de mecanismos de controle deverão ser requeridos para a entrada nesse nível: algum tipo de identificação individual, como cartão eletrônico, e identificação biométrica ou digitação de senha;

b) as paredes que delimitam o ambiente de nível 3 deverão ser de alvenaria ou material de resistência equivalente ou superior. Não deverá haver janelas ou outro tipo qualquer de abertura para o exterior, exceto a porta de acesso;

c) caso o ambiente de Nível 3 possua forro ou piso falsos, deverão ser adotados recursos para impedir o acesso ao ambiente por meio desses, tais como grades de ferro estendendo-se das paredes até as lajes de concreto superior e inferior;

d) deve haver uma porta única de acesso ao ambiente de nível 3, que abra somente depois que o funcionário tenha se autenticado eletronicamente no sistema de controle de acesso. A porta deverá ser dotada de dobradiças que permitam a abertura para o lado externo, de forma a facilitar a saída e dificultar a entrada no ambiente, bem como de mecanismo para fechamento automático, para evitar que permaneça aberta mais tempo do que o necessário;

3.1.1.1.4. O terceiro nível avançado - ou nível 3.1 -, especificamente para os PSC de assinatura digital, no interior ao ambiente de nível 3, deverá compreender pelo menos um gabinete reforçado trancado, que abrigará todo o hardware e software utilizado pelo PSC de assinatura digital:

a) para garantir a segurança do material armazenado, os gabinetes deverão obedecer às seguintes especificações mínimas:

i. ser feitos em aço ou material de resistência equivalente;

ii. possuir tranca com chave.

3.1.1.1.5. O quarto nível - ou nível 4 - especificamente para os PSC de armazenamento de chaves privadas, interior ao terceiro, é onde deverão ocorrer atividades especialmente sensíveis da operação do PSC de armazenamento de chaves privadas. Todos os sistemas e equipamentos necessários a essas atividades deverão estar localizados a partir desse nível. O nível 4 deverá possuir os mesmos controles de acesso do nível 3 e, adicionalmente, deverá exigir, em cada acesso ao seu ambiente, a identificação de, no mínimo, 2 (duas) pessoas autorizadas. Nesse nível, a permanência dessas pessoas deverá ser exigida enquanto o ambiente estiver ocupado.

3.1.1.1.6 No quarto nível, todas as paredes, piso e teto deverão ser revestidos de aço e concreto ou de outro material de resistência equivalente. As paredes, piso e o teto deverão ser inteiriços, constituindo uma célula estanque contra ameaças de acesso indevido, água, vapor, gases e fogo. Os dutos de refrigeração e de energia, bem como os dutos de comunicação, não deverão permitir a invasão física das áreas de quarto nível. Adicionalmente, esses ambientes de nível 4 - que constituem as chamadas salas-cofre - deverão possuir proteção contra interferência eletromagnética externa.

3.1.1.1.7. As salas-cofre deverão ser construídas segundo as normas brasileiras aplicáveis. Eventuais omissões dessas normas deverão ser sanadas por normas internacionais pertinentes.

3.1.1.2. Poderão existir, no PSC, vários ambientes de terceiro nível avançado, no caso de PSC de assinatura digital, ou vários ambientes de quarto nível, no caso de PSC de armazenamento de chaves privadas, para abrigar e segregar, quando for o caso:

a) equipamentos de produção on-line; e

b) equipamentos de rede e infraestrutura (firewall, roteadores, switches e servidores).

3.1.1.3. Todos os servidores e elementos de infraestrutura e proteção do segmento de rede, tais como roteadores, hubs, switches e firewalls devem:

a) operar em ambiente com segurança equivalente, no mínimo, no terceiro nível avançado para o caso de PSC de assinatura digital, ou no quarto nível, no caso de PSC de armazenamento de chaves privadas citados neste documento;

b) possuir acesso lógico restrito por meio de sistema de autenticação e autorização de acesso.

3.1.1.4. Os PSC devem ainda atender aos seguintes requisitos:

a) o ambiente físico do PSC deverá conter dispositivos que autentiquem e registrem o acesso de pessoas informando data e hora desses acessos;

b) o PSC deverá conter imagens que garantam a identificação de pessoas quando do acesso físico em qualquer parte de seu ambiente;

c) é mandatório o sincronismo de data e hora entre os mecanismos de segurança física garantindo a trilha de auditoria entre dispositivos de controle de acesso físico e de imagem;

d) todos que transitam no ambiente físico do PSC deverão portar crachás de identificação, inclusive os visitantes;

e) só é permitido o trânsito de material de terceiros pelos ambientes físicos do PSC mediante registro, garantindo a trilha de auditoria com informações de onde o material passou, a data e hora que ocorreu o trânsito e quem foi o responsável por sua manipulação;

f) o PSC deverá conter dispositivos de prevenção e controle de incêndios, temperatura, umidade, iluminação e oscilação na corrente elétrica em todo seu ambiente físico;

g) todo material crítico inservível, descartável ou não mais utilizável deverá ter tratamento especial de destruição, garantindo o sigilo das informações lá contidas. O equipamento enviado para manutenção deverá ter seus dados apagados, de forma irreversível, antes de ser retirado do ambiente físico do PSC;

h) os computadores pessoais, servidores e dispositivos de rede, e seus respectivos softwares, deverão estar inventariados com informações que permitam a identificação inequívoca;

i) em caso de inoperância dos sistemas automáticos, o controle de acesso físico deverá ser realizado provisoriamente por meio de um livro de registro onde constará quem acessou, a data, hora e o motivo do acesso;

j) deverão ser providenciados mecanismos para garantir a continuidade do fornecimento de energia nas áreas críticas, mantendo os ativos críticos de informação em funcionamento até que todos os processos e dados sejam assegurados caso o fornecimento de emergência se esgote;

l) no caso de armazenamento de chaves privadas para usuários finais, deve ter no mínimo dois ambientes físicos, sendo obrigatoriamente um para operação e outro para contingência;

m) no caso do PSC ser uma AC da ICP-Brasil, pode ser utilizado o nível 4 para abrigo do hardware criptográfico que armazenará as chaves privadas dos usuários finais, assim como os serviços de autenticação, desde que em gabinete cadeado, cuja chave do cadeado deve estar em posse de funcionário distinto dos perfis lógicos do PSC, segregados dos que operam o ambiente de uma AC;

n) todos os equipamentos e ambiente computacional que serão utilizados no PSC deverão ter sua data e horário sincronizados com a EAT.

4 SEGURANÇA LÓGICA

4.1 O acesso lógico ao ambiente computacional do PSC se dará no mínimo mediante usuário individual e senha, que deverá ser trocada periodicamente;

4.2 Todos os equipamentos do parque computacional deverão ter controle de forma a permitir somente o acesso lógico a pessoas autorizadas;

4.3 Os equipamentos deverão ter mecanismos de bloqueio de sessão inativa;

4.4 O PSC deverá ter explícita a política de cadastro, suspensão e remoção de usuários em seu ambiente computacional. Os usuários deverão estar cadastrados em perfis de acesso que permitam privilégio mínimo para realização de suas atividades;

4.5 Os usuários especiais (a exemplo do root e do administrador) de sistemas operacionais, do hardware criptográfico, do banco de dados e de aplicações em geral devem ter suas senhas segregadas de forma que o acesso lógico a esses ambientes se dê por, pelo menos, duas pessoas autorizadas;

4.6 Todo equipamento do PSC deverá ter log ativo e seu horário sincronizado com uma fonte confiável do tempo da ICP-Brasil;

4.7 As informações como log, trilhas de auditoria (do armazenamento de chaves privadas e serviço de assinatura), registros de acesso (físico e lógico) e imagens deverão ter cópia de segurança cujo armazenamento será de 7(sete) anos;

4.8 Os softwares dos sistemas operacionais, os antivírus e aplicativos de segurança devem ser mantidos atualizados;

4.9 É vedado qualquer tipo de acesso remoto dos operadores do PSC ao ambiente de nível 3.

5 SEGURANÇA DE REDE

5.1 O tráfego das informações no ambiente de rede deverá ser protegido contra danos ou perdas, bem como acesso, uso ou exposição indevidos;

5.2 Não poderão ser admitidos acessos externos à rede interna do PSC. As tentativas de acessos externos deverão ser inibidas e monitoradas por meio de aplicativos que criem barreiras e filtros de acesso, assim como mecanismos de detecção de intrusão;

5.3 Deverão ser aplicados testes de segurança na rede interna e externa com aplicativos especializados com periodicidade de, no mínimo, uma vez a cada mês. Os testes na rede deverão ser documentados e as vulnerabilidades detectadas corrigidas.

6 REQUISITOS PARA ARMAZENAMENTO DE CHAVES PRIVADAS

6.1 Armazenamento das chaves e certificados digitais.

6.1.1 As chaves privadas dos usuários finais, para os tipos de certificados que obrigatoriamente devem ser gerados e armazenados em hardware criptográficos, devem estar armazenadas dentro dos espaços (slots), ou equivalente, da fronteira criptográfica e segurança física de um HSM com certificação Inmetro válida no âmbito da ICP-Brasil, endereçados por conta de usuário;

6.1.2 Esse acesso ou comando de exportação às chaves privadas dos usuários deve ser de uso, conhecimento e controle exclusivo do titular, sem a possibilidade de ingresso por outros titulares no mesmo HSM, qualquer funcionário do PSC ou dependentes de outras chaves criptográficas;

6.1.3 O PSC deve prover mecanismos de duplo fator de autenticação ao titular para acesso à chave privada, devendo ser um fator dentro da fronteira criptográfica do HSM e outro dentro do ambiente seguro e primeira interface de comunicação com HSM ou ambos dentro da fronteira criptográfica do HSM. Cada fator deve ser de uma classe diferente (conhecimento, posse ou biometria). Os mecanismos de autenticação devem empregar método ou protocolo de validação que proteja a transmissão e os dados de autenticação por meio de criptografia. Essa funcionalidade será apensada aos requisitos técnicos na manutenção da certificação Inmetro dos HSM e devem ser:

a) senhas (PIN/PUK): segundo regras da ICP-Brasil;

b) OTP: segundo regras da RFC 6238 (TOTP), RFC 6287, RFC 4226 (HOTP);

c) biometria: segundo regras da ICP-Brasil;

d) certificado de atributo: segundo regras da ICP-Brasil;

e) Push Notification: segundo regras do XMPP extension protocol ou semelhante;

f) outras autenticações semânticas em acordo com esse documento e previamente aprovadas pela AC Raíz.

6.1.4 Deverá ser feita, em outro ambiente físico de contingência, a cópia das chaves dos usuários finais, observados os mesmos requisitos de armazenamento do ambiente principal. A entrada do ambiente de contingência deve ser em até 48 horas.

6.1.5 Esses espaços para armazenamento das chaves privadas dos usuários finais poderão ser liberados desde que não haja renovação por parte do mesmo ou a revogação da chave, entretanto deve-se manter o registro de armazenamento das chaves conforme Declaração de Prática do Prestador de Serviço de Confiança - DPPSC.

6.2 Protocolos

6.2.1 Os HSMs certificados na ICP-Brasil devem suportar a interface PKCS#11, atendendo às exigências de especificação da ICP-Brasil, além dos relatados nesse documento, os seguintes requisitos:

a) gerar chaves simétricas especificando os componentes de chaves simétricas em texto claro;

\* Gerar par de chaves especificando os componentes de chaves assimétricas em texto claro. Por exemplo os componentes Módulo, Expoente público, tamanho em bits, etc;

\* Gerar objeto de chaves especificando os componentes de chaves assimétricas (no mínimo chave pública) em texto claro. Por exemplo os componentes: Módulo, Expoente público, Expoente Privada em forma reduzida ou em forma de TRC (Teorema de Resto Chinês);

\* Cifrar e decifrar chaves especificando os componentes de chaves simétricas ou assimétrica em texto claro;

\* Exportar e importar chaves (PKCS#12) especificando os componentes de chaves assimétricas privadas criptografados;

\* Assinar conteúdo especificando os componentes de chaves assimétricas públicas em texto claro;

\* Verificar assinatura especificando os componentes de chaves assimétricas públicas em texto claro.

b) o módulo criptográfico deve suportar as seguintes chamadas de PKCS#11 (Cryptoki):

\* C\_Initalize

\* C\_Finalize

\* C\_OpenSession

\* C\_CloseSession

\* C\_Init\_Token

\* C\_Init\_PIN

\* C\_Login

\* C\_Logout

\* C\_CreateObject

\* C\_DestroyObject

\* C\_GetAttributeValue

\* C\_SetAttributeValue

\* C\_EncryptInit

\* C\_Encrypt

\* C\_DecryptInit

\* C\_Decrypt

\* C\_DigestInit

\* C\_Digest

\* C\_DigestKey

\* C\_SignInit

\* C\_Sign

\* C\_VerifyInit

\* C\_Verify

\* C\_GenerateKey

\* C\_GenerateKeyPair

\* C\_DeriveKey

\* C\_GenerateRandom

\* C\_WrapKey

\* C\_UnwrapKey

c) sendo obrigatória a implementação das seguintes funções:

\* C\_GenerateKey especificando templates de chaves simétricas;

\* C\_GenerateKeyPair especificando templates de chaves assimétricas;

\* C\_Sign para realizar assinatura de um conteúdo;

\* C\_Verify para verificar a assinatura de um conteúdo;

\* C\_Encrypt para cifrar um dado com uma chave já construída;

\* C\_Decrypt para decifrar um dado com uma chave já construída;

\* C\_CreateObject especificando templates de chaves assimétricas (no mínimo chave pública);

\* C\_DestroyObject especificando o handle do objeto.

6.2.2 Os HSMs certificados na ICP-Brasil devem suportar o protocolo Key Management Interoperability Protocol - KMIP, versão 1.3 ou superior, devendo seguir, além dos relatados nesse documento, os seguintes requisitos:

6.2.2.1 Os PSC devem definir um conjunto de operações que se aplicam aos objetos gerenciados, relacionados ao conjunto normativo do PSC e ao ciclo de vida das chaves, que por sua vez consistem em atributos, como mostrado, em exemplo, na tabela a seguir.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Operações do Protocolo</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Objetos Gerenciados</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Atributos dos Objetos</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Create</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Certificate</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Unique Identifier</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Create Key Pair</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Symmetric Key</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Name</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Register</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Public Key</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Object Type</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Re-key</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Private Key</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Cryptographic Algorithm</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Derive Key</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Split Key</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Cryptographic Length</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Certify</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Secret Data</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Cryptographic Parameters</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Re-certify</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Key Block (para chaves) ou<em>Value</em>(para certificados)</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p><em>Certificate Type</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Locate</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Certificate Issuer</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Check</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Certificate Subject</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Get</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Digest</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Get Attributes</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Operation Policy Name</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Get Attribute List</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Cryptographic Usage Mask</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Add Attribute</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Lease Time</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Modify Attribute</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Usage Limits</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Delete Attribute</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>State</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Obtain Lease</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Initial Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Get Usage Allocation</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Activation Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Activate</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Process Start Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Revoke</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Protect Stop Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Destroy</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Deactivation Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Archive</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Destroy Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Recover</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Compromise Occurrence Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Validate</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Compromise Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Query</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Revocation Reason</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Cancel</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Archive Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Poll</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Object Group</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Link</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Application Specific ID</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Contact Information</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Last Change Date</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Custom Attribute</p></td>     </tr>    </tbody>   </table>

6.2.2.2 Os objetos base são:

a) os componentes dos objetos gerenciados.

i. Atributo: identificado pelo seu nome;

ii. Key Block, contém o valor da chave;

b) os elementos do protocolo de mensagens;

c) os parâmetros das operações.

6.2.2.3 Os objetos criptográficos gerenciáveis são:

a) Certificado, com o tipo e valor;

b) Chave Simétrica, com o Key Block;

c) Chave Pública, com o Key Block;

d) Chave Privada, com o Key Block;

e) Chave Dividida, com o par e o Key Block;

f) Dados Reservados, com o tipo e o Key Block.

6.2.2.4 Os atributos contêm os metadados de um objeto gerenciável, nos quais:

a) número identificador único, estado, entre outros;

b) os atributos devem ser pesquisados com a operação "locate".

6.2.2.5 Os atributos podem ser configurados, modificados e apagados quando a especificação KMIP permitir esses pelo cliente.

6.2.2.6 Os valores das estruturas de codificações (TTLV, definição dos valores, Text String, Structure, Byte String, Integer, Big Integer, Long Integer, Boolean, Date-Time e Enumerations), dos campos dos objetos, dos atributos, dos formatos e conteúdos das mensagens, da manipulação de erros e dos parâmetros (solicitação e resposta) das operações cliente/servidor devem seguir integralmente o estabelecido neste documento e no Key Management Interoperability Protocol Specification Version 1.3, OASIS Standard, 27 December 2016, ou versionamento superior.

NOTA: O ITI poderá requisitar aos PSC em credenciamento ou credenciados testes dos modelos descritos, ou outras versões, nos sítios https://www.snia.org/forums/ssif/kmip, http://docs.oasis-open.org/kmip/profiles/v1.3/csd01/kmip-profiles-v1.3-csd01.html ou equivalente.

6.2.2.7 A criação do usuário deve seguir o estabelecido a seguir (xml):

&lt;RequestMessage>

&lt;RequestHeader>

&lt;ProtocolVersion>

&lt;ProtocolVersionMajor type="Integer" value="1"/>

&lt;ProtocolVersionMinor type="Integer" value="3"/>

&lt;/ProtocolVersion>

&lt;Authentication>

&lt;Credential>

&lt;CredentialType type="Enumeration" value="UsernameAndPassword"/>

&lt;CredentialValue>

&lt;Username type="TextString" value="vco\_test"/>

&lt;Password type="TextString" value="Teste112233$"/>

&lt;/CredentialValue>

&lt;/Credential>

&lt;/Authentication>

&lt;BatchCount type="Integer" value="1"/>

&lt;/RequestHeader>

&lt;BatchItem>

&lt;Operation type="Enumeration" value="CreateUser"/>

&lt;RequestPayload>

&lt;UserName type="TextString" value="labsec-pw"/>

&lt;UserType type="Enumeration" value="User"/>

&lt;/RequestPayload>

&lt;/BatchItem>

&lt;/RequestMessage>

6.2.2.8 Para a operação do duplo fator de autenticação do titular da chave privada, poderá ser criada uma nova extensão ao tipo de credencial, conforme relatado a seguir:

6.2.2.9 Para o novo tipo de credencial deve ser configurado o seguinte:

a) Credential Type: TOKEN

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Object</p></td>      <td rowspan="1" colspan="1"><p><em>Encoding</em></p></td>      <td rowspan="1" colspan="1"><p>Required</p></td>      <td rowspan="1" colspan="1"><p>Description</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Credential Value</p></td>      <td rowspan="1" colspan="1"><p>Structure</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Token</p></td>      <td rowspan="1" colspan="1"><p>Text String</p></td>      <td rowspan="1" colspan="1"><p>Yes</p></td>      <td rowspan="1" colspan="1"><p>Valor atual do "TOKEN"</p></td>     </tr>    </tbody>   </table>

b) fluxo de uso

i. durante o credenciamento, o PSC deve requisitar a criação de um novo usuário (via KMIP), indicando que o mesmo necessita de um segundo fator de autenticação para utilizar seus objetos e cadastrando seu nome de usuário e senha. O PSC indica ao usuário como instalar seu aplicativo de Token.

ii. o "TOKEN" do usuário deve ser inicializado para sincronizar seus dados. Esse processo pode ser feito pelo próprio usuário através do aplicativo de "TOKEN" via KMIP no momento da primeira conexão utilizando seu usuário e senha. O HSM gera então a chave que será utilizada no "TOKEN".

iii. na posse de seu "TOKEN" sincronizado e de seu usuário e senha, o usuário pode então criar sua chave no HSM utilizando a aplicação do PSC diretamente via comando KMIP.

iv. o usuário já pode utilizar sua chave criada anteriormente utilizando o aplicativo do PSC, de posse de sua Senha + Token.

6.2.2.10 Este mecanismo de "TOKEN" deve ser configurado na área de execução segura do HSM.

NOTA: Pode ser encontrada mais referências sobre o protocolo KMIP no sítio https://www.oasis-open.org/committees/tc\_home.php?wg\_abbrev=kmip.

6.2.2.11 As soluções do PSC deverão garantir a portabilidade da chave privada do usuário conforme o descritivo:

a) glossário:

CPrUi: Chave privada do usuário 'i', armazenada no HSM 1, a ser exportada e importada para o HSM 2;

CPrHe2: Chave privada do HSM 2, a ser utilizada para importação de chaves privadas de usuários gravadas no HSM 1;

CPuHe2: Chave Pública do HSM 2, utilizada para exportação de chaves privadas de usuários armazenadas no HSM 1, a serem importadas pelo HSM 2.

CPuHe2: deve ser armazenada no repositório do ITI, seguindo procedimentos já estabelecidos (CPuHe2 pode ser transformada em um certificado digital);

CSi: Chave simétrica a ser gerada pelo HSM 1, para exportação da chave privada do usuário 'i', CPrUi. CSi é utilizada para a cifração da chave privada do usuário 'i';

Algos: Algoritimo criptográfico simétrico, de sigilo, pode ser o AES ou Serpent, com modo de operação CTR e tamanho de chave 256 bits.

b) usuário deve solicitar, assinando digitalmente, uma requisição, que estará disponível no sítio dos PSCs, de portabilidade de sua chave privada, de exportação no PSC atual e de importação no PSC de destino.

c) os PSCs receberão essa requisição e autorizarão essa portabilidade com os três perfis (administrador, auditor e operador). Assim que receber a autorização do usuário, PSC 1 e PSC 2 devem iniciar os procedimentos de exportação e importação.

d) os PSCs devem estabelecer uma conexão ponta a ponta em um canal seguro de comunicação (HTTPS com dupla autenticação por certificado digital ICP-Brasil).

e) Modo Operacional:

i. procedimentos preliminares:

[a] Cada PSC gera um par de chaves ([CPuHe , CPrHe] - pública e privada) em cada um de seus HSMs. Este par tem como propósito prover portabilidade entre HSMs de quaisquer PSCs. Este par de chaves deve ser utilizado em possível exportação de chaves privadas de usuário, CprUi e também na assinatura das requisições para envelopamento utilizando a sua chave pública. Por analogia, para a chave CPuHe, 'C' significa 'Chave', Pu chave Pública, e He significa chave gerada pelo HSM para exportação de chave do usuário 'i', CPrUi. De forma similar, CPrHe e CPrUi têm significados equivalentes;

[b] CPuHe é armazenada em repositório do ITI, e CPrHe é mantida no HSM de origem;

ii. para exportação de chaves privadas dos usuários contidas no HSM 1 para o HSM 2:

[c] No PSC importa-se para o HSM 1 a chave pública do HSM 2, CPuHe2, do repositório do ITI;

[d] No HSM 1 gera-se uma chave de sessão simétrica, CSi, distinta, para cada chave privada de usuário a ser exportada;

[e] No HSM 1 cifra-se a chave simétrica, CSi, com a chave pública do HSM 2, CPuHe2, de destino, para exportação da chave do usuário 'i', CPrUi;

[f] No HSM 1 cifra-se a chave privada do usuário 'i', CPrUi, antes do procedimento de exportação de chaves, com a chave simétrica gerada, CSi, com o algoritmo de sigilo padrão AES ou Serpent, com o modo de operação CTR e tamanho de chave de 256 bits;

[g] No HSM 1 apaga-se cada chave de sessão simétrica gerada, CSi, após o procedimento de cifração do item 'f' ter sido executado;

[h] Após a cifração da chave privada do usuário 'i', CPrUi, ter sido realizada com sucesso, exporta-se essa chave, e a chave Csi cifrada, para o HSM 2;

iii. para importação de chaves privadas dos usuários contidas no HSM 1 para o HSM 2:

[i] O administrador do HSM 2, de destino, cria novo usuário e o habilita;

[j] O usuário importa do HSM 1 sua chave privada e a chave simétrica cifrada, itens 'e' e 'f';

[k] No HSM 2, de destino, recebe-se a chave privada CPrUi e a chave simétrica CSi cifradas, do usuário 'i';

[l] No HSM 2 decifra-se a chave simétrica, CSi, com a chave privada do HSM 2, CPrHe2;

[m] Em seguida, no HSM 2 decifra-se a chave privada do usuário 'i', CPrUi, que estava no HSM 1, com a chave simétrica CSi, com o algoritmo criptográfico padrão AES ou Serpent, com o modo de operação CTR e tamanho de chave de 256 bits;

[n] No HSM 2 grava-se a chave privada do usuário 'i', CPrUi, já decifrada, e importada do HSM 1;

[o] No HSM 2 destrói-se a chave simétrica CSi;

[p] O PSC 2 encaminha para o PSC 1 mensagem indicando que a importação ocorreu satisfatoriamente. Então, o HSM 1 apaga a chave privada do usuário 'i', CPrUi.

6.3 Rede

6.3.1 Poderá ser arquitetado um pool de HSM para operação, replicação e gerenciamento das chaves dos usuários finais, devendo seguir, além dos relatados nesse documento, os seguintes requisitos.

a) especificação e estabelecimento de uma comunicação segura (sessão SSL/TLS) ou equivalente entre os HSM;

b) os HSM poderão e'star em ambientes distintos desde que os mecanismos de acesso e segurança se mantenham os descritos neste documento.

6.3.2 Os PSC no âmbito da ICP-Brasil devem atender aos critérios mínimos de 99,99% de "nível de tempo de atividade" (uptime) a ser verificado por mês.

6.4. Requisitos para serviços de confiança de uso de chaves privadas

6.4.1. Definições para Interface de Serviços de Confiança

6.4.1.1 Deverá ser utilizado o protocolo TLS, definido pela RFC 5246 ou a versão atualizada, para comunicação com serviços de confiança.

6.4.1.2 Deverá ser utilizado o framework OAuth 2.0 (RFC 6749 e RFC 7636) para implementação da interface aos serviços de confiança dos PSC.

6.4.1.3 Adicionalmente, poderá ser implementada outra interface para os serviços de confiança, desde que o PSC proveja o software necessário para possibilitar ao titular o uso das suas chaves privadas de forma segura.

6.4.2. Definições para URI de base para Serviços de Confiança

6.4.2.1 A URI de base - URI-base - definirá o estilo e formato dos endereços HTTPS de serviços de confiança.

6.4.2.2 A URI de base conterá número correspondendo à versão de API definida pela ICP-Brasil.

6.4.2.3 Este documento trata da versão "v0" de API para PSC.

6.4.2.4 Exemplo de URI-base:

https://servico.provedor\_de\_servico.com.br/v0/

NOTA: O endereço*servico.provedor\_de\_servico.com.br*representa neste exemplo a porção*authority*da URI em domínio utilizado pelo PSC

6.4.2.5 As demais porções de URI presentes neste documento devem ser concatenadas à URI-base.

6.4.3. Autorização e Autenticação para Requisição de Serviços

6.4.3.1. Fluxo básico para Uso de Serviços de Confiança

6.4.3.1.1 Seguindo o fluxo de autorização estabelecido pela RFC 6749, o uso de chaves privadas em PSC deverá ser precedido de solicitação bem-sucedida, por parte de aplicações, dos seguintes serviços:

a) Código de Autorização

b) Token de Acesso

c) Assinatura

6.4.3.1.2 Quando for necessário utilizar serviço de confiança destinado somente à autenticação do titular, ou seja, sem o uso de chave privada, deverá ser precedido de solicitação bem-sucedida, por parte de aplicações, dos seguintes serviços:

a) Código de Autorização

b) Token de Acesso

c) Recuperação de Certificado

6.4.3.2. Trânsito de Fatores de Autenticação

6.4.3.2.1 As aplicações não deverão coletar fatores de autenticação do titular. Para este fim, os PSC deverão se comunicar diretamente com equipamento do titular, previamente identificado e cadastrado junto ao PSC de forma segura.

6.4.3.2.2 Excetua-se desta regra o Serviço "Autorização com Credenciais do Titular".

6.4.3.3. Autenticação de Aplicações de Assinatura

6.4.3.3.1 Para obter acesso aos serviços de confiança, os PSC deverão implementar obrigatoriamente o Serviço de Cadastro de Aplicação com Certificado ICP-Brasil para SSL.

6.4.3.3.2 O PSC poderá também implementar Serviços de Confiança Opcionais para Cadastro de Aplicação sem Certificado, Token de Acesso para Aplicações e Manutenção de Aplicações.

6.4.3.3.3 Os PSC poderão implementar, para as aplicações, outros métodos de acesso aos seus serviços, desde que os riscos associados sejam avaliados e possibilitem rastreabilidade.

6.4.4. Relação de Serviços de Confiança Disponibilizados por PSC

a) Serviços de Confiança Obrigatórios

i. Código de Autorização

ii. Token de Acesso

iii. Assinatura

iv. Cadastro de Aplicação com Certificado

v. Listagem de Certificados do Titular

vi. Localização de Titular

vii. Recuperação de Certificado

b) Serviços de Confiança Opcionais

i. Cadastro de Aplicação sem Certificado

ii. Token de Acesso para Aplicação

iii. Manutenção de Aplicação

iv. Autorização com Credenciais do Titular

6.4.5. Detalhamento de Serviços de Confiança Obrigatórios

6.4.5.1. Serviços de Autorização

6.4.5.1.1. Código de Autorização (Authorization Code Request)

a) Serviço para obter do titular a autorização de uso da sua chave privada ou autorizar autenticação sem uso da chave privada.

b) Caso o titular possua mais de um certificado, o PSC deverá apresentá-los para que o titular faça a escolha no mesmo contexto de aplicação em que transitarem os fatores de autenticação.

c) Caberá ao PSC apresentar ao titular o escopo da solicitação (vide parâmetro "scope" abaixo), permitindo a diferenciação inequívoca de solicitações que envolvam assinaturas daquelas que tratam somente de autenticação. Esta apresentação deverá ser feita durante o trânsito de fatores de autenticação.

i. Solicitação

\* Path : &lt;*URI-base>/oauth/authorize*;

\* Método HTTPS:*GET*;

\* Parâmetros da requisição: concatenados após o Path como parâmetros http query, usando o formato "*application/x-www-form-urlencoded*":

◦*response\_type*: obrigatório, valor "code";

*◦ client\_id*: obrigatório, deve conter a identificação da aplicação;

*◦ redirect\_uri:*opcional, deve ter a URI para redirecionar o usuário de volta para a aplicação de origem. A URI deve estar na lista de URI's autorizadas para a aplicação. Deve ser URL ENCODED. Se não informado, será considerada a primeira URI cadastrada para a aplicação;

*◦ state:*opcional, é retornado sem modificações para aplicação de origem;

◦ Recomendado. Um valor opaco usado pela aplicação para manter o estado entre a requisição e a resposta. O serviço de autorização incluirá este valor ao redirecionar o módulo do usuário de volta ao endereço da aplicação. Este parâmetro deverá ser usado para prevenir ataques de falsificação de requisições entre sites (cross-site request forgery).

◦*lifetime:*opcional, indica o tempo de vida desejado para o token a ser gerado. Inteiro, em segundos;

◦*scope:*opcional, se não informado, será considerado "authentication\_session". (ver lista de escopos abaixo). Possíveis valores para o parâmetro:

▪*single\_signature*: token que permite a assinatura de apenas um conteúdo (hash), sendo invalidado apos a sua utilização;

▪*multi\_signature*: token que permite a assinatura de múltiplos hashes em uma única requisição, sendo invalidado apos a sua utilização;

▪*signature\_session:*token de sessão OAuth que permite várias assinaturas em várias chamadas a API, desde que o token esteja dentro do prazo de validade ou que não tenha sido revogado pela aplicação ou pelo usuário;

▪*authentication\_session*: token de sessão OAuth para autenticação do titular, não permitindo a realização de assinaturas ou outras utilizações da chave privada.

◦*code\_challenge*: obrigatório, ver RFC 7636

◦*code\_challenge\_method*: obrigatório, valor "S256" (ver RFC 7636).

◦*login\_hint:*opcional, valor de CPF ou CNPJ a ser informado como filtro para seleção do certificado a ser utilizado.

ii. Resposta da Requisição de Código de Autorização:

a. Se o usuário autorizar a solicitação, o PSC emite um código de autorização com tempo de validade curto e retorna para aplicação cliente com uma URI de redirecionamento contendo os seguintes parâmetros no componente http query, usando o formato "application/x-www-form-urlencoded":

◦*code*: obrigatório, código de autorização gerado pelo PSC, a ser usado na solicitação do token de acesso;

◦*state*: obrigatório caso tenha sido informado na requisição, deverá conter o que foi enviado na requisição.

b. Se o usuário não autorizar a solicitação, o PSC retorna para aplicação cliente através de sua redirect\_uri os seguintes parâmetros via http query, usando o formato "application/x-www-form-urlencoded":

◦*error*: obrigatório, com o valor "user\_denied";

◦*state:*obrigatório caso tenha sido informado na requisição, deverá conter o que foi enviado na requisição.

6.4.5.1.2. Token de Acesso

Após a obtenção de código de autorização, o token de acesso deve ser solicitado com parâmetros no formato "application/x-www-form-urlencoded".

a) Solicitação

\**Path*: &lt;URI-base>/oauth/token;

\* Método HTTPS: POST;

\* Parâmetros da requisição: formato "*application/x-www-form-urlencoded*"

◦*grant\_type*: obrigatório, valor "*authorization\_code*";

◦*client\_id:*obrigatório, deve conter a identificação da aplicação;

◦*client\_secret:*obrigatório, deve conter o segredo associado à aplicação;

◦*code*: obrigatório, deve conter código de autorização retornado do Serviço Código de Autorização;

*◦ redirect\_uri:*opcional, deve ser igual ao informado no Serviço Código de Autorização;

◦*code\_verifier:*obrigatório, correspondendo a*code\_challenge*enviado na Requisição de Código de Autorização, ver RFC 7636.

Exemplo:

POST {.../oauth/token} HTTP/1.1

Host: {servidor do PSC}

Content-Type: application/x-www-form-urlencoded

grant\_type=authorization\_code

&client\_id=MyApplicationId

&client\_secret=123qwe

&code=09b30f74d40a7fece1a26cccc97746c364e61022

&redirect\_uri=https://idg.receita.fazenda.gov.br

&code\_verifier={Verifier}

b) Resposta da Requisição de*Token*de Acesso:

i. Se a requisição é valida e autorizada o PSC emite um*token*de acesso e retorna a requisição com sucesso, via HTTP*Status Code*200.

\* Parâmetros de retorno: formato "*application/json;charset=UTF-8*"

*◦ access\_token*: obrigatório, valor do token de acesso;

*◦ token\_type*: obrigatório, valor "Bearer";

◦*expires\_in:*obrigatório, valor inteiro com validade do token em segundos. Para acesso a objeto de pessoas físicas não deve ultrapassar (7 dias), sendo que para pessoas jurídicas este limite será de (30 dias);

*◦ scope*: opcional, deve ser informado se o escopo retornado for diferente do solicitado pela aplicação;

◦*authorized\_identification\_type*: obrigatório, deverá conter "CPF" ou "CNPJ"

◦*authorized\_identification*: obrigatório, valor correspondendo ao CPF ou CNPJ associado ao titular do certificado.

Exemplo:

HTTP/1.1 200 OK

Content-Type: application/json;charset=UTF-8

Cache-Control: no-store

Pragma: no-cache

{

"access\_token": "b923575f1ced0ee732ee274b2e02784040bd9606",

"expires\_in": 300,

"token\_type": "Bearer

"authorized\_identification\_type": "CPF

"authorized\_identification": 00000000001

}

&code\_verifier={Verifier}

NOTA: Não será permitido o*refresh\_token*.

ii. Se a requisição não for válida, houver falha na autenticação da aplicação cliente ou alguma outra falha, o PSC retorna a requisição com erro, via HTTP Status Code de erro correspondente à situação ocorrida via JSON com os seguintes parâmetros:

Parâmetros de retorno: formato "*application/json;charset=UTF-8*":

*\* error:*obrigatório, representa o código do erro. Possíveis valores para o parâmetro e HTTP Status Code de erro:

*◦ invalid\_request*: HTTP Status Code 400, ocorre quando algum parâmetro obrigatório não tiver sido informado ou inclui um valor de parâmetro não suportado ou algum parâmetro com valor duplicado informado ou a requisição é mal formada;

*◦ invalid\_grant*: HTTP Status Code 400, ocorre quando o código de autorização apresentado estiver inválido ou expirado ou tiver sido emitido para uma outra aplicação cliente diferente da informada ou já estiver sido utilizado em um cenário de uso único(scope single\_signature e multi\_signature). Ocorre também na validação da redirect\_uri e na validação do code\_verifier(ver RFC 7636);

*◦ invalid\_client*: HTTP Status Code 401, ocorre quando houver falha na autenticação da aplicação cliente, desde aplicação não identificada até credenciais inválidas;

*◦ unsupported\_grant\_type*: HTTP Status Code 400, ocorre quando o valor informado no parâmetro grant\_type não for suportado.

*◦ server\_error*: HTTP Status Code 500, ocorre quando houver algum erro interno não tratado pelo PSC.

*\* error\_description*: opcional, texto com informações adicionais descrevendo o erro a fim de assistir o entendimento do ocorrido;

*\* error\_uri*: opcional, URI de uma página WEB que contém informações sobre o erro ocorrido.

Exemplo:

HTTP/1.1 400 Bad Request

Content-Type: application/json;charset=UTF-8

Cache-Control: no-store

Pragma: no-cache

{

"error": "invalid\_request",

"error\_description": "Parâmetro obrigatório não informado: code",

"error\_uri":"https://psc.exemplo.com.br/docs/oauth2-error#invalid\_request"

}

6.4.5.2. Assinatura

6.4.5.2.1 Os parâmetros com conteúdo a ser assinado e assinaturas deverão conter valores em Base64.

6.4.5.2.2 As assinaturas RAW estarão em Base64.

6.4.5.2.3 Assinaturas CMS estarão em formato CMS PEM de acordo com RFC 7468: o cabeçalho e rodapé CMS são obrigatórios; quebra de linha e espaços no conteúdo são opcionais; e as aplicações devem estar preparadas para lidar com diferentes formas de espaços e quebra de linhas no conteúdo, ou com a ausência destes.

6.4.5.2.4 Se o escopo do token permitir apenas uma assinatura*(single\_signature*) e for informado mais de um conteúdo, uma mensagem de erro deve ser retornada.

6.4.5.2.5 Se o escopo for omitido ou assinalado para autenticação (*authentication\_session*) uma mensagem de erro deve ser retornada.

a) Solicitação

\**Path: &lt;URI-base>/oauth/signature*

\* Método HTTPS: POST

\* Cabeçalho:

◦*Content-type: application/json;*

◦*Accept : application/json;*

◦*Authorization: Bearer access\_token;*

\* Parâmetros: formato "application/json;charset=UTF-8" :

▪*certificate\_alias*: opcional, identificador do certificado correspondente à chave utilizada na assinatura;

▪*hashes*: conjunto com valores obrigatórios a serem assinados. Cada elemento do conjunto conterá:

\* id: identificador do conteúdo a ser assinado;

\* alias: forma legível do identificador do conteúdo;

*\* hash*: conteúdo a ser assinado;

*\* hash\_algorithm: Object Identifier*(OID) do algoritmo de*hash*. Por exemplo, para SHA256 utilize o OID 2.16.840.1.101.3.4.2.1;

\**signature\_format*: deverá conter um dos valores:

◦ "RAW",

◦ "CMS"

Exemplo

"hashes": [{

"id": "Signature request ID 1",

"alias": "Contrato de aluguel XPTO",

"hash": "hash to sign",

"hash\_algorithm": "2.16.840.1.101.3.4.2.1",

"signature\_format": "RAW"

},

{

"id": "Signature request ID 2",

"alias": "Documento do Word",

"hash": "hash to sign",

"hash\_algorithm": "2.16.840.1.101.3.4.2.1",

"signature\_format": "CMS"

}

{

"id": "Signature request ID n",

"alias": "Firefox",

"hash": "hash to sign",

"hash\_algorithm": "2.16.840.1.101.3.4.2.1",

"signature\_format" : "RAW"

}

]}

b) Resposta da Requisição de Assinatura:

O PSC retornará a requisição com sucesso, via HTTP*Status Code*200.

\* Parâmetros: formato "*application/json;charset=UTF-8*":

◦*certificate\_alias*: obrigatório, identificador do certificado correspondente à chave utilizada na assinatura;

◦*signatures*: obrigatório, conjunto com identificadores dos conteúdos assinados e valores assinados. Cada elemento do conjunto conterá:

▪ id: identificador do conteúdo assinado;

Um dos formatos abaixo:

\* caso a solicitação tenha sido feita com "*signature\_format*: RAW"

◦*raw\_signature*: valor numérico em base64 da assinatura produzida.

\* caso a solicitação tenha sido feita com "*signature\_format*: CMS"

◦ CMS*detached*(PKCS#7), contendo os seguintes atributos assinados:

*- contentType*

\- signingTime (hora do PSC)

*- messageDigest*(hash informado pela aplicação na requisição)

*- signingCertificateV2*(certificado do assinante)

NOTA: Os valores de assinatura deverão produzidos de acordo com a suíte de assinatura, se esta for informada.

Exemplo

{

"certificate\_alias": "CERTIFICADO TESTE 1:1234567889",

"signatures": [{

"id": "Signature request ID 1",

"raw\_signature": "my raw signature base64"

},

{

"id": "Signature request ID 2",

"raw\_signature": "my raw signature base64"

},

{

"id": "Signature request ID n",

"raw\_signature": "my raw signature base64"

}]}

6.4.5.3. Cadastro de Aplicação com Certificado

6.4.5.3.1 Serviço para cadastro de uma aplicação junto ao PSC, sendo que a aplicação utilizará um certificado SSL ICP-Brasil para assinar os dados enviados, substituindo neste caso o Serviço de Cadastro de Aplicação.

6.4.5.3.2 A assinatura dos dados necessários para o cadastro será realizada utilizando o formato JWT with RSA Signature, conhecido como JWS - Json Web Signature (ver RFC 7515), utilizando o algoritmo de hash SHA-256.

O header do JWS deverá conter os seguintes parâmetros:

\* alg: obrigatório, valor "RS256" representando RSA With SHA-256;

\* x5c: obrigatório, valor multivalorado contendo o certificado SSL ICP-Brasil no formato PEM.

Exemplo do Header do JWS desserializado:

{

"alg": "RS256",

"x5c": ["-----BEGIN CERTIFICATE-----ADFAASDFASDFAS. . . -----END CERTIFICATE-----"]

}

O conjunto de dados JWS deverá conter os seguintes parâmetros:

\* name: obrigatório, nome da aplicação;

*\* comments*: obrigatório, descrição da aplicação;

*\* redirect\_uris*: obrigatório, valor multivalorado contendo URI's autorizadas para redirecionamento (para serviços de requisição de autorização). Devem ser oriundas do host do certificado de equipamento apresentado, sendo vedada a utilização de fragments;

*\* host*: obrigatório, valor contendo o host único da aplicação;

*\* aud*: obrigatório, valor contendo o nome único do PSC a qual a assinatura é direcionada.

*\* email*: obrigatório, e-mail para suporte em caso de indisponibilidade, mudança de versão, entre outros.

Exemplo do*Payload*do JWS deserializado:

{

*"name": "Nome da Aplicação",*

"comments": "Descrição da Aplicação",

"host": "*www.aplicacao-exemplo.com",*

"redirect\_uris": ["https://www.aplicacao-exemplo.com/callback/certificado\_nuvem"],

"aud": "nome-unico-psc"

"email": "psc@psc.com.br"

}

a) Solicitação

\* Path: &lt;URI-base>/oauth/application\_cert

\* Método HTTPS: POST

\* Cabeçalho:

◦Accept: application/octet-stream;

◦*Body: string*contendo o JWS serializado.

b) Resposta do Serviço de Cadastro de Aplicação com Certificado

\* Parâmetros: formato "*application/json;charset=UTF-8*" :

◦*client\_id*: obrigatório, identificador único da aplicação gerado pelo PSC;

*◦ client\_secret:*obrigatório, credencial da aplicação gerada de forma aleatória pelo PSC;

6.4.5.4. Recuperação de Certificado

Serviço para recuperar certificado armazenado no PSC.

A aplicação deverá ter um Access Token válido.

a) Solicitação

\* Path :*&lt;URI-base>/oauth/certificate-discovery*;

\* Método HTTPS: GET

\* Cabecalho

◦*Content-type: application/json;*

◦*Accept: application/json;*

◦*Authorization: Bearer access\_token;*

\* Parâmetros da requisição: concatenados após o Path como parâmetros http query, utilizando o formato "application/x-form/urlencoded"

*◦ certificate\_alias*: opcional, é o identificador do certificado a ser recuperado.

b) Resposta

\* Parâmetros

*◦ status*: obrigatório, indicando "S" para resultado positivo ou "N" caso contrário;

*◦ certificates*: certificado em BASE64 recuperado;

Exemplo

{

"status": "S"

"certificates": [

{

"alias": "CERTIFICADO TESTE 1:123456789

"certificate": "-----BEGIN CERTIFICATE-----\\n{CERTIFICADO}\\n-----END CERTIFICATE-----",

}

{

"alias": "CERTIFICADO TESTE 2:123456789

"certificate": "-----BEGIN CERTIFICATE-----\\n{CERTIFICADO}\\n-----END CERTIFICATE-----",

}

]

}

6.4.5.5. Localização de Titular

Serviço para encontrar um titular mediante informação de CPF ou CNPJ.

a) Solicitação

\* Path: &lt;URI-base>/oauth/user-discovery;

\* Método HTTPS: POST;

\* Parâmetros da requisição: formato "*application/json;charset=UTF-8*":

*◦ client\_id*: obrigatório, deve conter a identificação da aplicação;

*◦ client\_secret*: obrigatório, deve conter o segredo associado à aplicação;

*◦ user\_cpf\_cnpj*: obrigatório, deve conter "CPF" para pessoa física ou "CNPJ" pessoa jurídica;

*◦ val\_cpf\_cnpj*: obrigatório, deve conter o valor do cpf ou cnpj ;

b) Resposta

\* Parâmetros

*◦ slots:*opcional, matriz com os alias de slots encontrados, composto pelos pares ordenados slot\_alias e label;

*◦ status:*obrigatório, indicando "S" para resultado positivo ou "N" caso contrário;

Exemplo

{

"slots": [

{

"slot\_alias": "12345678899-1",

"label": "A3 PESSOAL"

}

{

"slot\_alias": "12345678899-2",

"label": "A3 TRABALHO"

}

],

"status": "S"

}

6.4.6. Detalhamento de Serviços de Confiança Opcionais

6.4.6.1. Cadastro de Aplicação sem Certificado

Serviço para cadastro de uma aplicação junto ao PSC. É obrigatório para todas as aplicações que utilizarem serviços de autorização sem certificados ICP-Brasil.

a) Solicitação

\* Path :&lt;URI-base>/oauth/application

\* Método HTTPS: POST

\* Cabeçalho:

*◦ Content-type: application/json ;*

◦*Accept: application/json;*

\* Parâmetros: formato "application/json;charset=UTF-8" :

◦*name*: obrigatório, nome/descrição da aplicação;

*◦ comments*: obrigatório, observações gerais de uso da aplicação;

*◦ redirect\_uris*: obrigatório, URI's autorizadas para redirecionamento (para serviços de código de autorização).

*◦ email*: obrigatório, e-mail para suporte em caso de indisponibilidade, mudança de versão, entre outros.

Exemplo:

{

*"name": "(Nome/Descricao da aplicacao)",*

"comments": "(Observacoes gerais de uso da aplicacao)",

"redirect\_uris": [

"URI 1 pre cadastrada para redirecionamento",

"URI 2 pre cadastrada para redirecionamento",

"URI N pre cadastrada para redirecionamento"

]

"email": "psc@psc.com.br"

}

b) Resposta da Requisição de Cadastro de Aplicação

\* Parâmetros : formato"application/json;charset=UTF-8" :

◦*client\_id*: identificador da aplicação;

*◦ client\_secret*: segredo associado à aplicação;

*◦ status*: obrigatório, "success" para sucesso;

*◦ message*: obrigatório, mensagem com informações adicionais.

Exemplo:

{

*"client\_id": "(identificador da aplicacao)",*

"client\_secret": "(segredo da aplicacao)",

"status": "success",

"message": "Aplicacao cadastrada com sucesso"

}

6.4.6.2. Serviços de Manutenção de Cadastro de Aplicação

Serviço para manutenção das informações armazenadas de uma aplicação no PSC. É obrigatório para todas as aplicações que utilizarem serviços de autorização não identificadas por certificados ICP-Brasil para SSL.

6.4.6.2.1. Token de Acesso para Aplicação

Requisição para que uma aplicação obtenha token de acesso para manutenção de seu cadastro junto ao PSC.

a) Solicitação

\* Método HTTPS : POST;

\* Path:&lt;URI-base>/oauth/client\_token;

\* Parâmetros da requisição: formato "*application/x-www-form-urlencoded*":

◦*grant\_type*, obrigatório, valor "*client\_credentials*";

◦*client\_id*, obrigatório, deve conter a identificação da aplicação;

◦*client\_secret*, obrigatório para aplicações que possuem certificado digital;

Exemplo

*POST {.../oauth/client\_token} HTTP/1.1*

Host: {servidor do PSC}

Content-Type: application/x-www-form-urlencoded

client\_id=Identificacao\_aplicacao

&client\_secret=123qwe

&grant\_type=client\_credentials

b) Resposta da Requisição de Token de Acesso para Aplicações:

\* Parâmetros de retorno: formato "application/json;charset=UTF-8" :

◦ access\_token, obrigatório, valor do token de acesso;

◦ token\_type, obrigatório, valor "Bearer";

◦ expires\_in, opcional, validade do token em segundos.

Exemplo:

{

"access\_token": "b923575f1ced0ee732ee274b2e02784040bd9606",

"expires\_in": 7200,

"token\_type": "Bearer"

}

6.4.6.2.2. Manutenção de Aplicação

Serviço para atualização de informações de uma aplicação. Requer um token de acesso para aplicações, enviado no parâmetro de cabeçalho "Authorization" .

a) Solicitação

\* Path:*&lt;URI-base>/oauth/client\_maintenance*;

\* Método HTTPS: PUT;

\* Cabeçalho:

◦*Content-type: application/json ;*

◦*Accept: application/json;*

◦*Authorization: Bearer access\_token ("Bearer" concatenado com espaço e access\_token);*

\* Parâmetros: formato"application/json;charset=UTF-8" :

◦*client\_id,*obrigatório, deve conter a identificação da aplicação;

◦*client\_secret*, opcional, nova senha da aplicação;

*◦ name,*opcional, nome da aplicação;

*◦ comments*, opcional, descrição da aplicação;

◦*redirect\_uris*, opcional, URI's autorizadas para redirecionamento (para requisição de código de autorização).

*◦ email*: obrigatório, e-mail para suporte em caso de indisponibilidade, mudança de versão, entre outros.

Exemplo:

{

"client\_id": "identificador da aplicacao",

"client\_secret": "(Senha/Segredo da aplicacao)",

"name": "(Nome da aplicacao)",

"comments": "(Descrição da aplicação)",

"redirect\_uris": [

"URI 1 pre cadastrada para redirecionamento",

"URI 2 pre cadastrada para redirecionamento",

"URI N pre cadastrada para redirecionamento"

]

"email": "psc@psc.com.br"

}

b) Resposta da Requisição de Manutenção de Aplicações

\* Parâmetros de retorno: formato"application/json;charset=UTF-8" :

◦*client\_id*: obrigatório, deve conter a identificação da aplicação;

Exemplo :

{

"client\_id": "(identificador da aplicação)",

}

6.4.6.3. Autorização com Credenciais do Titular

6.4.6.3.1 Serviço para obter do titular autorização de uso da sua chave privada, com solicitação de fatores de autenticação.

6.4.6.3.2 No mínimo um fator de autenticação obtido deve ser válido para uma única solicitação de autorização (OTP- one-time password).

6.4.6.3.3 Os fatores de autenticação deverão ter seus valores concatenados e enviados no parâmetro "password".

a) Solicitação

\* Path:&lt;URI-base>/oauth/pwd\_authorize;

\* Método HTTPS: POST;

\* Cabeçalho:

*◦ Content-type: application/json;*

◦*Accept: application/json;*

\* Parâmetros: formato"application/json;charset=UTF-8" :

*◦ grant\_type*, obrigatório, valor "*password"*;

◦*client\_id*, obrigatório, identificação da aplicação;

◦*client\_secret*, opcional, sendo obrigatório apenas quando a aplicação não utilizar certificado ICP-Brasil;

◦*username*, obrigatório, identificação do usuário por meio de CPF ou CNPJ;

◦*password*, obrigatório, valor da concatenação de fatores de autenticação informadas pelo usuário;

*◦ lifetime*, opcional, valor inteiro, indica o tempo de vida desejado para o token a ser gerado em segundos. Para acesso a objeto de pessoas físicas não deve ultrapassar 7 (sete) dias, sendo que para pessoas jurídicas este limite será de 30 (trinta) dias;

*◦ scope*, opcional, se não informado será considerado "*authentication\_session*". (ver lista de escopos para Serviço de Código de Autorização).

*◦ slot\_alias*: opcional, indica o slot do usuário no qual a autenticação deve ser feita. Se não informado, o PSC decidirá em qual slot tentar a autenticação.

Exemplo:

{

"client\_id": "MyApplicationId",

"client\_secret": "123qwe",

"username": "0660457192",

"password": "123456SENHA",

"grant\_type": "password",

"scope": "single\_signature",

"lifetime": 900,

"slot\_alias": "12345678899"

}

b) Resposta da Requisição de Autorização com Credenciais do Titular

\* Parâmetros de retorno para os demais valores de "scope": formato "application/json;charset=UTF-8":

◦*access\_token*, obrigatório, valor do token de acesso;

◦*token\_type*, obrigatório, valor "*Bearer*";

◦*expires\_in*, obrigatório, valor inteiro com validade do token em segundos. Para acesso a objeto de pessoas físicas, não deve ultrapassar 7 (sete) dias, sendo que para pessoas jurídicas, esse limite será de 30 (trinta) dias;

◦*scope*, opcional, informado apenas se o escopo retornado for diferente do solicitado pela aplicação.

◦*slot\_alias*: obrigatório, indica o slot do usuário no qual a autenticação foi feita (sem middleware).

Exemplo:

{

"access\_token":

"b923575f1ced0ee732ee274b2e02784040bd9606",

"expires\_in": 300,

"token\_type": "Bearer",

"slot\_alias": "12345678899"

}

6.5 Lista de Prestador de Serviço de Confiança - LPSC

6.5.1 A Lista de Prestadores de Serviço de Confiança - LPSC contem as entidades credenciadas no âmbito da ICP-Brasil como Prestadores de Serviço de Confiança - PSC. A LPSC será publicada pela AC Raiz e atualizada no prazo máximo de 180 dias.

6.5.2 A LPSC será publicada no repositório da AC Raiz em versão textual, para leitura humana, e em XML, para processamento por máquina.

6.5.3 A autenticidade e a integridade da versão processável por máquina da lista compilada é assegurada por meio de uma assinatura digital XMLDSig suportada por um certificado digital do ITI.

6.5.4 As versões da LPSC e o certificado que assina a LPSC serão publicados no repositório da AC Raiz, disponível em:

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p> http://www.iti.gov.br/repositorio </p></td>     </tr>    </tbody>   </table>

6.5.5 A autenticidade e integridade da lista compilada devem ser verificadas pelas partes confiáveis antes de qualquer uso.

6.5.6 A LPSC é codificada em XML, em conformidade com a estrutura proposta pelo padrão ETSI TS 102 231, e contem os seguintes dados:

a) a informação do esquema (SchemeInformation), onde são apresentados os dados de identificação do emissor, o ITI, e a data da próxima atualização (NextUpdate) da lista;

b) a lista de prestadores de serviço (TrustServiceProviderList), que contem uma entrada (TrustServiceProvider) para cada PSC credenciado junto à ICP-Brasil; e

c) assinatura digital no formato XMLdSIG.

6.5.7 A LPSC conterá na URI de base que define o serviço (SchemeServiceDefinitionURI) a versão da API correspondente, podendo apresentar mais de uma instância de versão para minimizar comprometimento das aplicações integradas.

7 SERVIÇO DE ASSINATURA DIGITAL, VERIFICAÇÃO DE ASSINATURA DIGITAL

7.1. Introdução

7.1.1. Os requisitos a seguir foram baseadas nos padrões para criação e validação de assinaturas definidas nas especificações do ETSI.

7.2.Criação de Assinaturas

7.2.1. O objetivo da criação de assinaturas é para gerar uma assinatura cobrindo um documento eletrônico (texto, som, imagem, entre outros) do assinante, o certificado de assinatura ou uma referência a esse certificado, bem como os atributos da assinatura que suportam essa assinatura.

7.2.2 Um modelo funcional básico de um ambiente para a criação de assinaturas se constitui por:

a) signatário que quer criar uma assinatura em um documento eletrônico;

b) um aplicativo condutor que representa um ambiente de usuário (por exemplo, um aplicativo de negócios) que o assinante usa para acessar a funcionalidade de assinatura; e

c) um sistema de criação de assinatura, que implementa a funcionalidade de assinatura.

7.2.3. Antes de iniciar o procedimento de assinatura o sistema deve verificar a validade do certificado. Ao receber o retorno da assinatura o sistema deve bater a resposta com a chave pública.

NOTA: O envolvimento humano de um signatário nem sempre é necessário. A assinatura pode ser um processo automatizado e implementado na aplicação no ambiente do usuário.

7.3. Dispositivos para criação de assinaturas

7.3.1. São sistemas ou equipamentos configurados para implementar códigos e/ou outros mecanismos que possibilitem ativação da chave privada do signatário para a criação das assinaturas digitais.

7.3.2. Os dispositivos para criação de assinatura devem conter os certificados de assinatura ou possuírem uma referência inequívoca a eles. Devem, ainda, verificar os dados de autenticação do assinante.

7.3.3. Os equipamentos para criação de assinaturas devem possuir certificação Inmetro válida no âmbito da ICP-Brasil, conforme definido no conjunto de documentos DOC-ICP-10 [6], no documento DOC-ICP-01.01 [7], neste documento e seus complementares.

7.4. Interface da aplicação com o dispositivo de criação de assinaturas

7.4.1. A interface entre a aplicação de assinatura e o dispositivo ou equipamento de criação devem garantir que somente com a autenticação do titular do certificado, que deve ter controle exclusivo da chave privada, seja possível requerer a criação dos dados de uma assinatura digital.

7.4.2. O uso do dispositivo de criação deve exigir que o usuário insira dados específicos de autenticação do assinante. Toda informação trocada entre a aplicação e o dispositivo deve trafegar de forma criptografada.

7.4.3. Mais de um mecanismo de autenticação deve ser usado para fornecer uma garantia de autenticação suficiente.

7.4.4. Um mecanismo de autenticação do signatário deve ser de uma forma que evite ataques de representação.

NOTA 1: A natureza dos mecanismos de autenticação e os dados de autenticação do assinante são determinados pelo dispositivo de criação de assinaturas. Existem padrões para diferentes interfaces, tipos dispositivos ou equipamentos e mecanismos de autenticação.

NOTA 2: Em alguns casos, o uso de dados de autenticação do signatário será obrigatório e outros requisitos sobre a natureza dos mecanismos de autenticação e as interfaces podem ser impostas.

7.5. Suítes de Assinatura

7.5.1. Todos os algoritmos e tamanho de chaves envolvidos no cálculo de qualquer elemento da assinatura digital encontram-se definidos no documento DOC-ICP-01.01 [7].

7.6. Formatos de Assinaturas

7.6.1. A ICP-Brasil padroniza as assinaturas digitais baseadas em políticas explícitas de assinatura. As políticas de assinatura preveem os formatos CAdES, XAdES e PAdES.

7.6.2. Todos os formatos e perfis de assinatura digital no âmbito da ICP-Brasil estão definidos no conjunto de documentos DOC-ICP-15 [8] e seus complementares.

7.6.3. Os PSC devem implementar assinaturas digitais baseadas nas políticas de assinatura padronizadas e aprovadas na ICP-Brasil.

7.7 Assinatura com Carimbo do Tempo

7.7.1. Uma assinatura digital com carimbo do tempo evidencia que a assinatura digital já existia na data contida no carimbo do tempo. Os carimbos do tempo são emitidos pelas Autoridades de Carimbo do Tempo (ACT) credenciadas na ICP-Brasil e fornece data/hora como uma propriedade não assinada adicionada à uma assinatura digital.

7.7.2. A ICP-Brasil define no documento DOC-ICP-11 [9] o modelo de carimbo do tempo adotado em sua infraestrutura.

7.7.3 As politicas de assinatura regulamentadas no âmbito da ICP-Brasil definem o uso de carimbo do tempo.

7.8. Validação de Assinaturas

7.8.1. O processo de validação de uma assinatura digital deve ser realizada contra uma política explícita de assinatura digital, que consiste de um conjunto de restrições de validação, denominada Política de Assinatura, e deve gerar um relatório com indicação da situação de validação (Válida, Inválida ou Indeterminada), fornecendo os detalhes da validação técnica de cada uma das restrições aplicáveis, que podem ser relevantes para a aplicação demandante na interpretação dos resultados.

7.8.2. Na ICP-Brasil, conforme disposto no documento DOC-ICP-15 [8], uma assinatura digital é criada pelo signatário de acordo com uma política de assinatura. A validade de uma assinatura digital é avaliada pelo verificador utilizando a mesma política de assinatura usada na criação dessa assinatura digital. O item 7.6.2, acima, define os formatos e perfis regulamentados no âmbito da ICP-Brasil.

7.8.3. Os requisitos para geração e verificação de assinaturas digitais no âmbito da ICP-Brasil estão descritos no documento DOC-ICP-15.01 [10].

7.8.4. A AC Raiz gerencia as Políticas de Assinatura na ICP-Brasil, conforme definido no Anexo 3 do DOC-ICP-15.03 [11]. No processo de validação de uma assinatura digital, deve-se verificar a validade das Políticas de Assinatura por meio da Lista de Políticas de Assinatura Aprovadas (LPA), publicada no repositório da AC Raiz.

7.9. Acordo de Nível de Serviço

7.9.1. O acordo de nível de serviço para todos os serviços credenciados do PSC deverá ser de no mínimo 99,99%.

8\. CLASSIFICAÇÃO DA INFORMAÇÃO

8.1 Toda informação gerada e custodiada pelo PSC deverá ser classificada segundo o seu teor crítico e grau de confidencialidade, de acordo com sua própria Política de Classificação de Informação.

8.2 A classificação da informação no PSC deverá ser realizada independente da mídia onde se encontra armazenada ou o meio pelo qual é trafegada.

8.3 A informação poderá ser classificada em:

8.3.1 Público: Qualquer ativo de informação, de propriedade do PSC ou não, que poderá vir ao público sem maiores consequências danosas ao funcionamento normal do PSC. Poderá ser acessado por qualquer pessoa, seja interna ou externa ao PSC. Integridade da informação não é vital.

8.3.2 Pessoal: Qualquer ativo de informação relacionado à informação pessoal. Por exemplo: mensagem pessoal de correio eletrônico, arquivo pessoal, dados pessoais, entre outros.

8.3.3 Interna: Qualquer ativo de informação, de propriedade do PSC ou não, que não seja considerada pública. Ativo de informação relacionado às atividades do PSBio que é direcionada estritamente para uso interno. A divulgação não autorizada do ativo de informação poderia causar impacto à imagem do PSC. Por exemplo: código fonte de programa, cronograma de atividades, atas de reuniões, entre outros.

8.3.4 Confidencial: Qualquer ativo de informação que seja crítico para as atividades do PSC em relação ao sigilo e integridade. Qualquer material e informação recebida para ensaio, assim como qualquer resultado do ensaio (como relatório) deverá ser considerado confidencial.

NOTA: Caso o PSC seja entidade da Administração Pública Federal - APF, aplicar-se-á as disposições do Decreto nº 7.845/2012 e demais normas aplicáveis à APF, no que couber.

9 SALVAGUARDA DE ATIVOS DA INFORMAÇÃO

9.1 O PSC deverá, em sua Política de Segurança da Informação, definir como será realizada a salvaguarda de ativos de informação no formato eletrônico, também denominado backup.

9.2 A salvaguarda de ativos da informação deverá ter descrita as formas de execução dos seguintes processos:

i. procedimentos de backup;

ii. indicações de uso dos métodos de backup;

iii. tabela de temporalidade;

iv. local e restrições de armazenamento e salvaguarda em função da fase de uso;

v. tipos de mídia;

vi. controles ambientais do armazenamento;

vii. controles de segurança;

viii. teste de restauração de backup.

9.3 O PSC deverá ter política de recebimento, manipulação, depósito e descarte de materiais de terceiros.

10 GERENCIAMENTO DE RISCOS

O PSC deverá ter um processo de gerenciamento de riscos, atualizado, para prevenção contra riscos, inclusive àqueles advindos de novas tecnologias, visando a elaboração de planos de ação apropriados para proteção aos componentes ameaçados atualizado, no mínimo, anualmente.

11 PLANO DE CONTINUIDADE DE NEGÓCIOS

Um Plano de Continuidade do Negócio - PCN deverá ser implementado e testado no PSC, pelo menos uma vez por ano, para garantir a continuidade dos serviços críticos ao negócio em caso de inoperância total ou parcial de seu ambiente.

12 ANÁLISES DE REGISTRO DE EVENTOS

Todos os registros de eventos (logs, trilhas de auditorias e imagens) deverão ser analisados, no mínimo, mensalmente e um relatório deverá ser gerado com assinatura do responsável pelo PSC. Todos os registros da transação biométrica por parte do PSC deverão ser guardados por um período de 7 (sete) anos.

13 PLANO DE CAPACIDADE OPERACIONAL

13.1 Os PSC deverão elaborar e manter atualizado anualmente um Planejamento de Capacidade Operacional - PCO para determinar a capacidade de produção atual e futura com níveis de desempenho satisfatórios para responder a novas demandas, fornecendo níveis satisfatórios de serviços aos usuários, visando dimensionar os sistemas para suportar o crescimento orgânico, picos de utilização e sazonalidades.

13.2 O PCO deverá, no mínimo:

a) determinar os níveis de serviços requeridos pelos usuários;

b) analisar a capacidade de processamento de dados instalada; e

c) dimensionar a capacidade necessária de infraestrutura, hardware, comunicação de dados e link de internet para atender os níveis de serviços atuais e futuros.

14 DOCUMENTOS DA ICP-BRASIL REFERENCIADOS

14.1. Os documentos abaixo são aprovados por Resoluções do Comitê Gestor da ICP-Brasil, podendo ser alterados, quando necessário, pelo mesmo tipo de dispositivo legal. O sítio http://www.iti.gov.br publica a versão mais atualizada desses documentos e as Resoluções que os aprovaram.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Ref.</p></td>      <td rowspan="1" colspan="1"><p><em>Nome do documento</em></p></td>      <td rowspan="1" colspan="1"><p><em>Código</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p><strong>[1]</strong></p></td>      <td rowspan="1" colspan="1"><p>CRITÉRIOS E PROCEDIMENTOS PARA CREDENCIAMENTO DAS ENTIDADES INTEGRANTES DA ICP-BRASIL</p><p>Aprovado pela Resolução nº 40, de 18 de abril de 2006</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-03</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[2]</p></td>      <td rowspan="1" colspan="1"><p>REQUISITOS MÍNIMOS PARA AS POLÍTICAS DE CERTIFICADO NA ICP-BRASIL</p><p>Aprovado pela Resolução nº 07, de 12 de dezembro de 2001</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-04</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[3]</p></td>      <td rowspan="1" colspan="1"><p>CRITÉRIOS E PROCEDIMENTOS PARA REALIZAÇÃO DE AUDITORIAS NAS ENTIDADES INTEGRANTES DA ICP-BRASIL</p><p>Aprovado pela Resolução nº 24, de 29 de agosto de 2003</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-08</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[4]</p></td>      <td rowspan="1" colspan="1"><p>CRITÉRIOS E PROCEDIMENTOS PARA FISCALIZAÇÃO DAS ENTIDADES INTEGRANTES DA ICP-BRASIL</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-09</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[5]</p></td>      <td rowspan="1" colspan="1"><p>POLÍTICA DE SEGURANÇA DA ICP-BRASIL</p><p>Aprovado pela Resolução nº 02, de 25 de setembro de 2001</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-02</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[6]</p></td>      <td rowspan="1" colspan="1"><p>REGULAMENTO PARA HOMOLOGAÇÃO DE SISTEMAS E EQUIPAMENTOS DE CERTIFICAÇÃO DIGITAL NO ÂMBITO DA ICP-BRASIL</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-10</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[8]</p></td>      <td rowspan="1" colspan="1"><p>VISÃO GERAL SOBRE ASSINATURAS DIGITAIS NA ICP-BRASIL</p><p>Aprovado pela Resolução nº 62, de 09 de janeiro de 2009</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-15</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[9]</p></td>      <td rowspan="1" colspan="1"><p>VISÃO GERAL DO SISTEMA DE CARIMBOS DO TEMPO NA ICP-BRASIL</p><p>Aprovado pela Resolução n° 58, de 28 de novembro de 2008</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-11</p></td>     </tr>    </tbody>   </table>

14.2. Os documentos abaixo são aprovados por Instrução Normativa da AC Raiz, podendo ser alterados, quando necessário, pelo mesmo tipo de dispositivo legal. O sítio http://www.iti.gov.br publica a versão mais atualizada desses documentos e as Instruções Normativas que os aprovaram.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p><em>Ref.</em></p></td>      <td rowspan="1" colspan="1"><p><em>Nome do documento</em></p></td>      <td rowspan="1" colspan="1"><p><em>Código</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p><strong>[7]</strong></p></td>      <td rowspan="1" colspan="1"><p>PADRÕES E ALGORITMOS CRIPTOGRÁFICOS DA ICP-BRASIL</p><p>Aprovado pela Instrução Normativa nº 04, de 18 de maio de 2006</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-01.01</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[10]</p></td>      <td rowspan="1" colspan="1"><p>REQUISITOS PARA GERAÇÃO E VERIFICAÇÃO DE ASSINATURAS DIGITAIS NA ICP-BRASIL</p><p>Aprovado pela Instrução Normativa nº 01, de 09 de janeiro de 2009</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-15.01</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[11]</p></td>      <td rowspan="1" colspan="1"><p>REQUISITOS DAS POLÍTICAS DE ASSINATURA DIGITAL NA ICP-BRASIL</p><p>Aprovado pela Instrução Normativa nº 03, de 09 de janeiro de 2009</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-15.03</p></td>     </tr>    </tbody>   </table>

15 REFERÊNCIAS

BRASIL, Decreto nº 7.845, de 14 de novembro de 2012. Regulamenta procedimentos para credenciamento de segurança e tratamento de informação classificada em qualquer grau de sigilo, e dispõe sobre o Núcleo de Segurança e Credenciamento.

ETSI TS 102 231*- Electronic Signatures and Infrastructures (ESI); Provision of harmonized Trust-service status information; V3.1.2 (2009-12).*

RFC 4226, IETF - HOTP: An HMAC-Based One-Time Password Algorithm, december 2005.

RFC 5246, IETF - The Transport Layer Security (TLS) Protocol Version 1.2, august 2008.

RFC 6238, IETF - TOTP: Time-Based One-Time Password Algorithm, may 2011.

RFC 6287, IETF - OCRA: OATH Challenge-Response Algorithm, june 2011.

RFC 6749, IETF - The Oauth 2.0 Authorization Framework, october 2012.

RFC 7468, IETF - Textual Encodings of PKIX, PKCS, and CMS Structures, april 2015.

RFC 7515, IETF - JSON Web Signature (JWS), may 2015.

RFC 7636, IETF - Proof Key for Code Exchange by Oauth Public Clients, september 2015.
