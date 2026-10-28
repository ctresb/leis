# Legislação drasileira em Markdown

A Constituição Federal e normas federais, estaduais, distritais e municipais, convertidas de
fontes oficiais para Markdown, com cabeçalho estruturado e link para a origem de cada texto.
As contagens do acervo publicado são atualizadas a cada commit em **[PROGRESSO.md](PROGRESSO.md)**.

O histórico do git é a própria linha do tempo: as 323.849 normas da base entraram **uma por
commit**, assinadas por quem as promulgou e datadas do dia em que foram aprovadas.

O objetivo é maior do que o que já está aqui: **todo o ordenamento jurídico brasileiro** — leis,
decretos, atos infralegais das agências e órgãos reguladores, tratados internalizados,
jurisprudência vinculante e o direito estadual e municipal — num lugar só, em texto simples, de
graça, para qualquer pessoa.

[![progresso](progresso.svg)](PROGRESSO.md)

O escopo completo está em [`scripts/plano.py`](scripts/plano.py) e a medição item a item — o que
já tem, o que falta, de que fonte vem e em qual pasta fica — em **[PROGRESSO.md](PROGRESSO.md)**,
gerados por `scripts/progresso.py`.

> [!IMPORTANT]
> Os textos têm caráter informativo e **não substituem a publicação no Diário Oficial**. São
> conversões automáticas e OCR de documentos escaneados. Confira sempre a fonte
> indicada no cabeçalho antes de citar.

---

## Base inicial do histórico

As tabelas abaixo registram as 323.849 normas da base inicial; as coletas posteriores estão
contabilizadas em **[PROGRESSO.md](PROGRESSO.md)**.

| Esfera | Normas |
| --- | ---: |
| Constituição Federal | 1 |
| Federal | 29.184 |
| Estadual e distrital | 294.664 |
| **Total** | **323.849** |

Por tipo de instrumento:

| Tipo | Normas | | Tipo | Normas |
| --- | ---: | --- | --- | ---: |
| Lei Ordinária | 289.684 | | Lei Promulgada | 434 |
| Decreto-Lei | 18.366 | | Emenda à Lei Orgânica | 134 |
| Lei Complementar | 12.598 | | Constituição Estadual | 26 |
| Emenda Constitucional | 2.013 | | Decreto-Lei Complementar | 23 |
| Lei Delegada | 550 | | Lei Constitucional | 19 |

As contagens por estado, com o que ficou de fora e por quê, estão em
**[COBERTURA.md](COBERTURA.md)**. Para ver em gráficos — normas por estado, por década, por tema,
as palavras mais frequentes nas ementas e quem mais assinou — abra
**[estatisticas.html](estatisticas.html)** no navegador. É um arquivo único, sem servidor nem
dependência externa, gerado por `scripts/estatisticas.py`.

---

## Estrutura

```
constituicao.md                      Constituição Federal de 1988 (texto compilado, Planalto; edição/data no cabeçalho)
federal/
  leis-ordinarias/AAAA/*.md          Leis federais, de 1822 a hoje
  leis-complementares/AAAA/*.md
  leis-delegadas/  decretos-lei/
estaduais/UF/
  constituicao/                      Constituição estadual
  emendas-constitucionais/
  leis-ordinarias/  leis-complementares/  leis-delegadas/  decretos-lei/
reguladores/<orgao>/<tipo>/          atos infralegais federais (CONTRAN, ANVISA, RFB, CMN…)
jurisprudencia/<tribunal>/           súmulas, temas vinculantes e controle concentrado
tratados/                            tratados internacionais internalizados
municipais/UF/<municipio>/           legislação municipal
scripts/                             o código que baixa, converte e audita
scripts/plano.py                     o escopo: todo tipo de norma que deve estar aqui
COBERTURA.md                         números por esfera e tipo, e as lacunas
PROGRESSO.md                         o plano medido contra o acervo, item a item
progresso.svg                        a imagem de progresso do topo deste README
estatisticas.html                    página com gráficos sobre o acervo
```

Os nomes de pasta são os mesmos em todas as esferas. Algumas unidades têm pastas a mais, porque a
fonte distingue instrumentos que as outras não têm: `leis-promulgadas` (AM, PB),
`decretos-lei-complementares` (SP), `leis-constitucionais` (MG), `constituicoes-historicas` (BA),
`lei-organica` e `emendas-lei-organica` (DF).

