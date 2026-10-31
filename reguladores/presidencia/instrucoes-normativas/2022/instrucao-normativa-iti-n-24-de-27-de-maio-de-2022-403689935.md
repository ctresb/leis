---
titulo: "INSTRUÇÃO NORMATIVA ITI Nº 24, DE 27 DE MAIO de 2022"
orgao: "Presidência da República/Casa Civil/Instituto Nacional de Tecnologia da Informação"
tipo: "Instrução Normativa"
numero: "24"
data: 2022-05-27
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 30/05/2022, seção 1, p. 4"
data_publicacao: 2022-05-30
edicao: "101"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-iti-n-24-de-27-de-maio-de-2022-403689935"
sha256_html_fonte: 4029e87a412174d66047be7cef67eb511ab78d382eeb38ab5011686aa39a30b9
baixado_em: 2026-10-20
---
# INSTRUÇÃO NORMATIVA ITI Nº 24, DE 27 DE MAIO de 2022

INSTRUÇÃO NORMATIVA ITI Nº 24, DE 27 DE MAIO de 2022

Altera o DOC-ICP-05.03 para melhorias nos procedimentos de coleta e verificação da qualidade de biometrias.

**O DIRETOR-PRESIDENTE DO INSTITUTO NACIONAL DE TECNOLOGIA DA INFORMAÇÃO**, no uso das atribuições que lhe foram conferidas pelo inciso VI do art. 9º do anexo I do Decreto nº 8.985, de 8 de fevereiro de 2017, pelo art. 1º da Resolução nº 33 do Comitê Gestor da ICP-Brasil, de 21 de outubro de 2004, e pelo art. 2º da Resolução nº 163 do Comitê Gestor da ICP-Brasil, de 17 de abril de 2020,

CONSIDERANDO a necessidade de aprimorar continuamente a segurança e a confiabilidade nos processos de identificação de um requerente de um certificado digital ICP-Brasil, e

CONSIDERANDO a necessidade de atualizar os processos tecnológicos de identificação biométrica na ICP-Brasil, resolve:

**Art. 1º** Esta Instrução Normativa altera o documento "Procedimentos para identificação biométrica na ICP-Brasil DOC-ICP-05.03", consolidado pela Instrução Normativa ITI nº 09, de 22 de outubro de 2020, para melhorias nos procedimentos de coleta e verificação da qualidade de biometrias.

**Art. 2º** O Anexo da Instrução Normativa ITI nº 09, de 22 de outubro de 2020, (DOC-ICP-05.03) passa a vigorar com as seguintes alterações:

"2. ...................................................................................................................

2.1 A coleta de dados biométricos na modalidade presencial deve ser feita de forma assistida (acompanhada) por um agente de registro (AGR). Na modalidade remota por videoconferência, a coleta de dados biométricos deverá ser realizada pela captura de face (frame) do requerente durante a videoconferência de forma assistida e, opcionalmente, pela coleta das impressões digitais do requerente. Pode ser realizada a captura da face de forma não assistida e assíncrona à videoconferência, para execução do batimento biométrico junto a uma base oficial nacional ou PSBio.

....................................................................................................................................

2.4 A coleta biométrica na ICP-Brasil deve ser realizada e verificada a qualidade quando da captura conforme os seguintes parâmetros:

2.4.1 Parâmetros mínimos para biometria facial:

a) enquadrar a cabeça e a parte superior dos ombros para que o rosto ocupe de 70% a 80% da fotografia, apenas um rosto no enquadramento;

b) rosto virado para a frente;

c) olhos e boca não obstruídos;

d) pessoa não está sorrindo;

e) envio de apenas uma Face;

f) requisitos técnicos:

i. a coleta deverá ser realizada com no mínimo 90 pixels de distância entre o centro dos olhos. Esta medida assegura uma resolução mínima da foto e deve ser validada durante a coleta e na recepção no PSBio;

ii. a fotografia deve ser gerada em formato de imagem (PNG, JPEG ISO/IEC 10918), com cor, compressão limitada a garantir tamanho máximo da imagem de 1 Mb;

iii. a aplicação de videoconferência responsável pela captura da face (frame) deverá efetuar a crítica dos parâmetros dispostos nas alíneas acima. (Incluído pela Instrução Normativa ITI nº 05, de 2021); e

iv. o PSBio deve rejeitar a imagem caso ela não atenda os parâmetros mínimos mensuráveis no caso de cadastros.

2.4.2 .................................................................................................................

...................................................................................................................................

2.6.3 ................................................................................................................

2.6.3.1 A AC que não responder no prazo estabelecido assume o risco da fraude, e deve revogar o certificado, caso já tenha emitido.

...................................................................................................................................

2.6.8 Os PSBios devem excluir todas as transações pendentes a mais de 30 dias sem resposta e liberar o IDN, executando o fluxo estabelecido no item 4.4.7.

