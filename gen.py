# -*- coding: utf-8 -*-
import os, json
BASE = "/home/user/workspace/rmk_site"

# Bilingual content mirrored from content.js (server-side render the TJ default text + data attrs)
C = json.loads(open(os.path.join(BASE,"content.json"),encoding="utf-8").read())

ICONS = {
 'leaf':'<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/>',
 'spark':'<path d="M9.94 14.06 5 19m0-14 5 5m4-5-4.94 4.94M19 19l-4.94-4.94M12 2v3m0 14v3M2 12h3m14 0h3"/>',
 'people':'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
 'road':'<path d="M4 19 8 5m12 14L16 5M12 5v2m0 4v2m0 4v2"/>',
 'energy':'<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8Z"/>',
 'mountain':'<path d="m8 3 4 8 5-5 5 15H2L8 3Z"/>',
 'plant':'<path d="M7 20h10M12 20V8m0 0a5 5 0 0 0-5-5H5v2a5 5 0 0 0 5 5h2Zm0 4a5 5 0 0 1 5-5h2v1a5 5 0 0 1-5 5h-2Z"/>',
 'social':'<path d="M3 21h18M5 21V7l8-4v18M19 21V11l-6-4M9 9v.01M9 12v.01M9 15v.01M9 18v.01"/>',
 'shield':'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1Z"/>',
}

