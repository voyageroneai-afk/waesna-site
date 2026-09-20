#!/usr/bin/env python3
"""privacy.html ve terms.html sayfalarını VoyagerOne.py içindeki YASAL METİNLERDEN
üretir; böylece uygulama ile site asla farklılaşmaz.   Kullanım:  python3 legal.py
"""
import html
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
APP = HERE.parent / "VoyagerOne.py"
EMAIL = "voyageroneai@gmail.com"


def app():
    spec = importlib.util.spec_from_file_location("vg", APP)
    m = importlib.util.module_from_spec(spec)
    sys.modules["vg"] = m
    spec.loader.exec_module(m)
    m.LEGAL_CONTACT_EMAIL = EMAIL
    return m


def md(body: str) -> str:
    out, lst = [], False
    for raw in body.split("\n"):
        line = raw.strip()
        if line.startswith("- "):
            if not lst:
                out.append("<ul>")
                lst = True
            out.append(f"<li>{html.escape(line[2:])}</li>")
            continue
        if lst:
            out.append("</ul>")
            lst = False
        if not line:
            continue
        out.append(f"<h3>{html.escape(line[3:])}</h3>" if line.startswith("## ")
                   else f"<p>{html.escape(line)}</p>")
    if lst:
        out.append("</ul>")
    return "\n".join(out)


def style() -> str:
    """index.html'deki tokenları birebir kullan — iki sayfa aynı tasarımda kalsın."""
    src = (HERE / "index.html").read_text(encoding="utf-8")
    tokens = re.search(r":root\{(.*?)\}", src, re.S).group(0)
    dark = re.search(r"@media \(prefers-color-scheme:dark\)\{:root:not\(\[data-theme=light\]\)\{.*?\}\}", src, re.S).group(0)
    return tokens + "\n" + dark + """
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font:var(--t-body)/1.7 var(--body);-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.nav{display:flex;align-items:center;justify-content:space-between;padding:14px var(--pad);border-bottom:1px solid var(--rule)}
.logo{display:flex;align-items:center;gap:11px;font:600 15px/1 var(--display);letter-spacing:.16em;color:var(--ink);text-decoration:none}
.logo img{height:24px;width:auto}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .logo img{filter:invert(1)}}
.mono{font:500 var(--t-mono)/1.5 var(--mono);letter-spacing:.11em;text-transform:uppercase;color:var(--ink-3)}
main{max-width:780px;margin:0 auto;padding:clamp(40px,6vw,80px) var(--pad) 90px}
h1{font:600 clamp(32px,4vw,46px)/1.08 var(--display);letter-spacing:-.02em;margin:14px 0 10px}
h2{font:600 26px/1.2 var(--display);margin:54px 0 10px;padding-top:26px;border-top:1px solid var(--rule)}
h3{font:600 17px/1.35 var(--body);margin:26px 0 6px}
p,li{color:var(--ink-2);margin-bottom:10px}
ul{padding-left:20px}
.meta{color:var(--ink-3);font-size:var(--t-small);margin-bottom:26px}
.langbar{display:flex;gap:10px;font-size:var(--t-small);margin-bottom:8px}
footer{border-top:1px solid var(--rule);padding:28px var(--pad) 50px;font-size:13px;color:var(--ink-3);
  display:flex;gap:16px;justify-content:space-between;flex-wrap:wrap}
"""


def page(title, docs_by_lang, ids, version):
    body = ""
    for lang, label in (("tr", "Türkçe"), ("en", "English")):
        body += f'<section id="{lang}">'
        for did in ids:
            d = docs_by_lang[lang][did]
            body += f"<h2>{html.escape(d['title'])}</h2>" + md(d["body"])
        body += "</section>"
    return f"""<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — WAESNA</title>
<meta name="robots" content="index,follow">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600&family=Geist+Mono:wght@400;500&family=Geist:wght@400;500;600&display=swap" rel="stylesheet">
<style>{style()}</style></head><body>
<nav class="nav"><a class="logo" href="./"><img src="assets/waesna-mark.png" alt="WAESNA">WAESNA</a>
<a href="./" style="font-size:14px;color:var(--ink-2);text-decoration:none">← Ana sayfa</a></nav>
<main><p class="mono">VoyagerOne</p><h1>{html.escape(title)}</h1>
<p class="meta">Yürürlük / effective: {version} · Eray Mert Özüduru · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<div class="langbar"><a href="#tr">Türkçe</a><a href="#en">English</a></div>
{body}</main>
<footer><span>© 2026 WAESNA</span><span><a href="privacy.html">Gizlilik</a> · <a href="terms.html">Koşullar</a></span></footer>
</body></html>"""


def main():
    vg = app()
    docs = {lang: {d["id"]: d for d in vg._legal_docs(lang)} for lang in ("tr", "en")}
    (HERE / "privacy.html").write_text(
        page("Gizlilik Politikası ve KVKK Aydınlatma Metni", docs, ["privacy"], vg.LEGAL_VERSION), encoding="utf-8")
    (HERE / "terms.html").write_text(
        page("Kullanım Koşulları", docs, ["terms", "ai", "thirdparty"], vg.LEGAL_VERSION), encoding="utf-8")
    print("üretildi: privacy.html, terms.html")


if __name__ == "__main__":
    main()
