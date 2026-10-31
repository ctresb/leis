---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 637, DE 13 DE JUNHO DE 2025"
orgao: "Banco Central do Brasil/Área de Regulação/Departamento de Regulação do Sistema Financeiro"
tipo: "Instrução Normativa"
numero: "637"
data: 2025-06-13
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 16/06/2025, seção 1, p. 124"
data_publicacao: 2025-06-16
edicao: "112"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-637-de-13-de-junho-de-2025-636276549"
baixado_em: 2026-10-16
---
# INSTRUÇÃO NORMATIVA BCB Nº 637, DE 13 DE JUNHO DE 2025

INSTRUÇÃO NORMATIVA BCB Nº 637, DE 13 DE JUNHO DE 2025

Divulga a versão 8.0 do Manual de Experiência do Cliente no Open Finance.

Os Chefes do Departamento de Regulação do Sistema Financeiro (Denor) e do Departamento de Tecnologia da Informação (Deinf), no uso das atribuições que lhes conferem o art. 23, inciso I, alínea "a", do Regimento Interno do Banco Central do Brasil, anexo à Resolução BCB nº 340, de 21 de setembro de 2023, com base no art. 3º, inciso V, da Resolução BCB nº 32, de 29 de outubro de 2020, resolve M :

**Art. 1º** Esta Instrução Normativa divulga a versão 8.0 do Manual de Experiência do Cliente no Open Finance, de observância obrigatória por parte das instituições participantes, conforme Anexo.

**Parágrafo único.** O manual de que trata o caput, em sua versão mais recente, estará acessível na página do Open Finance no sítio eletrônico do Banco Central do Brasil na internet e no Portal do Open Finance no Brasil, mantido pelas instituições financeiras e pelas instituições de pagamento que integram a Estrutura Responsável pela Governança do Open Finance de que trata o art. 44, § 1º, da Resolução Conjunta nº 1, de 4 de maio de 2020.

**Art. 2º** Fica revogada a Instrução Normativa BCB nº 559, de 4 de dezembro de 2024, publicada no Diário Oficial da União de 5 de dezembro de 2024.

**Art. 3º** Esta Instrução Normativa entra em vigor na data de sua publicação.

MARDILSON FERNANDES QUEIROZ

Chefe do Denor

CAIO MOREIRA FERNANDES

Chefe do Deinf

## ANEXO

Manual de Experiência do Cliente no Open Finance Versão 8.0

Sumário de alterações

| Data | Versão | Descrição das alterações |
| --- | --- | --- |
| 13/6/2025 | 8.0 | Subseção 3.4: complementos ao princípio de Transparência. |
|  |  | Subseções 4.1.1; 4.1.2; 4.1.3: acréscimo de excepcionalidade na etapa de seleção de instituições transmissoras de dados e instituições detentoras de conta. |
|  |  | Subseção 4.1.4: inclusão da jornada de iniciação de transação de pagamentos sucessivos de Pix Automático. |

Termos de Uso

Este manual define os princípios básicos da experiência do cliente no Open Finance, complementando a regulamentação vigente sobre o tema.

Este manual será revisto e atualizado periodicamente a fim de preservar a compatibilidade com a regulamentação, bem como incorporar os aprimoramentos decorrentes da evolução do Open Finance.

Informações mais detalhadas e exemplos da aplicação deste manual poderão ser encontradas no Portal do Open Finance no Brasil (https://openfinancebrasil.org.br/), mantido pelas instituições financeiras e pelas instituições de pagamento que integram a Estrutura de Governança do Open Finance de que trata o art. 44, § 1º, da Resolução Conjunta nº 1, de 2020.

Sugestões, críticas ou pedidos de esclarecimento de dúvidas relativas ao conteúdo deste documento podem ser enviados ao Banco Central do Brasil por meio dos canais institucionais dessa autarquia.

Referências

As especificações constantes neste manual baseiam-se, referenciam e complementam, quando aplicável, os seguintes documentos:

I - Resolução Conjunta nº 1, de 4 de maio de 2020, que dispõe sobre a implementação do Open Finance, na qual estão estabelecidos conceitos, objetivos, princípios e outras obrigações para as instituições participantes;

II - Circular nº 4.015, de 4 de maio de 2020, que dispõe sobre o escopo de dados e serviços do Open Finance;

III - Resolução BCB nº 1, de 12 de agosto de 2020, que institui o arranjo de pagamentos Pix e aprova o seu Regulamento.

IV - Resolução BCB nº 32, de 29 de outubro de 2020, que estabelece os requisitos técnicos e os procedimentos operacionais para a implementação do Open Finance;

V - Resolução BCB nº 406, de 2 de agosto de 2024, que dispõe sobre o compartilhamento do serviço de iniciação de transação de pagamento sem o redirecionamento para outros ambientes; e

VI - Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais - LGPD).

Os atos normativos de competência do Conselho Monetário Nacional ou do Banco Central do Brasil podem ser acessados no sítio eletrônico do Banco Central do Brasil na internet (www.bcb.gov.br), por meio da opção de "Busca de normas".

1\. Introdução

Este manual visa a garantir que a experiência do cliente ao compartilhar dados e serviços entre as instituições participantes do Open Finance seja segura, ágil, precisa e conveniente. Os consumidores de produtos e serviços financeiros somente terão confiança para autorizar o compartilhamento de dados e serviços se a sua experiência for condizente com suas expectativas e se as informações a respeito do processo lhes forem apresentadas de maneira clara e intuitiva, permitindo que seu consentimento para compartilhamento de dados e serviços seja inequívoco e bem-informado. Para que isso aconteça, é essencial que a jornada de compartilhamento ocorra em um ambiente seguro, com o mínimo de fricções possíveis.

Ao longo deste manual, algumas expressões serão frequentemente utilizadas, entre as quais:

I - jornada simples de compartilhamento de dados e serviços: sequência de etapas do compartilhamento de dados ou serviços realizada por um único cliente, pessoa natural ou jurídica;

II - jornada múltipla de compartilhamento de dados e serviços: sequência de etapas do compartilhamento de dados ou serviços quando é necessária a autorização de mais de um cliente, a exemplo de contas de pessoas jurídicas, em que o cliente solicitante inicia o compartilhamento de dados ou serviços e clientes aprovadores (representantes ou procuradores da pessoa jurídica) precisam autorizá-lo; e

III - ambiente de gestão de consentimentos: ambiente disponibilizado pelas instituições participantes em seus canais eletrônicos para que o cliente consulte e gerencie os consentimentos já efetivados ou pendentes, inclusive para fins de sua revogação.

As expressões mencionadas são utilizadas com objetivo de facilitar a compreensão deste manual e não precisam ser, necessariamente, empregadas durante as etapas da solicitação de compartilhamento.

2\. Disposições gerais sobre a experiência do cliente no Open Finance

