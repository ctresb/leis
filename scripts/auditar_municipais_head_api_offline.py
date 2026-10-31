"""Audita vínculos API dos municípios publicados em um HEAD fixo; somente leitura.

Git é limitado a rev-parse HEAD, ls-tree municipal e cat-file dos blobs desse
escopo. Não consulta índice, status global, rede nem modifica normas. Ausência
de cache/metadado não constitui erro; achados são propostas individuais de revisão.
Uma versão TA privada paralela nunca é atribuída a uma transcrição que não a usa.
"""
import argparse
import collections
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata
from urllib.parse import urlsplit
sys.path.insert(0, str(Path(__file__).resolve().parent))
from auditar_municipal import metadados

ROOT = Path(__file__).resolve().parent.parent
UF = set('AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO'.split())


def sha(b):
    return hashlib.sha256(b).hexdigest()


def normal(s):
    return ' '.join(''.join(c for c in unicodedata.normalize('NFD',str(s).upper()) if unicodedata.category(c)!='Mn').split())


def vinculos(meta):
    norm = None
    tas = set()
    for field in ('fonte','fonte_registro','fonte_api','fonte_texto'):
        value = meta.get(field)
        if not isinstance(value,str):
            continue
        u = urlsplit(value)
        if u.scheme not in {'http','https'} or not u.hostname:
            continue
        host = u.hostname.lower()
        m = re.search(r'/norma/(?:normajuridica/)?(\d+)(?:/|$)',u.path)
        media = re.search(r'/normajuridica/\d{4}/(\d+)(?:/|$)',u.path)
        if norm is None and (m or media):
            norm = (host,int((m or media)[1]))
        ta = re.search(r'/ta/(\d+)/text/?$',u.path)
        if ta:
            tas.add((host,int(ta[1])))
    return norm, sorted(tas)


