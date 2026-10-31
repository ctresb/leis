import unittest,tempfile
from pathlib import Path
from promover_legis_ac_privado import metadata,identidade,id_oficial,conferir_dedup,publicar_sem_substituir

def row(path='estaduais/AC/leis-ordinarias/2018/l-8494-A-2018-id11810.md',id='11810',n='8494-A',url='https://legis.ac.gov.br/Arquivo/L8494A.html'):
 return dict(path=path,meta=dict(numero=n,data='2018-12-28',fonte='https://legis.ac.gov.br/detalhar/'+id,arquivo=url))
class PromocaoTest(unittest.TestCase):
 def test_alias_id_slug_diferente(self):
  with self.assertRaisesRegex(ValueError,'HEAD'):conferir_dedup([row()],[row(path='estaduais/AC/leis-ordinarias/2018/outro.md')])
 def test_id_namespace_diferente_nao_equivale(self):
  self.assertNotEqual(id_oficial(dict(fonte='https://sapl.al.ac.leg.br/norma/11810')),id_oficial(dict(fonte='https://legis.ac.gov.br/detalhar/11810')))
 def test_sufixo_e_identidade_distinta(self):
  self.assertNotEqual(identidade(row()['path'],row()['meta']),identidade(row(n='8494')['path'],row(n='8494')['meta']))
 def test_url_http_https_e_alias(self):
  old=row();new=row(id='12000',n='8495',url='http://legis.ac.gov.br/Arquivo/L8494A.html')
  with self.assertRaisesRegex(ValueError,'HEAD'):conferir_dedup([old],[new])
 def test_alias_identidade_id_diferente(self):
  with self.assertRaisesRegex(ValueError,'HEAD'):conferir_dedup([row()],[row(id='12000',url='https://legis.ac.gov.br/Arquivo/outro.html')])
 def test_colisao_interna(self):
  with self.assertRaisesRegex(ValueError,'interna'):conferir_dedup([],[row(),row()])
 def test_constituicao_sem_numero_nao_impede_dedup_lei(self):
  conferir_dedup([dict(path='estaduais/AC/constituicao/1989/constituicao.md',meta=dict(data='1989-10-03'))],[row()])
 def test_mesmo_numero_tipos_distintos_nao_fundir(self):
  new=row(path='estaduais/AC/leis-complementares/2018/lc-8494-A.md',id='12000',url='https://legis.ac.gov.br/Arquivo/outro.html')
  conferir_dedup([row()],[new])
 def test_padding_numerico_e_alias(self):
  with self.assertRaisesRegex(ValueError,'HEAD'):conferir_dedup([row()],[row(id='12000',n='08494-A',url='https://legis.ac.gov.br/Arquivo/outro.html')])
 def test_metadata_sha256_reconhecido(self):
  m,b=metadata(b'---\nsha256_texto: "abc"\n---\nT');self.assertEqual(m['sha256_texto'],'abc')
 def test_data_head_ausente_retem_mesmo_numero_todos_anos(self):
  old=row();old['meta']['data']=''
  with self.assertRaisesRegex(ValueError,'HEAD'):conferir_dedup([old],[row(id='12000',url='https://legis.ac.gov.br/Arquivo/outro.html')])
 def test_data_head_ausente_nao_inventa_data(self):
  old=row();old['meta']['data']=''
  conferir_dedup([old],[row(path='estaduais/AC/leis-ordinarias/2018/outro.md',n='8495',id='12000',url='https://legis.ac.gov.br/Arquivo/outro.html')]);self.assertEqual(old['meta']['data'],'')
 def test_metadata_nao_altera_body(self):
  m,b=metadata(b'---\nnumero: "8494-A"\ndata: 2018-12-28\nrevogada: null\n---\n# T\n\nR$ -100 0,5\n')
  self.assertEqual(m['numero'],'8494-A');self.assertEqual(m['data'],'2018-12-28');self.assertEqual(b,'# T\n\nR$ -100 0,5\n')
 def test_metadata_repetida_falha(self):
  with self.assertRaisesRegex(ValueError,'repetido'):metadata(b'---\nnumero: "1"\nnumero: "2"\n---\nT')
 def test_publicacao_atomica_nunca_substitui(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'ato.md';publicar_sem_substituir(p,b'original')
   with self.assertRaises(FileExistsError):publicar_sem_substituir(p,b'outro')
   self.assertEqual(p.read_bytes(),b'original');self.assertEqual(len(list(Path(d).iterdir())),1)
if __name__=='__main__':unittest.main()
