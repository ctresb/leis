---
titulo: "Portaria GM/MS Nº 6.093, DE 16 DE dezembro DE 2024"
orgao: "Ministério da Saúde/Gabinete da Ministra"
tipo: "Portaria"
numero: "6093"
data: 2024-12-16
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 17/12/2024, seção 1, p. 112"
data_publicacao: 2024-12-17
edicao: "242"
fonte: "https://www.in.gov.br/web/dou/-/portaria-gm/ms-n-6.093-de-16-de-dezembro-de-2024-602264704"
sha256_html_fonte: 179d6c44b4721e58da9578e9b87d05cc39b5f78e7446b6b403b8d256f63560b0
baixado_em: 2026-10-16
---
# Portaria GM/MS Nº 6.093, DE 16 DE dezembro DE 2024

Portaria GM/MS Nº 6.093, DE 16 DE dezembro DE 2024

Institui a Ontologia Brasileira de Medicamentos - OBM.

A MINISTRA DE ESTADO DA SAÚDE, no uso das atribuições que lhe confere o art. 87, parágrafo único, incisos I e II da Constituição, resolve:

**Art. 1º** Fica instituída a Ontologia Brasileira de Medicamentos-OBM, padrão terminológico com o objetivo de padronizar e sistematizar as informações sobre a identificação de medicamentos em âmbito nacional.

**Art. 2º** As classes principais que compõem a OBM, suas definições e propósitos estão descritos no Anexo desta Portaria.

**Art. 3º** A gestão do banco de dados e dos sistemas de gerenciamento e interoperabilidade, bem como a disponibilização das versões da OBM fica a cargo da Secretaria de Informação e Saúde Digital do Ministério da Saúde.

**Art. 4º** A OBM é requisito mínimo para integração e interoperabilidade com a Rede Nacional de Dados em Saúde - RNDS, sendo obrigatória sua adoção para identificação de medicamentos em todos os sistemas de informação e mecanismos de interoperabilidade existentes em território nacional.

**Art. 5º** Os prazos finais para implementação e uso da OBM serão estabelecidos em plano operativo estabelecido no âmbito tripartite, em até trinta dias, a partir das publicações pelo Ministério da Saúde dos modelos de dados, divulgados no sitio eletrônico do Portal de Serviços do Departamento de Informação e Informática do SUS do Ministério da Saúde.

**Art. 6º** Esta Portaria entra em vigor a partir de data de sua publicação.

NÍSIA TRINDADE LIMA

## ANEXO

Classes principais da Ontologia Brasileira de Medicamentos (OBM)

Introdução

A OBM tem como objetivo integrar e padronizar os dados de diferentes sistemas de informações, diretrizes regulatórias e normalizar registros de prescrições e dispensações, promovendo a interoperabilidade por meio da Rede Nacional de Dados em Saúde (RNDS). Dessa forma, proporciona a segurança do paciente por meio de uma lista padronizada de medicamentos, seguindo práticas internacionais para descrição e categorização de medicamentos, tal como o Padrão IDMP (Identification of Medicinal Products), conjunto de normas ISO (International Organization for Standardization) com o intuito de proporcionar a identificação única de medicamentos, subsidiando os processos de farmacovigilância e segurança de medicamentos.

A disponibilidade de uma base nacional de interoperabilidade de medicamentos, orientada por um padrão terminológico é fundamental para aprimorar a assistência farmacêutica. Essas iniciativas qualificam a interoperabilidade das informações de saúde, propiciando aos diferentes atuantes no setor saúde o aprimoramento do ciclo logístico (seleção, programação, aquisição, qualificação, distribuição e armazenamento), do ciclo da cadeia produtiva (pesquisa, desenvolvimento e inovação; registro, produção, mercado) e do ciclo do cuidado (prescrição, avaliação, dispensação, ministração, monitoramento e vigilância). Aos profissionais de saúde, os dados padronizados e atualizados viabilizarão ferramentas de monitoramento farmacoterapêutico mais efetivas, resultando num manejo farmacoterapêutico mais preciso, seguro e orientado para a excelência no cuidado ao paciente.

O dado público será acessível em granularidade primária, atualizado, acessível ao usuário comum e indexado na internet, processável por máquina, com acesso não discriminatório, em formato não proprietário, livre de licenças e contendo rastreabilidade das modificações com versionamento.

O conteúdo e detalhamento da estrutura da OBM, bem como toda a documentação relacionada, está disponível no endereço eletrônico https://portal-obm.saude.gov.br.

Descrição Geral

A OBM tem como objetivo incluir medicamentos em todos os níveis de atenção à saúde no âmbito público e privado.

A estrutura da OBM está baseada no modelo no Dictionary of Medicine and Devices (dm+d) do NHS (National Health System). Foram incluídas extensões para acomodar informações adicionais necessárias para descrever os medicamentos no Brasil. O principal objetivo de se construir uma Ontologia de Medicamentos é aumentar a segurança do paciente nos processos de prescrição e dispensação eletrônicas. Essa base de conhecimento, juntamente com os Modelos de Informação da RNDS, oferecerá aos sistemas de prontuário eletrônico (PE) a possibilidade de trabalhar em níveis de maturidade, garantindo a segurança do processo, à semelhança do que já acontece hoje em vários países, tais como Reino Unido, Austrália, Canada, França, Alemanha, Espanha, Países Baixos, Suécia, Dinamarca e outros membros da União Europeia.

Estrutura

A Ontologia Brasileira de Medicamentos está estruturada em cinco classes principais e classes auxiliares. A partir do relacionamento hierárquico é formado o termo de identificação dos medicamentos.