def analisar(meta, norm_records, used_ta_records, kinds, houses, ibge):
    findings = []
    spheres = sorted({normal(r['registro'].get('esfera_federacao','')) for r in norm_records})
    foreign = [r for r in norm_records if normal(r['registro'].get('esfera_federacao','')) in {'E','F'}]
    if foreign:
        findings.append(dict(regra='api_esfera_estadual_ou_federal',valores_registrados=spheres,
                             evidencias=norm_records if len(spheres)>1 else foreign,limite='Classificação do cache oficial; requer revisão individual do ato. Não afirma por si só que o texto seja federal/estadual ou que uma mudança cadastral tenha ocorrido na publicação.'))
    for r in used_ta_records:
        ta = r['registro']
        privacy = ta.get('privacidade')
        if isinstance(privacy,str) and privacy.isdigit():
            privacy = int(privacy)
        if isinstance(privacy,int) and privacy not in {0,69}:
            findings.append(dict(regra='ta_usado_com_status_nao_publico_no_cache',privacidade=privacy,
                                 evidencia=r,limite='Somente TA explicitamente vinculado pela fonte da transcrição; não confundir versão privada paralela com texto usado. Cache não demonstra retroativamente o status na data de publicação.'))
        descriptions = {normal(k['registro'].get('descricao','')) for k in kinds if k['registro'].get('id')==ta.get('tipo_ta')}
        if descriptions and 'NORMA JURIDICA' not in descriptions:
            findings.append(dict(regra='modelo_do_ta_usado_diferente_norma_juridica',descricoes=sorted(descriptions),
                                 evidencia_ta=r,evidencias_tipo=[k for k in kinds if k['registro'].get('id')==ta.get('tipo_ta')],
                                 limite='Descrição configurada pelo portal; revisar modelo e fonte literal antes de qualquer conclusão.'))
    unique = {}
    for r in houses:
        h = r['registro']
        uf,city = normal(h.get('uf','')),normal(h.get('municipio',''))
        if uf in UF and city:
            unique.setdefault((uf,city),r)
    # Uma casa ambígua ou incompleta não confirma divergência.
    if len(unique)==1:
        (uf,city),proof = next(iter(unique.items()))
        own_uf,own_city = normal(meta.get('uf','')),normal(meta.get('municipio',''))
        expected = ibge.get((uf,city))
        own_code = str(meta.get('codigo_ibge',''))
        if own_uf in UF and own_uf!=uf:
            findings.append(dict(regra='uf_publicada_diverge_casa_api',uf_publicada=own_uf,uf_casa=uf,evidencia=proof))
        elif expected and re.fullmatch(r'\d{7}',own_code) and own_code!=expected:
            findings.append(dict(regra='ibge_publicado_diverge_casa_api',codigo_publicado=own_code,codigo_casa_derivado_ibge=expected,evidencia=proof))
        elif not own_code and own_city and own_city!=city and (own_uf,own_city) in ibge:
            findings.append(dict(regra='municipio_publicado_diverge_casa_api',municipio_publicado=meta.get('municipio'),municipio_casa=proof['registro']['municipio'],evidencia=proof))
    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--saida',type=Path,required=True)
    a = ap.parse_args()
    a.saida.mkdir(parents=True,exist_ok=False)
    env = dict(os.environ,GIT_OPTIONAL_LOCKS='0')
    head = subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,env=env).decode().strip()
    tree = subprocess.check_output(['git','ls-tree','-r','-z',head,'--','municipais'],cwd=ROOT,env=env)
    selected = []
    for record in tree.split(b'\0'):
        if not record:
            continue
        info,path = record.split(b'\t',1)
        mode,kind,oid = info.split()
        name = path.decode()
        if kind==b'blob' and name.endswith('.md') and not any(p.startswith('_') for p in Path(name).parts):
            selected.append((name,oid.decode()))
    (a.saida/'publicados.paths.txt').write_text(''.join(p+'\n' for p,_ in selected))
    process = subprocess.Popen(['git','cat-file','--batch'],cwd=ROOT,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    published = []
    try:
        for name,oid in selected:
            process.stdin.write((oid+'\n').encode());process.stdin.flush()
            header = process.stdout.readline().split()
            if len(header)!=3 or header[1]!=b'blob':
                raise RuntimeError('Blob municipal indisponível: '+name)
            raw = process.stdout.read(int(header[2]))
            if process.stdout.read(1)!=b'\n':
                raise RuntimeError('Blob municipal incompleto')
            meta = metadados(raw.decode('utf-8',errors='replace'))
            norm,tas = vinculos(meta)
            published.append(dict(path=name,git_oid=oid,sha256=sha(raw),metadados=meta,norma=norm,tas=tas))
    finally:
        process.stdin.close();process.stdout.close()
        if process.wait()!=0:
            raise RuntimeError('cat-file não concluiu')
    hosts = {r['norma'][0] for r in published if r['norma']} | {h for r in published for h,_ in r['tas']}
    norms = collections.defaultdict(list);tas = collections.defaultdict(list)
    houses = collections.defaultdict(list);kinds = collections.defaultdict(list)
    cache_errors = [];cache_count = 0
    cache_ledger = (a.saida/'caches-lidos.jsonl').open('x')
    roots = [ROOT/'municipais/_indice/organicas-sapl',ROOT/'municipais/_fonte/texto-articulado-sapl',ROOT/'municipais/_fonte/organicas-sapl']
    try:
        for host in sorted(hosts):
            for base in roots:
                folder = base/host
                if not folder.is_dir():
                    continue
                for p in sorted(folder.rglob('*.json*')):
                    if not p.is_file() or p.name.endswith('.meta.json') or not (p.name.endswith('.json') or p.name.endswith('.json.gz')):
                        continue
                    try:
                        raw = p.read_bytes()
                        data = json.loads(gzip.decompress(raw) if p.name.endswith('.gz') else raw)
                    except (ValueError,OSError,EOFError) as e:
                        cache_errors.append(dict(arquivo=str(p.relative_to(ROOT)),erro=type(e).__name__))
                        continue
                    rows = data.get('results') if isinstance(data,dict) and isinstance(data.get('results'),list) else data if isinstance(data,list) else [data]
                    file_sha = sha(raw)
                    capture = None
                    meta_path = p.with_suffix('.meta.json')
                    if meta_path.exists():
                        try:capture=json.loads(meta_path.read_text()).get('capturado_em')
                        except (ValueError,OSError):pass
                    recognized = 0
                    for i,r in enumerate(rows):
                        if not isinstance(r,dict) or not isinstance(r.get('id'),int):
                            continue
                        target = None;fields = []
                        if 'esfera_federacao' in r or {'texto_integral','ementa','numero','data'}<=r.keys():
                            target=norms[(host,r['id'])];fields=['id','__str__','numero','ano','data','esfera_federacao','tipo','texto_integral','data_ultima_atualizacao']
                        elif {'privacidade','tipo_ta','content_type','object_id'}<=r.keys():
                            target=tas[(host,r['id'])];fields=['id','__str__','privacidade','tipo_ta','content_type','object_id','numero','ano','data']
                        elif {'nome','municipio','uf','endereco'}<=r.keys():
                            target=houses[host];fields=['id','nome','sigla','municipio','uf']
                        elif {'descricao','content_type'}<=r.keys():
                            target=kinds[host];fields=['id','descricao','content_type']
                        if target is not None:
                            pointer=('/results/'+str(i)) if isinstance(data,dict) and isinstance(data.get('results'),list) else '/'+str(i) if isinstance(data,list) else ''
                            target.append(dict(registro={k:r[k] for k in fields if k in r},arquivo=str(p.relative_to(ROOT)),sha256=file_sha,json_pointer=pointer,capturado_em=capture))
                            recognized+=1
                    cache_count+=1
                    cache_ledger.write(json.dumps(dict(arquivo=str(p.relative_to(ROOT)),sha256=file_sha,bytes=len(raw),registros_reconhecidos=recognized),ensure_ascii=False)+'\n')
            print(json.dumps(dict(host=host,caches_lidos=cache_count)),flush=True)
    finally:
        cache_ledger.close()
    ibge_path=ROOT/'municipais/_indice/ibge-municipios.json'
    ibge={(r['regiao-imediata']['regiao-intermediaria']['UF']['sigla'],normal(r['nome'])):str(r['id']) for r in json.loads(ibge_path.read_text())}
    counts=collections.Counter();findings=[]
    with (a.saida/'cobertura.jsonl').open('x') as coverage:
        for r in published:
            norm_records=norms.get(tuple(r['norma']),[]) if r['norma'] else []
            used=[row for key in r['tas'] for row in tas.get(tuple(key),[])]
            host=r['norma'][0] if r['norma'] else r['tas'][0][0] if r['tas'] else None
            rows=analisar(r['metadados'],norm_records,used,kinds.get(host,[]),houses.get(host,[]),ibge)
            counts['publicados']+=1;counts['vinculo_sapl_identificavel']+=bool(r['norma'] or r['tas']);counts['norma_com_cache_api']+=bool(norm_records);counts['ta_usado_com_cache_api']+=bool(used)
            counts['com_proposta_revisao']+=bool(rows)
            for row in rows:counts['regra_'+row['regra']]+=1
            coverage.write(json.dumps(dict(path=r['path'],sha256=r['sha256'],git_oid=r['git_oid'],norma=r['norma'],tas_usados=r['tas'],cache_norma=bool(norm_records),cache_ta_usado=bool(used),propostas=len(rows)),ensure_ascii=False)+'\n')
            if rows:
                findings.append(dict(path=r['path'],sha256=r['sha256'],git_oid=r['git_oid'],head=head,metadados_publicados={k:r['metadados'].get(k) for k in ['municipio','uf','codigo_ibge','tipo','numero','data','fonte','fonte_texto']},propostas=rows,
                                     decisao='Revisão individual; nenhum arquivo alterado ou removido automaticamente. Ausência de metadado/cache não é erro.'))
    (a.saida/'propostas.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2)+'\n')
    manifest=dict(head=head,escopo='Somente blobs municipais de normas no HEAD fixo; cache existente dos hosts explicitamente vinculados. Nenhuma consulta HTTP, índice ou status Git global.',contagens=counts,hosts=len(hosts),caches_lidos=cache_count,caches_ilegíveis=cache_errors,
                  ibge_sha256=sha(ibge_path.read_bytes()),codigo_sha256=sha(Path(__file__).read_bytes()),
                  limite='Propostas não são declaração de invalidade nem contagem de atos incorretos. API pode conter erro cadastral ou versões conflitantes; exigir fonte literal e contexto antes de corrigir. Versão TA privada paralela não utilizada é ignorada. Ausência de cache/metadado permanece inconclusiva.')
    (a.saida/'manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(manifest,ensure_ascii=False))


if __name__=='__main__':
    main()
