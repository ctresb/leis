"""Transcrição conservadora da camada textual: sem exclusão de números ou repetições."""
import os
import hashlib
import re
import shutil
import subprocess
import tempfile


def formatar_camada_textual(texto):
    maior = max((len(m.group()) for m in re.finditer(r'`+', texto)), default=0)
    cerca = '`' * max(3, maior + 1)
    partes = []
    paginas = texto.split('\f')
    if paginas and not paginas[-1].strip():
        paginas.pop()
    for numero, pagina in enumerate(paginas, 1):
        partes.append(f'Página {numero} da camada textual do PDF:\n\n{cerca}text\n' + pagina +
                      ('' if pagina.endswith('\n') else '\n') + cerca)
    return ('> Transcrição da camada textual do PDF oficial com a disposição de linhas preservada. '
            'Números, repetições e paginação não foram removidos; elementos exclusivamente gráficos '
            'exigem consulta ao PDF oficial.\n\n' + '\n\n'.join(partes) + '\n')


def extrair_camada_textual(bruto):
    if not bruto.startswith(b'%PDF'):
        raise ValueError('fonte não é PDF')
    binario = shutil.which('pdftotext') or '/opt/homebrew/bin/pdftotext'
    with tempfile.TemporaryDirectory() as pasta:
        caminho = os.path.join(pasta, 'fonte.pdf')
        with open(caminho, 'wb') as arquivo:
            arquivo.write(bruto)
        processo = subprocess.run([binario, '-q', '-layout', '-enc', 'UTF-8', caminho, '-'],
                                  capture_output=True, timeout=120)
        if processo.returncode:
            raise ValueError('pdftotext falhou: ' + processo.stderr.decode('utf8', 'replace')[:300])
    texto = processo.stdout.decode('utf8', 'strict')
    if len(re.sub(r'\W', '', texto)) < 80:
        raise ValueError('camada textual insuficiente; exige avaliação visual/OCR')
    return formatar_camada_textual(texto), texto


def validar_inventario_imagens(inventario, dimensoes_interface=()):
    """Só tolera dimensões que o chamador comprovou como recurso de interface."""
    permitidas = set(dimensoes_interface)
    for linha in inventario.splitlines()[2:]:
        colunas = linha.split()
        if len(colunas) > 5 and colunas[0].isdigit():
            dimensoes = (int(colunas[3]), int(colunas[4]))
            if dimensoes not in permitidas:
                raise ValueError('PDF contém imagem que exige conferência visual: ' + linha)


def conferir_visuais_pdf(bruto, dimensoes_interface=(), hashes_interface=()):
    binario = shutil.which('pdfimages') or '/opt/homebrew/bin/pdfimages'
    with tempfile.TemporaryDirectory() as pasta:
        caminho = os.path.join(pasta, 'fonte.pdf')
        with open(caminho, 'wb') as arquivo:
            arquivo.write(bruto)
        processo = subprocess.run([binario, '-list', caminho], capture_output=True, timeout=120)
        if processo.returncode:
            raise ValueError('inventário visual do PDF inconclusivo')
        inventario = processo.stdout.decode('utf8', 'strict')
        validar_inventario_imagens(inventario, dimensoes_interface)
        prefixo = os.path.join(pasta, 'imagem')
        extracao = subprocess.run([binario, '-png', caminho, prefixo], capture_output=True, timeout=120)
        if extracao.returncode:
            raise ValueError('extração dos recursos visuais do PDF inconclusiva')
        for nome in os.listdir(pasta):
            if not nome.startswith('imagem-'):
                continue
            with open(os.path.join(pasta, nome), 'rb') as arquivo:
                sha = hashlib.sha256(arquivo.read()).hexdigest()
            if sha not in hashes_interface:
                raise ValueError('PDF contém imagem sem hash visual comprovado: ' + sha)
    return inventario
