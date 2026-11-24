# Gorev 021: Mark r00-r02 dosyalarini push et (Gemini ISTEGI YOK)

ACIL, kisa is. Gemini'ye HIC istek atma (kota bitti, faturalandirma kapali kalacak).

1. ~/seslendirme/_g020 altindaki yeni Mark parcalarini (r00, r01, r02) HAM (_raw.wav) ve ISLENMIS (atempo/ses duzeltmeli) haliyle, hangisi varsa, `ciktilar` dalina `bulten/2026-11-23/ham/r/` altina push et. Force-push yok, mevcut dosyalarin ustune yazma.
2. Ayni klasore r_bilgi.txt yaz: her parcanin metni, karakter sayisi, ham sure, hece/sn, r02 icindeki sessizligin baslangic-bitis saniyesi.
3. Baska hicbir sey yapma: birlestirme, kirpma, yeni uretim YOK. Ben (Claude) sessizligi kirpip birlestirecegim.
4. Bitince Telegram'a "021 tamam, r dosyalari ciktilar/bulten/2026-11-23/ham/r/ altinda" yaz. Dosyalar bulunamazsa exit 1 ile cik (basarili sayilma).
