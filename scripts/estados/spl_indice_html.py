"""Identidades SPL/Agape pelo cartão HTML oficial; não usa CSV deslocado."""
import datetime as dt
import re
from urllib.parse import parse_qs,urljoin,urlparse
from lxml import html

BASES={'ES':'https://www3.al.es.gov.br','SE':'https://aleselegis.al.se.leg.br'}
TIPOS={'SE':{'3':'Lei Complementar','4':'Lei Ordinária'},'ES':{'3':'Lei Ordinária','4':'Lei Complementar'}}

def ler_indice(bruto,url,uf,tipo,ano):
    base=BASES[uf];parsed=urlparse(url)
    if parsed.netloc!=urlparse(base).netloc:raise ValueError('origem inesperada')
    tree=html.fromstring(bruto.decode('utf-8',errors='strict'));out=[];ids=set()
    for card in tree.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," kt-widget5__item ")]'):
        titles=card.xpath('.//a[contains(concat(" ",normalize-space(@class)," ")," kt-widget5__title ")]')
        if len(titles)!=1:raise ValueError('cartão sem epígrafe única')
        title=' '.join(titles[0].text_content().split());m=re.fullmatch(r'(Lei Ordinária|Lei Complementar)\s+n[°º]\s*([\d.]+(?:-[A-Za-z]+)?)/(\d{4})',title)
        if not m or m[1]!=TIPOS[uf][tipo] or m[3]!=str(ano):raise ValueError('tipo/ano/epígrafe do cartão divergem')
        link=urljoin(url,titles[0].get('href'));p=urlparse(link);q=parse_qs(p.query)
        if p.netloc!=parsed.netloc or not p.path.endswith('/norma.aspx') or q.get('tipo')!=[tipo] or q.get('ano')!=[str(ano)] or not q.get('id',[''])[0].isdigit():raise ValueError('identidade do link diverge')
        id_=q['id'][0]
        if id_ in ids:raise ValueError('ID repetido no índice')
        ids.add(id_);infos=card.xpath('.//div[contains(concat(" ",normalize-space(@class)," ")," kt-widget5__info ")]')[0];spans=infos.xpath('./span')
        if len(spans)!=4 or ' '.join(spans[0].text_content().split())!='Data:' or ' '.join(spans[2].text_content().split())!='Situação:':raise ValueError('estrutura data/situação inesperada')
        date=dt.datetime.strptime(' '.join(spans[1].text_content().split()),'%d/%m/%Y').date()
        if str(date.year)!=str(ano) or date>dt.date.today():raise ValueError('data não comprovada')
        texts=[urljoin(base,a.get('href')) for a in card.xpath('.//a[@href]') if re.match(r'^/Arquivo/Documents/legislacao/html/[^?#]+\.html$',a.get('href'),re.I)]
        texts=list(dict.fromkeys(texts));desc=card.xpath('.//a[contains(concat(" ",normalize-space(@class)," ")," kt-widget5__desc ")]')
        if len(desc)!=1:raise ValueError('ementa não única')
        out.append(dict(UF=uf,tipo=m[1],tipo_indice=tipo,id=id_,numero=m[2].replace('.','').upper(),ano=int(ano),data=date.isoformat(),titulo_indice=title,ementa=' '.join(desc[0].text_content().split()),situacao=' '.join(spans[3].text_content().split()),fonte=link,textos_completos_observados=texts))
    if not out:raise ValueError('índice sem cartões')
    return out
