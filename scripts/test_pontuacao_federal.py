"""Regressões de números e operadores que a comparação alfanumérica perderia."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parent))
from auditar_pontuacao_federal import contexto_numerico, normalizar_marcador_administrativo
from estados.pe_fidelidade_visivel import comparar_fidelidade


class PontuacaoFederal(unittest.TestCase):
    def test_alteracoes_de_valor_sinal_moeda_e_percentual(self):
        cases = [('0,5', '05'), ('-100', '100'), ('1.000,50', '1000,50'),
                 ('R$ 5,00', '5,00'), ('5%', '5'), ('(100)', '100')]
        for source, changed in cases:
            with self.subTest(source=source):
                result = comparar_fidelidade('<p>'+source+'</p>', source, changed)
                self.assertFalse(result['texto_visivel_md_igual_fonte_apos_formato_heading_comprovado'])
                self.assertFalse(result['numeros_sinais_moedas_percentuais_iguais_fonte'])

    def test_operador_e_asteriscos_literais(self):
        source = '<p>Resultado = 3*5*2 + 1; limite ≥ 0,5.</p>'
        md = r'Resultado = 3\*5\*2 + 1; limite ≥ 0,5.'
        self.assertTrue(comparar_fidelidade(source, md, md)['texto_visivel_md_igual_fonte_apos_formato_heading_comprovado'])
        changed = md.replace('+', '-')
        self.assertFalse(comparar_fidelidade(source, md, changed)['texto_visivel_md_igual_fonte_apos_formato_heading_comprovado'])

    def test_contexto_detecta_deslocamento_de_valores(self):
        source = 'Parcela principal: 10. Parcela acessória: 20.'
        changed = 'Parcela acessória: 10. Parcela principal: 20.'
        self.assertNotEqual(contexto_numerico(source), contexto_numerico(changed))

    def test_marcador_administrativo_exige_identidade_e_paragrafo_exclusivo(self):
        row = {'urn': 'urn:lex:br:federal:decreto:1958-12-04;45027',
               'epigrafe': {'numero': '45027', 'data': '1958-12-04'}}
        source = '<p>###DEC-045027-0-000-04-12-1958@@@</p><p>Art. 1º R$ -0,5%.</p>'
        clean, proof = normalizar_marcador_administrativo(source, row)
        self.assertIsNotNone(proof)
        self.assertEqual(clean, '<p></p><p>Art. 1º R$ -0,5%.</p>')
        wrong = source.replace('04-12-1958', '04-12-1957')
        self.assertEqual(normalizar_marcador_administrativo(wrong, row), (wrong, None))
        mixed = source.replace('@@@</p>', '@@@ Conteúdo próprio.</p>')
        self.assertEqual(normalizar_marcador_administrativo(mixed, row), (mixed, None))
        late = '<p>Art. 1º R$ -0,5%.</p>'+source
        self.assertEqual(normalizar_marcador_administrativo(late, row), (late, None))

    def test_tabela_nativa_conserva_decimal_e_operador_literal(self):
        source = '<table><tr><td>3*5*2</td><td>-0,5%</td></tr></table>'
        proof = comparar_fidelidade(source, source, source)
        self.assertTrue(proof['texto_visivel_md_igual_fonte_apos_formato_heading_comprovado'])
        changed = source.replace('-0,5%', '05%')
        self.assertFalse(comparar_fidelidade(source, source, changed)['numeros_sinais_moedas_percentuais_iguais_fonte'])


if __name__ == '__main__':
    unittest.main()
