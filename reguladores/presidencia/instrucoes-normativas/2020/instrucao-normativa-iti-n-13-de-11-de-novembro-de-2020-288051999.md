---
titulo: "INSTRUÇÃO NORMATIVA ITI Nº 13, DE 11 DE NOVEMBRO DE 2020"
orgao: "Presidência da República/Casa Civil/Instituto Nacional de Tecnologia da Informação"
tipo: "Instrução Normativa"
numero: "13"
data: 2020-11-11
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 13/11/2020, seção 1, p. 10"
data_publicacao: 2020-11-13
edicao: "217"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-iti-n-13-de-11-de-novembro-de-2020-288051999"
sha256_html_fonte: a2bc082f9a63824350315406f9ef57c0270d0173db35ff99f52d1899baf49cbf
baixado_em: 2026-10-21
---
# INSTRUÇÃO NORMATIVA ITI Nº 13, DE 11 DE NOVEMBRO DE 2020

**INSTRUÇÃO NORMATIVA ITI Nº 13, DE 11 DE NOVEMBRO DE 2020**

Aprova a versão revisada e consolidada do documento Requisitos Mínimos de Segurança PSBio na ICP-Brasil DOC-ICP-03.02

**O DIRETOR-PRESIDENTE DO INSTITUTO NACIONAL DE TECNOLOGIA DA INFORMAÇÃO**, no uso das atribuições que lhe foram conferidas pelo inciso VI do art. 9º do anexo I do Decreto nº 8.985, de 8 de fevereiro de 2017, pelo art. 1º da Resolução nº 33 do Comitê Gestor da ICP-Brasil, de 21 de outubro de 2004, e pelo art. 2º da Resolução nº 163 do Comitê Gestor da ICP-Brasil, de 17 de abril de 2020,

CONSIDERANDO a determinação estabelecida pelo Decreto nº 10.139, de 28 de novembro de 2019, para revisão e consolidação dos atos normativos inferiores a decreto, editados por órgãos e entidades da administração pública federal direta, autárquica e fundacional, resolve:

**Art. 1º** Esta Instrução Normativa aprova a versão revisada e consolidada do documento Requisitos Mínimos de Segurança PSBio na ICP-Brasil DOC-ICP-03.02.

**Art. 2º** Fica aprovada a versão 2.0 do documento DOC-ICP-03.02 - Requisitos Mínimos de Segurança PSBio na ICP-Brasil.

**Art. 3º** Esta Instrução Normativa entra em vigor em 1º de dezembro de 2020.

CARLOS ROBERTO FORTNER

## ANEXO

REQUISITOS MÍNIMOS DE SEGURANÇA

PSBIO NA ICP-BRASIL

DOC-ICP-03.02

Versão 2.0

11 de novembro de 2020

**1 CONTROLE DE ALTERAÇÕES**

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução ou IN que aprovou a alteração</p></td>      <td rowspan="1" colspan="1"><p>Item alterado</p></td>      <td rowspan="1" colspan="1"><p>Descrição da alteração</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IN ITI nº 13, de 11.11.2020</p><p>Versão 2.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Revisão e consolidação, conforme Decreto nº 10.139, de 28 de novembro de 2019.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa n° 07, de 29.05.2020</p><p>Versão 1.3</p></td>      <td rowspan="1" colspan="1"><p>4.g e 11</p></td>      <td rowspan="1" colspan="1"><p>Altera o tempo de armazenamento dos logs, trilhas de auditorias e imagens.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa n° 01, de 31.03.2016</p><p>Versão 1.2</p></td>      <td rowspan="1" colspan="1"><p>3.1.1.2,</p><p>3.1.1.3 (novo) e 6</p></td>      <td rowspan="1" colspan="1"><p>Atualização dos requisitos dos PSBio.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa n° 08, de 10.12.2015</p><p>Versão 1.1</p></td>      <td rowspan="1" colspan="1"><p>Item 4, "g"</p></td>      <td rowspan="1" colspan="1"><p>Inclui a previsão de backup para informações como log, trilhas de auditoria.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução nº 114, de 30.09.2015</p><p>Versão 1.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Aprova a versão 1.0 do Documento Requisitos mínimos de segurança PSBIO.</p></td>     </tr>    </tbody>   </table>

