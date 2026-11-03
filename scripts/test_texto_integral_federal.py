"""Evita publicar errata avulsa como se fosse a norma integral."""
from pathlib import Path
import sys
import unittest
import tempfile
import gzip
import json
from unittest.mock import patch, Mock
from urllib.error import HTTPError
sys.path.insert(0, str(Path(__file__).resolve().parent))
import baixar_federal as f


class TextoIntegral(unittest.TestCase):
    def test_recusa_http_nao_e_retentada(self):
        error = HTTPError('https://normas.leg.br/', 403, 'Forbidden', {}, None)
        with patch.object(f, 'LIMITE', Mock()), patch.object(f.urllib.request, 'urlopen', side_effect=error) as request:
            with self.assertRaisesRegex(RuntimeError, 'fonte recusou HTTP 403'):
                f.http_get('https://normas.leg.br/')
        self.assertEqual(request.call_count, 1)

    def test_original_antes_da_retificacao_mais_recente(self):
        original = {'contentUrl': 'https://normas.leg.br/original', 'version': 'Original', 'datePublished': '2000-01-01'}
        errata = {'contentUrl': 'https://normas.leg.br/errata', 'version': 'Intermediate', 'datePublished': '2000-02-01'}
        self.assertEqual(f.escolher_texto({'encoding': [original, errata]}), original)

    def test_refazer_so_regrava_republicacao(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / 'a.md'; b = Path(tmp) / 'b.md'
            a.write_text('---\nversao_texto: "republicação/retificação"\n---\n', encoding='utf-8')
            b.write_text('---\nversao_texto: "original"\n---\n', encoding='utf-8')
            self.assertTrue(f._e_so_republicacao(str(a)))
            self.assertFalse(f._e_so_republicacao(str(b)))

    def test_compilada_antes_do_original(self):
        original = {'contentUrl': 'https://normas.leg.br/original', 'version': 'Original'}
        atual = {'contentUrl': 'https://normas.leg.br/atual', 'version': 'Current'}
        self.assertEqual(f.escolher_texto({'encoding': [original, atual]}), atual)

    def test_artigo_citado_em_errata_nao_e_artigo_proprio(self):
        corpo = 'DECRETO Nº 3.435, DE 25 DE ABRIL DE 2000.\n\nNos arts. 3º e 5º do Anexo, onde se lê A, leia-se B.'
        self.assertIsNotNone(f.motivo_texto_parcial_decreto('DEC-n', corpo))

    def test_retificacao_com_artigo_copiado_continua_errata(self):
        self.assertIsNotNone(f.motivo_texto_parcial_decreto('DEC-n', '**RETIFICAÇÃO**\n\nArt. 1º Onde se lê A, leia-se B.'))

    def test_artigo_normativo_proprio(self):
        self.assertIsNone(f.motivo_texto_parcial_decreto('DEC-n', 'DECRETO Nº 1\n\n**Art**. 1º Fica aprovado o regulamento.\n\nArt. 2º Revogam-se as disposições.'))

    def test_errata_anexada_depois_da_norma_nao_torna_texto_avulso(self):
        corpo = 'DECRETO Nº 1\n\nArt. 1º Fica aprovado o regulamento.\n\nArt. 2º Este decreto entra em vigor.\n\nBrasília, 1 de janeiro de 2000.\n\nRETIFICAÇÃO\n\nNo anexo, onde se lê A, leia-se B.'
        self.assertIsNone(f.motivo_texto_parcial_decreto('DEC-n', corpo))

    def test_coletor_exige_epigrafe_e_revisao_so_em_area_privada(self):
        d = {'tipo': 'DEC-n', 'numero': '1', 'dataassinatura': '01/01/2000',
             'normaNome': 'Decreto nº 1 de 01/01/2000', 'norma': 'DEC-1-2000-01-01', 'id': 'fixture'}
        html = '<p>DECRETO Nº 1/2000</p><p>Art. 1º Fica autorizado o pagamento.</p><p>Brasília, 1 de janeiro de 2000.</p>'.encode()
        for revision in [False, True]:
            with self.subTest(revisao=revision), tempfile.TemporaryDirectory() as tmp:
                base = Path(tmp) / 'federal'
                stage = base / '_fonte/auditorias/revisao/work'
                with patch.object(f, 'RAIZ', str(stage if revision else base)):
                    info = f.montar(d)
                    meta = json.dumps({'legislationIdentifier': info['urn'], 'legislationDate': info['data'],
                                       'legislationType': 'Decreto Numerado',
                                       'encoding': {'contentUrl': 'https://example.invalid/texto', 'version': 'Original'}}).encode()
                    def response(url, *args, **kwargs):
                        return 200, meta if 'api/public/normas?' in url else html
                    with patch.object(f, 'http_get', response):
                        status, _, _ = f.processar(d, revisao_identidade=revision)
                    self.assertEqual(status, 'ok' if revision else 'sem_texto')
                    self.assertEqual(gzip.decompress(Path(info['fonte']).read_bytes()), html)
                    self.assertEqual(Path(info['md']).exists(), revision)
                    if revision:
                        self.assertIn('identidade_pendente_revisao: true', Path(info['md']).read_text())
                with patch.object(f, 'RAIZ', str(base)), patch.object(f, 'http_get', Mock()) as network:
                    with self.assertRaisesRegex(ValueError, 'nunca na raiz publicável'):
                        f.processar(d, revisao_identidade=True)
                    network.assert_not_called()

    def test_coletor_retem_visual_ou_anexo_ausente_preservando_fonte(self):
        d = {'tipo': 'DEC-n', 'numero': '1', 'dataassinatura': '01/01/2000',
             'normaNome': 'Decreto nº 1 de 01/01/2000', 'norma': 'DEC-1-2000-01-01', 'id': 'fixture'}
        base = '<p>DECRETO Nº 1, DE 1 DE JANEIRO DE 2000.</p><p>Art. 1º Fica aprovado o Regimento que com este baixa.</p><p>Brasília, 1 de janeiro de 2000.</p><p>PRESIDENTE</p>'
        for suffix in ['', '<img src="anexo.png">', '<!--[if gte vml 1]><v:imagedata src="a.wmz"/><![endif]-->']:
            with self.subTest(suffix=suffix), tempfile.TemporaryDirectory() as tmp, patch.object(f, 'RAIZ', tmp):
                info = f.montar(d)
                raw = (base + suffix).encode()
                meta = {'encoding': {'contentUrl': 'https://example.invalid/texto', 'version': 'Original'}}
                with patch.object(f, 'obter_metadados', return_value=(info['urn'], meta)), patch.object(f, 'http_get', return_value=(200, raw)):
                    status, _, detail = f.processar(d)
                self.assertEqual(status, 'sem_texto')
                self.assertFalse(Path(info['md']).exists())
                self.assertEqual(gzip.decompress(Path(info['fonte']).read_bytes()), raw)
                self.assertTrue(detail['elementos_visuais'] or detail['evidencia_anexo'])

    def test_visual_fora_tabela_e_em_comentario_condicional(self):
        from preparar_lote_decretos_cache import Visivel
        for html in ['<p>Anexo</p><img src="anexo.png">',
                     '<!--[if gte vml 1]><v:shape><v:imagedata src="anexo.wmz"/></v:shape><![endif]-->',
                     '<p>Fórmula</p><m:oMath>f</m:oMath>']:
            parser = Visivel()
            parser.feed(html)
            self.assertTrue(parser.visual, html)

    def test_comando_sem_artigos_exige_revisao(self):
        self.assertIsNotNone(f.motivo_texto_parcial_decreto('DEC-n', 'O PRESIDENTE faz públicos os depósitos.\n\nRio de Janeiro.'))


if __name__ == '__main__':
    unittest.main()
