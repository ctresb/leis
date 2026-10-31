"""Replay único: fonte/CSS/corpo integrais e dedup no snapshot HEAD independente."""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path
from am_legisla_head import conferir
SHA=lambda b:hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--manifesto',required=True);ap.add_argument('--recibo-head',required=True);ap.add_argument('--saida',required=True);a=ap.parse_args();raw=Path(a.manifesto).read_bytes();m=json.loads(raw);receipt=json.loads(Path(a.recibo_head).read_text())
    if SHA(raw)!=receipt['sha256_controle']:raise ValueError('controle mudou')
    captured={}
    for p,s in receipt['fontes_independentes_ROOT'].items():
        b=Path(p).read_bytes()
        if SHA(b)!=s:raise ValueError('fonte HEAD mudou')
        captured[Path(p).name]=json.loads(b)
    inventario=captured['am55-head-identidades-root-20261021.json'];mapa=captured['am55-head-destinos-root-20261021.json'];proof=conferir(m['documentos'],inventario,mapa)
    import reexecutar_legisla_am as replay
    subprocess.run([sys.executable,replay.__file__,'--manifesto',a.manifesto,'--saida',a.saida],check=True)
    print(json.dumps(dict(total=len(proof),HEAD=inventario['HEAD'],HEAD_ausentes=len(proof),aliases=0,namespace_SAPL_distinto_Legisla=True,sem_promocao=True)))
if __name__=='__main__':main()