**1 LISTA DE SIGLAS E ACRÔNIMOS**

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>SIGLA</p></td>      <td rowspan="1" colspan="1"><p>DESCRIÇÃO</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AC Raiz</p></td>      <td rowspan="1" colspan="1"><p>Autoridade Certificadora Raiz da ICP-BRASIL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>APF</p></td>      <td rowspan="1" colspan="1"><p>Administração Pública Federal</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>DOC-ICP</p></td>      <td rowspan="1" colspan="1"><p>Documentos Principais da ICP-BRASIL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ICP-Brasil</p></td>      <td rowspan="1" colspan="1"><p>Infraestrutura de Chaves Públicas Brasileira</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PCN</p></td>      <td rowspan="1" colspan="1"><p>Plano de Continuidade do Negócio</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>PSBio</p></td>      <td rowspan="1" colspan="1"><p>Prestador de Serviço Biométrico credenciado na ICP-BRASIL</p></td>     </tr>    </tbody>   </table>

**11 DISPOSIÇÕES GERAIS**

1.1 Este documento tem por finalidade regulamentar os requisitos mínimos de segurança e os procedimentos a serem adotados pelo Prestador de Serviços Biométricos - PSBio da ICP-Brasil.

1.2 Suplementa, para essas entidades, os regulamentos contidos no documento DOC-ICP-05.02 [2], tomando como base também a Política de Segurança da ICP-Brasil - DOC-ICP-02 [1].

1.3 Os requisitos abaixo informados deverão ser apresentados quando do credenciamento do PSBio e mantidos atualizados durante seu funcionamento enquanto a entidade estiver credenciada na ICP-Brasil.

1.4 O PSBio deverá ter uma Política de Segurança da Informação composta por diretrizes, normas e procedimentos que descrevem os controles de segurança que devem ser seguidos em suas dependências e atividades, em consonância com o DOC-ICP-02 [1].

1.5 Deverá existir um exemplar da Política de Segurança da Informação no formato impresso disponível para consulta no nível 1 de segurança do PSBio.

1.6 A Política de Segurança da Informação deverá ser seguida por todo pessoal envolvido nos projetos coordenados pelo PSBio, do seu próprio quadro ou contratado.

1.7 Este documento define normas de segurança que deverão ser aplicadas nas áreas internas ao PSBio, assim como no trânsito de informações e materiais com entidades externas.

1.8 A seguir são informados os requisitos que devem ser observados quanto a segurança de pessoal, segurança física, segurança lógica, segurança de rede, classificação da informação, salvaguarda de ativos da informação, gerenciamento de riscos, plano de continuidade de negócios e análise de registros de eventos.

**2. SEGURANÇA PESSOAL**

2.1 O PSBio deverá ter uma Política de Gestão de Pessoas que disponha sobre os processos de contratação, demissão, descrição de cargos, avaliação de desempenho e capacitação.

2.2 A comprovação da capacidade técnica do pessoal envolvido nos serviços prestados pelo PSBio deverá estar à disposição para eventuais auditorias e fiscalizações.

2.3 Todo pessoal envolvido nos projetos coordenados pelo PSBio, do próprio quadro ou contratado, deverá assinar um termo, com garantias jurídicas, que garanta o sigilo das informações internas e de terceiros, mesmo após a demissão ou o término do contrato.

2.4 O termo de sigilo da informação deverá conter cláusula explícita de responsabilização nos casos de quebra de regras ou regulamentos da ICP-Brasil.

2.5 Aplicar-se-á o termo de sigilo de informações a quaisquer outras entidades que porventura tenham acesso às informações internas e de terceiros originárias dos projetos coordenados pelo PSBio.

2.6 O PSBio deverá ter procedimentos formais de apuração e responsabilização em caso de descumprimento das regras estabelecidas pelas suas políticas ou pelas normas da ICP-Brasil.

2.7 O pessoal do PSBio, e contratados, deverão possuir um dossiê contendo os seguintes documentos:

a) contrato de trabalho ou cópia das páginas da carteira de trabalho onde conste o registro da contratação, termo de posse de servidor ou comprovante de situação funcional;

