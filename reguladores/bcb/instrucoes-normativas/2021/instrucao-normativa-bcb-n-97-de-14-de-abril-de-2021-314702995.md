---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 97, DE 14 DE ABRIL DE 2021"
orgao: "Ministério da Economia/Banco Central do Brasil/Àrea de Regulação/Departamento de Regulação do Sistema Financeiro"
tipo: "Instrução Normativa"
numero: "97"
data: 2021-04-14
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 19/04/2021, seção 1, p. 60"
data_publicacao: 2021-04-19
edicao: "72"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-97-de-14-de-abril-de-2021-314702995"
sha256_html_fonte: 3bbeecc84c2703c95bf730fce1127f6f6408a67d7817b8c862f649b913e17ab9
baixado_em: 2026-10-21
---
# INSTRUÇÃO NORMATIVA BCB Nº 97, DE 14 DE ABRIL DE 2021

INSTRUÇÃO NORMATIVA BCB Nº 97, DE 14 DE ABRIL DE 2021

Divulga a versão 1.0 do Manual de Experiência do Cliente no Open Banking.

Os Chefes do Departamento de Regulação do Sistema Financeiro (Denor) e do Departamento de Tecnologia da Informação (Deinf), no uso das atribuições que lhes conferem os arts. 23, inciso I, alínea "a", e 62, inciso IV, e 116, inciso I, alínea "b", do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, com base no art. 3º, inciso V, da Resolução BCB nº 32, de 29 de outubro de 2020, resolvem:

**Art. 1º** Esta Instrução Normativa divulga a versão 1.0 do Manual de Experiência do Cliente no Open Banking, de observância obrigatória por parte das instituições participantes, conforme Anexo.

**Parágrafo único.** O manual de que trata o caput, em sua versão mais recente, estará acessível na página do Open Banking no sítio eletrônico do Banco Central do Brasil na internet e no Portal do Open Banking no Brasil, mantido pela Estrutura Responsável pela Governança do Open Banking de que trata o art. 44, § 1º, da Resolução Conjunta nº 1, de 4 de maio de 2020.

**Art. 2º** Esta Instrução Normativa entra em vigor na data de sua publicação.

HAROLDO JAYME MARTINS FROES CRUZ

Chefe do Departamento de Tecnologia da Informação

JOÃO ANDRÉ CALVINO MARQUES PEREIRA

Chefe do Departamento de Regulação do Sistema Financeiro

## ANEXO

Manual de Experiência do Cliente no Open Banking Versão 1.0

Histórico de revisão

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p><strong>Data</strong></p></td>      <td rowspan="1" colspan="1"><p>Versão</p></td>      <td rowspan="1" colspan="1"><p>Descrição das alterações</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>14/4/2021</p></td>      <td rowspan="1" colspan="1"><p>1.0</p></td>      <td rowspan="1" colspan="1"><p>Versão inicial.</p></td>     </tr>    </tbody>   </table>

Termos de Uso

Este manual define os princípios básicos da experiência do cliente no Open Banking, complementando a regulamentação vigente sobre o tema.

O manual será revisto e atualizado periodicamente a fim de preservar a compatibilidade com a regulamentação, bem como para incorporar os aprimoramentos decorrentes da evolução do Open Banking.

Informações mais detalhadas e exemplos da aplicação deste manual poderão ser encontradas no Portal do Open Banking no Brasil, na Área do Desenvolvedor.

Sugestões, críticas ou pedidos de esclarecimento de dúvidas relativas ao conteúdo deste documento podem ser enviados ao Banco Central do Brasil por meio dos canais institucionais dessa autarquia.

Referências

Estas especificações baseiam-se, referenciam e complementam, quando aplicável, os seguintes documentos:

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Referência</p></td>      <td rowspan="1" colspan="1"><p>Origem</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução Conjunta nº 1, de 2020</p></td>      <td rowspan="1" colspan="1"><p>https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20Conjunta&amp;numero=1  </p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução BCB nº 32, de 2020</p></td>      <td rowspan="1" colspan="1"><p>https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&amp;numero=32</p></td>     </tr>    </tbody>   </table>

1\. Introdução

Este Manual foi elaborado com o objetivo de garantir que a experiência dos clientes ao compartilharem dados entre as instituições participantes do ambiente do Open Banking seja segura, ágil, precisa e conveniente. Os consumidores de produtos e serviços financeiros somente terão confiança para autorizar o compartilhamento de dados se a sua experiência for condizente com as suas expectativas e se as informações a respeito do processo lhes forem apresentadas de maneira clara e intuitiva, permitindo que seu consentimento para compartilhamento de dados seja inequívoco. Para que isso aconteça, é essencial que a jornada de compartilhamento ocorra em um ambiente seguro, com o mínimo de fricções possíveis.

