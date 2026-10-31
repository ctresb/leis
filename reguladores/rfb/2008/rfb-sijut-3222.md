---
titulo: "Ato Declaratório Executivo Corep nº 2, de 20 de março de 2008"
orgao: "Coordenação Especial de Vigilância e Repressão"
tipo: "Ato Declaratório Executivo"
numero: "2"
data: "2008-03-20"
revogada: false
evidencia_revogacao: "vigente:true"
vigente_fonte: true
versao_texto: "publicação original — visão original da fonte"
publicacao: "Publicado(a) no DOU de 26/03/2008, seção 1, página 24"
data_publicacao: "2008-03-26"
fonte: "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/3222/visao/original"
fonte_api: "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/3222/visao/original"
fonte_indice: "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
id_rfb: "3222"
sha256_texto: "991129df4ef7cbddf5bbf4632cd21d4a673d0071567442a1fc55a1ae7d5af306"
baixado_em: "2026-10-21"
---
# Ato Declaratório Executivo Corep nº 2, de 20 de março de 2008

Dispõe sobre regras de formação do Número Identificador da Carga (NIC) importada e a prestação da sua informação.

O COORDENADOR ESPECIAL DE VIGILÂNCIA E REPRESSÃO, no uso das atribuições que lhe confere o art. 116 do Regimento Interno da Secretaria da Receita Federal do Brasil, aprovado pela Portaria MF nº 95, de 30 de abril de 2007, e tendo em vista o disposto no art. 5º da Instrução Normativa SRF nº 680, de 2 de outubro de 2006, declara:

**Art. 1º** As regras de formação do Número Identificador da Carga (NIC) importada são as constantes do Anexo I a este Ato Declaratório Executivo.

**Art. 2º** A informação do NIC observará as seguintes regras:

I - no caso de via aérea, serão considerados apenas os 11 (onze) primeiros dígitos de cada campo;

II - no caso de carga marítima, o sistema somente permitirá o registro do NIC se o Número do Conhecimento Eletrônico (CE) existir no sistema Mercante e não estiver bloqueado para armazenamento no sistema Carga.

III - o depositário responsável pelo local alfandegado de descarga também registrará NIC para as cargas objeto de descarregamento direto para local não alfandegado;

IV - a transmissão por meio de EDI (Electronic Data Interchange) obedecerá à estrutura de dados constante do Anexo II;

V - o importador informará o NIC na Declaração de Importação (DI) ou na Declaração Simplificada de Importação (DSI);

VI - o registro de Declarações de Trânsito Aduaneiro (DTA) dos tipos DTA-EC, DTA-EE, DTA-PC e MIC-P para cargas aquaviárias é condicionado à existência do CE no sistema Mercante e, quando se tratar de trânsito com armazenamento na origem, a sua disponibilidade no Siscomex.

**Art. 3º** Este Ato Declaratório Executivo entra em vigor na data de sua publicação, produzindo efeitos a partir do dia 31 de março de 2008.

MAURO DE BRITO

ANEXO I  
REGRAS DE FORMAÇÃO DO NIC

a) Via Marítima: EEEEEEEEEEDDMMAAAANNNNNNNNNNNNNNNBBB (até 36 dígitos),

<table>   <tr>    <td>    <p>Via Marítima</p>    </td>    <td>    <p>Descrição</p>    </td>    <td>    <p>Tipo de campo</p>    </td>    <td>    <p>Qtde.de dígitos</p>    </td>   </tr>   <tr>    <td>    <p>EEEEEEEEEE</p>    </td>    <td>    <p>com preenchimento    fixo-ALFA = "CEMERCANTE"</p>    </td>    <td>    <p>alfa</p>    </td>    <td>    <p>10</p>    </td>   </tr>   <tr>    <td>    <p>DDMMAAAA</p>    </td>    <td>    <p>com preenchimento    fixo-numérico = 31032008</p>    </td>    <td>    <p>numérico</p>    </td>    <td>    <p>8</p>    </td>   </tr>   <tr>    <td>    <p>NNNNNNNNNNNNNNN</p>    </td>    <td>    <p>Número do    Conhecimento Eletrônico (CE) gerado para a carga no sistema Mercante</p>    </td>    <td>    <p>numérico</p>    </td>    <td>    <p>15</p>    </td>   </tr>   <tr>    <td>    <p>BBB</p>    </td>    <td>    <p>Posições livres e que    devem permanecer em branco</p>    </td>    <td>    <p>alfanumérico</p>    </td>    <td>    <p>3</p>    </td>   </tr>  </table>

b) Via Aérea: CCCCCCCCCCCHHHHHHHHHHH (até 22 dígitos)