É vedado às instituições participantes criar obstáculos ou adotar mecanismos que, de alguma maneira, prejudiquem a fluidez da jornada do cliente ou o incentivem, de forma voluntária ou involuntária, a desistir do compartilhamento de dados ou de serviços no âmbito do Open Finance. Tais obstáculos ou mecanismos incluem, por exemplo, a oferta de produtos e serviços ao cliente no decorrer de quaisquer jornadas do Open Finance, a inserção de telas, etapas ou informações desnecessárias, duplicadas ou redundantes, ou o uso de linguagem que possa gerar incerteza ou que afete negativamente, de forma direta ou indireta, a percepção do cliente quanto à credibilidade e à segurança do Open Finance ou das demais instituições participantes.

A vedação se aplica a todas as etapas da jornada do cliente no Open Finance referentes aos dados e serviços já tipificados ou que venham a sê-lo no âmbito do ecossistema, bem como às informações referentes à jornada de compartilhamento divulgadas nos diferentes canais de comunicação das instituições participantes com seus clientes.

As instituições participantes devem garantir que seus clientes vivenciem a melhor experiência nas jornadas do Open Finance. Com vistas a atingir esse objetivo, as instituições participantes que oferecem acesso aos seus produtos e serviços também por meio de aplicativo devem ofertar as jornadas do Open Finance também nesse canal.

As disposições ora estabelecidas devem constar de forma expressa no Guia de Experiência do Cliente, objeto da seção 4 deste manual.

3\. Princípios da experiência do cliente no Open Finance

Tendo por base as disposições da Resolução Conjunta nº 1, de 2020, consideram-se princípios da experiência do cliente no Open Finance:

I - a segurança e a privacidade;

II - a agilidade;

III - a conveniência e o controle; e

IV - a transparência e a clareza.

3.1 Segurança e privacidade

O compartilhamento de dados e serviços no Open Finance deve ser realizado em um ambiente seguro, que garanta a privacidade dos dados pessoais do cliente, com observância da legislação e da regulamentação vigentes, especialmente dos atos normativos que tratam de segurança e privacidade de dados pessoais.

Durante as jornadas do compartilhamento, o cliente deve ser adequadamente informado sobre a segurança do processo, objetivando o consentimento para o compartilhamento de seus dados cadastrais e transacionais, bem como do serviço de iniciação de transação de pagamento.

3.2 Agilidade

O processo de compartilhamento de dados e serviços no Open Finance deve ter duração compatível com os seus objetivos e o nível de complexidade, assegurando as condições necessárias para a livre escolha e a tomada de decisão por parte do cliente. Um processo desnecessariamente longo pode provocar a desistência do cliente, enquanto eventual precariedade na prestação de informações não permite uma tomada de decisão adequada.

O processo de compartilhamento de dados e serviços deve ocorrer de forma sucessiva e ininterrupta. Sendo assim, as etapas da solicitação de compartilhamento não devem ser interrompidas até a sua conclusão nem devem exigir ações desnecessárias por parte do cliente.

Nos casos de jornada múltipla de compartilhamento de dados e serviços, a confirmação do compartilhamento somente ocorrerá após a finalização do processo por todos os clientes envolvidos no compartilhamento, que não precisarão fazê-lo de forma simultânea ou imediata, observada a garantia da segurança e da transparência do processo, inclusive no que diz respeito aos prazos necessários para a sua conclusão.

3.3 Conveniência e controle

O compartilhamento de dados e serviços no Open Finance deve ser realizado para finalidades específicas e de forma conveniente e acessível ao cliente, inclusive no que diz respeito aos canais de acesso das instituições participantes. Deverão ser asseguradas ao cliente as condições necessárias para o exercício do controle dos seus dados pessoais compartilhados no Open Finance. Nesse sentido, a jornada de compartilhamento deve ser centrada no cliente, tendo em vista o seu perfil, as suas necessidades, os seus objetivos e as suas expectativas, com a disponibilização de informações e ambientes de gestão de consentimentos, inclusive para a revogação do consentimento quando entender oportuno e apropriado, respeitados os prazos definidos na regulamentação vigente.

As instituições participantes do Open Finance não podem criar etapas adicionais ou utilizar métodos de autenticação e confirmação mais rigorosos para confirmação do compartilhamento de dados e serviços no âmbito do Open Finance.

Em jornadas de múltipla alçada de pessoas jurídicas, os poderes e alçadas já constituídos e definidos para movimentação de contas nas suas políticas internas, tais como estatutos, contratos sociais ou outros documentos correlatos, devem ser utilizados para fins de compartilhamento de dados e serviços, de modo que é vedado às instituições transmissoras de dados e detentoras de conta exigirem a constituição de poderes e alçadas específicos para fins de compartilhamentos de dados e serviços no âmbito do Open Finance.

Adicionalmente, as instituições transmissoras de dados e detentoras de conta que disponibilizam, em seus canais, mecanismos para que representantes legais devidamente constituídos perante as próprias instituições possam autorizar ou delegar poderes para outras pessoas, devem contemplar, nesses mecanismos, a possibilidade de autorização ou delegação de poderes para compartilhamento de dados e serviços no âmbito do Open Finance.

3.4 Transparência e clareza

O cliente deve receber informações claras, objetivas e adequadas nas suas interações relacionadas ao Open Finance, desde o momento do consentimento até a prestação das informações posteriormente e no ambiente de gestão dos consentimentos.

A instituição receptora de dados deve informar ao cliente com clareza e de forma tempestiva sobre quais dados serão compartilhados, inclusive referentes a produtos ou serviços que poderão vir a ser contratados pelo cliente ou comercializados pela instituição transmissora de dados no futuro, e os motivos pelos quais esses dados serão necessários para as finalidades em questão, além de outras informações obrigatórias previstas na regulamentação vigente. No caso de compartilhamento de serviços, deve sempre ficar transparente para o cliente durante a jornada qual é a instituição participante responsável pela prestação desse serviço, bem como as condições do serviço que está sendo prestado.

Informações desnecessárias ou excessivamente complexas podem gerar dúvidas e inseguranças ao cliente, que poderá desistir do compartilhamento por falta de compreensão do processo. Assim, as informações fornecidas ao cliente devem ser suficientes e precisas para que sua tomada de decisão seja inequívoca e bem-informada.

A linguagem utilizada deve ser simples, inclusiva e compreensível, independentemente do nível de conhecimento prévio do cliente sobre produtos e serviços financeiros. Deve-se evitar o uso de termos técnicos. Os termos e expressões utilizados neste manual e nos demais atos normativos editados pelo Banco Central do Brasil relacionados ao Open Finance podem ser substituídos por outros considerados mais adequados para a compreensão de todos os clientes do Open Finance, desde que os seus significados sejam mantidos.

