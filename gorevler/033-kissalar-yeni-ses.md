# Gorev 033: Kissalar ajani artik ElevenLabs'siz, edge-tts sesiyle calissin; bugunku (25 Kasim) kissayi uret

DOKUNMA: shorts, bulten, mail, LinkedIn, Etsy ve diger gorevler. Sadece ~/kissalar.
ElevenLabs IPTAL edildi (kredi/abonelik YOK, acma). Gemini TTS KULLANMA.
1) ~/kissalar icinde ses uretimi hangi dosya/betikte ElevenLabs'e bagliysa, kalici olarak edge-tts'e cevir (~/mp2/venv, tr-TR-AhmetNeural, pitch -15Hz, rate +0%; HIZ/ATEMPO UYGULAMA, agir cekim olmasin). Cron satiri ve .env'deki ElevenLabs anahtarina artik bagimli kalma; hata yutma, ses uretilemezse exit 1 ve Telegram'a sebep yaz.
2) Cron 08:00 TRT'de her gun duzenli calissin; 24 ve 25 Kasim kosularinin neden atladigini log'dan tek satir yaz.
3) Bugunku kissayi hemen uret (defterde islenmemis, yeni bir Kuran kissasi; tekrar etme). Kurallar aynen: peygamber/melek/sahabe yuzu ASLA gosterilmez; tek videoda biten bagimsiz mini hikaye; sahne istemleri Turkce; kodla (SVG) cizim; ayet/hadis sadece dogrulanmis kaynaktan, emin degilsen yazma.
4) Paketi her zamanki gibi Telegram'a gonder, mesaja "yeni ses: edge-tts" yaz.
