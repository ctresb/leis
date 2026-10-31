---
titulo: "INSTRUÇÃO NORMATIVA Nº 15, DE 26 DE NOVEMBRO DE 2018 (*)"
orgao: "Presidência da República/Casa Civil/Instituto Nacional de Tecnologia da Informação"
tipo: "Instrução Normativa"
numero: "15"
data: 2018-11-26
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 29/11/2018, seção 1, p. 2"
data_publicacao: 2018-11-29
edicao: "229"
fonte: "https://www.in.gov.br/web/dou/-/instrucao-normativa-n-15-de-26-de-novembro-de-2018-52489611"
sha256_html_fonte: cd8654e2430a28a09984c124a58df2da7165572b3c5655d519908a3299f9164a
baixado_em: 2026-10-27
---
# INSTRUÇÃO NORMATIVA Nº 15, DE 26 DE NOVEMBRO DE 2018 (*)

I**NSTRUÇÃO NORMATIVA Nº 15, DE 26 DE NOVEMBRO DE 2018 (\*)**

Altera o DOC-ICP-01.01 para atualizar os Algoritmos e as Suítes de Assinatura e definir parâmetros para a curva E521.

**O DIRETOR-PRESIDENTE DO INSTITUTO NACIONAL DE TECNOLOGIA DA INFORMAÇÃO,SUBSTITUTO,**no uso das atribuições que lhe foram conferidas pelo inciso VI do art. 9º do anexo I do Decreto nº 8.985, de 8 de fevereiro de 2017, e pelo art. 1º da Resolução nº 33 do Comitê Gestor da ICP-Brasil, de 21 de outubro de 2004,

Considerando que o art. 12º da Resolução nº 139 do Comitê Gestor da ICP-Brasil incluiu no DOC-ICP-04, versão 6.6, a previsão de que a AC Raiz regulamentaria a curva elíptica a ser implementada pela ICP-Brasil, resolve:

**Art. 1º** A entrada "Algoritmo" da tabela "Geração de Chaves Assimétricas de AC

".................................................................................................................................

<table><tr></tr><tr><td><p>Algoritmo</p></td><td><p>RSA ou ECC-Brainpool (conforme RFC 5639) ou Ed448-Goldilocks (PureEdDSA e HashEdDSA, conforme RFC 8032) ou E-521 (Conforme parâmetros da curva estabelecidos neste DOC-ICP-01.01, PureEdDSA e HashEdDSA, conforme RFC 8032).</p></td></tr></table>

" (NR)

**Art. 2º** A entrada "Algoritmo" da tabela "Geração de Chaves Assimétricas de Usuário Final" do item 2 do DOC-ICP-01.01, versão 4.0, passa a vigorar com a seguinte redação:

"................................................................................................................................

<table><tr></tr><tr><td><p>Algoritmo</p></td><td><p>RSA ou ECC-Brainpool (conforme RFC 5639) ou Curve25519 (Conforme RFC 7748) ou Ed25519 (PureEdDSA e HashEdDSA, conforme RFC 8032) ou Ed448-Goldilocks (PureEdDSA e HashEdDSA, conforme RFC 8032) ou E-521 (Conforme parâmetros da curva estabelecidos neste DOC-ICP-01.01, PureEdDSA e HashEdDSA, conforme RFC 8032).</p></td></tr></table>

" (NR)

**Art. 3º** A entrada "Suíte de Assinatura" da tabela "Assinatura de Certificados de AC" do item 2 do DOC-ICP-01.01, versão 4.0, passa a vigorar com a seguinte redação:

".................................................................................................................................

<table><tr></tr><tr><td><p>Suíte de Assinatura</p></td><td><p>sha1WithRSAEncryption</p><p>sha512WithRSAEncryption</p><p>sha512WithECDSAEncryption</p><p>id-Ed448, id-Ed521</p><p>id-Ed448ph, id-Ed521ph</p></td></tr></table>

" (NR)

**Art. 4º** A entrada "Suíte de Assinatura" da tabela "Assinatura de Certificados de Usuário Final" do item 2 do DOC-ICP-01.01, versão 4.0, passa a vigorar com a seguinte redação:

".................................................................................................................................

<table><tr></tr><tr><td><p>Suíte de Assinatura</p></td><td><p>sha1WithRSAEncryption</p><p>sha256WithRSAEncryption</p><p>sha256WithECDSAEncryptin</p><p>sha512WithRSAEncryption</p><p>sha512WithECDSAEncryption</p></td></tr><tr><td></td><td><p>id-Ed25519, id-Ed448, id-Ed521</p><p>id-Ed25519ph, id-Ed448ph, id-Ed521ph</p></td></tr></table>

" (NR)

**Art. 5º** A entrada "Algoritmo de Assinatura" da tabela "Assinatura de Listas de Certificados Revogados e Respostas OCSP" do item 2 do DOC-ICP-01.01, versão 4.0, passa a vigorar com a seguinte redação:

".................................................................................................................................

