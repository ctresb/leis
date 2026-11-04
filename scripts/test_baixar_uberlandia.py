"""Regressões do coletor de Uberlândia: leitura das edições, do documento e do corpo."""
import gzip
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comum import canonico  # noqa: E402
import baixar_uberlandia as coletor  # noqa: E402

LISTAGEM = """
<div class="box-publicacao" data-key="22837">
        <h4 style="margin-bottom: -10px">Edição nº 7465/Ano XXXVIII</h4>
        Sexta-feira, 23 de outubro de 2026        <br /><br />
</div>
<div class="box-publicacao" data-key="22276">
        <h4 style="margin-bottom: -10px">Edição nº 7460/Ano XXXVIII</h4>
        Sexta-feira, 16 de outubro de 2026        <br /><br />
</div>
"""

EDICAO = """<div id="w0" class="publicacao"><div class="box-publicacao" style="padding:20px 25px 70px 25px" data-key="53507">
    <h4>DECRETO S/Nº - EXONERA DANIEL NORONHA DE ALCINO</h4>
    <p>Categoria: Decreto s/nº</p>
            <a class="col col-link-interno" href="/documento/view/53507/decreto-sn-exonera-daniel-noronha-de-alcino" title="Saiba mais">ÍNTEGRA</a></div>
<div class="box-publicacao" style="padding:20px 25px 70px 25px" data-key="53693">
    <h4>LEI Nº 14.877, DE 19 DE OUTUBRO DE 2026.</h4>
    <p>Categoria: Lei Ordinária</p>
            <a class="col col-link-interno" href="/documento/view/53693/lei-n-14877-de-19-de-outubro-de-2026" title="Saiba mais">ÍNTEGRA</a></div>
"""

PAGINA = """<meta name="csrf-token" content="Nv6IiJv20SJodtIED-xph8TubDmTrF1OOusa-sNg4ylXpv2l9L6oaAlGpUF1uyDC8IhbWNboFi9zhUi_mgaIeA==">
<h2 class="nomargin nopadding roboto text-uppercase"><strong>LEI Nº 14.877, DE 19 DE OUTUBRO DE 2026. </strong></h2>
<strong>Data de Veiculação:</strong> 19 de outubro de 2026<br />
<strong>Publicado Em:</strong> Diário Oficial - Edição nº 7461/Ano XXXVIII<br/>
<strong>Orgão/Secretaria:</strong> Atos do Prefeito<br />
<strong>Categoria:</strong> Lei Ordinária<br />
<div class="modal fade dontPrint" id="divImpressao">Imprimir</div></div><!-- /.modal -->
<hr /><br />
<p>ALTERA O ANEXO IX DA LEI Nº 11.966, E DÁ OUTRAS PROVIDÊNCIAS.</p>
<p><span>Art. 1º Fica alterado o anexo.</span></p>
<div class="col-12 col-lg-4 dontPrint"><div class="box-diario-view">Edição nº 7461</div></div>
"""


# Edição com o que a página real tem de irregular: bloco sem link de documento e
# publicação repetida. Serve para matar as mutações de `not link`/`vistos`.
EDICAO_IRREGULAR = """<div class="box-publicacao" data-key="900"><p>Categoria: Extrato</p></div>
<div class="box-publicacao" data-key="53507"><h4>DECRETO S/Nº - EXONERA</h4><p>Categoria: Decreto s/nº</p>
    <a href="/documento/view/53507/decreto-sn-exonera">ÍNTEGRA</a></div>
<div class="box-publicacao" data-key="53507"><h4>DECRETO S/Nº - EXONERA</h4><p>Categoria: Decreto s/nº</p>
    <a href="/documento/view/53507/decreto-sn-exonera">ÍNTEGRA</a></div>
<div class="box-publicacao" data-key="53693"><h4>LEI Nº 14.877</h4><p>Categoria: Lei Ordinária</p>
    <a href="/documento/view/53693/lei-n-14877">ÍNTEGRA</a></div>
"""


def bloco_edicao(ident, numero, dia):
    return (f'<div class="box-publicacao" data-key="{ident}">'
            f'<h4>Edição nº {numero}/Ano XXXVIII</h4>Sexta-feira, {dia} de outubro de 2026<br /><br /></div>')


# Duplicata na mesma página, um id só na primeira e outro só na segunda: é o que
# separa `continue` de `break` e o controle de parada entre páginas.
PAGINAS = {
    0: bloco_edicao("100", "7460", 16) + bloco_edicao("100", "7460", 16) + bloco_edicao("200", "7461", 19),
    1: bloco_edicao("300", "7462", 20),
    2: bloco_edicao("300", "7462", 20),
}


