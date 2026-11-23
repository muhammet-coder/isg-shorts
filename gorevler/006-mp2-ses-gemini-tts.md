# Görev 006: mp2 sesi için Gemini TTS (ElevenLabs kredisi bitti, edge-tts kurulamadı)

Kapsam: ~/mp2 ve shorts_mp2.py. Diğer her şeye DOKUNMA. Anahtarı asla yazdırma. pip/get-pip ve sistem paketi kurma girişimi YAPMA (izin reddedildi); sadece Python standart kütüphanesi (urllib, json, base64, wave) ve ffmpeg kullan.

DURUM (001-004 raporundan): şablon kart videosu üretiliyor, mevzuat doğrulaması tamam. Ses engeli: ElevenLabs 401 quota_exceeded, edge-tts kurulamadı. Gemini görsel üretimi ücretsiz katmanda 429 (görsel şablon kartlarla devam, faturalandırma açılmayacak).

YAPILACAK:
1. Gemini TTS'i REST ile çağır (pip gerekmez): POST https://generativelanguage.googleapis.com/v1beta/models/MODEL:generateContent, header x-goog-api-key (anahtar ~/mp2/.env veya ~/isgpro/.env), gövde: contents[0].parts[0].text = okunacak metin, generationConfig.responseModalities=["AUDIO"], generationConfig.speechConfig.voiceConfig.prebuiltVoiceConfig.voiceName=<ses>. MODEL: gemini-2.5-flash-preview-tts, 404 ise güncel gemini-*-tts adını ListModels (GET /v1beta/models) ile bul. Yanıt: candidates[0].content.parts[0].inlineData.data base64 PCM (16-bit, 24 kHz, mono); wave ile WAV yaz, ffmpeg ile 44100 Hz mono mp3'e çevir. Metne "Türkçe, sakin, net bir haber sunucusu gibi oku:" ön cümlesi ekleme; stil gerekiyorsa metnin dışında prompt'ta ver ve okunan metnin AYNEN okunduğunu doğrula.
2. 429 gelirse 20-60 sn bekleyip en çok 3 kez dene; kısa metinleri (cümle grubu başına <=400 karakter) ayrı istekle üret ve ffmpeg ile birleştir.
3. shorts_mp2.py ses sırası: (a) Gemini TTS, (b) ELEVENLABS_API_KEY varsa ve kredi varsa ElevenLabs, (c) hiçbiri çalışmazsa videoyu SESSİZ GÖNDERME, Telegram'a hata raporu yaz. Sahne süreleri ve altyazılar ses dosyasının gerçek süresinden (ffprobe) çıksın.
4. Mevcut test konusuyla (KKD yönetmeliği) sesli, şablon kartlı videoyu yeniden üret (1080x1920, üstte turuncu İSG-PRO.COM şeridi, sahne <=4 sn, filigransız); ffprobe ile ses akışı olduğunu doğrula; Telegram'a gönder (başlık <=100 karakter / açıklama (https://isg-pro.com) / etiketler ayrı mesajlarda).
5. Rapor: hangi model/ses, kota durumu, çıktı süresi, ses akışı var mı. 005'i (PKD seslendirmesi) bununla aynı TTS kodunu kullanarak yap; ikisi için ortak fonksiyon yaz.
