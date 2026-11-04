"""Fallback Linux de DOC/DOCX não altera a rota do textutil e não inventa texto."""
import io
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

from comum import extrair_texto, texto_office_sem_textutil

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def docx_bytes(texto):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("word/document.xml",
                   f'<w:document xmlns:w="{W}"><w:body>'
                   f'<w:p><w:r><w:t>{texto}</w:t></w:r></w:p>'
                   f"</w:body></w:document>")
    return buf.getvalue()


class OfficeLinuxTest(unittest.TestCase):
    def test_docx_xml_preserva_paragrafo(self):
        bruto = docx_bytes("Art. 1º Texto oficial.")
        self.assertEqual(texto_office_sem_textutil(bruto, "a.docx", ".docx").strip(),
                         "Art. 1º Texto oficial.")

    def test_zip_sem_document_xml_nao_inventa(self):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as z:
            z.writestr("readme.txt", "nada")
        self.assertEqual(texto_office_sem_textutil(buf.getvalue(), "a.zip", ".docx"), "")

    def test_extrair_texto_usa_textutil_quando_existe(self):
        bruto = docx_bytes("Art. 1º Texto oficial.")
        with mock.patch("comum.shutil.which", return_value="/usr/bin/textutil"):
            with mock.patch("comum.subprocess.run") as run:
                run.return_value.stdout = "<p>Art. 1º via textutil</p>".encode()
                html, texto = extrair_texto(bruto, "https://exemplo.leg.br/a.docx")
        self.assertEqual(html, "<p>Art. 1º via textutil</p>")
        self.assertIsNone(texto)
        self.assertEqual(run.call_args.args[0][0], "textutil")

    def test_extrair_texto_cai_para_xml_sem_textutil(self):
        bruto = docx_bytes("Art. 1º Texto oficial.")
        with mock.patch("comum.shutil.which", return_value=None):
            html, texto = extrair_texto(bruto, "https://exemplo.leg.br/a.docx")
        self.assertIsNone(html)
        self.assertEqual(texto.strip(), "Art. 1º Texto oficial.")

    def test_antiword_quando_disponivel(self):
        if not shutil.which("antiword"):
            self.skipTest("antiword não instalado")
        ole = Path(__file__).resolve().parent.parent / "municipais/_fonte/capitais/porto-alegre/porto-alegre-codigo-tributario-7-1973.doc"
        if not ole.exists():
            self.skipTest("DOC oficial ainda não capturado")
        with tempfile.TemporaryDirectory() as tmp:
            src = str(Path(tmp) / "a.doc")
            Path(src).write_bytes(ole.read_bytes())
            texto = texto_office_sem_textutil(ole.read_bytes(), src, ".doc")
        self.assertIn("tribut", texto.lower())


if __name__ == "__main__":
    unittest.main()