Fora do versionamento, porque os scripts os reproduzem: `_fonte/` (27 GB com o HTML e os PDFs
originais, comprimidos), `_indice/` (os índices de cada fonte) e os logs. Os `_falhas.jsonl`, que
registram linha por linha o que não entrou, **estão** versionados.

Fontes integrais, anexos e recibos necessários para verificar uma inclusão podem ser
versionados pontualmente, identificados por origem, captura e SHA-256. Isso preserva a
edição efetivamente consultada quando a fonte muda ou sua conversão exige revisão.

As auditorias registram hashes das dependências de cada lote. Execute os replays no commit
que publicou o lote, ou use os módulos legados e mapas de leitura quando disponibilizados.

---

## Formato dos arquivos

Todo arquivo tem cabeçalho YAML e, no corpo, o título em `#` seguido do texto da norma:

```markdown
---
titulo: "Lei nº 10.406 de 10/01/2002"
uf: "SP"                 # ausente nas normas federais
tipo: "Lei Ordinária"
numero: "10406"
data: 2002-01-10         # sempre presente; vazia quando a fonte não informa
ano: "2002"              # só quando a fonte dá apenas o ano (PA, PE)
ementa: "Institui o Código Civil."
situacao: "Em vigor"
revogada: false
versao_texto: "compilada (texto vigente)"
publicacao: "DOU de 11/01/2002"
data_publicacao: 2002-01-11
urn: "urn:lex:br:federal:lei:2002-01-10;10406"
fonte: "https://normas.leg.br/?urn=urn:lex:br:federal:lei:2002-01-10;10406"
arquivo: "https://…/lei10406.pdf"   # quando o texto veio de um PDF
baixado_em: 2026-10-13
---
# Lei nº 10.406 de 10/01/2002

LEI Nº 10.406, DE 10 DE JANEIRO DE 2002

Institui o Código Civil.
```

`titulo`, `tipo`, `numero`, `data`, `versao_texto`, `fonte` e `baixado_em` existem em **todos** os
arquivos; os demais aparecem quando a fonte os fornece. Os campos saem sempre nessa ordem.

Quando uma transcrição perderia conteúdo visual ou exigiria adivinhar uma leitura, a
representação individual pode incluir fac-símiles ou um PDF oficial integral como anexo
local. O Markdown identifica a forma de representação, a edição e os arquivos por caminho
relativo e SHA-256; texto principal e anexos precisam ter identidade e escopo conferidos.
Esses recursos compõem a mesma norma, sem contagem adicional. Uma referência externa
sem o conteúdo recuperado não resolve uma pendência de integralidade.

No LEGIS/AC, `versao_texto` e `edicao` identificam a transcrição digital do campo
`body-law` no modo Padrão. Esse modo pode incorporar alterações posteriores; a captura
não certifica a edição original do DOE ou a redação vigente.

O campo `tipo` usa o vocabulário canônico definido em `CANONICO`, em
`scripts/comum.py`. O mesmo mapa vale para quem baixa e para `scripts/normalizar.py`, que o reaplica
ao acervo já gravado — por isso `lei-ordinaria` e `leis-ordinarias`, ou `Lei` e `LEI ORDINARIA`, não
coexistem.

Duas exceções, ambas propositais: a `constituicao.md` na raiz é o único arquivo sem cabeçalho, por
ser o documento único de topo; e cinco arquivos trazem, no lugar do texto, um aviso em citação —
a fonte oficial serve um documento vazio para eles e só os metadados foram preservados.

`constituicao.md` é reproduzida pelo comando `python3 -I scripts/converter_constituicao.py`;
acrescente `--check` para conferir sem escrever. O snapshot oficial compilado está em
`fonte/constituicao-compilado.htm`, com origem, data de obtenção e SHA-256 no JSON de mesmo
nome. A captura anterior permanece em `fonte/constituicao.htm`. A EC 141/2026 consultada para
a nota de transição está preservada em `fonte/emc141.htm`, também identificada no JSON.

O conversor da Constituição omite apenas redações tachadas e conserva indicações de
revogação, vigência e decisões judiciais. Isso não certifica eficácia imediata: consulte também
as transições e os prazos das emendas. Os demais documentos mantêm suas versões históricas
e seus tachados; `html2md.convert(..., exclude_struck=True)` é uma opção explícita, nunca o
padrão. As regressões podem ser verificadas com
`python3 -I -m unittest discover -s scripts -p test_vigencia.py`.

---

## O histórico do git