class ColetorUberlandiaTest(unittest.TestCase):
    def test_edicoes_da_listagem(self):
        with patch.object(coletor.rede, "get", return_value=(200, LISTAGEM.encode("utf-8"), "")):
            lista = coletor.edicoes(limite_paginas=1)
        self.assertEqual([e[0] for e in lista], ["22837", "22276"])
        self.assertEqual(lista[0][2], "2026-10-23")

    def test_edicoes_paginam_e_param_na_primeira_pagina_sem_novidade(self):
        def pagina_falsa(url, *a, **kw):
            return (200, PAGINAS[int(url.rsplit("page=", 1)[1])].encode("utf-8"), "")
        with patch.object(coletor.rede, "get", side_effect=pagina_falsa) as chamadas:
            lista = coletor.edicoes()
        self.assertEqual([e[0] for e in lista], ["100", "200", "300"])
        self.assertEqual(lista[0][1], "Edição nº 7460/Ano XXXVIII")
        self.assertEqual(chamadas.call_count, 3)

    def test_edicoes_com_http_diferente_de_200_falham_alto(self):
        with patch.object(coletor.rede, "get", return_value=(500, b"<html>erro</html>", "")):
            with self.assertRaisesRegex(RuntimeError, "HTTP 500"):
                coletor.edicoes(limite_paginas=1)

    def test_edicoes_vazias_falham_alto(self):
        with patch.object(coletor.rede, "get", return_value=(200, b"<html></html>", "")):
            with self.assertRaisesRegex(RuntimeError, "listagem de edições vazia"):
                coletor.edicoes(limite_paginas=1)

    def test_publicacoes_da_edicao_trazem_categoria_e_titulo(self):
        with patch.object(coletor.rede, "get", return_value=(200, EDICAO.encode("utf-8"), "")):
            docs = coletor.publicacoes_da_edicao("22276")
        self.assertEqual([d[0] for d in docs], ["53507", "53693"])
        self.assertEqual(docs[0][2], "Decreto s/nº")
        self.assertEqual(docs[1][2], "Lei Ordinária")
        self.assertEqual(docs[1][3], "LEI Nº 14.877, DE 19 DE OUTUBRO DE 2026.")

    def test_publicacoes_ignoram_bloco_sem_link_e_repetido(self):
        with patch.object(coletor.rede, "get", return_value=(200, EDICAO_IRREGULAR.encode("utf-8"), "")):
            docs = coletor.publicacoes_da_edicao("22276")
        self.assertEqual([d[0] for d in docs], ["53507", "53693"])
        self.assertEqual(docs[1][1], "lei-n-14877")

    def test_publicacoes_com_http_diferente_de_200_falham_alto(self):
        with patch.object(coletor.rede, "get", return_value=(403, b"<html>bloqueado</html>", "")):
            with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
                coletor.publicacoes_da_edicao("22276")

    def test_edicao_sem_publicacoes_falha_alto(self):
        with patch.object(coletor.rede, "get", return_value=(200, b"<html></html>", "")):
            with self.assertRaisesRegex(RuntimeError, "sem publicações reconhecidas"):
                coletor.publicacoes_da_edicao("22276")

    def test_documento_e_corpo_sem_rodape(self):
        with patch.object(coletor.rede, "get", return_value=(200, PAGINA.encode("utf-8"), "")):
            doc, _ = coletor.ler("53693", "lei-n-14877", "2026-10-19")
        self.assertEqual(doc["chave"], "lei ordinaria")
        self.assertEqual(doc["numero"], "14877")
        self.assertEqual(doc["data"], "2026-10-19")
        self.assertEqual(doc["orgao"], "Atos do Prefeito")
        self.assertTrue(doc["corpo"].startswith("ALTERA O ANEXO IX DA LEI Nº 11.966"))
        self.assertIn("Art. 1º", doc["corpo"])
        self.assertNotIn("Edição nº 7461", doc["corpo"])
        self.assertNotIn("Imprimir", doc["corpo"])

    def test_documento_guarda_titulo_e_ano(self):
        with patch.object(coletor.rede, "get", return_value=(200, PAGINA.encode("utf-8"), "")):
            doc, _ = coletor.ler("53693", "lei-n-14877", "2026-10-19")
        self.assertEqual(doc["titulo"], "LEI Nº 14.877, DE 19 DE OUTUBRO DE 2026.")
        self.assertEqual(doc["ano"], "2026")

    def test_data_da_epigrafe_prevalece_sobre_a_da_veiculacao(self):
        pagina = PAGINA.replace("Data de Veiculação:</strong> 19 de outubro de 2026",
                                "Data de Veiculação:</strong> 20 de outubro de 2026")
        with patch.object(coletor.rede, "get", return_value=(200, pagina.encode("utf-8"), "")):
            doc, _ = coletor.ler("53693", "lei-n-14877", "2026-10-20")
        self.assertEqual(doc["data"], "2026-10-19")
        self.assertEqual(doc["data_publicacao"], "2026-10-20")

    def test_sem_epigrafe_nem_veiculacao_usa_a_data_da_edicao(self):
        pagina = PAGINA.replace(", DE 19 DE OUTUBRO DE 2026.", ".").replace(
            "Data de Veiculação:</strong> 19 de outubro de 2026", "Data de Veiculação:</strong> ")
        with patch.object(coletor.rede, "get", return_value=(200, pagina.encode("utf-8"), "")):
            doc, _ = coletor.ler("53693", "lei-n-14877", "2026-10-21")
        self.assertEqual(doc["data"], "2026-10-21")
        self.assertEqual(doc["data_publicacao"], "2026-10-21")

    def test_documento_com_http_diferente_de_200_falha_alto(self):
        with patch.object(coletor.rede, "get", return_value=(404, b"<html>sumiu</html>", "")):
            with self.assertRaisesRegex(RuntimeError, "HTTP 404"):
                coletor.ler("53693", "lei-n-14877", "2026-10-19")

    def test_corpo_curto_e_reportado_como_sem_texto(self):
        curto = PAGINA.replace("<p><span>Art. 1º Fica alterado o anexo.</span></p>", "<p>oi</p>")
        with patch.object(coletor.rede, "get", return_value=(200, curto.encode("utf-8"), "")):
            doc, bruto = coletor.ler("53693", "lei-n-14877", "2026-10-19")
        self.assertIsNone(doc)
        self.assertTrue(bruto)

    def test_corpo_sem_bloco_de_impressao_falha_alto(self):
        pagina = PAGINA.replace('id="divImpressao"', 'id="outraCoisa"').replace("<!-- /.modal -->", "<!-- x -->")
        with self.assertRaises(RuntimeError):
            coletor.corpo(pagina)

    def test_decreto_nao_numerado_vai_para_a_pasta_propria(self):
        self.assertEqual(canonico(coletor.CATEGORIAS[coletor.normalizar_chave("Decreto s/nº")]),
                         ("decretos-nao-numerados", "Decreto (não numerado)"))

    def test_data_extenso_aceita_dia_da_semana_e_epigrafe(self):
        self.assertEqual(coletor.data_extenso("Sexta-feira, 23 de outubro de 2026"), "2026-10-23")
        self.assertEqual(coletor.data_extenso("DE 8 DE OUTUBRO DE 2026"), "2026-10-08")
        self.assertIsNone(coletor.data_extenso("32 de outubro de 2026"))


    def test_data_extenso_acerta_todos_os_meses(self):
        nomes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
                 "agosto", "setembro", "outubro", "novembro", "dezembro"]
        for mes, nome in enumerate(nomes, 1):
            with self.subTest(mes=nome):
                self.assertEqual(coletor.data_extenso(f"1 de {nome} de 2026"), f"2026-{mes:02d}-01")


