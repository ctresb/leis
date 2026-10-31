import unittest
from auditar_constituicao_ap import projecao_markdown,intersecoes,linhas_por_intersecao,contexto_literal

class Projecao(unittest.TestCase):
    def test_pontuacao_e_offsets(self):
        body='# Título\n\n**Art. 1º** R$ -100,00; 0,5%; \\*nota\n\nCONSTITUIÇÃO DO ESTADO DO AMAPÁ CONSOLIDADA Página 10\n42 reais\nCONSTITUIÇÃO DO ESTADO DO AMAPÁ CONSOLIDADA Página 11\n'
        compact,positions,bytespos,anchors,kinds=projecao_markdown(body)
        self.assertIn('-100,00;0,5%;*nota',compact);self.assertIn('1º',compact);self.assertEqual(set(anchors),{10,11});self.assertIn('42reais',compact[slice(*anchors[11])])
        for i,pos in enumerate(positions):self.assertEqual(compact[i],body[pos]);self.assertEqual(bytespos[pos],len(body[:pos].encode()))
    def test_rodape_ao_fim_de_paragrafo(self):
        body='I - plebiscito; CONSTITUIÇÃO DO ESTADO DO AMAPÁ CONSOLIDADA Página 10\n'
        compact,p,b,a,k=projecao_markdown(body);self.assertEqual(compact[slice(*a[10])],'I-plebiscito;')
    def test_rodape_repetido_falha(self):
        footer='CONSTITUIÇÃO DO ESTADO DO AMAPÁ CONSOLIDADA Página 10\n'
        with self.assertRaisesRegex(ValueError,'ambíguo'):projecao_markdown(footer+footer)
    def test_html_ja_tachado_nao_e_reinterpretado(self):
        with self.assertRaisesRegex(ValueError,'fora do perfil'):projecao_markdown('<del>histórico</del>')

class Geometria(unittest.TestCase):
    def test_risco_meio_e_sublinhado_separados(self):
        char=dict(top=0,bottom=10,x0=0,x1=10)
        base=dict(fill=True,height=.6,width=10,x0=0,x1=10)
        self.assertEqual(intersecoes(dict(base,top=5,bottom=5.6),[char])[0][0],0)
        self.assertEqual(intersecoes(dict(base,top=9,bottom=9.6),[char]),[])
        self.assertEqual(intersecoes(dict(base,fill=False,top=5,bottom=5.6),[char]),[])
    def test_sobrescrito_no_lugar_exato(self):
        chars=[dict(text='l',top=10,bottom=22,x0=0,x1=3,size=12,matrix=(1,0,0,1,0,0)),dict(text='2',top=9.2,bottom=17.2,x0=3,x1=7,size=8,matrix=(1,0,0,1,3,4)),dict(text='x',top=25,bottom=37,x0=0,x1=6,size=12,matrix=(1,0,0,1,0,-15))]
        rows=linhas_por_intersecao(chars);self.assertEqual(len(rows),2);self.assertEqual(''.join(c['text'] for i,c in rows[0][1]),'l2')

class Contexto(unittest.TestCase):
    def row(self,n,text):return (n,[(n,dict(text=text))])
    def test_repeticao_resolvida_sem_rodape(self):
        rows=[self.row(0,'Contexto único'),self.row(1,'Legislativa;'),self.row(2,'RODAPÉ')]
        compact='OutraLegislativa;ContextoúnicoLegislativa;';mapping,found,margin=contexto_literal(rows,1,compact,(0,len(compact)),{1})
        self.assertEqual(len(found),1);self.assertEqual(margin,dict(antes=1,depois=0))
    def test_ambiguidades_contraditorias_falham(self):
        rows=[self.row(0,'Antes'),self.row(1,'X'),self.row(2,'Depois')];compact='AntesXZXDepois'
        mapping,found,margin=contexto_literal(rows,1,compact,(0,len(compact)),{1});self.assertEqual(found,[])
    def test_sinais_numericos_nao_normalizados(self):
        rows=[self.row(0,'-100,00 e 0,5%')];compact='10000e05%'
        mapping,found,margin=contexto_literal(rows,0,compact,(0,len(compact)),{0});self.assertFalse(found)
    def test_glifo_com_dois_codepoints(self):
        rows=[self.row(0,'fi')];mapping,found,margin=contexto_literal(rows,0,'fi',(0,2),{0});self.assertEqual([r[2] for r in mapping],['f','i']);self.assertEqual([r[1] for r in mapping],[0,1])
if __name__=='__main__':unittest.main()
