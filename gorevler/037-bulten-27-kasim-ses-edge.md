# Gorev 037: 27 Kasim bulten sesleri (edge-tts, ElevenLabs YOK, Gemini YOK)

Metinler: `gorevler/ref/mark_27.txt` (Mark) ve `gorevler/ref/muhammet_27.txt` (Muhammet). Metni DEGISTIRME.
Gorev 032'nin yontemiyle birebir ayni (edge-tts, ~/mp2/venv, HIZ/ATEMPO UYGULAMA, rate +0%):
1. Mark: tr-TR-AhmetNeural, pitch +0Hz -> mark.mp3. Muhammet: tr-TR-AhmetNeural, pitch -15Hz -> muhammet.mp3.
2. Her ses icin kelime sinirlari: mark.vtt, muhammet.vtt.
3. Uzun metin gerekirse cumle sinirindan bolunur, sonuc tek mp3; 1.5 sn'den uzun sessizlik varsa 0.4 sn'ye indir.
4. mark.mp3, muhammet.mp3, mark.vtt, muhammet.vtt dosyalarini `ciktilar` dalina `bulten/2026-11-27/` altina push et (force yok; -c user.name=isgpro-ajan -c user.email=ajan@isg-pro.com). Push basarili olduktan SONRA Telegram'a "bulten sesleri hazir (27 Kasim)" yaz.
5. Telegram mesajini SADECE push dogrulandiktan sonra gonder (&& ile bagla). Hata olursa exit 1.
