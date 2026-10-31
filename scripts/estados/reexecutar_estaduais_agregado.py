"""Replay único RN17+AM4 PDFs e GO64 mudanças exclusivas de revogada.

Somente leitura; nunca promove candidatos ou chama Git. --head-sha256 recebe
mapa produzido pelo coordenador: path -> SHA256 do blob HEAD, null se ausente.
Sem o mapa, valida conteúdo mas encerra2, deixando controle HEAD pendente.
"""
import argparse,gzip,hashlib,json,re
from pathlib import Path
from markdown_it import MarkdownIt
from auditar_rn_retomada_pdf import auditar as auditar_rn
from auditar_sapl_recentes_pdf import auditar as auditar_am
from pdf_texto_fiel import extrair_camada_textual
SHA=lambda b:hashlib.sha256(b).hexdigest()

def conferir_arquivo(frozen):
    raw=Path(frozen['congelado']).read_bytes()
    if SHA(raw)!=frozen['sha256_arquivo']:raise ValueError('snapshot mudou: '+frozen['congelado'])
    return raw

def conferir_diff_status(preimage,candidate):
    head,body=preimage.split(b'\n---\n',1);newhead,n=re.subn(rb'(?m)^revogada: false$',b'revogada: null',head)
    if n!=1 or candidate!=newhead+b'\n---\n'+body:raise ValueError('diferença não é exclusivamente revogada false→null no frontmatter')
    return True

def metadados(raw):
    out={}
    for line in raw.decode('utf8').split('\n---\n',1)[0].splitlines():
        if ': ' in line:
            k,v=line.split(': ',1)
            try:out[k]=json.loads(v)
            except ValueError:out[k]=v
    return out

def conferir_head(expected,observed):
    if set(expected)!=set(observed):raise ValueError('mapa HEAD não contém exatamente os85 caminhos')
    for p,sha in expected.items():
        if observed[p]!=sha:raise ValueError('preimagem HEAD diverge: '+p)

def auditar_go(r):
    pre=gzip.decompress(conferir_arquivo(r['preimagem']));candidate=gzip.decompress(conferir_arquivo(r['candidato']));current=Path(r['path']).read_bytes()
    if SHA(pre)!=r['sha256_MD_atual_esperado'] or SHA(current)!=SHA(pre):raise ValueError('canônico GO alterado ou preimagem mudou')
    if SHA(candidate)!=r['sha256_MD_futuro']:raise ValueError('candidato GO mudou')
    conferir_diff_status(pre,candidate);before=metadados(pre);after=metadados(candidate)
    if before['uf']!='GO' or before['revogada'] is not False or after['revogada'] is not None:raise ValueError('UF/status não confere')
    idx=json.loads(conferir_arquivo(r['indice_congelado']));index=next((it for it in idx if str(it['id'])==str(r['id_oficial'])),None)
    if index is None or index!=r['item_indice']:raise ValueError('item de índice congelado diverge')
    status=(index.get('estado_legislacao') or {}).get('nome')
    if status!=r['situacao_literal'] or before['situacao']!=status or after['situacao']!=status or status in ('Em Vigor','Revogada'):raise ValueError('situação literal não comprova correção conservadora')
    if before.get('fonte')!='https://legisla.casacivil.go.gov.br/pesquisa_legislacao/'+str(r['id_oficial']):raise ValueError('identidade/fonte GO não corresponde ao ID')
    source=gzip.decompress(conferir_arquivo(r['fonte_congelada']))
    if SHA(source)!=r['sha256_fonte']:raise ValueError('fonte GO diverge')
    return dict(preimagem_SHA256=SHA(pre),candidato_SHA256=SHA(candidate),fonte_SHA256=SHA(source),situacao_literal=status,corpo_byte_a_byte_igual=True,diff_exclusivo_frontmatter=True,canonico_inalterado=True)

def auditar_pdf(r):
    raw=Path(r['path']).read_bytes()
    if SHA(raw)!=r['sha256_MD_esperado']:raise ValueError('MD PDF diverge do pacote')
    conferido=conferir_arquivo(r['fonte_congelada']);body,proof=(auditar_rn if r['UF']=='RN' else auditar_am)(r['captura'],raw)
    _,layer=extrair_camada_textual(gzip.decompress(conferido));pages=layer.split('\f');pages=pages[:-1] if pages and not pages[-1].strip() else pages
    fenced=[t.content for t in MarkdownIt('commonmark',{'html':True}).parse(body) if t.type=='fence']
    if fenced!=[p if p.endswith('\n') else p+'\n' for p in pages]:raise ValueError('CommonMark diverge de página textual íntegra')
    return dict(**proof,CommonMark_paginas_iguais=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--controle',required=True);ap.add_argument('--head-sha256');ap.add_argument('--saida',required=True);a=ap.parse_args();m=json.loads(Path(a.controle).read_text());rows=m['documentos']
    if len(rows)!=85 or len({r['path'] for r in rows})!=85:raise ValueError('união de documentos não é85 distinta')
    if sum(r['acao']=='novo_pdf' for r in rows)!=21 or sum(r['acao']=='corrigir_status' for r in rows)!=64:raise ValueError('classes do agregado divergem')
    for f,s in m['dependencias'].items():
        if SHA(Path(f).read_bytes())!=s:raise ValueError('manifesto anterior mudou: '+f)
    for r in m['fontes_indices_primarias']:
        packed=conferir_arquivo(r['arquivo_congelado'])
        if SHA(gzip.decompress(packed))!=r['sha256_fonte']:raise ValueError('índice primário mudou')
    for v in m['evidencias_visuais']:conferir_arquivo(v)
    headok=False
    if a.head_sha256:
        conferir_head({r['path']:r['sha256_preimagem_HEAD_esperada'] for r in rows},json.loads(Path(a.head_sha256).read_text()));headok=True
    bad=0;sourcehashes=set();pages=0
    with Path(a.saida).open('x') as out:
        for r in rows:
            result=dict(path=r['path'],acao=r['acao'],aceito_conteudo=False,HEAD_conferido=headok)
            try:
                proof=auditar_pdf(r) if r['acao']=='novo_pdf' else auditar_go(r)
                if r['acao']=='novo_pdf':
                    if proof['sha256_fonte'] in sourcehashes:raise ValueError('PDF repetido em identidades distintas')
                    sourcehashes.add(proof['sha256_fonte']);pages+=proof['total_paginas']
                result.update(aceito_conteudo=True,QA=proof)
            except Exception as e:result['erro']=type(e).__name__+': '+str(e);bad+=1
            out.write(json.dumps(result,ensure_ascii=False)+'\n');out.flush()
    print(json.dumps(dict(total=85,novos_PDF=21,paginas_PDF=pages,reparos_status_GO=64,falhas_conteudo=bad,HEAD_conferido=headok,promocao_executada=False)))
    if bad:raise SystemExit(1)
    if not headok:raise SystemExit(2)
if __name__=='__main__':main()
