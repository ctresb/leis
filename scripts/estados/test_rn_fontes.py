import io,unittest,urllib.error
from unittest.mock import patch
from coletar_rn_fontes import capturar
class RespostasRN(unittest.TestCase):
    def test_http_erro_preserva_corpo_status_headers(self):
        for st in (404,429,500):
            with self.subTest(status=st):
                e=urllib.error.HTTPError('https://www.al.rn.leg.br/arquivo.pdf',st,'erro',{'Content-Type':'text/html'},io.BytesIO(b'pagina oficial indisponivel'))
                with patch('urllib.request.urlopen',side_effect=e):
                    code,body,headers,url=capturar(e.url)
                self.assertEqual(code,st);self.assertEqual(body,b'pagina oficial indisponivel');self.assertEqual(headers['Content-Type'],'text/html')
    def test_timeout_nao_parece_resposta_http(self):
        with patch('urllib.request.urlopen',side_effect=TimeoutError('timeout')):
            with self.assertRaises(TimeoutError):capturar('https://www.al.rn.leg.br/arquivo.pdf')
if __name__=='__main__':unittest.main()
