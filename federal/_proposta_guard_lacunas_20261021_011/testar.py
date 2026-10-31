"""Teste offline da proposta privada; não modifica os scripts em produção."""
import hashlib
import json
import sys
import types
import unittest
from pathlib import Path
sys.dont_write_bytecode = True
base = Path(__file__).resolve().parent
receipt = json.loads((base / 'recibo.json').read_text())
source = (base / 'integridade_anexos_decreto.py.txt').read_text()
tests = (base / 'test_integridade_anexos_decreto.py.txt').read_text()
assert hashlib.sha256(source.encode()).hexdigest() == receipt['sha_guard_candidato']
assert hashlib.sha256(tests.encode()).hexdigest() == receipt['sha_testes_candidatos']
module = types.ModuleType('integridade_anexos_decreto')
exec(compile(source, 'guard-candidato46', 'exec'), module.__dict__)
sys.modules[module.__name__] = module
test_module = types.ModuleType('test_guard_candidato46')
test_module.__file__ = str(base / 'test_integridade_anexos_decreto.py.txt')
exec(compile(tests, test_module.__file__, 'exec'), test_module.__dict__)
result = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromModule(test_module))
assert result.testsRun == 46
raise SystemExit(0 if result.wasSuccessful() else 1)
