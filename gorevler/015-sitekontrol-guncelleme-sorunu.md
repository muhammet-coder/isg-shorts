# Gorev 015: Sitekontrol botu "Guncelleme sorunu" (24 Kasim 10:56) - SADECE TESHIS
Telegram'daki "Sitekontrol" botu 24 Kasim 10:56'da "Guncelleme sorunu" mesaji gonderdi (onceki mesajlar "Site guncellendi TAMAM <eski hash> -> <yeni hash>" idi, son 23:21). 
YAP: Sunucuda bu mesaji gonderen betigi/cron'u bul (Sitekontrol, "Site guncellendi", "Guncelleme sorunu" metinleri icin ~, /etc/cron*, crontab -l, ~/*/ icinde grep). Hangi siteyi/depoyu guncelledigini, 10:56'daki calismanin logunu ve hata nedenini bul (git pull cakismasi, yetki, ag, disk, tarih kontrolu vb.). 
KISITLAR: Hicbir seyi DUZELTME, silme, push/pull, cron degistirme (sadece okuma). Diger gorevlere (013 bulten sesi, 014 kissalar) dokunma.
RAPOR: Telegram'a kisa: hangi site, hata nedeni, site su an eski surumde mi, onerilen duzeltme tek satir. Kok neden belli degilse "belirsiz" yaz.
