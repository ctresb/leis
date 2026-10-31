---
titulo: "INSTRUÇÃO NORMATIVA BCB Nº 658, DE 5 DE SETEMBRO DE 2025"
orgao: "Banco Central do Brasil/Área de Organização do Sistema Financeiro e de Resolução/Departamento de Competição e de Estrutura do Mercado Financeiro"
tipo: "Instrução Normativa"
numero: "658"
data: 2025-09-05
revogada: false
versao_texto: "publicação original"
publicacao: "DOU de 09/09/2025, seção 1, p. 83"
data_publicacao: 2025-09-09
edicao: "171"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-bcb-n-658-de-5-de-setembro-de-2025-654006146"
baixado_em: 2026-10-16
---
# INSTRUÇÃO NORMATIVA BCB Nº 658, DE 5 DE SETEMBRO DE 2025

INSTRUÇÃO NORMATIVA BCB Nº 658, DE 5 DE SETEMBRO DE 2025

Divulga a versão 2.9.0 do Manual de Padrões para Iniciação do Pix, que compõe o Regulamento do Pix.

O Chefe do Departamento de Competição e de Estrutura do Mercado Financeiro (Decem), no uso das atribuições que lhe conferem os arts. 23, caput, inciso I, alínea "a", e 94, caput, inciso IX, do Regimento Interno do Banco Central do Brasil, anexo à Resolução BCB nº 340, de 21 de setembro de 2023, e tendo em vista o disposto no art. 2º, caput, inciso II, do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020, resolve:

**Art. 1º** Esta Instrução Normativa divulga a versão 2.9.0 do Manual de Padrões para Iniciação do Pix, que compõe o Regulamento do Pix, conforme art. 2º do Regulamento anexo à Resolução BCB nº 1, de 12 de agosto de 2020.

**Parágrafo único.** O Manual de Padrões para Iniciação do Pix está disponível no endereço eletrônico do Banco Central do Brasil na internet, na página destinada aos manuais que compõem o Regulamento do Pix: https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento\_Pix/II\_ManualdePadroesparaIniciacaodoPix.pdf.

**Art. 2º** Fica revogada a Instrução Normativa BCB nº 630, de 5 de junho de 2025.

**Art. 3º** Esta Instrução Normativa entra em vigor na data de sua publicação.

Ricardo Teixeira Leite Mourão

## ANEXO

Manual de Padrões para Iniciação do Pix Versão 2.9.0

Histórico de revisão

Data

Versão

Descrição das alterações

11/8/2020

1.0

Versão inicial

23/9/2020

1.1

Ajustes nas definições nos campos do*payload*, especialmente na semântica do campo*txid*.

Incluídos os Anexos I e II, tratando dos Conceitos de Negócio da API Pix e das suas especificações técnicas.

13/10/2020

2.0

Seção 1.5.2: incluídas explicações sobre caracteres permitidos no campo*txid*.

Seção 1.6.1: incluído texto para deixar claro que o QR Code dinâmico pode ser gerado por meio de aplicativo.

Seção 1.6.6: excluído texto para deixar claro que o QR Code dinâmico não precisa ser necessariamente gerado por meio da API Pix.

Seção 1.6.8: ajuste na explicação do campo "calendario.vencimento" e exclusão do campo

"calendario.recebivelAposVencimento".

Seção 1.6.17: inclusão de nota de rodapé no campo 62 "Additional Data Field".

Seção 1.6.18: incluído texto para deixar claro que o QR Code dinâmico pode ser gerado por meio de aplicativo.

Incluída a seção 1.7, que trata sobre a funcionalidade "Pix Copia e Cola".

Seção 6.3.3 do Anexo I: correção da função associada à alteração da cobrança via API Pix.

6/11/2020

2.1

Seção 1.6: atualização dos campos do Payload JSON, com a inclusão de campos referentes às funcionalidades de cobrança para pagamentos com vencimento (juros, multa, abatimento, desconto e correlatos); reorganização das subseções para refletir as diferenças de campos entre as cobranças para pagamentos imediatos e pagamentos com vencimento;

Adicionados ao Anexo I casos de uso relacionados ao "Reuso de Location", cenários incluindo cobrança para pagamentos com vencimento e geração de cobranças em lotes.

Inclusão do Anexo III tratando sobre criação, atualização e cálculo de cobranças para pagamentos com vencimento.

9/12/2020

2.2

Seção 1.6.6.2: inserção na tabela que exibe a estrutura do payload JSON para cobranças com vencimento da informação calendario.validadeAposVencimento.

Anexo II - Seção 3.1: inserção de recomendação relativa ao uso de certificados nos webhooks.

12/2/2021

2.2.1

Seção 1.6.6.1: adicionada explicação para a regra de incrementos do campo.

Seção 1.6.6.2: adicionados esclarecimentos sobre o funcionamento do campo calendário.validadeAposVencimento

