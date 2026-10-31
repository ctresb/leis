import ast,gzip,hashlib,json,unittest
from pathlib import Path
import verificar_motores as m
class Portable(unittest.TestCase):
    def test_AST_comparadores_iguais_antecessor003(self):
        base=Path(__file__).parent;expected=json.loads((base/'comparador-AST-antecessor003.json').read_text());funcs={n.name:n for n in ast.parse((base/'verificar_motores.py').read_text()).body if isinstance(n,ast.FunctionDef)};sha=lambda n:hashlib.sha256(ast.dump(n,include_attributes=False).encode()).hexdigest()
        for name in ['percorrer','analisar']:self.assertEqual(sha(funcs[name]),expected[name])
        fn=funcs['comparar'];start=next(i for i,n in enumerate(fn.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='expected' for t in n.targets));end=next(i for i,n in enumerate(fn.body) if isinstance(n,ast.For) and isinstance(n.target,ast.Tuple) and isinstance(n.target.elts[0],ast.Name) and n.target.elts[0].id=='engine');self.assertEqual(sha(ast.Module(body=fn.body[start:end+1],type_ignores=[])),expected['bloco_comparador'])
    def test_arquivo_local_SHA_fixo(self):self.assertEqual(hashlib.sha256(gzip.decompress(m.MARKED.read_bytes())).hexdigest(),m.MARKED_SHA);self.assertEqual(m.NODE,'node')
    def test_negrito_link_lista_numeros_e_utf8(self):
        old='**ação** atual\n\n- [nota](https://example.org)\n- R$ -100,00; 0,5%\n';new='<del>**ação**</del> atual\n\n- [nota](https://example.org)\n- R$ -100,00; 0,5%\n';self.assertEqual(len(m.comparar(old,new,list(enumerate('ação')))['combinacoes']),4)
    def test_mesma_palavra_noutra_posicao_falha(self):
        with self.assertRaisesRegex(ValueError,'posição/caractere'):m.comparar('igual igual\n','igual <del>igual</del>\n',list(enumerate('igual')))
    def test_ancestralidade_negrito_nao_afrouxada(self):
        with self.assertRaisesRegex(ValueError,'negrito/link/lista'):m.comparar('**antigo** atual\n','<del>antigo</del> atual\n',list(enumerate('antigo')))
    def test_stream_unicode_grande(self):
        old=('público § 1º ação; '*8000)+'final\n';start=sum(not c.isspace() for c in old[:-6]);new=old.replace('final','<del>final</del>');self.assertEqual(len(m.comparar(old,new,[(start+i,c) for i,c in enumerate('final')])['combinacoes']),4)
if __name__=='__main__':unittest.main()
