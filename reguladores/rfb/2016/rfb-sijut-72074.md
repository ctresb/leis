---
titulo: "Ato Declaratório Executivo Cotec nº 1, de 29 de fevereiro de 2016"
orgao: "Coordenação-Geral de Tecnologia da Informação"
tipo: "Ato Declaratório Executivo"
numero: "1"
data: "2016-02-29"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado no sítio da RFB na internet em 09/03/2016"
data_publicacao: "2016-03-09"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/72074/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/72074/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "72074"
sha256_texto: "de7ec59681c6a2a27bc483922a7d87e8061f637c3cf428a2d546aa6eb32359fd"
baixado_em: "2026-10-16"
---
# Ato Declaratório Executivo Cotec nº 1, de 29 de fevereiro de 2016

Altera os leiautes dos modelos de Comprovante Eletrônico de Rendimentos Pagos e de Imposto sobre a Renda Retido na Fonte e de Comprovante Eletrônico de Pagamentos de Serviços Médicos e de Saúde.

A COORDENADOR-GERAL DE TECNOLOGIA DA INFORMAÇÃO, no uso da atribuição que lhe confere o inciso III do art. 312 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 203, de 14 de maio de 2012, e tendo em vista o disposto no art. 9º-A da Instrução Normativa RFB nº 1.416, de 04 de dezembro de 2013,

DECLARA:

**Art. 1º** Os anexos da Instrução Normativa RFB nº1416, de 04 de dezembro de 2013, ficam alterados conforme os anexos deste Ato Declaratório Executivo.

**Art. 2º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação na Internet.

CLAUDIA MARIA DE ANDRADE

ANEXO I - LEIAUTE DO COMPROVANTE DE RENDIMENTOS PAGOS

a

<?xml version="1.0" encoding="UTF-8"?> <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tipos="http://www.receita.fazenda.gov.br/Tipos" elementFormDefault="qualified"> <!-- importação dos tipos e elementos comuns --> <xs:import schemaLocation="informe\_tipos.xsd" namespace="http://www.receita.fazenda.gov.br/Tipos" /> <!-- início da definição dos tipos --> <xs:simpleType name="codigoTipoFundo"> <xs:restriction base="xs:token"> <xs:enumeration value="1" /><!--Previdência Complementar --> <xs:enumeration value="2" /><!--Fapi – Fundo de Aposentadoria Programa Individual --> <xs:enumeration value="3" /><!--Funpresp – Fundações de Previdência Complementar do Servidor Público Federal dos Poderes Executivo, Legislativo e Judiciário --> </xs:restriction> </xs:simpleType> <xs:simpleType name="codigoTipoRendimentoIsento"> <xs:restriction base="xs:token"> <xs:enumeration value="1" /><!--Valor parcela isenta 65 anos --> <xs:enumeration value="2" /><!--Valor moléstia grave --> <xs:enumeration value="3" /><!--Lucros e dividendos --> <xs:enumeration value="4" /><!--Valor Sócio ou Titular de microempresa ou empresa de pequeno porte --> <xs:enumeration value="5" /><!--Valor indenização rescisão, PDV, acidente de trabalho --> <xs:enumeration value="6" /><!--Benefícios indiretos e reembolso de despesas - Voluntários da Copa --> <xs:enumeration value="7" /><!--Bolsa de estudo recebida por médico --> <xs:enumeration value="8" /><!--Bolsa de estudo recebida por não médico --> <xs:enumeration value="9" /><!--IRRF - Valor compensado de anos-calendário anteriores --> <xs:enumeration value="10" /><!--Diárias e ajuda de custo --> <xs:enumeration value="11" /><!--Abono pecuniário --> </xs:restriction> </xs:simpleType> <xs:simpleType name="codigoTipoRendimentoTributacaoExclusiva"> <xs:restriction base="xs:token"> <xs:enumeration value="1" /><!--Juros Sobre Capital Próprio --> <xs:enumeration value="2" /><!--Participação nos Lucros ou Resultados --> </xs:restriction> </xs:simpleType> <!-- fim da definição dos tipos --> <!-- início da definição dos elementos simples --> <xs:element name="cpfBeneficiario" type="tipos:cpf" /> <xs:element name="cpfBeneficiarioServico" type="tipos:cpfOpcional" /> <xs:element name="nomeBeneficiario" type="tipos:nomePF" /> <xs:element name="nomeBeneficiarioServico" type="tipos:nomePF" /> <xs:element name="anoExercicio" type="tipos:ano" /> <xs:element name="anoCalendario" type="tipos:ano" /> <xs:element name="cpfCnpjFontePagadora" type="tipos:cpfCnpj" /> <xs:element name="nomeFontePagadora" type="tipos:nomePJ" /> <xs:element name="totalRendimentoInclusiveFerias" type="tipos:valor" /> <xs:element name="contribuicaoPrevidenciariaOficial" type="tipos:valor"

