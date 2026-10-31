---
titulo: "INSTRUÇÃO NORMATIVA SEORI/SG-MD Nº 1, DE 8 DE JANEIRO DE 2024"
orgao: "Ministério da Defesa/Secretaria de Orçamento e Organização Institucional"
tipo: "Instrução Normativa"
numero: "1"
data: 2024-01-08
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 12/01/2024, seção 1, p. 9"
data_publicacao: 2024-01-12
edicao: "9"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-seori/sg-md-n-1-de-8-de-janeiro-de-2024-537038850"
sha256_html_fonte: 8a8c6f3ec54d884dc85106dc479f20da6ff1493b2708598d096b520b0d82afb4
baixado_em: 2026-10-16
---
# INSTRUÇÃO NORMATIVA SEORI/SG-MD Nº 1, DE 8 DE JANEIRO DE 2024

INSTRUÇÃO NORMATIVA SEORI/SG-MD Nº 1, DE 8 DE JANEIRO DE 2024

Estabelece a política de backup de dados corporativos e restauração de dados digitais no âmbito da administração central do Ministério da Defesa.

O SECRETÁRIO DE ORÇAMENTO E ORGANIZAÇÃO INSTITUCIONAL DO MINISTÉRIO DA DEFESA, no uso das atribuições que lhe confere o art. 37, incisos X, XI e XIII, do Anexo I do Decreto nº 11.337, de 1º de janeiro 2023, e de acordo com o que consta do Processo Administrativo nº 60586.000188/2022-06, resolve:

**Art. 1º** Esta Instrução Normativa estabelece a política de backup de dados corporativos e restauração de dados digitais no âmbito da administração central do Ministério da Defesa, na forma do Anexo.

**Art. 2º** O disposto nesta Instrução Normativa tem a finalidade de preservar a disponibilidade, a integridade, a confidencialidade e a autenticidade das informações, por determinado período, frente a perdas, incidentes cibernéticos ou alterações não autorizadas em dados ou sistemas.

**Art. 3º** As regras contidas nesta Instrução Normativa se aplicam a todos os usuários dos recursos computacionais da rede de dados administrada pelo Departamento de Tecnologia da Informação e Comunicação da administração central do Ministério da Defesa que, de forma direta ou indireta, fazem uso dos recursos de backup, compreendendo:

I - servidores;

II - militares;

III - convidados e usuários externos que façam uso dos recursos computacionais da rede;

IV - ocupantes de postos de trabalho terceirizados, inclusive prestadores eventuais de serviço; e

V - estagiários.

**Art. 4º** Esta Instrução Normativa entra em vigor em 1º de fevereiro de 2024.

JOSÉ ROBERTO FERNANDES JÚNIOR

## ANEXO

POLÍTICA DE BACKUP E RESTAURAÇÃO DE DADOS DIGITAIS

Histórico de versões

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Data</p></td>      <td rowspan="1" colspan="1"><p>Versão</p></td>      <td rowspan="1" colspan="1"><p>Descrição</p></td>      <td rowspan="1" colspan="1"><p>Autor</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>25/08/2023</p></td>      <td rowspan="1" colspan="1"><p>1.0</p></td>      <td rowspan="1" colspan="1"><p>Primeira versão da Política de backup e restauração de dados digitais</p></td>      <td rowspan="1" colspan="1"><p>CGINF</p></td>     </tr>    </tbody>   </table>

(Tabela 1)

Histórico de revisão

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>ID da versão</p></td>      <td rowspan="1" colspan="1"><p>Data da Mudança</p></td>      <td rowspan="1" colspan="1"><p>Autor</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>     </tr>    </tbody>   </table>

(Tabela 2)

1\. INTRODUÇÃO

1.1. No contexto da transformação digital do Estado brasileiro, o Governo Federal publicou a Estratégia de Governo Digital, por meio do Decreto nº 10.332, de 29 de abril de 2020, iniciativa que se encontra em plena execução. Ela norteia as ações de todos os órgãos federais, com o objetivo de transformar o governo pela digitalização dos serviços, oferecendo políticas públicas e serviços de melhor qualidade, mais simples, acessíveis de qualquer lugar e a um custo menor para o cidadão.

1.2. Hoje, mais do que em qualquer outro momento da história, o Governo utiliza a tecnologia para melhorar e expandir a oferta de serviços públicos para o cidadão apoiado em sistemas informatizados.

1.3. Nesse contexto, os órgãos federais, com infraestrutura própria ou contratada de terceiros, coletam, recebem, acessam, processam, modificam, produzem, extraem, validam, armazenam, distribuem e transmitem informações confidenciais e públicas para apoiar a entrega de produtos e serviços essenciais como, por exemplo:

1.3.1. fornecimento de serviços financeiros;

1.3.2. fornecimento de serviços de emissões guias, certificados e carteiras;

1.3.3. processamento de autorizações de segurança ou dados de saúde;

1.3.4. fornecimento de serviços em nuvem;

1.3.5. desenvolvendo comunicações via cabo, wireless e/ou satélites; e

1.3.6. sistemas militares de defesa.

1.4. As informações federais são frequentemente compartilhadas, obedecidos os requisitos legais, com entidades como governos estaduais e municipais, empresas públicas e privadas, faculdades e universidades, organizações de pesquisa independentes ou públicas e organizações do terceiro setor.

1.5. A proteção dessas informações pelo Governo, enquanto agente responsável pelo tratamento de dados, decorre do art. 46 da Lei nº 13.709, de 14 de agosto de 2018 - Lei Geral de Proteção de Dados Pessoais (LGPD):

"Art. 46. Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito."

1.6. A não observância de tal normativo pode impactar diretamente a capacidade do Governo Federal em cumprir suas missões precípuas de promover uma gestão pública eficiente, ampliar o acesso à cidadania, estimular uma economia brasileira crescentemente digitalizada, dinâmica, produtiva e competitiva e, em última instancia, impedir a geração de valor público para o cidadão.

2\. PROPÓSITO