A seguir os conceitos das classes essenciais da OBM estão descritos:

Princípio Ativo Virtual (VTM - Virtual Therapeutic Moiety): representa as substâncias formuladas como medicamentos, dissociadas da forma farmacêutica, via de administração, dose ou concentração.

Nota: Um VTM pode conter uma ou mais substâncias.

Exemplos:

\- Atenolol;

\- Tramadol + Paracetamol.

Produto Medicinal Virtual (VMP - Virtual Medicinal Product): representa um medicamento na forma de princípio ativo, com sua concentração, unidade de medida e forma farmacêutica, sem informação a respeito da marca comercial ou da empresa detentora do registro.

O VMP é o principal componente da OBM, uma vez que possui os relacionamentos com as formas farmacêuticas, vias de administração, ingredientes, necessidade de controle especial e vínculos com as extensões nacionais, por exemplo: o medicamento faz parte da RENAME (Relação Nacional de Medicamentos Essenciais) ou respectivo código CATMAT.

Exemplos:

\- Atenolol 50mg comprimido;

\- Tramadol 37,5mg + Paracetamol 325mg comprimido revestido.

Produto Medicinal Virtual com Apresentação (VMPP - Virtual Medicinal Product Pack): representa a quantidade por embalagem comercializada de um VMP, desprovida de qualquer informação a respeito de marca comercial ou empresa detentora do registro.

Exemplos:

\- Atenolol 50mg comprimido x 30 comprimidos;

\- Cloridrato de tramadol 37,5mg + Paracetamol 325mg comprimido x 30 comprimidos revestidos.

Produto Medicinal Virtual com Apresentação (VMPP - Virtual Medicinal Product Pack): representa a quantidade por embalagem comercializada de um VMP, desprovida de qualquer informação a respeito de marca comercial ou empresa detentora do registro.

Exemplos:

\- Atenolol 50mg comprimido x 30 comprimidos;

\- Cloridrato de tramadol 37,5mg + Paracetamol 325mg comprimido x 30 comprimidos revestidos.

Produto Medicinal Comercial (AMP - Actual Medicinal Product): representa um produto acabado, ou seja, um medicamento de referência, genérico ou similar, associado à empresa detentora de registro.

Exemplos:

\- AtenoSUS 50mg comprimido (Laboratório Farmacêutico do SUS) x 30 comprimidos;

\- - Cloridrato de tramadol 37,5mg + Paracetamol 325mg comprimido revestido (Laboratório Farmacêutico do SUS)

Produtos e laboratórios fictícios para exemplificação.

Produto Medicinal Comercial com Apresentação (AMPP - Actual Medicinal Product Pack): representa um produto medicinal embalado. Um AMPP pode conter múltiplos componentes e cada um destes componentes podem, por si só, serem AMPPs independentes. A descrição do AMPP deve permitir a identificação unívoca do medicamento, incluindo informações relacionadas à quantidade, volume ou peso do medicamento por acondicionamento secundário.

Exemplos:

\- AtenoSUS 50mg comprimido (Laboratório Farmacêutico do SUS) x 30 comprimidos;

\- Cloridrato de tramadol 37,5mg + Paracetamol 325mg comprimido (Laboratório Farmacêutico do SUS) x 30 comprimidos revestidos.

Produtos e laboratórios fictícios para exemplificação.

Extensões

As seguintes informações adicionais foram incorporadas ao modelo da dm+d para descrever os medicamentos existentes no País, conforme registro na ANVISA:

\- Classe terapêutica, conforme ANVISA - ex.: antialérgico, anticoagulante, antiemético etc.;

\- Código Anatomic Theraupeutic Classification (ATC) - O Sistema de ATC é um sistema de classificação de medicamentos, controlado pelo Centro Colaborador da Organização Mundial da Saúde para Metodologia Estatística de Medicamentos (WHOCC), que classifica os princípios ativos dos medicamentos de acordo com o órgão ou sistema sobre o qual atuam e suas propriedades terapêuticas, farmacológicas e químicas;

\- Número do registro sanitário na ANVISA;

\- Número do processo do medicamento na ANVISA;

\- Validade do registro na ANVISA;

\- Data da publicação do registro sanitário na ANVISA;

\- Embalagem primária e secundária (blister, cartucho, ampola etc.);

\- Categoria regulatória do medicamento conforme ANVISA - ex.: referência, genérico ou similar;

\- Informação se o medicamento faz parte da base do Sistema HÓRUS (Sistema Nacional de Gestão da Assistência Farmacêutica);

\- Categoria de Controle Especial de acordo com a Portaria nº 344/GM/MS/1998.

Adicionalmente, foram criadas tabelas extras ao modelo da dm+d, denominadas de extensões brasileiras para relacionar às cinco classes principais com outras tabelas nacionais, tais como:

\- Código CATMAT: o Catálogo de Materiais (CATMAT) é um sistema que permite a catalogação e a distribuição de materiais (medicamentos e insumos) para a rede pública de atenção. O CATMAT estabelece uma codificação única e padronizada para identificação e descrição de produtos a serem adquiridos pelo Governo Federal. Por este motivo, estes códigos foram incluídos como extensão brasileira nos VMPs.

\- RENAME (Relação Nacional de Medicamentos Essenciais): todas as informações referentes à RENAME e seus componentes, conforme a Resolução de Consolidação n° 1/CIT/2021, foram incorporadas ao modelo da OBM.

\- DCB (Denominação Comum Brasileira): tabela com a denominação do fármaco ou princípio farmacologicamente ativo aprovada pelo órgão federal responsável pela vigilância sanitária, conforme Lei nº 9.787/1999.