<xs:element name="impostoRetidoFonte" type="tipos:valor" /> Página 1

<xs:element name="impostoRetidoFonteCompensadoAnosAnteriores" type="tipos:valor" /> <xs:element name="decimoTerceiro" type="tipos:valor" /> <xs:element name="irrfDecimoTerceiro" type="tipos:valor" /> <xs:element name="cnpjFundo" type="tipos:cnpj" /> <xs:element name="nomeFundo" type="tipos:nomePJ" /> <xs:element name="tipoFundo" type="codigoTipoFundo" /> <xs:element name="valorPagoFundo" type="tipos:valor" /> <xs:element name="valorContribuicaoPatrocinador" type="tipos:valor" /><!-- Incluido - IRPF 2016 --> <xs:element name="tipoRendimentoIsento" type="codigoTipoRendimentoIsento" /> <xs:element name="tipoRendimentoTributacaoExclusiva" type="codigoTipoRendimentoTributacaoExclusiva" /> <xs:element name="cpfAlimentando" type="tipos:cpfOpcional" /> <xs:element name="nomeAlimentando" type="tipos:nomePF" /> <xs:element name="valorPagoPensaoAlimenticia" type="tipos:valor" /> <xs:element name="valorDecimoTerceiroPensaoAlimenticia" type="tipos:valor" /> <xs:element name="numeroProcessoRendimentoExigibilidadeSuspensa" type="tipos:numeroProcesso" /> <xs:element name="valorRendimentoExigibilidadeSuspensa" type="tipos:valor" /> <xs:element name="valorDepositosJudiciaisExigibilidadeSuspensa" type="tipos:valor" /> <xs:element name="descricaoRendimento" type="tipos:descricao" /> <xs:element name="valorRendimento" type="tipos:valor" /> <xs:element name="numeroProcesso" type="tipos:numeroProcesso" /> <xs:element name="numeroMeses" type="tipos:decimal\_3\_1" /> <xs:element name="mesRecebimento" type="tipos:mes" /> <xs:element name="despesaComAcaoJudicial" type="tipos:valor" /> <xs:element name="valorRRAMolestiaGrave" type="tipos:valorOpcional" /> <xs:element name="valorPago" type="tipos:valor" /> <xs:element name="valorTotalPago" type="tipos:valor" /> <xs:element name="cpfcnpjPrestadorServico" type="tipos:cpfCnpjOpcional"

<xs:element name="nomePrestadorServico" type="tipos:nomePJOpcional" /> <xs:element name="valorReembolsado" type="tipos:valor" /> <!-- fim da definição dos elementos simples -->

<!-- início da definição dos elementos complexos --> <xs:element name="header">

<xs:element ref="cpfCnpjFontePagadora" /> <xs:element ref="nomeFontePagadora" /> <xs:element ref="cpfBeneficiario" /> <xs:element ref="nomeBeneficiario" /> <xs:element ref="anoExercicio" /> <xs:element ref="anoCalendario" />

<xs:element name="itemRendimentosTributaveisRecebidosPessoaJuridica">

<xs:element ref="totalRendimentoInclusiveFerias"

ref="contribuicaoPrevidenciariaOficial" /> <xs:element ref="impostoRetidoFonte" /> <xs:element ref="decimoTerceiro" /> <xs:element ref="irrfDecimoTerceiro" minOccurs="0" />

Página 2

<xs:element name="listaRendimentosTributaveisRecebidosPessoaJuridica">

ref="itemRendimentosTributaveisRecebidosPessoaJuridica"

<xs:element name="itemPrevidenciaComplementar">

<xs:element ref="cnpjFundo" /> <xs:element ref="nomeFundo" /> <xs:element ref="tipoFundo" /> <xs:element ref="valorPagoFundo" /> <xs:element ref="valorContribuicaoPatrocinador" minOccurs="0" /><!-- Incluido - IRPF 2016 -->

<xs:element name="listaPrevidenciaComplementar">

<xs:element ref="itemPrevidenciaComplementar"

<xs:element name="itemPensaoAlimenticia">

<xs:element ref="cpfAlimentando" minOccurs="0"

<xs:element ref="nomeAlimentando" /> <xs:element ref="valorPagoPensaoAlimenticia" />

ref="valorDecimoTerceiroPensaoAlimenticia" />

<xs:element name="listaPensaoAlimenticia">

<xs:element ref="itemPensaoAlimenticia"

<xs:element name="itemRendimentosIsentosNaoTributaveis">

<xs:element ref="tipoRendimentoIsento" /> <xs:element ref="valorRendimento" /> <xs:element ref="decimoTerceiro" minOccurs="0" /> <xs:element ref="contribuicaoPrevidenciariaOficial" minOccurs="0" /><!-- Incluido - IRPF 2016 -->

<xs:element name="listaRendimentosIsentosNaoTributaveis"> Página 3

