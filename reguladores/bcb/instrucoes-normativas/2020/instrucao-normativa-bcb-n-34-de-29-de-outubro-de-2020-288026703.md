---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 34, DE 29 DE OUTUBRO DE 2020"
orgao: "Ministério da Economia/Banco Central do Brasil/Àrea de Regulação/Departamento de Regulação do Sistema Financeiro"
tipo: "Instrução Normativa"
numero: "34"
data: 2020-10-29
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 13/11/2020, seção 1, p. 50"
data_publicacao: 2020-11-13
edicao: "217"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-34-de-29-de-outubro-de-2020-288026703"
sha256_html_fonte: 06afd56c3108c3f5149cb70b74fb20f3ffd176c3d1cee098cf6768b135351fbe
baixado_em: 2026-10-21
---
# INSTRUÇÃO NORMATIVA BCB Nº 34, DE 29 DE OUTUBRO DE 2020

INSTRUÇÃO NORMATIVA BCB Nº 34, DE 29 DE OUTUBRO DE 2020

Divulga a versão 1.0 do Manual de APIs do Open Banking.

Os Chefes do Departamento de Regulação do Sistema Financeiro (Denor) e de Tecnologia da Informação (Deinf), no uso das atribuições que lhe conferem os arts. 23, inciso I, alínea "a", e 62, inciso IV, do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, com base no art. 3º, inciso II, da Resolução BCB nº 32, de 29 de outubro de 2020, resolvem:

**Art. 1º** Esta Instrução Normativa divulga a versão 1.0 do Manual de APIs do Open Banking, de observância obrigatória por parte das instituições participantes, conforme Anexo.

**Parágrafo único.** O manual de que trata o caput, em sua versão mais recente, estará acessível na página do Open Banking no sítio eletrônico do Banco Central do Brasil na internet.

**Art. 2º** Esta Instrução Normativa entra em vigor na data de sua publicação.

HAROLDO JAYME MARTINS FROES CRUZ

Chefe do Departamento de Tecnologia da Informação

JOÃO ANDRÉ CALVINO MARQUES PEREIRA

Chefe do Departamento de Regulação do Sistema Financeiro

## ANEXO

Manual de APIs do Open Banking Versão 1.0

Histórico de revisão

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Data</p></td>      <td rowspan="1" colspan="1"><p>Versão</p></td>      <td rowspan="1" colspan="1"><p>Descrição das alterações</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>29/10/2020</p></td>      <td rowspan="1" colspan="1"><p>1.0</p></td>      <td rowspan="1" colspan="1"><p>Versão inicial.</p></td>     </tr>    </tbody>   </table>

Apresentação

Este manual define as especificações das APIs necessárias ao compartilhamento de dados e serviços do escopo do Open Banking.

Ao longo deste documento, será constante o uso de siglas e terminologia específica para designar algumas expressões cotidianas dos profissionais da área de tecnologia. Alguns exemplos das mais frequentemente utilizadas, com as correspondentes definições, são as seguintes:

I - API (Application Programming Interface): um conjunto de definições sobre como um sistema pode acessar dados ou funcionalidades providos por um outro sistema;

II - REST (Representational State Transfer): estilo arquitetural de software;

III - API RESTful: API que adere às restrições do estilo arquitetural REST;

IV - OpenAPI: linguagem de especificação de APIs RESTful;

V - Endpoint: elemento de uma especificação OpenAPI sobre o qual podem ser executadas operações para acessar dados ou funcionalidades;

VI - HTTP (Hypertext Transfer Protocol): protocolo para sistemas hipermídia, distribuídos e colaborativos; e

VII - Operação: elemento de uma especificação OpenAPI que declara uma maneira válida de se acessar um endpoint, informando, por exemplo, qual método HTTP (GET, POST, etc.) utilizar, nomes e tipos de parâmetros, etc.

Termos de Uso

Este manual detalha os requisitos técnicos para a implementação dos elementos necessários à operacionalização do Open Banking, complementando a regulamentação vigente sobre o tema.

O manual será revisto e atualizado periodicamente a fim de preservar a compatibilidade com a regulamentação, bem como para incorporar os aprimoramentos decorrentes da evolução do Open Banking e da tecnologia.

