# Gorev 029: Etsy'ye 3 TASLAK ilan yukle (YAYINLAMA YOK)

Hazir: etsy/ilan/agent.py + etsy/ilan/ilanlar.json + etsy/ilan/dosyalar/ (3 PDF/gorsel paketi: sc, hr, bd). Once `git pull` ile repoyu guncelle. Anahtar/token ~/.etsy.env ve ~/.etsy_token.json (etsy/etsy_api.py ile otomatik yenilenir); SIRLARI ASLA yazdirma/loglama/commit/Telegram.
Magaza: shop_id 59811467 (Celikelstore), para birimi TRY, taxonomy 1874 (Templates). Fiyatlar TRY: sc 249, hr 249, bd 399 (agent.py icinde).
1. `cd` repo/etsy/ilan && `python3 agent.py yukle` calistir (ilanlar tek tek TASLAK (draft) olusturulur, 4 gorsel + PDF dosyalari yuklenir, yuklenen.json'a yazilir; tekrar calistirmada zaten yuklenenleri atlar). Iade politikasi yoksa agent.py bunu "iade yok" olarak olusturmayi dener; olusmazsa devam eder.
2. Hata olursa (kod+govde, sirsiz) Telegram'a yaz; token hatasi (401) ise tek kez yeniden dene; baska hata icin hangi adimda kaldigini (ilan id, hangi gorsel/dosya) yaz. Yarim kalan ilani SILME, yenisini de acma; yuklenen.json'u koru.
3. Bitince her taslak icin listing_id, baslik, fiyat, yuklenen gorsel/dosya sayisini ve durum="draft" oldugunu GET /shops/{sid}/listings?state=draft ile dogrulayip Telegram'a 8 satirlik ozet yaz. Ilan SAYISI: tam 3 olmali; fazlaysa/azsa belirt.
YASAK: ilani yayinlama (state=active yapma), silme, fiyat/baslik degistirme (agent.py disinda), baska dosyaya dokunma.
exit 0 ile bitir; hata olsa da nedenini Telegram'a yaz.
