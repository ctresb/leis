"""Replay AM55 recuperado: snapshots intactos, prova própria e HEAD fornecido.

Não acessa Git/rede nem promove candidatos. Carrega o replay congelado no mesmo
processo, sem depender da precedência de importações de um subprocesso.
"""
import argparse,gzip,hashlib,importlib.util,json,sys
from pathlib import Path
SHA=lambda b:hashlib.sha256(b).hexdigest()
def modulo(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--pacote',required=True);ap.add_argument('--head',required=True);ap.add_argument('--saida',required=True);ap.add_argument('--resumo',required=True);a=ap.parse_args()
    if Path(a.saida).exists() or Path(a.resumo).exists():raise ValueError('saída já existe; preservar execução anterior')
    package=json.loads(Path(a.pacote).read_text());root=Path(package['raiz']);public=root/'scripts/estados/snapshots/am_legisla_publicacao_20261021_001'
    for group in ('dados','codigo','fontes'):
        for p,s in package[group].items():
            if SHA((root/p).read_bytes())!=s:raise ValueError('snapshot divergente: '+p)
    # Importações normativas são resolvidas exclusivamente no snapshot congelado.
    sys.path.insert(0,str(public));control=root/package['controle'];m=json.loads(control.read_text());headinput=json.loads(Path(a.head).read_text())
    invraw=Path(headinput['inventario']).read_bytes();mapraw=Path(headinput['destinos']).read_bytes()
    if SHA(invraw)!=headinput['sha256_inventario'] or SHA(mapraw)!=headinput['sha256_destinos']:raise ValueError('snapshot HEAD diverge da entrada independente')
    inv=json.loads(invraw);maps=json.loads(mapraw)
    if inv['HEAD']!=headinput['HEAD']:raise ValueError('HEAD do inventário diverge da prova')
    helper=modulo(root/'scripts/estados/snapshots/am_legisla_HEAD_20261021_001/am_legisla_head.py','_am55_head_recuperado');headproof=helper.conferir(m['documentos'],inv,maps)
    own=modulo(root/'scripts/estados/snapshots/am_legisla_integridade_20261021_001/auditar_legisla_am_cache.py','_am55_integridade_recuperada')
    native=modulo(public/'representacao_html_legisla_am.py','_am55_campo_recuperado');from pe_fidelidade_visivel import texto_visivel_html
    proofs=[]
    for r in m['documentos']:
        raw=gzip.decompress((root/r['captura']['cache']).read_bytes())
        if SHA(raw)!=r['captura']['sha256_fonte']:raise ValueError('fonte própria diverge')
        field,_=native.extrair_campo(raw.decode('utf8'));proofs.append(dict(destino=r['destino'],sha256_fonte=SHA(raw),dispositivo_proprio=own.dispositivo_proprio(texto_visivel_html(field))))
    replay=modulo(public/'reexecutar_legisla_am.py','_am55_replay_recuperado');oldargs=sys.argv
    try:sys.argv=[str(public/'reexecutar_legisla_am.py'),'--manifesto',str(control),'--saida',a.saida];replay.main()
    finally:sys.argv=oldargs
    output=[json.loads(s) for s in Path(a.saida).read_text().splitlines()]
    if len(output)!=55 or not all(r['aceito'] for r in output):raise ValueError('replay incompleto')
    summary=dict(total=55,replay_aceitos=55,dispositivo_proprio=55,HEAD=inv['HEAD'],HEAD_ausentes=len(headproof),aliases=0,sem_promocao=True,sem_Git=True,sha256_entrada_HEAD=SHA(Path(a.head).read_bytes()),sha256_pacote=SHA(Path(a.pacote).read_bytes()),sha256_replay=SHA(Path(a.saida).read_bytes()),provas_dispositivo=proofs)
    Path(a.resumo).write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in summary.items() if k!='provas_dispositivo'}))
if __name__=='__main__':main()
