# GÖREV: MoneyPrinterV2 mantığıyla İSG-PRO video üretim hattı (shorts_mp2.py)

Yayını Muhammet elle yapacak. YouTube'a yükleme YOK.

## Yapma (dokunma)
- MoneyPrinterV2'nin YouTube yükleme (Selenium/Firefox), Twitter botu, ortaklık pazarlaması ve Google Maps soğuk e-posta modüllerini kurma/çalıştırma/ayarlama.
- Mevcut cron satırları, shorts_hf.py, kuyruk/yayıncı betikleri ve ~/kissalar akışı.
- Lisans AGPL-3.0: MoneyPrinterV2 kodunu kopyalama; fikri/akışı kendi kodumuzla yaz.

## Yap
1. https://github.com/FujiwaraChoki/MoneyPrinterV2 deposunu ~/mp2 altına klonla; README ve src'yi oku; yalnız video üretim akışını (konu -> senaryo -> sahne görseli -> ses -> altyazı -> birleştirme) anla.
2. shorts_mp2.py yaz (bu depoda, mp2-gorev dalında; main'e birleştirme):
   - Girdi: konu cümlesi.
   - Senaryo: Claude ile yaz; mevzuatı sunucudaki kaynaklar/ metniyle doğrula, doğrulanamazsa konuyu atla.
   - Görsel: GEMINI_API_KEY varsa Gemini; yoksa sablon/ görselleri + HyperFrames animasyonu.
   - Ses: ElevenLabs kredisi yoksa/hata verirse edge-tts tr-TR-AhmetNeural; kredi varsa Adam (voice_id J17lijyP1BHYcM7ld0Rg).
   - Çıktı 1080x1920; üstte başından sonuna "İSG-PRO.COM" bandı; gömülü altyazı; içerikte İSG-PRO çözümü (belge isteme, termin takibi, kurulum onayı); bitişte isg-pro.com; YouTube arayüzünün kapattığı alt ve sağ kenar boş.
3. Çıktıyı videolar/mp2/ altına yaz; Telegram'a (telegram-video-gonder.sh) gönder: video, ardından başlık (en fazla 100 karakter), açıklama (https://isg-pro.com dahil), etiketler, üçü AYRI mesaj.
4. Deneme: konu "İskelede korkuluk ve yaşam hattı kontrolü".
5. Sırları sohbete yazma. Bitince Telegram'a kısa rapor: ne kuruldu, hangi ses/görsel yolu, deneme videosu, hata varsa ne yapıldı. Soru sorma, en makul seçeneği seç ve raporda belirt.
