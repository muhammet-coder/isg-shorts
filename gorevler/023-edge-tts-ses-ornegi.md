# Gorev 023: Ucretsiz edge-tts ile bulten ses ornekleri (Gemini YOK)

Amac: Gemini kotasi/yavaslik sorunu nedeniyle kotasiz ucretsiz alternatif test etmek.
1. `pip install edge-tts` (yoksa). Sunucuda calisiyor mu dene. (014'te Ahmet fallback olarak yazilmisti.)
2. Su metni (Mark'in 23 Kasim ilk paragrafi) tr-TR-AhmetNeural ile uret: "Önceki haberlerdeki gelişmelerle başlıyorum. Önceki bültenimizde yer alan Şanlıurfa Karaköprü ilçesindeki inşaat kazasında, hayatını kaybeden işçinin kimliği netleşti. Haberlere göre üçüncü kattan düşen kişi, on altı yaşındaki Ahmet Baytemur."
3. Ayni metni rate=+0%, +8% ve pitch varyasyonu olmadan iki hizda ver (ornek_ahmet_normal.mp3, ornek_ahmet_hizli.mp3). Muhammet'in bolumu icin: "Teşekkür ederim. Karaköprüdeki düşmenin de Güngörendeki toprak kaymasının da nedenini soruşturma ortaya çıkaracak, ben tahmin yürütmeyeceğim." metnini de varsa en derin erkek sesle (tr-TR-AhmetNeural) uret (ornek_muhammet.mp3). Kadin sese gerek yok.
4. Dosyalari `ciktilar` dalina `bulten/ornek_edge/` altina push et (force yok) VE Telegram'a ses dosyasi olarak gonder. Hizlandirma/yavaslatma (atempo) YAPMA, ham edge-tts cikisi olsun.
5. Calismazsa (ag/izin) hatayi yazip exit 1 ile cik. Gemini'ye hic istek atma.