ref="itemRendimentosIsentosNaoTributaveis"

<xs:element name="itemOutrosRendimentosIsentosNaoTributaveis">

<xs:element ref="descricaoRendimento" /> <xs:element ref="valorRendimento" />

<xs:element name="listaOutrosRendimentosIsentosNaoTributaveis">

ref="itemOutrosRendimentosIsentosNaoTributaveis"

<xs:element name="itemRendimentosSujeitosTributacaoExclusiva">

ref="tipoRendimentoTributacaoExclusiva" /> <xs:element ref="valorRendimento" />

<xs:element name="listaRendimentosSujeitosTributacaoExclusiva">

ref="itemRendimentosSujeitosTributacaoExclusiva"

<xs:element name="itemOutrosRendimentosSujeitosTributacaoExclusiva">

<xs:element ref="descricaoRendimento" /> <xs:element ref="valorRendimento" />

<xs:element name="listaOutrosRendimentosSujeitosTributacaoExclusiva">

ref="itemOutrosRendimentosSujeitosTributacaoExclusiva"

<xs:element name="itemPensaoAlimenticiaRRA"> Página 4

<xs:element ref="cpfAlimentando" minOccurs="0"

<xs:element ref="nomeAlimentando" /> <xs:element ref="valorPago" />

<xs:element name="listaPensaoAlimenticiaRRA">

<xs:element ref="itemPensaoAlimenticiaRRA"

<xs:element name="itemRendimentosRecebidosAcumuladamente">

<xs:element ref="numeroProcesso" minOccurs="0"

<xs:element ref="numeroMeses" /> <xs:element ref="mesRecebimento" /> <xs:element ref="valorRendimento" /> <xs:element ref="despesaComAcaoJudicial" />

ref="contribuicaoPrevidenciariaOficial" /> <xs:element ref="impostoRetidoFonte" /> <xs:element ref="valorRRAMolestiaGrave" minOccurs="0" /> <xs:element ref="listaPensaoAlimenticiaRRA" minOccurs="0" maxOccurs="unbounded" />

<xs:element name="listaRendimentosRecebidosAcumuladamente">

ref="itemRendimentosRecebidosAcumuladamente"

<xs:element name="itemPagamentos">

<xs:element ref="cpfBeneficiarioServico" minOccurs="0" /> <xs:element ref="nomeBeneficiarioServico" /> <xs:element ref="cpfcnpjPrestadorServico" minOccurs="0" /> <xs:element ref="nomePrestadorServico" minOccurs="0" /> <xs:element ref="valorTotalPago" /> <xs:element ref="valorReembolsado" />

<xs:element name="listaPagamentos">

Página 5

<xs:element ref="itemPagamentos"

<xs:element name="itemRendimentosExigibilidadeSuspensa">

ref="numeroProcessoRendimentoExigibilidadeSuspensa" minOccurs="0" />

ref="valorRendimentoExigibilidadeSuspensa" />

ref="valorDepositosJudiciaisExigibilidadeSuspensa" />

<xs:element name="listaRendimentosExigibilidadeSuspensa">

ref="itemRendimentosExigibilidadeSuspensa"

<xs:element name="informeRendimentosFontePagadora">

<xs:element ref="header" />

ref="listaRendimentosTributaveisRecebidosPessoaJuridica" minOccurs="0" /> <xs:element ref="listaPrevidenciaComplementar" minOccurs="0" /> <xs:element ref="listaPensaoAlimenticia" minOccurs="0" />

ref="listaRendimentosIsentosNaoTributaveis" minOccurs="0" />

ref="listaOutrosRendimentosIsentosNaoTributaveis" minOccurs="0" />

ref="listaRendimentosSujeitosTributacaoExclusiva" minOccurs="0" />

ref="listaOutrosRendimentosSujeitosTributacaoExclusiva" minOccurs="0" />

ref="listaRendimentosRecebidosAcumuladamente" minOccurs="0" /> <xs:element ref="listaPagamentos" minOccurs="0"

ref="listaRendimentosExigibilidadeSuspensa" minOccurs="0" />

<!-- fim da definição dos elementos complexos --> </xs:schema>

Página 6

PÁGINA DE AUTENTICAÇÃO

A Secretaria da Receita Federal do Brasil garante a integridade e a autenticidade deste documento nos termos do Art. 10, § 1º, da Medida Provisória nº 2.200-2, de 24 de agosto de 2001

Histórico de atividades sobre o documento:

Documento assinado digitalmente por: CLAUDIA MARIA DE ANDRADE em 29/02/2016. Confira o documento original pelo Smartphone conectado à Internet:

Dúvida? Acesse http://sadd.receita.fazenda.gov.br/sadd-internet/pages/qrcode.xhtml

Confira o documento original pela Internet:

