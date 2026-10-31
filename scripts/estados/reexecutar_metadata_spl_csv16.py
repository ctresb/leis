"""Replay offline de reparos privados mínimos de metadata SPL/CSV; sem promoção."""
import argparse,gzip,hashlib,json,re
from pathlib import Path
from lxml import html
from reparar_metadata_spl_csv import candidato
SHA=lambda b:hashlib.sha256(b).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--manifesto',required=True);ap.add_argument('--saida',required=True);a=ap.parse_args();m=json.loads(Path(a.manifesto).read_text());ctrl=json.loads(Path(m['controle_ROOT']).read_text());assert SHA(Path(m['controle_ROOT']).read_bytes())==m['sha256_controle_ROOT'];packed=Path(m['baseline_ROOT']).read_bytes();assert SHA(packed)==m['sha256_baseline_ROOT'];root=[json.loads(s) for s in gzip.decompress(packed).splitlines()];P={r['path']:r for r in root};assert len(P)==9955;seen=set();proof=[]
 for r in m['documentos']:
  original=gzip.decompress(Path(r['preimagem']).read_bytes());assert SHA(original)==r['sha256_MD_preimagem']==P[r['origem']]['sha256_md'];assert P[r['origem']]['oid']==r['OID_preimagem'];rawcache=Path(r['fonte_original_preservada']).read_bytes();assert SHA(rawcache)==r['sha256_cache_original'];source=gzip.decompress(rawcache);assert SHA(source)==r['sha256_fonte_original'];meta=P[r['origem']]['meta'];assert r['arquivo_observado']==meta['arquivo'];year=r['origem'].split('/')[3];expected,q=candidato(original,source,r['arquivo_observado'],str(meta['numero']),year);actual=Path(r['privado']).read_bytes();assert actual==expected and SHA(actual)==r['sha256_candidato'];assert q==r['QA'];assert r['destino'] not in P and r['destino'] not in seen;seen.add(r['destino'])
  observed=r['ID_observado']
  if observed:
   c=observed['indice'];z=Path(c['cache']).read_bytes();assert SHA(z)==c['sha256_cache'];raw=gzip.decompress(z);assert SHA(raw)==c['sha256_fonte'];doc=html.fromstring(raw.decode('utf8'));cards=doc.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," kt-widget5__item ")]');matches=[e for e in cards if any(re.search(r'(?:[?&])id='+re.escape(observed['id'])+r'(?:&|$)',x) for x in e.xpath('.//a/@href'))];assert len(matches)==1;assert any(r['arquivo_observado'].endswith(x) for x in matches[0].xpath('.//a/@href') if x.startswith('/Arquivo/'));assert '-id'+observed['id']+'.md' in r['destino']
  else:assert '-fonte'+r['sha256_fonte_original'][:12]+'.md' in r['destino']
  proof.append(dict(origem=r['origem'],destino=r['destino'],sha256_candidato=SHA(actual),corpo_inclusive_H1_preservado=True,ID_observado=observed['id'] if observed else None))
 out=dict(total=16,normas_novas=0,alteracoes='somente fonte/ementa/situacao/revogada',reparos=proof);Path(a.saida).open('x').write(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(total=len(proof),falhas=0,normas_novas=0)))
if __name__=='__main__':main()
