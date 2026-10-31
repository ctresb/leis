---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 225, DE 5 DE JANEIRO DE 2022"
orgao: "Banco Central do Brasil/Área de Organização do Sistema Financeiro e de Resolução/Departamento de Competição e de Estrutura do Mercado Financeiro"
tipo: "Instrução Normativa"
numero: "225"
data: 2022-01-05
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 10/01/2022, seção 1, p. 193"
data_publicacao: 2022-01-10
edicao: "6"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-225-de-5-de-janeiro-de-2022-372815465"
sha256_html_fonte: d4d3b9e61ec2a181ee3b43e0cf4fe8d2d77d6d68d87bd5413ed4f5c06e4318f5
baixado_em: 2026-10-20
---
# INSTRUÇÃO NORMATIVA BCB Nº 225, DE 5 DE JANEIRO DE 2022

INSTRUÇÃO NORMATIVA BCB Nº 225, DE 5 DE JANEIRO DE 2022

Divulga a versão 1.9 do Manual das Interfaces de Comunicação, que compõe o Regulamento do Pix.

O Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro (Decem), no uso das atribuições que lhe conferem os arts. 23, inciso I, alínea "a", e 97-A do Regimento Interno do Banco Central do Brasil, anexo à Portaria nº 84.287, de 27 de fevereiro de 2015, tendo em vista o disposto no art. 2º, inciso VIII, do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020, resolve:

**Art. 1º** Esta Instrução Normativa divulga a versão 1.9 do Manual das Interfaces de Comunicação, que compõe o Regulamento do Pix, conforme art. 2º do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020.

**Parágrafo único.** O Manual das Interfaces de Comunicação está disponível no endereço eletrônico do Banco Central do Brasil na internet, na página destinada aos manuais que compõem o Regulamento do Pix: https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Manual%20das%20Interfaces%20de%20Comunicacao-1.9.pdf.

**Art. 2º** Esta Instrução Normativa entra em vigor na data da sua publicação.

RICARDO PEREIRA DE ARAÚJO

Substituto

## ANEXO

Manual das Interfaces de Comunicação Versão 1.9

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Data</p></td>      <td rowspan="1" colspan="1"><p>Versão</p></td>      <td rowspan="1" colspan="1"><p>Descrição das alterações</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>14/11/2019</p></td>      <td rowspan="1" colspan="1"><p>1.0</p></td>      <td rowspan="1" colspan="1"><p>Versão inicial.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>17/01/2020</p></td>      <td rowspan="1" colspan="1"><p>1.1</p></td>      <td rowspan="1" colspan="1"><p>Conectividade:</p><p>- Inclusão de referência ao Manual de Redes da RSFN;</p><p>- Atualização do link para o Manual de Segurança RSFN;</p><p>- Detalhamento do comportamento do DNS.</p><p>Endpoints:</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>- Mudança da URL base de produção e inclusão da URL de homologação;</p><p>Endpoint Entrada:</p><p>- Esclarecimento sobre idem potência no envio de mensagens duplicadas.</p><p>Endpoint Saída:</p><p>- Esclarecimento sobre interrupção.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Diversos:</p><p>- Cabeçalhos SPI-ResourceId e SPI-PullNext alterados para PI-ResourceId e PI-PullNext.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>17/02/2020</p></td>      <td rowspan="1" colspan="1"><p>1.2</p></td>      <td rowspan="1" colspan="1"><p>Incluída a interface do DICT.</p><p>Renomeado o arquivo de "Manual da Interface de Comunicação" para "Manual das Interfaces de Comunicação".</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>28/07/2020</p></td>      <td rowspan="1" colspan="1"><p>1.3</p></td>      <td rowspan="1" colspan="1"><p>Retiradas referências ao documento de especificações e alterado o título e nome do arquivo.</p><p>DICT: Modificada a sessão do DICT para referenciar assinatura de mensagens.</p><p>ICOM:</p><p>- Remoção de "Transfer-Encoding: gzip, chunked" para envio compactado. Recomendação de uso de "ContentEncoding" para essa finalidade;</p><p>- Admitidos novos cabeçalhos;</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>- Adoção de envio e recebimento de múltiplas mensagens em uma mesma requisição (multipart);</p><p>- Incluído o endpoint Catálogo: versões das mensagens aceitas e enviadas pela API;</p><p>- Remoção da seção "Pendências".</p><p>ARQ: incluída documentação sobre o serviço de transferência de arquivos.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>12/08/2020</p></td>      <td rowspan="1" colspan="1"><p>1.4</p></td>      <td rowspan="1" colspan="1"><p>Alterado padrão visual.</p><p>Adicionada seção com dicas para melhoria de desempenho na leitura de mensagens em situação de carga.</p><p>Alteração nas portas HTTPS para os serviços ICOM e ARQ.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>19/08/2020</p></td>      <td rowspan="1" colspan="1"><p>1.5</p></td>      <td rowspan="1" colspan="1"><p>Correção na documentação de PI-ResourceId nos casos de requisições multipart no endpoint de saída.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>06/10/2020</p></td>      <td rowspan="1" colspan="1"><p>1.6</p></td>      <td rowspan="1" colspan="1"><p>API ARQ: informação sobre uso de cabeçalhos ETag, "ETag", "Last-Modified", "If-None-Match" e "If-ModifiedSince".</p><p>Cabeçalho Host deverá ser enviado sem a porta (ICOM, DICT e ARQ).</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>14/10/2020</p></td>      <td rowspan="1" colspan="1"><p>1.7</p></td>      <td rowspan="1" colspan="1"><p>Criação da seção 2.2.1.5 - Limitação da Quantidade Máxima de Transações Agendadas por Unidade de Tempo.</p><p>Ajuste pontual na definição do PI-Resource-ID, na seção 2.2.1.3.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>30/04/2021</p></td>      <td rowspan="1" colspan="1"><p>1.8</p></td>      <td rowspan="1" colspan="1"><p>Criação da seção 2.2.1.6 - Limitação de Tráfego de Mensagens e Operações.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>04/01/2022</p></td>      <td rowspan="1" colspan="1"><p>1.9</p></td>      <td rowspan="1" colspan="1"><p>Alteração nos valores da seção 2.2.1.5 - Limitação da quantidade máxima de transações agendadas por unidade de tempo.</p></td>     </tr>    </tbody>   </table>

NOTA

O Decreto nº 10.411, de 30 de junho de 2020, prevê a obrigatoriedade da realização de análise de impacto regulatório (AIR) para a edição de atos normativos de interesse geral produzidos pelos órgãos e entidades da administração pública federal direta e indireta.

Todavia, consoante se definiu no parágrafo 8 do Voto 280/2021-BCB, de 10 de novembro de 2021, o Regulamento do Pix, inclusive os demais documentos que o integram ou que o detalham e complementam, não se caracterizam como ato regulatório de força cogente, ostentando, em verdade, natureza eminentemente contratual; assim, modificações promovidas no referido regulamento e nos demais documentos que o integram ou que o detalham e complementam não se sujeitam à produção prévia de análise de impacto regulatório (AIR).

Dessa forma, fica a presente Instrução Normativa dispensada da prévia produção de AIR.
