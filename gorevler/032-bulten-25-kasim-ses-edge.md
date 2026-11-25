# Gorev 032: 25 Kasim bulten sesleri (edge-tts, ElevenLabs YOK, Gemini YOK)

Metinler: `gorevler/ref/mark_25.txt` (Mark) ve `gorevler/ref/muhammet_25.txt` (Muhammet). Metni DEGISTIRME.
Gorev 025'in yontemiyle birebir ayni (edge-tts, ~/mp2/venv, HIZ/ATEMPO UYGULAMA, rate +0%):
1. Mark: tr-TR-AhmetNeural, pitch +0Hz -> mark.mp3. Muhammet: tr-TR-AhmetNeural, pitch -15Hz -> muhammet.mp3.
2. Her ses icin kelime sinirlari: mark.vtt, muhammet.vtt.
3. Uzun metin gerekirse cumle sinirindan bolunur, sonuc tek mp3; 1.5 sn'den uzun sessizlik varsa 0.4 sn'ye indir.
4. mark.mp3, muhammet.mp3, mark.vtt, muhammet.vtt dosyalarini `ciktilar` dalina `bulten/2026-11-25/` altina push et (force yok; -c user.name=isgpro-ajan). Push basarili olduktan SONRA Telegram'a "bulten sesleri hazir (25 Kasim)" yaz.
5. Hata olursa exit 1.
