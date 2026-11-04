"""Catálogo das capitais: HTTPS preferido e formatos oficiais além de PDF."""
import unittest

from baixar_capitais_documentos import documento_oficial, preferir_https


class CapitaisHttpsTest(unittest.TestCase):
    def test_http_vira_https_sem_inventar_host(self):
        self.assertEqual(
            preferir_https("http://legislacao.portoalegre.rs.gov.br/media/a.pdf"),
            "https://legislacao.portoalegre.rs.gov.br/media/a.pdf")
        self.assertEqual(preferir_https("https://legislacao.portoalegre.rs.gov.br/media/a.pdf"),
                         "https://legislacao.portoalegre.rs.gov.br/media/a.pdf")

    def test_reconhece_pdf_doc_docx_html(self):
        self.assertTrue(documento_oficial(b"%PDF-1.4 fake"))
        self.assertTrue(documento_oficial(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1resto"))
        self.assertTrue(documento_oficial(b"PK\x03\x04resto"))
        self.assertTrue(documento_oficial(b"  <html><p>Art. 1</p>"))
        self.assertFalse(documento_oficial(b"GIF89a"))


if __name__ == "__main__":
    unittest.main()
