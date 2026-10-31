"""Coleta as súmulas de outros tribunais pelo BNP após terminar o coletor indicado."""
import argparse
import os
import subprocess
import sys
import time

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--aguardar-pid", type=int, required=True)
a = ap.parse_args()
while True:
    try:
        os.kill(a.aguardar_pid, 0)
    except ProcessLookupError:
        break
    time.sleep(5)
raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.exit(subprocess.call([sys.executable, "-I", "scripts/baixar_jurisprudencia.py",
                          "--somente", "bnp-outros", "--rps", "1"], cwd=raiz))