A interface deve ser intuitiva, ter organização e elementos que facilitem a legibilidade e o entendimento da informação e deve manter padrões de comunicação consistentes com os demais serviços da instituição. As instituições participantes devem observar os princípios de acessibilidade, na forma da legislação vigente.

A instituição deve dar retorno ao cliente acerca de suas ações ao longo das jornadas para aumentar a sua confiança, facilitar a compreensão das etapas e prevenir erros. No caso de erros, deve ser informado ao cliente, de maneira clara e específica, sobre o problema ocorrido e orientações sobre como proceder.

4\. Guia de Experiência do Cliente

Conforme a Resolução BCB nº 32, de 2020, a Estrutura Responsável pela Governança do Open Finance deverá disponibilizar às instituições participantes e ao público em geral o Guia de Experiência do Cliente, que congregará procedimentos operacionais e requisitos obrigatórios para todas as instituições participantes na interação com seus clientes durante a jornada do compartilhamento, observados os princípios e demais disposições deste manual e na regulamentação vigente sobre o Open Finance. A disponibilização desse documento, em sua versão mais atual, deverá ser realizada por meio do Portal do Open Finance no Brasil.

O Guia deverá ser revisado e atualizado periodicamente pela Estrutura Responsável pela Governança do Open Finance, que deverá manter controle transparente das versões publicadas. A publicação de novas versões do documento deverá ser acompanhada de testes de usabilidade com clientes representativos do público-alvo do Open Finance, bem como comunicada de forma tempestiva às instituições participantes e ao Banco Central do Brasil, que poderá determinar ajustes e correções.

Admite-se que o Guia estabeleça princípios e requisitos adicionais aos constantes neste manual. No entanto, o seu conteúdo deve estar em conformidade com o disposto na legislação e na regulamentação vigentes.

4.1 Conteúdo do Guia de Experiência do Cliente

O Guia de Experiência do Cliente deverá dispor sobre, no mínimo:

4.1.1 Jornada simples de compartilhamento de dados

O conteúdo dessa jornada deve abranger, no mínimo:

I - a identificação do cliente

Nessa etapa, a instituição receptora de dados deve identificar o cliente, conforme exigido pela regulamentação vigente.

II - as finalidades determinadas do consentimento

Nessa etapa, a instituição receptora de dados deve informar o cliente a(s) finalidade(s) e o(s) serviço(s) associados ao compartilhamento de dados.

III - a seleção dos dados objeto de compartilhamento na instituição receptora de dados

O cliente deve poder selecionar os dados que deseja compartilhar, observando os agrupamentos de dados definidos com base no art. 11 da Resolução Conjunta nº 1, de 2020.

O cliente deve ser informado sobre quais dados são necessários para a finalidade do compartilhamento e, conforme o caso, quais seriam opcionais. Os dados opcionais devem corresponder a uma finalidade determinada, mesmo que secundária em relação à finalidade principal. O cliente deve ser informado ainda sobre os motivos pelos quais esses dados são necessários para a(s) finalidade(s) em questão.

É facultada a apresentação de recurso de "Termos e Condições", ou similar, desde que não seja exigida ação adicional do cliente para o aceite dos termos.

IV - a seleção do prazo de compartilhamento de dados

O cliente deve poder selecionar o prazo pelo qual deseja compartilhar os dados selecionados, observada a finalidade e outros aspectos estabelecidos na regulamentação específica do Open Finance.

V - a seleção da instituição transmissora de dados

O cliente deve poder selecionar a instituição transmissora dos dados. Deve ser disponibilizado mecanismo de busca que propicie uma seleção ágil e clara da instituição desejada. Devem estar listadas todas as instituições participantes para fins de compartilhamento de dados no Open Finance devidamente registradas no Diretório de Participantes mantido pela Estrutura Responsável pela Governança do Open Finance.

Nos casos em que houver tickets bilaterais que se refiram a erros impeditivos durante ou após a jornada, de forma excepcional, a instituição transmissora de dados poderá estar desabilitada para seleção e o cliente deve ser informado de forma clara sobre essa restrição temporária. Essa excepcionalidade é válida apenas durante o período em que o ticket estiver em andamento no Service Desk mantido pela Estrutura de Governança do Open Finance.

VI - o redirecionamento para o ambiente da instituição transmissora de dados

O cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição transmissora de dados selecionada. Deve ficar claro para o cliente que o compartilhamento ainda não está concluído e que etapas adicionais são necessárias para a sua efetivação.

O redirecionamento não pode envolver qualquer ação do cliente, tendo caráter apenas informativo, e deve contemplar o que segue:

a) jornadas iniciadas na instituição receptora de dados em dispositivo desktop: o redirecionamento deve ocorrer, preferencialmente, para o mesmo dispositivo; e

b) jornadas iniciadas na instituição receptora de dados em dispositivo móvel:

1\. no caso das instituições transmissoras de dados pertencentes aos conglomerados sujeitos ao monitoramento de jornada do cliente, conforme Manual de Monitoramento do Open Finance, o redirecionamento deve ocorrer diretamente para o aplicativo da instituição transmissora sem a passagem por navegadores; e

2\. as demais instituições transmissoras de dados não abrangidas pelo monitoramento de jornada do cliente, conforme Manual de Monitoramento do Open Finance, devem observar, preferencialmente, o redirecionamento para seus aplicativos.

Os conglomerados enquadrados no item 1 podem apresentar ao Banco Central do Brasil pedidos fundamentados para a dispensa de instituições ou marcas específicas em que o redirecionamento obrigatório para o aplicativo possa prejudicar a jornada dos seus clientes.

Excepcionalmente, caso o cliente não possua o aplicativo da instituição transmissora instalado no dispositivo móvel, o redirecionamento deve ser feito para o ambiente da instituição no navegador ou para a loja de aplicativos, sempre no mesmo dispositivo.

VII - a autenticação do cliente na instituição transmissora de dados

O cliente deve se autenticar na instituição transmissora de dados. O cliente deve poder reconhecer que está no ambiente da instituição com a qual já mantém relacionamento e que as credenciais utilizadas para autenticação não estão visíveis e não serão compartilhadas com a instituição receptora dos dados.

Conforme estabelece a Resolução Conjunta nº 1, de 2020, os procedimentos e controles para autenticação do cliente devem ser compatíveis com os aplicáveis ao acesso aos canais de atendimento eletrônicos já disponibilizados pela instituição transmissora. Essa compatibilidade abrange, entre outros, os fatores de autenticação, a quantidade de etapas e a duração do procedimento.

VIII - a confirmação de compartilhamento pelo cliente na instituição transmissora de dados

O cliente deve confirmar o compartilhamento na instituição transmissora de dados. Deve ser apresentado ao cliente para conferência, no mínimo, a identificação da instituição receptora de dados, o período de validade do consentimento e os dados que serão objeto de compartilhamento.

