"""Construção de candidato novo após QA LEGIS/AC, com esquema README obrigatório."""
import json,hashlib
from metadados_legis_ac import montar,representar
from representacao_html_ac_legis import MODO
SHA=lambda b:hashlib.sha256(b).hexdigest()
def criar(captura,qa,native,edicao,observacao_contextual=None):
 it=captura['item']
 if qa['sha256_corpo']!=SHA(native.encode()) or captura['url']!=it['fonte']:raise ValueError('candidato não corresponde ao corpo/fonte auditados')
 meta=dict(titulo=it['titulo_indice'],uf='AC',tipo=it['tipo'],numero=it['numero'],data=it['data'],ementa=qa['ementa_indice'],situacao=None,revogada=None,fonte=it['fonte'],arquivo=captura['url'],id_fonte='LEGIS-AC:'+it['id_LEGIS'],representacao_corpo=MODO,edicao=edicao,sha256_texto=qa['sha256_corpo'],observacao_fonte='Transcrição do campo digital oficial com fonte integral/índice/CSS/JS preservados. Whitespace textual representado por entidades equivalentes para CommonMark, sem correção presumida de nomes/OCR/data; sem certificar edição DOE ou vigência global.')
 if observacao_contextual is not None:meta['observacao_contextual']=observacao_contextual
 meta=montar(meta,captura);blob=representar(meta,('# '+meta['titulo']+'\n\n'+native).encode())
 return blob