2.1. A Política de Backup e Restauração de Dados Digitais da administração central do Ministério da Defesa objetiva instituir diretrizes, responsabilidades e competências que visam à segurança, proteção e disponibilidade dos dados digitais custodiados pelo Departamento de Tecnologia da Informação e Comunicação, definidos formalmente como obrigatória salvaguarda dos dados para garantir a continuidade do negócio.

2.2. É fundamental estabelecer mecanismos que permitam a guarda dos dados e sua eventual restauração, em casos de indisponibilidades, ou perdas por erro humano, ataques, catástrofes naturais ou outras ameaças. O presente conjunto de procedimentos estabelece o modo e a periodicidade do backup armazenados pelos sistemas computacionais.

3\. ESCOPO

3.1. Em atendimento ao art.12, item I, da Instrução Normativa nº 01 GSI/PR, de 13 de junho de 2008, esta política se aplica a todos os dados no âmbito da administração central do Ministério da Defesa. Neste contexto, incluem documentos pessoais e institucionais em formato digital, e-mail, arquivos pessoais e compartilhados, bancos de dados, sistemas internos e conteúdo web.

3.2. Os serviços e sistemas críticos de TI da administração central do Ministério da Defesa devem ser formalmente elencados pela Comitê de Governança Digital - CGD (ou comitê equivalente).

3.3. Os serviços de infraestrutura e sistemas de informação elencadas no Anexo I, bem como a definição de suas criticidades serão revisados em caso de necessidade ou anualmente a partir da data da sua publicação.

3.4. Esta política se aplica a colaboradores, servidores, militares, ocupantes de cargos e funções de livre provimento e exoneração, terceirizados, estagiários, prestadores de serviço e aos que, de forma direta ou indireta, são usuários ou criadores de dados de propriedade do Ministério da Defesa e salvaguardados por backup.

3.5. A salvaguarda dos dados digitais de serviços e sistemas de TI que utilizam computação em nuvem (pública ou privada) deve ser garantida nos acordos ou contratos que formalizam a relação entre as partes.

3.6. Deverão ser feitas cópias de segurança dos seguintes serviços de infraestrutura:

a) Serviços de diretório;

b) Serviços de compartilhamento de arquivos;

c) Serviços de e-mail;

d) Serviços e sistemas de gerenciamento de banco de dados;

e) Serviços de segurança da informação;

f) Serviços de suporte às aplicações; e

g) Outros serviços essenciais.

3.7. Não serão feitas cópias dos dados armazenados localmente, nos microcomputadores dos usuários ou em quaisquer outros dispositivos fora dos centros de processamento de dados mantidos pelo Departamento de Tecnologia da Informação e Comunicação, ficando sobre a responsabilidade do indivíduo que usa o(s) dispositivo(s) a salvaguarda destes dados.

4\. CONCEITOS E DEFINIÇÕES

a) Administrador de Backup - responsável pelo planejamento de soluções de backup, definição de padrões, configurações, resolução de incidentes e problemas e operação técnica dos ativos e serviços de TI voltados ao serviço de backup;

b) Ativo Crítico - equipamento físico, unidade de armazenamento e dados que possuem elevada importância para a continuidade das atividades e serviços voltados à concretização dos objetivos do órgão;

c) Backup ou Cópia de Segurança - Conjunto de procedimentos que permitem salvaguardar os dados de um sistema computacional, garantindo retenção, proteção e recuperação, sempre com a fidelidade ao dado original assegurada. Esse termo também é utilizado para identificar a mídia em que a cópia é realizada;

d) Backup Completo - modalidade em que todos os dados a serem salvaguardados são copiados integralmente (cópia de segurança completa) para uma unidade de armazenamento, independentemente de terem sido ou não alterados desde o último backup;

e) Backup Incremental - modalidade em que são preservados apenas dados novos ou modificados desde o backup anterior, podendo esse ter sido realizado em qualquer modalidade;

f) Backup Diferencial - modalidade em que são salvaguardados apenas dados novos ou modificados desde o último backup completo efetuado;

g) Backup Sintético - modalidade em que combina backup completo com os incrementais ou diferenciais subsequentes, criando uma cópia de segurança consolidada que inclui todas as alterações desde o último backup completo, permitindo restaurações mais rápidas e eficientes;

h) Backup Forever - modalidade em que se realiza um backup completo inicial, seguido da configuração de backups incrementais, de forma contínua, para sempre;

i) Custodiante da Informação - qualquer indivíduo ou unidade administrativa de órgão ou entidade da Administração Pública Federal, direta e indireta, que tenha responsabilidade formal de proteger a informação e aplicar os níveis de controles de segurança em conformidade com as exigências de Segurança da Informação comunicadas pelo proprietário da informação;

j) Descarte - eliminação correta e controlada de informações, documentos, mídias e acervos digitais;

k) Disponibilidade - conceito ao qual se assegura que a informação esteja acessível e utilizável, sob demanda, por uma pessoa física ou determinado sistema, órgão ou entidade devidamente autorizados;

l) Eliminação - Exclusão de dado ou conjunto de dados armazenados em banco de dados, independentemente do procedimento empregado;

m) Mídia - base física ou tecnologia empregada para que dados possam ser armazenados, incluindo discos ópticos, magnéticos, CDs, fitas e papel, entre outros. Um recurso multimídia combina sons, imagens e vídeos;

n) Infraestrutura Crítica - instalações, serviços, bens e sistemas, virtuais ou físicos, que se forem incapacitados, destruídos ou tiverem desempenho extremamente degradado, provocarão sério impacto ao órgão, além de repercussão social, econômica, política, internacional ou na segurança;

o) Imagem de Backup - arquivo que contém os dados salvaguardados, gerado pela própria solução de backup, não necessariamente no formato original dos arquivos originais;

p) Recovery Point Objective (RPO) - ponto no tempo em que os dados dos serviços de TI devem ser recuperados após uma situação de parada ou perda, correspondendo ao prazo máximo em que se admite perder dados no caso de um incidente;

q) Recovery Time Objective (RTO) - tempo estimado para restaurar os dados e tornar os serviços de TI novamente operacionais, correspondendo ao prazo máximo em que se admite manter os serviços de TI inoperantes até a restauração de seus dados, após um incidente;

r) Restauração - processo de recuperação e disponibilização de dados salvaguardados em determinada imagem de backup;