a) Acesse o endereço: http://sadd.receita.fazenda.gov.br/sadd-internet/pages/validadocumento.xhtml

b) Digite o número abaixo ou leia o código de barras a seguir:

Código Hash obtido atraves do algoritmo SHA-256:

S7yBWsTMONVaWBaE9wFO9UKE4qAst/QfxQccswyQ/p8=


ANEXO II - LEIAUTE DO COMPROVANTE DE PAGAMENTOS DE SAÚDE

a

<?xml version="1.0" encoding="UTF-8"?> <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tipos="http://www.receita.fazenda.gov.br/Tipos" elementFormDefault="qualified">

<!-- importaca dos tipos e elementos comuns --> <xs:import schemaLocation="informe\_tipos.xsd" namespace="http://www.receita.fazenda.gov.br/Tipos" /> <!-- inicio da definicao dos elementos simples --> <xs:element name="cpfBeneficiario" type="tipos:cpf" /> <xs:element name="nomeBeneficiario" type="tipos:nomePF" /> <xs:element name="anoExercicio" type="tipos:ano" /> <xs:element name="anoCalendario" type="tipos:ano" /> <xs:element name="cnpjPlanoSaude" type="tipos:cnpj" /> <xs:element name="nomePlanoSaude" type="tipos:nomePJ" /> <xs:element name="cpfBeneficiarioPagamentoPremio" type="tipos:cpfOpcional" /> <xs:element name="nomeBeneficiarioPagamentoPremio" type="tipos:nomePF" /> <xs:element name="valorPagoPagamentoPremio" type="tipos:valor" /> <xs:element name="cpfBeneficiarioReembolso" type="tipos:cpfOpcional" /> <xs:element name="nomeBeneficiarioReembolso" type="tipos:nomePF" /> <xs:element name="cpfcnpjPrestadorServico" type="tipos:cpfCnpjOpcional" /> <xs:element name="nomePrestadorServico" type="tipos:nomePJOpcional" /> <xs:element name="valorTotalPago" type="tipos:valor" /> <xs:element name="valorReembolsado" type="tipos:valor" /> <!-- fim da definicao dos elementos simples --> <!-- início da definicao dos elementos complexos --> <xs:element name="header">

<xs:element ref="cnpjPlanoSaude" /> <xs:element ref="nomePlanoSaude" /> <xs:element ref="cpfBeneficiario" /> <xs:element ref="nomeBeneficiario" /> <xs:element ref="anoExercicio" /> <xs:element ref="anoCalendario" />

<xs:element name="itemPagamentoPremio">

<xs:element ref="cpfBeneficiarioPagamentoPremio"

<xs:element ref="nomeBeneficiarioPagamentoPremio" /> <xs:element ref="valorPagoPagamentoPremio" />

<xs:element name="listaPagamentoPremio">

<xs:element ref="itemPagamentoPremio"

<xs:element name="itemReembolso">

Página 1

<xs:element ref="cpfBeneficiarioReembolso"

<xs:element ref="nomeBeneficiarioReembolso" /> <xs:element ref="cpfcnpjPrestadorServico"

<xs:element ref="nomePrestadorServico"

<xs:element ref="valorTotalPago" /> <xs:element ref="valorReembolsado" />

<xs:element name="listaReembolso">

<xs:element ref="itemReembolso"

<xs:element name="informePlanoSaude">

<xs:element ref="header" /> <xs:element ref="listaPagamentoPremio" minOccurs="0" maxOccurs="unbounded" /> <xs:element ref="listaReembolso" minOccurs="0"

</xs:schema>

Página 2

PÁGINA DE AUTENTICAÇÃO

A Secretaria da Receita Federal do Brasil garante a integridade e a autenticidade deste documento nos termos do Art. 10, § 1º, da Medida Provisória nº 2.200-2, de 24 de agosto de 2001

Histórico de atividades sobre o documento:

Documento assinado digitalmente por: CLAUDIA MARIA DE ANDRADE em 29/02/2016. Confira o documento original pelo Smartphone conectado à Internet:

Dúvida? Acesse http://sadd.receita.fazenda.gov.br/sadd-internet/pages/qrcode.xhtml

Confira o documento original pela Internet:

a) Acesse o endereço: http://sadd.receita.fazenda.gov.br/sadd-internet/pages/validadocumento.xhtml

b) Digite o número abaixo ou leia o código de barras a seguir:

Código Hash obtido atraves do algoritmo SHA-256:

FTArnnQJnv+mxM1BbWVC1ergYxLVHvu3HQQBrrnlnjk=


ANEXO III - DEFINIÇÕES DE TIPOS DE DADOS

a

<?xml version="1.0" encoding="UTF-8"?> <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://www.receita.fazenda.gov.br/Tipos" targetNamespace="http://www.receita.fazenda.gov.br/Tipos" elementFormDefault="qualified"> <!-- inicio da definicao dos tipos comuns --> <xs:simpleType name="ano"> <xs:restriction base="xs:integer"> <xs:pattern value="\d{4}" />

