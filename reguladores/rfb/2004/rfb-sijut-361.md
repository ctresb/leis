---
titulo: "Ato Declaratório Coana nº 2, de 13 de fevereiro de 2004"
orgao: "Coordenação-Geral de Administração Aduaneira"
tipo: "Ato Declaratório"
numero: "2"
data: "2004-02-13"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 16/02/2004, seção 1, página 16"
data_publicacao: "2004-02-16"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/361/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/361/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "361"
sha256_texto: "8caf48c66f05448647c86cc746acc3fa033873df5af44528e5acf50686cc66c4"
baixado_em: "2026-10-21"
---
# Ato Declaratório Coana nº 2, de 13 de fevereiro de 2004

Declara regras de formação do número identificador da carga importada.

OS COORDENADORES-GERAIS DE ADMINISTRAÇÃO ADUANEIRA E DE TECNOLOGIA E SEGURANÇA DA INFORMAÇÃO, tendo em vista o disposto no art. 4º da Instrução Normativa SRF nº 138, de 23 de novembro de 1998, declaram, em caráter normativo:

2\. Quando o número do conhecimento, na via marítima, fluvial e lacustre ou aérea, e o número do "house", na via aérea, superar 11 dígitos, deverão ser consideradas, para efeito de preenchimento, apenas as 11 primeiras posições, contadas a partir da direita.

3\. No caso de ocorrência de duplicidade de número identificador de carga, o emitente do conhecimento alterará o seu número, mediante carta de correção, obedecidas as disposições da Instrução Normativa - SRF nº 25, de 22 de janeiro de 1986, que deverá ser apresentada à unidade da SRF jurisdicionante do despacho da mercadoria.

3.1 Após a alteração de que trata este item, o depositário informará, nos termos do item 1 deste Ato, o novo número identificador da carga em custódia.

4\. Quando se tratar de carga objeto de descarregamento direto para local não alfandegado, a informação de disponibilidade deverá ser prestada pelo depositário responsável pelo local alfandegado de descarga.

5\. Para a informação da carga em custódia deverá ser utilizada a transmissão por meio de EDI (Electronic Data Interchange), obedecida a estrutura de dados constante do anexo I deste Ato.

6\. O importador fará constar, na ficha "Transporte" da Declaração de Importação, o número identificador da carga, informado pelo depositário, nos termos dos itens 1 a 4 deste Ato.

7\. Fica revogado o Ato Declaratório SRF/COANA/COTEC/nº 13, de 09 de março de 1999.

RONALDO LÁZARO MEDINA Coordenador-Geral de Administração Aduaneira Vítor Marcos Almeida Machado Coordenador-Geral de Tecnologia e Sistemas de Informação

## ANEXO I

LAYOUT DO ARQUIVO EDI

O arquivo a ser enviado pelo depositário, via EDI, é composto de um registro header e de um registro de disponibilidade da carga.

O tamanho de cada registro é de 40 bytes.

Registro Header

Posição de até Tam Form Alin Conteúdo do Campo Observações 01 01 01 N - Tipo de registro Conteúdo = 0 (zero) 02 08 07 N DZ Código do recinto alfandegado Tabela 61 do Siscomex 09 10 02 A - Código da VAN Tabela de VAN homologada pelo SERPRO 11 21 11 N DZ CPF de representante do recinto alfandegado 22 29 08 N - Data de envio AAAAMMDD 30 33 04 N DZ Horário de envio HHMM 34 40 07 A - Filler Brancos

