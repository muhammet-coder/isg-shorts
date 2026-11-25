#!/usr/bin/env python3
"""ISG-PRO Etsy ilan ajani. Kullanim: agent.py giris | yukle | durum"""
import json,os,sys,time,base64,hashlib,secrets,getpass,mimetypes,urllib.request,urllib.parse,urllib.error
H=os.path.dirname(os.path.abspath(__file__)); CFG=os.path.expanduser("~/.etsy-ajan.json")
sys.path.insert(0,os.path.join(H,".."))
import etsy_api
SHOP=59811467; TAX=1874
TRY={"sc":"249","hr":"249","bd":"399"}
REDIR="http://localhost:3003/callback"; API="https://api.etsy.com/v3"
def load():
    try: return json.load(open(CFG))
    except Exception: return {}
def save(c):
    json.dump(c,open(CFG,"w")); os.chmod(CFG,0o600)
def req(method,url,c,data=None,files=None,auth=True,form=None):
    hdr={"x-api-key":c["key"]+(":"+c["secret"] if c.get("secret") else "")}
    if auth: hdr["Authorization"]="Bearer "+c["access"]
    body=None
    if form is not None: body=urllib.parse.urlencode(form,doseq=True).encode(); hdr["Content-Type"]="application/x-www-form-urlencoded"
    if files:
        b="----"+secrets.token_hex(8); parts=[]
        for k,v in (data or {}).items(): parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
        for k,(fn,raw) in files.items():
            ct=mimetypes.guess_type(fn)[0] or "application/octet-stream"
            parts.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{fn}"\r\nContent-Type: {ct}\r\n\r\n'.encode()+raw+b"\r\n")
        body=b"".join(parts)+f"--{b}--\r\n".encode(); hdr["Content-Type"]="multipart/form-data; boundary="+b
    r=urllib.request.Request(url,data=body,headers=hdr,method=method)
    try:
        with urllib.request.urlopen(r,timeout=120) as f: t=f.read().decode(); return json.loads(t) if t else {}
    except urllib.error.HTTPError as e:
        print("HATA",e.code,url,e.read().decode()[:400]); raise SystemExit(1)
def token(c,form):
    r=urllib.request.Request(API+"/public/oauth/token",data=urllib.parse.urlencode(form).encode(),method="POST")
    try:
        with urllib.request.urlopen(r,timeout=60) as f: return json.loads(f.read())
    except urllib.error.HTTPError as e:
        print("TOKEN HATA",e.code,e.read().decode()[:300]); raise SystemExit(1)
def giris():
    c=load()
    if not c.get("key"): c["key"]=getpass.getpass("Etsy keystring (gizli): ").strip()
    if not c.get("secret"): c["secret"]=getpass.getpass("Shared secret (gizli, yoksa bos birak): ").strip()
    ver=secrets.token_urlsafe(48); ch=base64.urlsafe_b64encode(hashlib.sha256(ver.encode()).digest()).rstrip(b"=").decode(); st=secrets.token_urlsafe(8)
    u="https://www.etsy.com/oauth/connect?"+urllib.parse.urlencode(dict(response_type="code",client_id=c["key"],redirect_uri=REDIR,scope="listings_w listings_r shops_r",state=st,code_challenge=ch,code_challenge_method="S256"))
    print("\nTabletten bu adresi ac, Etsy'de 'Erisime izin ver' de:\n\n"+u+"\n")
    print("Sayfa acilmaz (localhost hatasi) ama adres cubugunda 'code=' gorunur.")
    p=urllib.parse.urlparse(input("Adres cubugundaki TUM adresi buraya yapistir: ").strip()); q=urllib.parse.parse_qs(p.query)
    assert q.get("state",[""])[0]==st,"state uyusmadi"
    t=token(c,dict(grant_type="authorization_code",client_id=c["key"],redirect_uri=REDIR,code=q["code"][0],code_verifier=ver))
    c.update(access=t["access_token"],refresh=t["refresh_token"],exp=time.time()+t["expires_in"]-60); save(c); print("GIRIS TAMAM")
def hazir():
    e=etsy_api._env(); return {"key":e["ETSY_KEYSTRING"],"secret":e.get("ETSY_SHARED_SECRET",""),"access":etsy_api.token()}
def shop(c): return SHOP
def taxo(c): return TAX
def iade(c,sid):
    try:
        r=req("GET",f"{API}/application/shops/{sid}/policies/return",c); print("iade politikasi var"); return
    except SystemExit: pass
    try:
        r=req("POST",f"{API}/application/shops/{sid}/policies/return",c,form=dict(accepts_returns="false",accepts_exchanges="false")); print("iade politikasi olusturuldu (iade yok)")
    except SystemExit: print("iade politikasi olusturulamadi (dijital ilan icin gerekmeyebilir), devam")
def yukle():
    c=hazir(); sid=shop(c); tx=taxo(c); iade(c,sid)
    st=json.load(open(os.path.join(H,"yuklenen.json"))) if os.path.exists(os.path.join(H,"yuklenen.json")) else {}
    for L in json.load(open(os.path.join(H,"ilanlar.json"))):
        if L["id"] in st: print(L["id"],"zaten yuklendi"); continue
        r=req("POST",f"{API}/application/shops/{sid}/listings",c,form=dict(quantity=999,title=L["title"],description=L["description"],price=TRY[L["id"]],who_made="i_did",when_made="2020_2026",taxonomy_id=tx,type="download",tags=",".join(L["tags"]) if isinstance(L["tags"],list) else L["tags"],is_supply="false"))
        lid=r["listing_id"]; print(L["id"],"taslak olustu",lid)
        for n,im in enumerate(L["images"],1):
            raw=open(os.path.join(H,"dosyalar",im),"rb").read(); req("POST",f"{API}/application/shops/{sid}/listings/{lid}/images",c,data={"rank":n},files={"image":(im,raw)})
        for f in L["files"]:
            raw=open(os.path.join(H,"dosyalar",f),"rb").read(); req("POST",f"{API}/application/shops/{sid}/listings/{lid}/files",c,data={"name":f},files={"file":(f,raw)})
        st[L["id"]]=lid; json.dump(st,open(os.path.join(H,"yuklenen.json"),"w")); print(L["id"],"resim+dosya TAMAM")
    print("\nTaslaklar hazir. Etsy > Listings > Drafts bolumunden kontrol edip yayinla.")
{"yukle":yukle,"durum":lambda:print(load().get("shop_name"),bool(load().get("refresh")))}.get(sys.argv[1] if len(sys.argv)>1 else "",lambda:print(__doc__))()
