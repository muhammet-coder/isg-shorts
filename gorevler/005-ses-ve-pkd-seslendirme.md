# Görev 005: Türkçe ses (Gemini TTS / edge-tts) ve PKD videosu seslendirmesi

Kapsam: ~/mp2 ve yeni klasör ~/seslendirme. Mevcut cron'lara, MPV2 modüllerine, ~/kissalar'a DOKUNMA. API anahtarını asla yazdırma/Telegram'a gönderme. Bu görev 001-004 bittikten sonra çalışsın.

AMAÇ: Muhammet'in elle AI Studio'da ses üretmesini bitirmek. Ajan sesi kendisi üretsin (bülten ve videolar için).

1. GEMINI TTS TESTİ: GEMINI_API_KEY ile Gemini metinden-sese modelini (güncel gemini-*-tts, örn. gemini-2.5-flash-preview-tts veya daha yenisi) Türkçe dene. Mevcut hazır erkek seslerinden 3 tanesiyle (derin/otoriter haber sunucusu tonu, sıcak anlatıcı tonu, genç net ton) 10 sn örnek üret; örnekleri Telegram'a ses olarak gönder, mesaja ses adlarını yaz. Sonuç: çalışıyor mu / kota (429) / yetki (403) / model yok (404). Çalışmazsa edge-tts tr-TR-AhmetNeural ile devam et ve nedenini raporla.
2. PKD SESLENDİRMESİ: Aşağıdaki 8 sahne metnini, haber sunucusu tonundaki seçtiğin sesle (Gemini çalışıyorsa; yoksa edge-tts AhmetNeural), HER SAHNE AYRI mp3 olarak üret (sahne1.mp3 ... sahne8.mp3, 44100 Hz, mono). Metinleri AYNEN oku, hiçbir şeyi değiştirme (İSG-PRO okunuşu "i se ge pro" metinde yazıldığı gibi).
3. TESLİM: mp3'leri ~/seslendirme/pkd/ içine kaydet VE muhammet-coder/isg-shorts deposunda "ciktilar" dalına (yoksa oluştur: git checkout --orphan ciktilar) pkd/sahne1.mp3 ... sahne8.mp3 olarak commit edip push et (başka hiçbir şey push etme, anahtar dosyalarını ASLA ekleme). Telegram'a kısa rapor: kullanılan ses/model, her mp3'nin süresi (ffprobe), push edildi mi.

SAHNE METİNLERİ
sahne1: Akaryakıt istasyonunda en büyük tehlike gözle görülmez. Havaya karışan benzin buharı.
sahne2: Patlayıcı ortam oluşabilen her işyerinde işveren, Patlamadan Korunma Dokümanı hazırlamak zorundadır. Yanıcı madde, oksijen ve bir kıvılcım yeter.
sahne3: İstasyonu tanıyarak başlarız. Yakıt envanteri, parlama noktası, patlama sınırları ve sızıntı kaynakları tek tek çıkarılır.
sahne4: Sonra alan sınıflandırması yapılır. Tank içi bölge sıfır, dolum ağzı bölge bir, dağıtım adası bölge iki.
sahne5: Buharın rüzgârla nereye taşındığını open foam simülasyonuyla hesaplıyoruz. Alt patlama sınırı konturu, bölge sınırlarını doğrulamamızı sağlar. Sonuç, rapora ölçekli görselle eklenir.
sahne6: Unutulan risk, statik elektrik. Araçtan inen müşterinin üzerinde biriken yük, dolum anında ateşleme kaynağı olabilir. Önlem raporda açıkça yazılır.
sahne7: On üç ateşleme kaynağı tek tek değerlendirilir. Ex ekipman uygunluğu, bakım programı ve acil durum önlemleri aynı dokümanda toplanır.
sahne8: i se ge pro ile belge isteme, termin takibi ve kurulum onayı tek yerden yönetilir. Adres: i se ge pro nokta kom.

EK (Charon örneği incelendi): Gemini TTS çalışıyor (Charon, 6,3 sn örnek geldi). Ancak aynı ölçüm yönteminde bu örnek, Muhammet'in "gayet iyi" bulduğu edge-tts videosundan ~%40 daha hızlı. PKD seslendirmesinde (ve Gemini sesi kullanılan her yerde): önce prompt'ta "yavaş, sakin, net, cümleler arasında duraklayarak" iste, sonra her mp3'e ffmpeg atempo=0.80 uygula (gerekirse 0.75); cümleler arası 0,5 sn sessizlik. Her sahneyi ffprobe ile ölç ve hızı 4,2-4,8 hece/sn aralığında tut (hece = Türkçe sesli harf sayısı / konuşma süresi). Hız ve süreleri raporla.
