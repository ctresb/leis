# Fontes

Regra de ouro: **busca web serve para achar a URL oficial, nunca como fonte de citação.** Bases jurídicas governamentais estrangeiras não cobrem direito brasileiro.

## Federal

| Necessidade | Fonte |
|---|---|
| Texto de trabalho, consolidado | Planalto, texto **compilado** (`planalto.gov.br/ccivil_03/...`) |
| Consolidação por vigência, URN LexML | `normas.leg.br` (Senado) e `lexml.gov.br` |
| Publicação oficial, redação original, retificação | Imprensa Nacional — `in.gov.br` (DOU) |

O compilado do Planalto é facilitação de leitura; **a autenticidade está na publicação no DOU**. Se Planalto e DOU divergirem, prevalece o DOU e a divergência vai para os alertas.

Constituição: Planalto compilado. Atenção às emendas, ao ADCT e às regras de transição das ECs — texto vigente não é o mesmo que eficácia imediata.

## Estadual e distrital

Assembleia Legislativa ou Casa Civil do Estado. Em SP, ALESP. No Distrito Federal, CLDF e **SINJ-DF**; a referência entra por `DISTRITO FEDERAL.`, e a Lei Orgânica do DF não é Constituição estadual.

## Municipal

Fluxo próprio, porque é o caso mais frágil:

1. Identifique **município e UF** — há homônimos.
2. Procure na **Câmara Municipal** (portal de legislação) e no **Diário Oficial do Município**; para ato do Executivo, no portal da Prefeitura.
3. Compilação privada ou plataforma terceirizada só serve se for comprovadamente o **veículo oficial de publicação daquele ente** — o que precisa constar do próprio sítio oficial do município. Sem essa comprovação: `NÃO CONFERIDO`, e peça o ato ao operador.

Referência: `PRESIDENTE PRUDENTE (SP).`

## Infralegal

Sítio oficial do órgão: CNJ, CNMP, ANVISA, CONTRAN, Receita Federal, CMN/Bacen, CONAMA, conselhos profissionais. Resolução, portaria, instrução normativa e provimento entram como **ato administrativo normativo** (NBR 6023:2025, 7.11.5).

## Súmulas e julgados

- Súmula: portal do tribunal (STF: súmulas e súmulas vinculantes; STJ: súmulas). Informe se está **vigente, cancelada, revisada ou superada**, conforme a fonte. Súmula vinculante tem numeração própria e regime do art. 103-A da CF.
- Ementa: a ementa oficial é a do **acórdão publicado**. Diga de onde veio o texto (página de pesquisa, inteiro teor ou DJe) e, para uso formal, prefira o inteiro teor ou o DJe.
- Colete: tribunal, órgão julgador, classe, número e UF, relator, data de julgamento, data de publicação e URL do documento.
- Precedente qualificado (CPC, art. 927): repercussão geral, repetitivo, IRDR e IAC. **Tese não é ementa** — cite-a como publicada pelo tribunal, com o número do tema, e verifique afetação, suspensão e trânsito.

## Controle de constitucionalidade e eficácia

Checar, antes de afirmar vigência: ADI, ADC e ADPF; cautelar deferida; modulação de efeitos; declaração de inconstitucionalidade sem redução de texto; interpretação conforme; e suspensão da execução pelo Senado (CF, art. 52, X).

## Redação à época do fato

Quando o caso exigir a redação vigente na data do fato, o compilado **não resolve**. Vá a `normas.leg.br`/LexML (consolidação por vigência), ao DOU da redação original e aos atos modificadores. Se não conferir, registre `exigida e NÃO conferida` — nunca presuma que o texto atual valia antes.

## Repositório auxiliar — `github.com/ctresb/leis`

Acervo em Markdown de normas federais, estaduais, distritais, infralegais e (em coleta inicial) municipais. Cada arquivo traz cabeçalho YAML com `fonte` (URL oficial), `urn` (URN LexML), `publicacao` e `baixado_em`.

**Papel único: localizar a norma e obter a URL oficial.** O texto citado nunca sai dele. O próprio mantenedor adverte que os textos não substituem a publicação no Diário Oficial, por serem conversão automática e OCR.

Leitura eficiente: `raw.githubusercontent.com/ctresb/leis/main/<caminho>`. Caminhos são determinísticos — `federal/decretos-lei/AAAA/`, `federal/leis-ordinarias/AAAA/`, `estaduais/UF/<tipo>/AAAA/`, `municipais/UF/<municipio>/`, `jurisprudencia/<tribunal>/`, `reguladores/<orgao>/<tipo>/` — com arquivo nomeado `<tipo>-<numero>[-<sufixo>]-<AAAA-MM-DD>.md`. O nome exige a data completa, então número isolado não monta a URL: use a busca do repositório ou a listagem do ano.

**Vedado usar o repositório para:**

| Uso vedado | Por quê |
|---|---|
| citar texto | conversão automática e OCR; não é fonte |
| apurar vigência | `situacao` e `revogada` são metadados congelados em `baixado_em`; há estados com coleta parada ou parcial |
| checar redação anterior da Constituição | o conversor da CF omite as redações tachadas — a concordância é artefato, não conferência |
| obter ementa ou acórdão | jurisprudência em coleta inicial |
| obter data de norma | commits anteriores a 1970 têm data fixada em 01/01/1970; a data real está no título |

**Risco de OCR documentado:** ordem de leitura trocada em digitalização de duas colunas e ordinal lido como dezena (`Art. 19` por `Art. 1º`). Atinge os estados servidos por PDF escaneado — AC, AL, AM, PB, PI, RO, RR, TO, PA, MA, RN, RS. Neles, use o repositório só pelo índice e pela URL.

Concordância com o repositório **não é confirmação independente**. Se ele registrar divergência entre fontes oficiais, propague o alerta.

## Falha de acesso

Se a fonte não abrir, exigir captcha, bloquear acesso automatizado ou devolver página vazia:

1. **Não contorne** o bloqueio.
2. **Não** produza o texto de memória.
3. Registre `NÃO CONFERIDO` e peça ao operador o link aberto no navegador, o arquivo da página ou o texto copiado.
4. Trate o material recebido conforme a seção "Texto fornecido pelo operador" do `SKILL.md`: data de recebimento ≠ data de acesso.
