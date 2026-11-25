#!/usr/bin/env python3
"""Etsy OAuth2 (PKCE) tek seferlik yetkilendirme. Anahtarlar ~/.etsy.env, token ~/.etsy_token.json (chmod 600)."""
import os, sys, json, base64, hashlib, secrets, getpass, urllib.parse, urllib.request
HOME = os.path.expanduser("~")
ENV = os.path.join(HOME, ".etsy.env"); TOK = os.path.join(HOME, ".etsy_token.json"); ST = os.path.join(HOME, ".etsy_pkce.json")
REDIRECT = "https://isg-pro.com/etsy-callback"
SCOPE = "listings_r listings_w listings_d shops_r shops_w transactions_r"
def env():
    d = {}
    for l in open(ENV):
        if "=" in l:
            k, v = l.strip().split("=", 1); d[k] = v
    return d
def b64(b): return base64.urlsafe_b64encode(b).rstrip(b"=").decode()
def start():
    e = env(); ver = b64(secrets.token_bytes(48)); state = secrets.token_urlsafe(12)
    ch = b64(hashlib.sha256(ver.encode()).digest())
    fd = os.open(ST, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f: json.dump({"v": ver, "s": state}, f)
    q = urllib.parse.urlencode({"response_type": "code", "redirect_uri": REDIRECT, "scope": SCOPE,
        "client_id": e["ETSY_KEYSTRING"], "state": state, "code_challenge": ch, "code_challenge_method": "S256"})
    print("\nBu bağlantıyı tarayıcıda aç, Etsy'de 'Erişime izin ver'e bas:\n")
    print("https://www.etsy.com/oauth/connect?" + q + "\n")
def finish():
    e = env(); st = json.load(open(ST))
    raw = getpass.getpass("Açılan sayfanın adres çubuğundaki tüm adresi yapıştır (görünmez): ").strip()
    qs = urllib.parse.parse_qs(urllib.parse.urlparse(raw).query)
    code = qs.get("code", [""])[0]
    if not code or qs.get("state", [""])[0] != st["s"]:
        sys.exit("Kod veya state uyuşmadı. Baştan başlat: python3 etsy/etsy_auth.py")
    data = urllib.parse.urlencode({"grant_type": "authorization_code", "client_id": e["ETSY_KEYSTRING"],
        "redirect_uri": REDIRECT, "code": code, "code_verifier": st["v"]}).encode()
    r = urllib.request.urlopen(urllib.request.Request("https://api.etsy.com/v3/public/oauth/token", data=data))
    t = json.load(r)
    fd = os.open(TOK, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f: json.dump(t, f)
    os.remove(ST)
    print("TAMAM: token kaydedildi (", TOK, ") — süre", t.get("expires_in"), "sn; yenileme anahtarı var:", bool(t.get("refresh_token")))
if __name__ == "__main__":
    start() if len(sys.argv) < 2 or sys.argv[1] == "start" else finish()
