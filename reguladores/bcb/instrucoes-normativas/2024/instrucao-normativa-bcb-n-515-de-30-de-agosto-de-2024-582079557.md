---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 515, DE 30 DE AGOSTO DE 2024"
orgao: "Banco Central do Brasil/Área de Organização do Sistema Financeiro e de Resolução/Departamento de Competição e de Estrutura do Mercado Financeiro"
tipo: "Instrução Normativa"
numero: "515"
data: 2024-08-30
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 03/09/2024, seção 1, p. 101"
data_publicacao: 2024-09-03
edicao: "170"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-515-de-30-de-agosto-de-2024-582079557"
sha256_html_fonte: 249a983f52e84f1a9bdd80ed8dc218d8a5e5d10e5f70bcd41c54c3e0705c8b13
baixado_em: 2026-10-16
---
# INSTRUÇÃO NORMATIVA BCB Nº 515, DE 30 DE AGOSTO DE 2024

INSTRUÇÃO NORMATIVA BCB Nº 515, DE 30 DE AGOSTO DE 2024

Divulga a versão 2.0 do Manual de Fluxos do Processo de Efetivação do Pix, que compõe o Regulamento do Pix.

O Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro (Decem), no uso das atribuições que lhe conferem os arts. 23, caput, inciso I, alínea "a", e 94, caput, inciso IX, do Regimento Interno do Banco Central do Brasil, anexo à Resolução BCB nº 340, de 21 de setembro de 2023, e tendo em vista o disposto no art. 2º, caput, inciso III, do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020, resolve:

**Art. 1º** Esta Instrução Normativa divulga a versão 2.0 do Manual de Fluxos do Processo de Efetivação do Pix, que compõe o Regulamento do Pix, conforme art. 2º do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020.

**Parágrafo único.** O Manual de Fluxos do Processo de Efetivação do Pix está disponível no endereço eletrônico do Banco Central do Brasil na internet, na página destinada aos manuais que compõem o Regulamento do Pix: https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento\_Pix/versoes\_futuras/III\_ManualdeFluxosdoProcessodeEfetivacaodoPix-versao2-0.pdf.

**Art. 2º** Fica revogada a Instrução Normativa BCB nº 368, de 31 de março de 2024.

**Art. 3º** Esta Instrução Normativa entra em vigor na data da sua publicação.

Ricardo Teixeira Leite Mourão

## ANEXO

Manual de Manual de Fluxos do Processo de Efetivação do Pix Versão 2.0

Histórico de revisão

<table>    <tbody>     <tr></tr>     <tr>      <td rowspan="1" colspan="1"><p>Data</p></td>      <td rowspan="1" colspan="1"><p>Versão</p></td>      <td rowspan="1" colspan="1"><p>Descrição das alterações</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>11/8/2020</p></td>      <td rowspan="1" colspan="1"><p>1.0</p></td>      <td rowspan="1" colspan="1"><p>Versão inicial.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>10/9/2020</p></td>      <td rowspan="1" colspan="1"><p>1.1</p></td>      <td rowspan="1" colspan="1"><p>Ajuste no fluxo 2.3, sobre a geração da ordem de pagamento por QR Code dinâmico. Fluxo é exatamente igual ao fluxo de geração da ordem de pagamento por QR Code estático. Após o usuário pagador ler o QR Code dinâmico, PSP do pagador envia a chave contida no payload do QR para o DICT. Após retorno do DICT, PSP do pagador apresenta as informações do payload e as informações do usuário recebedor para o usuário pagador, solicitando confirmação do pagamento.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>22/7/2021</p></td>      <td rowspan="1" colspan="1"><p>1.2</p></td>      <td rowspan="1" colspan="1"><p>Estrutura: inserção da subseção 2.1.3 "Prestador de serviço de iniciação de transação de pagamento, com acesso direto ao DICT".</p><p>Estrutura: inserção da subseção 2.4 "Geração da ordem de pagamento pelo serviço de iniciação de transação de pagamento, nos casos em que o participante possui todas as informações do usuário recebedor".</p><p>Seção 2.3: detalhamento da tabela de passo a passo, para explicitar melhor o processo de geração da ordem por QR Code dinâmico.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>29/9/2021</p></td>      <td rowspan="1" colspan="1"><p>1.3</p></td>      <td rowspan="1" colspan="1"><p>Ajuste no fluxo 2.2 "Geração da ordem de pagamento por QR Code estático" e na tabela.</p><p>Estrutura: inserção da subseção 2.3.1 "Pix Cobrança para pagamento imediato".</p><p>Estrutura: inserção da subseção 2.3.2 "Pix Cobrança para pagamento com vencimento".</p><p>Estrutura: inserção da seção 2.4 "Geração da ordem de pagamento de um Pix Agendado por inserção manual de dados ou por meio de chave Pix".</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Estrutura: ajustes de numeração na subseção subsequente 2.5. "Geração da ordem de pagamento pelo serviço de iniciação de transação de pagamento, nos casos em que o participante possui todas as informações do usuário recebedor."</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>29/10/2023</p></td>      <td rowspan="1" colspan="1"><p>1.4</p></td>      <td rowspan="1" colspan="1"><p>Seção 3.1: ajuste no texto explicativo e no fluxo para definição das ordens de pagamento que devem ser enviadas para o canal primário de transmissão de mensagens do SPI e para o canal secundário de transmissão de mensagens do SPI.</p><p>Seção 3.2: ajuste no texto explicativo e no fluxo para definição das ordens de pagamento que devem ser enviadas para o canal primário de transmissão de mensagens do SPI e para o canal secundário de transmissão de mensagens do SPI.</p><p>Seção 3.3: ajuste no texto explicativo e no fluxo em razão da criação do canal secundário de transmissão de mensagens do SPI.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"></td>      <td rowspan="1" colspan="1"><p>Seção 3.4: ajuste no texto explicativo e no fluxo em razão da criação do canal secundário de transmissão de mensagens do SPI.</p></td>     </tr>     <tr>      <td rowspan="1" colspan="1"><p>30/08/2024</p></td>      <td rowspan="1" colspan="1"><p>2.0</p></td>      <td rowspan="1" colspan="1"><p>Seção 3: inclusão de fluxos com liquidação agendada da ordem de pagamento (Pix Agendado, Pix Agendado recorrente e Pix Cobrança com vencimento).</p><p>Estrutura: inserção da seção 5 - Fluxos do Pix Automático.</p><p>Estrutura: revisão geral dos fluxos e textos explicativos.</p></td>     </tr>    </tbody>   </table>

NOTA

O Decreto nº 10.411, de 30 de junho de 2020, prevê a obrigatoriedade da realização de análise de impacto regulatório (AIR) para a edição de atos normativos de interesse geral produzidos pelos órgãos e entidades da administração pública federal direta e indireta.

Todavia, consoante se definiu no parágrafo 8 do Voto 280/2021-BCB, de 10 de novembro de 2021, o Regulamento do Pix, inclusive os demais documentos que o integram ou que o detalham e complementam, não se caracterizam como ato regulatório de força cogente, ostentando, em verdade, natureza eminentemente contratual; assim, modificações promovidas no referido regulamento e nos demais documentos que o integram ou que o detalham e complementam não se sujeitam à produção prévia de análise de impacto regulatório (AIR).

Dessa forma, fica a presente Instrução Normativa dispensada da prévia produção de AIR.

Ricardo Teixeira Leite Mourão