Informações mais detalhadas e exemplos da aplicação deste manual poderão ser encontrados nos guias e tutoriais disponíveis no Portal do Open Banking Brasil, na Área do Desenvolvedor.

Sugestões, críticas ou pedidos de esclarecimento de dúvidas relativas ao conteúdo deste documento podem ser enviados ao Banco Central do Brasil por meio dos canais institucionais dessa autarquia.

Referências

Estas especificações baseiam-se, referenciam e complementam, quando aplicável, os seguintes documentos:

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Referência</p></td>      <td rowspan="1" colspan="1"><p>Origem</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução Conjunta nº 1, de 2020</p></td>      <td rowspan="1" colspan="1"><p>https://www.bcb.gov.br/estabilidadefinanceira/</p><p>exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20</p><p>Conjunta&amp;numero=1  </p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Resolução BCB nº 32, de 2020</p></td>      <td rowspan="1" colspan="1"><p>https://www.bcb.gov.br/estabilidadefinanceira/</p><p>exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20</p><p>BCB&amp;numero=32</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Hypertext Transfer Protocol - HTTP/1.1</p></td>      <td rowspan="1" colspan="1"><p>https://tools.ietf.org/html/rfc2616</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>ISO 20022</p></td>      <td rowspan="1" colspan="1"><p>https://www.iso20022.org/</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>OpenAPI Specification</p></td>      <td rowspan="1" colspan="1"><p>https://github.com/OAI/OpenAPI-Specification/blob/3.0.0/versions/3.0.0.md</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Representational State Transfer</p></td>      <td rowspan="1" colspan="1"><p>https://www.ics.uci.edu/~fielding/pubs/dissertation/</p><p>rest_arch_style.htm  </p></td>     </tr>    </tbody>   </table>

1\. Introdução

O Open Banking está intrinsecamente ligado às APIs, interfaces por meio das quais será possível interligar os diferentes sistemas das instituições. Ao serem disponibilizadas pelos participantes, as APIs precisam satisfazer condições tais como padronização, robustez e segurança, a fim de que o objetivo de compartilhamento de dados e serviços seja atendido a contento.

Nesse sentido, este manual visa a definir os principais aspectos relativos às especificações e implementações das APIs (Application Programming Interfaces) que integram o Open Banking no País, observando as disposições da Resolução Conjunta nº 1, de 4 de maio de 2020, e da Resolução BCB nº 32, de 29 de outubro de 2020.

São tratados neste documento aspectos como: formato para a troca de dados, desenho da interface, protocolo para transmissão de dados, versionamento, modelo de APIs e endpoints. Desse modo, o manual estabelece as diretrizes gerais sem esgotar todos os aspectos necessários à implementação das APIs para o Open Banking. As demais definições a cargo do mercado, por meio da estrutura responsável pela governança, nos termos da Circular nº 4.032, de 23 de junho de 2020, estarão disponíveis no Portal do Open Banking no Brasil, no qual poderão ser encontrados guias, tutoriais e outras informações operacionais sobre as APIs.

2\. APIs do Open Banking

A tabela abaixo exibe as APIs que integram o Open Banking. A coluna "Tipo" informa a classificação da API para fins de desempenho (ver a subseção "Desempenho" da seção "Requisitos Não Funcionais").

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Nome</p></td>      <td rowspan="1" colspan="1"><p>Descrição</p></td>      <td rowspan="1" colspan="1"><p>Tipo</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Produtos e Serviços</p></td>      <td rowspan="1" colspan="1"><p>Deve dar acesso a dados abertos relacionados a produtos e serviços oferecidos pelos participantes do Open Banking</p></td>      <td rowspan="1" colspan="1"><p>Média prioridade</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Canais de Atendimento</p></td>      <td rowspan="1" colspan="1"><p>Deve dar acesso a dados abertos relacionados aos canais de atendimento ao público oferecidos pelos participantes do Open Banking</p></td>      <td rowspan="1" colspan="1"><p>Média prioridade</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Situação do Ambiente</p></td>      <td rowspan="1" colspan="1"><p>Deve dar acesso a dados sobre a disponibilidade atual das implementações das APIs. Também deve dar acesso a dados sobre indisponibilidades programadas.</p></td>      <td rowspan="1" colspan="1"><p>Alta prioridade</p></td>     </tr>    </tbody>   </table>