Este manual estabelece diretrizes e princípios elementares para a experiência do cliente no Open Banking. Informações adicionais, inclusive o Guia de Experiência do Cliente de que trata a seção 3 deste manual, poderão ser encontradas no Portal do Open Banking no Brasil.

Ao longo deste manual algumas expressões serão frequentemente utilizadas, dentre as quais:

I - jornada simples de compartilhamento de dados: sequência de etapas do compartilhamento de dados realizada por um único cliente;

II - jornada múltipla de compartilhamento de dados: sequência de etapas do compartilhamento de dados quando realizada por mais de um cliente, a exemplo de contas de pessoas jurídicas em que o compartilhamento de dados dependa do consentimento de mais de um representante ou procurador da empresa;

III - aprovação do compartilhamento: ação executada pelos clientes da jornada múltipla que não iniciaram a jornada para autorizar o compartilhamento de dados; e

IV - ambiente de gestão de consentimentos: ambiente disponibilizado pelas instituições transmissoras e receptoras em seus canais eletrônicos para que os clientes consultem e gerenciem os consentimentos já efetivados ou pendentes, inclusive para fins de sua revogação.

Ressalta-se que as mencionadas expressões não devem ser necessariamente empregadas durante as etapas da solicitação de compartilhamento, mas como termos que se aplicam apenas a este manual com o objetivo de facilitar a sua compreensão.

2\. Princípios da Experiência do Cliente no Open Banking

Tendo por base as disposições da Resolução Conjunta nº 1, de 2020, consideram-se como Princípios da Experiência do Cliente no Open Banking:

I - a segurança e a privacidade;

II- a agilidade;

III - a conveniência e o controle; e

IV - a transparência.

2.1 Segurança e Privacidade

O compartilhamento de dados no Open Banking deve ser realizado em um ambiente seguro, que garanta a privacidade dos dados pessoais dos clientes, com observância da legislação e da regulamentação vigentes que tratam de segurança e privacidade de dados pessoais.

Durante a jornada do compartilhamento, os clientes devem ser adequadamente informados sobre a segurança do processo para que se sintam seguros ao consentir o compartilhamento de seus dados cadastrais e transacionais.

2.2 Agilidade

O processo de compartilhamento de dados no Open Banking deve ter duração compatível com os seus objetivos e nível de complexidade, assegurando as condições necessárias para a livre escolha e a tomada de decisão por parte dos clientes. Um processo desnecessariamente longo pode provocar a desistência do cliente, enquanto eventual precariedade na prestação de informações não permite uma tomada de decisão adequada.

O processo de compartilhamento de dados deve ocorrer de forma sucessiva e ininterrupta. Sendo assim, como regra geral, as diferentes etapas da solicitação de compartilhamento não devem ser interrompidas até a sua conclusão por parte de cada cliente. Nos casos de jornada múltipla de compartilhamento de dados, a confirmação do compartilhamento somente ocorrerá após a finalização do processo por todas os clientes envolvidos no compartilhamento, que não precisarão fazê-lo de forma simultânea ou imediata, contudo de forma que seja garantida a segurança e a transparência do processo, inclusive no que diz respeito aos prazos necessários para a sua conclusão.

2.3 Conveniência e controle

O compartilhamento de dados no Open Banking deve ser realizado para finalidades específicas e de forma conveniente e acessível ao cliente, inclusive no que diz respeito aos canais de acesso nas instituições participantes. Deverão ser asseguradas ao cliente as condições necessárias para o exercício do controle dos seus dados pessoais compartilhados no Open Banking. Nesse sentido, a jornada de compartilhamento deve ser centrada no cliente, tendo em vista o seu perfil, as suas necessidades, os seus objetivos e expectativas, com a disponibilização de informações e ambientes de gestão de consentimentos, inclusive para a revogação do consentimento quando entender oportuno e apropriado, respeitados os prazos definidos na regulamentação vigente.

2.4 Transparência

Os clientes devem receber informações claras, objetivas e adequadas durante o processo de compartilhamento de dados. Espera-se que o cliente seja informado com clareza e de forma tempestiva sobre quais dados serão compartilhados e os motivos pelos quais esses dados serão necessários para as finalidades em questão, além de outras informações obrigatórias previstas na regulamentação vigente.

Informações desnecessárias ou excessivamente complexas podem gerar dúvidas e inseguranças ao cliente, que poderá desisitir do compartilhamento por falta de compreensão do processo. Assim, as informações fornecidas aos clientes devem ser suficientes e precisas para que sua tomada de decisão seja inequívoca. A linguagem utilizada deve ser simples e compreensível, independentemente do nível de conhecimento prévio sobre produtos e serviços financeiros.