A base do histórico é uma linha do tempo da legislação: **323.851 commits**, um por norma, em
ordem cronológica de 1822 até hoje, cada um assinado por quem promulgou a norma — **5.414
autores**. Foi montada de uma vez só por `scripts/montar_repositorio.py`, com `git fast-import`.

> [!NOTE]
> **As normas que chegam depois entram em commits de lote**, um por coleta — "153.637 decretos
> federais (1889–2026)" —, não mais um commit por norma. Reconstruir a linha do tempo a cada lote
> significaria reescrever e reenviar meio milhão de commits para acrescentar texto novo; o custo
> não se paga. A linha do tempo norma a norma continua no histórico e continua verdadeira para o
> que ela cobre, e `montar_repositorio.py` continua funcionando para quem quiser gerá-la de novo,
> do acervo inteiro, num repositório à parte.

Os autores que mais assinaram, na base:

| Normas | Signatário |
| ---: | --- |
| 4.247 | Marconi Ferreira Perillo Júnior |
| 3.795 | Aécio Neves |
| 3.457 | Geraldo Alckmin |
| 3.097 | Ronaldo Caiado |
| 2.654 | Getúlio Vargas |

O autor sai do bloco de assinatura do próprio texto (`scripts/signatarios.py`). Em cerca de 48% dos
casos a assinatura não está na camada de texto do PDF, ou o OCR a perdeu; nesses, o autor é a
instituição — "Estado do Pará", "República Federativa do Brasil". **A mensagem do commit sempre diz
de onde a autoria saiu**, na linha `Autoria:`. Os demais signatários entram como `Co-Authored-By`.

Os e-mails são sintéticos, no formato `nome-sobrenome-NNNNN@exemplo.com`, com os cinco dígitos
derivados do próprio nome — cada pessoa tem uma identidade só no histórico inteiro.

> [!NOTE]
> **Datas anteriores a 1970.** O git conta a data em segundos desde 1970; qualquer data anterior
> vira timestamp negativo, que o `git fsck` reprova como `badDate` e o GitHub rejeita ao receber.
> Como a maior parte do acervo é anterior a 1970, essas normas têm a data do commit fixada em
> 01-01-1970 e a **data real no fim do título, depois de ` | `**, e repetida no corpo. Nos commits
> com data representável o título fica limpo. A ordem cronológica se mantém pela sequência de
> commits, que é linear.

```
Lei nº 86, de 21/04/1880 | 21-04-1880

AUTORIZA O GOVERNO A DISPENSAR DE PROVAS DE CAPACIDADE PARA EXERCER O MAGISTÉRIO…

Data da norma: 1880-04-21
A data do commit está fixada em 01-01-1970: o git não representa data anterior a essa
(vira timestamp negativo, que o GitHub rejeita). A data real da norma é a do título e
a da linha acima.
Autoria: signatário não identificado no texto; autoria institucional.
Fonte: https://www.al.sp.gov.br/norma/139216
```

As 1.595 normas cuja data não existe em nenhuma fonte ficam no fim do histórico, com
`| sem data na fonte` no título.

---

## Fontes

| UF | Fonte | Texto |
| --- | --- | --- |
| — | Planalto | Constituição Federal, texto vigente |
| Federal | Dados abertos do Senado (índice) + normas.leg.br (texto) | compilado vigente quando existe; senão a publicação original |
| AC, AL, AM, PB, PI, RO, RR, TO | SAPL das Assembleias (API REST) | PDF anexado, com OCR quando escaneado |
| AP | e-Legis da Assembleia | texto integral em PDF + Constituição consolidada |
| BA | Portal de Legislação (Casa Civil) | HTML |
| CE | BELT – Banco Eletrônico de Leis Temáticas | HTML |
| DF | SINJ-DF | texto compilado |
| ES, SE | sistema de legislação das Assembleias | HTML, compilado quando disponível |
| GO | Legisla Goiás (Casa Civil) | HTML |
| MA | GED da Assembleia | PDF |
| MG | Dados abertos da ALMG | texto atualizado quando existe |
| MS | Legislação da Governadoria (Lotus Notes) | HTML |
| MT | Assembleia Legislativa | redação atual, PDF gerado pelo site |
| PA | Banco de Leis da ALEPA | PDF, com OCR quando escaneado |
| PE | Alepe Legis | texto atualizado quando existe |
| PR | Sistema Estadual de Legislação | — ver pendências |
| RJ | Legislação Estadual da ALERJ (Lotus Notes) | — ver pendências |
| RN | Assembleia Legislativa | PDF, acervo a partir de 1994 |
| RS | Sistema LEGIS da Assembleia; Constituição no portal do DAL | PDF nas recentes, HTML nas antigas |
| SC | Legislação SC (ALESC) | texto anotado |
| SP | ALESP (dados abertos + API) | texto atualizado quando existe |

