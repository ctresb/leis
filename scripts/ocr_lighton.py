import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time

import pypdfium2 as pdfium
import torch
from transformers import AutoProcessor, Qwen3_5ForConditionalGeneration

MODELO = "lightonai/LightOnOCR-3-0.8B"


def carregar(revisao):
    modelo = Qwen3_5ForConditionalGeneration.from_pretrained(MODELO, revision=revisao, dtype=torch.bfloat16,
                                                             device_map="cuda")
    return modelo, AutoProcessor.from_pretrained(MODELO, revision=revisao)


def camada_texto(pdf, pagina):
    return subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", "-f", str(pagina), "-l", str(pagina), str(pdf), "-"],
                          capture_output=True, check=True).stdout.decode("utf-8", "replace")


@torch.inference_mode()
def transcrever(modelo, processador, imagem, max_tokens, semente=None):
    conversa = [{"role": "user", "content": [{"type": "image", "image": imagem}]}]
    entradas = processador.apply_chat_template(conversa, add_generation_prompt=True, tokenize=True, return_dict=True,
                                               return_tensors="pt", enable_thinking=False).to(modelo.device)
    if semente is None:
        amostragem = {"do_sample": False}
    else:
        torch.manual_seed(semente)
        amostragem = {"do_sample": True, "temperature": 0.2, "top_p": 0.9}
    saida = modelo.generate(**entradas, max_new_tokens=max_tokens, use_cache=True, **amostragem)
    gerados = saida[0, entradas["input_ids"].shape[1]:]
    return processador.decode(gerados, skip_special_tokens=True), len(gerados)


def refazer(modelo, processador, pdf, destino, max_tokens):
    partes, ocr, paginas, truncadas, nome, revisao, *resto = json.loads(destino.read_text(encoding="utf-8"))
    sementes = resto[0] if resto else {}
    documento = pdfium.PdfDocument(str(pdf))
    for n in list(truncadas):
        imagem = documento[n - 1].render(scale=400 / 72).to_pil().convert("RGB")
        imagem.thumbnail((2048, 2048))
        for semente in range(3):
            texto, tokens = transcrever(modelo, processador, imagem, max_tokens, semente)
            if tokens < max_tokens:
                partes[n - 1], sementes[str(n)] = texto, semente
                truncadas.remove(n)
                break
        print(f"{pdf.stem} pág {n}: " + (f"refeita com semente {sementes[str(n)]}" if n not in truncadas else "continua truncada"),
              flush=True)
    documento.close()
    destino.write_text(json.dumps([partes, ocr, paginas, truncadas, nome, revisao, sementes], ensure_ascii=False),
                       encoding="utf-8")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("pasta", type=Path)
    p.add_argument("--revisao", required=True)
    p.add_argument("--ids", nargs="*")
    p.add_argument("--max-tokens", type=int, default=4096)
    p.add_argument("--refazer-truncadas", action="store_true")
    a = p.parse_args()
    modelo, processador = carregar(a.revisao)
    pdfs = sorted(a.pasta.glob("*.pdf"), key=lambda x: int(x.stem))
    if a.ids:
        pdfs = [x for x in pdfs if x.stem in set(a.ids)]
    for i, pdf in enumerate(pdfs, 1):
        sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
        destino = a.pasta / f"{pdf.stem}.{sha[:16]}.lighton.json"
        if a.refazer_truncadas:
            if destino.exists() and json.loads(destino.read_text(encoding="utf-8"))[3]:
                refazer(modelo, processador, pdf, destino, a.max_tokens)
            continue
        if destino.exists():
            continue
        inicio = time.time()
        documento = pdfium.PdfDocument(str(pdf))
        partes, ocr, truncadas = [], False, []
        for n in range(len(documento)):
            camada = camada_texto(pdf, n + 1)
            if len(re.sub(r"\W", "", camada)) >= 300:
                partes.append(camada)
                continue
            imagem = documento[n].render(scale=400 / 72).to_pil().convert("RGB")
            imagem.thumbnail((2048, 2048))
            texto, tokens = transcrever(modelo, processador, imagem, a.max_tokens)
            if tokens >= a.max_tokens:
                truncadas.append(n + 1)
            partes.append(texto)
            ocr = True
        paginas = len(documento)
        documento.close()
        destino.write_text(json.dumps([partes, ocr, paginas, truncadas, MODELO, a.revisao], ensure_ascii=False),
                           encoding="utf-8")
        print(f"{i}/{len(pdfs)} {pdf.stem} {paginas}p {time.time() - inicio:.1f}s"
              + (f" TRUNCADA {truncadas}" if truncadas else ""), flush=True)


if __name__ == "__main__":
    sys.exit(main())