b) comprovante da verificação de antecedentes criminais;

c) comprovante da verificação de situação de crédito;

d) comprovante da verificação de histórico de empregos anteriores;

e) comprovação de residência;

f) comprovação de capacidade técnica;

g) resultado da entrevista inicial, com a assinatura do entrevistador;

h) declaração em que afirma conhecer as suas atribuições e em que assume o dever de cumprir as regras aplicáveis da ICP-Brasil;

i) termo de sigilo.

2.8 Não serão admitidos estagiários no exercício fim das atividades do PSBio.

2.9 Quando da demissão, o referido dossiê deverá possuir os seguintes documentos:

a) evidências de exclusão dos acessos físico e lógico nos ambientes do PSBio;

b) declaração assinada pelo empregado ou servidor de que não possui pendências, conforme previsto no item sobre processo de liberação do DOC-ICP-02 [1].

**43 SEGURANÇA FISÍCA**

3.1. Disposições Gerais de Segurança Física

3.1.1. Níveis de acesso

3.1.1.1. São definidos pelo menos 4 (quatro) níveis de acesso físico aos diversos ambientes do PSBio.

3.1.1.1.1. O primeiro nível - ou nível 1 - deverá situar-se após a primeira barreira de acesso às instalações do PSBio. O ambiente de nível 1 dos PSBio da ICP-Brasil desempenha a função de interface com cliente ou fornecedores que necessita comparecer ao PSBio.

3.1.1.1.2. O segundo nível - ou nível 2 - será interno ao primeiro e deverá requerer a identificação individual das pessoas que nele entram. Esse será o nível mínimo de segurança requerido para a execução de qualquer processo operacional ou administrativo do PSBio. A passagem do primeiro para o segundo nível deverá exigir identificação por meio eletrônico e o uso de crachá.

a) o ambiente de nível 2 deverá ser separado do nível 1 por paredes divisórias de escritório, alvenaria ou pré-moldadas de gesso acartonado. Não deverá haver janelas ou outro tipo qualquer de abertura para o exterior, exceto a porta de acesso;

b) o acesso a este nível deverá ser permitido apenas a pessoas que trabalhem diretamente com as atividades de serviços biométricos ou ao pessoal responsável pela manutenção de sistemas e equipamentos do PSBio, como administradores de rede e técnicos de suporte de informática. Demais funcionários do PSBio ou do possível ambiente que esta compartilhe não deverão acessar este nível;

c) preferentemente, nobreaks, geradores e outros componentes da infraestrutura física deverão estar abrigados neste nível, para evitar acessos ao ambiente de nível 3 por parte de prestadores de serviços de manutenção;

d) excetuados os casos previstos em lei, o porte de armas não será admitido nas instalações do PSBio, a partir do nível 2. A partir desse nível, equipamentos de gravação, fotografia, vídeo, som ou similares, bem como computadores portáteis, terão sua entrada controlada e somente poderão ser utilizados mediante autorização formal e sob supervisão.

3.1.1.1.3. O terceiro nível - ou nível 3 - deverá situar-se dentro do segundo e será o primeiro nível a abrigar material e atividades sensíveis da operação do PSBio. Qualquer atividade relativa à Transação Biométrica Digital deverá ser realizada nesse nível. Somente pessoas autorizadas poderão permanecer nesse nível.

a) no terceiro nível deverão ser controladas tanto as entradas quanto as saídas de cada pessoa autorizada. Dois tipos de mecanismos de controle deverão ser requeridos para a entrada nesse nível: algum tipo de identificação individual, como cartão eletrônico, e identificação biométrica ou digitação de senha;

b) as paredes que delimitam o ambiente de nível 3 deverão ser de alvenaria ou material de resistência equivalente ou superior. Não deverá haver janelas ou outro tipo qualquer de abertura para o exterior, exceto a porta de acesso;

c) caso o ambiente de Nível 3 possua forro ou piso falsos, deverão ser adotados recursos para impedir o acesso ao ambiente por meio desses, tais como grades de ferro estendendo-se das paredes até as lajes de concreto superior e inferior;

