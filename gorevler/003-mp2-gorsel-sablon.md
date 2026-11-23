# Görev 003: mp2 görselleri (002 sonrası test videosu incelendi)

Kapsam aynı: sadece ~/mp2 ve shorts_mp2.py; MPV2 upload/Twitter/affiliate/cold-email, mevcut cron'lar, shorts_hf.py, ~/kissalar'a DOKUNMA. YouTube'a yükleme yok.

002 sonrası video (47 sn) incelendi. DÜZELDİ: ses var, son kart temiz, bantta madde etiketi var ("KKD Yönetmeliği md. 6").
HÂLÂ YANLIŞ:
1. Pollinations görselleri: "pollinations.ai" filigranı, bozuk yüzler, görselin içinde anlamsız yazı ("konatun"). Pollinations'ı TAMAMEN KALDIR. GEMINI_API_KEY yoksa görsel üretmeye çalışma; sadece şablon sahneler kullan.
2. Aynı görsel 4. - 7. altyazılar boyunca (~16 sn) duruyor. Her sahne en çok 4 sn; şablon sahnelerde her cümleye ayrı kart (madde kartı, mevzuat kartı, "Yanlış / Doğru" kartı, rakam kartı, İSG-PRO çözüm kartı) ve kartlar arasında geçiş animasyonu.
3. Üst bant: kırmızı "İSG-PRO" rozeti yerine başından sonuna turuncu (#FF8C00) şerit, içinde koyu (#0D1B2A) "İSG-PRO.COM". Madde etiketi (örn. "KKD Yönetmeliği md. 6") şeridin altında ayrı küçük kart olsun.
4. Şablon sahneleri HyperFrames ile üret (hyperframes-isgpro becerisi: arka plan #0D1B2A, kart #162C44 + sol turuncu kenar, DejaVu Sans Bold, 1080x1920). Kişi/yüz çizme.
5. GEMINI_API_KEY ileride .env'e girilirse: sadece gerçekçi saha fotoğrafı tarzı (baret, yelek, şantiye) görseller; yüz yakın çekimi yok; görselin içinde yazı yok; her görsel filigransız olduğu doğrulanmadan kullanılmasın.

Teslim 002 ile aynı: videolar/mp2/, telegram-video-gonder.sh, başlık (≤100 karakter) / açıklama (https://isg-pro.com) / etiketler ayrı mesajlarda. Raporda her sahnenin kaynağını (şablon/Gemini) yaz.