2.6.9 As AC não podem realizar operações de verificação (1:1), na forma estabelecida no item 2.5.4, com dados biométricos que não tenham sido aprovados pela rede de PSBio.

...................................................................................................................................

3.6.4 Deve ter, no mínimo, capacidade operacional para realizar 99% das transações de identificação que chegam das ACs e de outros PSBios, por dia. Cabe notar que quando houver acúmulo de transações pendentes, estas deverão ser tratadas em ordem cronológica, de forma que serão atendidas o equivalente a no mínimo 99% das transações de identificação 1:N que chegam em um dia, mesmo que isso não implique que 99% das transações do dia sejam atendidas.

3.6.5 O PSBIO que não atingir, no mês, o SLA (Service Level Agreement) estabelecido nos itens 3.6.1 e 3.6.4 fica impedido de prestar serviços para novas AC.

...................................................................................................................................

3.7.3 Deve verificar a qualidade das biometrias recebidas das suas ACs e de outros PSBios, confirmando que as coletas foram realizadas dentro dos padrões mínimos de qualidade estabelecidos nesta norma, incluindo, no mínimo, as seguintes verificações automáticas:

a) para face:

i. enquadramento da cabeça e a parte superior dos ombros para que o rosto ocupe de 70% a 80% da fotografia, apenas um rosto no enquadramento;

ii. rosto virado para a frente;

iii. olhos e boca sem obstrução; e

iv. pessoa não está sorrindo.

b) .....................................................................................................................

3.7.3.1 O campo PID do pacote NIST (não conformidade de face), deve ser habilitado e indica que o PSBio não deve utilizar a face coletada nos seus processamentos biométricos dos fluxos descritos no item 4 deste documento. Se para a mesma transação houver dedos com índice NFIQ, a face poderá ser armazenada em base exclusivamente para fins de consulta e exibição em operações que envolverão inspeção visual da face para fins de tratamento de exceção. Caso contrário a transação deve ser recusada.

...................................................................................................................................

3.10.5 Prazo para resolver outros erros

3.10.5.1 Devem ser também retiradas imediatamente da lista de pendências transações que receberam uma resposta de erro assíncrona ou não processados com mais de 30 (trinta) dias independente do motivo. Essas transações devem ser colocadas sob análise no PSBio de origem e devem ser reenviadas após o problema ser sanado quando isto for possível, e, uma vez aceitas, podem novamente constar na lista de pendências.

3.10.5.2 O PSBio de destino, ao receber nova versão de uma transação anteriormente recusada, deve seguir o definido nos itens 3.10.2, 3.10.3 e 3.10.4

....................................................................................................................................

3.14.1 O PSBio deverá ter um sistema para gestão de comunicações de erros de negócio e de outros erros assíncronos recebidos de outros PSBios.

...................................................................................................................................

3.14.5 O prazo para tratamento dos erros de negócio e de outros erros é de até 12 (doze) horas para serem sanados pelos PSBios.

...................................................................................................................................

4.1.6 Captura Antecipada

4.1.6.1 As AC poderão realizar captura antecipada de minucias biométricas (face e impressão digital) possibilitando ao usuário a coleta biométrica antes de iniciar a emissão do certificado na modalidade de videoconferência com batimento biométrico em base oficial nacional ou na verificação na rede PSBio.

4.1.6.2 Somente poderá ser realizada captura antecipada com software que permita a detecção de vivacidade (liveness) do requerente, obrigatória, para minimizar manipulação de rosto e voz em montagens de vídeo conhecidas como "deepfake" e com a verificação de parâmetros de qualidade da biometria estabelecido no item 3.7.3.

.........................................................................................................................." (NR)

**Art. 3º** Fica aprovada a versão 3.1 do documento "DOC-ICP 05.03 - Procedimentos para identificação biométrica na ICP-Brasil".

**Parágrafo único.** A identificação da versão do documento "Procedimentos para identificação biométrica na ICP-Brasil" deverá ser atualizada no preâmbulo e incluída no controle de versões do anexo da Instrução Normativa ITI nº 09, de 22 de outubro de 2020.

**Art. 4º** A Instrução Normativa ITI nº 09, de 22 de outubro de 2020, passa a vigorar com a seguinte alteração:

"Art. 2º Fica aprovada a versão 3.1 do documento DOC-ICP-05.03 - Procedimentos para Identificação Biométrica na ICP-Brasil, anexa a esta Instrução Normativa." (NR)

**Art. 5º** Esta Instrução Normativa entra em vigor em 1º de julho de 2022.

**Parágrafo único.** Os PSBios têm o prazo de até 1º de agosto de 2022 para corrigir ou cancelar as transações pendentes de tratamento de erro. Após esse prazo deve ser observado o item 3.14.5 do anexo da Instrução Normativa ITI nº 09, de 22 de outubro de 2020, (DOC-ICP-05.03).

CARLOS ROBERTO FORTNER