d) deve haver uma porta única de acesso ao ambiente de nível 3, que abra somente depois que o funcionário tenha se autenticado eletronicamente no sistema de controle de acesso. A porta deverá ser dotada de dobradiças que permitam a abertura para o lado externo, de forma a facilitar a saída e dificultar a entrada no ambiente, bem como de mecanismo para fechamento automático, para evitar que permaneça aberta mais tempo do que o necessário;

e) poderão existir no PSBio vários ambientes de nível 3 para abrigar e segregar, quando for o caso:

i. equipamentos de produção e cofre de armazenamento;

ii. equipamentos de rede e infraestrutura (firewall, roteadores, switches e servidores).

NOTA 1: Caso o PSBio se situe dentro de um data center, com requisitos de segurança julgados adequados pela AC Raiz, poderá ser dispensada a existência de um ambiente de nível 3 específico para a PSBio.

3.1.1.1.4. O terceiro nível avançado - ou nível 3.1 -, no interior ao ambiente de nível 3, deverá compreender pelo menos um gabinete reforçado trancado, que abrigará o banco com a base de dados biométrico da ICP-Brasil:

a) para garantir a segurança do material armazenado, os gabinetes deverão obedecer às seguintes especificações mínimas:

i. ser feitos em aço ou material de resistência equivalente;

ii. possuir tranca com chave.

3.1.1.2. Todos os servidores e elementos de infraestrutura e proteção do segmento de rede, tais como roteadores, hubs, switches e firewalls devem:

a) operar em ambiente com segurança equivalente, no mínimo, ao nível 3 citado neste documento; e

b) possuir acesso lógico restrito por meio de sistema de autenticação e autorização de acesso.

3.1.1.3. Os PSBio devem ainda atender aos seguintes requisitos:

a) o ambiente físico do PSBio deverá conter dispositivos que autentiquem e registrem o acesso de pessoas informando data e hora desses acessos;

b) o PSBio deverá conter imagens que garantam a identificação de pessoas quando do acesso físico em qualquer parte de seu ambiente;

c) é mandatório o sincronismo de data e hora entre os mecanismos de segurança física garantindo a trilha de auditoria entre dispositivos de controle de acesso físico e de imagem;

d) todos que transitam no ambiente físico do PSBio deverão portar crachás de identificação, inclusive os visitantes;

e) só é permitido o trânsito de material de terceiros pelos ambientes físicos do PSBio mediante registro, garantindo a trilha de auditoria com informações de onde o material passou, a data e hora que ocorreu o trânsito e quem foi o responsável por sua manipulação;

f) o PSBio deverá conter dispositivos de prevenção e controle de incêndios, temperatura, umidade, iluminação e oscilação na corrente elétrica em todo seu ambiente físico;

g) todo material crítico inservível, descartável ou não mais utilizável deverá ter tratamento especial de destruição, garantindo o sigilo das informações lá contidas. O equipamento enviado para manutenção deverá ter seus dados apagados, de forma irreversível, antes de ser retirado do ambiente físico do PSBio;

h) os computadores pessoais, servidores e dispositivos de rede, e seus respectivos softwares, deverão estar inventariados com informações que permitam a identificação inequívoca;

i) em caso de inoperância dos sistemas automáticos, o controle de acesso físico deverá ser realizado provisoriamente por meio de um livro de registro onde constará quem acessou, a data, hora e o motivo do acesso;

j) deverão ser providenciados mecanismos para garantir a continuidade do fornecimento de energia nas áreas críticas, mantendo os ativos críticos de informação em funcionamento até que todos os processos e dados sejam assegurados caso o fornecimento de emergência se esgote.

**4 SEGURANÇA LÓGICA**

4.1 O acesso lógico ao ambiente computacional do PSBio se dará no mínimo mediante usuário individual e senha, que deverá ser trocada periodicamente;

4.2 Todos os equipamentos do parque computacional deverão ter controle de forma a permitir somente o acesso lógico a pessoas autorizadas;

4.3 Os equipamentos deverão ter mecanismos de bloqueio de sessão inativa;

4.4 O PSBio deverá ter explícita a política de cadastro, suspensão e remoção de usuários em seu ambiente computacional. Os usuários deverão estar cadastrados em perfis de acesso que permitam privilégio mínimo para realização de suas atividades;

