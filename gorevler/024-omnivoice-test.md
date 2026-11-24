# Gorev 024: OmniVoice (ucretsiz, Apache-2.0, k2-fsa) ile Turkce ses testi

Amac: Gemini kotasi/hiz sorunu olmadan, kotasiz ucretsiz TTS. Muhammet'in ElevenLabs ile begendigi Mark ve Adam seslerini referans alip klonlamak.
1. `pip install omnivoice` (venv icinde; sistemi bozma). Modeli indir. GPU yoksa CPU'da calistir (yaklasik 3 kat yavas, sorun degil). RAM/disk yetmiyorsa nedenini yaz, exit 1.
2. Referans sesler: `gorevler/ref/mark_ref.mp3` (Mark) ve `gorevler/ref/adam_ref.mp3` (Adam). Referans metni (ref_text) yazima donusturme araci yoksa bos birak; Turkce transkript cikarabiliyorsan (faster-whisper kuruluysa) ekle, kaliteyi artirir.
3. Su iki metni Turkce uret, HIZLANDIRMA/YAVASLATMA (atempo) YAPMA:
   a) Mark ref ile: "Önceki haberlerdeki gelişmelerle başlıyorum. Önceki bültenimizde yer alan Şanlıurfa Karaköprü ilçesindeki inşaat kazasında, hayatını kaybeden işçinin kimliği netleşti. Haberlere göre üçüncü kattan düşen kişi, on altı yaşındaki Ahmet Baytemur."
   b) Adam ref ile: "Teşekkür ederim. Karaköprüdeki düşmenin de Güngörendeki toprak kaymasının da nedenini soruşturma ortaya çıkaracak, ben tahmin yürütmeyeceğim."
4. Sonuclari (ornek_omni_mark.mp3, ornek_omni_adam.mp3) ve sure/hece-sn olcumunu `ciktilar` dalinda `bulten/ornek_omni/` altina push et (force yok) ve Telegram'a ses dosyasi olarak gonder. Uretim suresini (RTF) yaz.
5. Gemini'ye hic istek atma. Model indirilemezse veya cikti bozuksa hatayi yazip exit 1 ile cik.