s) Retenção - período de tempo no qual os dados devem ser salvaguardados e estar aptos à restauração;

t) Retenção em Disco - período de tempo no qual os dados devem ser mantidos em disco;

u) Retenção em Fita - período de tempo no qual os dados devem ser preservados em fita;

v) Objetos de Backup - qualquer informação que pode ser salvaguardada;

w) Rotina de Backup - procedimento utilizado para se realizar um backup;

x) Serviços de Tecnologia da Informação - provimento de serviços de desenvolvimento, de implantação, de manutenção, de armazenamento e de recuperação de dados e de operação de sistemas de informação, projeto de infraestrutura de redes de comunicação de dados, modelagem de processos e assessoramento técnico necessários à gestão da informação;

y) Serviços de Infraestrutura - conjunto de equipamentos e sistemas tecnológicos necessários para que os usuários finais possam interagir com as soluções de tecnologia da informação;

z) Unidade de Armazenamento - dispositivo para armazenamento de dados em suporte digital; e

aa) Unidade de Armazenamento de Cópia de Segurança - unidade de armazenamento com características específicas para retenção de cópia de segurança de dados digitais.

5\. DIRETRIZES GERAIS

5.1. Dos Princípios Gerais

5.1.1. A Política de Backup deve estar alinhada à Política de Segurança da Informação da administração central do Ministério da Defesa.

5.1.2. A Política de Backup deve estar alinhada com a Política de gestão de continuidade de negócios em nível organizacional, quando disponível.

5.1.3. As rotinas de backup devem ser orientadas para a restauração dos dados no menor tempo possível, principalmente quando da indisponibilidade de serviços de TI.

5.1.4. As rotinas de backup devem utilizar soluções próprias e especializadas para este fim, preferencialmente de forma automatizada.

5.1.5. As rotinas de backup devem possuir requisitos mínimos diferenciados de acordo com o tipo de serviço de TI ou dado salvaguardado, dando prioridade aos serviços de TI críticos da organização.

5.1.6. O armazenamento do backup, deve ser realizado em local distinto da infraestrutura crítica e da sede do órgão, para armazenamento extra das principais cópias de segurança, tendo como exemplo os dados de serviços críticos.

5.1.7. A infraestrutura da rede de backup deve ser apartada, de forma lógica e física, dos sistemas críticos da organização.

5.1.8. Dever ser mantida a reserva de recursos (físicos e lógicos) de infraestrutura, para realização de teste e restauração de backup.

5.1.9. Em situações em que a confidencialidade seja importante, convém proteger as cópias de segurança por meio de uso de mecanismos de criptografia.

5.2. Da frequência, retenção e testes de recuperação

5.2.1. A Tabela 3 apresenta a classificação dos sistemas, dados, arquivos e serviços, chamados de objetos de backup e abrangidos pela política de backup, sendo do menor para o maior, cuja classificação 0 (zero) possui a maior prioridade e a 4 (quatro) com a menor prioridade.

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Classificação</p></td>      <td rowspan="1" colspan="1"><p>Prioridade</p></td>      <td rowspan="1" colspan="1"><p>RPO</p></td>      <td rowspan="1" colspan="1"><p>Retenção em Stage</p></td>      <td rowspan="1" colspan="1"><p>Retenção em Fita</p></td>      <td rowspan="1" colspan="1"><p>Teste de Restore</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>0</p></td>      <td rowspan="1" colspan="1"><p>Crítico</p></td>      <td rowspan="1" colspan="1"><p>1h</p></td>      <td rowspan="1" colspan="1"><p>1 ano</p></td>      <td rowspan="1" colspan="1"><p>5 anos</p></td>      <td rowspan="1" colspan="1"><p>1 mês</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>1</p></td>      <td rowspan="1" colspan="1"><p>Alto</p></td>      <td rowspan="1" colspan="1"><p>12h</p></td>      <td rowspan="1" colspan="1"><p>3 meses</p></td>      <td rowspan="1" colspan="1"><p>1 ano</p></td>      <td rowspan="1" colspan="1"><p>3 meses</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>2</p></td>      <td rowspan="1" colspan="1"><p>Médio</p></td>      <td rowspan="1" colspan="1"><p>24h</p></td>      <td rowspan="1" colspan="1"><p>1 mês</p></td>      <td rowspan="1" colspan="1"><p>1 ano</p></td>      <td rowspan="1" colspan="1"><p>6 meses</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>3</p></td>      <td rowspan="1" colspan="1"><p>Baixo</p></td>      <td rowspan="1" colspan="1"><p>120h</p></td>      <td rowspan="1" colspan="1"><p>1 mês</p></td>      <td rowspan="1" colspan="1"><p>1 ano</p></td>      <td rowspan="1" colspan="1"><p>6 meses</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>4</p></td>      <td rowspan="1" colspan="1"><p>Legado</p></td>      <td rowspan="1" colspan="1"><p>N/A</p></td>      <td rowspan="1" colspan="1"><p>N/A</p></td>      <td rowspan="1" colspan="1"><p>1 ano</p></td>      <td rowspan="1" colspan="1"><p>N/A</p></td>     </tr>    </tbody>   </table>

(Tabela 3)

5.2.2. Classificação 0 - Crítico

a) Objetos de backup com prioridade crítica cuja indisponibilidade podem causar prejuízos para todo o Ministério;

b) Deverão ser realizados testes de recuperação (restore) para 100% dos objetos de backup com prioridade crítica; e

c) A classificação de objetos de backup com nível (0 - Crítico) deverá ser aprovada pelo Comitê de Governança Digital - CGD (ou equivalente).

5.2.3. Classificação 1 - Alto

a) Objetos de backup com prioridade alta cuja indisponibilidade podem causar prejuízos para parte do Ministério;

b) Deverão ser realizados testes de recuperação (restore) para 50% dos objetos de backup com prioridade alta; e

c) A classificação de objetos de backup com nível (1 - Alto) deverá ser aprovada pelo Diretor da Departamento de Tecnologia da Informação e Comunicação.

5.2.4. Classificação 2 - Médio

