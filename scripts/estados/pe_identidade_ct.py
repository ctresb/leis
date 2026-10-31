"""Prova explícita da divergência índice -C versus epígrafe -CT, sem alterar fonte."""
import copy,re
from pe_identidade import numero_indice,identidade_do_texto

def comprovar_ct(item,corpo):
    if item.get('tipo')!='8':raise ValueError('categoria não é portaria')
    indexed=numero_indice(item)
    if not re.fullmatch(r'\d+-C',indexed):raise ValueError('índice não possui a divergência -C selecionada')
    lines=[ln.strip() for ln in corpo.splitlines() if ln.strip()][:6];ep=next((ln for ln in lines if re.match(r'^\*{0,2}\s*PORTARIA(?:\s+ADMINISTRATIVA)?\s+N[º°o.\s]*[\d.]+\s*-\s*CT\b',ln,re.I)),None)
    if ep is None:raise ValueError('epígrafe própria -CT não comprovada')
    m=re.search(r'N[º°o.\s]*([\d.]+)\s*-\s*CT\b',ep,re.I);printed=(m[1].replace('.','').lstrip('0') or '0')+'-CT';want=(indexed[:-2].lstrip('0') or '0')+'-CT'
    if printed!=want:raise ValueError('número impresso não corresponde ao número-base do índice')
    adjusted=copy.deepcopy(item);adjusted['nome']=re.sub(r'(?<=\d)-C\b','-CT',item['nome'],flags=re.I)
    # Só a cópia usada para reconhecer a epígrafe remove espaços em torno do hífen.
    # O corpo oficial e a representação produzida permanecem literais.
    normalized=re.sub(r'\s*-\s*(?=CT\b)','-',ep,flags=re.I);num,date,_=identidade_do_texto(adjusted,normalized)
    return adjusted,dict(numero=num,data=date,epigrafe_literal=ep,numero_indice=indexed,titulo_indice=item['nome'],regra='Mesmo ID oficial e número-base; índice termina-C, epígrafe impressa termina-CT. Não considera equivalentes outros sufixos nem corrige o corpo.')


def auditar_ct(raw,source,item,ctype='text/html; charset=utf-8'):
    """Replay serial da exceção comprovada, mantendo todos os gates congelados.

    Só o resolvedor de identidade recebe a prova -CT; o auditor integral continua
    confrontando a resposta original, sem alterar bytes do campo nem metadado-base.
    Não usar concorrência por threads com este adaptador privado.
    """
    from unittest.mock import patch
    import auditar_pe_infralegal_cache as base
    from pe import limites_texto_html
    from comum import decodificar,html_para_md
    def resolver(used,pagina):
        a,b=limites_texto_html(pagina);adjusted,proof=comprovar_ct(item,html_para_md(pagina[a:b]))
        if adjusted!=used:raise ValueError('cópia de índice ajustada não confere com prova literal')
        return proof['numero'],proof['data'],proof['epigrafe_literal']
    pagina=decodificar(source,ctype);a,b=limites_texto_html(pagina);adjusted,identity=comprovar_ct(item,html_para_md(pagina[a:b]))
    with patch.object(base,'identidade_primaria',side_effect=resolver):qa=base.auditar(raw,source,adjusted,ctype)
    qa['divergencia_indice']=identity
    return qa
