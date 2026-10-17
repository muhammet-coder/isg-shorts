#!/usr/bin/env python3
"""
İSG PRO — Sınav Sorusu Shorts üreticisi.

Kullanım:
    python3 shorts_uret.py sorular.json [cikti_klasoru]

sorular.json biçimi (liste):
[
  {
    "no": 12,                                  # isteğe bağlı, kanal genelinde soru numarası
    "sinif": "C",                              # A / B / C / "Genel"
    "konu": "Yüksekte Çalışma",
    "soru": "Soru metni ...",
    "secenekler": ["...", "...", "...", "...", "..."],   # 4 veya 5 şık (A–E)
    "dogru": "B",
    "aciklama": "Kısa gerekçe (1-2 cümle).",
    "kaynak": "Yapı İşlerinde İSG Yönetmeliği, Ek-4"
  }
]

Her soru için <klasor>/soru_<no>.mp4 (1080x1920, ~24 sn) ve
<klasor>/soru_<no>_youtube.txt (başlık, açıklama, etiketler) üretir.
Gereken: python3, Pillow, ffmpeg. İnternet gerekmez.
"""
from __future__ import annotations

import json
import math
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FPS = 30
LACIVERT = (11, 31, 58)
LACIVERT2 = (22, 50, 90)
KIRMIZI = (212, 32, 39)
SARI = (242, 176, 30)
YESIL = (34, 160, 90)
BEYAZ = (245, 248, 252)
GRI = (170, 186, 206)
KART = (24, 44, 78)

SURE_KAPAK = 2.0
SURE_GERI_SAYIM = 15         # saniye, soru ekranı
SURE_CEVAP = 7.0
SURE_KAPANIS = 2.5
HARFLER = "ABCDE"

FONT_ADAYLARI = {
    "bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ],
    "regular": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ],
}


def font(kalin: bool, boyut: int) -> ImageFont.FreeTypeFont:
    ozel = os.environ.get("ISG_FONT_BOLD" if kalin else "ISG_FONT")
    for yol in ([ozel] if ozel else []) + FONT_ADAYLARI["bold" if kalin else "regular"]:
        if yol and os.path.exists(yol):
            return ImageFont.truetype(yol, boyut)
    raise SystemExit("Uygun font bulunamadı. 'sudo apt install fonts-dejavu-core' kurun.")


# ─────────────────────────── çizim yardımcıları ───────────────────────────

