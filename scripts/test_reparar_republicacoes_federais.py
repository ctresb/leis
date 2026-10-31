import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reparar_republicacoes_federais as r


class ReparoTest(unittest.TestCase):
    def setUp(self):
        self.meta = {'urn': 'urn:lei:123', 'numero': '123'}
        self.api = {'legislationIdentifier': 'urn:lei:123'}
        self.enc = {'version': 'Original'}
        self.html = '<p>LEI Nº 123</p><p>Art. 1º Texto completo.</p>'
        self.md = 'LEI Nº 123\n\nArt. 1º Texto completo.'

    def check(self, **kwargs):
        args = dict(meta=self.meta, api=self.api, enc=self.enc, html=self.html,
                    markdown=self.md, rendered=self.html)
        args.update(kwargs)
        r.validar(**args)

    def test_original_integral(self):
        self.check()

    def test_artigo_unico_nao_e_falso_positivo(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(r, 'ROOT', Path(folder)):
            path = Path(folder) / 'lei.md'
            path.write_text('---\nversao_texto: "republicação/retificação"\n---\n# Lei\n\nArtigo único. Fica autorizado.')
            with patch.object(r.federal, 'http_get') as request:
                result = r.preparar(path, Path(folder) / 'saida', [])
            self.assertEqual(result['status'], 'pulado')
            request.assert_not_called()

    def test_compilada_integral(self):
        self.check(enc={'version': 'Current'})

    def test_intermediate_nao_e_fallback(self):
        with self.assertRaisesRegex(ValueError, 'intermediária'):
            self.check(enc={'version': 'Intermediate'})

    def test_urn_divergente(self):
        with self.assertRaisesRegex(ValueError, 'URN'):
            self.check(api={'legislationIdentifier': 'urn:outra:123'})

    def test_artigo_citado_na_promulgacao_parcial(self):
        with self.assertRaisesRegex(ValueError, 'vetadas'):
            self.check(markdown='LEI Nº 123\nPartes vetadas\nArt. 1º Texto completo.')

    def test_sem_artigo_inicial(self):
        with self.assertRaisesRegex(ValueError, 'artigo 1'):
            self.check(markdown='LEI Nº 123\nArt. 2º Outro artigo.')

    def test_outro_numero(self):
        with self.assertRaisesRegex(ValueError, 'número'):
            self.check(meta={'urn': 'urn:lei:123', 'numero': '124'})

    def test_perda_de_texto_renderizado(self):
        with self.assertRaisesRegex(ValueError, 'pontuação'):
            self.check(rendered=self.html.replace('completo.', 'completo'))

    def test_visual_nao_descartado(self):
        with self.assertRaisesRegex(ValueError, 'visual'):
            self.check(html=self.html + '<img src="anexo.png">')

    def test_tachado_css_nao_descartado(self):
        with self.assertRaisesRegex(ValueError, 'CSS'):
            self.check(html='<style>.antigo{text-decoration:line-through}</style>' + self.html)

    def test_perda_de_tachado_inline(self):
        with self.assertRaisesRegex(ValueError, 'tachados'):
            self.check(html=self.html.replace('Texto completo.', '<s>Texto completo.</s>'))

    def test_tabela_nao_pode_ser_achatada(self):
        with self.assertRaisesRegex(ValueError, 'tabelas'):
            self.check(html=self.html + '<table><tr><td>ABC</td></tr></table>', rendered=self.html+'<p>ABC</p>')

    def test_titulo_nao_recebe_pontuacao_inventada(self):
        source = '<p>CAPÍTULO I</p><p>DISPOSIÇÕES</p>'
        md = r.federal.convert(source, preserve_heading_punctuation=True)
        self.assertNotIn('—', md)
        self.assertIn('CAPÍTULO I DISPOSIÇÕES', md)

    def test_preimagem_divergente_nao_altera_nenhum_documento(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(r, 'ROOT', Path(folder)):
            root = Path(folder)
            rows = []
            for i in range(2):
                path = root / f'{i}.md'
                path.write_bytes(b'antigo')
                backup = root / str(i)
                backup.mkdir()
                (backup / 'anterior.md').write_bytes(b'antigo')
                (backup / 'candidato.md').write_bytes(b'novo')
                rows.append({'status': 'preparado', 'arquivo': path.name, 'pasta': str(i),
                             'sha256_anterior': r.sha(b'antigo'), 'sha256_novo': r.sha(b'novo')})
            (root / '1.md').write_bytes(b'edicao concorrente')
            with self.assertRaisesRegex(ValueError, 'preimagem'):
                r.aplicar(rows)
            self.assertEqual((root / '0.md').read_bytes(), b'antigo')

    def test_backup_permanece_apos_aplicar(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(r, 'ROOT', Path(folder)):
            root = Path(folder)
            (root / 'lei.md').write_bytes(b'antigo')
            (root / 'anterior.md').write_bytes(b'antigo')
            (root / 'candidato.md').write_bytes(b'novo')
            self.assertEqual(r.aplicar([{'status': 'preparado', 'arquivo': 'lei.md', 'pasta': '.',
                                        'sha256_anterior': r.sha(b'antigo'), 'sha256_novo': r.sha(b'novo')}]), 1)
            self.assertEqual((root / 'anterior.md').read_bytes(), b'antigo')
            self.assertEqual((root / 'lei.md').read_bytes(), b'novo')


if __name__ == '__main__':
    unittest.main()