<xs:simpleType name="data">

<xs:pattern value="\d{2}/\d{2}/\d{4}" />

<xs:simpleType name="mes">

<xs:pattern value="(0[1-9])|(1[0-2])" />

<xs:simpleType name="descricao">

<xs:simpleType name="valor">

<xs:pattern value="\d{1,11},\d{2}" />

<xs:simpleType name="valorOpcional">

<xs:pattern value="|(\d{1,11},\d{2})" />

<xs:simpleType name="cpf">

<xs:pattern value="\d{11}" />

<xs:simpleType name="cpfOpcional">

<xs:pattern value="|\d{11}" />

<xs:simpleType name="cnpj">

<xs:pattern value="\d{14}" />

<xs:simpleType name="cpfCnpj">

<xs:pattern value="\d{11}|\d{14}" />

Página 1

<xs:simpleType name="cpfCnpjOpcional">

<xs:pattern value="|\d{11}|\d{14}" />

<xs:simpleType name="nomePF">

<xs:pattern value="[\p{L}\s]{1,60}" />

<xs:simpleType name="nomePJ">

<xs:simpleType name="nomePJOpcional">

<xs:minLength value="0" />

<xs:simpleType name="numeroProcesso">

<xs:pattern value="|\d{1,20}" />

<xs:simpleType name="decimal\_3\_1">

<xs:pattern value="\d{1,3},\d{1}" />

<!-- fim da definicao dos tipos comuns -->

</xs:schema>

Página 2

PÁGINA DE AUTENTICAÇÃO

A Secretaria da Receita Federal do Brasil garante a integridade e a autenticidade deste documento nos termos do Art. 10, § 1º, da Medida Provisória nº 2.200-2, de 24 de agosto de 2001

Histórico de atividades sobre o documento:

Documento assinado digitalmente por: CLAUDIA MARIA DE ANDRADE em 29/02/2016. Confira o documento original pelo Smartphone conectado à Internet:

Dúvida? Acesse http://sadd.receita.fazenda.gov.br/sadd-internet/pages/qrcode.xhtml

Confira o documento original pela Internet:

a) Acesse o endereço: http://sadd.receita.fazenda.gov.br/sadd-internet/pages/validadocumento.xhtml

b) Digite o número abaixo ou leia o código de barras a seguir:

Código Hash obtido atraves do algoritmo SHA-256:

7pkCxE7+3vmKa+wvHg9FKoZLm13K7/JgRZKjl7KfJE0=


ANEXO IV - INSTRUÇÕES PARA PREENCHIMENTO DO COMPROVANTE DE RENDIMENTOS PAGOS

a

ANEXO IV INSTRUÇÕES PARA PREENCHIMENTO DO COMPROVANTE DE RENDIMENTOS PAGOS

Os formatos dos campos utilizados no arquivo XML estão descritos no Anexo III.

Lista de campos códigos com domínio fechado: codigoTipoFundo 1 – Previdência Complementar 2 – Fapi – Fundo de Aposentadoria Programa Individual 3 – Funpresp – Fundações de Previdência Complementar do Servidor Público Federal dos Poderes Executivo, Legislativo e Judiciário

codigoTipoRendimentoIsento 1 – Valor parcela isenta 65 anos 2 – Valor moléstia grave 3 – Lucros e dividendos 4 – Valor Sócio ou Titular de microempresa ou empresa de pequeno porte 5 – Valor indenização rescisão, PDV, acidente de trabalho 6 – Benefícios indiretos e reembolso de despesas – Voluntários da Copa 7 – Bolsa de estudo recebida por médico residente e pronatec 8 – Bolsa de estudo e de pesquisa 9 – IRRF – Valor compensado de anos-calendário anteriores 10 – Diárias e ajuda de custo 11 – Abono pecuniário

codigoTipoRendimentoTributacaoExclusiva 1 – Juros Sobre Capital Próprio 2 – Participação nos Lucros ou Resultados

Campos e seus tipos utilizados no informe de rendimentos. Os tipos estão definidos no Anexo III cpfBeneficiario – cpf cpfBeneficiarioServico – cpfOpcional nomeBeneficiario – nomePF nomeBeneficiarioServico – nomePF anoExercicio – ano anoCalendario – ano cpfCnpjFontePagadora – cpfCnpj

