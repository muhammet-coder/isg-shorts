# Gorev 038: 27 Kasim bulteni kazalarini istatistige ekle

Anahtar ~/.env icindeki ILAN_ANAHTARI (ASLA yazdirma/commit/Telegram'a koyma). Asagidaki JSON'u BENZERSIZ ad (mktemp) gecici dosyaya yaz ve:
curl -s -X POST https://isg-pro.com/api/istatistik-ekle -H "content-type: application/json" -H "x-ilan-anahtari: $ILAN_ANAHTARI" --data @DOSYA
EKSTRA: Duzce'de otomotiv bayisinin aku odasinda cikan yangin (5 isci dumandan etkilendi, kaynak Saray Medya) JSON'da yok; haberi bul (WebSearch), tarihini ve URL'sini dogrula, listeye {"il":"Düzce","tur":"Yangın / patlama","olu":0,"yarali":5} olarak ekle. Tarih bulunamazsa 2026-11-27 yaz ve Telegram'da belirt.
Sonra GET https://isg-pro.com/api/istatistik ile uc olayin listede oldugunu dogrula. Telegram'a 2 satirlik sonuc yaz (anahtari yazma). Exit 0.

[
{"tarih":"2026-11-26","il":"Zonguldak","ilce":"","olay":"TTK Karadon Gelik maden ocağında üretim sırasında kömür yığını kaydı, 2 işçi yaralandı.","tur":"Maden / taş ocağı","olu":0,"yarali":2,"kaynak":"Bursa Hakimiyet","kaynak_url":"https://www.bursahakimiyet.com.tr/gundem/zonguldak-ta-maden-ocagindaki-is-kazasinda-2-isci-yaralandi-1760216"},
{"tarih":"2026-11-26","il":"Konya","ilce":"Çumra","olay":"Kamyonla hububat işlemi sırasında sıkışan kamyon sürücüsü hayatını kaybetti.","tur":"Diğer","olu":1,"yarali":0,"kaynak":"Yeni Konya","kaynak_url":"https://www.yenikonya.com.tr/konya/konya_da_feci_olum_2_sehri_uzen_olay-1988848"}
]
