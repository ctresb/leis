# -*- coding: utf-8 -*-
"""Audita decretos PE contra o campo HTML oficial em cache, sem alterar arquivos.

Exemplo: python3 scripts/estados/auditar_pe_cache.py --lista lote.txt --saida resultado.jsonl
Retenções são conservadoras. Cada documento tem limite de tempo de 20 segundos;
problemas de fonte, identidade, imagens, anexos ou tabelas permanecem explícitos.
"""
from pathlib import Path
import sys,json,re,gzip,hashlib,html,collections,concurrent.futures,time,signal
sys.path[:0]=[str(Path(__file__).resolve().parent.parent),str(Path(__file__).resolve().parent)]
from comum import html_para_md
from pe import limites_texto_html
from integridade_texto import verificar_integridade_texto
from avisos_fonte import avisos_de_omissao
from anexos_fonte import remissoes_sem_representacao
from visuais_fonte import imagens_html
from tabelas_estrutura import conferir_tabelas_complexas
R=Path(__file__).resolve().parents[2];index=R/'estaduais/PE/_indice/lista.json';catalog={str(x['id']):x for x in json.loads(index.read_text())} if index.exists() else {};MONTH={m:i for i,m in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split(),1)}
MONTH['marco']=3
EP=re.compile(r'\bDECRETO(?:\s+DO\s+EXECUTIVO)?\s+N[º°o.]*\s*([\d.]+)\s*,?\s*DE\s+(\d{1,2})[º°o]?\s+DE\s+(\w+)\s+DE\s+(\d{4})',re.I)
APP=re.compile(r'\b(?:fica[m]?|é|são)\s+aprovad[oa]s?\b[\s\S]{0,190}?\b(documento|manual|plano|programa|regulamento|regimento|estatuto|projeto|quadro|tabela|c[oó]digo|conv[eê]nio|acordo|termo)\b',re.I)
FOREIGN=re.compile(r'(?m)^[ *#>]*(LEI(?: COMPLEMENTAR)?|DECRETO(?: LEGISLATIVO)?|RESOLU[ÇC][ÃA]O|PORTARIA|EDITAL|ATO)\s+N[º°o.\s]*\s*(\d[\d.]*)\s*[,.-]?\s*DE\s+\d{1,2}[ºo.]*\s+DE\s+\w+\s+DE\s+\d{4}[. *]*$',re.I)
def alpha(s):return ''.join(c.casefold() for c in html.unescape(re.sub('<[^>]+>',' ',s)) if c.isalnum())
def pipes(s):return [tuple(alpha(c) for c in l.split('|')[1:-1]) for l in s.splitlines() if l.strip().startswith('|') and not re.fullmatch(r'[| :\-]+',l)]
def timeout_handler(*args):raise TimeoutError('conversão/gate excedeu 20 segundos; manter retido para revisão isolada')
def limpar_residuo_limite(body,converted):
    """Só retira o sufixo técnico quando o restante corresponde à fonte delimitada."""
    cleaned=re.sub(r'\n\s*\n(?:&lt;div|<div)\s*$', '',body).rstrip()
    if cleaned!=body and alpha(cleaned)==alpha(converted):
        return cleaned,body[len(cleaned):]
    return body,None