<table>   <tr>    <td>    <p>Via    Aérea</p>    </td>    <td>    <p>Descrição</p>    </td>    <td>    <p>Tipo de    campo</p>    </td>    <td>    <p>Qtde.de    dígitos</p>    </td>   </tr>   <tr>    <td>    <p>CCCCCCCCCCC</p>    </td>    <td>    <p>Número    do conhecimento emitido pela companhia aérea</p>    </td>    <td>    <p>alfanumérico</p>    </td>    <td>    <p>até 11</p>    </td>   </tr>   <tr>    <td>    <p>HHHHHHHHHHH</p>    </td>    <td>    <p>Número    do "house" emitido pelo agente de carga quando houver    desconsolidação da carga.</p>    </td>    <td>    <p>alfanumérico</p>    </td>    <td>    <p>até 11</p>    </td>   </tr>  </table>

c) Via Ferroviária: UUUUUUUAAAANNNNN (16 dígitos)

<table>   <tr>    <td>    <p>Via    Ferroviária</p>    </td>    <td>    <p>Descrição</p>    </td>    <td>    <p>Tipo de campo</p>    </td>    <td>    <p>Qtde.de dígitos</p>    </td>   </tr>   <tr>    <td>    <p>UUUUUUU</p>    </td>    <td>    <p>Código    da Unidade da RFB (tabela 60 do Siscomex) de entrada da carga no País (IN SRF    Nº 12, de 1993).</p>    </td>    <td>    <p>numérico</p>    </td>    <td>    <p>7</p>    </td>   </tr>   <tr>    <td>    <p>AAAA</p>    </td>    <td>    <p>Ano de    emissão do conhecimento</p>    </td>    <td>    <p>numérico</p>    </td>    <td>    <p>4</p>    </td>   </tr>   <tr>    <td>    <p>NNNNN</p>    </td>    <td>    <p>Número    seqüencial e anual a ser gerado pela unidade da RFB de entrada para o TIF/DTA    (IN SRF Nº 12, de 1993).</p>    </td>    <td>    <p>numérico</p>    </td>    <td>    <p>5</p>    </td>   </tr>  </table>

d) Via Rodoviária: AAAAPPCCCCCNNNNN (16 dígitos)

<table>   <tr>    <td>    <p>Via    Rodoviária</p>    </td>    <td>    <p>Descrição</p>    </td>    <td>    <p>Tipo de    campo</p>    </td>    <td>    <p>Qtde.de    dígitos</p>    </td>   </tr>   <tr>    <td>    <p>AAAA</p>    </td>    <td>    <p>Ano de    emissão do conhecimento</p>    </td>    <td>    <p>numérico</p>    </td>    <td>    <p>4</p>    </td>   </tr>   <tr>    <td>    <p>PP</p>    </td>    <td>    <p>Código    alfabético ISSO Alfa-2 correspondente ao país de partida da operação de    transporte internacional (IN SNT/DpRF Nº 58, de 1991)</p>    </td>    <td>    <p>alfabético</p>    </td>    <td>    <p>2</p>    </td>   </tr>   <tr>    <td>    <p>CCCCC</p>    </td>    <td>    <p>Número    do certificado de idoneidade (permissão original) outorgado pela autoridade    de transporte ou, se carga em transporte próprio ou ocasional, número    identificador do tipo de transporte (99999 próprio, 99998 ocasional) (IN    SNT/DpRF Nº 58, de 1991)</p>    </td>    <td>    <p>numérico</p>    </td>    <td>    <p>5</p>    </td>   </tr>   <tr>    <td>    <p>NNNNN</p>    </td>    <td>    <p>número    do conhecimento ou, quando transporte próprio ou ocasional, número seqüencial    em ordem crescente obtido junto à autoridade de transporte (IN SNT/DpRF Nº    58, de 1991)</p>    </td>    <td>    <p>numérico</p>    </td>    <td>    <p>5</p>    </td>   </tr>  </table>

ANEXO II  
REGRAS DE LAYOUT DO ARQUIVO EDI

O arquivo enviado via EDI, pelo depositário, é composto de um registro header e de um registro de disponibilidade da carga.O tamanho de cada registro é de 40 bytes.

a) Registro Header

