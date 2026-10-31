"""Reconstrói páginas de diário por coordenadas: coluna esquerda, depois direita.

Não usa a ordem dos objetos/fluxos internos do PDF, que pode misturar atos.
Requer pdftotext e pypdf no Python local (inspeção vetorial em subprocesso).
"""
import argparse
import fcntl
import json
import sys
import hashlib
import datetime as dt
from pathlib import Path
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET


def linhas_palavras(palavras):
    linhas = []
    for w in sorted(palavras, key=lambda w: (w[1], w[0])):
        if linhas and abs(linhas[-1][0] - w[1]) < 1.5:
            linhas[-1][1].append(w)
        else:
            linhas.append([w[1], [w]])
    textos = []
    for _, words in linhas:
        words.sort(key=lambda w: w[0])
        texto = ""
        anterior = None
        for w in words:
            if anterior:
                distancia = w[0] - anterior[2]
                espacos = max(1, min(24, round(distancia / max((w[3] - w[1]) * .3, 1))))
                texto += " " * espacos
            texto += w[4]
            anterior = w
        textos.append(texto.strip())
    return "\n".join(textos)


VERSAO = "geometria-colunas-v2"
SHA_EXTRATOR = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


# Provas locais vinculadas aos bytes do PDF; qualquer alteração invalida o cache.
LAYOUTS_VERIFICADOS = {('6e4f6233bbb4f2b53371a3ed1a89e9c1dc9e6ecbcd08adc4979f18a6d3dd3c58', 246): {'dimensoes': [841.92, 595.32],
                                                                             'faixas': [[36.12, 44.9]],
                                                                             'render_sha256': '9bd68099b05c39b7fcfd63c02bf4864b53c310a3fb57c3b32551611d1a59c616',
                                                                             'render': 'municipais/_referencias/layouts-verificados/arom4340-p246.png',
                                                                             'prova': 'Última linha de tabela '
                                                                                      'continuada;12 bordas '
                                                                                      'verticais36,12–43,92pt, '
                                                                                      'travessa inferior44,4pt; '
                                                                                      'revisão visual do PDF.'},
 ('9f6079de7536489aff09779be03e078910038d16cba16d82f502be97f2aa02c1', 151): {'dimensoes': [595.32, 841.92],
                                                                             'faixas': [[34.2, 42.9]],
                                                                             'render_sha256': '4bd6984e990a953256e9cc9bf3b87c1b78aacbbb33e51946bbd1b629d049f939',
                                                                             'render': 'municipais/_referencias/layouts-verificados/aam4103-p151.png',
                                                                             'prova': 'Última linha de tabela '
                                                                                      'continuada;6 bordas '
                                                                                      'verticais34,2–41,88pt, travessa '
                                                                                      'inferior42,4pt; revisão visual '
                                                                                      'do PDF.'},
 ('6e4f6233bbb4f2b53371a3ed1a89e9c1dc9e6ecbcd08adc4979f18a6d3dd3c58', 248): {'dimensoes': [841.92, 595.32],
                                                                             'faixas': [[548.7, 567.3]],
                                                                             'render_sha256': 'fd0052a5ff060d4fdb4a04f636c9b32c2322a7cbd2b6f5a88600766adc030f94',
                                                                             'render': 'municipais/_referencias/layouts-verificados/arom4340-p248.png',
                                                                             'prova': 'Cabeçalho tabular com células '
                                                                                      'mescladas no '
                                                                                      'rodapé;bordas550,056–566,28pt,travessas548,7/566,8pt;revisão '
                                                                                      'visual do PDF.'},
 ('9f6079de7536489aff09779be03e078910038d16cba16d82f502be97f2aa02c1', 159): {'dimensoes': [595.32, 841.92],
                                                                             'faixas': [[34.2, 42.9]],
                                                                             'render_sha256': 'f292def95a8d7c773bf098dcc7dad495c6af38d86f44c42cf12431b12d0b4d7c',
                                                                             'render': 'municipais/_referencias/layouts-verificados/aam4103-p159.png',
                                                                             'prova': 'Última linha de tabela '
                                                                                      'continuada;6 bordas '
                                                                                      'verticais34,2–41,88pt,travessa '
                                                                                      'inferior42,4pt;revisão visual '
                                                                                      'do PDF.'},
 ('9f6079de7536489aff09779be03e078910038d16cba16d82f502be97f2aa02c1', 166): {'dimensoes': [595.32, 841.92],
                                                                             'faixas': [[34.2, 42.9]],
                                                                             'render_sha256': 'af0e723f61feafc17024212824ad5463af47d6127277aa1543af79f5bbba731a',
                                                                             'render': 'municipais/_referencias/layouts-verificados/aam4103-p166.png',
                                                                             'prova': 'Última linha de tabela '
                                                                                      'continuada;6 bordas '
                                                                                      'verticais34,2–41,88pt,travessa '
                                                                                      'inferior42,4pt;revisão visual '
                                                                                      'do PDF.'}}


