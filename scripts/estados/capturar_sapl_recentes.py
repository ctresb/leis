"""Inventário serial recente SAPL; preserva respostas e nunca cria MD."""
import datetime,gzip,hashlib,json,re,time,urllib.request,urllib.error
from pathlib import Path
from zoneinfo import ZoneInfo
HOSTS={'AM':'sapl.al.am.leg.br','PB':'sapl.al.pb.leg.br','AL':'sapl.al.al.leg.br','RR':'sapl.al.rr.leg.br','AC':'sapl.al.ac.leg.br','RO':'sapl.al.ro.leg.br','PI':'sapl.al.pi.leg.br','TO':'sapl.al.to.leg.br'}
SHA=lambda b:hashlib.sha256(b).hexdigest()

def main():
    manifests=[]
    for uf,host in HOSTS.items():
        base=Path('estaduais')/uf/'_indice/retomada-recente-20261021-001'
        if base.exists():raise ValueError('Captura já existe: '+str(base))
        base.mkdir(parents=True);baseline=Path('estaduais')/uf/'_indice/sapl.json';old=json.loads(baseline.read_text());ids={int(m[1]) for p in (Path('estaduais')/uf).glob('*/*/*.md') if (m:=re.search(r'-id(\d+)\.md$',p.name))};page=1;rows=[];receipts=[];seen=set();bad=0
        while True:
            url=f'https://{host}/api/norma/normajuridica/?data__gte=2026-10-13&data__lte=2026-10-21&page_size=100&page={page}';r=dict(url=url,iniciado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat())
            try:
                with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; legislative archive)','Accept':'application/json'}),timeout=40) as resp:st=resp.status;b=resp.read();headers=dict(resp.headers)
            except urllib.error.HTTPError as e:st=e.code;b=e.read();headers=dict(e.headers)
            except Exception as e:r['erro']=type(e).__name__+': '+str(e);receipts.append(r);break
            cache=base/(f'pagina{page}.json.gz');cache.write_bytes(gzip.compress(b));r.update(http=st,headers=headers,cache=str(cache),sha256_fonte=SHA(b),finalizado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat());receipts.append(r);print(uf,page,st,len(b),flush=True)
            if st!=200:break
            d=json.loads(b)
            for it in d['results']:
                if not '2026-10-13' <= (it.get('data') or '') <= '2026-10-21':raise ValueError('API não aplicou intervalo documental; não paginar')
                if it['id'] in seen:raise ValueError('ID repetido na paginação')
                seen.add(it['id']);rows.append(dict(item=it,ID_ja_no_disco=it['id'] in ids,tipo_indice=old['tipos'].get(str(it['tipo'])),arquivo_publico=bool(it.get('texto_integral'))))
            if not d['pagination'].get('next_page'):break
            page=int(d['pagination']['next_page']);time.sleep(1.2)
        manifests.append(dict(UF=uf,capturas=receipts,sha256_indice_anterior=SHA(baseline.read_bytes()),total_resultados=len(rows),candidatos_novos_com_anexo=[r for r in rows if not r['ID_ja_no_disco'] and r['tipo_indice'] and r['arquivo_publico']],novos_sem_anexo=[r for r in rows if not r['ID_ja_no_disco'] and r['tipo_indice'] and not r['arquivo_publico']],todos=rows));time.sleep(1.2)
    Path('scripts/estados/manifestos/sapl-indice-recente-20261021-001.json').write_text(json.dumps(dict(capturado_em=datetime.datetime.now(ZoneInfo('America/Recife')).isoformat(),intervalo=['2026-10-13','2026-10-21'],sem_MD=True,UFs=manifests),ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
