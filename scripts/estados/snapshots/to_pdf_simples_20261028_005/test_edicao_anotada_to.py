import unittest,hashlib,json
from edicao_anotada_to import conferir_anotacoes
from metadados_to_pdf import criar,verificar,VERSAO_ANOTADA

class EdicaoAnotada(unittest.TestCase):
    def test_notas_parenteses_e_asterisco(self):
        text='LEI Nº 1\n(Revogada pela Lei nº 2.)\n *Redação determinada pela Lei 3.\n'
        notes=conferir_anotacoes(text)
        self.assertEqual(len(notes),2);self.assertEqual(notes[0]['trecho_literal'],'(Revogada pela Lei nº 2.)');self.assertEqual(notes[1]['linha_inicial'],3)
    def test_declaracao_judicial_nao_e_revogacao(self):
        self.assertEqual(len(conferir_anotacoes('*Declarada Inconstitucional na ADI nº 1.\n')),1)
    def test_dispositivo_nao_vira_nota(self):
        with self.assertRaisesRegex(ValueError,'dispositivo/citação'):conferir_anotacoes('Art. 1º Fica revogada pela presente Lei a norma anterior.\n')
    def test_citacao_nao_vira_nota(self):
        with self.assertRaises(ValueError):conferir_anotacoes('Considerando a redação dada pela Lei 2, aplica-se...\n')
    def test_texto_sem_nota(self):self.assertEqual(conferir_anotacoes('Art. 1º A Lei 2 passa a vigorar com a seguinte redação:\n'),[])
    def test_corpo_e_status_preservados(self):
        body='```text\n(Revogada pela Lei nº 2.)\nArt. 1º R$ -100,00 e 0,5%.\n```\n'
        row=dict(capturado_em='2026-10-28T12:00:00-03:00',url='https://www.al.to.leg.br/arquivo/999',url_final='https://www.al.to.leg.br/arquivos/999.pdf',sha256_fonte='a'*64,item=dict(id_ALETO='999'))
        q=dict(sha256_corpo=hashlib.sha256(body.encode()).hexdigest(),epigrafe='LEI Nº 1, DE 1 DE JANEIRO DE 2020',tipo='Lei Ordinária',numero='1',data='2020-01-01',anotacoes_editoriais=conferir_anotacoes('(Revogada pela Lei nº 2.)\n'))
        blob=criar(row,q,body).decode();h,actual=blob[4:].split('\n---\n',1);meta=dict((k,json.loads(v)) for k,v in (l.split(': ',1) for l in h.splitlines()))
        self.assertEqual(actual,'# '+q['epigrafe']+'\n\n'+body);self.assertEqual(meta['versao_texto'],VERSAO_ANOTADA);self.assertIsNone(meta['revogada']);self.assertIsNone(meta['situacao']);self.assertTrue(verificar(meta,row))
        meta['revogada']=True
        with self.assertRaisesRegex(ValueError,'não autoriza inferir'):verificar(meta,row)

if __name__=='__main__':unittest.main()
