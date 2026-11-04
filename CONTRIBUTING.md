# Contribuindo com o ctresb/leis

Este repositório consolida o ordenamento jurídico brasileiro em Markdown estruturado. Para manter a integridade de um acervo com centenas de milhares de normas e garantir que os scripts de auditoria passem sem erros, siga as diretrizes abaixo.

---

## 1. Clonando o repositório sem sobrecarregar a máquina

O repositório possui centenas de milhares de commits e múltiplos gigabytes de histórico. **Evite fazer um `git clone` comum**.

### Clone raso (Shallow Clone)
Para contribuir pontualmente com uma norma ou script:
```bash
git clone --depth 1 [https://github.com/ctresb/leis.git](https://github.com/ctresb/leis.git)
```

### Sparse Checkout (Recomendado para normas municipais)
Se for trabalhar apenas com uma região (por exemplo, normas municipais de SC), baixe somente o que precisa:
```bash
git clone --depth 1 --filter=blob:none --no-checkout [https://github.com/ctresb/leis.git](https://github.com/ctresb/leis.git)
cd leis
git sparse-checkout init --cone
git sparse-checkout set scripts municipais/SC
git checkout main
```

---

## 2. Padrão de Arquivos e Metadados (YAML Frontmatter)

Todo arquivo `.md` precisa conter obrigatoriamente um cabeçalho YAML com os campos rigorosamente na ordem abaixo, seguido por uma linha em branco, o título principal (`#`) e o texto compilado:

```markdown
---
titulo: "Lei nº 1.234 de 10/05/2010"
uf: "SC"
municipio: "Joinville"
tipo: "Lei Ordinária"
numero: "1234"
data: 2010-05-10
ementa: "Ementa oficial da norma."
situacao: "Em vigor"
revogada: false
versao_texto: "compilada (texto vigente)"
publicacao: "DOM de 11/05/2010"
data_publicacao: 2010-05-11
fonte: "https://url-oficial-da-fonte"
baixado_em: 2026-10-21
---

# Lei nº 1.234 de 10/05/2010

LEI Nº 1.234, DE 10 DE MAIO DE 2010

Texto oficial da lei em Markdown...
```

### Regras do vocabulário canônico:
* O campo `tipo` e as pastas correspondentes devem seguir exclusivamente as strings definidas no dicionário `CANONICO` em `scripts/comum.py`.
* **Não** utilize títulos adicionais (`#`, `##`) no corpo da lei. Apenas o título principal da norma recebe `#`. Artigos, parágrafos e incisos permanecem em texto corrido limpo.

---

## 3. Diretrizes para Scripts de Raspagem (Scrapers)

Ao propor novos baixadores (especialmente para a Fase 3 - Legislação Municipal):
1. **Taxa de requisição:** Limite a 1 a 4 requisições por segundo (`time.sleep(1)`).
2. **Idempotência:** O script deve verificar se o arquivo `.md` já existe no destino antes de fazer a requisição de download.
3. **Cache de brutos:** Mantenha os arquivos brutos (HTML ou PDFs baixados) separados do versionamento do git para reprodução futura.

---

## 4. Validação Pré-Commit (Obrigatório)

Nenhum Pull Request deve ser submetido sem antes rodar a ferramenta interna de validação. O script valida a sintaxe YAML, existência no calendário e integridade estrutural:

```bash
git add municipais/
python3 scripts/auditar.py --staged
```

O commit só deve ser criado se o script reportar zero erros.
