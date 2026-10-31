import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parent))
from auditar_municipais_head_api_offline import analisar,vinculos


def record(**r):
    return dict(registro=r,arquivo='cache.json',sha256='a'*64,json_pointer='/results/0')


class AuditoriaOffline(unittest.TestCase):
    def test_cache_ausente_e_esfera_vazia_nao_sao_erros(self):
        meta=dict(municipio='Porto Velho',uf='RO',codigo_ibge='1100205')
        self.assertEqual(analisar(meta,[],[],[],[],{}),[])
        self.assertEqual(analisar(meta,[record(id=1,esfera_federacao='')],[],[],[],{}),[])

    def test_versao_privada_paralela_nao_contamina_pdf_publicado(self):
        norm,tas=vinculos(dict(fonte='https://sapl.example.leg.br/norma/15',fonte_texto='https://sapl.example.leg.br/media/sapl/public/normajuridica/2020/15/lei.pdf'))
        self.assertEqual(norm,('sapl.example.leg.br',15))
        self.assertEqual(tas,[])
        self.assertEqual(analisar({},[record(id=15,esfera_federacao='M')],[],[record(id=1,descricao='Projeto de Lei')],[],{}),[])

    def test_ta_realmente_usado_tem_status_e_modelo_confrontados(self):
        _,tas=vinculos(dict(fonte='https://sapl.example.leg.br/norma/15',fonte_texto='https://sapl.example.leg.br/ta/77/text'))
        self.assertEqual(tas,[('sapl.example.leg.br',77)])
        found=analisar({},[],[record(id=77,privacidade=89,tipo_ta=3)],[record(id=3,descricao='Matéria Legislativa')],[],{})
        self.assertEqual({r['regra'] for r in found},{'ta_usado_com_status_nao_publico_no_cache','modelo_do_ta_usado_diferente_norma_juridica'})

    def test_variantes_m_e_e_sao_evidenciadas_sem_declarar_invalidade(self):
        found=analisar({},[record(id=15,esfera_federacao='M'),record(id=15,esfera_federacao='E')],[],[],[],{})
        self.assertEqual(found[0]['valores_registrados'],['E','M'])
        self.assertEqual(len(found[0]['evidencias']),2)
        self.assertIn('revisão individual',found[0]['limite'])

    def test_casa_unica_divergente_e_casa_ambigua(self):
        meta=dict(municipio='Porto Velho',uf='RO',codigo_ibge='1100205')
        house=record(id=1,nome='Câmara',municipio='Boa Vista',uf='RR')
        self.assertEqual(analisar(meta,[],[],[],[house],{('RR','BOA VISTA'):'1400100'})[0]['regra'],'uf_publicada_diverge_casa_api')
        matching=record(id=2,nome='Câmara',municipio='Porto Velho',uf='RO')
        self.assertEqual(analisar(meta,[],[],[],[house,matching],{}),[])


if __name__=='__main__':
    unittest.main()
