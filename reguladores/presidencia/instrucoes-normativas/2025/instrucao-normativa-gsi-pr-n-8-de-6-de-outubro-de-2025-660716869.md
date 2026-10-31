---
titulo: "INSTRUÇÃO NORMATIVA GSI/PR Nº 8, DE 6 DE OUTUBRO DE 2025"
orgao: "Presidência da República/Gabinete de Segurança Institucional"
tipo: "Instrução Normativa"
numero: "8"
data: 2025-10-06
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 07/10/2025, seção 1, p. 1"
data_publicacao: 2025-10-07
edicao: "191"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-gsi/pr-n-8-de-6-de-outubro-de-2025-660716869"
baixado_em: 2026-10-16
sha256_html_fonte: c8246993251d01c118e90a2d147725ed54b62b8fcd5006f716212c9e1407f866
---
# INSTRUÇÃO NORMATIVA GSI/PR Nº 8, DE 6 DE OUTUBRO DE 2025

**INSTRUÇÃO NORMATIVA GSI/PR Nº 8, DE 6 DE OUTUBRO DE 2025**

Dispõe sobre os requisitos mínimos de segurança da informação para tratamento de informação classificada em computação em nuvem.

**O MINISTRO DE ESTADO CHEFE DO GABINETE DE SEGURANÇA INSTITUCIONAL DA PRESIDÊNCIA DA REPÚBLICA,**no uso das atribuições que lhe confere o art. 87, parágrafo único, inciso II, da Constituição, e tendo em vista o disposto na Lei nº 12.527, de 18 de novembro de 2011; no art. 8º,*caput*, incisos IV e V, da Lei nº 14.600, de 19 de junho de 2023; no art. 6º,*caput*, inciso I, do Decreto nº 7.845, de 14 de novembro de 2012; no art. 8º,*caput*, inciso II, do Decreto nº 12.572, de 4 de agosto de 2025; resolve:

**Art. 1º** Ficam dispostos os requisitos mínimos de segurança da informação para tratamento de informação classificada em computação em nuvem.

**Art. 2º** Para os fins desta Instrução Normativa, entende-se como nuvem para tratamento de informação classificada a infraestrutura de computação em nuvem privada ou comunitária gerida exclusivamente por órgãos de registro ou por empresas habilitadas como postos de controle.

#### CAPÍTULO I — DOS REQUISITOS PARA TRATAMENTO DE INFORMAÇÃO CLASSIFICADAEM COMPUTAÇÃO EM NUVEM

**Art. 3º** O tratamento de informação classificada em computação em nuvem deverá observar os seguintes requisitos, além dos previstos nos arts. 10 a 19 da Instrução Normativa GSI/PR nº 5, de 30 de agosto de 2021:

I - utilizar procedimentos de segmentação de rede, baseados em arquiteturas e técnicas adequadas ao ambiente computacional e aos riscos associados, para isolar os ambientes de processamento e armazenamento de informações classificadas;

II - utilizar tecnologias de virtualização com certificações de segurança que garantam o isolamento entre as máquinas virtuais alocadas a cada órgão de registro que utilize o serviço;

III - caso sejam utilizados contêineres, possuir mecanismos que possibilitem implementar controles de isolamento, além de ferramentas de segurança específicas para contêineres;

IV - criptografar todas as informações classificadas em grau de sigilo, tanto as arquivadas ou armazenadas quanto aquelas em transporte ou transmissão, utilizando-se algoritmos de Estado;

V - garantir que as chaves criptográficas sejam gerenciadas exclusivamente pelos órgãos de registro;

VI - implementar um processo de gestão de*backup*e recuperação de dados, realizando os*backups*criptografados em infraestrutura local, com garantia de recuperação em caso de desastre;

VII - exigir a utilização de autenticação multifatorial para todos os acessos aos sistemas que armazenam ou processam informações classificadas;

VIII - implementar políticas e controles de acesso que garantam que somente pessoal credenciado e com necessidade de conhecer poderá acessar as informações classificadas;

IX - realizar o registro detalhado e imutável de todos os acessos ao ambiente de nuvem para tratamento de informação classificada, especialmente, mas não limitado a, contas administrativas, contas de usuários, contas de aplicativos e contas de serviço, com auditorias periódicas conduzidas por equipe independente;