class ProvenienciaTest(unittest.TestCase):
    def test_grava_hashes_e_detecta_divergencia(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(coletor, "RAIZ", tmp):
            with patch.object(coletor.rede, "get", return_value=(200, PAGINA.encode("utf-8"), "")):
                doc, bruto = coletor.ler("53693", "lei-n-14877", "2026-10-19")
            sha_fonte = coletor.hash_fonte(bruto)
            self.assertEqual(coletor.gravar(doc, sha_fonte), "novo")
            texto = next(Path(tmp).rglob("*.md")).read_text()
            self.assertIn(f'sha256_fonte: "{sha_fonte}"', texto)
            self.assertIn(f'sha256_texto: "{hashlib.sha256(doc["corpo"].encode()).hexdigest()}"', texto)
            self.assertEqual(coletor.gravar(doc, sha_fonte), "pulado")
            doc["corpo"] += "\n\nArt. 3º Revogam-se as disposições em contrário.\n"
            self.assertEqual(coletor.gravar(doc, sha_fonte), "divergente")

    def test_decreto_sem_numero_usa_sn_no_nome_do_arquivo(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(coletor, "RAIZ", tmp):
            with patch.object(coletor.rede, "get", return_value=(200, PAGINA.encode("utf-8"), "")):
                doc, bruto = coletor.ler("53693", "lei-n-14877", "2026-10-19")
            doc["chave"], doc["numero"] = "decreto nao numerado", ""
            self.assertEqual(coletor.gravar(doc, coletor.hash_fonte(bruto)), "novo")
            self.assertEqual([p.name for p in Path(tmp).rglob("*.md")],
                             ["decreto-nao-numerado-sn-2026-dom-53693.md"])

    def test_cabecalho_com_data_vazia(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(coletor, "RAIZ", tmp):
            with patch.object(coletor.rede, "get", return_value=(200, PAGINA.encode("utf-8"), "")):
                doc, bruto = coletor.ler("53693", "lei-n-14877", "2026-10-19")
            doc["data"] = ""
            coletor.gravar(doc, coletor.hash_fonte(bruto))
            texto = next(Path(tmp).rglob("*.md")).read_text()
        self.assertIn('data: ""', texto)

    def test_dois_documentos_na_mesma_pasta(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(coletor, "RAIZ", tmp):
            with patch.object(coletor.rede, "get", return_value=(200, PAGINA.encode("utf-8"), "")):
                doc, bruto = coletor.ler("53693", "lei-n-14877", "2026-10-19")
            sha = coletor.hash_fonte(bruto)
            self.assertEqual(coletor.gravar(doc, sha), "novo")
            doc["id"] = "53694"
            self.assertEqual(coletor.gravar(doc, sha), "novo")
            self.assertEqual(len(list(Path(tmp).rglob("*.md"))), 2)

    def test_registrar_falha_usa_a_chave_da_casa(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(coletor, "FALHAS", tmp + "/falhas.jsonl"):
            coletor.registrar_falha("https://exemplo/doc", "estourou")
            coletor.registrar_falha("https://exemplo/doc2", "mudou", status="divergente")
            coletor.registrar_falha("https://exemplo/doc3", "ção" * 200)
            brutas = (Path(tmp) / "falhas.jsonl").read_text().splitlines()
            linhas = [json.loads(l) for l in brutas]
        self.assertEqual(linhas[0]["assoc"], "uberlandia")
        self.assertEqual(linhas[0]["status"], "erro")
        self.assertEqual(linhas[1]["status"], "divergente")
        self.assertEqual(linhas[0]["url"], "https://exemplo/doc")
        self.assertIn("ção", brutas[2])
        self.assertEqual(len(linhas[2]["erro"]), 300)

    def test_original_arquivado_bate_com_o_sha256_fonte(self):
        with tempfile.TemporaryDirectory() as tmp, \
                patch.object(coletor, "RAIZ", tmp), patch.object(coletor, "FONTE", tmp):
            with patch.object(coletor.rede, "get", return_value=(200, PAGINA.encode("utf-8"), "")):
                doc, bruto = coletor.ler("53693", "lei-n-14877", "2026-10-19")
            sha_fonte = coletor.hash_fonte(bruto)
            self.assertEqual(coletor.gravar(doc, sha_fonte), "novo")
            coletor.guardar_bruto("53693", coletor.fonte_limpa(bruto))
            arquivado = gzip.decompress((Path(tmp) / "documento-53693.html.gz").read_bytes())
            self.assertEqual(hashlib.sha256(arquivado).hexdigest(), sha_fonte)

    def test_hash_da_fonte_ignora_o_token_csrf(self):
        a = PAGINA.replace("Nv6IiJv20SJodtIED", "AAAA1111BBBB2222")
        b = PAGINA.replace("Nv6IiJv20SJodtIED", "ZZZZ9999YYYY8888")
        self.assertEqual(coletor.hash_fonte(a.encode("utf-8")), coletor.hash_fonte(b.encode("utf-8")))

    def test_fonte_limpa_preserva_o_resto_da_pagina(self):
        limpo = coletor.fonte_limpa(PAGINA.encode("utf-8")).decode("utf-8")
        self.assertIn('name="csrf-token" content=""', limpo)
        self.assertIn("Art. 1º Fica alterado o anexo.", limpo)


if __name__ == "__main__":
    unittest.main()
