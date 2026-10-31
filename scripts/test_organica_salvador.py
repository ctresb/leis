import gzip
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent))
from converter_organica_salvador import preparar, OLD_MARKER, NEW_MARKER, ROOT


class Salvador(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(gzip.decompress((ROOT/'municipais/_lotes/20261020-salvador-lo/extracao-integral.json.gz').read_bytes()))

    def test_89_paginas_e_reversao_unica_do_marcador(self):
        result, proof = preparar(self.fixture['layout_original'], self.fixture['bbox'])
        self.assertEqual(len(proof), 89)
        self.assertEqual(sum(r['sequencia_caracteres_identica'] for r in proof), 85)
        self.assertEqual(result.replace(NEW_MARKER, OLD_MARKER, 1), self.fixture['layout_original'])

    def test_pontuacao_perdida_nao_passa_por_tokens(self):
        chunks = self.fixture['layout_original'].split('\f')
        chunks[5] = chunks[5].replace('.', '', 1)
        with self.assertRaises(ValueError):
            preparar('\f'.join(chunks), self.fixture['bbox'])

    def test_permutacao_em_pagina_visual_exige_nova_revisao(self):
        chunks = self.fixture['layout_original'].split('\f')
        chunks[1] = chunks[1].replace('Carlos', 'sCarlo', 1)
        self.assertNotEqual(chunks[1], self.fixture['layout_original'].split('\f')[1])
        with self.assertRaisesRegex(ValueError, 'revista visualmente'):
            preparar('\f'.join(chunks), self.fixture['bbox'])


if __name__ == '__main__':
    unittest.main()
