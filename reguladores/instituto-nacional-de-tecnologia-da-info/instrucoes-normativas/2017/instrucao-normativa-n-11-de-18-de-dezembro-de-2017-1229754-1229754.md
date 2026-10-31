---
titulo: "INSTRUÇÃO NORMATIVA Nº 11, DE 18 DE DEZEMBRO DE 2017"
orgao: "Instituto Nacional de Tecnologia da Informação/Instituto Nacional de Tecnologia da Informação"
tipo: "Instrução Normativa"
numero: "11"
data: 2017-12-18
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 21/12/2017, seção 1, p. 113-114-115"
data_publicacao: 2017-12-21
edicao: "244"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-n-11-de-18-de-dezembro-de-2017-1229754-1229754"
sha256_html_fonte: 52f34c6785c0745006d4189d9064577f74cb42b4c537f66ecbff072abe8e4c04
baixado_em: 2026-10-28
---
# INSTRUÇÃO NORMATIVA Nº 11, DE 18 DE DEZEMBRO DE 2017

**O DIRETOR-PRESIDENTE DO INSTITUTO NACIONAL DE TECNOLOGIA DA INFORMAÇÃO,** no uso das atribuições que lhe foram conferidas pelo inciso VI do art. 9º do anexo I do Decreto nº 8.985, de 8 de fevereiro de 2017, pelo art. 1º da Resolução nº 33, do Comitê Gestor da ICP-Brasil, de 21 de outubro de 2004,

Considerando a necessidade de atualizar os processos tecnológicos da identificação biométrica na ICP-Brasil, resolve:

**Art. 1º** o item 2.2, do DOC-ICP-05.03, versão 1.5, passa a vigorar acrescido da alínea "e" com a seguinte redação:

"2.2 ...................................................................................................................................................

?...........................................................................................................................................................

e. pousada sobre o leitor." (NR)

**Art. 2º** A alínea "b" do item 3.2, do DOC-ICP-05.03, versão 1.5, passa a vigorar com a seguinte redação:

"3.2 ?...................................................................................................................................................

?...........................................................................................................................................................

b. o tráfego de informações deve ocorrer por meio de transações biométricas especificadas neste documento e deve utilizar canal seguro de comunicação (HTTPS com dupla autenticação por certificado digital ICP-Brasil).

?................................................................................................................................................" (NR)

**Art. 3º** O item 3.2.2, do DOC-ICP-05.03, versão 1.5, passa a vigorar com a seguinte redação:

"3.2.2 Em geral, pela sua característica assíncrona, o HUB retorna os erros de forma assíncrona com um arquivo ANSI/NIST de resposta conforme descrito neste documento. Em algumas situações específicas o erro é gerado em tempo de execução da requisição. Nestes casos, o serviço deve retornar um código de erro HTTP 500, seguidos de uma mensagem de erro no padrão descrito abaixo. A codificação deve ser "string".

{

"error\_code":""

"error\_message":"",

"additional\_data":""

} " (NR)

**Art. 4º** O item 3.3.6.8, do DOC-ICP-05.03, versão 1.5, passa a vigorar acrescido da seguinte nota:

"3.3.6.8 ?.........................................................................................................................................

?......................................................................................................................................................

?......................................................................................................................................................

NOTA 2: As respostas das transações com sucesso devem vir em formato JSON conforme descrito abaixo:

{

"responseCode": "200"

"response": "Success"

} " (NR)

**Art. 5º** O item 3.4, do DOC-ICP-05.03, versão 1.5, passa a vigorar com a seguinte redação:

"3.4. Fluxo padrão de cadastramento e consulta biométrica e consistência das bases biométricas

O fluxo padrão de uma consulta ou cadastramento de biometria exige que o PSBio consulte os diretórios em busca da existência do IDN em um dos PSBios, se o IDN for localizado, deve ser executada uma verificação biométrica 1:1 entre os PSBio.

Caso o registro não seja encontrado em nenhum dos PSBios, um novo cadastramento pode ser feito no PSBio. A execução desta operação exige que o PSBio execute uma busca 1:N em todos os outros PSBios antes de considerar o processo de cadastramento completo.

**Fluxo de Cadastro**

a. A AC envia um pacote ENR do IDN-a coletado ao PSBIO 1;

b. PSBIO 1 envia idn query para toda rede;

b1. Se o IDN-a não estiver livre, notifica a AC que não é possível fazer enroll (Envia ERR 101), encerra fluxo (AC deve produzir um pacote de UPR - fluxo de atualização abaixo); ou