Todas as origens ou agrupamentos de dados apresentados ao cliente devem estar pré-selecionados, de modo que somente seja requerida ação do cliente caso ele deseje excluir um ou mais itens do escopo a ser compartilhado (opt-out).

A seleção dos agrupamentos de dados para compartilhamento não pode ser alterada no ambiente da instituição transmissora. Seleções no ambiente da instituição transmissora devem se restringir à origem dos dados.

Excepcionalmente no caso de operações de crédito, de investimento e de câmbio, os dados devem ser apresentados em agrupamentos únicos que englobem todas as diferentes modalidades de produtos ou serviços existentes, inclusive as modalidades não contratadas pelo cliente ou que ainda não são comercializadas pela instituição, sendo vedada a possibilidade de seleção pelo cliente da origem dos dados (modalidades, submodalidades, ou contratos específicos) para o compartilhamento.

O eventual detalhamento dos dados objeto do compartilhamento deve ser ocultado por padrão. Deve ser disponibilizado recurso (botão, link, entre outros) para que o cliente, caso deseje, possa acessar o detalhamento dos dados que serão compartilhados.

A jornada de compartilhamento de dados no ambiente da instituição transmissora de dados não deve conter recurso de "Termos e Condições", ou similar. O referido recurso pode, a critério da instituição, constar no ambiente de Gestão de Consentimentos da transmissora, de que trata a subseção 4.1.5 deste manual.

IX - o redirecionamento para o ambiente da instituição receptora de dados

O cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição receptora de dados e que essa etapa é necessária para conclusão do compartilhamento. O redirecionamento não pode envolver qualquer ação do cliente, tendo caráter apenas informativo, e deve ocorrer para o mesmo canal eletrônico da instituição receptora de dados utilizado pelo cliente na etapa inicial da jornada.

As instituições sujeitas à obrigação de redirecionamento para o aplicativo sem a passagem por navegadores, conforme disposto no inciso VI desta subseção, quando estiverem atuando como receptoras de dados, devem implementar o redirecionamento previsto nesta etapa também sem a passagem por navegadores.

X - a efetivação da solicitação de compartilhamento de dados

O cliente deve ser comunicado pela instituição receptora de dados sobre a efetivação da solicitação de compartilhamento de dados. A comunicação deve incluir, no mínimo, a(s) finalidade(s), o prazo e os dados do compartilhamento.

4.1.2 Jornada simples de compartilhamento de serviço de iniciação de transação de pagamento com redirecionamento

O conteúdo dessa jornada deve abranger, no mínimo:

I - a identificação do cliente

A instituição iniciadora de transação de pagamento deve identificar o cliente, conforme exigido pela regulamentação vigente.

II - a seleção da instituição detentora de conta

O cliente deve poder selecionar a instituição na qual mantém a conta que será utilizada para o pagamento. Deve ser disponibilizado mecanismo de busca que propicie uma seleção ágil e clara da instituição desejada. Devem estar listadas todas as instituições participantes para fins de compartilhamento do serviço de iniciação de transação pagamento no Open Finance devidamente registradas como instituições detentoras de conta no Diretório de Participantes mantido pela Estrutura Responsável pela Governança do Open Finance com APIs publicadas para oferta do produto.

Nos casos em que houver tickets bilaterais que se refiram a erros impeditivos durante ou após a jornada, de forma excepcional, a instituição detentora de conta poderá estar desabilitada para seleção e o cliente deve ser informado de forma clara sobre essa restrição temporária. Essa excepcionalidade é válida apenas durante o período em que o ticket estiver em andamento no Service Desk mantido pela Estrutura de Governança do Open Finance.

III - as informações sobre a transação de pagamento ou a configuração de uma recorrência, no caso de pagamentos sucessivos

Devem ser solicitadas ou apresentadas ao cliente, no mínimo, as informações abaixo:

a) no caso de pagamentos únicos:

1\. o valor do pagamento;

2\. a forma de pagamento, de acordo com os serviços de pagamento de que trata o art. 6º da Circular nº 4.015, de 2020;

3\. os dados do recebedor do pagamento, de acordo com os parâmetros referentes à forma de pagamento;

4\. a data do pagamento; e

5\. o valor da tarifa cobrada pelo serviço de iniciação de transação de pagamento, quando houver; e

b) no caso de configuração de recorrência para pagamentos sucessivos:

1\. o valor do pagamento, quando aplicável, sendo facultativo nos casos de transações de pagamento sucessivas em que o valor pactuado seja variável;

2\. a forma de pagamento, de acordo com os serviços de pagamento de que trata o art. 6º da Circular nº 4.015, de 2020;

3\. as datas futuras dos pagamentos, quando aplicável;

4\. a periodicidade das transações ou as condições que as desencadeiem;

5\. o prazo do consentimento, quando aplicável;

6\. limites, quando aplicável;

7\. os dados do recebedor do pagamento, de acordo com os parâmetros referentes à forma de pagamento; e

8\. o valor da tarifa cobrada pelo serviço de iniciação de transação de pagamento, quando houver.

Além das informações mínimas para a iniciação de transação de pagamento dispostas acima, devem ser observados, de forma geral, os dados dispostos nos regulamentos ou instrumentos que disciplinem o funcionamento do arranjo de pagamento referente à respectiva transação de pagamento e demais dados estabelecidos nas especificações disponíveis no Portal do Open Finance no Brasil.

É facultada nessa etapa a apresentação de recurso de "Termos e Condições", ou similar, desde que não seja exigida ação adicional do cliente para o aceite dos termos.

IV - o redirecionamento para o ambiente da instituição detentora de conta

O cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição detentora de conta selecionada. Deve ficar claro para o cliente que o pagamento ainda não está concluído e que etapas adicionais são necessárias para a sua efetivação. O cliente deve ser informado, ainda, sobre o tempo máximo que ele possui para confirmar a transação.

O redirecionamento não pode exigir qualquer ação do cliente, tendo caráter apenas informativo, e deve contemplar o que segue:

a) jornadas iniciadas na instituição iniciadora de transação de pagamentos em dispositivo desktop: o redirecionamento deve ocorrer, preferencialmente, para o mesmo dispositivo; e

b) jornadas iniciadas na instituição iniciadora de transação de pagamentos em dispositivo móvel:

1\. no caso das instituições detentoras de conta pertencentes aos conglomerados sujeitos ao monitoramento de jornada do cliente, conforme Manual de Monitoramento do Open Finance, o redirecionamento deve ocorrer diretamente para o aplicativo da instituição detentora sem a passagem por navegadores; e

2\. as demais instituições detentoras de conta não abrangidas pelo monitoramento de jornada do cliente, conforme Manual de Monitoramento do Open Finance, devem realizar, preferencialmente, o redirecionamento para seus aplicativos.