Seção 2.1: alterado de obrigatório para opcional o preenchimento dos campos logradouro, cidade, UF e CEP do campo "devedor" na criação de uma cobrança com vencimento.

Seção 1.6.1: Excluído o trecho que erroneamente se referia a um possível valor "0" no campo de valor EMV.

22/3/2021

2.3.0

Seção 1.4: removidas notas de rodapé e adicionadas explicações para explicitar que a regra de formatação das chaves Pix segue as determinações constantes do Manual Operacional do DICT.

Seção 1.6.3: removido o fragmento que indica a versão do location.

Seção 1.6.6: ajuste redacional para esclarecer que o código do município a ser informado pelo PSP do pagador deve corresponder à informação cadastral de endereço do usuário pagador.

Seção 1.6.6.1: adicionado o campo modalidadeAlteracao no objeto "valor" para Pix Cobrança para pagamentos imediatos.

Seção 1.6.6.2: inseridos esclarecimentos sobre o comportamento da data de vencimento e da validade após vencimento em caso de fim de semana e de feriado para o usuário pagador.

Seção 1.6.7: exemplo revisado: valor (EMV, opcional) retirado; Ref.Label (txid) modificado (enfatiza que vale o payload da cobrança); fragmento 'v2' (tornado opcional) retirado da location (url da cobrança).

Anexo III: inseridos esclarecimentos sobre o comportamento da data de vencimento em caso de fim de semana e de feriado para o usuário pagador e sobre os consequentes impactos nos campos que façam referência a esta data (validadeAposVencimento; desconto; juros e multa).

22/7/2021

2.4.0

Seção 1: Generalização de 'celular' para 'dispositivo móvel';

Seção 2.4.2: Reforçando obrigatoriedade da chave;

Seção 1.6.2. Nota de rodapé promovida para evidenciar reuso de QR Codes;

Seção 1.6.3. Correção de fdqnPspRecebdor para fqdnPspRecebedor;

Seção 2.7.1. Estruturando pontos de atenção;

Seção 2.7.1.1: na descrição do campo valor, texto alterado para refletir que o campo segue a regex especificada na API Pix: \\d{1,10}\\.\\d{2};

