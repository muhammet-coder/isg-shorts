# Gorev 027: Etsy API baglanti testi (SADECE OKUMA)

Etsy API baglandi. Anahtarlar ~/.etsy.env, token ~/.etsy_token.json (SIRLARI ASLA YAZDIRMA, Telegram'a/ciktiya/commit'e koyma). Yardimci: etsy/etsy_api.py (call(method, path, body/form), token yenilemeyi kendisi yapar).
Bu gorev HICBIR sey olusturma/degistirme/silme YAPMAZ. Yalnizca oku:
1. `GET /openapi-ping` benzeri yerine once `GET /v3/application/users/me` (call("GET","/users/me")): user_id ve shop_id al. Hata olursa (401/403) hata kodunu ve govdesini (sirsiz) raporla, token'i yenilemeyi dene, olmazsa dur.
2. `GET /shops/{shop_id}`: magaza adi, para birimi (currency_code), listing_active_count, ulke. Para birimini ozellikle bildir.
3. `GET /shops/{shop_id}/listings?state=active&limit=10` ve state=draft: sayilari ve baslik/ID/fiyat ozetini ver (eski e-kitap ilanlari var mi).
4. `GET /seller-taxonomy/nodes`: "Digital"/"Templates"/"Documents" benzeri dijital belge kategorisinin taxonomy_id'sini bul ve listele (en uygun 3 aday).
5. `GET /shops/{shop_id}/shipping-profiles` ve `/shops/{shop_id}/return-policies`: dijital urun icin gerekli profil/politika var mi, ID'leri ver.
6. Sonuc: gorevler degil, `ciktilar` dalina etsy/durum.md olarak yaz (sirsiz), Telegram'a 10 satirlik ozet gonder: user/shop id, para birimi, mevcut ilan sayisi, aday taxonomy_id'ler, eksikler (ornegin kargo profili/iade politikasi yoksa belirt).
Not: Kisisel erisim anahtari yalnizca kendi magazamiza erisir; bu normal. Calistirma exit 0 ile bitmeli; hata olsa bile Telegram'a nedenini yaz.
