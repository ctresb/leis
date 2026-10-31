"""Regressões do inventário literal, sem dispensar nenhum gate de publicação."""
from pathlib import Path
import json
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from inventariar_cores_ta_privado_20261028 import inventario, sha, ROOT


class InventarioCores(unittest.TestCase):
    def test_cor_e_tachado_nao_sao_excluidos(self):
        source = '<div class="dptt" id="a"><span style="color: red !important" title="nota"><del>Redação</del> literal</span></div>'
        row = inventario(source)['ocorrencias'][0]
        self.assertEqual(row['texto_descendente'], 'Redação literal')
        self.assertEqual(row['atributos_literais']['title'], 'nota')
        self.assertEqual(row['declaracoes'][0]['propriedade'], 'color')
        self.assertTrue(row['declaracoes'][0]['important'])

    def test_borda_nao_e_confundida_com_cor_do_texto(self):
        rows = inventario('<div class="dptt" id="a"><table><tr><td style="border-color:#fff">0</td></tr></table></div>')['ocorrencias']
        self.assertEqual(rows[0]['declaracoes'][0]['propriedade'], 'border-color')
        self.assertEqual(rows[0]['texto_descendente'], '0')

    def test_historico_continua_identificado(self):
        source = '<div class="dptt desativado" id="old"><font color="red">Antes</font></div><div class="dptt" id="new"><font color="blue">Agora</font></div>'
        result = inventario(source)
        self.assertEqual(result['historicos_desativados'], ['old'])
        self.assertEqual([r['texto_descendente'] for r in result['ocorrencias']], ['Agora'])
        self.assertEqual(result['ocorrencias'][0]['atributos_cor'], {'color': 'blue'})

    def test_folha_desconhecida_fica_explicita(self):
        result = inventario('<link rel="stylesheet" href="/externo.css"><div class="dptt" id="a" style="color:var(--incerto)">Texto</div>')
        self.assertEqual(result['folhas_externas_nao_consultadas'][0]['href'], '/externo.css')
        self.assertEqual(result['ocorrencias'][0]['declaracoes'][0]['valor'], 'var(--incerto)')

    def test_caso_real_nota_vermelha_tem_fonte_confirmada(self):
        gate = ROOT / 'municipais/_indice/_recuperacao_20261027/lotes/ta-gates-0033/resultados.jsonl'
        row = next(json.loads(line) for line in gate.read_text().splitlines()
                   if json.loads(line)['host'] == 'sapl.fozdoiguacu.pr.leg.br'
                   and json.loads(line)['ta_id'] == 1933)
        raw = (ROOT / row['prova_frontend']['arquivo']).read_bytes()
        self.assertEqual(sha(raw), row['prova_frontend']['sha256'])
        result = inventario(raw.decode())
        self.assertIn('Este texto não substitui o original publicado no Diário Oficial', result['ocorrencias'][0]['texto_descendente'])
        self.assertEqual(result['ocorrencias'][0]['atributos_literais']['style'], 'color: #e03e2d;')
        self.assertEqual(len(result['folhas_externas_nao_consultadas']), 4)


if __name__ == '__main__':
    unittest.main()