X - implementar mecanismos automatizados de alertas para atividades suspeitas;

XI - utilizar sistema centralizado de gestão de identidades, permissões e revogação de acessos com governança completa do ciclo de vida, desde a criação até a desativação, com o registro de todas as operações realizadas;

XII - implementar a gestão do controle de acesso, utilizando tanto o modelo de controle de acesso com base em papéis (*role-based access control*- RBAC) como o modelo de controle de acesso com base em atributos (*attribute-based access control*- ABAC), de acordo com a necessidade, com revisão, no mínimo, a cada seis meses; e

XIII - implementar controles técnicos e administrativos que impeçam o acesso do provedor de nuvem ao conteúdo das informações.

**Art. 4º** As informações classificadas em grau de sigilo reservado ou secreto e seus documentos preparatórios deverão ser transitados em redes localizadas exclusivamente em território nacional, preferencialmente em infraestruturas tecnológicas sob controle direto de órgãos da administração pública federal, direta e indireta, bem como de empresas públicas.

**§ 1º** É permitido o trânsito da informação de que trata o*caput*fora do território nacional, mediante uso de meios criptográficos compatíveis com o grau de sigilo, exclusivamente nas seguintes hipóteses:

I - comunicações com representantes diplomáticos, consulares ou de adidâncias de órgãos de registro; e

II - em demais missões oficiais, mediante autorização da alta administração do órgão de registro.

**§ 2º** O trânsito de dados de que trata o*caput*e o § 1º somente poderá ocorrer em redes que permitam, no mínimo, a aplicação de mecanismos de rastreabilidade, registro e monitoração integral de todos os pacotes de dados recebidos e enviados, e incluam, no mínimo, metadados de origem, destino, horário, tamanho e protocolo utilizado.

**§ 3º** A implementação dos mecanismos previstos no § 2º é de responsabilidade do provedor do serviço de nuvem, devendo estar prevista em contrato, garantindo-se o acesso irrestrito aos*logs*pela equipe de segurança do órgão de registro contratante.

**Art. 5º** As informações classificadas em grau de sigilo reservado ou secreto e seus documentos preparatórios deverão ser armazenados e processados em*datacenters*localizados exclusivamente em território nacional, preferencialmente em infraestruturas tecnológicas sob controle direto de órgãos da administração pública federal, direta e indireta, bem como de empresas públicas, observadas as disposições constantes dos tratados e convenções internacionais de que o Brasil seja signatário.

**Parágrafo único.** É vedada replicação ou*backup*das informações de que trata o*caput*fora do território nacional, bem como a execução de qualquer outra ação que resulte na saída de informações do território nacional.

**Art. 6º** As informações classificadas em grau de sigilo ultrassecreto e seus documentos preparatórios não poderão ser tratados em computação em nuvem.

#### CAPÍTULO II — DOS REQUISITOS MÍNIMOS PARA PROVEDOR DE SERVIÇO DE NUVEMPARA TRATAMENTO DE INFORMAÇÃO CLASSIFICADA

**Art. 7º** O provedor de serviço de nuvem para tratamento de informação classificada, além de observar os requisitos previstos nos arts. 10 e 11 do Decreto nº 7.845, de 14 de novembro de 2012, e no art. 20 da Instrução Normativa nº 5, de 30 de agosto de 2021, do Gabinete de Segurança Institucional da Presidência da República, deverá, no mínimo:

I - estar estabelecido no Brasil, ter situação cadastral ativa e ter como principal atividade econômica provimento de serviços de tecnologia da informação;

II - possuir certificação vigente nas seguintes normas:

a) ABNT NBR ISO/IEC 27001;

b) ABNT NBR ISO/IEC 27017;

c) ABNT NBR ISO/IEC 27018;

d) ABNT NBR ISO/IEC 27701; e

e) ABNT NBR ISO/IEC 22237;

III - demonstrar que todos os recursos físicos necessários, tais como servidores, equipamentos de armazenamento, equipamentos de rede e outros, estão localizados em*datacenters*em território nacional;

IV - disponibilizar infraestrutura física dedicada, sem compartilhamento com clientes ou entidades não autorizados pelo órgão de registro contratante;

V - disponibilizar infraestrutura projetada para alta disponibilidade, com redundância e planos de recuperação de desastres;

