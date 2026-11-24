# Gorev 018: Mail ajani (isg-mail-ajan) listesi bitti, bugun 0 mail gitti (24 Kasim 17:41 raporu)
DURUM: Gunluk rapor: bugun 0 mail, listede 0 firma kaldi, hata kaydi yok. Toplam: gonderildi 268, gecersiz 34, cevap 1. Apify'dan otomatik yeni firma cekme kurulmustu; bugun cekilmedi ve hata da bildirilmedi.
YAP (sadece ~/isg-mail-ajan; shorts/bulten/kissalar/diger gorevlere dokunma):
1) NEDEN yeni firma cekilmedi: apify otomasyonunun logu, cron, butce kontrolu (Apify aylik ucretsiz limit/yenilenme tarihi, 20 dolar ust sinir kuralin) ve gunluk kontrol mantigini incele; nedeni Telegram'a tek satir yaz.
2) Butce varsa: mevcut kurallarla (sadece mail adresi dogrulanmis firmalar, web adresi olan, MX/format kontrolu, alan adi tekrari yok, genel info@ tercih, firma adi mutlaka var) yeni bir parti cek; gunluk ve toplam butceyi ASLA asma, ek ucret/odeme baslatma. Butce yoksa DUR, Telegram'a "Apify butcesi bitti, yenilenme: <tarih>" yaz.
3) Ceken parti firmalar.csv'ye eklendiyse mail ajaninin bugun/yarin gonderim yapabilir hale geldigini dogrula (kuyruk sayisi). Gonderim limiti ve hatirlatma mantigini DEGISTIRME.
4) Telegram'a kisa ozet: kac firma eklendi, maliyet, yarin kac mail gidecek.