<table>   <tbody><tr>    <td>    <p>Posição de até  </p>     </td>    <td>    <p>Tam  </p>    </td>    <td>    <p>Form  </p>    </td>     <td>    <p>Alin  </p>    </td>    <td>    <p>Conteúdo do Campo  </p>    </td>    <td>     <p>Observações  </p>    </td>    </tr>   <tr>    <td>    <p>01 01  </p>    </td>     <td>    <p>01  </p>    </td>    <td>    <p>N  </p>    </td>    <td>     <p>-  </p>    </td>    <td>    <p>Tipo de registro  </p>    </td>    <td>    <p>Conteúdo = 0 (zero)  </p>     </td>    </tr>   <tr>    <td>    <p>02 08  </p>    </td>    <td>    <p>07  </p>     </td>    <td>    <p>N  </p>    </td>    <td>    <p>DZ  </p>    </td>     <td>    <p>Código do recinto alfandegado  </p>    </td>    <td>    <p>Tabela 61 do Siscomex  </p>    </td>    </tr>    <tr>    <td>    <p>09 10  </p>    </td>    <td>    <p>02  </p>    </td>     <td>    <p>A  </p>    </td>    <td>    <p>-  </p>    </td>    <td>     <p>Código da VAN  </p>    </td>    <td>    <p>Tabela de VAN homologada pelo SERPRO  </p>    </td>    </tr>   <tr>     <td>    <p>11 21  </p>    </td>    <td>    <p>11  </p>    </td>    <td>     <p>N  </p>    </td>    <td>    <p>DZ  </p>    </td>    <td>    <p>CPF de representante do recinto alfandegado  </p>     </td>    <td>    <p>  </p>    </td>    </tr>   <tr>    <td>    <p>22 29  </p>     </td>    <td>    <p>08  </p>    </td>    <td>    <p>N  </p>    </td>     <td>    <p>-  </p>    </td>    <td>    <p>Data de envio  </p>    </td>    <td>     <p>AAAAMMDD  </p>    </td>    </tr>   <tr>    <td>    <p>30 33  </p>    </td>     <td>    <p>04  </p>    </td>    <td>    <p>N  </p>    </td>    <td>     <p>DZ  </p>    </td>    <td>    <p>Horário de envio  </p>    </td>    <td>    <p>HHMM  </p>     </td>    </tr>   <tr>    <td>    <p>34 40  </p>    </td>    <td>    <p>07  </p>     </td>    <td>    <p>A  </p>    </td>    <td>    <p>-  </p>    </td>     <td>    <p>Filler  </p>    </td>    <td>    <p>Brancos  </p>    </td>    </tr>   </tbody></table>

Registro de Disponibilidade da Carga

Posição de até Tam Form Alin Conteúdo do Campo Observações 01 01 01 N - Tipo de registro Conteúdo = 1 (um) 02 02 01 N - Código da via de transporte Tabela de via transporte 03 38 36 AN - Número identificador da carga\* 39 39 01 A - Tipo de Operação I - Inclusão E - Exclusão 40 40 01 A - Filler Brancos

<table>   <tbody><tr>     <td>    <p>Posição de até  </p>    </td>    <td>    <p>Tam  </p>    </td>    <td>     <p>Form  </p>    </td>    <td>    <p>Alin  </p>    </td>    <td>    <p>Conteúdo do Campo  </p>     </td>    <td>    <p>Observações  </p>    </td>    </tr>   <tr>    <td>    <p>01 01  </p>     </td>    <td>    <p>01  </p>    </td>    <td>    <p>N  </p>    </td>     <td>    <p>-  </p>    </td>    <td>    <p>Tipo de registro  </p>    </td>    <td>     <p>Conteúdo = 1 (um)  </p>    </td>    </tr>   <tr>    <td>    <p>02 02  </p>    </td>     <td>    <p>01  </p>    </td>    <td>    <p>N  </p>    </td>    <td>     <p>-  </p>    </td>    <td>    <p>Código da via de transporte  </p>    </td>    <td>    <p>Tabela de via transporte  </p>     </td>    </tr>   <tr>    <td>    <p>03 38  </p>    </td>    <td>    <p>36  </p>     </td>    <td>    <p>AN  </p>    </td>    <td>    <p>-  </p>    </td>     <td>    <p>Número identificador da carga*  </p>    </td>    <td>    <p>  </p>    </td>    </tr>    <tr>    <td rowspan="2">    <p>39 39  </p>    </td>    <td rowspan="2">    <p>01  </p>    </td>     <td rowspan="2">    <p>A  </p>    </td>    <td rowspan="2">    <p>-  </p>    </td>    <td rowspan="2">     <p>Tipo de Operação  </p>    </td>    <td>    <p>I - Inclusão  </p>    </td>    </tr>   <tr>     <td>    <p>E - Exclusão  </p>    </td>    </tr>   <tr>    <td>    <p>40 40  </p>     </td>    <td>    <p>01  </p>    </td>    <td>    <p>A  </p>    </td>     <td>    <p>-  </p>    </td>    <td>    <p>Filler  </p>    </td>    <td>     <p>Brancos  </p>    </td>    </tr>  </tbody></table>

\*Preenchimento do número identificador da Carga Via Marítima, Fluvial e Lacustre