3\. Princípios

Os princípios abaixo norteiam as especificações e implementações das APIs do Open Banking.

3.1 Experiência do usuário

As especificações e implementações das APIs devem oferecer uma boa experiência para os usuários, sejam eles implementadores ou consumidores das APIs.

3.2 Independência de tecnologia

As especificações das APIs devem ser independentes de tecnologia, podendo ser implementadas e consumidas em diferentes linguagens e/ou plataformas tais como Java, JavaScript, Python e Windows, Linux, Android e iOS.

3.3 Segurança

Procedimentos e controles (assinaturas digitais, criptografia, protocolos de autenticação e autorização, entre outros) devem ser adotados de forma a proteger os participantes do Open Banking, seus clientes, os consumidores das APIs e demais participantes do ecossistema, observada a compatibilidade com a política de segurança cibernética da instituição.

3.4 Extensibilidade

No futuro, as APIs poderão ser evoluídas para atender a novos casos de uso e, portanto, devem ser especificadas e implementadas de forma a permitir e facilitar extensões como, por exemplo, novos endpoints, operações, parâmetros e propriedades.

3.5 Padrões abertos

Padrões abertos devem ser adotados sempre que possível.

3.6 APIs RESTful

As especificações das APIs devem atender às restrições do estilo arquitetural REST sempre que possível.

3.7 ISO 20022

