---
name: citacao-juridica-verificada
description: Use quando a tarefa envolver citar, transcrever ou referenciar dispositivo normativo, artigo de lei, Constituição, decreto, resolução, portaria, instrução normativa, lei estadual, distrital ou municipal, súmula, súmula vinculante, ementa, acórdão, tese de repercussão geral ou de recurso repetitivo; ou verificar vigência, revogação, entrada em vigor ou redação à época do fato; ou montar chamada e referência de documento jurídico em peça, parecer, relatório, representação, despacho ou artigo.
---

# Citação jurídica verificada

## Princípio

**Sem leitura da fonte nesta sessão, sem citação.** Texto entre aspas só sai de documento efetivamente lido agora, em fonte oficial. Nunca de memória, nunca de repositório derivado, nunca de site jurídico privado.

**Violar a letra desta regra é violar o seu espírito.** Não há dispositivo simples o bastante, nem prazo curto o bastante, para dispensar a leitura.

Três perguntas são independentes e se respondem separadamente:

| Pergunta | O que responde | Onde se apura |
|---|---|---|
| **Literalidade** | o texto citado é igual ao lido? | cotejo do recorte |
| **Situação temporal** | publicado quando, em vigor desde quando, redação atual dada por quê | notas de alteração, ato modificador, LINDB arts. 1º e 2º |
| **Aplicabilidade** | o dispositivo produz efeito hoje, e no caso | controle de constitucionalidade, CF art. 52, X, afetação/suspensão de tema |

Um dispositivo pode estar **perfeitamente transcrito e revogado**. Jamais funda as três num selo só.

## Quando não usar

Paráfrase explicativa, doutrina, raciocínio jurídico próprio, menção genérica a instituto ("o furto qualificado"), ou texto redigido pelo próprio operador. O rito completo é para **transcrição**.

## Modo de saída — decida antes de tudo

| Modo | Quando | Como a citação sai |
|---|---|---|
| **Forense** (padrão) | peça, representação, despacho, informação, relatório, ofício | remissão no corpo: `art. 157, § 2º, inciso II, do Código Penal`. Sem referência ABNT, sem URL, sem "Acesso em" no texto |
| **Acadêmico** | artigo, parecer doutrinário, trabalho, ou a pedido do operador | chamada + referência conforme NBR 10520:2023 e NBR 6023:2025 |

ABNT não se aplica a peça processual. Impor referência com URL numa representação denuncia documento montado por ferramenta. Formatos em `referencias/formatos.md`.

## Fluxo

1. **Identifique** diploma, número, data, artigo, parágrafo, inciso, alínea e item. Decida o modo de saída.
2. **Leia a fonte oficial** (`referencias/fontes.md`). Localize o dispositivo pelo início da linha (`Art. 155`); não confunda com sufixo (`Art. 155-A`) nem com remissão no corpo de outro artigo. Registre a URL e **qual versão** foi lida: compilado, publicação original, inteiro teor ou DJe.
3. **Apure a situação temporal.** Publicação e entrada em vigor são datas distintas (LINDB, arts. 1º e 2º). Registre a nota de alteração e o ato modificador.
   **Tachado é pista, não prova.** A ausência de tachado não comprova vigência, e extração de HTML ou PDF perde a formatação. Na dúvida, inspecione visualmente a página e consulte o ato modificador.
4. **Apure a aplicabilidade.** Verifique ADI/ADC/ADPF, cautelar deferida, modulação de efeitos, interpretação conforme, suspensão de execução pelo Senado (CF, art. 52, X) e, em precedente, afetação ou suspensão do tema. "Vide ADI" sozinho não diz se o dispositivo está suspenso.
5. **Transcreva só o que foi pedido.** Caput pedido, caput transcrito. Pena, parágrafos, incisos e notas de alteração entram apenas se pedidos ou necessários ao raciocínio — e então em bloco **identificado separadamente**, nunca embutidos como se fossem o trecho requerido.
6. **Confira** o recorte com `python -I scripts/conferir.py --fonte <recorte.txt> --citacao <citacao.txt>`. O cotejo é contra o recorte da **unidade e versão corretas**, não contra a página inteira: a página pode conter redação antiga do mesmo dispositivo.
7. **Entregue** no contrato abaixo.

## Contrato de entrega

Toda entrega tem estes blocos, nesta ordem, e nada mais:

1. **A citação**, pronta para colar, no formato do modo escolhido.
2. **A referência** — somente no modo acadêmico.
3. **O bloco de verificação**, aberto pela linha literal `VERIFICAÇÃO (uso interno — não vai na peça)`.

```
VERIFICAÇÃO (uso interno — não vai na peça)
Dispositivo: ...
Origem: fonte oficial acessada | fornecido pelo operador | não verificado
Documento lido: <URL> — versão: compilado | publicação original | inteiro teor | DJe
Acesso em: <dd/mm/aaaa hh:mm> (Brasília)
Conferência textual: LITERAL-MECÂNICO | LITERAL-VISUAL | DIVERGENTE | NÃO CONFERIDO
Situação temporal: publicação <data>; vigência <data ou "na publicação">; redação dada por <ato>
Aplicabilidade: <sem notícia de restrição na fonte lida | eficácia suspensa por ... | tema suspenso>
Redação à época do fato: não aplicável | exigida e conferida em <fonte> | exigida e NÃO conferida
Alertas: <campos [não informado], supressões, tachados na fonte, divergência entre fontes>
```