4.5 Os usuários especiais (a exemplo do root e do administrador) de sistemas operacionais, de banco de dados e de aplicações em geral devem ter suas senhas segregadas de forma que o acesso lógico a esses ambientes se dê por, pelo menos, duas pessoas autorizadas;

4.6 Todo equipamento do PSBio deverá ter log ativo e seu horário sincronizado com uma fonte confiável de tempo;

4.7 As informações como log, trilhas de auditoria (das transações e coletas biométricas), registros de acesso (físico e lógico) e imagens deverão ter cópia de segurança cujo armazenamento será de 7 anos;

4.8 Os softwares dos sistemas operacionais, os antivírus e aplicativos de segurança devem ser mantidos atualizados.

**5 SEGURANÇA DE REDE**

5.1 O tráfego das informações no ambiente de rede deverá ser protegido contra danos ou perdas, bem como acesso, uso ou exposição indevidos;

5.2 Não poderão ser admitidos acessos do mundo externo a rede interna do PSBio. As tentativas de acessos externos deverão ser inibidas e monitoradas por meio de aplicativos que criem barreiras e filtros de acesso, assim como mecanismos de detecção de intrusão;

5.3 Deverão ser aplicados testes de segurança na rede interna e externa com aplicativos especializados com periodicidade de, no mínimo, uma vez a cada 3 (três) meses. Os testes na rede deverão ser documentados e as vulnerabilidades detectadas corrigidas.

**6 REQUISITOS BIOMÉTRICOS**

Os PSBios deverão ser entidades com capacidade técnica para realizar a identificação (1:N) biométrica, tornando um registro/requerente único em um ou mais bancos/sistemas de dados biométrico para toda ICP-Brasil, e a verificação (1:1) biométrica do requerente de um certificado digital a comparação de uma biometria, que possua característica perene e unívoca, de acordo com os padrões internacionais de uso, como, por exemplo, impressão digital, face, íris, voz, coletada no processo de emissão do certificado digital com outra que está armazenada, com o mesmo registro/indexador (IDN) deste requerente, em um ou mais bancos/sistemas de dados biométrico da ICP-Brasil, como estabelecido no DOC-ICP-05.03 [3], bem como os descritos neste documento.

**7 CLASSIFICAÇÃO DA INFORMAÇÃO**

7.1 Toda informação gerada e custodiada pelo PSBio deverá ser classificada segundo o seu teor crítico e grau de confidencialidade, de acordo com sua própria Política de Classificação de Informação;

7.2 A classificação da informação no PSBio deverá ser realizada independente da mídia onde se encontra armazenada ou o meio pelo qual é trafegada;

7.3 A informação poderá ser classificada em:

a) Público: Qualquer ativo de informação, de propriedade do PSBio ou não, que poderá vir ao público sem maiores consequências danosas ao funcionamento normal do PSBio. Poderá ser acessado por qualquer pessoa, seja interna ou externa ao PSBio. Integridade da informação não é vital;

b) Pessoal: Qualquer ativo de informação relacionado à informação pessoal. Por exemplo: mensagem pessoal de correio eletrônico, arquivo pessoal, dados pessoais, etc;

c) Interna: Qualquer ativo de informação, de propriedade do PSBio ou não, que não seja considerada pública. Ativo de informação relacionado às atividades do PSBio que é direcionada estritamente para uso interno. A divulgação não autorizada do ativo de informação poderia causar impacto à imagem do PSBio. Por exemplo: código fonte de programa, cronograma de atividades, atas de reuniões, etc;

d) Confidencial: Qualquer ativo de informação que seja crítico para as atividades do PSBio em relação ao sigilo e integridade. Qualquer material e informação recebida para ensaio, assim como qualquer resultado do ensaio (como relatório) deverá ser considerado confidencial.

NOTA 2: Caso o PSBio seja entidade da Administração Pública Federal - APF, aplicar-se-á as disposições do Decreto nº 7.845/2012 e demais normas aplicáveis à APF, no que couber.

**8 SALVAGUARDA DE ATIVOS DA INFORMAÇÃO**

8.1 O PSBio deverá, em sua Política de Segurança da Informação, definir como será realizada a salvaguarda de ativos de informação no formato eletrônico, também denominado backup.