a) Objetos de backup com prioridade média cuja indisponibilidade podem causar prejuízos para parte do Ministério;

b) Deverão ser realizados testes de recuperação (restore) para 25% dos objetos de backup com prioridade média; e

c) A classificação de objetos de backup com nível (2 - Médio) deverá ser aprovada pelo Diretor do Departamento de Tecnologia da Informação e Comunicação.

5.2.5. Classificação 3 - Baixo

a) Objetos de backup com prioridade baixa cuja indisponibilidade podem causar pouco ou nenhum prejuízo para o Ministério;

b) Deverão ser realizados testes de recuperação (restore) para 10% dos objetos de backup com prioridade média; e

c) A classificação de objetos de backup com nível (3 - Baixo) deverá ser solicitada pelo gestor do objeto de backup, sendo essa a classificação padrão caso não seja solicitado.

5.2.6. Classificação 4 - Legado

a) Objetos de backup com prioridade legada cuja indisponibilidade não causam prejuízo para o Ministério;

b) Não serão feitos testes de recuperação (restore); e

c) Deverão ser solicitados pelo gestor do objeto de backup.

5.2.7. A solicitação de salvaguarda dos dados referentes aos objetos de backup, deve ser realizada pelo custodiante técnico do serviço ou do sistema de informação, com a anuência prévia e formal da Coordenação-Geral de Infraestrutura e Serviços (CGINF) e aprovada pela autoridade competente, refletindo os requisitos de negócio da organização, bem como os requisitos de segurança da informação e proteção de dados envolvidos e a criticidade da informação para a continuidade da operação da organização.

5.2.8. Os responsáveis pelos dados, devem ter ciência do tempo de retenção estabelecido para cada tipo de informação e os administradores de backup deverão zelar pelo cumprimento das diretrizes estabelecidas.

5.3. Da modalidade de backup

a) Completo (full);

b) Incremental;

c) Diferencial;

d) Sintético; e

e) Forever.

5.4. Do Uso da Rede de Dados

5.4.1. O administrador de backup deve considerar o impacto da execução das rotinas sobre o desempenho da rede de dados do Ministério da Defesa, garantindo que o tráfego necessário às suas atividades não ocasione indisponibilidade dos demais serviços de TI.

5.4.2. A execução das rotinas de backup deve se concentrar, preferencialmente, no período da janela de tempo previamente definido, minimizando o impacto no desempenho da rede de comunicação da administração central do Ministério da Defesa ou, ainda, evitar uma possível indisponibilidade de algum ativo necessário para execução de backup específico.

5.4.3. O período da janela de tempo para executar as rotinas deve ser determinado pelo administrador de backup, conforme acordo estabelecido com área técnica responsável pela administração da rede de dados.

5.5. Do transporte e armazenamento

5.5.1. As unidades de armazenamento utilizadas na salvaguarda dos dados digitais devem considerar as seguintes características dos dados resguardados:

a) A criticidade do dado salvaguardado;

b) O tempo de retenção do dado;

c) A probabilidade de necessidade de restauração;

d) O tempo esperado para restauração;

e) O custo de aquisição da unidade de armazenamento de backup; e

f) A vida útil da unidade de armazenamento de backup.

5.5.2. O administrador de backup deve identificar a viabilidade de utilização de diferentes tecnologias na realização das cópias de segurança, propondo a melhor solução para cada caso.

5.5.3. Poderão ser utilizadas técnicas de compressão de dados, contanto que o acréscimo no tempo de restauração dos dados seja considerado aceitável pelos gestores das informações.

5.5.4. A execução das rotinas de backup deve envolver a previsão de ampliação da capacidade dos dispositivos envolvidos no armazenamento.

5.5.5. As unidades de armazenamento e demais hardwares (servidor de backup, robô de backup, discos, etc.) do Sistema de Backup estão acondicionadas no Centro de Processamento de Dados (CPD) do Departamento de Tecnologia da Informação e Comunicação, com controle de fatores ambientais sensíveis como umidade, temperatura, poeira e pressão, e com acesso restrito às pessoas autorizadas pela Coordenação-Geral de Infraestrutura e Serviços.

5.5.6. Em casos de necessidade de descarte de unidades de armazenamento de backups, tais mídias devem ser fisicamente destruídas de forma a inutilizá-las, atentando-se à legislação vigente quanto ao descarte sustentável e ambientalmente correto.

5.5.7. As mídias de backup serão transportadas e armazenadas conforme descrito a seguir:

a) A mídia magnética (cartucho) deverá ser claramente identificada e armazenada em uma área segura, acessível apenas para a equipe de administração e operação do sistema de backup e pessoa(s) autorizada(s);

b) A mídia não deverá ser desguarnecida de supervisão durante o transporte; e

c) As mídias magnéticas armazenadas em local seguro, em área externa ao Departamento de Tecnologia da Informação e Comunicação, poderão ser transportadas para o CPD do Departamento após o término do prazo de retenção para reuso ou descarte, ou para restauração dos dados salvaguardados.

5.6. Dos testes de restauração (restore)

5.6.1. Os arquivos de backup serão verificados periodicamente.

5.6.2. Diariamente os logs de backup serão revisados em busca de erros, durações anormais e em busca de oportunidades para melhorar o desempenho do backup.

5.6.3. Ações corretivas serão tomadas quando os problemas de backup forem identificados, a fim de reduzir os riscos associados às possíveis falhas.

5.6.4. A equipe de administração de backup manterá os registros de backups e testes de restauração para demonstrar conformidade com esta política.

5.6.5. Os testes devem ser realizados em ambientes distintos, abrangendo ambientes de virtualização e sub-redes, para correta execução do backup.

5.6.6. Os serviços críticos deverão ser testados integralmente. Os testes de restauração para os serviços não críticos devem ser realizados por amostragem, a fim de verificar o funcionamento, segurança e eficiência do sistema.

5.6.7. Os acordos de serviço de backup formalizados devem estar em conformidade, tais como RPO e tempo de retenção.

5.6.8. Os registros dos testes deverão conter, no mínimo, o tipo de sistema e ou serviço que teve o seu reestabelecimento testado, a data da realização do teste, o tempo gasto para o retorno do backup e se o procedimento foi concluído com sucesso.

