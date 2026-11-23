# Görev 002: mp2 video hattı düzeltmeleri (001'in test videosu incelendi)

Kapsam: sadece ~/mp2 ve shorts_mp2.py. MPV2 upload / Twitter / affiliate / cold-email modüllerine, mevcut cron'lara, shorts_hf.py ve ~/kissalar'a DOKUNMA. YouTube'a yükleme yok; yayını Muhammet yapar.

001 ile üretilen test videosu (KKD Yönetmeliği, 50,8 sn, 1080x1920) Telegram'dan geldi. Hat çalışıyor, ama şu hatalar var; hepsini düzelt, yeni bir test videosu üret ve Telegram'a gönder:

1. SES YOK. Çıktı mp4'te ses akışı hiç yok. Ses ekle: ELEVENLABS_API_KEY varsa ElevenLabs Adam (J17lijyP1BHYcM7ld0Rg), yoksa edge-tts tr-TR-AhmetNeural. Altyazı ve sahne süreleri sesin gerçek süresinden çıksın. ElevenLabs metinlerinde: apostrof yok, sayılar yazıyla, İSG-PRO okunuşu "i se ge pro", adres "i se ge pro nokta kom". Videonun sonunda ses kesilmesin; ffprobe ile çıktıda audio stream olduğunu doğrula.
2. FİLİGRAN VE GÖRSEL KALİTESİ. Görsellerde "pollinations.ai" filigranı var ve görseller düşük kalite (anime tarzı yüzler, bulanık yakın çekim). Pollinations'ı bırak. GEMINI_API_KEY varsa Gemini görsel üret (gerçekçi saha fotoğrafı tarzı, baret/yelek, şantiye); yoksa görselsiz şablon sahneler üret: HyperFrames ile madde kartları, mevzuat kartı, İSG-PRO çözüm kartı (/home/claude/hf veya ~/hf kurulumu, hyperframes-isgpro becerisi). Filigranlı hiçbir görsel kullanma.
3. TEKİL KARE. 16 sn boyunca aynı bulanık kare kalıyor (4. - 7. altyazılar). Her sahne en çok 4-5 sn sürsün; sahne sayısını artır veya yavaş zoom/kaydırma (Ken Burns) ekle; aynı görseli arka arkaya kullanma.
4. ÜST BANT. Bantta "İSG-PRO" kısa rozeti ve kesilmiş başlık var ("...İşyerlerinde K..."). Başından sonuna üstte turuncu (#FF8C00) şerit, içinde "İSG-PRO.COM" (koyu #0D1B2A) olsun; başlık şeritte değil, ilk 3 sn'de ekranda tam yazsın.
5. UZUN ÇIKIŞ: Altyazı son kartta "önce yapılan küçük bir" gibi anlamsız parça kalıyor; son kart altyazısız, sadece isg-pro.com ve kısa kapanış cümlesi olsun.
6. MEVZUAT: Sahnede söylenen her madde numarası ve ifade resmi metinden doğrulansın (mevzuat.gov.tr); doğrulanamayan cümleyi çıkar. Kanun ile yönetmelik maddesini karıştırma.

Teslim: videolar/mp2/ içine kaydet, telegram-video-gonder.sh ile gönder; başlık (en fazla 100 karakter), açıklama (https://isg-pro.com bağlantısı + yapay zekâ notu) ve etiketler (#işgüvenliği biçiminde, boşluksuz) AYRI mesajlarda gitsin. Sonunda raporda: ses akışı var mı, süre, her sahnenin kaynağı (Gemini/şablon), doğrulanan madde listesi.
