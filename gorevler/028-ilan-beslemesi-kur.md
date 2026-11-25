# Gorev 028: Is ilanlari beslemesini KUR (016'nin devami; ILAN_ANAHTARI artik ~/.env icinde)

016'daki hedef/kurallar aynen gecerli (gorevler/016-site-yukleme-botu-tasima.md oku). 016 anahtar eksik oldugu icin kurulamadi; anahtar simdi ~/.env icinde (ILAN_ANAHTARI=...). Degerini ASLA yazdirma/loglama/commit etme/Telegram'a yazma.
Yapilacaklar:
1. ~/.env icinde ILAN_ANAHTARI var mi kontrol et (sadece degisken adini dogrula). Yoksa tek satir Telegram mesaji yaz ve DUR.
2. Bot token ve chat id ~/isgpro/.env icinde (TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID); degerleri yazdirma. Betik: ~/ilan-besleme/besle.py (python3, sadece stdlib). Bot: @isgpro_asistan_bot. Telegram getUpdates ile offset dosyasi tutarak oku (~/ilan-besleme/offset.txt); baska bir getUpdates tuketicisi/webhook varsa (getWebhookInfo bak) CAKISMA yaratma: webhook varsa silme, once Telegram'a bildir ve dur.
3. Her update icin sadece from.id == 821197798 ve chat.type == "private" olanlari, metin/caption'i al, update'i oldugu gibi (message govdesi) POST https://isg-pro.com/api/ilan-telegram , header x-ilan-anahtari: ILAN_ANAHTARI (~/.env'den oku). Yanit "atlandi" ise Telegram'a "atlandi: <neden>", basarili ise "ilan eklendi: <adres>" yaz. Ayni update_id'yi iki kez isleme.
4. Ilk calismada son 24 saatteki bekleyen mesajlari isle; sonra crontab'a her 5 dakikada bir calisan satir ekle (mevcut cron satirlarini BOZMA/silme, yalnizca ekle; once crontab -l yedegini ~/ilan-besleme/crontab.yedek'e al).
5. Bitince Telegram'a "ilan beslemesi hazir: ilan metnini bota ilet" yaz. Hata olursa tek mesaj, en fazla 2 deneme.
KISITLAR: isg-pro.com (Radore) sunucusuna baglanma; isg-pro-app deposuna push etme; diger gorevlere dokunma; silme yasagina uy; exit 0 ile bitir (hata olsa da nedenini Telegram'a yaz).