5.7. Dos procedimentos para inclusão de objetos de backup na política

5.7.1. O formulário para inclusão dos objetos de backup está presente no ANEXO II.

5.7.2. O atendimento de solicitações de inclusão de objetos de backup no Departamento de Tecnologia da Informação e Comunicação deve ser realizado conforme abaixo:

5.7.2.1. O responsável pelo ativo ou o gestor técnico pode solicitar a inclusão no sistema de backup. Esta solicitação deve ser feita utilizando o Sistema de Registros de Chamados do Departamento de Tecnologia da Informação e Comunicação ou e-mail.

5.7.2.2. O documento deverá conter as seguintes informações:

a) Dados do responsável (nome completo, ramal, e -mail, setor e vínculo); e

b) Dados do sistema (IP, nome descrição, severidade e justificativa).

5.8. Dos procedimentos para restauração de objetos de backup na política

5.8.1. O atendimento das solicitações de restauração de objetos de backup deverá obedecer às seguintes orientações:

a) A solicitação de restauração de objetos deverá sempre partir do responsável pelo recurso, através de chamado utilizando o Sistema de Registros de Chamados;

b) A restauração de objetos somente será possível nos casos em que este tenha sido atingido pela estratégia de backup definida na política; e

c) O operador de backup terá a prerrogativa de negar a restauração de dados cujo conteúdo não seja condizente com a atividade institucional, cabendo recurso da negativa ao gestor da unidade do demandante.

5.9. Do cronograma para restauração dos objetos de backup na política

5.9.1. O tempo de restauração, preferencialmente definido em Acordo de Nível de Serviço (SLA) entre as áreas de negócio e o Departamento de Tecnologia da Informação e Comunicação, é proporcional ao volume de dados necessários para a restauração.

5.9.2. A restauração de backup é realizada pela equipe de administração de backup da Coordenação de Banco de Dados.

5.10. Dos procedimentos para alteração da severidade dos objetos de backup na política

5.10.1. O formulário para alteração da severidade dos objetos de backup está presente no ANEXO II.

5.10.2. O atendimento de solicitações deve ser realizado conforme abaixo:

5.10.3. O responsável pelo ativo ou o gestor técnico pode solicitar a alteração no sistema de backup. Esta solicitação deve ser feita utilizando o Sistema de Registros de Chamados do Departamento de Tecnologia da Informação e Comunicação ou e-mail.

5.10.4. O documento deverá conter as seguintes informações:

a) Dados do responsável (nome completo, ramal, e-mail, setor e vínculo); e

b) Dados do sistema (IP, nome e justificativa).

5.11. Dos procedimentos para exclusão de objetos de backup

5.11.1. O formulário para exclusão da severidade dos objetos de backup está presente no ANEXO II.

5.11.2. O atendimento de solicitações deve ser realizado conforme abaixo:

5.11.2.1. O responsável pelo ativo ou o gestor técnico pode solicitar a alteração no sistema de backup. Esta solicitação deve ser feita utilizando o Sistema de Registros de Chamados do Departamento de Tecnologia da Informação e Comunicação ou e-mail.

5.11.2.2. O documento deverá conter as seguintes informações:

a) Dados do responsável (nome completo, ramal, e-mail, setor e vínculo); e

b) Dados do sistema (IP, nome, descrição, severidade e justificativa).

5.12. Do Descarte da Mídia de Backup

5.12.1. A mídia de backup será retirada e descartada conforme descrito neste documento:

a) A equipe de operação do Sistema de Backup será a responsável em efetuar o descarte seguro de toda mídia de backup destinada a este fim. Ela garantirá que a mídia não contém mais imagens e arquivos válidos passíveis de serem recuperados por terceiros em hipótese alguma;

b) A equipe de operação do Sistema de Backup garantirá a destruição física da mídia antes do seu descarte em definitivo; e

c) Após a inutilização física da mídia de backup e a certeza de que não há mais a possibilidade de conserto ou recuperação dos dados, a equipe de operação entregará todo o equipamento inutilizado a área administrativa do Departamento de Tecnologia da Informação e Comunicação responsável pelo descarte seguro sem agredir o meio ambiente e as leis ambientais.

5.13. Das Responsabilidades

5.13.1. O administrador de backup e o operador de backup devem ser capacitados para as tecnologias, procedimentos e soluções utilizadas no sistema de backup;

5.13.2. São atribuições e responsabilidades do administrador do sistema de backup:

a) Configurar e administrar o software de backup;

b) Definir procedimentos de criação e restauração das rotinas de backup, a criticidade, escalabilidade e prioridade dos Jobs de backup;

c) Acompanhar as soluções de sistemas de backup de ponta do mercado e propor melhorias para atendimento das necessidades do Departamento de Tecnologia da Informação e Comunicação;

d) Solicitar, sempre que necessário, treinamentos e atualizações técnicas para operação do sistema de backup; e

e) Responder, caso solicitado por instâncias superiores, sobre o serviço de backup, funcionalidades da ferramenta de backup e futuras necessidades a fim de que os serviço e sistemas se mantenham com alta disponibilidade.

5.13.3. São atribuições e responsabilidades do operador do sistema de backup:

a) Criar, testar e implantar as rotinas de backups;

b) Efetuar periodicamente as rotinas de testes de backup com o objetivo de verificar e manter o funcionamento;

c) Criar, etiquetar, gerenciar e manter a guarda das mídias magnéticas em local próprio e seguro, seguindo as condições físicas e ambientais explicitadas pelo fabricante dos equipamentos;

d) Fazer a troca das mídias de backup no robô de backup substituindo as mídias com armazenamento esgotado, defeituosas ou inservíveis;

e) Mídias magnéticas inservíveis ou defeituosas devem ser inutilizadas em definitivo e descartadas após a certeza de que os dados inseridos não são possíveis de restauradas por terceiros;

f) Executar, programar a execução e restaurar as rotinas de backups;

g) Verificar diariamente o funcionamento do ambiente, se for o caso, criar relatórios e verificar os logs de execução dos backups no software de backup; e

h) Executar rotinas de testes do sistema de backup e restauração dos backups em disco e mídias magnéticas.