def zemin() -> Image.Image:
    img = Image.new("RGB", (W, H), LACIVERT)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(LACIVERT2[i] * (1 - t) + LACIVERT[i] * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return img


def sar(d: ImageDraw.ImageDraw, metin: str, f, genislik: int) -> list[str]:
    satirlar: list[str] = []
    for paragraf in metin.split("\n"):
        kelimeler, satir = paragraf.split(), ""
        for k in kelimeler:
            deneme = (satir + " " + k).strip()
            if d.textlength(deneme, font=f) <= genislik:
                satir = deneme
            else:
                if satir:
                    satirlar.append(satir)
                satir = k
        satirlar.append(satir)
    return satirlar


def sigdir(d, metin, kalin, genislik, max_yukseklik, buyuk, kucuk, aralik=1.25):
    """Metni kutuya sığan en büyük punto ile sarar."""
    for b in range(buyuk, kucuk - 1, -2):
        f = font(kalin, b)
        s = sar(d, metin, f, genislik)
        if len(s) * b * aralik <= max_yukseklik:
            return f, s, b
    f = font(kalin, kucuk)
    return f, sar(d, metin, f, genislik), kucuk


def yaz(d, x, y, satirlar, f, boyut, renk, aralik=1.25, ortala=False, genislik=0):
    for s in satirlar:
        xx = x + (genislik - d.textlength(s, font=f)) / 2 if ortala else x
        d.text((xx, y), s, font=f, fill=renk)
        y += int(boyut * aralik)
    return y


def baret(d, cx, cy, olcek=1.0, renk=SARI):
    s = olcek
    d.pieslice([cx - 44 * s, cy - 44 * s, cx + 44 * s, cy + 44 * s], 180, 360, fill=renk)
    d.rounded_rectangle([cx - 58 * s, cy - 2 * s, cx + 58 * s, cy + 14 * s], radius=int(5 * s), fill=renk)
    d.rounded_rectangle([cx - 7 * s, cy - 50 * s, cx + 7 * s, cy], radius=int(4 * s), fill=(209, 143, 0))


def logo(d, x, y, olcek=1.0):
    """Sol üstten başlayan 'İSG PRO' logosu; genişliği döner."""
    baret(d, x + 58 * olcek, y + 52 * olcek, olcek)
    f = font(True, int(56 * olcek))
    tx = x + 130 * olcek
    d.text((tx, y + 14 * olcek), "İSG", font=f, fill=BEYAZ)
    w = d.textlength("İSG", font=f)
    fb = font(True, int(36 * olcek))
    bx = tx + w + 14 * olcek
    bw = d.textlength("PRO", font=fb) + 24 * olcek
    d.rounded_rectangle([bx, y + 20 * olcek, bx + bw, y + 70 * olcek], radius=int(10 * olcek), fill=SARI)
    d.text((bx + 12 * olcek, y + 24 * olcek), "PRO", font=fb, fill=LACIVERT)
    return bx + bw - x


def ust_serit(d, soru):
    logo(d, 60, 70, 0.9)
    etiket = f"{soru.get('sinif', 'Genel')} SINIFI" if soru.get("sinif", "Genel") != "Genel" else "İSG SINAVI"
    f = font(True, 34)
    w = d.textlength(etiket, font=f) + 44
    d.rounded_rectangle([W - 60 - w, 82, W - 60, 146], radius=32, fill=KIRMIZI)
    d.text((W - 60 - w + 22, 92), etiket, font=f, fill=BEYAZ)


def alt_serit(d):
    f = font(True, 34)
    t = "isg-pro.com  •  @isg-pro"
    d.text(((W - d.textlength(t, font=f)) / 2, H - 120), t, font=f, fill=GRI)


# ─────────────────────────── sahneler ───────────────────────────

def sahne_kapak(soru) -> Image.Image:
    img = zemin()
    d = ImageDraw.Draw(img)
    logo(d, (W - 440) // 2, 420, 1.3)
    f = font(True, 96)
    for i, t in enumerate(["İSG UZMANLIK", "SINAVI"]):
        d.text(((W - d.textlength(t, font=f)) / 2, 640 + i * 115), t, font=f, fill=BEYAZ)
    no = f"SORU #{soru['no']}" if soru.get("no") else "GÜNÜN SORUSU"
    f2 = font(True, 64)
    w = d.textlength(no, font=f2) + 80
    d.rounded_rectangle([(W - w) / 2, 920, (W + w) / 2, 1020], radius=50, fill=KIRMIZI)
    d.text(((W - d.textlength(no, font=f2)) / 2, 935), no, font=f2, fill=BEYAZ)
    konu = soru.get("konu", "")
    if konu:
        f3 = font(False, 48)
        d.text(((W - d.textlength(konu, font=f3)) / 2, 1080), konu, font=f3, fill=SARI)
    f4 = font(True, 44)
    t = f"{SURE_GERI_SAYIM} saniyen var. Hazır mısın?"
    d.text(((W - d.textlength(t, font=f4)) / 2, 1300), t, font=f4, fill=GRI)
    alt_serit(d)
    return img


def soru_govdesi(soru, vurgula: str | None = None) -> tuple[Image.Image, int]:
    """Soru + şıklar. vurgula verilirse doğru şık yeşil, diğerleri soluk."""
    img = zemin()
    d = ImageDraw.Draw(img)
    ust_serit(d, soru)

    # Soru metni
    f, satirlar, b = sigdir(d, soru["soru"], True, W - 140, 430, 58, 40)
    y = yaz(d, 70, 230, satirlar, f, b, BEYAZ)
    y += 40

    # Şıklar
    secenekler = soru["secenekler"]
    kalan = H - 300 - y
    kutu_h = min(170, (kalan - 24 * (len(secenekler) - 1)) // len(secenekler))
    for i, sec in enumerate(secenekler):
        harf = HARFLER[i]
        dogru = harf == soru["dogru"].upper()
        if vurgula is None:
            zemin_r, harf_r, metin_r = KART, SARI, BEYAZ
        elif dogru:
            zemin_r, harf_r, metin_r = YESIL, BEYAZ, BEYAZ
        else:
            zemin_r, harf_r, metin_r = (20, 36, 62), (90, 108, 134), (110, 128, 154)
        d.rounded_rectangle([60, y, W - 60, y + kutu_h], radius=26, fill=zemin_r)
        fh = font(True, 52)
        d.text((92, y + (kutu_h - 60) / 2), harf, font=fh, fill=harf_r)
        fs, sat, bs = sigdir(d, sec, False, W - 280, kutu_h - 24, 44, 28, 1.18)
        th = len(sat) * int(bs * 1.18)
        yaz(d, 170, y + (kutu_h - th) / 2 - 2, sat, fs, bs, metin_r, 1.18)
        if vurgula is not None and dogru:
            fk = font(True, 52)
            d.text((W - 120, y + (kutu_h - 60) / 2), "✓", font=fk, fill=BEYAZ)
        y += kutu_h + 24
    return img, y


def sahne_geri_sayim(soru, kalan: int) -> Image.Image:
    img, _ = soru_govdesi(soru)
    d = ImageDraw.Draw(img)
    # Geri sayım çubuğu ve rakamı
    oran = kalan / SURE_GERI_SAYIM
    d.rounded_rectangle([60, H - 230, W - 60, H - 200], radius=15, fill=(40, 60, 92))
    renk = YESIL if oran > 0.5 else (SARI if oran > 0.25 else KIRMIZI)
    d.rounded_rectangle([60, H - 230, 60 + (W - 120) * oran, H - 200], radius=15, fill=renk)
    f = font(True, 40)
    t = f"Kalan süre: {kalan} sn" if kalan > 0 else "Süre doldu!"
    d.text(((W - d.textlength(t, font=f)) / 2, H - 180), t, font=f, fill=BEYAZ)
    return img


def sahne_cevap(soru) -> Image.Image:
    img, y = soru_govdesi(soru, vurgula=soru["dogru"])
    d = ImageDraw.Draw(img)
    # Alt panel: doğru cevap + açıklama + kaynak (şıkların üstüne biner)
    panel_ust = max(y - 10, H - 640)
    panel_ust = min(panel_ust, H - 470)
    d.rounded_rectangle([40, panel_ust, W - 40, H - 150], radius=30, fill=(8, 22, 44), outline=YESIL, width=4)
    f1 = font(True, 50)
    d.text((80, panel_ust + 30), f"Doğru cevap: {soru['dogru'].upper()}", font=f1, fill=YESIL)
    alan = (H - 150) - (panel_ust + 110) - 70
    f2, sat, b2 = sigdir(d, soru.get("aciklama", ""), False, W - 160, alan, 44, 30)
    yy = yaz(d, 80, panel_ust + 100, sat, f2, b2, BEYAZ)
    if soru.get("kaynak"):
        f3 = font(False, 30)
        d.text((80, H - 210), "Kaynak: " + soru["kaynak"], font=f3, fill=GRI)
    return img


def sahne_kapanis(soru) -> Image.Image:
    img = zemin()
    d = ImageDraw.Draw(img)
    logo(d, (W - 440) // 2, 560, 1.3)
    f = font(True, 64)
    for i, t in enumerate(["Her gün yeni soru", "için abone ol!"]):
        d.text(((W - d.textlength(t, font=f)) / 2, 780 + i * 82), t, font=f, fill=BEYAZ)
    f2 = font(False, 42)
    t2 = "Cevabını yorumlara yaz!"
    d.text(((W - d.textlength(t2, font=f2)) / 2, 990), t2, font=f2, fill=GRI)
    f3 = font(True, 56)
    t3 = "isg-pro.com"
    w = d.textlength(t3, font=f3) + 70
    d.rounded_rectangle([(W - w) / 2, 1110, (W + w) / 2, 1210], radius=50, fill=KIRMIZI)
    d.text(((W - d.textlength(t3, font=f3)) / 2, 1125), t3, font=f3, fill=BEYAZ)
    return img


# ─────────────────────────── ses (sentetik, telifsiz) ───────────────────────────

def ses_uret(yol: Path, toplam: float, tik_zamanlari: list[float], ding_zamani: float, whoosh: list[float]):
    sr = 44100
    n = int(toplam * sr)
    buf = [0.0] * n

    def ekle(t0, sure, frek, genlik, sonum):
        i0 = int(t0 * sr)
        for k in range(int(sure * sr)):
            i = i0 + k
            if i >= n:
                break
            t = k / sr
            buf[i] += genlik * math.sin(2 * math.pi * frek * t) * math.exp(-t * sonum)

    for t in tik_zamanlari:
        ekle(t, 0.06, 900, 0.22, 60)
    for f_, g in ((880, 0.35), (1320, 0.25), (1760, 0.15)):
        ekle(ding_zamani, 1.2, f_, g, 3.5)
    for t in whoosh:
        i0 = int(t * sr)
        import random
        rnd = random.Random(7)
        for k in range(int(0.35 * sr)):
            i = i0 + k
            if i >= n:
                break
            env = math.sin(math.pi * k / (0.35 * sr))
            buf[i] += 0.12 * env * (rnd.random() * 2 - 1)

    with wave.open(str(yol), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, x)) * 30000)) for x in buf))