Excepcionalmente, caso o cliente não possua o aplicativo da instituição detentora de conta instalado em seu dispositivo móvel, o redirecionamento deve ser realizado para o ambiente da instituição no navegador ou para a loja de aplicativos, sempre no mesmo dispositivo.

Ressalta-se que não há obrigatoriedade de desenvolvimento de aplicativo para as instituições que não ofereçam esse canal aos seus clientes. Nesse último caso, pode ser utilizado o canal da instituição no navegador.

V - a autenticação do cliente na instituição detentora de conta

O cliente deve se autenticar na instituição detentora de conta. O cliente deve poder reconhecer que está no ambiente da instituição com a qual já mantém relacionamento e que as credenciais utilizadas para autenticação não estão visíveis e não serão compartilhadas com a instituição iniciadora de transação de pagamento.

Conforme estabelece a Resolução Conjunta nº 1, de 2020, os procedimentos e controles para autenticação do cliente devem ser compatíveis com os aplicáveis ao acesso aos canais de atendimento eletrônicos já disponibilizados pela instituição detentora de conta. Essa compatibilidade abrange, entre outros, os fatores de autenticação, a quantidade de etapas e a duração do procedimento.

VI - a confirmação de compartilhamento pelo cliente na instituição detentora de conta

O cliente deve confirmar o pagamento na instituição detentora de conta. Caso seja titular de mais de uma conta associada às credenciais com as quais se autenticou, o cliente deve poder selecionar a conta que deseja utilizar para a transação de pagamento.

Devem ser apresentadas ao cliente para confirmação, no mínimo, as informações listadas nos itens 1 a 4 da alínea "a" e 1 a 7 da alínea "b" do inciso III desta subseção, que tratam da etapa das informações sobre a transação de pagamento. Adicionalmente, deve ser apresentado ao cliente o valor da tarifa cobrada pela instituição detentora de conta na realização da transação de pagamento, quando houver.

A jornada de compartilhamento de serviço de iniciação de transação de pagamento no ambiente da instituição detentora de conta não deve conter recurso de "Termos e Condições", ou similar. O referido recurso pode, a critério da instituição, constar no ambiente de Gestão de Consentimentos da detentora de conta, de que trata a subseção 4.1.5 deste manual.

VII - o redirecionamento para o ambiente da instituição iniciadora de transação de pagamento

O cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição iniciadora de transação de pagamento e que essa etapa é necessária para conclusão do compartilhamento. O redirecionamento não pode exigir qualquer ação do cliente, tendo caráter apenas informativo, e deve ocorrer para o mesmo canal eletrônico da instituição iniciadora de transação de pagamento utilizado pelo cliente na etapa inicial da jornada.

As instituições sujeitas à obrigação de redirecionamento para o aplicativo sem a passagem por navegadores, conforme disposto no inciso IV desta subseção, quando estiverem atuando como iniciadoras de transação de pagamento, devem implementar o redirecionamento previsto nesta etapa também sem a passagem por navegadores.

VIII - a efetivação da transação de pagamento

A instituição iniciadora de transação de pagamento deve apresentar o comprovante da efetivação da transação de pagamento, seja ele único ou sucessivo. Deve ser apresentado ao cliente comprovante com, no mínimo, as informações listadas no inciso III desta subseção, que trata da etapa das informações sobre a transação de pagamento.

4.1.3 Jornada simples de compartilhamento de serviço de iniciação de transação de pagamento sem redirecionamento

A jornada simples de compartilhamento de serviço de iniciação de transação de pagamento sem redirecionamento é composta por duas etapas: a de vinculação de conta e a de transação de pagamento.

4.1.3.1 Etapa de vinculação de conta

O conteúdo dessa jornada deve abranger, no mínimo:

I - a identificação do cliente

A instituição iniciadora de transação de pagamento deve identificar o cliente, conforme exigido pela regulamentação vigente.

II - a seleção da instituição detentora de conta

O cliente deve poder selecionar a instituição na qual mantém a conta que será vinculada para a realização das transações de pagamento. Deve ser disponibilizado mecanismo de busca que propicie uma seleção ágil e clara da instituição desejada. Devem estar listadas as instituições detentoras de conta com implementação obrigatória, de acordo com a Resolução BCB nº 406, de 2024, art. 6º, e as que facultativamente aderirem ao serviço.

Nos casos em que houver tickets bilaterais que se refiram a erros impeditivos durante ou após a jornada, de forma excepcional, a instituição detentora de conta poderá estar desabilitada para seleção e o cliente deve ser informado de forma clara sobre essa restrição temporária. Essa excepcionalidade é válida apenas durante o período em que o ticket estiver em andamento no Service Desk mantido pela Estrutura de Governança do Open Finance.

III - o redirecionamento para o ambiente da instituição detentora de conta

O cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição detentora de conta selecionada. Deve ficar claro para o cliente que a vinculação de conta ainda não está concluída e que etapas adicionais são necessárias para a sua efetivação. O cliente deve ser informado, ainda, sobre o tempo máximo que ele possui para confirmar a vinculação.

São aplicáveis todas as disposições previstas na subseção 4.1.2, inciso IV.

IV - a autenticação do cliente na instituição detentora de conta

São aplicáveis todas as disposições previstas na subseção 4.1.2, inciso V.

V - a apresentação das informações sobre a vinculação de conta

Devem ser apresentadas ao cliente as informações sobre a vinculação de conta que será realizada. As informações devem incluir, no mínimo:

a) a identificação do usuário;

b) a identificação da instituição iniciadora;

c) o prazo de validade do consentimento de cinco anos, conforme exigido pela regulamentação vigente, que o cliente deve poder reduzir ou aumentar;

d) os valores máximos por transação e por dia:

1\. o campo do valor máximo por transação de R$500,00 preenchido, que o cliente deve poder reduzir; e

2\. o campo do valor máximo por dia não preenchido, que o cliente deve ter a opção de inserir um valor; e

e) a identificação da conta de origem.

O cliente deve ser informado que serão respeitados os limites para transações Pix estabelecidos na instituição detentora da conta vinculada.

Instituições participantes com contratos bilaterais poderão apresentar um limite por transação superior, conforme o parágrafo único do art. 7º da Resolução BCB nº 406, de 2024.

VI - a confirmação de compartilhamento pelo cliente na instituição detentora de conta:

O cliente deve confirmar a vinculação de conta na instituição detentora de conta ao visualizar as informações listadas nas alíneas "a" a "e" do inciso V da subseção 4.1.3.1, que trata das informações sobre a vinculação de conta.

Caso seja titular de mais de uma conta associada às credenciais com as quais se autenticou, o cliente deve poder selecionar a conta que deseja utilizar para a vinculação.

A jornada de compartilhamento de serviço de iniciação de transação de pagamento no ambiente da instituição detentora de conta não deve conter recurso de "Termos e Condições", ou similar. O referido recurso pode, a critério da instituição, constar no ambiente de Gestão de Consentimentos da instituição detentora de conta, de que trata a subseção 4.1.5 deste manual.

