from pathlib import Path
import json
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from propor_cores_html_ta_privado_20261028 import propor, ROOT


class PropostaLiteral(unittest.TestCase):
    def test_cor_tachado_contexto_e_sinais_preservados(self):
        source = '<div class="dptt" id="a"><p>Art. 1º. <span style="color: #e03e2d;" title="literal"><del cite="/ato" datetime="2020-01-01">R$ 0,50</del> — “texto”.</span></p></div>'
        body, proof = propor(source)
        self.assertIn('style="color: #e03e2d;"', body)
        self.assertIn('cite="/ato" datetime="2020-01-01"', body)
        self.assertTrue(proof['replay_V3']['marcacao_tachado_por_caractere_confere'])
        self.assertTrue(proof['inventario_cor_confere'])
        self.assertFalse(proof['apto_para_publicacao'])

    def test_linha_vazia_textual_sem_perda_de_atributos(self):
        body, proof = propor('<div class="dptt" id="a"><p style="color:red">A\n\nB</p></div>')
        self.assertIn('&#10;', body)
        self.assertTrue(proof['DOM_textual_da_selecao_confere'])

    def test_negativos_nao_sao_limpos(self):
        for content in ['<pre style="color:red">A\n\nB</pre>',
                        '<span hidden style="color:red">A</span>',
                        '<span style="white-space:pre;color:red">A</span>',
                        '<span onclick="x()" style="color:red">A</span>',
                        '<span style="color:red;\n\nfont-size:10pt">A</span>']:
            with self.subTest(content=content), self.assertRaises(ValueError):
                propor('<div class="dptt" id="a">' + content + '</div>')

    def test_tabela_colorida_nao_dispensa_gate_congelado(self):
        with self.assertRaisesRegex(ValueError, 'Apresentação contextual'):
            propor('<div class="dptt" id="a"><table><tr><td style="color:red">0</td></tr></table></div>')

    def test_fonte_real_nota_vermelha_sem_aprovacao(self):
        gate = ROOT / 'municipais/_indice/_recuperacao_20261027/lotes/ta-gates-0033/resultados.jsonl'
        row = next(json.loads(x) for x in gate.read_text().splitlines()
                   if json.loads(x)['ta_id'] == 1933 and json.loads(x)['host'] == 'sapl.fozdoiguacu.pr.leg.br')
        raw = (ROOT / row['prova_frontend']['arquivo']).read_text()
        body, proof = propor(raw)
        self.assertIn('Nota: Este texto não substitui o original publicado no Diário Oficial.', body)
        self.assertTrue(proof['replay_V3']['aprovado'])
        self.assertEqual(len(proof['folhas_externas_nao_consultadas']), 4)
        self.assertFalse(proof['apto_para_publicacao'])


if __name__ == '__main__':
    unittest.main()