# ─────────────────────────── video ───────────────────────────

def video_uret(soru: dict, cikti: Path) -> Path:
    if len(soru["secenekler"]) not in (4, 5):
        raise ValueError("Şık sayısı 4 veya 5 olmalı")
    if soru["dogru"].upper() not in HARFLER[: len(soru["secenekler"])]:
        raise ValueError(f"Doğru cevap şıklar arasında değil: {soru['dogru']}")

    no = soru.get("no", "x")
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        parcalar: list[tuple[Path, float]] = []
        sahne_kapak(soru).save(tmp / "00.png")
        parcalar.append((tmp / "00.png", SURE_KAPAK))
        for i, kalan in enumerate(range(SURE_GERI_SAYIM, 0, -1)):
            p = tmp / f"1{i:02d}.png"
            sahne_geri_sayim(soru, kalan).save(p)
            parcalar.append((p, 1.0))
        sahne_cevap(soru).save(tmp / "20.png")
        parcalar.append((tmp / "20.png", SURE_CEVAP))
        sahne_kapanis(soru).save(tmp / "30.png")
        parcalar.append((tmp / "30.png", SURE_KAPANIS))

        liste = tmp / "liste.txt"
        with open(liste, "w") as f:
            for p, s in parcalar:
                f.write(f"file '{p}'\nduration {s}\n")
            f.write(f"file '{parcalar[-1][0]}'\n")

        toplam = sum(s for _, s in parcalar)
        t_soru = SURE_KAPAK
        tikler = [t_soru + i for i in range(max(0, SURE_GERI_SAYIM - 5), SURE_GERI_SAYIM)]
        t_cevap = t_soru + SURE_GERI_SAYIM
        ses = tmp / "ses.wav"
        ses_uret(ses, toplam, tikler, t_cevap, [])

        cikti.mkdir(parents=True, exist_ok=True)
        mp4 = cikti / f"soru_{no}.mp4"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(liste), "-i", str(ses),
             "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
             "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(mp4)],
            check=True,
        )
    (cikti / f"soru_{no}_youtube.txt").write_text(youtube_metni(soru), encoding="utf-8")
    return mp4


