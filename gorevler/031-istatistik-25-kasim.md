# Gorev 031: 25 Kasim bulteni kazalarini istatistige ekle

Anahtar ~/.env icindeki ILAN_ANAHTARI (ASLA yazdirma/commit/Telegram'a koyma). Asagidaki JSON'u gecici dosyaya yaz ve:
curl -s -X POST https://isg-pro.com/api/istatistik-ekle -H "content-type: application/json" -H "x-ilan-anahtari: $ILAN_ANAHTARI" --data @/tmp/kaza25.json
Beklenen cevap {"eklendi":3} (tekrar calisirsa 0 olabilir, sorun degil). Sonra GET https://isg-pro.com/api/istatistik ile bu uc olayin listede oldugunu dogrula. Telegram'a 2 satirlik sonuc yaz (anahtari yazma). Exit 0.

[
{"tarih":"2026-11-24","il":"İzmir","ilce":"Aliağa","olay":"Limanda çalışan işçi hurda kamyonunun altında kalarak hayatını kaybetti.","tur":"Araç çarpması","olu":1,"yarali":0,"kaynak":"Evrensel","kaynak_url":"https://www.evrensel.net/haber/6011143/izmir-demir-celik-limaninda-is-cinayeti-isciler-ihmalleri-anlatti"},
{"tarih":"2026-11-25","il":"Yozgat","ilce":"Sorgun","olay":"İnşaat işçilerini taşıyan kamyonet gizli buzlanmada yoldan çıkıp takla attı; sürücüyle birlikte 5 kişi yaralandı.","tur":"Trafik / servis","olu":0,"yarali":5,"kaynak":"İşçi Haber","kaynak_url":"https://www.iscihaber.net/yozgat/yozgatta-iscileri-tasiyan-kamyonet-buzlanma-nedeniyle-takla-atti-5-yarali/285166"},
{"tarih":"2026-11-25","il":"Bursa","ilce":"Nilüfer","olay":"İşçi servisi ile hafif ticari araç çarpıştı; servisteki 8 kişi yaralandı.","tur":"Trafik / servis","olu":0,"yarali":8,"kaynak":"GZT","kaynak_url":"https://www.gzt.com/gundem/bursada-isci-servisi-kazasi-8-kisi-yaralandi-4282706"}
]
