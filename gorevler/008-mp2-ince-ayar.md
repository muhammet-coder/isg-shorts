# Görev 008: mp2 ince ayar (007 sonrası video: 67,9 sn, iskele, çok daha iyi)

Kapsam aynı (~/mp2, shorts_mp2.py). 007 sonucu iyi: süre 67,9 sn, kartlar ~6 sn, ses var. Kalan küçük düzeltmeler, hepsini yap ve yeniden üret:

1. SES HÂLÂ BİRAZ HIZLI: ölçülen ~5,8 hece/sn. Hedef 4,5-5,0. edge-tts rate'i -25% yap (veya Gemini TTS sonrası atempo=0.88). Süre 75-85 sn'ye çıkabilir, sorun değil (Shorts <3 dk). Cümleler arası sessizlik 0,6 sn.
2. ALTYAZI KÜÇÜK: altyazı yazısı ~34 px görünüyor. 54 px, DejaVu Sans Bold, beyaz, koyu yarı saydam (rgba 13,27,42,0.85) zemin, en çok 2 satır x 26 karakter, ekranın alt kısmında (y≈1450-1650). Vurgulanan anahtar kelime turuncu (#FF8C00) olabilir.
3. KART YAZISI ve ETİKET: ana kart cümlesi 64-72 px; kartın üstündeki küçük turuncu etiket (ör. "MEVZUAT · Ankraj ve yaşam hattı") 34 px; madde numarası etikette görünsün (ör. "Yapı İşlerinde İSG Yönetmeliği md. 20" — madde numarası resmi metinden doğrulanmışsa; doğrulanamıyorsa numarasız bırak). Üstteki küçük "Yapı İşlerinde İSG Yönetmeliği" yazısı 30 px'ten küçük kalmasın.
4. KART KONUMU: kart bloğu dikey olarak şeridin altı ile altyazı alanı arasının tam ortasında olsun; mevcut halde alt yarıda boşluk fazla. Kart yüksekliğini içeriğe göre büyüt (en az 620 px).
5. KAPANIŞ: son kart 6 sn kalsın, ses bittikten sonra 1 sn sessizlik; "isg-pro.com" büyük (96 px).
6. Başlığı (<=100 karakter), açıklamayı (https://isg-pro.com + yapay zekâ notu) ve etiketleri yine AYRI mesajlarda gönder. Raporda hece/sn, toplam süre, kart sayısı ve doğrulanan madde numaralarını yaz.