Posição de até Tam Form Alin Conteúdo do Campo Observações 01 04 04 AN EB Código identificador do emissor do conhecimento 05 07 03 AN - Trigrama de identificação do porto de origem XXX 08 10 03 AN - Trigrama de identificação do porto de descarga XXX 11 18 08 N - Data de emissão do conhecimento DDMMAAAA 19 25 07 AN EB Código de identificação da embarcação (LRNUMBER) 26 36 11 AN EB Número do conhecimento

<table>   <tbody><tr>    <td>     <p>Posição de até  </p>    </td>    <td>    <p>Tam  </p>    </td>    <td>    <p>Form  </p>     </td>    <td>    <p>Alin  </p>    </td>    <td>    <p>Conteúdo do Campo  </p>    </td>     <td>    <p>Observações  </p>    </td>    </tr>   <tr>    <td>    <p>01 04  </p>     </td>    <td>    <p>04  </p>    </td>    <td>    <p>AN  </p>    </td>     <td>    <p>EB  </p>    </td>    <td>    <p>Código identificador do emissor do conhecimento  </p>    </td>    <td>     <p>  </p>    </td>    </tr>   <tr>    <td>    <p>05 07  </p>    </td>     <td>    <p>03  </p>    </td>    <td>    <p>AN  </p>    </td>    <td>     <p>-  </p>    </td>    <td>    <p>Trigrama de identificação do porto de origem  </p>    </td>    <td>    <p>XXX  </p>     </td>    </tr>   <tr>    <td>    <p>08 10  </p>    </td>    <td>    <p>03  </p>     </td>    <td>    <p>AN  </p>    </td>    <td>    <p>-  </p>    </td>     <td>    <p>Trigrama de identificação do porto de descarga  </p>    </td>    <td>    <p>XXX  </p>    </td>    </tr>    <tr>    <td>    <p>11 18  </p>    </td>    <td>    <p>08  </p>    </td>     <td>    <p>N  </p>    </td>    <td>    <p>-  </p>    </td>    <td>     <p>Data de emissão do conhecimento  </p>    </td>    <td>    <p>DDMMAAAA  </p>    </td>    </tr>   <tr>     <td>    <p>19 25  </p>    </td>    <td>    <p>07  </p>    </td>    <td>     <p>AN  </p>    </td>    <td>    <p>EB  </p>    </td>    <td>    <p>Código de identificação da embarcação (LRNUMBER)  </p>     </td>    <td>    <p>  </p>    </td>    </tr>   <tr>    <td>    <p>26 36  </p>     </td>    <td>    <p>11  </p>    </td>    <td>    <p>AN  </p>    </td>     <td>    <p>EB  </p>    </td>    <td>    <p>Número do conhecimento  </p>    </td>    <td>     <p>  </p>    </td>    </tr>  </tbody></table>

Via Aérea

Posição de até Tam Form Alin Conteúdo do Campo Observações 01 11 11 AN EB Número do conhecimento emitido pela companhia aérea 19 29 11 AN EB Número do "house" emitido pelo agen-te de carga Campo preenchido apenas quando se tratar de carga desconsolidada

<table>    <tbody><tr>    <td>    <p>Posição de até  </p>    </td>    <td>    <p>Tam  </p>    </td>     <td>    <p>Form  </p>    </td>    <td>    <p>Alin  </p>    </td>    <td>     <p>Conteúdo do Campo  </p>    </td>    <td>    <p>Observações  </p>    </td>    </tr>   <tr>     <td>    <p>01 11  </p>    </td>    <td>    <p>11  </p>    </td>    <td>     <p>AN  </p>    </td>    <td>    <p>EB  </p>    </td>    <td>    <p>Número do conhecimento emitido pela companhia aérea  </p>     </td>    <td>    <p>  </p>    </td>    </tr>   <tr>    <td>    <p>19 29  </p>     </td>    <td>    <p>11  </p>    </td>    <td>    <p>AN  </p>    </td>     <td>    <p>EB  </p>    </td>    <td>    <p>Número do "house" emitido pelo agen-te de    carga  </p>    </td>    <td>     <p>Campo preenchido apenas quando se tratar de carga    desconsolidada  </p>    </td>    </tr>  </tbody></table>

Via Ferroviária

Posição de até Tam Form Alin Conteúdo do Campo Observações 01 07 07 N DZ Código da Unidade da SRF de entrada da carga no país IN SRF 12/93 08 11 04 N - Ano de emissão do conhecimento AAAA 12 16 05 N DZ Número seqüencial IN SRF 12/93

