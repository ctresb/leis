---
titulo: "RESOLUÇÃO Nº 119, DE 6 DE JULHO DE 2017"
orgao: "Presidência da República/CASA CIVIL/COMITÊ GESTOR DA INFRAESTRUTURA DE CHAVES PÚBLICAS"
tipo: "Resolução"
numero: "119"
data: 2017-07-06
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 19/07/2017, seção 1, p. 8"
data_publicacao: 2017-07-19
edicao: "137"
fonte: "https://www.in.gov.br/web/dou/-/resolucao-n-119-de-6-de-julho-de-2017-19183695"
sha256_html_fonte: 787e8d412f05d948ddac929ac5e83b6ae6fcdfdf87c82da8e808bfaba4f89947
baixado_em: 2026-10-27
---
# RESOLUÇÃO Nº 119, DE 6 DE JULHO DE 2017

RESOLUÇÃO Nº 119, DE 6 DE JULHO DE 2017

APROVA A OBRIGATORIEDADE DEREALIZAÇÃO DE AUDITORIAS WEBTRUSTPARA AC QUE EMITE CERTIFICADOPARA USUÁRIO FINAL E DEIMPLEMENTAÇÃO DE RESPOSTASOCSP PARA AC QUE EMITE CERTIFICADODO TIPO SSL/TLS NAS CADEIASDE CERTIFICAÇÃO DIGITALICP-BRASIL.

O COORDENADOR DO COMITÊ GESTOR DA IN-

FRAESTRUTURA DE CHAVES PÚBLICAS BRASILEIRA, nouso das atribuições que lhe confere o art. 6º, §1º, inc. III, do RegimentoInterno, torna público que o COMITÊ GESTOR DA INFRAESTRUTURADE CHAVES PÚBLICAS BRASILEIRA, noexercício das competências previstas no art. 4°, da Medida Provisórian° 2.200-2, de 24 de agosto de 2001, em reunião extraordináriarealizada em 06 de julho de 2017,

Considerando a necessidade de conformidade aos requisitosdo programa de raízes confiáveis para manutenção dos certificados daAC RAIZ da ICP-Brasil nos repositórios dos navegadores de internet,resolveu:

**Art. 1º** Alterar alínea "e" do item 7.1.2.2 do DOC-ICP-04,versão 6.1, que passa a vigorar com a seguinte redação:

e) "Authority Information Access", não crítica: A primeira

entrada deve conter o método de acesso id-ad-caIssuer, utilizando

um dos seguintes protocolos de acesso, HTTP, HTTPS ou LDAP,

para a recuperação da cadeia de certificação. A segunda entrada

deve conter o método de acesso id-ad-ocsp, com o respectivo

endereço do respondedor OCSP, utilizando um dos seguintes pro tocolosde acesso, HTTP, HTTPS ou LDAP, para certificados de

autenticação de servidor (SSL/TLS). Todos os outros tipos de

certificado podem conter essa segunda entrada. Essas extensões

somente são aplicáveis para certificados de usuário final.

**Art. 2º** Alterar o item 2.7.1 do DOC-ICP-05, versão 4.1, quepassa a vigorar com a seguinte redação:

2.7.1. As fiscalizações e auditorias realizadas no âmbito da

ICP-Brasil têm por objetivo verificar se os processos, proce dimentose atividades das entidades integrantes da ICP-Brasil

estão em conformidade com suas respectivas DPCs, PCs, PSs e

demais normas e procedimentos estabelecidos pela ICP-Brasil e

com os princípios e critérios definidos pelo We b Tr u s t .

**Art. 3º** Alterar o item 4.4.10 do DOC-ICP-05, versão 4.1,que passa a vigorar com a seguinte redação:

4.4.10. Requisitos para verificação de Certificados Revogados

4.4.10.1. Neste item a DPC deve observar que todo cer-

tificado deverá ter a sua validade verificada, na respectiva LCR

ou OCSP, antes de ser utilizado. ACs que emitem certificados

SSL devem suportar requisições OCSP em conformidade com a

RFC 6960 e/ou RFC5019. Para certificados SSL, a resposta

OCSP deve ter validade mínima de um dia e máxima de uma

semana, sendo que a próxima atualização deve estar disponível

na metade desse período.

4.4.10.2 A DPC deve observar, ainda, que a autenticidade da

LCR/OCSP deverá também ser confirmada por meio das ve rificaçõesda assinatura da AC emitente e do período de validade

da LCR/OCSP.

**Art. 4º** Alterar o item 6.1.1 do DOC-ICP-08, versão 4.1, quepassa a vigorar com a seguinte redação:

6.1.1 As auditorias têm por objetivo avaliar se os processos,

procedimentos, atividades e controles estão em conformidade

com as respectivas Políticas de Certificado, Declaração de Prá ticasde Certificação, Política de Segurança e demais normas e

procedimentos estabelecidos pelo Comitê Gestor da ICP-Brasil.

O documento ADE-ICP-08-E[6] detalha os processos que com põema cadeia de certificação e deverá nortear as auditorias

realizadas na cadeia da ICP-Brasil. Adicionalmente, as auditorias

do tipo 1 também devem avaliar os princípios e critérios de finidospelo We b Tr u s t .

**Art. 5º** Incluir a alínea "p" no item 4.2 do DOC-ICP-08,versão 4.1, com a seguinte redação:

p) certificação WebTrust para executar auditorias de Autori dadeCertificadoras - AC (WebTrust for Certification Authorities),

para entidades interessadas em realizar auditorias do Tipo 1.

**Art. 6º** Ficam aprovadas as novas versões dos Documentos:DOC-ICP-04 - REQUISITOS MÍNIMOS PARA AS POLÍTICAS DECERTIFICADO NA ICP-BRASIL (versão 6.2), DOC-ICP-05 - REQUISITOSMÍNIMOS PARA AS DECLARAÇÕES DE PRÁTICASDE CERTIFICAÇÃO DAS AUTORIDADES CERTIFICADORASDA ICP-BRASIL (versão 4.2) e DOC-ICP-08 - CRITÉRIOS E PROCEDIMENTOSPARA AUDITORIA DAS ENTIDADES INTEGRANTESDA ICP - BRASIL (versão 4.2).

**§ 1º** As demais cláusulas dos referidos documentos, nas suasversões imediatamente anteriores, em sua ordem originária, integramas presentes versões e mantêm-se válidas.

**§ 2º** Os documentos referidos no caput encontram-se disponibilizados,em sua totalidade, no sítio http://www.iti.gov.br.

**Art. 7º** As entidades da ICP-Brasil têm o prazo de até 180(cento e oitenta) dias, contados da data da publicação, para se adequaremàs mudanças previstas nos artigos 1º e 3º e até 18 (dezoito)meses para o artigos 2º, 4º e 5º.

**Art. 8º** Esta Resolução entra em vigor na data de sua publicação.

LUIZ CARLOS DE AZEVEDO

LUIZ CARLOS DE AZEVEDO

Este conteúdo não substitui o publicado na versão certificada.
