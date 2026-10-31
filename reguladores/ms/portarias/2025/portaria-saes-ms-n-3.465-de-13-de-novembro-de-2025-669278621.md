---
titulo: "Portaria SAES/MS Nº 3.465, DE 13 DE novembro DE 2025"
orgao: "Ministério da Saúde/Secretaria de Atenção Especializada à Saúde"
tipo: "Portaria"
numero: "3465"
data: 2025-11-13
revogada: false
versao_texto: "publicação original"
publicacao: "DOU de 17/11/2025, seção 1, p. 94"
data_publicacao: 2025-11-17
edicao: "219"
fonte: "https://www.in.gov.br/web/dou/-/portaria-saes/ms-n-3.465-de-13-de-novembro-de-2025-669278621"
baixado_em: 2026-10-16
---
# Portaria SAES/MS Nº 3.465, DE 13 DE novembro DE 2025

Portaria SAES/MS Nº 3.465, DE 13 DE novembro DE 2025

Altera a Portaria SAES/MS nº 37, de 18 de janeiro de 2021, redefinido o modelo de informação do Módulo Equipes do CNES, para ajustes dos campos de identificação dos veículos vinculados às equipes de Saúde da Família Ribeirinhas.

O SECRETÁRIO DE ATENÇÃO ESPECIALIZADA À SAÚDE, no uso das atribuições que lhe confere o Decreto nº 11.798, de 28 de novembro de 2023, alterado pelo Decreto nº 12.489, de 04 de junho de 2025,

**Art. 1º** Fica alterado o Anexo II da Portaria SAES/MS nº 37, de 18 de janeiro de 2021, que passa a vigorar conforme Anexo a esta Portaria.

**Art. 2º** Cabe aos gestores Municipais e Estaduais, se for o caso, realizar o registro do Tipo de Veículo e do Registro do Veículo na aba de Informações Complementares 1 do Módulo Equipes, no prazo de 06 (seis) competências, a partir da implementação dos campos no sistema do Cadastro Nacional de Estabelecimentos de Saúde - CNES, nos termos da análise constante do processo 25000.140493/2024-26.

**Art. 3º** Cabe à Coordenação-Geral de Gestão de Sistemas de Informação em Saúde do Departamento de Regulação Assistencial e Controle da Secretaria de Atenção Especializada à Saúde (CGSI/DRAC/SAES/MS) a adoção das providências necessárias no sentido de adequar o CNES para a implementação das alterações definidas por esta Portaria.

**Art. 4º** Esta Portaria entra em vigor na data de sua publicação, com efeitos operacionais na competência seguinte a sua publicação.

MOZART JULIO TABOSA SALES

## ANEXO

## ANEXO II — MODELO DE INFORMAÇÃO DO CNES: MÓDULO EQUIPES

O modelo de informação do Módulo de Equipes foi elaborado utilizando a seguinte notação:

Coluna 1 (Nível): indica a relação de dependência do elemento aos demais. Um número maior significa que aquele item depende ou está subordinado ao de número menor e anterior à ele no modelo. Assim, um elemento de nível 2 é subitem de um elemento de nível 1, um de nível 3 é subitem de um de nível 2 e assim sucessivamente.

Coluna 2 (Ocorrência): demonstra a obrigatoriedade e a quantidade de ocorrências do elemento:

\- [0..] - indica que o elemento é opcional;

\- [1..] - indica que o elemento é obrigatório;

\- [..1] - indica que o elemento só pode ocorrer uma única vez;

\- [..N] - indica que o elemento pode ocorrer várias vezes.

Coluna 3 (Seção/Item): descrição do elemento ou de um agrupador de elementos (seção).

Coluna 4 (Tipo de Dados): demonstra a forma de representar o elemento.

Coluna 5 (Conceito): conceitua ou esclarece o elemento.