8.2 A salvaguarda de ativos da informação deverá ter descrita as formas de execução dos seguintes processos:

a) procedimentos de backup;

b) indicações de uso dos métodos de backup;

c) tabela de temporalidade;

d) local e restrições de armazenamento e salvaguarda em função da fase de uso;

e) tipos de mídia;

f) controles ambientais do armazenamento;

g) controles de segurança;

h) teste de restauração de backup.

8.3 O PSBio deverá ter política de recebimento, manipulação, depósito e descarte de materiais de terceiros.

**9 GERENCIAMENTO DE RISCOS**

O PSBio deverá ter um processo de gerenciamento de riscos, atualizado, para prevenção contra riscos, inclusive àqueles advindos de novas tecnologias, visando a elaboração de planos de ação apropriados para proteção aos componentes ameaçados atualizado, no mínimo, anualmente.

**10 PLANO DE CONTINUIDADE DE NEGÓCIOS**

Um Plano de Continuidade do Negócio - PCN deverá ser implementado e testado no PSBio, pelo menos uma vez por ano, para garantir a continuidade dos serviços críticos ao negócio em caso de inoperância total ou parcial de seu ambiente.

**11 ANÁLISES DE REGISTRO DE EVENTOS**

Todos os registros de eventos (logs, trilhas de auditorias e imagens) deverão ser analisados, no mínimo, mensalmente e um relatório deverá ser gerado com assinatura do responsável pelo PSBio. Todos os registros da transação biométrica por parte do PSBio deverão ser guardados por um período de 7 (sete) anos.

**12 DOCUMENTOS REFERENCIADOS**

12.1 Os documentos abaixo são aprovados por Resoluções do Comitê Gestor da ICP-Brasil, podendo ser alterados, quando necessário, pelo mesmo tipo de dispositivo legal. O sítio http://www.iti.gov.br publica a versão mais atualizada desses documentos e as Resoluções que os aprovaram.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p><em>Ref.</em></p></td>      <td rowspan="1" colspan="1"><p><em>Nome do documento</em></p></td>      <td rowspan="1" colspan="1"><p><em>Código</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[1]</p></td>      <td rowspan="1" colspan="1"><p>POLÍTICA DE SEGURANÇA DA ICP-BRASIL</p><p>Aprovado pela Resolução nº 02, de 25 de setembro de 2001</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-02</p></td>     </tr>    </tbody>   </table>

12.2 Os documentos abaixo são aprovados por Instrução Normativa da AC Raiz, podendo ser alterados, quando necessário, pelo mesmo tipo de dispositivo legal. O sítio https://www.gov.br/iti/pt-br publica a versão mais atualizada desses documentos e as Instruções Normativas que os aprovaram.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p><em>Ref.</em></p></td>      <td rowspan="1" colspan="1"><p><em>Nome do documento</em></p></td>      <td rowspan="1" colspan="1"><p><em>Código</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[2]</p></td>      <td rowspan="1" colspan="1"><p>PROCEDIMENTOS PARA IDENTIFICAÇÃO DO REQUERENTE E COMUNICAÇÃO DE IRREGULARIDADES NO PROCESSO DE EMISSÃO DE UM CERTIFICADO DIGITAL ICP-BRASIL</p><p>Aprovado pela Instrução Normativa nº 02, de 23.06.2015</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-05.02</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[3]</p></td>      <td rowspan="1" colspan="1"><p>PROCEDIMENTOS PARA IDENTIFICAÇÃO BIOMÉTRICA NA ICP-BRASIL</p><p>Aprovado pela Instrução Resolução nº 114, de 30.09.2015</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-05.03</p></td>     </tr>    </tbody>   </table>

**INSTRUÇÃO NORMATIVA ITI Nº 14, DE 11 DE NOVEMBRO DE 2020**

Aprova a versão revisada e consolidada do documento Perfil do alvará do carimbo do tempo da ICP-Brasil DOC-ICP-12.01.