nomeFontePagadora – nomePJ totalRendimentoInclusiveFerias – valor contribuicaoPrevidenciariaOficial – valor impostoRetidoFonte – valor impostoRetidoFonteCompensadoAnosAnteriores – valor decimoTerceiro – valor irrfDecimoTerceiro - valor cnpjFundo – cnpj nomeFundo – nomePJ tipoFundo – codigoTipoFundo valorPagoFundo – valor valorContribuicaoPatrocinador - valor tipoRendimentoIsento – codigoTipoRendimentoIsento tipoRendimentoTributacaoExclusiva – codigoTipoRendimentoTributacaoExclusiva cpfAlimentando – cpfOpcional nomeAlimentando – nomePF valorPagoPensaoAlimenticia – valor valorDecimoTerceiroPensaoAlimenticia – valor numeroProcessoRendimentoExigibilidadeSuspensa – numeroProcesso valorRendimentoExigibilidadeSuspensa – valor valorDepositosJudiciaisExigibilidadeSuspensa – valor descricaoRendimento – descricao valorRendimento – valor numeroProcesso – numeroProcesso numeroMeses – decimal\_3\_1 mesRecebimento – mes despesaComAcaoJudicial – valor valorRRAMolestiaGrave – valorOpcional valorPago – valor valorTotalPago – valor cpfcnpjPrestadorServico – cpfCnpjOpcional nomePrestadorServico – nomePJOpcional valorReembolsado – valor

Tipos definidos no Anexo III ano – ano com 4 dígitos data – data válida no formato dd/mm/aaaa

mes – número entre 01 e 12 descricao – tamanho mínimo: 1 tamanho mínimo:60 valor – valor numérico com 11 dígitos e 2 casa decimais valorOpcional – opcional com 11 dígitos e 2 casa decimais cpf – campo numérico com 11 dígitos cpfOpcional – campo opcional numérico com 11 dígitos cnpj – campo numérico com 14 dígitos cpfCnpj – campo numérico com 11 ou 14 dígitos cpfCnpjOpcional – campo opcional numérico com 11 ou 14 dígitos nomePF – Primeira letra maiúscula tamanho mínimo:1 tamanho máximo: 60 nomePJ – tamanho mínimo:1 tamanho máximo: 60 nomePJOpcional – tamanho mínimo:0 tamanho máximo: 60 numeroProcesso – campo opcional numérico com 20 dígitos decimal\_3\_1 – campo numérico com 3 dígitos e uma casa decimal

Informações sobre o arquivo XML A tag inicial é informeRendimentosFontePagadora. Ela é composta por: <informeRendimentosFontePagadora> <header> - Obrigatório <listaRendimentosTributaveisRecebidosPessoaJuridica> - Opcional <istaPrevidenciaComplementar> - Opcional <listaPensaoAlimenticia> - Opcional <listaRendimentosIsentosNaoTributaveis> - Opcional <listaOutrosRendimentosIsentosNaoTributaveis> - Opcional <listaRendimentosSujeitosTributacaoExclusiva> - Opcional <listaOutrosRendimentosSujeitosTributacaoExclusiva> - Opcional <listaRendimentosRecebidosAcumuladamente> - Opcional <listaPagamentos> - Opcional <listaRendimentosExigibilidadeSuspensa> - Opcional </informeRendimentosFontePagadora>

O cabeçalho é obrigatório e todos os seus campos devem ser preenchidos. <header> <cpfCnpjFontePagadora> <nomeFontePagadora> <cpfBeneficiario>

<nomeBeneficiario> <anoExercicio> <anoCalendario> </header>

Todas as listas são opcionais no informe, mas se existirem devem possuir pelo menos um item. <listaRendimentosTributaveisRecebidosPessoaJuridica> <itemRendimentosTributaveisRecebidosPessoaJuridica> </listaRendimentosTributaveisRecebidosPessoaJuridica>

<listaPrevidenciaComplementar> <itemPrevidenciaComplementar> </listaPrevidenciaComplementar>

<listaPensaoAlimenticia> <itemPensaoAlimenticia> </listaPensaoAlimenticia>

<listaRendimentosIsentosNaoTributaveis> <itemRendimentosIsentosNaoTributaveis> </listaRendimentosIsentosNaoTributaveis>

<listaOutrosRendimentosIsentosNaoTributaveis> <itemOutrosRendimentosIsentosNaoTributaveis> </listaOutrosRendimentosIsentosNaoTributaveis>

<listaRendimentosSujeitosTributacaoExclusiva> <itemRendimentosSujeitosTributacaoExclusiva> </listaRendimentosSujeitosTributacaoExclusiva>

<listaOutrosRendimentosSujeitosTributacaoExclusiva> <itemOutrosRendimentosSujeitosTributacaoExclusiva> <listaOutrosRendimentosSujeitosTributacaoExclusiva>

<listaRendimentosRecebidosAcumuladamente>

<itemRendimentosRecebidosAcumuladamente> </listaRendimentosRecebidosAcumuladamente>

<listaPagamentos> <itemPagamentos> </listaPagamentos>

<listaRendimentosExigibilidadeSuspensa> <itemRendimentosExigibilidadeSuspensa> </listaRendimentosExigibilidadeSuspensa>