def layout_vetorial(pdf):
    from pypdf import PdfReader
    saida = []
    sha_pdf = hashlib.sha256(Path(pdf).read_bytes()).hexdigest()
    for numero,pagina in enumerate(PdfReader(pdf).pages,1):
        largura, altura = float(pagina.mediabox.width), float(pagina.mediabox.height)
        rotacao = pagina.rotation % 360
        if rotacao != 0:
            raise RuntimeError(f"página {numero}: rotação de página não zero; layout exige revisão antes da extração")
        matrix = (1, 0, 0, 1, 0, 0)
        pilha, formas, ponto, retangulos, horizontais = [], [], None, [], []
        def transformar(x, y):
            a,b,c,d,e,f = matrix
            x,y = a*x+c*y+e, b*x+d*y+f
            if rotacao == 90:
                return y,x
            if rotacao == 180:
                return largura-x,y
            if rotacao == 270:
                return altura-y,largura-x
            return x,altura-y
        conteudo = pagina.get_contents()
        for args, op in (conteudo.operations if conteudo is not None else []):
            if op == b"q":
                pilha.append(matrix)
            elif op == b"Q":
                matrix = pilha.pop()
            elif op == b"cm":
                a,b,c,d,e,f = matrix
                aa,bb,cc,dd,ee,ff = map(float,args)
                matrix = (a*aa+c*bb,b*aa+d*bb,a*cc+c*dd,b*cc+d*dd,a*ee+c*ff+e,b*ee+d*ff+f)
            elif op == b"re":
                x,y,w,h = map(float,args)
                pts = [transformar(x,y),transformar(x+w,y),transformar(x,y+h),transformar(x+w,y+h)]
                formas.append((min(z[0] for z in pts),min(z[1] for z in pts),max(z[0] for z in pts),max(z[1] for z in pts)))
            elif op == b"m":
                ponto = transformar(*map(float,args))
            elif op == b"l" and ponto:
                novo = transformar(*map(float,args))
                formas.append((min(ponto[0],novo[0]),min(ponto[1],novo[1]),max(ponto[0],novo[0]),max(ponto[1],novo[1])))
                ponto = novo
            elif op in (b"f",b"f*",b"S",b"s",b"B",b"B*",b"b",b"b*"):
                retangulos.extend(formas)
                formas,ponto = [],None
            elif op == b"n":
                formas,ponto = [],None
        if rotacao in (90,270):
            largura,altura = altura,largura
        meio = largura/2
        zonas = [(y1,y2) for x1,y1,x2,y2 in retangulos if x2-x1 < 2 and y2-y1 > 35 and abs((x1+x2)/2-meio) < 2]
        hs = sorted((round((y1+y2)/2,1),x1,x2) for x1,y1,x2,y2 in retangulos if y2-y1 < 2 and x2-x1 > 4 and 0 <= y1 <= altura)
        linhas_h = []
        for y,x1,x2 in hs:
            if linhas_h and abs(linhas_h[-1][0]-y) < 1.5:
                linhas_h[-1][1].append((x1,x2))
            else:
                linhas_h.append([y,[(x1,x2)]])
        cruzadas = []
        barras = []
        for y, segmentos in linhas_h:
            unidos = []
            for x1,x2 in sorted(segmentos):
                if unidos and x1 <= unidos[-1][1]+2:
                    unidos[-1][1] = max(unidos[-1][1],x2)
                else:
                    unidos.append([x1,x2])
            for x1,x2 in unidos:
                if x1 < meio-10 and x2 > meio+10:
                    if 35 < y < altura-35:
                        cruzadas.append(y)
                    barras.append((y,x1,x2))
        grupos = []
        for y in cruzadas:
            if grupos and y-grupos[-1][-1] < 80:
                grupos[-1].append(y)
            else:
                grupos.append([y])
        tabelas = [(g[0]-1,g[-1]+1) for g in grupos if len(g)>=3]
        verticais = {}
        for x1,y1,x2,y2 in retangulos:
            if x2-x1 < 2 and y2-y1 > 2:
                verticais.setdefault(round((x1+x2)/2,1),[]).append((y1,y2))
        bordas = []
        for x, trechos in verticais.items():
            unidos = []
            for a,b in sorted(trechos):
                if unidos and a <= unidos[-1][1]+2:
                    unidos[-1][1]=max(unidos[-1][1],b)
                else:
                    unidos.append([a,b])
            bordas.extend((x,a,b) for a,b in unidos)
        grades = []
        for xe,ae,be in bordas:
            if xe >= meio-10:
                continue
            for xd,ad,bd in bordas:
                a,b=max(ae,ad),min(be,bd)
                if xd <= meio+10 or b-a < 35:
                    continue
                internas=[]
                for x in sorted({x for x,y1,y2 in bordas if xe+4 < x < xd-4 and y1 <= a+2 and y2 >= b-2}):
                    if not internas or x-internas[-1]>2:
                        internas.append(x)
                travessas=[y for y,x1,x2 in barras if a-2 <= y <= b+2 and abs(x1-xe)<2 and abs(x2-xd)<2]
                if len(internas)>=1 and len(travessas)>=3:
                    grades.append((a,b))
        # Células altas: bordas externas podem continuar além da grade interna.
        for xe,ae,be in bordas:
            if xe >= meio-10:
                continue
            for xd,ad,bd in bordas:
                if xd <= meio+10:
                    continue
                for xi,ai,bi in bordas:
                    a,b=max(ae,ad,ai),min(be,bd,bi)
                    if not xe+4 < xi < xd-4 or b-a < 35:
                        continue
                    internas=[]
                    for x in sorted({x for x,y1,y2 in bordas if xe+4 < x < xd-4 and y1 <= a+2 and y2 >= b-2}):
                        if not internas or x-internas[-1]>2:
                            internas.append(x)
                    travessas={round(y,1) for y,x1,x2 in barras if a-2 <= y <= b+2 and abs(x1-xe)<2 and abs(x2-xd)<2}
                    if len(internas)>=2 and len(travessas)>=2:
                        grades.append((min(travessas)-1,max(travessas)+1))
        linhas_grade=[]
        curtas=[((x1+x2)/2,y1,y2) for x1,y1,x2,y2 in retangulos if x2-x1 < 2 and y2-y1 > 2]
        for xe,ae,be in curtas:
            if xe >= meio-10:
                continue
            for xd,ad,bd in curtas:
                a,b=max(ae,ad),min(be,bd)
                if xd <= meio+10 or not 4 <= b-a <= 35:
                    continue
                internas=[]
                for x in sorted({x for x,y1,y2 in curtas if xe+4 < x < xd-4 and y1 <= a+2 and y2 >= b-2}):
                    if not internas or x-internas[-1]>2:
                        internas.append(x)
                travessas={round(y,1) for y,x1,x2 in barras if a-2 <= y <= b+2 and abs(x1-xe)<2 and abs(x2-xd)<2}
                if len(internas)>=1 and len(travessas)>=2:
                    grades.append((a,b))
                    linhas_grade.append((xe,xd,a,b,internas))
        # Continuação no topo: a linha seguinte precisa comprovar a mesma grade.
        for xe,ae,be in curtas:
            for xd,ad,bd in curtas:
                a,b=max(ae,ad),min(be,bd)
                if not (xe < meio-10 and xd > meio+10 and 4 <= b-a <= 35 and a <= 60):
                    continue
                internas={round(x,1) for x,y1,y2 in curtas if xe+4 < x < xd-4 and y1 <= a+2 and y2 >= b-2}
                base=any(abs(y-b)<2 and abs(x1-xe)<2 and abs(x2-xd)<2 for y,x1,x2 in barras)
                proxima=any(abs(le-xe)<2 and abs(ld-xd)<2 and abs(la-b)<2
                            and len({x for x in internas if any(abs(x-i)<2 for i in li)})>=1
                            for le,ld,la,lb,li in linhas_grade)
                if base and proxima:
                    grades.append((a,b))
        tabelas.extend(grades)
        prova = LAYOUTS_VERIFICADOS.get((sha_pdf,numero))
        if prova:
            if any(abs(a-b)>.5 for a,b in zip(prova["dimensoes"],[largura,altura])):
                raise RuntimeError(f"página {numero}: dimensões divergem da prova local verificada")
            tabelas.extend(prova["faixas"])
        saida.append({"largura":largura,"altura":altura,"reguas_colunas":zonas,"tabelas_largura_total":tabelas,"grades_largura_total":grades,"prova_layout_verificado":prova})
    return saida


