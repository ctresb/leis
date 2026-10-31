---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 328, DE 23 DE NOVEMBRO DE 2022"
orgao: "Banco Central do Brasil/Área de Fiscalização/Departamento de Monitoramento do Sistema Financeiro"
tipo: "Instrução Normativa"
numero: "328"
data: 2022-11-23
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 24/11/2022, seção 1, p. 89"
data_publicacao: 2022-11-24
edicao: "221"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-328-de-23-de-novembro-de-2022-445757542"
sha256_html_fonte: 61612edd72d822e63594f15fc0a25a7331ef62866b09c7c5426aa919d486c466
baixado_em: 2026-10-20
---
# INSTRUÇÃO NORMATIVA BCB Nº 328, DE 23 DE NOVEMBRO DE 2022

INSTRUÇÃO NORMATIVA BCB Nº 328, DE 23 DE NOVEMBRO DE 2022

Altera as Instruções de preenchimento e o Leiaute do documento de código 2030 - Documento de Risco Social, Ambiental e Climático (DRSAC), de que trata a Instrução Normativa BCB nº 222, de 28 de dezembro de 2021.

O Chefe do Departamento de Monitoramento do Sistema Financeiro (Desig), no uso da atribuição que confere o art. 23, inciso I, alínea "a", do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, com base no art. 77, inciso III, do referido Regimento, e tendo em vista o disposto na Resolução BCB nº 151, de 6 de outubro de 2021, e na Instrução Normativa BCB nº 222, de 28 de dezembro de 2021, resolve:

**Art. 1º** Passam a vigorar, a partir da data-base de dezembro de 2022, as novas versões das Instruções de preenchimento e do Leiaute do documento de código 2030 - Documento de Risco Social, Ambiental e Climático (DRSAC), disponíveis na página do Banco Central do Brasil na internet, no endereço eletrônico https://www.bcb.gov.br/estabilidadefinanceira/leiautedocumentoscrd.

**Art. 2º** Foram feitas as seguintes modificações nas Instruções de Preenchimento:

I - no capítulo 4 - Origem da informação: critérios para envio dos dados: ajustes na redação das instruções referentes à tag "ExpSetor";

II - no capítulo 5 - Orientações gerais sobre o arquivo XML:

a) no item 3: inclusão da tag "Setores";

b) no item 5: exclusão da tag "ExpSetor" da tag "Cliente";

c) no item 12: inclusão da tag "Setores", contendo a tag "ExpSetor";

d) no item 13: alteração do nome do atributo "codSetor" para "CNAE".

**Art. 3º** Foram feitas as seguintes modificações no Leiaute:

I - na aba Estrutura XML:

a) na tag "DocumentoDRSAC": criação da tag "Setores", contendo a tag "ExpSetor";

b) na tag "Cliente": inclusão do atributo "CNAE" e exclusão da tag "ExpSetor";

c) na tag "SetorRestrito": a tag passou a ser obrigatória e o nome do atributo "codSetor" foi alterado para "CNAE";

II - na aba Leiaute:

a) no grupo "Cabeçalho do documento XML":

1\. no campo "Documento DRSAC": inclusão da tag "Setores";

b) no grupo "Cliente":

1\. no campo "Clientes": o campo passou a ser obrigatório, inclusão do atributo "CNAE" e exclusão da tag "ExpSetor";

2\. no campo "Identificador do Cliente": ajuste na descrição do atributo "ident" (informando o tamanho do CNPJ a ser enviado);

3\. Inclusão do campo "CNAE";

c) no grupo "Exposição ao Risco do Cliente":

1\. no campo "Exposição do Cliente": o campo passou a ser obrigatório;

d) no grupo "Exposição ao Risco do Setor Econômico do Cliente":

1\. inclusão do o campo "Setores"

2\. no campo "Exposição do Setor": o campo passou a ser obrigatório e alteração na descrição do atributo;

3\. no campo "CNAE": alteração na descrição do atributo.

e) no grupo "Detalhe das Informações":

1\. os campos "Contribuição Positiva", "Detalhe de Enquadramento Contribuição Positiva", "Mitigador Risco Climático Físico", "Histórico de Absorção e Emissão de GEE", "Expectativa de Absorção e Emissão de GEE", "Compensação de Emissões de GEE" e "Agravantes e Mitigadores" passaram a ser obrigatórios;

f) no grupo "Setor de Atividade Econômica Restrita":

1\. no campo "SetorRestrito": o campo passou a ser obrigatório e alteração do atributo "codSetor" para "CNAE";

2\. alteração do nome do campo "codSetor" para "CNAE".

**Art. 4º** Foram feitas as seguintes modificações no arquivo XSD:

I - na tag "DocumentoDRSAC": criação da tag "Setores", com a inclusão da tag "ExpSetor", que foi removida da tag "Cliente";

II - as seguintes tags passaram a ser obrigatórias: "Clientes", "ExpCliente", "ExpSetor" e "SetorRestrito";

III - na tag "Cliente": inclusão do atributo "CNAE" e exclusão da tag "ExpSetor";

IV - na tag "CompEmissGEE": correção no número mínimo de ocorrências para 2;

V - na tag "SetorRestrito": alteração do nome do atributo "codSetor" para "CNAE".

**Art. 5º** Esta Instrução Normativa entra em vigor em 1º de dezembro de 2022.

Gilneu Francisco Astolfi Vivan