VI - possuir mecanismos capazes de implementar medidas para proteger os dados armazenados contra acessos não autorizados por parte de ameaças persistentes avançadas;

VII - demonstrar ser capaz de atender aos requisitos previstos no art. 3º; e

VIII - providenciar, junto ao órgão de registro contratante, o credenciamento de segurança de pessoas físicas com acesso à infraestrutura.

**Parágrafo único.** Auditoria técnica do órgão de registro contratante avaliará o cumprimento dos requisitos de que trata o*caput,*especialmente os previstos nos incisos III e VII.

**Art. 8º** O provedor de serviço de nuvem para tratamento de informação classificada deverá ser habilitado como órgão de registro ou posto de controle nos termos dos arts. 10 e 11 do Decreto nº 7.845, de 14 de novembro de 2012.

**Parágrafo único.** O Gabinete de Segurança Institucional da Presidência da República poderá realizar a habilitação de que trata o*caput*dos órgãos e entidades vinculados a outros Ministérios não habilitados como órgãos de registro nível 1, desde que haja anuência expressa do respectivo Ministro de Estado.

#### CAPÍTULO III — DAS RESPONSABILIDADES

**Art. 9º** Compete aos órgãos de registro contratantes de serviços de nuvem para tratamento de informação classificada, além dos requisitos previstos na Instrução Normativa GSI/PR nº 5, de 30 de agosto de 2021:

I - estabelecer contrato sigiloso para a prestação de serviços de nuvem para tratamento de informação classificada, nos termos do art. 48 do Decreto nº 7.845, de 14 de novembro de 2012, com expressa previsão de que a contratada deverá observar as disposições desta Instrução Normativa;

II - monitorar e auditar, no mínimo anualmente, o cumprimento das normas de segurança pelo provedor de serviço de nuvem para tratamento de informação classificada, com definição prévia de escopo técnico mínimo, periodicidade e critérios de conformidade;

III - realizar o credenciamento de segurança, conforme a legislação vigente, de todas as pessoas que tenham necessidade de acessar e operar a infraestrutura de nuvem para tratamento de informação classificada;

IV - capacitar periodicamente equipe de pessoal com acesso às informações classificadas, com conteúdo atualizado sobre proteção de dados, segurança da informação e incidentes cibernéticos;

V - apurar eventual infração nos casos de suspeita de descumprimento, por parte da contratada, de qualquer dispositivo do contrato previsto no inciso I ou das normas de segurança da informação classificada; e

VI - adotar imediatamente as ações necessárias nos casos de suspeita de comprometimento de segurança, o que poderá incluir a suspensão do acesso às informações armazenadas ou processadas pelo provedor.

**Art. 10.** Compete ao provedor de serviço em nuvem para tratamento de informação classificada:

I - garantir a conformidade com as normas e padrões de segurança estabelecidos nesta Instrução Normativa;

II - fornecer ao órgão de registro contratante relatório, no mínimo anual, sobre a segurança das informações classificadas sob sua guarda, contemplando, no mínimo, aspectos de segurança cibernética, segurança de rede, segurança de nuvem, segurança de aplicações e segurança de dados;

III - cooperar com as autoridades competentes em investigações relacionadas a incidentes de segurança;

IV - preservar e entregar os indícios e evidências relacionadas a incidentes de segurança, quando necessário à apuração de ilícitos penais, cíveis ou administrativos; e

V - impedir que pessoas não autorizadas pelo órgão de registro contratante tenham acesso aos recursos e instalações onde estão armazenadas as informações classificadas.

#### CAPÍTULO IV — DAS DISPOSIÇÕES FINAIS E TRANSITÓRIAS

**Art. 11.** A Instrução Normativa GSI/PR nº 5, de 30 de agosto de 2021, passa a vigorar com a seguinte alteração:

"Art. 17 ...............................................................................................................

.......................................................................................................................................

II - informação classificada em grau de sigilo e seus documentos preparatórios poderão ser tratados em ambiente de computação em nuvem nos termos da regulamentação específica; e

............................................................................................................................." (NR)

**Art. 12.** Esta Instrução Normativa entra em vigor na data de sua publicação.

MARCOS ANTONIO AMARO DOS SANTOS