def youtube_metni(soru: dict) -> str:
    sinif = soru.get("sinif", "Genel")
    sinif_txt = f"{sinif} Sınıfı " if sinif != "Genel" else ""
    no = f" #{soru['no']}" if soru.get("no") else ""
    konu = soru.get("konu", "İş Güvenliği")
    baslik = f"{sinif_txt}İSG Sınav Sorusu{no}: {konu} | Cevabı Biliyor musun? #shorts"
    if len(baslik) > 100:
        baslik = f"İSG Sınav Sorusu{no}: {konu} #shorts"[:100]
    aciklama = (
        f"İSG uzmanlık sınavına hazırlananlar için günün sorusu: {konu}.\n"
        f"Cevabını yorumlara yaz, doğru cevap ve gerekçesi videonun sonunda.\n\n"
        f"Kaynak: {soru.get('kaynak', '-')}\n\n"
        "Sorular çıkmış sınav konularından esinlenerek hazırlanmıştır, birebir ÖSYM sorusu değildir.\n\n"
        "Şantiyede İSG'yi tek platformda yönetin: https://isg-pro.com\n\n"
        "#isg #işgüvenliği #isgsınavı #isguzmanlığı #6331"
    )
    etiketler = (
        "isg sınav soruları, iş güvenliği uzmanlığı sınavı, c sınıfı isg, b sınıfı isg, a sınıfı isg, "
        f"isg sınavı, 6331, iş güvenliği, isg-pro, {konu.lower()}"
    )
    return f"BAŞLIK:\n{baslik}\n\nAÇIKLAMA:\n{aciklama}\n\nETİKETLER:\n{etiketler}\n"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg bulunamadı: sudo apt install ffmpeg")
    sorular = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    cikti = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("shorts_cikti")
    for s in sorular:
        p = video_uret(s, cikti)
        print(p)


if __name__ == "__main__":
    main()