VII - o redirecionamento para o ambiente da instituição iniciadora de transação de pagamento

O cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição iniciadora de transação de pagamento e que esse passo é necessário para conclusão da vinculação de conta. O redirecionamento deve ocorrer para o mesmo canal eletrônico da instituição iniciadora de transação de pagamento utilizado pelo cliente na etapa inicial da jornada.

As instituições sujeitas à obrigação de redirecionamento para o aplicativo sem a passagem por navegadores, conforme disposto no inciso IV da subseção 4.1.2, quando estiverem atuando como iniciadoras de transação de pagamento, devem implementar o redirecionamento previsto nesta etapa também sem a passagem por navegadores.

VIII - a criação de chaves no dispositivo eletrônico

O cliente deve ser informado de que, para concluir a vinculação da conta, é necessário que ele valide a geração de chaves de segurança por meio de suas credenciais cadastradas no dispositivo (biometria, senha etc.).

IX - a efetivação da vinculação de conta

A instituição iniciadora de transação de pagamento deve confirmar a vinculação de conta.

Deve ser informado ao cliente que o resumo do pedido de vinculação estará disponível para consulta no ambiente de gestão de consentimentos (contas vinculadas) e que a revogação pode ser feita a qualquer momento, com a indicação do local para essa ação.

4.1.3.2 Etapa de transação de pagamento

O conteúdo dessa jornada deve abranger, no mínimo:

I - a identificação do cliente

A instituição iniciadora de transação de pagamento deve identificar o cliente, conforme exigido pela regulamentação vigente.

II - a solicitação de iniciação de transação de pagamentos com a conta vinculada

A instituição iniciadora de transação de pagamento deve apresentar ao cliente a possibilidade de realizar o pagamento utilizando sua conta previamente vinculada dentre as demais opções de pagamento.

Deve ficar claro para o cliente o arranjo de pagamento que está sendo utilizado.

III - a seleção da instituição detentora da conta vinculada

O cliente deve poder selecionar a instituição na qual já tenha realizado a etapa de vinculação de conta. Deve ser disponibilizado mecanismo de busca que propicie uma seleção ágil e clara da instituição desejada. Devem estar listadas todas as instituições com as quais o cliente já tenha efetuado etapa de vinculação de conta naquela instituição iniciadora de transação de pagamento e naquele dispositivo.

Nos casos em que houver tickets bilaterais que se refiram a erros impeditivos durante ou após a jornada, de forma excepcional, a instituição detentora de conta poderá estar desabilitada para seleção e o cliente deve ser informado de forma clara sobre essa restrição temporária. Essa excepcionalidade é válida apenas durante o período em que o ticket estiver em andamento no Service Desk mantido pela Estrutura de Governança do Open Finance.

IV - As informações sobre a transação de pagamento único

Devem ser solicitadas ou apresentadas ao cliente, no mínimo, as informações:

a) o valor do pagamento;

b) a forma de pagamento, de acordo com os serviços de pagamento de que trata o art. 6º da Circular nº 4.015, de 2020;

c) os dados do recebedor do pagamento, de acordo com os parâmetros referentes à forma de pagamento;

d) a data do pagamento; e

e) o valor da tarifa cobrada pelo serviço de iniciação de transação de pagamento, quando houver.

Além das informações mínimas para a iniciação de transação de pagamento dispostas acima, devem ser observados, de forma geral, os dados dispostos nos regulamentos ou instrumentos que disciplinam o funcionamento do arranjo de pagamento referente à respectiva transação de pagamento e demais dados estabelecidos nas especificações disponíveis no Portal do Open Finance no Brasil.

É facultada a apresentação de recurso de "Termos e Condições", ou similar, desde que não seja exigida ação adicional do cliente para o aceite dos termos.

V - a confirmação de compartilhamento pelo cliente na instituição iniciadora de transação de pagamento

O cliente deve confirmar o pagamento na instituição iniciadora de transação de pagamento. Deve ser solicitado que o cliente confirme com suas credenciais cadastradas no dispositivo.

VI - a efetivação da transação de pagamento

A instituição iniciadora de transação de pagamento deve apresentar o comprovante da efetivação da transação de pagamento. Deve ser apresentado ao cliente comprovante com, no mínimo, as informações listadas no inciso IV da subseção 4.1.3.2, que trata da etapa das informações sobre a transação de pagamento.

4.1.4 Jornada de compartilhamento de serviço de iniciação de transação de pagamentos sucessivos de Pix Automático

Esta subseção dispõe, especificamente, sobre as características das jornadas de iniciação de transação de pagamento para Pix Automático, em complemento ao disposto nos regulamentos e instrumentos que disciplinam o arranjo de pagamento.

O termo "autorização" utilizado no arranjo de pagamento para esse serviço corresponde, neste Manual, à obtenção do consentimento do cliente.

4.1.4.1 Informações gerais do serviço

Ao utilizar o Pix Automático pela primeira vez na instituição iniciadora de transação de pagamento, o cliente deve receber informações gerais sobre o serviço e suas regras, cobrindo, no mínimo, os seguintes aspectos: o que é o Pix Automático; vantagens e aplicações; e funcionamento geral.

4.1.4.2 Etapa de configuração dos parâmetros do consentimento

Para a identificação do cliente e a seleção da instituição detentora de conta, a instituição iniciadora de transação de pagamento deve observar o disposto nos incisos I e II, respectivamente, da subseção 4.1.2.

I - as informações sobre o consentimento

As informações mínimas a serem apresentadas ao cliente pela instituição iniciadora de transação de pagamento devem seguir o especificado para o prestador de serviços de pagamento (PSP) do pagador na regulamentação do arranjo de pagamento para Pix Automático, incluindo aquelas referentes a pagamentos avulsos, ou seja, pagamentos iniciais que não fazem parte da recorrência, podendo ser imediatos ou agendados. O cliente deve ser, ainda, informado sobre a forma de pagamento - Pix Automático -, a instituição iniciadora de transação de pagamento e eventual valor da tarifa cobrada pelo serviço de iniciação de transação de pagamento.

Com relação ao valor máximo das transações, é vedado à iniciadora de transação de pagamento permitir ao recebedor o acesso a informações sobre valores definidos pelo cliente nesse campo, bem como alterações realizadas posteriormente no ambiente de gestão.

Além das informações mínimas para a iniciação de transação de pagamento dispostas acima, devem ser observados os dados dispostos em outros regulamentos ou instrumentos que disciplinem o funcionamento do arranjo de pagamento referente à respectiva transação de pagamento e demais dados estabelecidos nas especificações disponíveis no Portal do Open Finance no Brasil.