<table>   <tbody><tr>    <td>     <p>Posição de até  </p>    </td>    <td>    <p>Tam  </p>    </td>    <td>    <p>Form  </p>     </td>    <td>    <p>Alin  </p>    </td>    <td>    <p>Conteúdo do Campo  </p>    </td>     <td>    <p>Observações  </p>    </td>    </tr>   <tr>    <td>    <p>01 07  </p>     </td>    <td>    <p>07  </p>    </td>    <td>    <p>N  </p>    </td>     <td>    <p>DZ  </p>    </td>    <td>    <p>Código da Unidade da SRF de entrada da carga no    país  </p>    </td>    <td>     <p>IN SRF    12/93  </p>    </td>    </tr>   <tr>    <td>    <p>08 11  </p>    </td>     <td>    <p>04  </p>    </td>    <td>    <p>N  </p>    </td>    <td>     <p>-  </p>    </td>    <td>    <p>Ano de emissão do conhecimento  </p>    </td>    <td>    <p>AAAA  </p>     </td>    </tr>   <tr>    <td>    <p>12 16  </p>    </td>    <td>    <p>05  </p>     </td>    <td>    <p>N  </p>    </td>    <td>    <p>DZ  </p>    </td>     <td>    <p>Número seqüencial  </p>    </td>    <td>    <p>IN SRF 12/93  </p>    </td>    </tr>   </tbody></table>

Via Rodoviária

Posição de até Tam Form Alin Conteúdo do Campo Observações 01 04 04 N - Ano de emissão do conhecimento AAAA 05 06 02 A - Código alfabético ISSO IN SNT/DpRF 58/91 07 11 05 N DZ Número do certificado de idoneidade ou número identificador do tipo de transporte IN SNT/DpRF58/91 12 16 05 N DZ Número do conhecimento ou número seqüencial, em ordem crescente, obtido junto à autoridade de transporte IN SNT/DpRF 58/91

<table>    <tbody><tr>    <td>    <p>Posição de até  </p>    </td>    <td>    <p>Tam  </p>    </td>     <td>    <p>Form  </p>    </td>    <td>    <p>Alin  </p>    </td>    <td>     <p>Conteúdo do Campo  </p>    </td>    <td>    <p>Observações  </p>    </td>    </tr>   <tr>     <td>    <p>01 04  </p>    </td>    <td>    <p>04  </p>    </td>    <td>     <p>N  </p>    </td>    <td>    <p>-  </p>    </td>    <td>    <p>Ano de emissão do conhecimento  </p>     </td>    <td>    <p>AAAA  </p>    </td>    </tr>   <tr>    <td>    <p>05 06  </p>     </td>    <td>    <p>02  </p>    </td>    <td>    <p>A  </p>    </td>     <td>    <p>-  </p>    </td>    <td>    <p>Código alfabético ISSO  </p>    </td>    <td>     <p>IN    SNT/DpRF 58/91  </p>    </td>    </tr>   <tr>    <td>    <p>07 11  </p>    </td>     <td>    <p>05  </p>    </td>    <td>    <p>N  </p>    </td>    <td>     <p>DZ  </p>    </td>    <td>    <p>Número do certificado de idoneidade ou número    identificador do tipo de transporte  </p>    </td>    <td>    <p>IN    SNT/DpRF58/91  </p>     </td>    </tr>   <tr>    <td>    <p>12 16  </p>    </td>    <td>    <p>05  </p>     </td>    <td>    <p>N  </p>    </td>    <td>    <p>DZ  </p>    </td>     <td>    <p>Número do conhecimento ou número seqüencial, em    ordem crescente, obtido junto à autoridade de transporte  </p>    </td>    <td>    <p>IN    SNT/DpRF 58/91  </p>    </td>    </tr>   </tbody></table>

Legenda

A - Alfabético

Alin - Alinhamento

AN - Alfanumérico

DZ - Alinhado à direita com zeros à esquerda

EB - Alinhado à esquerda com brancos à direita

Form - Formato

N - Numérico

Tam - Tamanho

Tabela de VAN homologada pelo SERPRO

AS - ASBACE EB - EMBRATEL

EB - MULTILINK

GE - GEIS

GS - GSI

IC - INTERCHANGE

MN - MEMONET

NS - NSI

PR - PROCEDA

SE - SERASA

TD - TELEDATA

Tabela de via de transporte

1 - Marítima, Fluvial e Lacustre

