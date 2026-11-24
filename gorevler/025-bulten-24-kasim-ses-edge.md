# Gorev 025: 24 Kasim bulten sesleri (edge-tts, ACIL, Gemini YOK)

Metinler: `gorevler/ref/mark_24.txt` (Mark) ve `gorevler/ref/muhammet_24.txt` (Muhammet). Metni DEGISTIRME.
1. edge-tts (~/mp2/venv, 023'te calisti) ile uret, HIZ/ATEMPO UYGULAMA (rate +0%):
   - Mark: tr-TR-AhmetNeural, pitch +0Hz -> mark.mp3
   - Muhammet: tr-TR-AhmetNeural, pitch -15Hz (Mark'tan ayirt edilsin diye), rate +0% -> muhammet.mp3
2. Her ses icin kelime sinirlari (edge-tts --write-subtitles .vtt veya WordBoundary) cikar: mark.vtt, muhammet.vtt.
3. Uzun metni parcalara bolmen gerekirse cumle sinirindan bol; sonuc tek mp3 olsun, mp3'lerde 1.5 sn'den uzun sessizlik varsa kirp (0.4 sn'ye indir).
4. mark.mp3, muhammet.mp3, mark.vtt, muhammet.vtt dosyalarini `ciktilar` dalina `bulten/2026-11-24/` altina push et (force yok; git kimligi icin gecici -c user.name=isgpro-ajan). Push BASARILI olduktan SONRA Telegram'a "bulten sesleri hazir (24 Kasim)" yaz, once degil.
5. Hata olursa exit 1. Gemini'ye istek atma.
