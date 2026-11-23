# Görev 007: mp2 video ritmi, kart yerleşimi ve ses hızı (sesli şablon videosu incelendi)

Kapsam: ~/mp2 ve shorts_mp2.py; diğer her şeye DOKUNMA. Sesli şablon videosu (44 sn, iskele korkuluğu) incelendi: ses ve filigran sorunu çözüldü. Kalan sorunlar:

1. KARTLAR ÇOK HIZLI VE KÜÇÜK. ~18 kart 44 sn'ye sığıyor (kart başına ~2 sn), ekranda dar bir alanda sol üstte duruyor, alt yarı boş; izleyici nereye bakacağını bilemiyor.
   - Kart sayısını azalt: 60-70 sn'lik videoda en çok 8-9 kart. Her kart en az 5 sn ekranda kalsın; kısa kart yerine tek cümle/tek fikir.
   - Kartı büyüt ve ekranın dikey ortasına koy: kart genişliği ~960 px, yüksekliği içeriğe göre 700-1000 px; ana metin en az 64 px, vurgu satırı 80 px, DejaVu Sans Bold. Üst şerit (İSG-PRO.COM) ve alt altyazı alanı arasında kalan alana ortala.
   - Her kartta tek odak: başlık (küçük, turuncu) + tek büyük cümle. "Yanlış / Doğru" kartında iki kutu alt alta, her biri en az 220 px yüksek, büyük yazı, ikisi birden 5-6 sn ekranda.
   - Kart geçişi yumuşak: 0,3 sn fade; kart seste cümle başlarken gelsin, cümle bitince 0,5 sn sonra kalksın (sesle senkron).
2. SES ACELE OKUYOR (~6,2 hece/sn; hedef 4,2-4,8 hece/sn). Ses hızını düşür: edge-tts için rate="-18%" (veya --rate=-18%); Gemini TTS için prompt'ta "yavaş, sakin, net" ver ve ses üretildikten sonra ffmpeg atempo=0.9 uygula (gerekirse 0.85). Cümleler arasına 0,5 sn sessizlik koy; virgülden sonra 0,2 sn. Anlatım sonunda 1 sn sessiz kuyruk. Sonuçta toplam süre 60-75 sn olsun.
3. ALTYAZI sesle aynı hızda, bir seferde en çok 2 satır x 28 karakter, en az 1,2 sn ekranda; altyazı alanı (ekranın alt kısmı y≈1450-1650) ve kartla çakışmasın.
4. Yeniden üretip Telegram'a gönder (başlık <=100 karakter / açıklama (https://isg-pro.com) / etiketler ayrı mesajlarda). Raporda: kart sayısı, her kartın süresi, hece/sn hızı (ffprobe + konuşma süresi), toplam süre.