def one(d):
 p=d['path'];m=d['metadata'];ret=[];ev={};result={'path':p,'sha256_md':d['sha256'],'id_oficial':d['id'],'fonte':m.get('fonte'),'tipo':m.get('tipo'),'numero':m.get('numero'),'data':m.get('data'),'versao_texto':m.get('versao_texto')}
 signal.signal(signal.SIGALRM,timeout_handler);signal.alarm(20)
 try:
  raw=(R/p).read_bytes();assert hashlib.sha256(raw).hexdigest()==d['sha256'];s=raw.decode();body=s.split('\n---\n',1)[1].split('\n',1)[1];body=re.sub(r'^# [^\n]*\n','',body,count=1).strip();cache=R/'estaduais/PE/_fonte'/Path(p).relative_to('estaduais/PE').with_suffix('.html.gz');z=cache.read_bytes();src=gzip.decompress(z).decode('utf-8');result.update(cache=str(cache.relative_to(R)),sha256_cache=hashlib.sha256(z).hexdigest(),sha256_fonte=hashlib.sha256(src.encode()).hexdigest())
  limits=limites_texto_html(src,fragmento='id="divTexto"' not in src);assert limits is not None;field=src[limits[0]:limits[1]];result['limite_campo']={'inicio':limits[0],'fim':limits[1],'bytes_fora_do_campo':len(src)-limits[1],'tipo':'fragmento divTexto fechado' if limits[0]==0 else 'resposta completa divTexto fechado'};result['sha256_campo']=hashlib.sha256(field.encode()).hexdigest();converted=html_para_md(field);result['sha256_reconversao']=hashlib.sha256(converted.encode()).hexdigest()
  body,result['residuo_limite_removivel']=limpar_residuo_limite(body,converted)
  literal=alpha(body)==alpha(converted);result['corpo_confere_sequencia_alfanumerica_fonte']=literal
  if not literal:ret.append('corpo diverge da reconversão fiel do campo');ev['inicio_reconversao']=converted[:500];ev['fim_reconversao']=converted[-500:]
  plain=html.unescape(re.sub('<[^>]+>',' ',converted)).replace('**','');pl=' '.join(plain.split());ep=EP.search(pl[:1600]);cat=catalog.get(d['id']);num=re.sub(r'\D','',str(m.get('numero',''))).lstrip('0');ev['inicio_fonte']=pl[:1000]
  if not cat:ret.append('ID ausente do índice oficial em cache')
  else:
   cn=re.search(r'n[º°o.]?\s*([\d.]+)',cat['nome'],re.I);ev['indice']={'id':cat['id'],'nome':cat['nome'],'publicacao':cat['publicacao'],'tipo':cat['tipo']}
   if not cn or re.sub(r'\D','',cn[1]).lstrip('0')!=num or str(cat['tipo'])!='6':ret.append('identidade índice e MD diverge')
  if not ep:ret.append('epígrafe própria de decreto não comprovada')
  else:
   date=f'{ep[4]}-{MONTH.get(ep[3].lower(),0):02d}-{int(ep[2]):02d}';ev['epigrafe_literal']=ep[0]
   if re.sub(r'\D','',ep[1]).lstrip('0')!=num or date!=str(m.get('data')) or date[:4]!=str(m.get('ano')):ret.append('número/data/ano da epígrafe e MD divergem')
  issue,proof=verificar_integridade_texto(converted);result['dispositivo_proprio']=proof
  if issue:ret.append(issue)
  imgs=imagens_html(field)
  if imgs:ret.append('imagem no campo normativo sem representação comprovada');ev['imagens']=imgs
  avis=avisos_de_omissao(converted)+[x[0] for x in re.finditer(r'(?i)\banexos?\s+(?:dispon[ií]veis|publicad[oa]s?|consta[m]?)\s+(?:no|em|na)\s+(?:Di[áa]rio Oficial|DODF)[^\n]{0,160}',converted)]
  if avis:ret.append('aviso explícito de material omitido');ev['avisos']=avis
  ann=remissoes_sem_representacao(converted)
  if ann:ret.append('remissão própria a anexo sem representação comprovada');ev['remissoes']=ann
  if not re.search(r'(?im)^\s*[#*\s]{0,8}(?:ANEXO|TABELA|QUADRO)\b|<table\b|^\s*\|',converted):
   loose=[x[0] for x in re.finditer(r'\b(?:indicad[oa]s?|constantes?|relacionad[oa]s?|na forma|conforme)[^.;\n]{0,100}\bAnex[oa]s?\s*[IVX\d]*\b(?!\s+(?:d[oa]|a[oa])\s+(?:Lei|Decreto|Regulamento|RICMS))',plain,re.I)]
   if loose:ret.append('remissão contextual a anexo sem representação comprovada');ev['remissoes_contextuais']=loose
  a=re.search(r'(?im)^\s*Art\.?\s*1[ºo°.]?\b',plain)
  if a:
   window=plain[a.start():a.start()+2500];end=re.search(r'(?im)^\s*Art\.?\s*2[ºo°.]?\b',window);window=window[:end.start()] if end else window;ap=APP.search(window)
   if ap:ret.append('objeto aprovado próprio exige conferência contextual');ev['objeto_aprovado']={'objeto':ap[1],'trecho':window[:1800]}
  foreign=[x[0].strip() for x in FOREIGN.finditer(plain) if re.sub(r'\D','',x[2]).lstrip('0')!=num]
  if foreign:ret.append('outra epígrafe completa no campo exige revisão de granularidade');ev['outras_epigrafes']=foreign
  struck=bool(re.search(r'<(?:s|strike|del)\b|style\s*=\s*[\"\'][^\"\']*line-through',field,re.I));css=[x[0] for st in re.findall(r'<style\b[^>]*>(.*?)</style>',src,re.I|re.S) for x in re.finditer(r'[^{}]{1,200}\{[^{}]*text-decoration[^{}]*line-through[^{}]*\}',st,re.I)]
  if struck or css:ret.append('texto tachado em edição atualizada exige separação histórica/compilada');ev['tachados']={'inline_ou_tag':struck,'regras_css':css}
  tables=conferir_tabelas_complexas(field,body);result['tabelas_complexas_conferidas']=len(tables)
  if pipes(converted)!=pipes(body):ret.append('linhas/células de tabela GFM divergem da reconversão')
  if len(alpha(converted))<40:ret.append('campo normativo vazio ou aviso')
 except Exception as e:ret.append('erro de validação: '+type(e).__name__+': '+str(e)[:250])
 signal.alarm(0)
 result.update(problemas=ret,evidencias=ev,publicavel=not ret);return result