É facultada, nessa etapa, a apresentação de recurso de "Termos e Condições", ou similar, desde que não seja exigida ação adicional do cliente para o aceite dos termos.

II - o redirecionamento para o ambiente da instituição detentora de conta

O cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição detentora de conta selecionada. Deve ficar claro para o cliente que a configuração do consentimento ainda não está concluída e que etapas adicionais são necessárias para a sua efetivação. O cliente deve ser informado, ainda, sobre o tempo máximo que ele possui para confirmar o consentimento.

São aplicáveis todas as disposições previstas na subseção 4.1.2, inciso IV.

III - a autenticação do cliente na instituição detentora de conta

São aplicáveis todas as disposições previstas na subseção 4.1.2, inciso V.

IV - a confirmação de compartilhamento pelo cliente na instituição detentora de conta

Nesta etapa, a instituição detentora de conta deve:

a) permitir que o cliente selecione a conta que deseja utilizar para a configuração, caso seja titular de mais de uma conta associada às credenciais com as quais se autenticou;

b) apresentar as informações na forma do estabelecido no inciso I desta subseção, além do valor da tarifa cobrada pela instituição detentora de conta na realização da transação de pagamento, quando houver;

c) deixar clara a necessidade de pagamento avulso, imediato ou agendado, bem como a data de vencimento e seu respectivo valor; e

d) informar o prazo máximo para aprovação do consentimento, em casos que requeiram múltiplas alçadas, de acordo com os prazos determinados pela Estrutura de Governança do Open Finance.

Nessa etapa, o ambiente da instituição detentora de conta não deve apresentar ao cliente Termos e Condições", ou similar, sendo permitida a sua disponibilização no ambiente de gestão de consentimentos da instituição detentora de conta, de que trata a subseção 4.1.6 deste manual.

É vedado à instituição detentora de conta permitir a edição de campos nesta etapa de confirmação pelo cliente, exceto para escolha da conta de débito, quando necessário.

V - o redirecionamento para o ambiente da instituição iniciadora de transação de pagamento

O cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição iniciadora de transação de pagamento e que esse passo é necessário para a efetivação do consentimento. O redirecionamento deve ocorrer para o mesmo canal eletrônico da instituição iniciadora de transação de pagamento utilizado pelo cliente na etapa inicial da jornada.

As instituições sujeitas à obrigação de redirecionamento para o aplicativo sem a passagem por navegadores, conforme disposto no inciso IV da subseção 4.1.2, quando estiverem atuando como iniciadoras de transação de pagamento, devem implementar o redirecionamento previsto nesta etapa também sem a passagem por navegadores.

VI - a efetivação do consentimento

Nessa etapa, a instituição iniciadora de transação de pagamento deve informar ao cliente sobre a efetivação do consentimento. Devem ser observadas as diretrizes que no arranjo de pagamento se referem à autorização para Pix Automático e à conclusão de pagamentos avulsos.

Quando houver falha na liquidação ou no agendamento do pagamento avulso, a instituição iniciadora de transação de pagamento deve informar ao cliente se o consentimento será ou não mantido, de acordo com o previsto pelo recebedor, e orientá-lo sobre como proceder.

Caso ocorra falha no processamento da efetivação do consentimento, porém com liquidação do pagamento imediato, a instituição iniciadora de transação de pagamento deve fornecer ao cliente o comprovante do pagamento ou do agendamento e uma mensagem clara de orientação sobre como proceder.

Adicionalmente, deve ser informado ao cliente quais ações referentes a alterações e cancelamentos são permitidas no ambiente de gestão da instituição iniciadora de transação de pagamento e da instituição detentora de conta, esclarecendo que o consentimento pode ser revogado a qualquer tempo, em qualquer um dos dois ambientes.

Nos casos em que seja necessária a aprovação em outras alçadas, informar ao cliente o prazo para essa confirmação.

4.1.4.3 Ambiente de gestão

I - Características gerais

As instituições iniciadoras de transação de pagamento e detentoras de conta devem dispor de ambiente de gestão que permita ao cliente realizar consultas, alterações e revogação dos consentimentos relacionados a Pix Automático, bem como dos pagamentos sucessivos associados ao serviço.

Para a instituição detentora de conta, esse ambiente deve ser o mesmo utilizado para as transações realizadas via PSP do pagador, de modo a unificar a experiência do cliente.

II - Consultas a consentimentos e a pagamentos

Nos ambientes da instituição iniciadora de transação de pagamento e da instituição detentora de conta, deve ser permitido ao cliente consultar o histórico de consentimentos para Pix Automático. Deve ser apresentado o estado atual de cada consentimento, a exemplo de: ativo, revogado, pendente etc., e as informações mínimas previstas no arranjo de pagamento de acordo com cada estado do consentimento. Da mesma forma, para consultas e revogação de pagamentos agendados e consultas a pagamentos já liquidados devem ser apresentadas ao cliente as informações definidas pelo arranjo de pagamento para esses casos, inclusive no tocante à disponibilização do comprovante dessas transações.

III - Outras ações possíveis em cada ambiente

Além das funcionalidades previstas no inciso anterior, o ambiente de gestão deve possibilitar ao cliente:

Na instituição iniciadora de transação de pagamento:

a) visualizar e editar, caso seja permitido pelo recebedor, o prazo do consentimento, inclusive alterando-o para prazo indeterminado. Nos casos em que houver redução no prazo do consentimento, o cliente deve ser informado sobre as consequências dessa ação em relação a pagamentos agendados para dias futuros à nova data de expiração;

b) visualizar e editar o valor máximo das transações, sendo que, no caso de edição desse campo, deve-se respeitar eventual valor mínimo estabelecido pelo recebedor e informar ao cliente quando o novo valor passará a ter efeito;

c) editar a data do primeiro pagamento, caso seja permitido pelo recebedor;

d) cancelar o consentimento; e

e) habilitar ou desabilitar notificações.

Nenhuma das alterações acima requer redirecionamento do cliente para a instituição detentora de conta.

Com relação ao valor máximo, é vedado à instituição iniciadora de transação de pagamento permitir ao recebedor o acesso a informações sobre o valor máximo de transações definido pelo cliente, inclusive suas alterações.

Na instituição detentora de conta:

a) visualizar o prazo do consentimento;

b) visualizar e editar o valor máximo das transações, sendo que, no caso de edição desse campo, deve-se respeitar eventual valor mínimo estabelecido pelo recebedor e informar ao cliente quando o novo valor passará a ter efeito;

c) visualizar e editar possibilidade de utilização de limite de crédito, sendo o padrão estar habilitado;

d) cancelar o consentimento; e

e) habilitar ou desabilitar notificações.

Nenhuma das alterações acima requer redirecionamento do cliente para a instituição iniciadora de transação de pagamento.

Na revogação de consentimentos, em quaisquer dos ambientes, o cliente deve ser avisado sobre a impossibilidade de desfazer a ação, bem como suas consequências em relação aos pagamentos futuros.

