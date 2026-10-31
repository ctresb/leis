"""Fila sequencial do calendário público; aguarda um coletor ativo antes de iniciar.

    python3 -I scripts/fila_municipal.py --aguardar-pid 1234
"""
import argparse
import datetime as dt
import os
import subprocess
import sys
import time

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--aguardar-pid", type=int)
ap.add_argument("--ano-inicial", type=int, default=dt.date.today().year)
ap.add_argument("--ano-final", type=int, default=2002)
a = ap.parse_args()
if a.aguardar_pid:
    while True:
        try:
            os.kill(a.aguardar_pid, 0)
        except ProcessLookupError:
            break
        time.sleep(5)
raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
falhou = False
for ano in range(a.ano_inicial, a.ano_final - 1, -1):
    inicio = dt.date(ano, 1, 1)
    fim = min(dt.date(ano, 12, 31), dt.date.today())
    if inicio > fim:
        continue
    print(f"ANO {ano}", flush=True)
    r = subprocess.run([sys.executable, "-I", "scripts/baixar_municipal.py",
                        "--de", inicio.isoformat(), "--ate", fim.isoformat(), "--rps", "1"], cwd=raiz)
    if r.returncode:
        falhou = True
        print(f"ANO {ano}: coleta parcial (status {r.returncode}); seguindo próximo ano", flush=True)
sys.exit(1 if falhou else 0)