Rendimentos Tributáveis Recebidos Pessoa Jurídica Campo irrfDecimoTerceiro não é obrigatório, demais campos são obrigatórios, mesmo que os valores sejam zeros. <itemRendimentosTributaveisRecebidosPessoaJuridica> <totalRendimentoInclusiveFerias> <contribuicaoPrevidenciariaOficial> <impostoRetidoFonte> <decimoTerceiro> <irrfDecimoTerceiro> </itemRendimentosTributaveisRecebidosPessoaJuridica>

Previdência Complementar O campo valorContribuicaoPatrocinador não é obrigatório, demais campos são obrigatórios, mesmo que os valores sejam zeros. <itemPrevidenciaComplementar> <cnpjFundo> <nomeFundo> <tipoFundo> <valorPagoFundo> <valorContribuicaoPatrocinador > </itemPrevidenciaComplementar>

Pensão Alimentícia Campo cpfAlimentando é opcional, demais campos são obrigatórios, mesmo que os valores sejam

zeros <itemPensaoAlimenticia> <cpfAlimentando> <nomeAlimentando> <valorPagoPensaoAlimenticia> <valorDecimoTerceiroPensaoAlimenticia> </itemPensaoAlimenticia>

Rendimentos Isentos Não Tributáveis Os campos decimoTerceiro e contribuicaoPrevidenciariaOficial são opcionais, demais campos são obrigatórios, mesmo que os valores sejam zeros <itemRendimentosIsentosNaoTributaveis> <tipoRendimentoIsento> <valorRendimento> <decimoTerceiro> <contribuicaoPrevidenciariaOficial > </itemRendimentosIsentosNaoTributaveis>

Outros Rendimentos Isentos Não Tributáveis Todos os campos são obrigatórios, mesmo que os valores sejam zeros <itemOutrosRendimentosIsentosNaoTributaveis> <descricaoRendimento> <valorRendimento> </itemOutrosRendimentosIsentosNaoTributaveis>

Rendimentos Sujeitos Tributação Exclusiva Todos os campos são obrigatórios, mesmo que os valores sejam zeros <itemRendimentosSujeitosTributacaoExclusiva> <tipoRendimentoTributacaoExclusiva> <valorRendimento> </itemRendimentosSujeitosTributacaoExclusiva>

Outros Rendimentos Sujeitos Tributação Exclusiva Todos os campos são obrigatórios, mesmo que os valores sejam zeros <itemOutrosRendimentosSujeitosTributacaoExclusiva>

<descricaoRendimento> <valorRendimento> </itemOutrosRendimentosSujeitosTributacaoExclusiva>

Rendimentos Recebidos Acumuladamente Cada item de RRA poderá ter opcionalmente uma lista de Pensões Alimentícias Os campos numeroProcesso, valorRRAMolestiaGrave e listaPensaoAlimenticiaRRA são opcionais demais campos são obrigatórios, mesmo que os valores sejam zeros <itemRendimentosRecebidosAcumuladamente> <numeroProcesso> <numeroMeses> <mesRecebimento> <valorRendimento> <despesaComAcaoJudicial> <contribuicaoPrevidenciariaOficial> <impostoRetidoFonte> <valorRRAMolestiaGrave> <listaPensaoAlimenticiaRRA> </itemRendimentosRecebidosAcumuladamente>

<listaPensaoAlimenticiaRRA> <itemPensaoAlimenticiaRRA> </listaPensaoAlimenticiaRRA>

Pensão Alimentícia RRA Campo cpfAlimentando é opcional, demais campos são obrigatórios, mesmo que os valores sejam zerados <itemPensaoAlimenticiaRRA> <cpfAlimentando> <nomeAlimentando> <valorPago> </itemPensaoAlimenticiaRRA>

Pagamentos Campos cpfBeneficiarioServico, cpfcnpjPrestadorServico, nomePrestadorServico são opcionais,

demais campos são obrigatórios, mesmo que os valores sejam zerados <itemPagamentos> <cpfBeneficiarioServico> <nomeBeneficiarioServico> <cpfcnpjPrestadorServico> <nomePrestadorServico> <valorTotalPago> <valorReembolsado> </itemPagamentos>

Rendimentos Exigibilidade Suspensa Campo numeroProcessoRendimentoExigibilidadeSuspensa é opcional, demais campos são obrigatórios, mesmo que os valores sejam zerados <itemRendimentosExigibilidadeSuspensa> <numeroProcessoRendimentoExigibilidadeSuspensa> <valorRendimentoExigibilidadeSuspensa> <valorDepositosJudiciaisExigibilidadeSuspensa> </itemRendimentosExigibilidadeSuspensa>

PÁGINA DE AUTENTICAÇÃO

A Secretaria da Receita Federal do Brasil garante a integridade e a autenticidade deste documento nos termos do Art. 10, § 1º, da Medida Provisória nº 2.200-2, de 24 de agosto de 2001

Histórico de atividades sobre o documento:

Documento assinado digitalmente por: CLAUDIA MARIA DE ANDRADE em 29/02/2016. Confira o documento original pelo Smartphone conectado à Internet:

Dúvida? Acesse http://sadd.receita.fazenda.gov.br/sadd-internet/pages/qrcode.xhtml

Confira o documento original pela Internet:

a) Acesse o endereço: http://sadd.receita.fazenda.gov.br/sadd-internet/pages/validadocumento.xhtml

b) Digite o número abaixo ou leia o código de barras a seguir:

Código Hash obtido atraves do algoritmo SHA-256:

p/qvguc7qj6CgCVUwqVSAzSGlIUG0LJLbC71/v6Ir6Q=


ANEXO V - INSTRUÇÕES PARA PREENCHIMENTO DO COMPROVANTE DE PAGAMENTOS DE SAÚDE



ANEXO V INSTRUÇÕES PARA PREENCHIMENTO DO COMPROVANTE DE PAGAMENTOS DE SAÚDE

Os formatos dos campos utilizados no arquivo XML estão descritos no Anexo III.

Campos e seus tipos utilizados no informe do plano de saúde. Os tipos estão definidos no

Anexo III cpfBeneficiario - cpf nomeBeneficiario - nomePF anoExercicio - ano anoCalendario - ano cnpjPlanoSaude - cnpj nomePlanoSaude - nomePJ cpfBeneficiarioPagamentoPremio - cpfOpcional nomeBeneficiarioPagamentoPremio - nomePF valorPagoPagamentoPremio - valor cpfBeneficiarioReembolso - cpfOpcional nomeBeneficiarioReembolso - nomePF cpfcnpjPrestadorServico - cpfCnpjOpcional nomePrestadorServico - nomePJOpcional valorTotalPago - valor valorReembolsado - valor

Tipos definidos no Anexo III ano – ano com 4 dígitos valor – valor numérico com 11 dígitos e 2 casa decimais cpf – campo numérico com 11 dígitos cpfOpcional - campo opcional numérico com 11 dígitos cnpj - campo numérico com 14 dígitos cpfCnpjOpcional – campo opcional numérico com 11 ou 14 dígitos nomePF – Primeira letra maiúscula tamanho mínimo:1 tamanho máximo: 60 nomePJ - tamanho mínimo:1 tamanho máximo: 60 nomePJOpcional – tamanho mínimo:0 tamanho máximo: 60

Informações sobre o arquivo XML A tag inicial é informePlanoSaude. Ela é composta por: <informePlanoSaude> <header>

</informePlanoSaude>

O cabeçalho é obrigatório e todos os seus campos devem ser preenchidos. <header> <cnpjPlanoSaude> <nomePlanoSaude> <cpfBeneficiario> <nomeBeneficiario> <anoExercicio>

<anoCalendario> </header>

A listaPagamentoPremio é opcional, mas se existir deve possuir pelo menos um item.

<itemPagamentoPremio> </listaPagamentoPremio>

A listaReembolso é opcional, mas se existir deve possuir pelo menos um item.

<itemReembolso> </listaReembolso>

Pagamento Prêmio Campo cpfBeneficiarioPagamentoPremio é opcional, demais campos são obrigatórios, mesmo que o valor seja zero. <itemPagamentoPremio> <cpfBeneficiarioPagamentoPremio> <nomeBeneficiarioPagamentoPremio> <valorPagoPagamentoPremio> </itemPagamentoPremio>

Reembolso Campos cpfBeneficiarioReembolso, cpfcnpjPrestadorServico, nomePrestadorServico são opcionais, demais campos são obrigatórios, mesmo que os valores sejam zeros. <itemReembolso> <cpfBeneficiarioReembolso> <nomeBeneficiarioReembolso <cpfcnpjPrestadorServico> <nomePrestadorServico> <valorTotalPago> <valorReembolsado> </itemReembolso>

PÁGINA DE AUTENTICAÇÃO

A Secretaria da Receita Federal do Brasil garante a integridade e a autenticidade deste documento nos termos do Art. 10, § 1º, da Medida Provisória nº 2.200-2, de 24 de agosto de 2001

Histórico de atividades sobre o documento:

Documento assinado digitalmente por: CLAUDIA MARIA DE ANDRADE em 29/02/2016. Confira o documento original pelo Smartphone conectado à Internet:

Dúvida? Acesse http://sadd.receita.fazenda.gov.br/sadd-internet/pages/qrcode.xhtml

Confira o documento original pela Internet:

a) Acesse o endereço: http://sadd.receita.fazenda.gov.br/sadd-internet/pages/validadocumento.xhtml

b) Digite o número abaixo ou leia o código de barras a seguir:

Código Hash obtido atraves do algoritmo SHA-256:

5ZA/br6VsC9Egl5G5j9TOsYnZaD5c+Nwu7kReSw6oJc=

