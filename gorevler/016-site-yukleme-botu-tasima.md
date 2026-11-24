# Gorev 016: Site guncelleme akisini yeni ajana tasi (eski "Claude bot" suresi bitti)
DURUM: Muhammet site guncellemelerini (zip) bir Telegram botuna atiyordu; o bot (ucretli surumde kurulmustu) yayinliyordu, aboneligi bitti. Dunku "is ilanlari" sayfasi bu yuzden yayinlanmadi (GitHub muhammet-coder/isg-pro-app deposuna 23 Kasim'dan beri commit yok). Site sunucusunda (Radore) surum d8f9659 = depodaki seo-guncelleme-v88 dali ucu; sunucu bu daldan guncelleniyor (Sitekontrol/n8n akisi, SEN ORAYA BAGLANMA).
HEDEF: Muhammet @isgpro_asistan_bot'a (ya da Telegram'a) site zip'i atinca sen: indir, gecici klasorde ac, icerik ozetini cikar (hangi dosyalar yeni/degisti), mevcut isg-pro-app seo-guncelleme-v88 dali uzerine uygula (silme yok, sadece ekle/guncelle), tek commit yap, ayni dala push et, Telegram'a "yuklendi: <commit>, sunucu ~5 dk icinde guncellenir" yaz. 
ADIMLAR:
1) Once ~/isgpro altinda Telegram'dan zip indirme betigi var mi bak (telegram-video-indir.sh benzeri); zip icin uyarla.
2) isg-pro-app deposuna bu sunucudan push yetkisi (deploy key/token) var mi kontrol et. YOKSA: dur, Muhammet'e Telegram'da tek satirla ne gerektigini yaz (token'i sohbete yazdirma, read -rsp ile .env'e girilecek).
3) Calismazsa hata Telegram'a gitsin; sessizce bozma. Silme/force-push YASAK. main dalina dokunma, sadece seo-guncelleme-v88.
4) Muhammet'in dunku is ilanlari zip'i bu bota atilmadiysa Telegram'da "zip'i bana at" diye hatirlat.
KISITLAR: Radore sunucusuna baglanma; 013 (bulten sesi), 014 (kissalar) gorevlerine dokunma. Anahtarlari yazdirma.
