"""Parser da base Domino da CMRJ, sem rede."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cmrj

XML = """<?xml version="1.0" encoding="UTF-8"?>
<viewentries timestamp="20261028T000000,00Z" toplevelentries="2">
<viewentry position="1" unid="AAA111" noteid="1" siblings="2">
<entrydata columnnumber="0" name="$8"><text>43</text></entrydata>
<entrydata columnnumber="3" name="ComplL"><number>2025</number></entrydata>
<entrydata columnnumber="4" name="Status"><text>Em Vigor</text></entrydata>
<entrydata columnnumber="5" name="$9"><text>Altera dispositivos.</text></entrydata>
</viewentry>
<viewentry position="2" unid="BBB222" noteid="2" siblings="2">
<entrydata columnnumber="0" name="$8"><text>1</text></entrydata>
<entrydata columnnumber="3" name="ComplL"><number>1993</number></entrydata>
<entrydata columnnumber="4" name="Status"><text>Declarado Inconstitucional Total</text></entrydata>
<entrydata columnnumber="5" name="$9"><text>Primeira emenda.</text></entrydata>
</viewentry>
</viewentries>
"""

HTML = """<!DOCTYPE HTML><html><body>
<table><tr><td>Emenda  nº</td><td>43</td><td>/</td><td>2025</td>
<td>Data da promulgação</td><td>09/10/2025</td></tr></table>
<div id="cSec2">chrome</div>
<div id="xSec2"><a href="#"><img src="/icons/collapse.gif"></a>
<b><font>Texto da Emenda</font></b><br>
<b>EMENDA À LEI ORGÂNICA Nº 43, DE 10 DE SETEMBRO DE 2025.</b>
<br>Art. 1º Fica alterado o art. 41.<br>
Art. 2º Esta Emenda entra em vigor na data de sua publicação.
<table border="1"><tr><td>Status da Lei</td><td>Em Vigor</td></tr></table>
</div>
<script>_dSectionExpand('2');</script>
<b>Atalho para outros documentos</b>
</body></html>
"""


class CmrjTest(unittest.TestCase):
    def test_entradas_xml_conta_toplevel_e_campos(self):
        total, itens = cmrj.entradas_xml(XML)
        self.assertEqual(total, 2)
        self.assertEqual([i["numero"] for i in itens], ["43", "1"])
        self.assertEqual(itens[0]["ano"], "2025")
        self.assertEqual(itens[1]["situacao"], "Declarado Inconstitucional Total")
        self.assertEqual(itens[0]["unid"], "AAA111")

    def test_categoria_view_rejeita_count_acima_de_1000(self):
        with self.assertRaises(ValueError):
            cmrj.ler_view(None, "emenda", count=1001)

    def test_data_prefere_epigrafe_e_header_e_mm_dd(self):
        corpo, html = cmrj.corpo_documento(HTML.encode(), "text/html; charset=UTF-8")
        self.assertIn("EMENDA À LEI ORGÂNICA Nº 43", corpo)
        self.assertIn("Art. 1º", corpo)
        self.assertNotIn("Texto da Emenda", corpo)
        self.assertNotIn("<img", corpo)
        self.assertEqual(cmrj.data_do_documento(html, corpo), "2025-09-10")
        self.assertEqual(cmrj.data_do_documento(
            "Data da Lei 01/16/2024", "sem epígrafe"), "2024-01-16")
        self.assertEqual(cmrj.data_do_documento(
            "Data da Lei 12/28/2018",
            "LEI COMPLEMENTAR Nº 197, DE 27 DE DEZEMBRO DE 2018."), "2018-12-27")
        self.assertEqual(cmrj.data_do_documento(
            "Data da Lei 01/16/2024",
            "Lei Complementar nº 201 de 29 de maio de 2019. LEI COMPLEMENTAR Nº 270\\*, DE 16 DE JANEIRO DE 2024."),
            "2024-01-16")

    def test_anexos_so_do_mesmo_unid(self):
        html = (
            '<a href="/APL/Legislativos/contlei.nsf/0/abc123/$FILE/Anexo%201.pdf">a</a>'
            '<a href="/APL/Legislativos/scpro.nsf/0/xyz/$FILE/Dec.pdf">b</a>'
            '<a href="/APL/Legislativos/contlei.nsf/0/abc123/$FILE/Anexo%201.pdf">dup</a>'
        )
        anexos = cmrj.anexos_pdf(html, "ABC123")
        self.assertEqual(len(anexos), 1)
        self.assertTrue(anexos[0][1].startswith("Anexo"))


if __name__ == "__main__":
    unittest.main()
