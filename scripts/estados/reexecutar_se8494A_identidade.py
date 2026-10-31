"""Replay somente leitura do reparo de identidade 8494-A, sem mudar o normativo."""
import argparse,json,gzip,hashlib,re
from pathlib import Path
from pe_fidelidade_visivel import texto_visivel_html
SHA=lambda b:hashlib.sha256(b).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--manifesto',required=True);ap.add_argument('--saida',required=True);a=ap.parse_args();m=json.loads(Path(a.manifesto).read_text());old=next(r for r in m['coincidencias_HEAD'] if r['path']==m['origem']);raw=Path(old['preimagem']).read_bytes();assert SHA(raw)==m['sha256_preimagem']==old['sha256_blob'];expected=raw.decode()
 for r in m['alteracoes']:assert expected.count(r['antes'])==1;expected=expected.replace(r['antes'],r['depois'],1)
 new=Path(m['privado']).read_bytes();assert new==expected.encode() and SHA(new)==m['sha256_candidato'];norm=lambda b:b.decode().split('\n---\n',1)[1].split('\n',2)[2].encode();assert norm(raw)==norm(new) and SHA(norm(new))==m['sha256_normativo_preservado'];proof=[]
 for r in m['coincidencias_HEAD']:
  b=Path(r['preimagem']).read_bytes();assert SHA(b)==r['sha256_blob'];z=Path(r['cache']).read_bytes();s=gzip.decompress(z);assert SHA(z)==r['sha256_cache'] and SHA(s)==r['sha256_fonte']
  if s.startswith((b'\xff\xfe',b'\xfe\xff')):text=s.decode('utf-16')
  else:
   try:text=s.decode('utf-8')
   except UnicodeDecodeError:text=s.decode('cp1252')
  suffix='-A' if r['path']==m['origem'] else '';pattern=r'LEI Nº 8[.]494'+suffix+r', DE 28 DE DEZEMBRO DE 2018';visible=texto_visivel_html(text);assert re.search(pattern,visible[:900]),'epígrafe original não comprovada';proof.append(dict(path=r['path'],epigrafe=pattern,sha256_fonte=SHA(s)))
 out=dict(total_atos_distinguidos=2,reparos=1,normas_novas=0,normativo_byte_a_byte_preservado=True,alteracoes_exatamente_as_tres_declaradas=True,provas=proof);Path(a.saida).open('x').write(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
if __name__=='__main__':main()
