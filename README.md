# WAESNA — kurumsal site

Statik site. Derleme adımı, bağımlılık ve build aracı **yok** — `index.html`
dosyasını düzenleyip commit'lemen yeterli, GitHub Pages birkaç dakikada yayınlar.

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `index.html` | **Sitenin tamamı.** İçerik, stil ve script tek dosyada. |
| `404.html` | Hatalı adreslerde çıkan markalı sayfa |
| `assets/waesna-mark.svg` | Amblem (W) — vektör, her boyutta net |
| `assets/waesna-wordmark.svg` | WAESNA yazısı — vektör |
| `assets/waesna-lockup.svg/.png` | Amblem + yazı birlikte |
| `assets/og.png` | WhatsApp / X / LinkedIn paylaşım önizlemesi |
| `assets/favicon.svg` | Sekme ikonu |
| `.nojekyll` | GitHub Pages'in dosyalara karışmasını engeller |

## Ayarlar

`index.html` dosyasının en altındaki `CONFIG` bloğu tek ayar yeri:

```js
const CONFIG = {
  email: "hello@waesna.com",
  buy: { voyagerone: "", appify: "" },  // ödeme sayfası linkleri
  web3formsKey: "",                      // iletişim formu (Web3Forms)
  formEndpoint: ""                       // ya da Formspree adresi
};
```

Boş bırakılan alanlar **kırık görünmez**: satın alma düğmesi "Bilgi Al"a döner ve
e-postaya yönlendirir, form yapılandırılmamışsa kendini gizler.

## ⚠️ Güvenlik

Bu depo **herkese açık** (GitHub Pages ücretsiz katmanı bunu gerektirir).
`index.html` içine yazdığın her şeyi internetteki herkes okuyabilir.

- ✅ Ödeme sayfası **linki** — açık olması normal
- ✅ Web3Forms **access key** — zaten herkese açık olacak şekilde tasarlanmış
- ❌ Ödeme sağlayıcısının **secret/API key**'i — buraya asla yazma
- ❌ SMTP şifresi, veritabanı bilgisi, lisans imzalama sırrı — asla

## Güncelleme

```bash
cd "waesna-site"
# index.html dosyasını düzenle
git add -A
git commit -m "içerik güncellendi"
git push
```

Push'tan ~1–2 dakika sonra site canlı olur.

## Yerelde önizleme

```bash
python3 -m http.server 8080
```

Sonra tarayıcıda `http://localhost:8080` adresini aç.