As respostas das APIs devem ter como base, sempre que possível, os elementos e componentes de mensagem ISO 20022 (https://www.iso20022.org/), os quais poderão ser modificados, caso necessário, para deixar as respostas mais simples e/ou atender às características locais, tal como implementado em diferentes jurisdições.

3.8 Declaração de obrigatoriedade

Todos os elementos que compõem as especificações das APIs (endpoints, operações, parâmetros, propriedades de respostas, etc.) devem ser explicitamente declarados como "Obrigatório", "Opcional" ou "Condicional", caso sejam obrigatórios apenas em certas condições.

4\. Definições e recomendações

As definições e recomendações abaixo devem ser observadas pelas especificações e implementações das APIs do Open Banking.

4.1 Especificações

As APIs devem ser especificadas com a versão 3.0.0 da linguagem OpenAPI (https://github.com/OAI/OpenAPI-Specification/blob/3.0.0/versions/3.0.0.md).

Implementações de exemplo das APIs devem ser disponibilizadas. Os dados retornados por elas não precisam ser dados reais e nem volumosos, pois o objetivo da disponibilização é dar ao Banco Central do Brasil, aos implementadores e aos consumidores das APIs mais um recurso para dirimir eventuais dúvidas acerca de suas especificações e implementações.

4.2 Versionamento

As versões das especificações das APIs serão tipificadas como "major", "minor", "patch" e "release candidate" de acordo com os critérios a seguir:

I - major - inclui novas características da implementação, mudanças, correções a serem incorporadas e que podem ser incompatíveis com versões anteriores, por exemplo, v1.0.0 e v2.0.0;

II - minor - pequenas mudanças nos elementos já existentes, com manutenção da compatibilidade com as versões até a major imediatamente anterior, por exemplo, v1.1.0 e v1.2.0;

III - patch - esclarecimentos às especificações minor, não incluem alterações funcionais, por exemplo, v1.1.1, v1.1.2; e

IV - release candidate - versões de pré-lançamento de qualquer versão futura do tipo patch, minor ou major, por exemplo, v1.0.0-rc e v1.0.0-rc2.

A estrutura responsável pela governança de que trata o art. 44, § 1º, da Resolução Conjunta nº 1, de 2020, poderá lançar novas versões dos tipos minor, patch e release candidate das APIs. Entretanto, versões do tipo major só poderão ser lançadas com a anuência do Banco Central do Brasil, o qual será responsável por definir o cronograma de implantação de versões major.

Por fim, credenciais de acesso associadas às APIs devem ser agnósticas às suas versões.

4.3 Portal do Open Banking no Brasil

O sítio eletrônico de que trata o art. 15 da Resolução BCB nº 32, de 2020, deverá conter definições e recomendações acessórias não presentes neste manual, bem como outros artefatos necessários à especificação, implementação e consumo das APIs do Open Banking. Todas as definições e recomendações acessórias e artefatos publicados no portal deverão estar em concordância com este e com os demais manuais do Open Banking

4.4 Cronograma

O Portal do Open Banking deverá listar as APIs em produção, suas versões atuais, datas em que entraram em produção e link para suas especificações. Também deverá apresentar o cronograma de homologação das APIs, indicando versão, data de divulgação, data prevista de entrada em produção e outras informações relevantes.

4.5 Definições acessórias

A Estrutura Responsável pela Governança do Open Banking deverá estabelecer e publicar no Portal do Open Banking um guia de estilo de especificações de APIs contendo definições e recomendações para os seguintes elementos:

I - estrutura de URIs (Uniform Resource Identifiers);

II - cabeçalhos HTTP;

III - códigos de status HTTP;

IV - convenções de corpo de requisições e respostas;

V - convenções de nomenclatura;

VI - tipos de dados comuns;

VII - paginação; e

VIII - estabilidade de identificadores.

4.6 Extensibilidade

As especificações das APIs do Open Banking podem não dar acesso a todos os dados e funcionalidades que um ou mais participantes desejam expor para os consumidores das APIs. Isso pode ser necessário para mais bem suportar casos de uso ou possibilitar inovações em produtos e serviços financeiros. Para atender estas e outras necessidades, é facultado aos participantes implementarem versões estendidas das APIs inteiramente compatíveis com as especificações padrões das APIs que são:

I - novos endpoints;

II - novas operações em endpoints pré-existentes;

III - novos parâmetros em operações pré-existentes, desde que opcionais; e

IV - novas propriedades em respostas pré-existentes.

A Estrutura Responsável pela Governança do Open Banking deverá publicar no Portal do Open Banking as definições e recomendações acessórias relacionadas às extensões das APIs.

Todas as extensões implementadas pelos participantes deverão estar listadas, com sua documentação referenciada, em seção específica no Portal do Open Banking e disponíveis para consumo, observadas as regras de ressarcimento de despesas previstas na regulamentação vigente.

5\. Requisitos não funcionais

Esta seção apresenta os requisitos não funcionais que as instituições participantes devem observar na implementação das APIs do Open Banking.

5.1 Limites de tráfego

As APIs deverão suportar, no mínimo:

I - 300 requisições por segundo globalmente, ou seja, independente do endereço IP (Internet Protocol) de onde provêm as requisições; e

II - 500 requisições por minuto originadas de um mesmo endereço IP.

As requisições que excederem os limites poderão ser enfileiradas ou recusadas, caso em que deverão ser respondidas com o código de status HTTP 429 (Too Many Requests).

Por fim, as requisições que ultrapassarem os limites deverão ser desprezadas no cálculo do tempo de resposta das implementações das APIs.

5.2 Desempenho

Deverá ser medido o tempo de resposta de cada requisição, ou seja, o tempo transcorrido entre o recebimento de uma requisição que não ultrapassa os limites de tráfego e o momento em que a requisição é completamente respondida. Adicionalmente, esta medição deverá ser feita de maneira que os tempos medidos sejam os mais próximos possíveis dos tempos de resposta experimentados por quem fez a requisição. Neste contexto, as APIs deverão manter o percentil 95 do tempo de resposta em no máximo:

I - 1000ms, caso sejam classificadas como APIs de alta prioridade;

II - 1500ms, caso sejam classificadas como APIs de média prioridade; e

III - 4000ms, caso sejam APIs administrativas.

Por exemplo, em um dia que uma API da alta prioridade receba 10.000 requisições, o tempo de resposta de pelo menos 9.500 requisições deve ser inferior a 1.000ms.

5.3 Disponibilidade

As APIs para compartilhamento de dados sobre canais de atendimento e produtos e serviços deverão satisfazer requisitos mínimos de disponibilidade. Cada um de seus endpoints deverá estar disponível:

I - 95% do tempo a cada 24 horas; e

II - 99,5% do tempo a cada 3 meses.

Há perspectiva de elevação dos requisitos mínimos de disponibilidade das APIs destinadas ao compartilhamento de outros dados e serviços do escopo do Open Banking, de forma a harmonizá-los com os dos sistemas de pagamentos críticos.

Brasília, 29 de outubro de 2020.