def texto_da_pagina(pagina, layout):
    largura, altura = float(pagina.attrib["width"]), float(pagina.attrib["height"])
    if abs(largura-layout["largura"]) > .5 or abs(altura-layout["altura"]) > .5:
        raise RuntimeError("dimensões bbox e vetoriais divergentes; coordenadas não comparáveis")
    meio = largura / 2
    ns = "{http://www.w3.org/1999/xhtml}"
    linhas = []
    for linha in pagina.iter(ns + "line"):
        palavras = [(float(w.attrib["xMin"]), float(w.attrib["yMin"]),
                     float(w.attrib["xMax"]), float(w.attrib["yMax"]), "".join(w.itertext()))
                    for w in linha.iter(ns + "word")]
        if not palavras:
            continue
        texto = " ".join(w[4] for w in palavras)
        y = min(w[1] for w in palavras)
        if y < 60 and ("Diário Oficial" in texto or re.match(r"^ANO [IVX]+", texto)):
            continue
        if y > altura - 40 and ("diariomunicipal.com.br" in texto or re.fullmatch(r"\d+", texto)):
            continue
        linhas.append(palavras)
    palavras = [w for l in linhas for w in l]
    zonas = layout["reguas_colunas"]
    def gap_central(linha):
        ordenadas=sorted(linha,key=lambda w:w[0])
        return any(largura*.25 <= (a[2]+b[0])/2 <= largura*.75 and b[0]-a[2] > 12
                   for a,b in zip(ordenadas,ordenadas[1:]))
    largas = [(min(w[1] for w in l),max(w[3] for w in l)) for l in linhas
              if min(w[0] for w in l) < meio-10 and max(w[2] for w in l) > meio+10
              and not gap_central(l)]
    inteiras = layout["tabelas_largura_total"] + largas
    limites = sorted({0,altura,*[y for z in zonas+inteiras for y in z]})
    for inicio,fim in zip(limites,limites[1:]):
        centro=(inicio+fim)/2
        if any(a<=centro<=b for a,b in zonas+inteiras):
            continue
        locais=[l for l in linhas if inicio <= sum(w[1]+w[3] for w in l)/(2*len(l)) < fim]
        esquerda=sum(max(w[2] for w in l)<meio+5 or gap_central(l) for l in locais)
        direita=sum(min(w[0] for w in l)>meio-5 or gap_central(l) for l in locais)
        origens_duplas=any(
            abs(min(w[0] for w in a)-min(w[0] for w in b)) > largura*.15
            and max(min(w[1] for w in a),min(w[1] for w in b))
                <= min(max(w[3] for w in a),max(w[3] for w in b))+1
            for i,a in enumerate(locais) for b in locais[i+1:])
        if any(gap_central(l) for l in locais) or origens_duplas:
            raise RuntimeError("faixa com duas colunas sem régua divisória ou prova local de largura total")
    if not zonas:
        return linhas_palavras(palavras), {"colunas":1, **layout}
    cortes = sorted({0,altura,*[y for z in zonas+inteiras for y in z]})
    bandas = []
    for inicio,fim in zip(cortes,cortes[1:]):
        y = (inicio+fim)/2
        colunas = 2 if any(a<=y<=b for a,b in zonas) and not any(a<=y<=b for a,b in inteiras) else 1
        if bandas and bandas[-1][2]==colunas:
            bandas[-1][1]=fim
        else:
            bandas.append([inicio,fim,colunas])
    partes = []
    for inicio,fim,colunas in bandas:
        words = [w for w in palavras if inicio <= (w[1]+w[3])/2 < fim]
        if colunas==2:
            partes.append(linhas_palavras([w for w in words if (w[0]+w[2])/2<meio]))
            partes.append(linhas_palavras([w for w in words if (w[0]+w[2])/2>=meio]))
        else:
            partes.append(linhas_palavras(words))
    return "\n".join(p for p in partes if p), {"colunas":2,"bandas":bandas, **layout}