**O DIRETOR-PRESIDENTE DO INSTITUTO NACIONAL DE TECNOLOGIA DA INFORMAÇÃO**, no uso das atribuições que lhe foram conferidas pelo inciso VI do art. 9º do anexo I do Decreto nº 8.985, de 8 de fevereiro de 2017, pelo art. 1º da Resolução nº 33 do Comitê Gestor da ICP-Brasil, de 21 de outubro de 2004, e pelo art. 2º da Resolução nº 163 do Comitê Gestor da ICP-Brasil, de 17 de abril de 2020,

**CONSIDERANDO**a determinação estabelecida pelo Decreto nº 10.139, de 28 de novembro de 2019, para revisão e consolidação dos atos normativos inferiores a decreto, editados por órgãos e entidades da administração pública federal direta, autárquica e fundacional, resolve:

**Art. 1º** Esta Instrução Normativa aprova a versão revisada e consolidada do documento Perfil do alvará do carimbo do tempo da ICP-Brasil DOC-ICP-12.01.

**Art. 2º** Fica aprovada a versão 2.0 do documento DOC-ICP-12.01 - Perfil do alvará do carimbo do tempo da ICP-Brasil, anexa a esta Instrução Normativa.

**Art. 3º** Esta Instrução Normativa entra em vigor em 1° de dezembro de 2020.

CARLOS ROBERTO FORTNER

## ANEXO

PERFIL DO ALVARÁ DO CARIMBO DO TEMPO DA ICP-BRASIL

DOC-ICP-12.01

Versão 2.0

11 de novembro de 2020

**5 CONTROLE DE ALTERAÇÕES**

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução ou IN que aprovou a alteração</p></td>      <td rowspan="1" colspan="1"><p>Item alterado</p></td>      <td rowspan="1" colspan="1"><p>Descrição da alteração</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Instrução Normativa ITI nº 14, de 11/11/2020</p><p>Versão 2.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Revisão e consolidação, conforme Decreto nº 10.139, de 28 de novembro de 2019.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução nº 155, de</p><p>03/12/2019</p><p>Versão 1.0</p></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Aprova a versão 1.0 do Documento Perfil do Alvará do Carimbo do Tempo da ICP-Brasil.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>     </tr>    </tbody>   </table>

**6 LISTA DE SIGLAS E ACRÔNIMOS**

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>SIGLA</p></td>      <td rowspan="1" colspan="1"><p>DESCRIÇÃO</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>AC</p></td>      <td rowspan="1" colspan="1"><p>Autoridade Certificadora</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ASN.1</p></td>      <td rowspan="1" colspan="1"><p>Abstract Syntax Notation One</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ICP-Brasil</p></td>      <td rowspan="1" colspan="1"><p>Infraestrutura de Chaves Públicas Brasileira</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>MCT</p></td>      <td rowspan="1" colspan="1"><p>Manual de Conduta Técnica</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>MSC</p></td>      <td rowspan="1" colspan="1"><p>Módulo de Segurança Criptográfica</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>RFC</p></td>      <td rowspan="1" colspan="1"><p>Request For Comments</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>SAS</p></td>      <td rowspan="1" colspan="1"><p>Sistemas de Auditoria e Sincronismo</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>XML</p></td>      <td rowspan="1" colspan="1"><p>Extensible Markup Language</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>     </tr>    </tbody>   </table>

**71 DEFINIÇÃO**

1.1 No contexto da infraestrutura de carimbo do tempo da ICP-Brasil um certificado de atributo digital também é conhecido como Alvará. Um alvará consiste de um objeto de dados que contém uma estrutura de campos que segue o formato definido pela RFC 5755, podendo ser codificado em formato ASN.1 ou XML.

1.2 Todo Alvará, antes de sua emissão, deve ser assinado digitalmente utilizando certificados digitais de equipamento por meio do MSC contido no SAS.

2\. LOCAL ADMITIDO

2.1 O alvará, como limitador de autorização, tem seu uso admitido no TSTInfo, conforme previsto no MCT 10 da ICP-Brasil [3], e no signingCertificate, admitido pelas RFC 5035 e RFC 2634.

2.2 Quando presente no signingCertificate a validação do alvará deverá seguir, no mínimo, os procedimentos previstos no item 3.1.1. No TSTInfo essa validação não é obrigatória, sendo uma decisão do verificador realizá-la.