5.14. Não conformidade

5.14.1. Em caso de violação desta política poderão ser aplicadas sanções previstas na Lei 8.112/1990 e outras legislações cabíveis aos agentes públicos civis e militares.

6\. ANEXOS

ANEXO I - Serviços de infraestrutura e sistemas de informação considerados na política de backup; e

ANEXO II - Formulários de inclusão, restauração, alteração e exclusão de objetos de backup.

## ANEXO I — SERVIÇOS DE INFRAESTRUTURA E SISTEMAS DE INFORMAÇÃO CONSIDERADOS NA POLÍTICA DE BACKUP

Nível de prioridade dos serviços de infraestrutura

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Item</p></td>      <td rowspan="1" colspan="1"><p>Sistema</p></td>      <td rowspan="1" colspan="1"><p>Descrição do sistema</p></td>      <td rowspan="1" colspan="1"><p>Severidade do Serviço</p></td>      <td rowspan="1" colspan="1"><p>Setor Responsável</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>1</p></td>      <td rowspan="1" colspan="1"><p>Correio MD</p></td>      <td rowspan="1" colspan="1"><p>Aplicação servidora de e<em>-</em>mails</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COINS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>2</p></td>      <td rowspan="1" colspan="1"><p>Serviço de Diretório</p></td>      <td rowspan="1" colspan="1"><p>AD, DNS e DHCP</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COINS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>3</p></td>      <td rowspan="1" colspan="1"><p>Serviço de Arquivo</p></td>      <td rowspan="1" colspan="1"><p>Servidor de Arquivos</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COINS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>4</p></td>      <td rowspan="1" colspan="1"><p>Nagios (NOC)</p></td>      <td rowspan="1" colspan="1"><p>Sistema de Monitoramento de Rede</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COINS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>5</p></td>      <td rowspan="1" colspan="1"><p>AADS Server</p></td>      <td rowspan="1" colspan="1"><p>Sistema de Gerenciamento de Terminais</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>6</p></td>      <td rowspan="1" colspan="1"><p>DNS TELEBRAS</p></td>      <td rowspan="1" colspan="1"><p>DNS Autoritativo TELEBRAS</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>7</p></td>      <td rowspan="1" colspan="1"><p>DNS RNP</p></td>      <td rowspan="1" colspan="1"><p>DNS Autoritativo RNP</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>8</p></td>      <td rowspan="1" colspan="1"><p>ePO</p></td>      <td rowspan="1" colspan="1"><p>Sistema de Gerenciamento de Segurança</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>9</p></td>      <td rowspan="1" colspan="1"><p>Gerência do IPS</p></td>      <td rowspan="1" colspan="1"><p>Sistema de Prevenção de Intrusão</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>10</p></td>      <td rowspan="1" colspan="1"><p>Gerenciador DNS</p></td>      <td rowspan="1" colspan="1"><p>Gerenciador DNS</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>11</p></td>      <td rowspan="1" colspan="1"><p>Logs DLP</p></td>      <td rowspan="1" colspan="1"><p>Prevenção de Perda de Dados</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>12</p></td>      <td rowspan="1" colspan="1"><p>MX</p></td>      <td rowspan="1" colspan="1"><p>MX</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>13</p></td>      <td rowspan="1" colspan="1"><p>ProxyInterno</p></td>      <td rowspan="1" colspan="1"><p>ProxyInterno</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>14</p></td>      <td rowspan="1" colspan="1"><p>ProxyExterno</p></td>      <td rowspan="1" colspan="1"><p>ProxyExterno</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>15</p></td>      <td rowspan="1" colspan="1"><p>Proxy Reverso</p></td>      <td rowspan="1" colspan="1"><p>ProxyReverso</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>16</p></td>      <td rowspan="1" colspan="1"><p>Tanable</p></td>      <td rowspan="1" colspan="1"><p>Tenable Network Security</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>17</p></td>      <td rowspan="1" colspan="1"><p>TIE-MAR</p></td>      <td rowspan="1" colspan="1"><p>Tenable Network Security</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>18</p></td>      <td rowspan="1" colspan="1"><p>Splunk</p></td>      <td rowspan="1" colspan="1"><p>Sistema de Gerenciamento de Logs/Eventos</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>NUSIC</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>19</p></td>      <td rowspan="1" colspan="1"><p>ArcserveUDP</p></td>      <td rowspan="1" colspan="1"><p>Sistema Unificado de Proteção de Dados</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COBDA</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>20</p></td>      <td rowspan="1" colspan="1"><p>OEM</p></td>      <td rowspan="1" colspan="1"><p>OracleEnterpriseManager</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COBDA</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>21</p></td>      <td rowspan="1" colspan="1"><p>PowerDesigner</p></td>      <td rowspan="1" colspan="1"><p>Plataforma de Gerenciamento de Metadados de Modelagem e Design</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COBDA</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>22</p></td>      <td rowspan="1" colspan="1"><p>NFS Backup</p></td>      <td rowspan="1" colspan="1"><p>Repositório de backup</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COBDA</p></td>     </tr>    </tbody>   </table>

(Anexo I - Tabela I)