def documento_da_lista(path):
    """Inventaria somente caminhos normativos canônicos; não admite buffers auxiliares."""
    if not re.fullmatch(r'estaduais/PE/decretos/(?:[0-9]{4}|sem-ano)/[^/]+\.md',path) or any(x.startswith('_') for x in Path(path).parts[2:]):
        raise ValueError('caminho fora do escopo canônico de decretos PE: '+path)
    raw=(R/path).read_bytes();text=raw.decode();metadata={}
    for line in text.split('\n---\n',1)[0].splitlines():
        name,sep,value=line.partition(':')
        if sep:
            try:metadata[name]=json.loads(value.strip())
            except json.JSONDecodeError:metadata[name]=value.strip()
    identity=re.search(r'[?&]id=(\d+)',str(metadata.get('fonte','')))
    return {'path':path,'sha256':hashlib.sha256(raw).hexdigest(),'metadata':metadata,'id':identity[1] if identity else None}


def main():
    """Audita cache local sem alterar MD, baixar fontes ou publicar resultados."""
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lista',required=True,help='Lista UTF-8 de caminhos MD relativos à raiz')
    parser.add_argument('--saida',required=True,help='JSONL de resultados; deve ser um novo arquivo')
    parser.add_argument('--workers',type=int,default=4)
    args=parser.parse_args()
    paths=Path(args.lista).read_text().splitlines()
    if len(paths)!=len(set(paths)):raise ValueError('lista contém caminhos repetidos')
    docs=[documento_da_lista(p) for p in paths if p]
    out=Path(args.saida);count=collections.Counter();t=time.monotonic()
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as ex,out.open('x') as f:
        for n,r in enumerate(ex.map(one,docs,chunksize=25),1):
            f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush();count['publicavel' if r['publicavel'] else 'retido']+=1
            if n%250==0:print(n,dict(count),'seg',round(time.monotonic()-t),flush=True)
    print('FINAL',len(docs),dict(count),flush=True)


if __name__=='__main__':main()
