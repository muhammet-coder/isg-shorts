# Gorev 026: Claude Code guncellemesi + yeni ozellikleri test et (dikkatli)

Hedef: 2.1.329+ surume gec ve uc ozelligi guvenle kullanilabilir hale getir. Bu gorev calisan ajan duzenini BOZMAMALI.
1. Once yedek/durum: `claude --version`, kurulum yolu (npm mi native mi), crontab -l ciktisi (sirlari yazdirma). Mevcut surumu ve geri donus komutunu r_bilgi gibi bir not dosyasina yaz.
2. Guncelle: kurulum yontemine gore resmi yolla (`claude update` veya `npm i -g @anthropic-ai/claude-code@latest`). Sonra `claude -p "tamam yaz"` ile calistigini dogrula. Calismazsa hemen eski surume don ve Telegram'a yaz.
3. Gorev kutusu cron'unu bozmadigini dogrula (bir sonraki */30 turunda gorev calismali; calistirma komutu ayni kaldi mi bak).
4. Kod Modu (deneysel): GLOBAL ACMA. Sadece `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 claude -p "<basit cok adimli dosya taramasi>"` ile bir kez dene, sureyi normal moda gore karsilastir ve sonucu raporla. Calismazsa/kararsizsa kapali birak.
5. `claude mcp add-json <ad> -` stdin ozelligi: Etsy anahtari icin kullanilacak. Su an hicbir anahtar ekleme; yalnizca `claude mcp add-json --help` ile komutun var oldugunu dogrula.
6. Etkilenen planli gorev var mi (claude icindeki scheduled tasks, /tasks) kontrol et; crontab etkilenmez.
7. Rapor: eski surum, yeni surum, hangi adim basarili, Kod Modu sure karsilastirmasi, sorun varsa geri alma durumu. Telegram'a ozet. Silme yasagina uy.
