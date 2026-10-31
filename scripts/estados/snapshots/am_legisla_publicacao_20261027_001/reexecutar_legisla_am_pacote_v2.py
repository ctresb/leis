"""Replay de pacote Legisla.AM congelado + inventário HEAD independente.

Somente leitura dos candidatos/canônicos; escreve apenas duas saídas novas.
"""
import argparse,hashlib,importlib.metadata,importlib.util,json,subprocess,sys
from pathlib import Path
SHA=lambda b:hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--recibo',required=True);ap.add_argument('--head',required=True);ap.add_argument('--saida',required=True);ap.add_argument('--resumo',required=True);a=ap.parse_args()
    if Path(a.saida).exists() or Path(a.resumo).exists():raise ValueError('saída existente deve ser preservada')
    receipt=json.loads(Path(a.recibo).read_text());control=Path(receipt['controle']);raw=control.read_bytes()
    if SHA(raw)!=receipt['sha256_controle']:raise ValueError('controle alterado')
    for name,expected in receipt['runtime'].items():
        if importlib.metadata.version(name)!=expected:raise ValueError('versão QA divergente: '+name)
    modules={}
    for c in receipt['codigo']:
        if SHA(Path(c['congelado']).read_bytes())!=c['sha256']:raise ValueError('código congelado alterado')
        modules[Path(c['congelado']).name]=c['congelado']
    for p,s in receipt['fontes_congeladas'].items():
        if SHA(Path(p).read_bytes())!=s:raise ValueError('fonte congelada alterada: '+p)
    m=json.loads(raw);head=json.loads(Path(a.head).read_text());invraw=Path(head['inventario']).read_bytes();mapraw=Path(head['destinos']).read_bytes()
    if SHA(invraw)!=head['sha256_inventario'] or SHA(mapraw)!=head['sha256_destinos']:raise ValueError('fonte HEAD alterada')
    inv=json.loads(invraw)
    if inv['HEAD']!=head['HEAD']:raise ValueError('HEAD declarado diverge do inventário')
    spec=importlib.util.spec_from_file_location('_legisla_head_frozen',modules['am_legisla_head.py']);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);proof=helper.conferir(m['documentos'],inv,json.loads(mapraw))
    # O próprio diretório do script contém todos os módulos normativos congelados.
    subprocess.run([sys.executable,modules['reexecutar_legisla_am.py'],'--manifesto',str(control),'--saida',a.saida],check=True)
    result=[json.loads(s) for s in Path(a.saida).read_text().splitlines()]
    if len(result)!=len(proof) or not all(r['aceito'] and r['QA']['dispositivo_proprio'] for r in result):raise ValueError('replay/Art.1º próprio incompleto')
    summary=dict(total=len(proof),aceitos=len(result),dispositivo_proprio=len(result),HEAD=head['HEAD'],HEAD_ausentes=len(proof),aliases=0,namespace_SAPL_distinto_Legisla=True,sem_promocao=True,sha256_controle=SHA(raw),sha256_entrada_HEAD=SHA(Path(a.head).read_bytes()),sha256_replay=SHA(Path(a.saida).read_bytes()))
    Path(a.resumo).write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary))
if __name__=='__main__':main()