**83 IDENTIFICAÇÃO E VALIDAÇÃO DO ALVARÁ**

3.1 Os procedimentos descritos a seguir tem como objetivo identificar e validar o alvará quando estiver presente no signingCertificate, podendo ser utilizado para validação no TSTInfo.

3.1.1 Para identificar se um certificado de atributo, presente em um carimbo do tempo, é um alvará é necessário averiguar os seguintes fatores:

a) O certificado de atributo tem o formato especificado no Manual de Condutas Técnicas (MCT) 10, Volume I [3];

b) Checar a integridade da sua assinatura;

c) O emissor deve ser um certificado considerado confiável para emissão de alvarás na ICP-Brasil;

d) O alvará deverá estar válido no período do carimbo do tempo, conforme DOC-ICP 12 [1], item 9.6.1.2.c e atender ao procedimento de validação definido.

3.1.2 Recomenda-se, ainda, a validação completa do alvará, que pode ser feita acrescentando os itens abaixo, além daqueles descritos no item sobre validação de uma assinatura digital ICP-Brasil com referência de tempo, constante no DOC-ICP 15.01 [2], no processo de validação.

a) O certificado do emissor do alvará não deve ser uma AC, ou seja, o valor de sua extensão basicConstraints.cA deve ser falso;

b) O certificado do emissor precisa ter o bit de assinatura digital configurado como verdadeiro, ou 1, em sua extensão keyUsage;

c) Validar o conteúdo do alvará conforme os requisitos V7 ao V14 e V17, do MCT 10, Volume I [3].

**4 DOCUMENTOS DA ICP-BRASIL**

4.1 4.1 Os documentos abaixo são aprovados por Resoluções do Comitê Gestor da ICP-Brasil, podendo ser alterados, quando necessário, pelo mesmo tipo de dispositivo legal. O sítio http://www.iti.gov.br publica a versão mais atualizada desses documentos e as Resoluções que os aprovaram.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p><em>Ref.</em></p></td>      <td rowspan="1" colspan="1"><p><em>Nome do documento</em></p></td>      <td rowspan="1" colspan="1"><p><em>Código</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[1]</p></td>      <td rowspan="1" colspan="1"><p>REQUISITOS MÍNIMOS PARA AS DECLARAÇÕES DE PRÁTICAS DAS AUTORIDADES DE CARIMBO DO TEMPO DA ICP- BRASIL</p><p>Aprovado pela Resolução nº 59, de 28 de novembro de 2008</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-12</p></td>     </tr>    </tbody>   </table>

4.2 Os documentos abaixo são aprovados por Instrução Normativa da AC Raiz, podendo ser alterados, quando necessário, pelo mesmo tipo de dispositivo legal. O sítio http://www.iti.gov.br publica a versão mais atualizada desses documentos e as Instruções Normativas que os aprovaram.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p><em>Ref.</em></p></td>      <td rowspan="1" colspan="1"><p><em>Nome do documento</em></p></td>      <td rowspan="1" colspan="1"><p><em>Código</em></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[2]</p></td>      <td rowspan="1" colspan="1"><p>REQUISITOS PARA GERAÇÃO E VERIFICAÇÃO DE ASSINATURAS DIGITAIS NA ICP-BRASIL</p><p>Aprovado pela Instrução Normativa nº 01, de 09 de janeiro de 2009</p></td>      <td rowspan="1" colspan="1"><p>DOC-ICP-15.01</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>[3]</p></td>      <td rowspan="1" colspan="1"><p>REQUISITOS E DOCUMENTOS TÉCNICOS PARA HOMOLOGAÇÃO DE CARIMBO DO TEMPO NO ÂMBITO DA ICP-BRASIL</p><p>Aprovado pela Instrução Normativa nº 04, de 23 de abril de 2010</p></td>      <td rowspan="1" colspan="1"><p>MCT10-VOLUME I E II</p></td>     </tr>    </tbody>   </table>

**5 REFERÊNCIAS**

RFC 5035, Enhanced Security Services (ESS) Update: Adding CertID Algorithm Agility, 2007.

RFC 5755, An Internet Attribute Certificate Profile for Authorization, 2010.

RFC 2634, Enhanced Security Services for S/MINE, 1999