3\. Guia de Experiência do Cliente

Conforme a Resolução BCB nº 32, de 2020, a Estrutura Responsável pela Governança do Open Banking de que trata o art. 44, § 1º, da Resolução Conjunta nº 1, de 2020, deverá disponibilizar às instituições participantes do Open Banking e ao público em geral o Guia de Experiência do Cliente, que congregará procedimentos operacionais e requisitos que deverão ser observados por todas as instituições participantes na interação com clientes durante a jornada do compartilhamento, observados o disposto neste manual e na regulamentação vigente sobre o Open Banking. A disponibilização desse documento, em sua versão mais atual, deverá ser realizada por meio do Portal do Open Banking no Brasil

O Guia deverá ser revisado e atualizado periodicamente pela Estrutura Responsável pela Governança do Open Banking, que deverá manter controle transparente das versões publicadas. A publicação de novas versões do documento deve ser precedida e acompanhada de testes de usabilidade com clientes representativos do público-alvo do Open Banking, bem como de comunicação tempestiva às instituições participantes e ao Banco Central do Brasil, que poderá determinar ajustes e correções.

Admite-se que o Guia estabeleça princípios e requisitos adicionais aos constantes neste manual. No entanto, o conteúdo do Guia de Experiência do Cliente deve estar em conformidade com o disposto na legislação e na regulamentação vigentes.

3.1 Conteúdo do Guia de Experiência do Cliente

O Guia de Experiência do Cliente deverá dispor sobre, no mínimo:

3.1.1 O fluxo e o conteúdo das etapas da jornada simples de compartilhamento de dados, abrangendo, no mínimo:

3.1.1.1 A identificação do cliente

Nessa etapa, a instituição receptora de dados deve identificar o cliente, conforme exigido pela regulamentação vigente.

3.1.1.2 As finalidades determinadas do consentimento

Nessa etapa, a instituição receptora de dados deve prestar informações ao cliente acerca do(s) serviço(s) associados ao processo de compartilhamento de dados.

3.1.1.3 A seleção dos dados objeto de compartilhamento na instituição receptora de dados

Nessa etapa, o cliente deve poder selecionar os dados que deseja compartilhar, observando os agrupamentos de dados definidos com base no art. 11 da Resolução Conjunta nº 1, de 2020.

O cliente deve ser informado sobre quais dados são necessários para a finalidade do compartilhamento e quais seriam opcionais, conforme o caso. O cliente deve ser informado sobre porque esses dados são necessários para a(s) finalidade(s) em questão.

3.1.1.4 A seleção do prazo de compartilhamento de dados

Nessa etapa, o cliente deve poder selecionar o prazo pelo qual deseja compartilhar os dados selecionados, observada a finalidade os os prazos máximos estabelecidos no art. 10 da Resolução Conjunta nº 1, de 2020.

3.1.1.5 A seleção da instituição transmissora de dados

Nessa etapa, o cliente deve poder selecionar a instituição transmissora dos dados. Deve ser disponibilizado mecanismo de busca que propicie uma seleção ágil e clara da instituição desejada. Devem estar disponíveis para seleção todas as instituições participantes para fins de compartilhamento de dados no Open Banking devidamente registradas no Diretório de Participantes mantido pela estrutura de governança do Open Banking.

3.1.1.6 O redirecionamento para o ambiente da instituição transmissora de dados

Nessa etapa, o cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição transmissora de dados selecionada. Deve ficar claro para o cliente que o compartilhamento ainda não está concluído e que mais etapas são necessárias para a sua efetivação. O redirecionamento deve ser feito, preferencialmente, para o mesmo tipo de canal eletrônico que está sendo utilizado pelo cliente na instituição receptora (e.g. app-to-app, browser-to-browser).

3.1.1.7 A autenticação do cliente na instituição transmissora de dados

essa etapa, o cliente deve se autenticar na instituição transmissora de dados. O cliente deve poder reconhecer que está no ambiente da instituição com a qual já mantém relacionamento e que os seus dados utilizados para autenticação não estão visíveis e não serão compartilhados com a instituição receptora dos dados.

Conforme estabelece a Resolução Conjunta nº 1, de 2020, os procedimentos e controles para autenticação do cliente devem ser compatíveis com os aplicáveis ao acesso aos canais de atendimento eletrônicos já disponibilizados pela instituição transmissora e que essa compatibilidade abrange os fatores de autenticação, a quantidade de etapas e a duração do procedimento.

3.1.1.8 A confirmação de compartilhamento pelo cliente na instituição transmissora de dados

