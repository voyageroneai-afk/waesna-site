# WAESNA — kurumsal site

Statik site. Derleme adımı, bağımlılık ve build aracı **yok** — `index.html`
dosyasını düzenleyip commit'lemen yeterli, GitHub Pages birkaç dakikada yayınlar.

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `index.html` | **Sitenin tamamı.** İçerik, stil ve script tek dosyada. |
| `privacy.html`, `terms.html` | Yasal sayfalar — `legal.py` üretir, elle düzenleme. |
| `legal.py` | Yasal metinleri VoyagerOne.py'den alıp sayfalara çevirir. |
| `assets/waesna-mark.png` | Şirket logosu (şeffaf zemin) |
| `404.html` | Hatalı adreslerde çıkan markalı sayfa |

## Ayarlar

`index.html` dosyasının altındaki `CONFIG` bloğu tek ayar yeri:

```js
const CONFIG = {
  email: "voyageroneai@gmail.com",
  version: "1.0.0",
  buy:       { pro: "", team: "", company: "" },   // ödeme sayfası linkleri
  downloads: { mac: "", windows: "", linux: "" }   // GitHub Releases linkleri
};
```

Boş bırakılan alan kırık görünmez: satın alma düğmesi e-postaya döner,
indirme kartı "yakında" olur.

## Yasal sayfaları güncelle

VoyagerOne.py içindeki metinler değiştiyse:

```bash
python3 legal.py
```

## ⚠️ Güvenlik

Bu depo herkese açık. `index.html` içine yazdığın her şeyi herkes okuyabilir.

- ✅ Ödeme sayfası **linki**, indirme linki — açık olması normal
- ❌ Ödeme sağlayıcısının **secret/API key**'i — buraya asla yazma
- ❌ SMTP şifresi, lisans imzalama anahtarı — asla

## Güncelleme

```bash
git add -A && git commit -m "içerik güncellendi" && git push
```

Push'tan 1–2 dakika sonra site canlı olur.

## Yerelde önizleme

```bash
python3 -m http.server 8080
```