| NÍVEL | OCORRÊNCIA | SEÇÃO/ITEM | TIPO DE DADO | CONCEITO |
| --- | --- | --- | --- | --- |
| 1 | [1..N] | Equipes |  |  |
| 2 | [1..N] | Identificação da Equipe |  |  |
| 3 | [1..1] | CNES | 07 Caracteres Alfanuméricos | Número de registro do estabelecimento de saúde no CNES ao qual a equipe está vinculada |
| 3 | [1..1] | Nome Fantasia | Caracteres Alfanuméricos | Nome Fantasia do estabelecimento de saúde ao qual a equipe está vinculada |
| 3 | [1..1] | Identificador Nacional de Equipes (INE) | 10 Caracteres Numéricos | Número identificador de equipes multiprofissionais preconizadas por Políticas Nacionais. |
| 3 | [1..1] | Tipo de Equipe | Tabela de Domínio | Identifica a estratégia de atenção preconizada em Política Nacional no formato ao qual a equipe atua. |
| 3 | [1..1] | Nome de Referência | Caracteres Alfanuméricos | Nome pela qual a Equipe é identificada pela gestão local ou usuários do SUS |
| 3 | [1..1] | População Assistida | Check | Tipo de população específica que a equipe assiste |
| 3 | [1..1] | Data de Ativação | Data | Data de início da atuação da equipe naquele estabelecimento |
| 3 | [0..1] | Data de Desativação | Data | Data de início de desativação da equipe naquele estabelecimento |
| 3 | [0..1] | Motivo da Desativação | Tabela de Domínio | Motivo pelo qual a equipe foi desativada |
| 2 | [1..1] | Composição da Equipe |  |  |
| 3 | [1..N] | CNS | Seleção | Cartão Nacional de Saúde do profissional que participa da equipe |
| 3 | [1..1] | Nome do Profissional | Seleção | Nome do profissional que atua da equipe |
| 3 | [1..1] | CBO | Seleção | Ocupação em que o profissional atua na equipe conforme Classificação Brasileira de Ocupações (CBO) |
| 3 | [1..1] | CHS na Equipe | 02 Caracteres Numéricos | Carga horária semanal em que o profissional atua na equipe |
| 3 | [1..1] | Data de Entrada na Equipe | Data | Data de início da atuação do profissional naquela equipe |
| 3 | [0..1] | Data de Saída da Equipe | Data | Data de final da atuação do profissional naquela equipe |
| 2 | [0..1] | Identificação Complementar |  |  |
| 3 | [0..N] | Unidades de Apoio | Secção | Identifica as Unidade de Apoio (Satélite) identificadas conforme programação visual padronizada das unidades de saúde do SUS |
| 4 | [0..N] | Nome de Referência | Caracteres Alfanuméricos | Nome de Referência do endereço complementar utilizado como Unidade de Apoio |
| 4 | [1..1] | Data de Ativação | Data | Data de ativação do endereço complementar |
| 3 | [0..N] | Apoio à Estabelecimentos / Equipes | Secção | Identifica quais estabelecimentos ou equipes recebem apoio de uma outra equipe |
| 4 | [0..N] | CNES | Seleção | Número CNES do Estabelecimento apoiado pela equipe |
| 4 | [0..N] | INE | Seleção | Número INE de equipe apoiada pela equipe |
| 3 | [0..N] | Veículos de Apoio | Secção | Embarcações de pequeno porte ou pick-up com cabine dupla com tração 4×4 para o deslocamento dos profissionais da equipe identificadas conforme programação visual padronizada das unidades de saúde do SUS |
| 4 | [0..N] | Número do Veículo | Caracteres Alfanuméricos | Número do veículo identificado conforme programação visual padronizada das unidades de saúde do SUS |
| 4 | [0..N] | Nome do Veículo | Caracteres Alfanuméricos | Nome de referência do veículo conforme programação visual padronizada das unidades de saúde do SUS |
| 4 | [0..N] | Tipo de Veículo | Seleção | Identifica se é o veículo é uma Embarcação de pequeno porte ou pick-up com tração 4×4 |
| 4 | [0..N] | Registro do Veículo | Caracteres Alfanuméricos | Nº identificador da embarcação na Marinha do Brasil ou Placa da pick-up com tração 4×4 |
| 4 | [0..N] | Comunidade(s) Atendida(s) | Caracteres Alfanuméricos | Identifica as comunidades ribeirinhas atendidas com o apoio do veículo |
| 3 | [0..N] | Mapeamento Indígena | Secção | Apenas para equipes 08 EMSI |
| 4 | [0..N] | DSEI | Seleção | Identifica o Distrito Sanitário Especial Indígena aos quais pertencem as aldeias atendidas pela Equipe Multidisciplinar de Atenção à Saúde Indígena |
| 4 | [0..N] | Polo Base | Seleção | Identifica os Polos Base aos quais pertencem as aldeias atendidas pela Equipe Multidisciplinar de Atenção à Saúde Indígena |
| 4 | [0..N] | Aldeia | Seleção | Identifica as aldeias atendidas pela Equipe Multidisciplinar de Atenção à Saúde Indígena |