Nessa etapa, o cliente deve confirmar o compartilhamento na instituição transmissora de dados. Deve ser apresentado ao cliente para conferência, no mínimo, a identificação da instituição receptora de dados, o período de validade do consentimento e os dados que serão objeto de compartilhamento.

3.1.1.9 O redirecionamento para o ambiente da instituição receptora de dados

Nessa etapa, o cliente deve ser informado que está sendo redirecionado de forma segura para o ambiente da instituição receptora de dados, responsável por comunicar ao cliente a efetivação da solicitação de compartilhamento.

3.1.2 O fluxo das etapas da jornada múltipla de compartilhamento de dados

O Guia deve estabelecer parâmetros para a experiência de clientes em jornada múltipla de compartilhamento de dados, quando for o caso.

Nesse caso, todos os clientes envolvidos no compartilhamento devem ser informados com clareza sobre os procedimentos e as etapas necessárias para a efetivação do compartilhamento. Adicionalmente, os clientes devem ser notificados pela instituição transmissora sobre a necessidade de ação para efetivação do compartilhamento de dados iniciada por outro cliente.

Em particular, o Guia deve dispor, quando for o caso, sobre os prazos máximos para ação dos demais clientes, que deverão ser aplicados de maneira uniforme por todas as instituições participantes. Ademais, o Guia deve estabelecer parâmetros para os casos em que um ou mais clientes não autorizem o compartilhamento abrangendo, no mínimo, a notificação aos demais clientes e a comunicação à instituição receptora.

3.1.3 Ambiente de gestão dos consentimentos

O Guia deve estabelecer requisitos para o ambiente de gestão de consentimentos das instituições participantes. No caso, referidas instituições devem disponibilizar em seu canal eletrônico um ambiente específico para a gestão dos compartilhamentos que estiveram envolvidas no âmbito do Open Banking.

Nesse ambiente, os clientes devem ter acesso de forma simples, ágil, precisa e conveniente a, no mínimo, informações sobre consentimentos vigentes ou que estejam pendentes de efetivação na jornada múltipla de que trata a seção 3.1.2, com a possibilidade de pesquisa com base em critérios definidos para observância homogênea por todas as instituições participantes.

Adicionalmente, os clientes devem ter acesso à possibilidade de consulta e revogação de consentimentos, com observância do disposto no art. 15 da Resolução Conjunta nº 1, de 2020. A efetivação de revogação deve ser precedida de tela de confirmação com informações sobre as consequências da ação.

3.1.4 A terminologia utilizada pelas instituições participantes durante a jornada do compartilhamento

O Guia deve padronizar a terminologia utilizada pelas instituições participantes na comunicação com os clientes durante a jornada de compartilhamento de dados.

Os termos e expressões utilizados neste manual e nos demais atos normativos editados pelo Banco Central podem ser subsitituídos por outros que sejam considerados mais adequados para a compreensão de todos os clientes do Open Banking, desde que os seus significados sejam mantidos.

A terminologia contida no Guia deve ser adotada por todas as instituições participantes, inclusive em seus processos de comunicação ao público em geral associadas ao Open Banking, garantida a uniformidade da experiência dos clientes e prevenindo o surgimento de dúvidas ou insegurança durante o compartilhamento de dados.

3.2 Estrutura do Guia de Experiência do Cliente

O Guia de Experiência do Cliente deve ser estruturado de maneira clara e coesa, de modo que seja interpretado adequadamente pelas partes interessadas. Adicionalmente, o Guia deve conter telas de exemplo que ilustrem as etapas das jornadas de compartilhamento de dados pelos clientes.

Por sua vez, os dispositivos do Guia devem ser classificados em, no mínimo:

I - requisitos: disposições que devem ser seguidas obrigatoriamente pelas instituições participantes; e

II - recomendações: disposições de observação não obrigatória pelas instituições participantes, mas recomendável, considerando boas práticas para a experiência do cliente.

A esse respeito, o Guia deve conter requisitos e recomendações aplicáveis às divesas situações de compartilhamento de dados, abrangendo, no mínimo:

I - compartilhamento de dados por pessoas naturais;

II - compartilhamento de dados por pessoas jurídicas;

III - compartilhamento de dados por pessoas naturais titulares de contas conjuntas em que seja exigida o consentimento de mais de um titular da conta;

IV - compartilhamento de dados por pessoas jurídicas em que seja exigida o consentimento de mais de um representante ou procurador da empresa; e

V - ambiente de gestão de consentimentos concedidos por parte de pessoas naturais e jurídicas nas instituições receptoras e transmissoras de dados.

Brasília, 14 de abril de 2021.
