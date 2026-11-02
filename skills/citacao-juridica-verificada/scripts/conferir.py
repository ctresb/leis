#!/usr/bin/env python3
"""Cotejo literal de citacao juridica contra o recorte lido da fonte oficial.

Uso:
    python -I conferir.py --fonte recorte.txt --citacao citacao.txt

A fonte deve ser o RECORTE da unidade e da versao corretas (o caput lido, o
paragrafo lido, o enunciado lido) -- nao a pagina inteira. Pagina inteira
produz falso positivo: a redacao revogada do mesmo dispositivo costuma estar
na mesma pagina, e um trecho antigo casaria sem que ninguem percebesse.

Veredito no codigo de saida: 0 LITERAL, 1 NAO CONFERE, 2 AMBIGUO,
3 erro de uso. Qualquer coisa diferente de 0 impede a entrega da citacao.
"""

import argparse
import re
import sys
import unicodedata

MIN_CITACAO = 10          # caracteres normalizados; abaixo disso nada se afirma
MIN_SEGMENTO = 8          # idem, por segmento entre supressoes
MARCAS_TACHADO = ("~~", "<s>", "<strike>", "<del>", "text-decoration")

# Variantes tipograficas que a fonte oficial e a transcricao trocam sem que o
# texto mude: espacos especiais, aspas curvas, travessoes, indicadores de
# ordinal, hifen opcional e caracteres de largura zero.
EQUIVALENCIAS = {
    " ": " ", " ": " ", " ": " ", " ": " ", "　": " ",
    "‘": "'", "’": "'", "‚": "'", "′": "'", "´": "'",
    "“": '"', "”": '"', "„": '"', "″": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-",
    "―": "-", "−": "-",
    "º": "o", "°": "o", "ª": "a",
    "­": "", "​": "", "‌": "", "‍": "", "﻿": "",
}
TABELA = str.maketrans(EQUIVALENCIAS)

RE_SUPRESSAO = re.compile(r"\[\s*(?:\.\.\.|…)\s*\]")


def normalizar(texto):
    texto = unicodedata.normalize("NFC", texto).translate(TABELA)
    texto = re.sub(r"\s+", " ", texto)
    texto = re.sub(r"§\s*", "§", texto)   # "§ 2o" == "§2o"
    return texto.strip()


def prefixo_que_casa(fonte, segmento, inicio):
    """Maior prefixo do segmento ainda encontrado na fonte, para localizar
    o ponto exato em que a transcricao se afasta do original."""
    baixo, alto = 0, len(segmento)
    while baixo < alto:
        meio = (baixo + alto + 1) // 2
        if fonte.find(segmento[:meio], inicio) != -1:
            baixo = meio
        else:
            alto = meio - 1
    return baixo


def conferir(fonte_bruta, citacao_bruta, permitir_ambiguidade=False):
    fonte = normalizar(fonte_bruta)
    citacao = normalizar(citacao_bruta)
    alertas = []

    if not fonte:
        return 3, "ERRO DE USO", ["O arquivo da fonte esta vazio."]
    if len(citacao) < MIN_CITACAO:
        return 3, "ERRO DE USO", [
            "A citacao esta vazia ou e curta demais para ser conferida "
            f"({len(citacao)} caracteres; minimo {MIN_CITACAO})."
        ]

    segmentos = [s.strip() for s in RE_SUPRESSAO.split(citacao)]
    segmentos = [s for s in segmentos if s]
    if not segmentos:
        return 3, "ERRO DE USO", ["A citacao so contem supressoes."]

    n_supressoes = len(RE_SUPRESSAO.findall(citacao))
    if n_supressoes:
        alertas.append(
            f"{n_supressoes} supressao(oes) com [...]: confira se a omissao "
            "nao altera o sentido do dispositivo."
        )

    if any(marca in fonte_bruta for marca in MARCAS_TACHADO):
        alertas.append(
            "A fonte contem marcas de texto tachado: confirme visualmente que "
            "o trecho citado nao esta em redacao revogada ou substituida."
        )

    cursor = 0
    for i, segmento in enumerate(segmentos, 1):
        if len(segmento) < MIN_SEGMENTO:
            alertas.append(
                f"Segmento {i} tem {len(segmento)} caracteres: curto demais "
                "para sustentar conferencia; reveja o recorte."
            )

        ocorrencias = fonte.count(segmento)
        if ocorrencias == 0:
            casa = prefixo_que_casa(fonte, segmento, cursor)
            detalhe = [
                f"Segmento {i} de {len(segmentos)} nao foi encontrado na fonte.",
                f"Divergencia a partir do caractere {casa + 1} do segmento.",
                f"  transcrito: ...{segmento[max(0, casa - 30):casa + 40]}",
            ]
            if casa:
                pos = fonte.find(segmento[:casa], cursor)
                if pos != -1:
                    detalhe.append(f"  na fonte:   ...{fonte[pos + max(0, casa - 30):pos + casa + 40]}")
            return 1, "NAO CONFERE", detalhe + alertas

        if ocorrencias > 1 and not permitir_ambiguidade:
            return 2, "AMBIGUO", [
                f"Segmento {i} aparece {ocorrencias} vezes na fonte.",
                "A fonte pode conter a redacao antiga do mesmo dispositivo. "
                "Recorte a unidade e a versao corretas e confira de novo.",
            ] + alertas

        pos = fonte.find(segmento, cursor)
        if pos == -1:
            return 1, "NAO CONFERE", [
                f"Segmento {i} existe na fonte, mas nao depois do segmento "
                "anterior: a ordem dos trechos nao corresponde ao original.",
            ] + alertas
        cursor = pos + len(segmento)

    return 0, "LITERAL", alertas


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--fonte", required=True,
                   help="arquivo com o RECORTE lido da fonte oficial")
    p.add_argument("--citacao", required=True,
                   help="arquivo com o texto que se pretende citar")
    p.add_argument("--permitir-ambiguidade", action="store_true",
                   help="aceita trecho repetido na fonte (use so quando a "
                        "repeticao for do proprio texto vigente)")
    a = p.parse_args()

    try:
        fonte = open(a.fonte, encoding="utf-8").read()
        citacao = open(a.citacao, encoding="utf-8").read()
    except OSError as e:
        print(f"ERRO DE USO: {e}", file=sys.stderr)
        return 3

    codigo, veredito, notas = conferir(fonte, citacao, a.permitir_ambiguidade)
    print(f"Conferencia textual: {veredito}")
    for nota in notas:
        print(f"  - {nota}")
    if codigo == 0:
        print("  Selo autorizado: LITERAL-MECANICO")
    else:
        print("  NAO ENTREGUE a citacao: releia a fonte e corrija.")
    return codigo


if __name__ == "__main__":
    sys.exit(main())