Nível de prioridade dos sistemas de informação

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Item</p></td>      <td rowspan="1" colspan="1"><p>Sistema</p></td>      <td rowspan="1" colspan="1"><p>Descrição do sistema</p></td>      <td rowspan="1" colspan="1"><p>Severidade do Serviço</p></td>      <td rowspan="1" colspan="1"><p>Setor Responsável</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>1</p></td>      <td rowspan="1" colspan="1"><p>SUPERBR</p></td>      <td rowspan="1" colspan="1"><p>Sistema oficial de gestão de documentos e processos administrativos eletrônicos do Governo Federal</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DESEG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>2</p></td>      <td rowspan="1" colspan="1"><p>SGED</p></td>      <td rowspan="1" colspan="1"><p>Sistema de Gestão Eletrônica de Documentos</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DESEG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>3</p></td>      <td rowspan="1" colspan="1"><p>BIEG BOX</p></td>      <td rowspan="1" colspan="1"><p>Nuvem privada do MD</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COINS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>4</p></td>      <td rowspan="1" colspan="1"><p>ProjetoRondon</p></td>      <td rowspan="1" colspan="1"><p>Sistema Projeto Rondon</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEPESD/DPS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>5</p></td>      <td rowspan="1" colspan="1"><p>Intranet</p></td>      <td rowspan="1" colspan="1"><p>Portal de informações internas aos usuários do MD</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>GM/ASCOM</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>6</p></td>      <td rowspan="1" colspan="1"><p>MDLegis</p></td>      <td rowspan="1" colspan="1"><p>Sistema para pesquisas de legislações relativa ao Ministério da Defesa</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DEORG/DILEG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>7</p></td>      <td rowspan="1" colspan="1"><p>TI Ajudo (GLPI)</p></td>      <td rowspan="1" colspan="1"><p>TI Ajudo - Sistema de suporte de TI</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>CGSIS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>8</p></td>      <td rowspan="1" colspan="1"><p>SIRHU</p></td>      <td rowspan="1" colspan="1"><p>Sistema que realiza o cadastramento de funcionários do Ministério da Defesa</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DEADI/COGEPES</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>9</p></td>      <td rowspan="1" colspan="1"><p>Eficiente</p></td>      <td rowspan="1" colspan="1"><p>Sistema para controle de Ordem de serviço - Contrato Interagi/ASCOM</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>GM/ASCOM</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>10</p></td>      <td rowspan="1" colspan="1"><p>Proposta</p></td>      <td rowspan="1" colspan="1"><p>Gerenciar o cadastro dos proponentes para as medalhas da Vitória e OMD</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>GM/ASCER</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>11</p></td>      <td rowspan="1" colspan="1"><p>Ultrasistec</p></td>      <td rowspan="1" colspan="1"><p>Sistema de controle de acesso das catracas do MD</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DESEG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>12</p></td>      <td rowspan="1" colspan="1"><p>EAD</p></td>      <td rowspan="1" colspan="1"><p>Plataforma de educação a distância do Ministério da Defesa</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DEADI/COGEPES</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>13</p></td>      <td rowspan="1" colspan="1"><p>SisAtleta</p></td>      <td rowspan="1" colspan="1"><p>Sistemas de cadastro de atletas e eventos esportivos militares</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEPESD/DDM/CDMB</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>14</p></td>      <td rowspan="1" colspan="1"><p>Portal MD</p></td>      <td rowspan="1" colspan="1"><p>Portal de informações externas</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>CGSIS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>15</p></td>      <td rowspan="1" colspan="1"><p>PGMD</p></td>      <td rowspan="1" colspan="1"><p>Programa de Gestão</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DEADI/COGEPES</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>16</p></td>      <td rowspan="1" colspan="1"><p>MDLIST</p></td>      <td rowspan="1" colspan="1"><p>Sistema informativo por meio de mensagem eletrônica</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>CISET/GEORI</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>17</p></td>      <td rowspan="1" colspan="1"><p>BDAnistia</p></td>      <td rowspan="1" colspan="1"><p>Sistema para cadastro, controle e acompanhamento, no âmbito do Departamento de Organização e Legislação (DEORG) das informações relativas aos Anistiados</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEPESD/DEPES</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>18</p></td>      <td rowspan="1" colspan="1"><p>LoginMD</p></td>      <td rowspan="1" colspan="1"><p>Subsistema que controla e permite o cadastro e gerenciamento de usuário da maioria dos sistemas desenvolvidos pela CGSIS</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DETIC/CGSIS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>19</p></td>      <td rowspan="1" colspan="1"><p>Representação</p></td>      <td rowspan="1" colspan="1"><p>Informações alusivas às representações institucionais da administração central do MD</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DEORG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>20</p></td>      <td rowspan="1" colspan="1"><p>LimeSurvey</p></td>      <td rowspan="1" colspan="1"><p>Aplicação de questionários com perguntas e respostas online para pesquisas de opinião</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>CGSIS</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>21</p></td>      <td rowspan="1" colspan="1"><p>Imprensa</p></td>      <td rowspan="1" colspan="1"><p>Informações de declarações à imprensa</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>GM/ASCOM</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>22</p></td>      <td rowspan="1" colspan="1"><p>SisCovel</p></td>      <td rowspan="1" colspan="1"><p>Sistema de controle de solicitação de viaturas do MD</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEORI/DESEG/GESEP/COSER</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>23</p></td>      <td rowspan="1" colspan="1"><p>SISPROD</p></td>      <td rowspan="1" colspan="1"><p>Sistema de gerenciamento de banco de dados de Exportação de Produtos de Defesa</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>SEPROD/DEPCOM</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>24</p></td>      <td rowspan="1" colspan="1"><p>SISCLATEN - PROD</p></td>      <td rowspan="1" colspan="1"><p>Ferramenta<em>web</em>que permite às entidades especializadas públicas e privadas solicitarem a autorização de projetos para realizarem a atividade de aerolevantamento no território nacional</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>CHELOG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>25</p></td>      <td rowspan="1" colspan="1"><p>OSMDEFESA</p></td>      <td rowspan="1" colspan="1"><p>OpenStreetMap</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>CHELOG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>26</p></td>      <td rowspan="1" colspan="1"><p>Apolo-interop</p></td>      <td rowspan="1" colspan="1"><p>Sistema de Informações Gerenciais de Logística e Mobilização de Defesa - SIGLMD. (Sistema APOLO)</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>CHELOG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>27</p></td>      <td rowspan="1" colspan="1"><p>Apolo-proxy</p></td>      <td rowspan="1" colspan="1"><p>Sistema de Informações Gerenciais de Logística e Mobilização de Defesa - SIGLMD. (Sistema APOLO)</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>CHELOG</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>28</p></td>      <td rowspan="1" colspan="1"><p>MDBOX</p></td>      <td rowspan="1" colspan="1"><p>Nuvem privada do MD</p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p>COINS</p></td>     </tr>    </tbody>   </table>

(Anexo I - Tabela II)

