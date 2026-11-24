# Gorev 016 (GUNCEL): Site degisiklik taleplerini Telegram mesajiyla alip yayinlayan akis (eski "Claude bot" yerine)
DURUM: Muhammet site degisikliklerini ZIP degil, bir Telegram botuna YAZILI MESAJLA ("su sayfayi ekle/degistir") bildiriyordu; eski Claude tabanli bot bunu isleyip yayinliyordu, aboneligi bitti. Dunku "is ilanlari" talebi bu yuzden yayinlanmadi (GitHub muhammet-coder/isg-pro-app'e 23 Kasim'dan beri commit yok). Site sunucusu (Radore) seo-guncelleme-v88 dalindan otomatik guncelleniyor; SEN ORAYA BAGLANMA, sadece depoya push.
HEDEF: @isgpro_asistan_bot'a gelen mesajlardan "site:" ile baslayanlari (ornek: "site: is ilanlari sayfasi ekle ...") 5 dakikada bir tarayan bir akis kur:
1) Telegram getUpdates ile yeni "site:" mesajlarini oku (offset dosyasi tut, ayni mesaji iki kez isleme; sadece Muhammet'in chat id'sinden gelenleri kabul et).
2) isg-pro-app deposunu (seo-guncelleme-v88 dali) ~/site-calisma altinda klonla/guncelle; talebi `claude -p` ile uygula (var olan sayfa/dizin yapisina uy; yeni sayfa ise menuye/sitemap'e ekle; mevcut icerigi SILME; mevzuat/rakam uydurma, emin degilsen "ornek" diye isaretle).
3) Degisiklikleri kisa ozetle, TEK commit yap, ayni dala push et (force-push YASAK, main'e dokunma). Telegram'a "yuklendi: <commit> - ne eklendi (2 satir); sunucu ~5 dk icinde alir" yaz.
4) Hata/limit olursa Telegram'a tek mesaj; sessizce bozma. Ayni talebi sonsuz deneme: en fazla 2.
5) Depoya push yetkisi (deploy key/token) bu sunucuda yoksa DUR; Telegram'a tek satirla ne gerektigini yaz (anahtari sohbete yazdirma; read -rsp ile .env'e girilecek).
KISITLAR: Radore sunucusuna baglanma; 013 (bulten sesi) ve 014 (kissalar) gorevlerine dokunma; anahtarlari yazdirma.