<table><tr></tr><tr><td><p>Algoritmo de Assinatura</p></td><td><p>sha1WithRSAEncryption</p><p>sha256WithRSAEncryption</p><p>sha256WithECDSAEncryption</p><p>sha512WithRSAEncryption</p></td></tr><tr><td></td><td><p>sha512WithECDSAEncryption</p><p>id-Ed448, id-Ed521</p><p>id-Ed448ph, id-Ed521ph</p></td></tr></table>

" (NR)

**Art. 6º** A entrada "Suíte de Assinatura" da tabela "Assinaturas Digitais ICP-Brasil*CAdES, XAdES e PAdES*" do item 2 do DOC-ICP-01.01, versão 4.0, passa a vigorar com a seguinte redação:

".................................................................................................................................

<table><tr></tr><tr><td><p>Suíte de Assinatura</p></td><td><p>sha1WithRSAEncryption</p><p>sha256WithRSAEncryption</p><p>sha256WithECDSAEncryption</p><p>sha512WithRSAEncryption</p><p>sha512WithECDSAEncryption</p></td></tr><tr><td></td><td><p>id-Ed25519, id-Ed448, id-Ed521</p><p>id-Ed25519ph, id-Ed448ph, id-Ed521ph</p></td></tr></table>

" (NR)

**Art. 7º** A entrada "Suíte de Assinatura" da tabela "Assinatura de Pedidos e Respostas de Carimbos do Tempo" do item 2 do DOC-ICP-01.01, versão 4.0, passa a vigorar com a seguinte redação:

"................................................................................................................................

<table><tr></tr><tr><td><p>Suíte de Assinatura</p></td><td><p>sha1WithRSAEncryption</p><p>sha256WithRSAEncryption</p><p>sha256WithECDSAEncryption</p><p>sha512WithRSAEncryption</p><p>sha512WithECDSAEncryption</p></td></tr><tr><td></td><td><p>id-Ed25519, id-Ed448, id-Ed521</p><p>id-Ed25519ph, id-Ed448ph, id-Ed521ph</p></td></tr></table>

" (NR)

**Art. 8º** O item 2 do DOC-ICP-01.01, versão 4.0, passa a vigorar acrescido da tabela "Parâmetros para a curva E521":

".................................................................................................................................

<table><tr></tr><tr><td><p>Parâmetros para a curva E521</p></td></tr><tr><td><p>Parâmetros</p></td><td><p>Valor</p></td></tr><tr><td><p>p</p></td><td><p>p da E-521 (i.e., 2^521 - 1)</p></td></tr><tr><td><p>b</p></td><td><p>528</p></td></tr><tr><td><p>Codificação do GF(p)</p></td><td><p>527-bit codificação little-endian de {0, 1, ..., p-1}</p></td></tr><tr><td><p>H(x)</p></td><td><p>SHAKE256(dom5(phflag,context)||x, 132)</p></td></tr><tr><td><p>phflag</p></td><td><p>0</p></td></tr><tr><td><p>c</p></td><td><p>logaritmo base 2 do cofator da E-521 (i.e., 2)</p></td></tr><tr><td><p>n</p></td><td><p>520</p></td></tr><tr><td><p>d</p></td><td><p>d da E-521(i.e., -376014)</p></td></tr><tr><td><p>a</p></td><td><p>1</p></td></tr><tr><td><p>B</p></td><td><p>(X(P),Y(P)) da E-521 (i.e., (15710548 94184995387535939749894317568645297350402905821437625 18115230499438118852963259119606760410077267392791511 4267193389905003276673749012051148356041324, 12))</p></td></tr><tr><td><p>L</p></td><td><p>ordem da E-521 (i.e., 171619941503265242874 54751997703483043173588250358263523486158647963857958 49413675475876651663657849636693659065234142604319282 948702542317993421293670108523)</p></td></tr><tr><td><p>PH(x)</p></td><td><p>x (i.e., a função identidade)</p></td></tr></table>

Ed521ph é o mesmo, mas com PH sendo SHA-3 (512 bits) ou SHAKE256(x, 64) e phflag sendo 1, i.e., é feito um hash antes da assinatura com Ed521, com a constante hash modificada.

dom5(x, y): na geração de chave, uma string vazia. Na assinatura e verificação, a string do octeto "SigEd521" || octet(x) || octet(OLEN(y)) || y, onde x está no range 0-255 e y é uma string de octeto com no máximo 255 octetos. "SigEd521" está em ASCII (8 octets).

" (NR)

**Art. 9º** Aprovar a versão 4.1 do documento DOC-ICP-01.01 - PADRÕES E ALGORITMOS CRIPTOGRÁFICOS DA ICP-BRASIL.

**§ 1º** As demais cláusulas do referido documento, na sua versão imediatamente anterior, integram a presente versão e mantêm-se válidas.

**§ 2º** O documento referido no caput encontra-se disponibilizado, em sua totalidade, no sítio http://www.iti.gov.br.

**Art. 10.** Esta Instrução Normativa entra em vigor na data de sua publicação.

WALDECK PINTO DE ARAUJO JUNIOR

Republicada por ter saído no DOU nº 228, de 28-11-2018, Seção 1, páginas 16 e 17, com incorreção no original.