def texto_colunas(pdf, paginas=None, metadados=None):
    try:
        bruto=subprocess.check_output([sys.executable, __file__, "--layout-json", str(pdf)],stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as erro:
        motivo=erro.stderr.decode("utf-8",errors="replace").strip().splitlines()
        raise RuntimeError(motivo[-1] if motivo else "inspeção vetorial recusada") from erro
    layout = json.loads(bruto)
    with tempfile.TemporaryDirectory() as pasta:
        xml = Path(pasta) / "texto.html"
        subprocess.run(["pdftotext", "-bbox-layout", "-enc", "UTF-8", str(pdf), str(xml)],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        textos = []
        numero = 0
        for _, elemento in ET.iterparse(xml, events=("end",)):
            if elemento.tag.endswith("}page"):
                numero += 1
                if paginas is None or numero in paginas:
                    try:
                        texto, dados = texto_da_pagina(elemento,layout[numero-1])
                    except RuntimeError as e:
                        raise RuntimeError(f"página {numero}: {e}") from e
                    textos.append(texto)
                    if metadados is not None:
                        metadados.append({"pagina":numero,**dados})
                elemento.clear()
        if not textos:
            raise RuntimeError("PDF sem páginas textuais reconhecidas")
        return "\n\f\n".join(textos) + "\n"


def caminhos_cache(pdf):
    pdf = Path(pdf)
    base=str(pdf)+"."+VERSAO+"."+SHA_EXTRATOR[:16]
    return Path(base+".txt"), Path(base+".json")


def texto_colunas_cache(pdf):
    pdf = Path(pdf)
    txt, meta = caminhos_cache(pdf)
    with Path(str(meta)+".lock").open("a") as trava:
        fcntl.flock(trava,fcntl.LOCK_EX)
        digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if txt.exists() and meta.exists():
            dados = json.loads(meta.read_text())
            bruto = txt.read_bytes()
            if (dados.get("extrator")==VERSAO and dados.get("sha256_extrator")==SHA_EXTRATOR and dados.get("sha256_pdf")==digest and
                    dados.get("sha256_texto")==hashlib.sha256(bruto).hexdigest()):
                return bruto.decode("utf-8")
        paginas = []
        texto = texto_colunas(pdf, metadados=paginas)
        dados = {"extrator":VERSAO,"sha256_extrator":SHA_EXTRATOR,"pdf":str(pdf),"sha256_pdf":digest,
                 "sha256_texto":hashlib.sha256(texto.encode()).hexdigest(),
                 "extraido_em":dt.datetime.now().isoformat(),"paginas":paginas}
        for destino,conteudo in [(txt,texto),(meta,json.dumps(dados,ensure_ascii=False,indent=2))]:
            tmp = Path(str(destino)+".tmp")
            tmp.write_text(conteudo,encoding="utf-8")
            tmp.replace(destino)
        return texto


if __name__ == "__main__":
    if len(sys.argv)==3 and sys.argv[1]=="--layout-json":
        print(json.dumps(layout_vetorial(sys.argv[2])))
        raise SystemExit(0)
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("saida", type=Path)
    ap.add_argument("--paginas", help="números de páginas separados por vírgula")
    a = ap.parse_args()
    paginas = {int(x) for x in a.paginas.split(",")} if a.paginas else None
    a.saida.write_text(texto_colunas(a.pdf, paginas), encoding="utf-8")