Cada script em `scripts/estados/` documenta no cabeçalho a API ou o caminho que usa.

Todos limitam a taxa a 1–4 requisições por segundo, são retomáveis (pulam o que já existe) e
guardam o original em `_fonte/`. **Bloqueios de acesso automatizado não são contornados.**

---

## O que ainda não está aqui

O plano inteiro, com meta e fonte por tipo de norma, está em **[PROGRESSO.md](PROGRESSO.md)**. Em
resumo, o que falta se organiza em três fases:

| Fase | O quê | Por que nessa ordem |
| --- | --- | --- |
| **1** | Fechar a esfera federal: emendas constitucionais, decretos do Executivo (as duas séries), decretos legislativos, medidas provisórias, resoluções das Casas, regulamentos consolidados (RIR, RIPI, Aduaneiro, RPS) e tratados promulgados | fonte única e já conhecida — `normas.leg.br` e Planalto, a mesma infraestrutura do baixador federal |
| **2** | O infralegal, onde mora a norma que de fato se aplica: CONTRAN e o Manual de Sinalização, NRs do trabalho, RDC da ANVISA, IN da Receita, resoluções do CMN e do Banco Central, CONAMA, CNE, CNJ, TSE, conselhos profissionais; a jurisprudência vinculante (súmulas, repercussão geral, repetitivos, controle concentrado); e o infralegal estadual, com destaque para os 27 RICMS | uma fonte por órgão, cada uma com seu formato — é trabalho de muitos raspadores pequenos |
| **3** | Direito municipal: leis orgânicas, planos diretores, códigos tributários, de obras e de posturas, e as leis das câmaras — começando pelas 27 capitais | 5.570 fontes sem índice central; sozinho é maior que todo o resto somado |

Além disso, ficam de fora as normas cujo texto não existe na fonte ou não pôde ser obtido — cada
caso tem uma linha, com o motivo, no `_falhas.jsonl` da respectiva pasta.

### Pendências

| O quê | Por quê |
| --- | --- |
| **PR** — destravado em 15/10/2026 | o WAF de `legislacao.pr.gov.br` devolvia 403 a partir da segunda requisição. Em novo teste, seis requisições seguidas responderam 200: o bloqueio saiu. `scripts/estados/pr.py` passou a coletar, com lei, lei complementar, emenda, Constituição, decreto, resolução e portaria |
| **RJ** — nada coletado | o Lotus Notes da ALERJ fecha a conexão ou leva mais de 60 s por página. `scripts/estados/rj.py` está pronto para quando o servidor voltar |
| **AC** — só até 2009 | limite do SAPL da Assembleia |
| **TO** — a partir de 2020 | limite do SAPL da Assembleia |
| **RN** — a partir de 1994 | o acervo da Assembleia não tem PDF anterior |
| **RS** — 5.569 leis antigas | estão no índice, mas a página de texto responde "NORMA SEM TEXTO": nunca foram digitalizadas |
| **ES e SE** — 311 e 411 normas | o servidor da Assembleia derruba a conexão nessas mesmas normas, de forma consistente |
| **CE e MA** — só leis | o BELT do Ceará é um Banco Eletrônico de Leis e o GED do Maranhão só serve LEI, EC e LC: nenhuma das duas fontes carrega decreto ou ato infralegal. Precisam das Casas Civis estaduais |
| **MG** — não atualiza mais | `dadosabertos.almg.gov.br/arquivo/legislacao-mineira/download` passou a responder 204 sem conteúdo para todo ano, e o serviço `ws/legislacao` não responde. As 26.733 normas já coletadas continuam no acervo; a atualização precisa de outro caminho na ALMG |

### Qualidade do OCR

Na base inicial, 17.016 arquivos vieram de PDF escaneado, com OCR pelo framework Vision do macOS.
Há dois problemas conhecidos, com correções de alcance diferente:

- **ordem de leitura trocada** em digitalizações de duas colunas — detector implementado, com
  reprocessamento integral do acervo ainda pendente. Sem precisar de
  modelo nenhum: o Vision devolve a caixa de cada linha, então `scripts/ocr.swift` procura a calha
  vertical entre as colunas e emite a da esquerda inteira antes da direita. A correção é
  conservadora por desenho — só age quando há uma calha limpa, com os dois lados cheios e linhas
  largas o bastante para serem prosa, o que afasta tabela de duas colunas, que se lê por linha e
  não por coluna. Numa amostra de 120 PDFs escaneados (431 páginas) de sete estados, **uma página
  tinha calha de prosa**: o defeito é real, e é raro. `scripts/bin/ocr --diagnostico arquivo.pdf`
  relata, por página, se uma calha foi encontrada;
- **ordinais confundidos** (`Art. 19` por `Art. 1º`) — corrigido em 1.509 arquivos por
  `scripts/corrigir_ocr.py`, que só reescreve a corrida `19, 29, 39…` quando ela começa em 19, tem
  ao menos dois termos e a numeração resultante fica coerente. Assim um `Art. 19` legítimo, ou um
  `Art. 99` que cita outra lei, não é tocado.

As correções usam regras de texto e geometria. Ainda podem existir erros de reconhecimento,
segmentação e ordem de leitura; a amostra não comprova a qualidade de todo o acervo.

`baidu/Unlimited-OCR` foi testado em Apple Silicon e não serve localmente: na resolução de treino o
encoder de visão pede ~21 GB, e numa resolução que caiba o prefill leva 221 s por página com saída
vazia. Reprocessar o lote exige GPU NVIDIA.

---

## Reproduzir e atualizar

**Requisitos:** macOS, Python 3 e `pdftotext` (poppler). A reconstrução geométrica dos
diários municipais requer também `pypdf` no mesmo Python. Para o OCR, usa-se o
framework Vision via `swiftc -O scripts/ocr.swift -o scripts/bin/ocr`.

Para JPEG/TIFF/PNG, o conversor pode usar Tesseract 5 com o modelo português
[`tessdata_best/por.traineddata`](https://raw.githubusercontent.com/tesseract-ocr/tessdata_best/main/por.traineddata)
em `scripts/bin/tessdata/por.traineddata`. SHA-256 esperado:
`711de9dbb8052067bd42f16b9119967f30bada80d57e2ef24f65d09f531adb04`.
O Markdown identifica o motor utilizado; os originais permanecem no cache.

```sh
# baixar — todos os scripts são retomáveis: pulam o que já existe
python3 -I scripts/baixar_federal.py
python3 -I scripts/estados/sp.py                # um estado por script
python3 -I scripts/estados/sapl.py baixar PB    # estados com SAPL
python3 -I scripts/estados/spl_agape.py ES      # ES e SE

# manter em ordem
python3 -I scripts/reconverter.py [UF ...]      # regenera os .md a partir de _fonte
python3 -I scripts/normalizar.py                # pastas, tipos e cabeçalhos canônicos
python3 -I scripts/corrigir_ocr.py              # ordinais do OCR
python3 -I scripts/corrigir_datas_invalidas.py  # datas que não existem no calendário
python3 -I scripts/relatorio.py                 # atualiza COBERTURA.md
python3 -I scripts/progresso.py                 # atualiza PROGRESSO.md e progresso.svg
python3 -I scripts/estatisticas.py              # atualiza estatisticas.html

# remontar o histórico do git
python3 -I scripts/montar_repositorio.py --saida /caminho/do/repo
```

Os quatro scripts de manutenção são **idempotentes** e rodam em simulação por padrão: só gravam com
`--aplicar`. Rodar de novo, depois de aplicado, relata zero mudanças.

### Auditorias da base inicial

Os resultados abaixo são da base inicial. Os lotes posteriores exigem validação própria;
`scripts/auditar.py --staged` verifica os arquivos exatamente como entrarão no próximo commit.

| Verificação | Resultado |
| --- | --- |
| `git fsck --strict` | zero erros |
| data em todos os arquivos | 323.848 de 323.848 (a Constituição não tem cabeçalho) |
| data que existe no calendário e não está no futuro | 100% |
| nomes de pasta canônicos | 100% |
| `tipo` no vocabulário fechado | 100% |
| cabeçalho + `# título` + texto | 323.843; 5 com aviso de ausência; 1 por desenho |

---

## Licença

Os textos das normas são **atos oficiais do poder público** e, pelo art. 8º, I, da Lei nº 9.610/98,
não são objeto de proteção autoral. Os scripts deste repositório estão sob a licença MIT — veja
[LICENSE](LICENSE).