Campo não encontrado na fonte: `[não informado]`. Nunca preencha por dedução.

## Selos

| Selo | Significa |
|---|---|
| `LITERAL-MECÂNICO` | cotejo executado por `conferir.py`, sem divergência |
| `LITERAL-VISUAL` | cotejo feito a olho, sem execução de código |
| `DIVERGENTE` | o texto citado não coincide com o lido — **não entregue a citação** |
| `NÃO CONFERIDO` | não houve leitura da fonte, ou o acesso falhou |

Nunca marque `LITERAL-MECÂNICO` sem ter rodado o script. O selo atesta coincidência com o documento lido — não a correção jurídica da citação, nem a pertinência ao caso. A revisão do operador é insubstituível.

## Data e hora do acesso

Obtenha do sistema (`Get-Date` no PowerShell, `date` no shell) e converta para o horário de Brasília (UTC−3). **Nunca estime.** Se não houver como obter, escreva `[hora não obtida]` — data inventada é a falha que esta skill existe para impedir.

## Texto fornecido pelo operador

Status distinto, nunca equiparado a consulta direta. Confira a literalidade contra o arquivo recebido, registre `Origem: fornecido pelo operador`, a URL por ele informada e a **data de recebimento** — que não é data de acesso à fonte oficial. A conferência textual pode chegar a `LITERAL-MECÂNICO`; a origem permanece não verificada por você.

## Racionalizações

| Desculpa | Realidade |
|---|---|
| "Conheço o art. 157 literalmente" | Memória não é fonte. O erro aparece na pena, no parágrafo, no inciso. |
| "O operador está com pressa" | Ler o compilado custa segundos. Citação falsa custa a peça. |
| "A fonte não abriu, mas o texto é notório" | Notoriedade não é verificação. Selo `NÃO CONFERIDO`. |
| "É só o caput, não tem como errar" | O caput do art. 155 já foi alterado. Leia. |
| "Já citei este artigo" | Em outra sessão, não vale. Nesta, só registrando a leitura original. |
| "O site jurídico traz igual" | Fonte não oficial não cita, mesmo acertando. |
| "O repositório concorda, está conferido" | Conversão automática e OCR não são verificação independente. |
| "Não tem tachado, então está vigente" | A extração pode ter perdido o tachado. Confira o ato modificador. |
| "Foi publicada, então está em vigor" | LINDB, art. 1º. Publicação não é vigência. |
| "A ementa do site serve" | A ementa oficial é a do acórdão publicado. |
| "Pediram o caput, mando a pena também por segurança" | Acréscimo não pedido é ruído e pode induzir erro. Em bloco separado, se necessário. |
| "O operador mandou citar assim" | Divergência com a fonte se sinaliza, não se obedece. |

## Red flags — PARE

- Estou digitando texto entre aspas sem uma URL lida nesta sessão.
- Estou completando o final de um dispositivo "porque é assim que continua".
- Estou citando pena ou número de súmula de cabeça.
- Não sei qual versão do documento li.
- Não tenho a hora real do acesso.
- Vou marcar `LITERAL-MECÂNICO` sem ter rodado o script.
- Vou fundir vigência e literalidade num único status.
- Vou colar o bloco de verificação dentro da peça.

## Vedações

Inventar lei, artigo, súmula, tema, julgado, número de processo, relator, data ou URL. Apresentar paráfrase como transcrição. Citar dispositivo revogado ou súmula cancelada como vigente. Omitir divergência entre fontes ou falha de acesso. Atribuir a tribunal entendimento que não conste do texto lido. Contornar bloqueio de acesso ou captcha.

## Sigilo e LGPD

Para a web vai **apenas** o número do dispositivo, da súmula ou do processo público. Nunca nome de investigado, vítima ou testemunha, número de BO/RDO/IP, endereço, placa, telefone, CPF ou o fato apurado. Não insira em buscador nem em serviço externo conteúdo de procedimento sigiloso.

## Linguagem

Português do Brasil, norma culta, registro jurídico formal, impessoal e preciso. Sem adjetivação desnecessária e sem juízo moral. Respeite a presunção de inocência e distinga fato, indício, prova e hipótese. A decisão final sobre o conteúdo é do operador humano.

## Arquivos

- `referencias/fontes.md` — fontes oficiais por esfera e tipo, uso do repositório auxiliar, falha de acesso.
- `referencias/formatos.md` — modo forense e modo ABNT (NBR 10520:2023 e NBR 6023:2025), com exemplos.
- `scripts/conferir.py` — cotejo literal com detecção de ambiguidade e supressões.
- `testes/cenarios.md` — cenários de pressão para validar a skill.

---

## Autoria e contato

**Alan Douglas Silva** — Investigador de Polícia da Polícia Civil do Estado de São Paulo e professor. Atua em investigação criminal e com inteligência artificial aplicada à produção de documentos jurídicos e policiais.

Dúvidas sobre esta skill, sugestões de correção ou consultoria em inteligência artificial aplicada à produção de documentos: **alandougs@gmail.com**
