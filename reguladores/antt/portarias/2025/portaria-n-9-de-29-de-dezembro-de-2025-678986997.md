---
titulo: "PORTARIA Nº 9 DE 29 DE dezembro DE 2025"
orgao: "Ministério dos Transportes/Agência Nacional de Transportes Terrestres/Superintendência de Serviços de Transporte Rodoviário de Passageiros"
tipo: "Portaria"
numero: "9"
data: 2025-12-29
revogada: false
versao_texto: "publicação original"
publicacao: "DOU de 31/12/2025, seção 1, p. 409"
data_publicacao: 2025-12-31
edicao: "249"
fonte: "https://www.in.gov.br/web/dou/-/portaria-n-9-de-29-de-dezembro-de-2025-678986997"
baixado_em: 2026-10-16
---
# PORTARIA Nº 9 DE 29 DE dezembro DE 2025

PORTARIA Nº 9 DE 29 DE dezembro DE 2025

O Superintendente de Serviços de Transporte Rodoviário de Passageiros da Agência Nacional de Transportes Terrestres, no uso de suas atribuições e em conformidade com o art. 25-A da Resolução ANTT nº 4.499, de 28 de novembro de 2014, resolve:

**Art. 1º** Aprovar o Documento de Interface de Software - Versão 4.0, que define as especificações de estrutura de dados dos registros do Sistema de Monitoramento do Transporte Rodoviário Coletivo Interestadual e Internacional de Passageiros a serem transmitidos à ANTT pelas empresas dos serviços rodoviário regular, rodoviário fretado e semiurbano regular.

**Parágrafo único.** O documento de que trata o caput será disponibilizado no sítio eletrônico da ANTT: https://www.gov.br/antt/pt-br

**Art. 2º** Os dados primários correspondem aos registros (logs) a serem gerados pelos Subsistemas Não Embarcado e Embarcado.

**Parágrafo único.** Um registro (log) corresponde a um conjunto de dados bem definidos e estruturados, segundo uma sequência específica.

**Art. 3º** O Subsistema Não Embarcado é composto pelos seguintes logs:

| LogVendaPassagem | Rodoviário Regular |
| --- | --- |
| LogRegistroOcorrenciaRodoviario | Rodoviário Regular |
| LogCancelarPassagem | Rodoviário Regular |
| LogCartaoEmitidoRecargaEfetuada | Semiurbano Regular |
| LogRegistroOcorrenciaSemiurbano | Semiurbano Regular |
| LogReembolsoCartao | Semiurbano Regular |

**Art. 4º** O Subsistema Embarcado é composto pelos seguintes logs:

| LogVelocidadeTempoLocalizacao | Rodoviário Regular, Semiurbano Regular, Rodoviário Fretado |
| --- | --- |
| LogJornadaTrabalhoMotorista | Rodoviário Regular, Semiurbano Regular, Rodoviário Fretado |
| LogDetectorParada | Rodoviário Regular, Semiurbano Regular, Rodoviário Fretado |
| LogInicioFimViagemRegular | Rodoviário Regular, Semiurbano Regular |
| LogInicioFimViagemFretado | Rodoviário Fretado |
| LogBilheteEmbarque | Rodoviário Regular |
| LogLeitorCartaoRFID | Semiurbano Regular |

**Art. 5º** Todos os dados deverão ser enviados por meio de API REST disponibilizada pela ANTT, utilizando requisições HTTPS e payloads no formato JSON, conforme padrão especificado no Documento de Interface de Software (DIS).

**§ 1º** A empresa operadora deve disponibilizar os dados por meio de um ponto de disponibilização, utilizando conexão segura (HTTPS) e autenticação baseada em OAuth 2.0 com emissão de token de acesso à API REST da ANTT, contendo todos os dados especificados no Documento de Interface de Software (DIS).

**§ 2º** Todos os dados deverão ser protegidos por mecanismos de segurança, incluindo controle de integridade e criptografia em trânsito via TLS 1.2 ou superior, sendo sua autenticação realizada por meio de tokens OAuth 2.0, com escopo e tempo de expiração definidos pela ANTT.

**§ 3º** Os dados enviados à ANTT através das APIs disponibilizadas são de inteira responsabilidade da empresa de transporte.

**Art. 6º** Todos os dados deverão ser enviados, conforme os protocolos de transmissão e de segurança especificados pela área de tecnologia da ANTT.

**Art. 7º** Os registros (logs) recebidos serão validados em função da compatibilidade entre as informações transmitidas e as cadastradas na ANTT.

**§ 1º** Os registros (logs) transmitidos fora dos prazos estabelecidos ou transmitidos em inconformidade com as especificações não serão considerados válidos.

**§ 2º** Somente o recebimento do registro (log) pela ANTT não garante a sua validação.

**Art. 8º** A ANTT disponibilizará à empresa de transporte um recibo eletrônico como resposta ao envio dos registros (logs) às APIs.

**§ 1º** Os recibos eletrônicos serão disponibilizados pela ANTT, em formato JSON, no payload de resposta das APIs.

**§ 2º** O recibo eletrônico será emitido e disponibilizado pela ANTT, no ato do envio, após a verificação de integridade dos dados disponibilizados pela empresa de transporte.

**§ 3º** O recibo eletrônico é a garantia para a empresa de transporte do recebimento, pela ANTT, dos dados enviados, devendo ser armazenado pelo período mínimo de 5 (cinco) anos.

**§ 4º** Solicitações de nova disponibilização dos dados devido a erros de transmissão ou inconsistência dos dados podem ser realizadas pela ANTT a qualquer tempo.

**Art. 9º** Será de responsabilidade das empresas a aquisição, a implantação e a manutenção dos equipamentos e dos sistemas necessários para o atendimento a esta Portaria.

**Art. 10** As alterações promovidas pelo Documento de Interface de Software - Versão 4.0 deverão ser implementadas em até 60 (sessenta) dias a partir da vigência desta Portaria.

**Parágrafo único.** Fica revogado o Documento de Interface de Software - Versão 3.0, de 04 de abril de 2024, findo o prazo estabelecido no caput.

**Art. 11** Esta Portaria entra em vigor na data de sua publicação.

JULIANO DE BARROS SAMÔR
