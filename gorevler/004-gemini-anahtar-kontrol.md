# Görev 004: Gemini anahtarı ve görsel üretim kontrolü

Kapsam: sadece okuma ve test; hiçbir dosyayı silme/değiştirme, anahtarı ASLA yazdırma veya Telegram'a gönderme (sadece "var/yok" ve son 4 hanesi).

Muhammet'in Google AI Studio hesabında "isgpro-youtube" adlı proje var (ücretsiz katman, faturalandırma yok). Şunu yap:
1. Sunucuda GEMINI_API_KEY (veya GOOGLE_API_KEY) tanımlı mı bak: ~/.env, ~/mp2/.env, ~/isgpro/.env, ortam değişkenleri, mevcut betikler (grep -rl "generativelanguage\|GEMINI" ~ --include=*.py --include=*.sh --include=.env* ile; DEĞERİ yazdırma).
2. Anahtar varsa küçük bir görsel üretim testi yap (gemini-2.5-flash-image veya güncel görsel model; "güvenlik baretli işçi, gerçekçi şantiye fotoğrafı, yazı yok" gibi). Sonuç: başarılı / kota (429) / yetki (403) / model yok (404) hangisi? Ücretsiz katmanda görsel üretim çalışıyor mu?
3. Başarılıysa mp2'nin görsel adımını bu anahtarla çalışacak şekilde bağla (003'teki kurallarla: filigransız, yüz yakın çekimi yok, görselde yazı yok, yoksa şablon kartlara düş). Başarısızsa mp2 şablon kartlarla devam etsin.
4. Telegram'a kısa rapor: anahtar var/yok (son 4 hane), test sonucu, ücretsiz katmanda görsel çalışıyor mu, faturalandırma gerekiyor mu.