b2. Se o IDN-a não estiver livre, o PSBio pode checar internamente, em um processo de verificação (1:1), a biometria; em caso de match avisar o resultado positivo para AC (podendo ou não montar um pacote UPR); em caso de no-match base local, avisar o resultado negativo a AC para as providências de fraude; em caso de no-match no cache, a AC deve montar um pacote UPR (seguir passo b2 do fluxo de atualização);

c. IDN-a está livre, faz pesquisa em lista negativa;

c1. Se houve uma ocorrência (biometrias encontradas na blacklist), notifica AC que as biometrias estão na lista negativa, não se pode fazer cadastro com essas biometrias, encerra fluxo;

d. Não houve ocorrência em lista negativa, faz o processo de deduplicação local;

d1. Se houve ocorrência na base local (biometrias encontradas na base local com outro IDN-b), notifica a AC de possível fraude, reserva o IDN, mas fica esperando decisão da AC para continuar fluxo, encerra fluxo;

d2. Se houve ocorrência no cache, notifica AC de possível exceção para esperar o processo, mas continua para passo e) do fluxo de cadastro;

e. Envia pacote de identificação (IDE) com todas as biometrias para o PSBio 2 (para confirmar a não existência da biometria na rede ou para confirmar ocorrência no cache) - que deverá realizar 1:N somente na base local; PSBio 1 fica aguardando a resposta do PSBio 2;

f. Após receber a resposta (VRE) do último PSBio na rede;

f1. Se houve alguma resposta da biometria encontrada em outro registro em outro PSBio, notifica a AC sobre duplicidade e aguarda a resolução por parte das ACs (AC entrará em contato com ITI);

g. Não houve ocorrência de duplicidade das biometrias em outro PSBio, conclui o cadastro da pessoa enviando ERE para a AC e change\_status 1 para os PSBios da rede.

**Caso alternativo 1 originado de d1**

Houve ocorrência na base local, a AC pode resolver como:

•? Mesmas biometrias, o PSBio então move para a lista negativa as biometrias de ambos os cadastros, libera os dois IDNs, IDN-a e IDN-b, e envia change status 0 para toda a rede.

•? Biometrias diferentes, para casos de falso positivo, retoma o fluxo para o IDN-a a partir de e).

•? Recoleta, quando houver erros de operação, desconsiderar a transação que gerou a exceção (candidato para o cadastro).

•? Cadastro incorreto, considera que houve erro de operação no cadastro mais antigo, IDN-b, remove as biometrias do IDN-b do servidor sem mover para lista negativa, mas envia change status 0 para rede apenas para informar que o IDN deve ser removido do cache dos demais PSBios. O processo de atualização da Lista Negativa Biométrica será comunicada pelo ITI e terá como base o Sistema Anti-Fraude das ACs (Lista Negativa).

**Fluxo de Atualização**

a. A AC envia um pacote UPR do IDN-a coletado ao PSBIO 1;

b. PSBIO 1 envia idn query para toda rede;

b1. Se o IDN não existir, notifica a AC que não é possível fazer update (é enviado ERR 201), encerra fluxo;

b2. Se o IDN existir no PSBio 2 (cache do PSBio 1), envia o pacote UPR inteiro ao PSBio 2 apenas trocando a origem e destino do pacote recebido da AC (DAI e ORI), fica aguardando resposta do PSBio 2;

c. IDN pertence à base local do PSBio 1, faz pesquisa em lista negativa;

c1. Se houve uma ocorrência (biometrias encontradas na blacklist), notifica a AC que as biometrias estão na lista negativa. Não se pode fazer atualização com essas biometrias, encerra fluxo;

d. Não houve ocorrência em lista negativa, separa as biometrias em dois conjuntos:

\- Conjunto A = existentes A, ou seja, índices de dedos que já constam no cadastro; e

\- Conjunto B = novas biometrias, biometrias cujos índices dos dedos ainda não foram cadastrados;

e. Com o conjunto A, faz verificação (1:1) local com as biometrias cadastradas anteriormente;

e1. Caso o conjunto A seja vazio ou a verificação não retorne match biométrico, notifica a AC de possível fraude, bloqueia IDN, mas não permite novas operações sobre ele enquanto a exceção não for resolvida, encerra fluxo;

f. Se o conjunto B não for vazio (existem novas biometrias), faz deduplicação do conjunto B localmente:

