# Gorev 030: Etsy magaza dondurma (frozen) durumu - SADECE OKUMA

Gorev 029'da ilan olusturma "frozen shop" nedeniyle 403 verdi. Hicbir sey olusturma/degistirme/silme YAPMA, sirlari yazdirma.
1. GET /shops/59811467 ve /users/me: tum alanlari oku (state/is_vacation/is_shop_us_based/announcement/sale_message/listing_active_count vb.). Dondurma nedenine dair her alani (varsa) ozetle.
2. GET /shops/59811467/listings?state=active|draft|inactive|expired ve sayilari ver.
3. Payment account / seller onboarding / verification ile ilgili okunabilen endpoint varsa (ornegin /shops/{id}/payment-account-ledger-entries veya benzeri) yalnizca oku; 403/404 olanlari belirt.
4. Etsy genelde dondurmayi kimlik/odeme dogrulamasi, vergi bilgisi, politika ihlali veya hesap guvenligi nedeniyle yapar; API bunu vermiyorsa bunu acikca yaz.
5. Telegram'a en fazla 8 satirlik ozet: durum alanlari, neden bilgisi var mi, Muhammet'in tabletten Etsy'de nereye dokunup bakacagi (Shop Manager ana ekrandaki uyari/bildirim ve Yardim > Destek ile iletisim) kisaca.
Exit 0 ile bit.