4 - Aérea

6 - Ferroviária

7 - Rodoviária

1\. Para os fins a que se referem os artigos 1º e 2º da Instrução Normativa SRF Nº 138, de 23 de novembro de 1998, serão utilizadas as seguintes regras de formação do número identificador da carga importada:

Via Marítima, Fluvial e Lacustre:

EEEEOOOPPPDDMMAAAAIIIIIIINNNNNNNNNNN(até 36 dígitos)

Via Marítima Descrição Tipo de campo Qtde.de dígitos EEEE código identificador do emissor do conhecimento alfanumérico 4 OOO trigrama de identificação do porto de origem(Código Internacional de Sinais-CIS da International Maritime Organization IMO) alfanumérico 3 PPP trigrama de identificação do porto de descarga (Código Internacional de Sinais - CIS da International Maritime Organization IMO) alfanumérico 3 DDMMAAAA data de emissão do conhecimento (dia, mês e ano) numérico 8 I I I I I I I código de identificação da embarcação LRNUMBER (Lloyd's Registrer of Shipping) alfanumérico 7 NNNNNNNNNNN No do conhecimento alfanumérico até 11

<table>   <tbody><tr>    <td>    <p>Via Marítima  </p>     </td>    <td>    <p>Descrição  </p>    </td>    <td>    <p>Tipo de campo  </p>    </td>     <td>    <p>Qtde.de dígitos  </p>    </td>    </tr>   <tr>    <td>    <p>EEEE  </p>     </td>    <td>    <p>código identificador do emissor do conhecimento  </p>    </td>    <td>    <p>alfanumérico  </p>    </td>     <td>    <p>4  </p>    </td>    </tr>   <tr>    <td>    <p>OOO  </p>     </td>    <td>    <p>trigrama de identificação do porto de origem(Código    Internacional de Sinais-CIS da International Maritime Organization IMO)  </p>    </td>    <td>    <p>alfanumérico  </p>    </td>     <td>    <p>3  </p>    </td>    </tr>   <tr>    <td>    <p>PPP  </p>     </td>    <td>    <p>trigrama de identificação do porto de descarga    (Código Internacional de Sinais - CIS da International Maritime Organization    IMO)  </p>    </td>    <td>    <p>alfanumérico  </p>    </td>     <td>    <p>3  </p>    </td>    </tr>   <tr>    <td>    <p>DDMMAAAA  </p>     </td>    <td>    <p>data de emissão do conhecimento (dia, mês e ano)  </p>    </td>    <td>    <p>numérico  </p>    </td>     <td>    <p>8  </p>    </td>    </tr>   <tr>    <td>    <p>I I I I I I I  </p>     </td>    <td>    <p>código de identificação da embarcação LRNUMBER    (Lloyd's Registrer of Shipping)  </p>    </td>    <td>    <p>alfanumérico  </p>    </td>     <td>    <p>7  </p>    </td>    </tr>   <tr>    <td>    <p>NNNNNNNNNNN  </p>     </td>    <td>    <p>No do conhecimento  </p>    </td>    <td>    <p>alfanumérico  </p>    </td>     <td>    <p>até 11  </p>    </td>    </tr>  </tbody></table>

Via Aérea: CCCCCCCCCCCHHHHHHHHHHH (até 22 dígitos)

ViaAérea Descrição Tipo de campo Qtde.de dígitos CCCCCCCCCCC Número do conhecimento emitido pela companhia aérea alfanumérico até 11 HHHHHHHHHHH Número do "house" emitido pelo agente de carga, se houver desconsolidação da carga alfanumérico até 11

<table>   <tbody><tr>    <td>     <p>ViaAérea  </p>    </td>    <td>    <p>Descrição  </p>    </td>    <td>    <p>Tipo de campo  </p>     </td>    <td>    <p>Qtde.de dígitos  </p>    </td>    </tr>   <tr>    <td>    <p>CCCCCCCCCCC  </p>     </td>    <td>    <p>Número do conhecimento emitido pela companhia aérea  </p>    </td>    <td>    <p>alfanumérico  </p>    </td>     <td>    <p>até 11  </p>    </td>    </tr>   <tr>    <td>    <p>HHHHHHHHHHH  </p>     </td>    <td>    <p>Número do "house" emitido pelo agente de    carga, se houver desconsolidação da carga  </p>    </td>    <td>    <p>alfanumérico  </p>    </td>     <td>    <p>até 11  </p>    </td>    </tr>  </tbody></table>

Via Ferroviária: UUUUUUUAAAANNNNN (16 dígitos)

Via Ferroviária Descrição Tipo de campo Qtde.de dígitos UUUUUUU Código da Unidade da SRF (tabela 60 do SISCOMEX) de entrada da carga no país (IN SRF Nº 12/93) numérico 7 AAAA Ano de emissão do conhecimento numérico 4 NNNNN número seqüencial e anual a ser gerado pela unidade da SRF de entrada para o TIF/DTA (IN-SRF Nº 12/93) numérico 5

<table>   <tbody><tr>    <td>    <p>Via Ferroviária  </p>    </td>    <td>    <p>Descrição  </p>     </td>    <td>    <p>Tipo de campo  </p>    </td>    <td>    <p>Qtde.de    dígitos  </p>    </td>     </tr>   <tr>    <td>    <p>UUUUUUU     </p>    </td>    <td>    <p>Código da Unidade da SRF (tabela 60 do SISCOMEX) de    entrada da carga no país (IN SRF Nº 12/93)  </p>     </td>    <td>    <p>numérico  </p>    </td>    <td>    <p>7  </p>    </td>     </tr>   <tr>    <td>    <p>AAAA  </p>    </td>    <td>    <p>Ano de emissão do conhecimento  </p>     </td>    <td>    <p>numérico  </p>    </td>    <td>    <p>4  </p>    </td>     </tr>   <tr>    <td>    <p>NNNNN  </p>    </td>    <td>    <p>número seqüencial e anual a ser gerado pela unidade    da SRF de entrada para o TIF/DTA (IN-SRF Nº 12/93)  </p>     </td>    <td>    <p>numérico  </p>    </td>    <td>    <p>5  </p>    </td>     </tr>  </tbody></table>

Via Rodoviária: AAAAPPCCCCCNNNNN (16 dígitos)

Via Rodoviária Descrição Tipo de campo Qtde.de dígitos AAAA ano de emissão do conhecimento numérico 4 PP código alfabético ISSO Alfa-2 correspondente ao país de partida da operação de transporte internacional (IN-SNT/DpRF Nº 58/91) alfabético 2 CCCCC número do certificado de idoneidade (permissão original) outorgado pela autoridade de transporte ou, se carga em transporte próprio ou ocasional, número identificador do tipo de transporte (99999 próprio, 99998 ocasional) (IN-SNT/DpRF Nº 58/91) numérico 5 NNNNN número do conhecimento ou, no caso de transporte próprio ou ocasional, número seqüencial em ordem crescente obtido junto à autoridade de transporte (IN-SNT/DpRF Nº 58/91) numérico 5

<table>   <tbody><tr>    <td>    <p>Via Rodoviária  </p>    </td>    <td>    <p>Descrição  </p>     </td>    <td>    <p>Tipo de campo  </p>    </td>    <td>    <p>Qtde.de dígitos  </p>    </td>     </tr>   <tr>    <td>    <p>AAAA  </p>    </td>    <td>    <p>ano de emissão do conhecimento  </p>     </td>    <td>    <p>numérico  </p>    </td>    <td>    <p>4  </p>    </td>     </tr>   <tr>    <td>    <p>PP  </p>    </td>    <td>    <p>código alfabético ISSO Alfa-2 correspondente ao    país de partida da operação de transporte internacional (IN-SNT/DpRF Nº    58/91)  </p>     </td>    <td>    <p>alfabético  </p>    </td>    <td>    <p>2  </p>    </td>     </tr>   <tr>    <td>    <p>CCCCC  </p>    </td>    <td>    <p>número do certificado de idoneidade (permissão    original) outorgado pela autoridade de transporte ou, se carga em transporte    próprio ou ocasional, número identificador do tipo de transporte (99999    próprio, 99998 ocasional) (IN-SNT/DpRF Nº 58/91)  </p>     </td>    <td>    <p>numérico    </p>    </td>    <td>    <p>5  </p>     </td>    </tr>   <tr>    <td>    <p>NNNNN  </p>    </td>    <td>    <p>número do conhecimento ou, no caso de transporte    próprio ou ocasional, número seqüencial em ordem crescente obtido junto à    autoridade de transporte (IN-SNT/DpRF Nº 58/91)  </p>     </td>    <td>    <p>numérico   </p>    </td>    <td>    <p>5  </p>    </td>     </tr>  </tbody></table>
