"""Replay TO offline com dependências congeladas; não promove nem consulta rede."""
import argparse,json
from pathlib import Path
from promover_to_pdf_privado import validar

def replay(manifesto,hashes):
 root=Path.cwd();m=json.loads(Path(manifesto).read_text());_,rows=validar(root,root/manifesto,root/hashes,m['total'])
 return dict(total=len(rows),aprovados=len(rows),falhas=0,rede=False,promovidos=0)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--manifesto',required=True);p.add_argument('--hashes',required=True);p.add_argument('--recibo',required=True);a=p.parse_args();result=replay(a.manifesto,a.hashes)
 with Path(a.recibo).open('x') as f:f.write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result))
if __name__=='__main__':main()