4.1.4.4 Notificações e mensagens de erro

Fica estabelecido o que segue para as notificações relacionadas a Pix Automático no âmbito do Open Finance.

Para a instituição iniciadora de transação de pagamento:

I - notificações ao usuário pagador relacionadas ao consentimento são obrigatórias, não podendo ser desabilitadas pelo usuário; e

II - notificações ao usuário pagador sobre agendamento e liquidações são opcionais. Se implementadas, deve ser permitido que possam ser desabilitadas pelo usuário.

É vedado à instituição iniciadora de transação de pagamento o encaminhamento ao recebedor de mensagens de erro e motivos de rejeição que especifiquem que houve falha no pagamento por insuficiência de saldo ou de limites. Nesses casos, a instituição iniciadora de transação de pagamento deve comunicar o recebedor sobre o não processamento do pagamento de modo genérico. A orientação para o cliente deve ser a de que busque informações em sua instituição detentora de conta.

Para a instituição detentora de conta:

I - notificações ao usuário pagador relacionadas a agendamento e liquidação de pagamentos deverão estar habilitadas por padrão na instituição detentora de conta e seguir o disposto no arranjo de pagamento para o PSP do pagador;

II - apenas notificações de sucesso de agendamento poderão ser desabilitadas pelos usuários na instituição detentora de conta. As demais permanecerão ativas, também seguindo o definido no arranjo de pagamento;

III - notificações relacionadas ao consentimento são de envio opcional por parte da instituição detentora de conta. Nos casos relacionados a alteração de valor máximo, de configuração de notificações e de utilização ou não do limite de crédito, a instituição detentora de conta também deverá obrigatoriamente notificar o cliente em caso de alteração; e

IV - a instituição detentora de conta deverá comunicar todas as ocorrências de sucesso ou não sucesso de agendamentos e pagamentos à instituição iniciadora de transação de pagamento, para que esta avalie se deseja ou não notificar também o cliente.

Mensagens ao cliente referentes a erros ocorridos durante o processo de consentimento ou de liquidação dos pagamentos devem ser claras e específicas, de modo a possibilitar a compreensão pelo cliente sobre qual foi o problema, de acordo com o princípio de transparência e clareza detalhado no item 3.4 deste documento.

4.1.5 Jornada de múltipla alçada de compartilhamento de dados e serviços

O Guia deve estabelecer parâmetros para a experiência do cliente em jornada múltipla de compartilhamento de dados e serviços, quando for o caso.

Nesse caso, todos os clientes envolvidos no compartilhamento devem ser informados com clareza sobre os procedimentos e as etapas necessárias para a efetivação do compartilhamento. Adicionalmente, os clientes aprovadores devem ser notificados tempestivamente pela instituição transmissora de dados ou detentora de conta sobre a necessidade de ação para efetivação do compartilhamento de dados ou serviços iniciado pelo cliente solicitante.

Em particular, o Guia deve estabelecer, quando for o caso, os prazos máximos para ação dos clientes aprovadores, que deverão ser aplicados de maneira uniforme por todas as instituições participantes. Ademais, o Guia deve estabelecer parâmetros para os casos em que um ou mais clientes aprovadores não autorizem o compartilhamento abrangendo, no mínimo, a notificação aos demais clientes (solicitantes ou aprovadores) e a comunicação à instituição receptora de dados ou iniciadora de transação de pagamento.

Para fins de compartilhamento de dados relacionados a contas conjuntas de pessoas naturais, a instituição transmissora de dados deve garantir que a instituição receptora de dados tenha acesso a dados cadastrais apenas do titular da conta responsável pelo consentimento, não sendo admitido o compartilhamento dos dados cadastrais dos demais titulares da respectiva conta.

A instituição transmissora de dados deve exigir a confirmação de todos os titulares da conta para efetivar o compartilhamento somente se o acesso a informações transacionais da conta depender da autorização de todos os titulares.

4.1.6 Ambiente de gestão dos consentimentos

O Guia deve estabelecer requisitos para o ambiente de gestão de consentimentos das instituições participantes. No caso, as referidas instituições devem disponibilizar em seu canal eletrônico um ambiente específico para a gestão dos compartilhamentos em que estiveram envolvidas no âmbito do Open Finance.

Nesse ambiente, o cliente deve ter acesso de forma simples, ágil, precisa e conveniente a, no mínimo, informações sobre consentimentos e vínculos de contas vigentes ou que estejam pendentes de efetivação na jornada múltipla, com a possibilidade de pesquisa com base em critérios definidos para observância homogênea por todas as instituições participantes.

Adicionalmente, o cliente deve ter a faculdade de consultar e revogar os consentimentos, com observância do disposto no art. 15 da Resolução Conjunta nº 1, de 2020. A efetivação de revogação deve ser precedida de tela de confirmação com informações sobre as consequências da ação.

4.1.7 A padronização da terminologia utilizada pelas instituições participantes durante a jornada do compartilhamento

O Guia deve padronizar a terminologia utilizada pelas instituições participantes na comunicação com seus clientes durante a jornada de compartilhamento de dados e serviços.

A terminologia contida no Guia deve ser adotada por todas as instituições participantes, inclusive em seus processos de comunicação ao público em geral associados ao Open Finance, garantida a uniformidade da experiência dos clientes e prevenindo o surgimento de dúvidas ou insegurança durante o compartilhamento de dados e serviços.

4.2 Estrutura do Guia de Experiência do Cliente

O Guia deve ser estruturado de modo claro e coeso, a fim de que seja interpretado adequadamente pelas partes interessadas. Adicionalmente, o Guia deve conter telas de exemplo que ilustrem as etapas das jornadas de compartilhamento de dados e serviços pelo cliente.

Por sua vez, os dispositivos do Guia devem ser classificados em, no mínimo:

I - requisitos: disposições que devem ser seguidas obrigatoriamente pelas instituições participantes; e

II - recomendações: disposições de observação não obrigatória pelas instituições participantes, mas cuja implementação é recomendável, considerando boas práticas para a experiência do cliente.

A esse respeito, o Guia deve conter requisitos e recomendações aplicáveis às diversas situações de compartilhamento de dados e serviços, abrangendo, no mínimo:

I - compartilhamento de dados e serviços por pessoas naturais;

II - compartilhamento de dados e serviços por pessoas jurídicas;

III - compartilhamento de dados e serviços por pessoas naturais titulares de contas conjuntas em que seja exigido o consentimento de mais de um titular da conta;

IV - compartilhamento de dados e serviços por pessoas jurídicas em que seja exigido o consentimento de mais de um representante ou procurador da empresa; e

V - ambiente de gestão de consentimentos concedidos por parte de pessoas naturais e jurídicas nas instituições participantes.

Brasília, 13 de junho de 2025.