<table>   <tr>    <td>    <p>Posição de até</p>    </td>    <td>    <p>Tam</p>    </td>    <td>    <p>Form</p>    </td>    <td>    <p>Alin</p>    </td>    <td>    <p>Conteúdo do Campo</p>    </td>    <td>    <p>Observações</p>    </td>   </tr>   <tr>    <td>    <p>01    01</p>    </td>    <td>    <p>01</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Tipo de registro</p>    </td>    <td>    <p>Conteúdo = 0 (zero)</p>    </td>   </tr>   <tr>    <td>    <p>02    08</p>    </td>    <td>    <p>07</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>DZ</p>    </td>    <td>    <p>Código do recinto    alfandegado</p>    </td>    <td>    <p>Tabela 61 do Siscomex</p>    </td>   </tr>   <tr>    <td>    <p>09    10</p>    </td>    <td>    <p> 02</p>    </td>    <td>    <p> A</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Código da Van</p>    </td>    <td>    <p>Tabela de Van    homologada pelo Serpro</p>    </td>   </tr>   <tr>    <td>    <p>11    21</p>    </td>    <td>    <p>11</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>DZ</p>    </td>    <td>    <p>CPF de representante    do recinto alfandegado</p>    </td>    <td>    <p> </p>    </td>   </tr>   <tr>    <td>    <p>22     29</p>    </td>    <td>    <p>08</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Data de envio</p>    </td>    <td>    <p>AAAAMMDD</p>    </td>   </tr>   <tr>    <td>    <p>30     33</p>    </td>    <td>    <p>04</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>DZ</p>    </td>    <td>    <p>Horário de envio</p>    </td>    <td>    <p>HHMM</p>    </td>   </tr>   <tr>    <td>    <p>34  40</p>    </td>    <td>    <p>07</p>    </td>    <td>    <p>A</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Filler</p>    </td>    <td>    <p>Brancos</p>    </td>   </tr>  </table>

b) Registro de Disponibilidade da Carga

<table>   <tr>    <td>    <p>Posição de até</p>    </td>    <td>    <p>Tam</p>    </td>    <td>    <p>Form</p>    </td>    <td>    <p>Alin</p>    </td>    <td>    <p>Conteúdo do Campo</p>    </td>    <td>    <p>Observações</p>    </td>   </tr>   <tr>    <td>    <p>01 01</p>    </td>    <td>    <p>01</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Tipo de registro</p>    </td>    <td>    <p>Conteúdo = 1 (um)</p>    </td>   </tr>   <tr>    <td>    <p>02 02</p>    </td>    <td>    <p>01</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Código da via de    transporte</p>    </td>    <td>    <p>Tabela de via    transporte</p>    </td>   </tr>   <tr>    <td>    <p>03 38</p>    </td>    <td>    <p>36</p>    </td>    <td>    <p>AN</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Número identificador    da carga (NIC)*</p>    </td>    <td>    <p> </p>    </td>   </tr>   <tr>    <td>    <p>39 39</p>    </td>    <td>    <p>01</p>    </td>    <td>    <p>A</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Tipo de Operação</p>    </td>    <td>    <p>I - Inclusão E - Exclusão</p>    </td>   </tr>   <tr>    <td>    <p>40 40</p>    </td>    <td>    <p>01</p>    </td>    <td>    <p>A</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Filler</p>    </td>    <td>    <p>Brancos</p>    </td>   </tr>  </table>

\*Preenchimento do NIC

c) Via Marítima

<table>   <tr>    <td>    <p>Posição de até</p>    </td>    <td>    <p>Tam</p>    </td>    <td>    <p>Form</p>    </td>    <td>    <p>Alin</p>    </td>    <td>    <p>Conteúdo do Campo</p>    </td>    <td>    <p>Observações</p>    </td>   </tr>   <tr>    <td>    <p>01    10</p>    </td>    <td>    <p>10</p>    </td>    <td>    <p>A</p>    </td>    <td>    <p>EB</p>    </td>    <td>    <p>CEMERCANTE</p>    </td>    <td>    <p>Campo fixo</p>    </td>   </tr>   <tr>    <td>    <p>11    18</p>    </td>    <td>    <p>08</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>31032008</p>    </td>    <td>    <p>Campo fixo</p>    </td>   </tr>   <tr>    <td>    <p>19    33</p>    </td>    <td>    <p>15</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Número do Conhecimento    eletrônico (CE)</p>    </td>    <td>    <p>Campo variável</p>    </td>   </tr>   <tr>    <td>    <p>34    36</p>    </td>    <td>    <p>03</p>    </td>    <td>    <p>AN</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Campo em branco</p>    </td>    <td>    <p>Campo em branco</p>    </td>   </tr>  </table>

d) Via Aérea

<table>   <tr>    <td>    <p>Posição    de até</p>    </td>    <td>    <p>Tam</p>    </td>    <td>    <p>Form</p>    </td>    <td>    <p>Alin</p>    </td>    <td>    <p>Conteúdo    do Campo</p>    </td>    <td>    <p>Observações</p>    </td>   </tr>   <tr>    <td>    <p>01 11</p>    </td>    <td>    <p>11</p>    </td>    <td>    <p>AN</p>    </td>    <td>    <p>EB</p>    </td>    <td>    <p>Número    do conhecimento emitido pela companhia aérea</p>    </td>    <td>    <p> </p>    </td>   </tr>   <tr>    <td>    <p>19 29</p>    </td>    <td>    <p>11</p>    </td>    <td>    <p>AN</p>    </td>    <td>    <p>EB</p>    </td>    <td>    <p>Número    do "house" emitido pelo agente de carga</p>    </td>    <td>    <p>Campo    preenchido apenas quando se tratar de carga desconsolidada</p>    </td>   </tr>  </table>