Seção 2.7.1.2: na descrição do campo valor, texto alterado para refletir que o campo segue a regex especificada na API Pix: \\d{1,10|\\.\\d{2}; corrigida a obrigatoriedade dos campos logradouro, cidade, uf e cep, pertencentes ao objeto `recebedor`. Estes campos estavam constando erroneamente como opcionais.

Seção 2.7.1.2: Remoção da obrigatoriedade do calendario.validadeAposVencimento;

Seção 1.8: Inclusão de campos para o serviço de iniciação de transação de pagamento

Seção 0: Informações gerais sobre como mapear os campos do serviço de iniciação de transação de pagamento

Anexo III: Seção 2.1: Obrigatoriedade do campo calendario.validadeAposVencimento removida.

Anexo III: Seção 2.3.3.2: Definição da precisão a ser utilizada no cálculo do fator de juros

26/8/2021

2.5.0

Seção 1: Esclarecimentos no texto

Seção 1.2 e 1.5: Inclusão do novo campo de FSS relativos ao Pix Saque no QR Estático

Seção 1.5.1: Inclusão de situação em que o campo fss é utilizado

Seção 1.6: Inclusão dos campos relativos ao Pix Saque e Pix Troco no QR Dinâmico

Seção 1.6.6.2: Adequação da descrição e da obrigatoriedade do campo calendario.validadeAposVencimento à especificação

da API Pix

Seção 1.8: Alteração no quadro com as informações obrigatórias sobre iniciação através do serviço de iniciação de transação de pagamento

Seção 2: Inclusão dos campos nas mensagens de pagamento relativos ao Pix Saque e Pix Troco

Anexo I: Seção 1: Inclusão das funcionalidades relacionadas ao Pix Saque e ao Pix Troco dentre as contempladas pela API Pix

Anexo I: Seção 4: Inclusão da definição de FSS

Anexo I: Seção 5.4.2: Inclusão das funcionalidades obrigatórias por produto ofertado

Anexo III: Seção 2.1: Adequação da obrigatoriedade do campo calendario.validadeAposVencimento à especificação da API Pix

Anexo 4: Inclusão do cronograma de implementação das funcionalidades obrigatórias

17/9/2021

2.6.0

Seção 2: Adequação das informações contidas nos campos das mensagens de pagamento e inclusão de orientações referentes a um Pix Saque via QR Code estático

29/10/2021

2.6.1

Seção 1.6.1: Alteração de texto da nota de rodapé 35 sobre o código do município

Seção 1.6.6.1: Correção de AGTET para AGTEC

Seção 1.6.6.1: Adequação sobre o conteúdo do campo valor.retirada.troco. modalidadeAgente para o Pix Troco

Seção 1.6.6.2: Reforço da obrigatoriedade do campo calendario.validadeAposVencimento no retorno

Seção 1.8: Inclusão de campos para o serviço de iniciação de transação de pagamento

Seção 2.3: Inclusão de campo do serviço de iniciação de transação de pagamento para pacs.008

09/12/2021

2.6.2

Seção 1: Adequação das terminologias relacionadas ao Pix Saque e Pix Troco

Seção 1.5.4, 1.6.6.1 e 2.2: Inclusão dos correspondentes bancários como agente de Saque (modalidade AGTOT)

30/8/2022

2.6.3

Seção 1.5: Alteração na denominação do campo pss para fss no QR Code estático, com semântica equivalente

Seções 1 e 2: Adequação das terminologias relacionadas ao Pix Saque e Pix Troco, em relação ao Facilitador de Serviço de Saque

Seção 1.8: Alteração no quadro com as informações obrigatórias sobre iniciação através do serviço de iniciação de transação de pagamento, com adequação da data de obrigatoriedade da geração do código &lt;EndToEndId> pelo iniciador e

inclusão de informação sobre o codMun do usuário pagador

Anexo III. Seção 2.1: Inseridos esclarecimentos sobre os campos valor e valor do desconto, na composição do valor da cobrança

Anexo III. Seção 2.3.2: Ajuste no cálculo do valor do desconto, na cobrança com vencimento, podendo ser aplicado para datas menores ou iguais à data de vencimento, conforme especificação da API Pix.

31/10/2024

2.7.0

Reorganização do documento:

Criação da seção "1. Introdução"

Seção anterior "1. Iniciação do Pix por QR Code" foi dividida em duas seções: "2. Iniciação por QR Code" e "3. Outras formas de iniciação"

Seção anterior "2. Mapeamento para Mensagens ISO 20022" foi transferida para o "ANEXO V - Mapeamento para Mensagens ISO 20022"

O "ANEXO IV - Prazos para implementação das funcionalidades" foi alterado para "ANEXO VI - Prazos para implementação das funcionalidades"

Inclusão do produto Pix Automático:

Criação da seção "2.8 Iniciação via QR Code Composto"

Criação da seção "3.3 Pix Automático"

Inclusão de conteúdo relativo ao Pix Automático e ao QR Code Composto no "ANEXO I - API Pix: Conceitos de negócio"

Criação do "ANEXO IV - Pix Automático"

Inclusão das mensagens utilizadas no Pix Automático no "ANEXO V - Mapeamento para Mensagens ISO 20022"

29/11/2024

2.8.0

Anexo IV, Seção 2.2.1: Inclusão de esclarecimento sobre os identificadores das recorrências.

Inclusão do ANEXO VI sobre o Arquivo Padronizado do Pix Automático.

Reorganização no documento: O "ANEXO VI - Prazos para implementação das funcionalidades" foi alterado para "ANEXO VII - Prazos para implementação das funcionalidades".

14/03/2025

2.8.1

Anexo IV, Seção 2.1.2: Ajuste na redação e inclusão da referência ao convênio no atributo recebedor da recorrência.

Anexo IV, Seção 2.3.9: Inclusão da referência ao atributo ajusteDiaUtil na cobrança recorrente.

Anexo IV, Seção 3.3.5: Inclusão da tabela de códigos de rejeição das tentativas de agendamento de cobranças recorrentes que provocam a rejeição da cobrança recorrente correlata.

Anexo IV, Seção 4.3.1: Ajuste na regra para definição da data de início dos ciclos de cobrança, quando a data esperada da

cobrança não existe.

05/06/2025

2.8.2

Seção 2.8.4.2: Ajuste na coluna Mult. da tabela de forma a evidenciar a opcionalidade do campo vinculo.objeto dos parâmetros da recorrência.

Inclusão de seção 3.4 sobre forma de iniciação "Pix por aproximação"

05/09/25

2.9.0

Seção 2.5.1: inclusão de exemplo de chave CNPJ alfanumérica.

Anexo IV, Seção 2.1 e Seção 2.2: adaptação das regras de formação do idRec e idSolicRec ao CNPJ alfanumérico.

NOTA

O Decreto nº 10.411, de 30 de junho de 2020, prevê a obrigatoriedade da realização de análise de impacto regulatório (AIR) para a edição de atos normativos de interesse geral produzidos pelos órgãos e entidades da administração pública federal direta e indireta.

Todavia, consoante se definiu no parágrafo 8 do Voto 280/2021-BCB, de 10 de novembro de 2021, o Regulamento do Pix, inclusive os demais documentos que o integram ou que o detalham e o complementam, não se caracterizam como ato regulatório de força cogente, ostentando, em verdade, natureza eminentemente contratual. Assim, modificações promovidas no referido regulamento e nos demais documentos que o integram ou que o detalham e o complementam não se sujeitam à produção prévia de AIR.