def icon(name, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

def bi(node):
    # returns (tj_text, attrs) -> element with data-tj/data-en
    return f'data-tj="{esc(node["tj"])}" data-en="{esc(node["en"])}"', node["tj"]

def esc(s):
    return s.replace('&','&amp;').replace('"','&quot;').replace('<','&lt;').replace('>','&gt;')

def nav_links():
    out=[]
    for n in C["nav"]:
        out.append(f'<a href="#{n["id"]}" data-tj="{esc(n["tj"])}" data-en="{esc(n["en"])}">{n["tj"]}</a>')
    return "\n".join(out)

def lang_toggle():
    return '''<div class="lang">
      <button data-lang-btn="tj" class="is-active" aria-pressed="true">TJ</button>
      <span class="lang-sep">/</span>
      <button data-lang-btn="en" aria-pressed="false">EN</button>
    </div>'''

def kpi_html():
    out=[]
    for k in C["about"]["kpi"]:
        out.append(f'''<div class="kpi reveal">
          <div class="kpi-num">{k["num"]}</div>
          <div class="kpi-lbl" data-tj="{esc(k["tj"])}" data-en="{esc(k["en"])}">{k["tj"]}</div>
        </div>''')
    return "\n".join(out)

def values_html():
    out=[]
    for v in C["about"]["values"]:
        out.append(f'''<div class="value reveal">
          {icon(v["icon"],"v-ico")}
          <h3 data-tj="{esc(v["tj"])}" data-en="{esc(v["en"])}">{v["tj"]}</h3>
          <p data-tj="{esc(v["dtj"])}" data-en="{esc(v["den"])}">{v["dtj"]}</p>
        </div>''')
    return "\n".join(out)

def services_html():
    out=[]
    for i,s in enumerate(C["services"]["items"]):
        out.append(f'''<article class="svc reveal">
          <div class="svc-ico">{icon(s["icon"])}</div>
          <h3 data-tj="{esc(s["tj"])}" data-en="{esc(s["en"])}">{s["tj"]}</h3>
          <p data-tj="{esc(s["dtj"])}" data-en="{esc(s["den"])}">{s["dtj"]}</p>
          <span class="svc-num">{i+1:02d}</span>
        </article>''')
    return "\n".join(out)

def projects_html():
    out=[]
    for p in C["projects"]["items"]:
        out.append(f'''<article class="proj reveal">
          <div class="proj-img"><img src="../assets/img/{p["img"]}" alt="" loading="lazy"></div>
          <div class="proj-body">
            <span class="proj-cat"><span data-tj="{esc(p["ctj"])}" data-en="{esc(p["cen"])}">{p["ctj"]}</span> · {p["year"]}</span>
            <h3 data-tj="{esc(p["tj"])}" data-en="{esc(p["en"])}">{p["tj"]}</h3>
          </div>
        </article>''')
    return "\n".join(out)

def contact_html():
    ct=C["contact"]; f=ct["form"]
    return f'''<div class="contact-info reveal">
      <p class="ci-row"><span class="ci-lbl">Email</span><a href="mailto:{ct["email"]}">{ct["email"]}</a></p>
      <p class="ci-row"><span class="ci-lbl">Tel</span><a href="tel:+99237000000">{ct["phone"]}</a></p>
      <p class="ci-row"><span class="ci-lbl" data-tj="Суроға" data-en="Address">Суроға</span><span data-tj="{esc(ct["addr"]["tj"])}" data-en="{esc(ct["addr"]["en"])}">{ct["addr"]["tj"]}</span></p>
    </div>
    <form class="contact-form reveal" data-form>
      <input type="text" required data-ph-tj="{esc(f["name"]["tj"])}" data-ph-en="{esc(f["name"]["en"])}" placeholder="{esc(f["name"]["tj"])}">
      <input type="email" required data-ph-tj="Email" data-ph-en="Email" placeholder="Email">
      <textarea rows="4" required data-ph-tj="{esc(f["msg"]["tj"])}" data-ph-en="{esc(f["msg"]["en"])}" placeholder="{esc(f["msg"]["tj"])}"></textarea>
      <button type="submit" class="btn btn-primary" data-tj="{esc(f["send"]["tj"])}" data-en="{esc(f["send"]["en"])}">{f["send"]["tj"]}</button>
      <p class="form-msg" data-form-msg></p>
    </form>'''

H=C["hero"]; A=C["about"]; S=C["services"]; P=C["projects"]; CT=C["contact"]

def page(title, fonts, css, logo, hero_img, hero_extra="", body_class="", header_logo_class=""):
    return f'''<!DOCTYPE html>
<html lang="tj">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Рушди Манотиқи Кӯҳистон</title>
{fonts}
<style>{css}</style>
</head>
<body class="{body_class}">
<a href="../index.html" class="back-gallery" data-tj="{esc(C["gallery"]["back"]["tj"])}" data-en="{esc(C["gallery"]["back"]["en"])}">{C["gallery"]["back"]["tj"]}</a>

<header data-header>
  <div class="wrap hdr-inner">
    <a href="#home" class="logo {header_logo_class}"><img src="../assets/img/{logo}" alt="РМК"></a>
    <nav class="nav">{nav_links()}</nav>
    <div class="hdr-right">
      {lang_toggle()}
      <button class="burger" data-burger aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<section id="home" class="hero">
  <div class="hero-bg"><img src="../assets/img/{hero_img}" alt=""></div>
  <div class="hero-overlay"></div>
  {hero_extra}
  <div class="wrap hero-inner">
    <span class="eyebrow reveal" data-tj="{esc(H["eyebrow"]["tj"])}" data-en="{esc(H["eyebrow"]["en"])}">{H["eyebrow"]["tj"]}</span>
    <h1 class="reveal" data-tj="{esc(H["title"]["tj"])}" data-en="{esc(H["title"]["en"])}">{H["title"]["tj"]}</h1>
    <p class="hero-sub reveal" data-tj="{esc(H["subtitle"]["tj"])}" data-en="{esc(H["subtitle"]["en"])}">{H["subtitle"]["tj"]}</p>
    <div class="hero-cta reveal">
      <a href="#contact" class="btn btn-primary" data-tj="{esc(H["cta1"]["tj"])}" data-en="{esc(H["cta1"]["en"])}">{H["cta1"]["tj"]}</a>
      <a href="#projects" class="btn btn-ghost" data-tj="{esc(H["cta2"]["tj"])}" data-en="{esc(H["cta2"]["en"])}">{H["cta2"]["tj"]}</a>
    </div>
  </div>
</section>

<section id="about" class="about section">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-text">
        <span class="tag reveal" data-tj="{esc(A["tag"]["tj"])}" data-en="{esc(A["tag"]["en"])}">{A["tag"]["tj"]}</span>
        <h2 class="reveal" data-tj="{esc(A["title"]["tj"])}" data-en="{esc(A["title"]["en"])}">{A["title"]["tj"]}</h2>
        <p class="lead reveal" data-tj="{esc(A["body"]["tj"])}" data-en="{esc(A["body"]["en"])}">{A["body"]["tj"]}</p>
      </div>
      <div class="values">{values_html()}</div>
    </div>
    <div class="kpis">{kpi_html()}</div>
  </div>
</section>

<section id="services" class="services section">
  <div class="wrap">
    <div class="sec-head">
      <span class="tag reveal" data-tj="{esc(S["tag"]["tj"])}" data-en="{esc(S["tag"]["en"])}">{S["tag"]["tj"]}</span>
      <h2 class="reveal" data-tj="{esc(S["title"]["tj"])}" data-en="{esc(S["title"]["en"])}">{S["title"]["tj"]}</h2>
    </div>
    <div class="svc-grid">{services_html()}</div>
  </div>
</section>

<section id="projects" class="projects section">
  <div class="wrap">
    <div class="sec-head">
      <span class="tag reveal" data-tj="{esc(P["tag"]["tj"])}" data-en="{esc(P["tag"]["en"])}">{P["tag"]["tj"]}</span>
      <h2 class="reveal" data-tj="{esc(P["title"]["tj"])}" data-en="{esc(P["title"]["en"])}">{P["title"]["tj"]}</h2>
    </div>
    <div class="proj-grid">{projects_html()}</div>
  </div>
</section>

<section id="contact" class="contact section">
  <div class="wrap">
    <div class="sec-head">
      <span class="tag reveal" data-tj="{esc(CT["tag"]["tj"])}" data-en="{esc(CT["tag"]["en"])}">{CT["tag"]["tj"]}</span>
      <h2 class="reveal" data-tj="{esc(CT["title"]["tj"])}" data-en="{esc(CT["title"]["en"])}">{CT["title"]["tj"]}</h2>
    </div>
    <div class="contact-grid">{contact_html()}</div>
  </div>
</section>

<footer class="footer">
  <div class="wrap foot-inner">
    <img src="../assets/img/{logo}" alt="РМК" class="foot-logo">
    <p data-tj="{esc(C["footer"]["tj"])}" data-en="{esc(C["footer"]["en"])}">{C["footer"]["tj"]}</p>
  </div>
</footer>

<script src="../assets/content.js"></script>
<script src="../assets/app.js"></script>
<script>RMK_init();</script>
</body>
</html>'''

# ---- Base CSS shared structure (layout) reused, theme overrides per template ----
BASE_CSS = '''
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:var(--body);color:var(--ink);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;display:block}
.wrap{width:100%;max-width:1200px;margin:0 auto;padding:0 24px}
a{color:inherit;text-decoration:none}
.section{padding:clamp(64px,9vw,120px) 0}
h1,h2,h3{font-family:var(--head);line-height:1.12;font-weight:var(--head-w,700)}
.tag{display:inline-block;font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;color:var(--accent);margin-bottom:14px}
.sec-head{margin-bottom:clamp(36px,5vw,56px);max-width:760px}
.sec-head h2{font-size:clamp(1.9rem,4.2vw,3rem)}
/* back to gallery */
.back-gallery{position:fixed;left:14px;bottom:14px;z-index:200;font-size:.8rem;font-weight:600;padding:9px 14px;border-radius:999px;background:var(--accent);color:var(--on-accent,#fff);box-shadow:0 6px 22px rgba(0,0,0,.25);transition:transform .2s}
.back-gallery:hover{transform:translateY(-2px)}
/* header */
header{position:fixed;top:0;left:0;right:0;z-index:100;transition:all .35s}
.hdr-inner{display:flex;align-items:center;justify-content:space-between;height:74px}
.logo img{height:44px;width:auto}
.nav{display:flex;gap:30px}
.nav a{font-size:.92rem;font-weight:600;position:relative;transition:color .2s}
.nav a::after{content:"";position:absolute;left:0;bottom:-5px;height:2px;width:0;background:var(--accent);transition:width .25s}
.nav a:hover::after{width:100%}
.hdr-right{display:flex;align-items:center;gap:16px}
.lang{display:flex;align-items:center;gap:6px;font-weight:700;font-size:.85rem}
.lang button{background:none;border:none;color:inherit;cursor:pointer;font-weight:700;opacity:.5;font-size:.85rem;font-family:var(--body);transition:opacity .2s}
.lang button.is-active{opacity:1;color:var(--accent)}
.lang-sep{opacity:.4}
.burger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:6px}
.burger span{width:24px;height:2px;background:currentColor;transition:.3s}
/* hero */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;overflow:hidden}
.hero-bg{position:absolute;inset:0;z-index:0}
.hero-bg img{width:100%;height:100%;object-fit:cover}
.hero-overlay{position:absolute;inset:0;z-index:1}
.hero-inner{position:relative;z-index:3;padding-top:90px;padding-bottom:60px;max-width:820px}
.eyebrow{display:inline-block;font-size:.82rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;margin-bottom:18px}
.hero h1{font-size:clamp(2.1rem,6vw,4.4rem);margin-bottom:22px}
.hero-sub{font-size:clamp(1rem,1.8vw,1.25rem);max-width:600px;margin-bottom:34px;opacity:.92}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap}
.btn{display:inline-block;padding:14px 30px;border-radius:var(--btn-r,8px);font-weight:700;font-size:.95rem;cursor:pointer;border:none;transition:transform .2s,box-shadow .2s,background .2s,color .2s}
.btn:hover{transform:translateY(-2px)}
/* about */
.about-grid{display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(36px,5vw,72px);align-items:start}
.about-text h2{font-size:clamp(1.8rem,4vw,2.8rem);margin-bottom:22px}
.lead{font-size:1.08rem;opacity:.85}
.values{display:flex;flex-direction:column;gap:18px}
.value{padding:22px 24px;border-radius:var(--card-r,14px);display:flex;flex-direction:column;gap:8px}
.v-ico{width:30px;height:30px;color:var(--accent)}
.value h3{font-size:1.15rem}
.value p{font-size:.92rem;opacity:.8}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:clamp(48px,6vw,80px)}
.kpi{text-align:center;padding:26px 12px;border-radius:var(--card-r,14px)}
.kpi-num{font-family:var(--head);font-size:clamp(2rem,4vw,2.8rem);font-weight:800;color:var(--accent);line-height:1}
.kpi-lbl{font-size:.85rem;letter-spacing:.04em;opacity:.75;margin-top:8px}
/* services */
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.svc{position:relative;padding:30px 28px;border-radius:var(--card-r,14px);overflow:hidden;transition:transform .3s,box-shadow .3s}
.svc:hover{transform:translateY(-6px)}
.svc-ico{width:46px;height:46px;display:flex;align-items:center;justify-content:center;border-radius:12px;color:var(--accent);margin-bottom:18px}
.svc-ico .ico{width:26px;height:26px}
.svc h3{font-size:1.2rem;margin-bottom:10px}
.svc p{font-size:.92rem;opacity:.8}
.svc-num{position:absolute;top:20px;right:24px;font-family:var(--head);font-weight:800;font-size:1.1rem;opacity:.18}
/* projects */
.proj-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}
.proj{border-radius:var(--card-r,14px);overflow:hidden;position:relative;transition:transform .3s}
.proj:hover{transform:translateY(-6px)}
.proj-img{aspect-ratio:16/10;overflow:hidden}
.proj-img img{width:100%;height:100%;object-fit:cover;transition:transform .6s}
.proj:hover .proj-img img{transform:scale(1.06)}
.proj-body{padding:22px 24px}
.proj-cat{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:var(--accent)}
.proj-body h3{font-size:1.35rem;margin-top:8px}
/* contact */
.contact-grid{display:grid;grid-template-columns:1fr 1.2fr;gap:clamp(36px,5vw,64px);align-items:start}
.ci-row{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid var(--hair);font-size:1rem}
.ci-lbl{min-width:80px;font-weight:700;opacity:.6;font-size:.85rem;text-transform:uppercase;letter-spacing:.06em}
.contact-form{display:flex;flex-direction:column;gap:14px}
.contact-form input,.contact-form textarea{padding:14px 16px;border-radius:var(--btn-r,8px);border:1px solid var(--hair);background:var(--field-bg,transparent);color:var(--ink);font-family:var(--body);font-size:1rem;width:100%}
.contact-form input:focus,.contact-form textarea:focus{outline:none;border-color:var(--accent)}
.contact-form .btn{align-self:flex-start}
.form-msg{opacity:0;transform:translateY(6px);transition:.4s;font-weight:600;color:var(--accent)}
.form-msg.show{opacity:1;transform:none}
/* footer */
.footer{padding:48px 0;border-top:1px solid var(--hair)}
.foot-inner{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}
.foot-logo{height:46px;width:auto}
.footer p{font-size:.9rem;opacity:.7}
/* reveal */
.reveal{opacity:0;transform:translateY(28px);transition:opacity .7s cubic-bezier(.2,.7,.2,1),transform .7s cubic-bezier(.2,.7,.2,1)}
.reveal.revealed{opacity:1;transform:none}
/* responsive */
@media(max-width:880px){
  .nav{position:fixed;inset:0 0 0 auto;width:78%;max-width:320px;flex-direction:column;background:var(--menu-bg,#16243A);padding:100px 32px 32px;gap:8px;transform:translateX(100%);transition:transform .35s;z-index:95;box-shadow:-20px 0 60px rgba(0,0,0,.3);pointer-events:none}
  body.nav-open .nav{transform:none;pointer-events:auto}
  .burger{position:relative;z-index:120}
  .nav a{color:var(--menu-ink,#fff);font-size:1.05rem;padding:10px 0}
  .burger{display:flex}
  body.nav-open .burger span:nth-child(1){transform:translateY(7px) rotate(45deg)}
  body.nav-open .burger span:nth-child(2){opacity:0}
  body.nav-open .burger span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
  .about-grid,.contact-grid{grid-template-columns:1fr}
  .svc-grid{grid-template-columns:repeat(2,1fr)}
  .kpis{grid-template-columns:repeat(2,1fr)}
  .proj-grid{grid-template-columns:1fr}
}
@media(max-width:560px){
  .wrap{padding:0 18px}
  .svc-grid{grid-template-columns:1fr}
  .hdr-inner,.hdr-inner{height:64px}
  .logo img{height:38px}
  .hero h1{font-size:clamp(1.8rem,8vw,2.6rem)}
  .foot-inner{flex-direction:column;text-align:center}
}
'''

# Save BASE_CSS for templates to import via concatenation
themes = {}

# ---------- THEME 1: Corporate Premium (blue/silver) ----------
themes[1] = dict(
  name="Корпоративный премиум",
  fonts='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">',
  logo="logo_silver.png", hero="hero_mountains.png", header_logo_class="logo-dark",
  css=BASE_CSS + '''
:root{--body:'Manrope',sans-serif;--head:'Montserrat',sans-serif;--ink:#16243A;--bg:#FFFFFF;--accent:#1E3A5F;--on-accent:#fff;--hair:#E2E8F0;--card-r:16px;--btn-r:10px;--menu-bg:#16243A;--field-bg:#F5F7FA}
header.scrolled{background:rgba(255,255,255,.92);backdrop-filter:blur(12px);box-shadow:0 1px 0 #E2E8F0}
.hdr-inner{color:#fff}
header.scrolled .hdr-inner{color:#16243A}
.hero-overlay{background:linear-gradient(105deg,rgba(16,23,38,.82) 0%,rgba(30,58,95,.45) 55%,rgba(16,23,38,.1) 100%)}
.hero-inner{color:#fff}
.eyebrow{color:#C7CFD9}
.btn-primary{background:#fff;color:#16243A}
.btn-primary:hover{background:#C7CFD9}
.hero .btn-ghost{background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.55)}
.hero .btn-ghost:hover{background:rgba(255,255,255,.12)}
.about{background:#fff}
.value{background:#F5F7FA;border:1px solid #E2E8F0}
.kpi{background:linear-gradient(160deg,#16243A,#1E3A5F);color:#fff}
.kpi-num{color:#C7CFD9}
.kpi-lbl{color:#C7CFD9}
.services{background:#F5F7FA}
.svc{background:#fff;border:1px solid #E2E8F0;box-shadow:0 1px 2px rgba(16,23,38,.04)}
.svc:hover{box-shadow:0 20px 40px rgba(16,23,38,.1)}
.svc-ico{background:#EEF2F7}
.proj{background:#fff;border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(16,23,38,.06)}
.contact{background:#16243A;color:#fff;--hair:rgba(255,255,255,.16);--ink:#fff;--field-bg:rgba(255,255,255,.06)}
.contact .tag{color:#C7CFD9}
.contact .btn-primary{background:#fff;color:#16243A}
.contact .ci-lbl{color:rgba(255,255,255,.55)}
.footer{background:#0E1726;color:#fff;--hair:rgba(255,255,255,.1)}
'''
)

# ---------- THEME 2: Luxury Gold (navy + gold, serif) ----------
themes[2] = dict(
  name="Роскошный золотой",
  fonts='<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700;800&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">',
  logo="logo_gold.png", hero="hero_dark.png", header_logo_class="",
  css=BASE_CSS + '''
:root{--body:'Manrope',sans-serif;--head:'Playfair Display',serif;--ink:#EAE6DC;--bg:#11203A;--accent:#C9A44C;--on-accent:#11203A;--hair:rgba(201,164,76,.22);--card-r:6px;--btn-r:4px;--menu-bg:#0C1830;--menu-ink:#EAE6DC;--field-bg:rgba(255,255,255,.04);--head-w:600}
header.scrolled{background:rgba(12,24,48,.9);backdrop-filter:blur(12px);box-shadow:0 1px 0 rgba(201,164,76,.25)}
.hdr-inner{color:#EAE6DC}
.nav a{font-weight:500;letter-spacing:.02em}
.lang button.is-active{color:#E6C566}
.hero-overlay{background:linear-gradient(100deg,rgba(12,24,48,.94) 0%,rgba(17,32,58,.6) 60%,rgba(17,32,58,.25) 100%)}
.hero-inner{color:#EAE6DC}
.eyebrow{color:#E6C566}
.hero h1{font-weight:600;letter-spacing:.005em}
.btn-primary{background:linear-gradient(135deg,#E6C566,#C9A44C);color:#11203A}
.btn-primary:hover{box-shadow:0 12px 30px rgba(201,164,76,.35)}
.btn-ghost{background:transparent;color:#E6C566;border:1px solid rgba(230,197,102,.5)}
.btn-ghost:hover{background:rgba(230,197,102,.1)}
.tag{color:#E6C566;letter-spacing:.24em}
.value{background:rgba(255,255,255,.03);border:1px solid rgba(201,164,76,.2)}
.kpi{background:rgba(255,255,255,.03);border:1px solid rgba(201,164,76,.25)}
.kpi-num{color:#E6C566}
.services{background:#0E1B33}
.svc{background:rgba(255,255,255,.03);border:1px solid rgba(201,164,76,.18)}
.svc:hover{border-color:rgba(201,164,76,.5);box-shadow:0 20px 50px rgba(0,0,0,.4)}
.svc-ico{background:rgba(201,164,76,.12);border:1px solid rgba(201,164,76,.3)}
.svc-num{color:#E6C566}
.proj{background:rgba(255,255,255,.03);border:1px solid rgba(201,164,76,.18)}
.contact-form input,.contact-form textarea{border:1px solid rgba(201,164,76,.3)}
.footer{background:#0C1830;--hair:rgba(201,164,76,.2)}
.about{position:relative}
.section h2{position:relative}
.sec-head .tag::before{content:"";display:inline-block;width:34px;height:1px;background:#C9A44C;vertical-align:middle;margin-right:10px}
'''
)

# ---------- THEME 3: Glassmorphism ----------
themes[3] = dict(
  name="Стекломорфизм",
  fonts='<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">',
  logo="emblem_silver.png", hero="hero_development.png", header_logo_class="logo-round",
  css=BASE_CSS + '''
:root{--body:'Sora',sans-serif;--head:'Sora',sans-serif;--ink:#F4F7FC;--bg:#0a1530;--accent:#7FB2FF;--on-accent:#0a1530;--hair:rgba(255,255,255,.18);--card-r:22px;--btn-r:14px;--menu-bg:rgba(14,23,40,.95);--field-bg:rgba(255,255,255,.08)}
body{background:radial-gradient(1200px 700px at 80% -10%,#3358a8 0%,transparent 55%),radial-gradient(900px 600px at 0% 30%,#1b2f63 0%,transparent 50%),#0a1530;background-attachment:fixed}
.logo.logo-round img{height:46px;border-radius:50%}
header.scrolled{background:rgba(10,21,48,.55);backdrop-filter:blur(18px);box-shadow:0 1px 0 rgba(255,255,255,.12)}
.hdr-inner{color:#F4F7FC}
.hero-overlay{background:linear-gradient(180deg,rgba(10,21,48,.55),rgba(10,21,48,.35) 40%,rgba(10,21,48,.75))}
.hero-inner{color:#fff}
.eyebrow{color:#Bcd4ff}
.btn-primary{background:linear-gradient(135deg,#9cc2ff,#6f9dff);color:#0a1530;box-shadow:0 10px 30px rgba(111,157,255,.4)}
.btn-ghost{background:rgba(255,255,255,.1);backdrop-filter:blur(10px);color:#fff;border:1px solid rgba(255,255,255,.3)}
.btn-ghost:hover{background:rgba(255,255,255,.18)}
.glass{background:rgba(255,255,255,.08);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.18);box-shadow:0 20px 50px rgba(0,0,0,.25)}
.value,.kpi,.svc,.proj,.contact-form,.contact-info{background:rgba(255,255,255,.08);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.18);box-shadow:0 16px 40px rgba(0,0,0,.22)}
.contact-info{padding:24px 26px;border-radius:22px}
.svc:hover{background:rgba(255,255,255,.14);box-shadow:0 24px 60px rgba(0,0,0,.32)}
.svc-ico{background:rgba(127,178,255,.18);border:1px solid rgba(127,178,255,.35)}
.kpi-num{color:#9cc2ff}
.tag{color:#9cc2ff}
.contact-form input,.contact-form textarea{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22)}
.footer{--hair:rgba(255,255,255,.14)}
'''
)

# ---------- THEME 4: Light Minimal ----------
themes[4] = dict(
  name="Светлый минимализм",
  fonts='<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">',
  logo="emblem_silver.png", hero="hero_light.png", header_logo_class="logo-round",
  css=BASE_CSS + '''
:root{--body:'Inter',sans-serif;--head:'Inter',sans-serif;--ink:#1f2d3d;--bg:#FBFCFE;--accent:#3E78B2;--on-accent:#fff;--hair:#E9EEF4;--card-r:18px;--btn-r:999px;--menu-bg:#fff;--menu-ink:#1f2d3d;--field-bg:#fff;--head-w:600}
.logo.logo-round img{height:44px;border-radius:50%}
header.scrolled{background:rgba(251,252,254,.85);backdrop-filter:blur(12px);box-shadow:0 1px 0 #E9EEF4}
.hdr-inner{color:#1f2d3d}
.nav a{font-weight:500}
.hero{min-height:96vh}
.hero-overlay{background:linear-gradient(100deg,rgba(251,252,254,.96) 0%,rgba(251,252,254,.8) 38%,rgba(251,252,254,.25) 75%,transparent 100%)}
.hero-inner{color:#1f2d3d}
.hero h1{font-weight:600;letter-spacing:-.02em}
.eyebrow{color:#3E78B2}
.btn-primary{background:#3E78B2;color:#fff}
.btn-primary:hover{background:#2f6098}
.btn-ghost{background:transparent;color:#1f2d3d;border:1px solid #cdd7e3}
.btn-ghost:hover{border-color:#3E78B2;color:#3E78B2}
.value{background:transparent;border:1px solid #E9EEF4}
.kpi{background:#F3F7FB;border:1px solid #E9EEF4}
.services{background:#F6F9FC}
.svc{background:#fff;border:1px solid #E9EEF4;box-shadow:none}
.svc:hover{box-shadow:0 16px 40px rgba(62,120,178,.12)}
.svc-ico{background:#EAF1F8}
.proj{background:#fff;border:1px solid #E9EEF4}
.contact{background:#fff}
.footer{--hair:#E9EEF4}
.tag{font-weight:600;letter-spacing:.16em}
'''
)

# ---------- THEME 5: Dark Premium (neon/gold glow) ----------
themes[5] = dict(
  name="Тёмная премиальная",
  fonts='<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;700&display=swap" rel="stylesheet">',
  logo="logo_gold.png", hero="hero_dark.png", header_logo_class="",
  css=BASE_CSS + '''
:root{--body:'Manrope',sans-serif;--head:'Space Grotesk',sans-serif;--ink:#D8DEE9;--bg:#0E1726;--accent:#E6C566;--on-accent:#0E1726;--hair:rgba(230,197,102,.18);--card-r:16px;--btn-r:10px;--menu-bg:#0a1018;--field-bg:rgba(255,255,255,.04)}
body{background:radial-gradient(900px 500px at 85% -5%,rgba(230,197,102,.1),transparent 60%),#0E1726;background-attachment:fixed}
header.scrolled{background:rgba(14,23,38,.85);backdrop-filter:blur(14px);box-shadow:0 1px 0 rgba(230,197,102,.2)}
.hdr-inner{color:#D8DEE9}
.lang button.is-active{color:#E6C566}
.hero-overlay{background:linear-gradient(95deg,rgba(8,12,20,.95) 0%,rgba(14,23,38,.7) 55%,rgba(14,23,38,.3) 100%)}
.hero-inner{color:#fff}
.eyebrow{color:#E6C566;text-shadow:0 0 22px rgba(230,197,102,.5)}
.hero h1{text-shadow:0 0 40px rgba(0,0,0,.6)}
.btn-primary{background:linear-gradient(135deg,#E6C566,#C9A44C);color:#0E1726;box-shadow:0 0 30px rgba(230,197,102,.4)}
.btn-primary:hover{box-shadow:0 0 44px rgba(230,197,102,.65)}
.btn-ghost{background:transparent;color:#E6C566;border:1px solid rgba(230,197,102,.5)}
.btn-ghost:hover{background:rgba(230,197,102,.1);box-shadow:0 0 24px rgba(230,197,102,.25)}
.tag{color:#E6C566}
.value{background:rgba(255,255,255,.03);border:1px solid rgba(230,197,102,.18)}
.kpi{background:rgba(255,255,255,.03);border:1px solid rgba(230,197,102,.22)}
.kpi-num{color:#E6C566;text-shadow:0 0 24px rgba(230,197,102,.45)}
.services{background:#0a1018}
.svc{background:linear-gradient(160deg,rgba(255,255,255,.05),rgba(255,255,255,.02));border:1px solid rgba(230,197,102,.16)}
.svc:hover{border-color:rgba(230,197,102,.55);box-shadow:0 0 50px rgba(230,197,102,.18)}
.svc-ico{background:rgba(230,197,102,.12);border:1px solid rgba(230,197,102,.35);box-shadow:0 0 20px rgba(230,197,102,.15)}
.svc-num{color:#E6C566}
.proj{background:rgba(255,255,255,.03);border:1px solid rgba(230,197,102,.16)}
.proj:hover{box-shadow:0 0 50px rgba(230,197,102,.15)}
.contact-form input,.contact-form textarea{border:1px solid rgba(230,197,102,.25)}
.footer{background:#0a1018;--hair:rgba(230,197,102,.16)}
'''
)

# ---------- THEME 6: Nature / Eco ----------
themes[6] = dict(
  name="Природа / эко",
  fonts='<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=Nunito+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">',
  logo="emblem_gold.png", hero="hero_development.png", header_logo_class="logo-round",
  css=BASE_CSS + '''
:root{--body:'Nunito Sans',sans-serif;--head:'Fraunces',serif;--ink:#24332b;--bg:#FBF8F1;--accent:#3E7C59;--on-accent:#fff;--hair:#E4DDCD;--card-r:26px;--btn-r:999px;--menu-bg:#1f3a2c;--field-bg:#fff;--head-w:600}
.logo.logo-round img{height:46px;border-radius:50%}
header.scrolled{background:rgba(251,248,241,.9);backdrop-filter:blur(12px);box-shadow:0 1px 0 #E4DDCD}
.hdr-inner{color:#fff}
header.scrolled .hdr-inner{color:#24332b}
.nav a::after{background:#3E7C59}
.hero{min-height:98vh}
.hero-overlay{background:linear-gradient(105deg,rgba(31,58,44,.85) 0%,rgba(31,58,44,.45) 55%,rgba(62,124,89,.2) 100%)}
.hero-inner{color:#fff}
.eyebrow{color:#C9A44C}
.hero h1{font-weight:600}
.btn-primary{background:#3E7C59;color:#fff}
.btn-primary:hover{background:#336649}
.hero .btn-ghost{background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.5)}
.btn-ghost:hover{background:rgba(255,255,255,.2)}
.tag{color:#C9A44C;letter-spacing:.16em}
.about{background:#FBF8F1}
.value{background:#fff;border:1px solid #E4DDCD;box-shadow:0 8px 24px rgba(36,51,43,.05)}
.v-ico{color:#3E7C59}
.kpi{background:#1f3a2c;color:#F3EFE5;border-radius:26px}
.kpi-num{color:#C9A44C}
.kpi-lbl{color:#cdd6cd}
.services{background:#F1ECE0}
.svc{background:#fff;border:1px solid #E4DDCD;box-shadow:0 8px 28px rgba(36,51,43,.06)}
.svc:hover{box-shadow:0 20px 44px rgba(36,51,43,.12)}
.svc-ico{background:#E9F0EA;color:#3E7C59;border-radius:50%}
.svc-num{color:#3E7C59}
.proj{background:#fff;border:1px solid #E4DDCD}
.proj-img{border-radius:0}
.contact{background:#1f3a2c;color:#F3EFE5;--ink:#F3EFE5;--hair:rgba(255,255,255,.16);--field-bg:rgba(255,255,255,.06)}
.contact .tag{color:#E6C566}
.contact .btn-primary{background:#C9A44C;color:#1f3a2c}
.contact .ci-lbl{color:rgba(255,255,255,.55)}
.footer{background:#16291f;color:#F3EFE5;--hair:rgba(255,255,255,.1)}
'''
)

for i in range(1,7):
    t=themes[i]
    d=os.path.join(BASE,f"template{i}")
    os.makedirs(d,exist_ok=True)
    html=page(t["name"],t["fonts"],t["css"],t["logo"],t["hero"],header_logo_class=t["header_logo_class"],body_class=f"theme{i}")
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(html)
    print("wrote template",i,t["name"])

# ---------- GALLERY index.html ----------
descs={
 1:{"tj":"Сине-серебристый, тоза, солидный корпоративный стиль.","en":"Blue-silver, clean grid, large type — solid corporate look."},
 2:{"tj":"Navy + золото, элегантные засечки, премиальная атмосфера.","en":"Navy + gold, elegant serifs, premium luxury feel."},
 3:{"tj":"Стекломорфизм: полупрозрачные карточки blur, яркий фон.","en":"Glassmorphism: frosted translucent cards, vivid background."},
 4:{"tj":"Светлый минимализм: воздух, тонкие линии, спокойствие.","en":"Light minimalism: airy, thin lines, calm pastel blue."},
 5:{"tj":"Тёмная премиальная тема с золотым свечением.","en":"Dark premium theme with glowing gold accents."},
 6:{"tj":"Зелёно-земляные эко-тона, органичные формы.","en":"Warm green-earth eco tones, organic rounded shapes."},
}
cards=[]
for i in range(1,7):
    t=themes[i]; dd=descs[i]
    cards.append(f'''<a class="g-card reveal g-{i}" href="template{i}/index.html">
      <div class="g-preview"><iframe src="template{i}/index.html" scrolling="no" loading="lazy" tabindex="-1" title="{t['name']}"></iframe><span class="g-shield"></span></div>
      <div class="g-body">
        <span class="g-num">0{i}</span>
        <h3>{t['name']}</h3>
        <p data-tj="{esc(dd['tj'])}" data-en="{esc(dd['en'])}">{dd['tj']}</p>
        <span class="g-btn" data-tj="Просмотреть →" data-en="View →">Просмотреть →</span>
      </div>
    </a>''')

gallery=f'''<!DOCTYPE html>
<html lang="tj">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Рушди Манотиқи Кӯҳистон — Дизайн-шаблоны</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Manrope',sans-serif;background:#0E1726;color:#E7ECF4;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
body{{background:radial-gradient(1000px 600px at 80% -10%,rgba(127,178,255,.14),transparent 60%),radial-gradient(800px 500px at 0% 20%,rgba(230,197,102,.08),transparent 55%),#0E1726;background-attachment:fixed}}
img{{max-width:100%;display:block}}
.wrap{{max-width:1240px;margin:0 auto;padding:0 28px}}
a{{color:inherit;text-decoration:none}}
.g-head{{padding:48px 0 18px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}}
.g-brand{{display:flex;align-items:center;gap:16px}}
.g-brand img{{height:54px;width:auto}}
.g-brand .bt{{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:1.15rem;line-height:1.15}}
.g-brand .bs{{font-size:.8rem;opacity:.6}}
.lang{{display:flex;gap:6px;align-items:center;font-weight:700}}
.lang button{{background:none;border:none;color:#E7ECF4;opacity:.5;font-weight:700;cursor:pointer;font-size:.9rem;font-family:inherit}}
.lang button.is-active{{opacity:1;color:#9cc2ff}}
.lang-sep{{opacity:.4}}
.hero-line{{padding:30px 0 56px;max-width:880px}}
.hero-line .eyebrow{{font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:#9cc2ff;display:block;margin-bottom:18px}}
.hero-line h1{{font-family:'Space Grotesk',sans-serif;font-size:clamp(2rem,5vw,3.6rem);line-height:1.08;margin-bottom:20px;font-weight:700}}
.hero-line p{{font-size:1.1rem;opacity:.78;max-width:640px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;padding-bottom:80px}}
.g-card{{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:20px;overflow:hidden;transition:transform .35s,box-shadow .35s,border-color .35s;display:flex;flex-direction:column}}
.g-card:hover{{transform:translateY(-8px);border-color:rgba(127,178,255,.5);box-shadow:0 30px 70px rgba(0,0,0,.45)}}
.g-preview{{position:relative;height:300px;overflow:hidden;background:#0a1018;border-bottom:1px solid rgba(255,255,255,.08)}}
.g-preview iframe{{width:1280px;height:854px;border:0;transform:scale(.33);transform-origin:top left;pointer-events:none}}
.g-shield{{position:absolute;inset:0}}
.g-body{{padding:24px 26px 28px;position:relative}}
.g-num{{position:absolute;top:22px;right:26px;font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:1rem;opacity:.3}}
.g-body h3{{font-family:'Space Grotesk',sans-serif;font-size:1.3rem;font-weight:600;margin-bottom:10px}}
.g-body p{{font-size:.94rem;opacity:.72;margin-bottom:18px;min-height:48px}}
.g-btn{{font-weight:700;color:#9cc2ff;font-size:.95rem}}
.g-1 .g-btn{{color:#9cc2ff}} .g-2 .g-btn{{color:#E6C566}} .g-3 .g-btn{{color:#9cc2ff}} .g-4 .g-btn{{color:#7FB2FF}} .g-5 .g-btn{{color:#E6C566}} .g-6 .g-btn{{color:#7FD6A0}}
.g-foot{{padding:30px 0 56px;border-top:1px solid rgba(255,255,255,.08);font-size:.88rem;opacity:.6}}
.reveal{{opacity:0;transform:translateY(28px);transition:opacity .7s cubic-bezier(.2,.7,.2,1),transform .7s cubic-bezier(.2,.7,.2,1)}}
.reveal.revealed{{opacity:1;transform:none}}
@media(max-width:980px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:640px){{.grid{{grid-template-columns:1fr}}.wrap{{padding:0 20px}}.g-preview{{height:260px}}}}
</style>
</head>
<body>
<div class="wrap">
  <header class="g-head">
    <div class="g-brand">
      <img src="assets/img/logo_silver.png" alt="РМК">
    </div>
    <div class="lang">
      <button data-lang-btn="tj" class="is-active">TJ</button><span class="lang-sep">/</span><button data-lang-btn="en">EN</button>
    </div>
  </header>

  <section class="hero-line">
    <span class="eyebrow" data-tj="Варианты дизайна на выбор" data-en="Design options to choose from">Варианты дизайна на выбор</span>
    <h1 data-tj="6 дизайн-шаблонов сайта-визитки" data-en="6 website design templates">6 дизайн-шаблонов сайта-визитки</h1>
    <p data-tj="Ниже представлены шесть современных вариантов оформления сайта компании «Рушди Манотиқи Кӯҳистон». Откройте каждый, чтобы увидеть полную страницу, и выберите понравившийся стиль." data-en="Below are six modern design options for the «Mountain Regions Development (RMK)» website. Open each one to see the full page and choose your favourite style.">Ниже представлены шесть современных вариантов оформления сайта компании «Рушди Манотиқи Кӯҳистон». Откройте каждый, чтобы увидеть полную страницу, и выберите понравившийся стиль.</p>
  </section>

  <main class="grid">
    {''.join(cards)}
  </main>

  <footer class="g-foot">
    <p data-tj="© 2026 Рушди Манотиқи Кӯҳистон — выбор дизайна" data-en="© 2026 Mountain Regions Development — design selection">© 2026 Рушди Манотиқи Кӯҳистон — выбор дизайна</p>
  </footer>
</div>
<script>
(function(){{
  function applyLang(l){{document.documentElement.lang=l;document.querySelectorAll('[data-tj]').forEach(function(e){{var v=e.getAttribute('data-'+l);if(v!==null)e.textContent=v;}});document.querySelectorAll('[data-lang-btn]').forEach(function(b){{b.classList.toggle('is-active',b.getAttribute('data-lang-btn')===l);}});}}
  document.querySelectorAll('[data-lang-btn]').forEach(function(b){{b.addEventListener('click',function(){{applyLang(b.getAttribute('data-lang-btn'));}});}});
  applyLang('tj');
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('revealed');io.unobserve(e.target);}}}});}},{{threshold:.12}});
  document.querySelectorAll('.reveal').forEach(function(el,i){{el.style.transitionDelay=(Math.min(i,6)*60)+'ms';io.observe(el);}});
}})();
</script>
</body>
</html>'''
open(os.path.join(BASE,"index.html"),"w",encoding="utf-8").write(gallery)
print("wrote gallery")
