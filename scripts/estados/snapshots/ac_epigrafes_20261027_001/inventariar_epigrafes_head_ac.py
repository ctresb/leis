"""Alertas contextuais em blobs integrais. Não corta nem modifica documentos."""
import json,gzip,re,hashlib,subprocess,datetime,html as entities,argparse
from pathlib import Path
ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--saida',required=True);args=ap.parse_args();base=Path(args.saida)
if base.is_absolute() or '..' in base.parts or not str(base).startswith('estaduais/AC/_fonte/auditorias/'):raise ValueError('saída fora do espaço privado AC')
base.mkdir(parents=True,exist_ok=False)
SHA=lambda b:hashlib.sha256(b).hexdigest()
MESES={m:i for i,m in enumerate('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split(),1)}
# A visão de reconhecimento elimina somente delimitadores Markdown/tags e resolve
# entidades. Mantém mapa de posição para citar o trecho original byte-preservado.
def visao(body):
 out=[];pos=[]
 for m in re.finditer(r'<!--[\s\S]*?-->|<[^>]*>|\*\*|__|&(?:#\d+|#x[0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]+);|[\s\S]',body):
  token=m[0]
  if token in ('**','__'):continue
  value=' ' if token.startswith('<') else entities.unescape(token)
  out.append(value);pos.extend([m.start()]*len(value))
 return ''.join(out),pos

def normalnum(n):
 s=re.sub(r'[.\s]','',str(n)).upper();m=re.fullmatch(r'(\d+)(-[A-Z]+)?',s)
 return str(int(m[1]))+(m[2] or '') if m else s

def tipopasta(s):
 t=s.upper()
 if 'COMPLEMENTAR' in t:return 'leis-complementares'
 if 'DELEGADA' in t:return 'leis-delegadas'
 if t.startswith('LEI'):return 'leis-ordinarias'
 if t.startswith('DECRETO'):
  if 'LEGISLATIVO' in t:return 'decretos-legislativos'
  return 'decretos-lei' if t.replace('-',' ').endswith('LEI') else 'decretos'
 if t.startswith(('RESOLUÇÃO','RESOLUCAO')):return 'resolucoes'
 if t.startswith('EMENDA'):return 'emendas-constitucionais'
 return None

RX=re.compile(r'\b(?P<tipo>LEI(?:\s+(?:COMPLEMENTAR|DELEGADA))?|DECRETO(?:[-\s]+LEI|\s+LEGISLATIVO)?|RESOLU[ÇC][ÃA]O|EMENDA(?:\s+[ÀA]\s+CONSTITUI[ÇC][ÃA]O|\s+CONSTITUCIONAL)?)\s+N(?:[.º°o]*|[ÚU]MERO)\s*(?P<num>\d[\d.]*(?:\s*-\s*[A-Z]+)?)\s*,?\s*DE\s+(?:(?P<dia>\d{1,2})[º°]?\s+DE\s+(?P<mes>[A-ZÇ]+)\s+DE\s+(?P<ano>\d{4})|(?P<numeric>\d{1,2}[/.]\d{1,2}[/.]\d{4}))',re.I)
head=subprocess.check_output(['git','rev-parse','HEAD']).decode().strip();tree=subprocess.check_output(['git','ls-tree','-r','-z',head,'--','estaduais/AC/']);(base/'HEAD-ls-tree.z').open('xb').write(tree)
new=json.load(open('estaduais/AC/_fonte/auditorias/legis-triagem-20261027-004/novos.json'));candidate_keys={}
for r in new:candidate_keys.setdefault((r['pasta'],normalnum(r['numero']),r['data']),[]).append(dict(id_LEGIS=r['id_LEGIS'],fonte=r['fonte'],titulo=r['titulo_indice']))
proc=subprocess.Popen(['git','cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE);results=[];allmeta=[];read=0;allhits=0;same=0;proof=[]
for part in tree.split(b'\0'):
 if not part:continue
 h,p=part.split(b'\t',1);path=p.decode('utf-8',errors='strict')
 if not path.endswith('.md') or '/_fonte/' in path:continue
 oid=h.split()[2].decode();proc.stdin.write((oid+'\n').encode());proc.stdin.flush();hdr=proc.stdout.readline().split();assert hdr[:2]==[oid.encode(),b'blob'];blob=proc.stdout.read(int(hdr[2]));assert proc.stdout.read(1)==b'\n';read+=1
 text=blob.decode('utf-8',errors='strict');header,body=text[4:].split('\n---\n',1);bodyoffset=len(text)-len(body);meta={}
 for ln in header.splitlines():
  if ': ' not in ln:continue
  k,v=ln.split(': ',1)
  try:meta[k]=json.loads(v)
  except json.JSONDecodeError:meta[k]=v
 allmeta.append(dict(path=path,oid=oid,sha256_MD=SHA(blob),numero=meta.get('numero'),data=meta.get('data'),tipo=meta.get('tipo')))
 view,positions=visao(body);alerts=[];block_seen=0;firstart=re.search(r'\bArt[.]\s*1',body,re.I);firstart=firstart.start() if firstart else len(body)
 for m in RX.finditer(view):
  allhits+=1
  try:
   if m['numeric']:
    day,month,year=map(int,re.split('[/.]',m['numeric']));date=datetime.date(year,month,day).isoformat()
   else:date=datetime.date(int(m['ano']),MESES[m['mes'].lower()],int(m['dia'])).isoformat()
  except (ValueError,KeyError):continue
  number=normalnum(m['num']);folder=tipopasta(m['tipo'])
  a=positions[m.start()];b=positions[m.end()-1]+1;line=text.count('\n',0,bodyoffset+a)+1;line_start=body.rfind('\n',0,a)+1;prefix=re.sub(r'<[^>]*>|\*\*|__','',body[line_start:a]).strip();kind='epigrafe_de_bloco' if not prefix else 'bloco_com_aspas' if not prefix.strip('“”\"\' ') else 'referencia_no_texto'
  if kind!='referencia_no_texto':block_seen+=1
  own=(folder==tipopasta(str(meta.get('tipo',''))) and number==normalnum(meta.get('numero','')) and date==str(meta.get('data','')))
  if own:same+=1;continue
  role='epigrafe_inicial_divergente_da_metadata' if kind!='referencia_no_texto' and block_seen==1 and a<firstart else 'epigrafe_secundaria_contextual' if kind!='referencia_no_texto' else 'referencia_no_texto'
  hit=dict(tipo_impresso=m['tipo'],numero_impresso=m['num'],numero_comparacao=number,data=date,linha_MD=line,trecho_literal=body[a:b],contexto_literal=body[max(0,a-180):min(len(body),b+420)],classificacao_contextual=kind,papel_estrutural=role,correspondencias_LEGIS=candidate_keys.get((folder,number,date),[]),nota='Alerta de identidade secundária. Citação, anexo incorporado e ato autônomo ainda precisam de contexto; isto não prova duplicação, não autoriza corte/máscara e não altera contagem de normas qualificadas.')
  alerts.append(hit)
 if alerts:
  r=dict(path=path,OID=oid,sha256_MD=SHA(blob),metadata=meta,alertas=alerts);results.append(r)
  if any(a['correspondencias_LEGIS'] for a in alerts):
   p=base/'preimagens'/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(blob);r['preimagem_integral']=str(p)
proc.stdin.close();proc.stdout.close();assert proc.wait()==0
with gzip.open(base/'inventario-blobs-lidos.jsonl.gz','xt',encoding='utf-8') as f:
 for r in allmeta:f.write(json.dumps(r,ensure_ascii=False)+'\n')
(base/'alertas-contextuais.json').open('x').write(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
matched=[dict(path=r['path'],OID=r['OID'],sha256_MD=r['sha256_MD'],preimagem_integral=r.get('preimagem_integral'),alertas=[a for a in r['alertas'] if a['correspondencias_LEGIS']]) for r in results if any(a['correspondencias_LEGIS'] for a in r['alertas'])]
(base/'correspondencias-candidatos-LEGIS.json').open('x').write(json.dumps(matched,ensure_ascii=False,indent=2)+'\n')
summary=dict(preparado_em=datetime.datetime.now().astimezone().isoformat(),HEAD=head,blobs_integrais_lidos=read,ocorrencias_reconhecidas=allhits,identidade_primaria_igual_metadata=same,blobs_com_alertas=len(results),alertas_impressos=sum(len(r['alertas']) for r in results),epigrafes_iniciais_divergentes=sum(a['papel_estrutural']=='epigrafe_inicial_divergente_da_metadata' for r in results for a in r['alertas']),epigrafes_secundarias_de_bloco=sum(a['papel_estrutural']=='epigrafe_secundaria_contextual' for r in results for a in r['alertas']),blobs_com_correspondencia_LEGIS=len(matched),ocorrencias_correspondentes_LEGIS=sum(len(r['alertas']) for r in matched),candidatos_LEGIS_distintos=sorted({a['id_LEGIS'] for r in matched for h in r['alertas'] for a in h['correspondencias_LEGIS']}),sem_corte=True,sem_mascara=True,normas_novas_qualificadas=0,limites='Inventário de alertas em identidades impressas reconhecíveis por data/número; não se declara lista exaustiva de atos autônomos. Citações e anexos não equivalem a duplicação. O caso93/93-A tem prova específica separada. Cabeçalhos iniciais divergentes da metadata não são rotulados como outro ato embutido. Protótipo006 privado preservado; versão007 reconhece N.º e compara a família de tipo impressa com o tipo metadata, evitando chamar a própria resolução de epígrafe secundária.')
(base/'resumo.json').open('x').write(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(summary)
