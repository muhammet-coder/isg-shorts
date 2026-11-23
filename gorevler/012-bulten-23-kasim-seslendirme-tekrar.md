# (011 limit hatasi nedeniyle yeniden gonderildi; once ~/mp2/.env anahtarini ve Gemini TTS yolunu kullan, bitince Telegram bildir)
# Görev 011: 23 Kasım 2026 bülteni, Mark ve Muhammet bölümlerinin seslendirmesi

Kapsam: ~/seslendirme (005/006'daki ortak Gemini TTS fonksiyonunu kullan). Mevcut cron'lara, ~/kissalar'a, ~/mp2 altın standardına DOKUNMA. API anahtarını yazdırma. Metinler Muhammet'ten geldi; METİNLERİ DEĞİŞTİRME, haber arama, yeniden yazma; sadece AYNEN seslendir. Bu görev 005 ve 006 bittikten sonra çalışsın.

SESLER (Gemini TTS): mark.mp3 = Iapetus; muhammet.mp3 = Charon. İkisinde de "yavaş, sakin, net, cümleler arasında duraklayarak" prompt'u, ardından ffmpeg atempo=0.80, cümle aralarına 0,5 sn sessizlik, 44100 Hz mono. Hedef 4,2-4,8 hece/sn; ölç ve raporla. Uzun metni cümle gruplarına (<=400 karakter) bölüp ayrı üret, ffmpeg ile birleştir; birleşim yerlerinde ses seviyesi eşit kalsın.

TESLİM: mark.mp3 ve muhammet.mp3 dosyalarını muhammet-coder/isg-shorts deposunda "ciktilar" dalına bulten/2026-11-23/ klasörüyle commit edip push et (anahtar dosyaları ASLA ekleme). Telegram'a iki ses dosyasını gönder; mesajda süreler ve hece/sn.

=== MARK METNİ (mark.mp3, AYNEN oku) ===
Önceki haberlerdeki gelişmelerle başlıyorum. Önceki bültenimizde yer alan Şanlıurfa Karaköprü ilçesindeki inşaat kazasında, hayatını kaybeden işçinin kimliği netleşti. Haberlere göre üçüncü kattan düşen kişi, on altı yaşındaki Ahmet Baytemur. Bir meslek lisesinin çocuk gelişimi bölümünde son sınıf öğrencisi olduğu ve bir anaokulunda staj yaptığı belirtiliyor. Polis ekipleri soruşturma başlattı, düşmenin nedeni henüz açıklanmadı.

Yeni habere geçiyorum. İstanbul Güngören ilçesi Merkez Mahallesinde bir inşaatın temel kazısında toprak kaydı. Toprağın altında kalan işçi Mustafa Sekmen, itfaiye ve sağlık ekiplerince çıkarılıp hastaneye kaldırıldı, ancak yapılan müdahaleye rağmen kurtarılamadı. Haberlere göre belediye ekipleri şantiyede çalışmayı durdurdu, iş makinesi operatörü ile bir şirket çalışanı emniyete götürüldü. Soruşturma sürüyor.

Konuyla ilgili uzman görüşünü paylaşması için sözü Muhammet beye bırakıyorum.

=== MUHAMMET METNİ (muhammet.mp3, AYNEN oku) ===
Teşekkür ederim. Karaköprüdeki düşmenin de Güngörendeki toprak kaymasının da nedenini soruşturma ortaya çıkaracak, ben tahmin yürütmeyeceğim. Ama iki haberde aklıma aynı soru geliyor: risk, iş başlamadan önce konuşulmuş muydu? Altı bin üç yüz otuz bir sayılı Kanunun on sekizinci maddesi, işverenin çalışanların ve çalışan temsilcilerinin görüşünü alıp katılımlarını sağlamasını ister. Risk değerlendirmesi yapılırken, alınacak tedbirler ve koruyucu donanım belirlenirken, çalışanlara verilecek eğitim planlanırken bu görüşlerin önceden alınması gerekir.

Sahada şunu görüyorum: kazıda toprak çatlıyor, dökülüyor, kenarda su birikiyorsa bunu önce aşağıdaki işçi görür. O işçinin uyarısı işi durdurma sebebi sayılmalı. Kazı kenarına yük ve iş makinesi yaklaştırılmaz, derin kazıda iksa ve çıkış merdiveni hazır olur. Genç, stajyer ya da yeni başlayan işçi çekindiği için risk söylemez. Onu yüksekte tek başına bırakmayın, işe başlamadan önce nelere dikkat edeceğini birlikte konuşun. Hepinize iyi akşamlar, güvenli çalışmalar dilerim.