## ANEXO II — Formulário para inclusão de objetos de backup

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="10"><p>IDENTIFICAÇÃO DO RESPONSÁVEL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="3"><p></p><p>Nome completo:</p><p></p></td>      <td rowspan="1" colspan="3"><p></p><p>Ramal:</p><p></p></td>      <td rowspan="1" colspan="3"><p></p><p>E-mail:</p><p></p></td>      <td rowspan="1" colspan="1"><p></p><p>Setor:</p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="10"><p>Vínculo:</p><p>( ) Servidor civil ( ) Servidor militar</p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="9"><p>IDENTIFICAÇÃO / CLASSIFICAÇÃO DO SISTEMA</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IP</p></td>      <td rowspan="1" colspan="1"><p>Nome</p></td>      <td rowspan="1" colspan="2"><p>Descrição</p></td>      <td rowspan="1" colspan="5"><p>Severidade</p></td>      <td rowspan="1" colspan="1"><p>Justificativa</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="2"></td>      <td rowspan="1" colspan="1"><p>Crítico</p></td>      <td rowspan="1" colspan="1"><p>Alto</p></td>      <td rowspan="1" colspan="1"><p>Médio</p></td>      <td rowspan="1" colspan="1"><p>Baixo</p></td>      <td rowspan="1" colspan="1"><p>Legado</p></td>      <td rowspan="1" colspan="1"></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="2"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="2"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>     </tr>    </tbody>   </table>

(Anexo II - Tabela I)

Formulário para restauração de objetos de backup

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="4"><p>IDENTIFICAÇÃO DO RESPONSÁVEL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>Nome completo:</p></td>      <td rowspan="1" colspan="1"><p>Ramal:</p></td>      <td rowspan="1" colspan="1"><p>E-mail:</p></td>      <td rowspan="1" colspan="1"><p>Setor:</p></td>     </tr>     <tr>      <td rowspan="1" colspan="4"><p>Vínculo:</p><p>( ) Servidor civil ( ) Servidor militar</p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="4"><p>INFORMAÇÕES SOBRE OS OBJETOS DE BACKUP</p></td>     </tr>     <tr>      <td rowspan="1" colspan="4"><p>TIPO DE RESTAURAÇÃO:</p><p>( ) Arquivos ( ) Banco de dados (BD)</p><p>( ) Pasta completa (incluindo arquivos) ( ) Servidor virtual (VM)</p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="4"><p>NOME DA BASE, SERVIDOR VIRTUAL OU CAMINHO COMPLETO DO ARQUIVO OU PASTA (Ex.: S:\dir1\dir2\arquivo):</p><p></p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="4"><p>DATA/HORA DA INFORMAÇÃO A SER RECUPERADA:</p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="4"><p>ONDE RESTAURAR:</p><p>( ) No mesmo local de origem dos dados (Importante ressaltar que SOBRESCREVERÁ os arquivos atuais)</p><p>( ) Em um local diferente? ESPECIFIQUE:</p></td>     </tr>     <tr>      <td rowspan="1" colspan="4"><p>MOTIVOS DA SOLICITAÇÃO</p><p></p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="4"><p>INSTRUÇÕES PARA SOLICITAÇÃO</p><p>Preencher este formulário com todas as informações solicitadas e enviar pelo Sistema de Registro de Chamados ou por enviar para a Coordenação de Banco de Dados COBDA (cobda@defesa.gov.br), solicitando a abertura do chamado.</p></td>     </tr>    </tbody>   </table>

(Anexo II - Tabela II)

Formulário para alteração da severidade de objetos de backup

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="10"><p>IDENTIFICAÇÃO DO RESPONSÁVEL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="3"><p></p><p>Nome completo:</p><p></p></td>      <td rowspan="1" colspan="3"><p></p><p>Ramal:</p><p></p></td>      <td rowspan="1" colspan="3"><p></p><p>E-mail:</p><p></p></td>      <td rowspan="1" colspan="1"><p></p><p>Setor:</p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="10"><p>Vínculo:</p><p>( ) Servidor civil ( ) Servidor militar</p><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="9"><p>IDENTIFICAÇÃO / CLASSIFICAÇÃO DO SISTEMA</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IP</p></td>      <td rowspan="1" colspan="1"><p>Nome</p></td>      <td rowspan="1" colspan="2"><p>Descrição</p></td>      <td rowspan="1" colspan="5"><p>Severidade</p></td>      <td rowspan="1" colspan="1"><p>Justificativa</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="2"></td>      <td rowspan="1" colspan="1"><p>Crítico</p></td>      <td rowspan="1" colspan="1"><p>Alto</p></td>      <td rowspan="1" colspan="1"><p>Médio</p></td>      <td rowspan="1" colspan="1"><p>Baixo</p></td>      <td rowspan="1" colspan="1"><p>Legado</p></td>      <td rowspan="1" colspan="1"></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="2"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="2"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="1"><p></p></td>     </tr>    </tbody>   </table>

(Anexo II - Tabela III)

Formulário para exclusão de objetos de backup

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="5"><p>IDENTIFICAÇÃO DO RESPONSÁVEL</p></td>     </tr>     <tr>      <td rowspan="1" colspan="2"><p>Nome:</p><p></p></td>      <td rowspan="1" colspan="1"><p>Ramal:</p></td>      <td rowspan="1" colspan="1"><p>E-mail:</p></td>      <td rowspan="1" colspan="1"><p>Setor:</p></td>     </tr>     <tr>      <td rowspan="1" colspan="5"><p>Vínculo:</p><p>( ) Servidor civil ( ) Servidor militar</p></td>     </tr>     <tr>      <td rowspan="1" colspan="5"><p>IDENTIFICAÇÃO / CLASSIFICAÇÃO DO SISTEMA</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>IP</p></td>      <td rowspan="1" colspan="2"><p>Nome</p></td>      <td rowspan="1" colspan="2"><p>Justificativa</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p></p></td>      <td rowspan="1" colspan="2"><p></p></td>      <td rowspan="1" colspan="2"><p></p></td>     </tr>     <tr>      <td rowspan="1" colspan="5"><p>POR QUANTO TEMPO OS DADOS DEVEM FICAR ARMAZENADOS:</p><p></p></td>     </tr>    </tbody>   </table>

(Anexo II - Tabela IV)
