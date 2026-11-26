# Gorev 035: 26 Kasim bulteni kazalarini istatistige ekle

Anahtar ~/.env icindeki ILAN_ANAHTARI (ASLA yazdirma/commit/Telegram'a koyma). Asagidaki JSON'u gecici dosyaya yaz ve:
curl -s -X POST https://isg-pro.com/api/istatistik-ekle -H "content-type: application/json" -H "x-ilan-anahtari: $ILAN_ANAHTARI" --data @/tmp/kaza26.json
Beklenen cevap {"eklendi":3} (tekrar calisirsa 0 olabilir, sorun degil). Sonra GET https://isg-pro.com/api/istatistik ile bu uc olayin listede oldugunu dogrula. Telegram'a 2 satirlik sonuc yaz (anahtari yazma). Exit 0.

[
{"tarih":"2026-11-25","il":"Trabzon","ilce":"Ortahisar","olay":"Elektrik arızası çalışmasında kaza geçiren işçi hastanede öldü; haberlerde elektrik akımı ve vinç devrilmesi anlatılıyor.","tur":"Elektrik çarpması","olu":1,"yarali":0,"kaynak":"Haber61","kaynak_url":"https://www.haber61.net/trabzon/trabzon-da-vinc-faciasi-devrilen-vincte-elektrik-akimina-kapilarak-can-verdi/650564"},
{"tarih":"2026-11-25","il":"İzmir","ilce":"Narlıdere","olay":"Ağaçlık alanda ağaç kesen işçi, devrilen ağacın başına çarpması sonucu öldü.","tur":"Düşen cisim","olu":1,"yarali":0,"kaynak":"Yeni Asır","kaynak_url":"https://www.yeniasir.com.tr/izmir/2026/11/25/izmir-narliderede-agac-kesimi-sirasinda-feci-kaza-uzerine-agac-devrilen-isci-kurtarilamadi"},
{"tarih":"2026-11-22","il":"Denizli","ilce":"Honaz","olay":"Lastikçide janttan ayrılmak istenen kamyon lastiği fırlayıp çalışana çarptı; yaralı tedavinin dördüncü gününde öldü.","tur":"Ekipman / basınçlı kap","olu":1,"yarali":0,"kaynak":"Hürriyet","kaynak_url":"https://www.hurriyet.com.tr/yerel-haberler/denizli/janttan-ayirmaya-calistigi-lastigin-carptigi-is-43391580"}
]