f1. Se o conjunto B for vazio - ou seja, não existem novas biometrias - envia ERE para a entidade que pediu a atualização do idn (PSBio ou AC) e acaba fluxo (cache de outros PSBios são atualizados no período noturno);

f2. Se houve ocorrência (duplicidade de biometrias) na base local, notifica a AC de possível fraude, bloqueia o IDN, mas não permite novas operações sobre ele enquanto a exceção biométrica não for resolvida, encerra o fluxo;

f3. Se houve ocorrência (duplicidade de biometrias) no cache, notifica AC de possível exceção, mas continua para passo g) do fluxo;

g. Envia notificação para a AC e envia identificação (IDE) para outros PSBios para checar a não existência da biometria na rede ou confirmar a ocorrência no cache, fica aguardando a resposta dos demais PSBios;

h. Após receber a resposta (VRE) do último PSBio:

h1. Se houve alguma resposta positiva (duplicidade de biometrias), notifica a AC da situação e fica esperando a resolução da exceção biométrica por parte das ACs;

i. Se não houve ocorrência de duplicidade das biometrias em outro PSBio, conclui a atualização enviando ERE para a entidade que pediu a atualização do IDN (PSBio ou AC) e change\_status 1 para toda a rede.

**Caso alternativo originado a partir b2**

O PSBio para o qual foi repassado o UPR respondeu (sucesso ou falha na atualização), lança a notificação da resposta recebida para a AC que originou a transação de atualização.

**Caso alternativo originado de e1**

Houve problemas na verificação 1:1, a AC pode resolver como as opções:

• ? Biometrias diferentes mantendo o cadastro original: move para a lista negativa as biometrias da transação que está tentando entrar (biometrias da segunda transação) e desbloqueia o IDN mantendo as biometrias anteriores do cadastro original.

• ? Biometrias diferentes mantendo novo perfil: move para a lista negativa as biometrias da transação que já estava na base e desbloqueia o IDN, promovendo as biometrias da segunda transação como as autênticas. É também enviado change status 0 para a rede a fim de limpar o cache das biometrias antigas (as novas serão atualizadas no período noturno).

• ? Mesmas biometrias, para casos de falso negativo, retoma o fluxo a partir de f).

• Cadastro incorreto: considera que houve erro de operação no cadastro mais antigo (cadastro original), remove as biometrias do cadastro antigo do servidor sem mover para lista negativa, mas envia change status 0 para os demais PSBios para que o IDN seja removido do cache dos outros PSBios. Após isso, começa um fluxo de cadastro para a segunda transação a partir do passo d).

• Recoleta: houve erro de operação, desconsiderar a transação que gerou a exceção e desbloqueia o IDN." (NR)

**Art. 6º** O item 5, do DOC-ICP-05.03, versão 1.5, passa a vigorar com a seguinte redação:

"5. PUBLICAÇÃO DOS SERVIÇOS DE PSBIO

Serão publicados pela ICP-Brasil uma listagem de todos os PBios homologados, esta listagem deve conter a seguintes informações de cada PSBio:

\- ID do PSBio

\- Localização/URL do serviço de diretório

\- Localização/URL do serviço de troca de arquivos ANSI/NIST (HUB biométrico)

\- x509/certificado para fins de autenticação do PSBio

A publicação será feita em arquivo em formato JSON, seguindo o formato abaixo.

[

{

"PSBioId:" "*NamePSBio*",

"nist\_endpoint": "URL PARA ENVIO DE ARQUIVOS ANSI/NIST",

"directory\_endpoint": "URL PARA SERVIÇO DE DIRETÓRIO",

"x509": "BASE64 X.509"

},

{...}

] " (NR)

**Art. 7º** O item 8.1, do DOC-ICP-05.03, versão 1.5, passa a vigorar com a seguinte redação:

"8.1. O ciclo de vida de uma transação biométrica digital compreende os processos descritos na tabela a seguir e no fluxo descrito no item 3.4. As referências dos pacotes biométricos estão relacionadas no adendo ADE-ICP-05.03.A.

?............................................................................................................................................." (NR)

**Art. 8º** O item 8.3, do DOC-ICP-05.03, versão 1.5, passa a vigorar acrescido da seguinte nota:

"8.3 ?................................................................................................................................................

?...........................................................................................................................................................

NOTA: O pacote IDE não possui marcação de dedo não coletado por amputação ou restrição temporária." (NR)