e) Via Ferroviária

<table>   <tr>    <td>    <p>Posição    de até</p>    </td>    <td>    <p>Tam</p>    </td>    <td>    <p>Form</p>    </td>    <td>    <p>Alin</p>    </td>    <td>    <p>Conteúdo    do Campo</p>    </td>    <td>    <p>Observações</p>    </td>   </tr>   <tr>    <td>    <p>01 07</p>    </td>    <td>    <p>07</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>DZ</p>    </td>    <td>    <p>Código    da Unidade da RFB de entrada da carga no País</p>    </td>    <td>    <p>Instrução    Normativa SRF nº 12, de 25 de janeiro de 1993.</p>    </td>   </tr>   <tr>    <td>    <p>08 11</p>    </td>    <td>    <p>04</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Ano de    emissão do conhecimento</p>    </td>    <td>    <p>AAAA</p>    </td>   </tr>   <tr>    <td>    <p>12 16</p>    </td>    <td>    <p>05</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>DZ</p>    </td>    <td>    <p>Número    seqüencial</p>    </td>    <td>    <p>Instrução    Normativa SRF nº 12, de 25 de janeiro de 1993.</p>    </td>   </tr>  </table>

f)Via Rodoviária

<table>   <tr>    <td>    <p>Posição    de até</p>    </td>    <td>    <p>Tam</p>    </td>    <td>    <p>Form</p>    </td>    <td>    <p>Alin</p>    </td>    <td>    <p>Conteúdo    do Campo</p>    </td>    <td>    <p>Observações</p>    </td>   </tr>   <tr>    <td>    <p>01 04</p>    </td>    <td>    <p>04</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Ano de    emissão do conhecimento</p>    </td>    <td>    <p>AAAA</p>    </td>   </tr>   <tr>    <td>    <p>05  06</p>    </td>    <td>    <p>02</p>    </td>    <td>    <p>A</p>    </td>    <td>    <p>-</p>    </td>    <td>    <p>Código    alfabético ISSO</p>    </td>    <td>    <p>Instrução    Normativa Conjunta SNT/DpRF nº 58, de 27 de agosto de 1991.</p>    </td>   </tr>   <tr>    <td>    <p>07 11</p>    </td>    <td>    <p>05</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>DZ</p>    </td>    <td>    <p>Número    do certificado de idoneidade ou número identificador do tipo de transporte</p>    </td>    <td>    <p>Instrução    Normativa Conjunta SNT/DpRF nº 58, de 27 de agosto de 1991.</p>    </td>   </tr>   <tr>    <td>    <p>12  16</p>    </td>    <td>    <p>05</p>    </td>    <td>    <p>N</p>    </td>    <td>    <p>DZ</p>    </td>    <td>    <p>Número    do conhecimento ou número seqüencial, em ordem crescente, obtido junto à    autoridade de transporte.</p>    </td>    <td>    <p>Instrução    Normativa Conjunta SNT/DpRF nº 58, de 27 de agosto de 1991.</p>    </td>   </tr>  </table>

g) tabela auxiliar para envio dos dados

<table>   <tr>    <td>    <p>Legenda</p>    </td>    <td>    <p>VAN    homologada    pelo SERPRO</p>    </td>    <td>    <p>Vias de transporte</p>    </td>   </tr>   <tr>    <td>    <p>A    -Alfabético</p>    <p>Alin - Alinhamento</p>    <p>AN    - Alfanumérico</p>    <p>DZ    - Alinhado    à direita com zeros à esquerda</p>    <p>EB    - Alinhado    à esquerda com brancos à direita</p>    <p>Form - Formato</p>    <p>N    - Numérico</p>    <p>Tam - Tamanho</p>    </td>    <td>    <p>AS    - ASBACE</p>    <p>EB    - EMBRATEL </p>    <p>EB    - MULTILINK </p>    <p>GE  -    GEIS </p>    <p>GS    - GSI </p>    <p>IC  -    INTERCHANGE </p>    <p> </p>    <p>MN    - MEMONET</p>    <p>NS    - NSI</p>    <p>PR    - PROCEDA</p>    <p>SE    - SERASA</p>    </td>    <td>    <p>1    - Marítima</p>    <p>4    - Aérea</p>    <p>6    - Ferroviária</p>    <p>7    - Rodoviária</p>    </td>   </tr>  </table>
