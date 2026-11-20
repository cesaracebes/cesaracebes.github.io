# -*- coding: utf-8 -*-
"""
Static site generator for cesaracebes.github.io (Python 3, standard library only).

    python3 _source/build.py

Reads _source/content.py and writes /en, /es, /ca, index.html, 404.html and sitemap.xml
at the repository root. Assets live in /assets and are not touched.
"""
import html
import os
import shutil
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content as C  # noqa: E402

YEAR = date.today().year


def t(x, lang):
    return x.get(lang, x.get("en", "")) if isinstance(x, dict) else x


def e(s):
    return html.escape(s or "", quote=True)


# ------------------------------------------------------------------ media
def media(item, lang, label="", ratio="", extra_class=""):
    """item = {"video": {"provider", "id"}, "image": "path"} -> iframe, <img> or empty placeholder tile."""
    item = item or {}
    video = item.get("video") or {}
    image = item.get("image", "")
    cls = ("media " + extra_class).strip()
    style = ' style="aspect-ratio:%s"' % ratio if ratio else ""
    if isinstance(video, dict) and video.get("id"):
        vid = e(video["id"])
        if video.get("provider") == "youtube":
            src = ("https://www.youtube-nocookie.com/embed/%s?autoplay=1&amp;mute=1&amp;loop=1&amp;playlist=%s"
                   "&amp;controls=0&amp;playsinline=1&amp;rel=0&amp;modestbranding=1" % (vid, vid))
        elif video.get("provider") == "sketchfab":
            # interactive 3D model; shows its thumbnail + play button until clicked (light on load)
            src = ("https://sketchfab.com/models/%s/embed?autostart=0&amp;dnt=1&amp;ui_theme=dark"
                   "&amp;ui_hint=2&amp;ui_infos=0&amp;ui_watermark_link=0" % vid)
            cls += " is-3d"
        else:
            src = "https://player.vimeo.com/video/%s?background=1&amp;dnt=1" % vid
        return ('<div class="%s"%s><iframe src="%s" title="%s" loading="lazy" '
                'allow="autoplay; fullscreen; picture-in-picture; xr-spatial-tracking" allowfullscreen></iframe></div>'
                % (cls, style, src, e(label)))
    if image:
        return '<div class="%s"%s><img src="{ROOT}%s" alt="%s" loading="lazy"></div>' % (cls, style, e(image), e(label))
    note = C.UI["video_soon"] if "video" in item else C.UI["image_soon"]
    return ('<div class="%s is-empty"%s><span class="media-note">%s</span></div>'
            % (cls, style, e(t(note, lang))))


# ------------------------------------------------------------------ layout
def nav_html(lang, slug, pre):
    items = []
    for s, label, _num in C.PAGES:
        cur = ' aria-current="page"' if s == slug else ""
        items.append('<li><a href="%s%s/%s/"%s>%s</a></li>' % (pre, lang, s, cur, e(t(label, lang))))
    return "".join(items)


def lang_links(lang, slug, pre):
    out = []
    for L in C.LANGS:
        path = "%s%s/%s" % (pre, L, (slug + "/") if slug else "")
        cur = ' aria-current="true"' if L == lang else ""
        out.append('<li><a href="%s" hreflang="%s" lang="%s"%s title="%s">%s</a></li>'
                   % (path, L, L, cur, e(t(C.UI["lang_name"], L)), L.upper()))
    return "".join(out)


def page(lang, slug, title, body, desc=""):
    depth = 2 if slug else 1
    pre = "../" * depth
    full_title = C.PERSON["name"] if not slug else "%s · %s" % (title, C.PERSON["name"])
    desc = desc or t(C.HOME["meta"], lang)
    alternates = "".join(
        '<link rel="alternate" hreflang="%s" href="%s/%s/%s">' % (L, C.SITE_URL, L, (slug + "/") if slug else "")
        for L in C.LANGS)
    ui = C.UI
    links = "".join('<li><a href="%s" rel="me">%s</a></li>' % (e(u), e(n)) for n, u in C.PERSON["links"])
    out = """<!doctype html>
<html lang="{lang}" data-theme="night">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}/{lang}/{slugpath}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{site}/en/{slugpath}">
<script>(function(){{var t=(location.search.match(/[?&]theme=(day|night)/)||[])[1];if(!t){{try{{t=localStorage.getItem("theme")}}catch(_){{}}}}if(t!=="day"&&t!=="night"){{t=window.matchMedia&&matchMedia("(prefers-color-scheme: light)").matches?"day":"night"}}document.documentElement.setAttribute("data-theme",t)}})();</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;700;900&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/css/style.css">
<link rel="icon" href="{pre}assets/img/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
</head>
<body>
<a class="skip" href="#main">{skip}</a>
<header class="site-header">
  <div class="wrap header-bar">
    <a class="brand" href="{pre}{lang}/">{short}</a>
    <nav class="nav" aria-label="{menu}"><ul>{nav}</ul></nav>
    <div class="tools">
      <ul class="langs">{langs}</ul>
      <button class="theme-toggle" type="button"
        data-to-day="{to_day}" data-to-night="{to_night}"
        data-to-day-label="{to_day_label}" data-to-night-label="{to_night_label}">{to_day}</button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-bar">
    <a href="mailto:{email}">{email}</a>
    <ul class="footer-links">{links}</ul>
    <span class="muted">© {year} {name}</span>
  </div>
</footer>
<script src="{pre}assets/js/site.js" defer></script>
</body>
</html>
""".format(
        lang=lang, title=e(full_title), desc=e(desc), site=C.SITE_URL,
        slugpath=(slug + "/") if slug else "", alternates=alternates, pre=pre,
        skip=e(t(ui["skip"], lang)), short=e(C.PERSON["short"]), menu=e(t(ui["menu"], lang)),
        nav=nav_html(lang, slug, pre), langs=lang_links(lang, slug, pre),
        to_day=e(t(ui["to_day"], lang)), to_night=e(t(ui["to_night"], lang)),
        to_day_label=e(t(ui["to_day_label"], lang)), to_night_label=e(t(ui["to_night_label"], lang)),
        body=body, email=e(C.PERSON["email"]), links=links, year=YEAR, name=e(C.PERSON["name"]))
    return out.replace("{ROOT}", pre)


def page_head(num, title, desc, kicker=""):
    k = '<p class="kicker">%s</p>' % e(kicker) if kicker else ""
    return """<section class="wrap page-head">
  <span class="big-num" aria-hidden="true">{num}</span>
  <div class="page-head-title">{k}<h1>{title}</h1></div>
  <p class="lead">{desc}</p>
</section>""".format(num=e(num), k=k, title=e(title), desc=e(desc))


def section_title(title, note=""):
    n = '<span class="muted">%s</span>' % e(note) if note else ""
    return '<div class="sec-title"><h2>%s</h2>%s</div>' % (e(title), n)


def next_areas(lang, current):
    items = []
    for s, label, num in C.PAGES:
        if num and s != current:
            items.append('<a href="../%s/"><span><span class="accent-text">%s</span> %s</span><span aria-hidden="true">→</span></a>'
                         % (s, num, e(t(label, lang))))
    return '<nav class="wrap next-areas" aria-label="%s">%s</nav>' % (e(t(C.UI["menu"], lang)), "".join(items))


def case_tile(case, lang, cls=""):
    title = t(case["title"], lang)
    spec = case["spec"]
    return ('<figure class="tile %s" data-spec="%s">%s<figcaption class="tile-cap">%s</figcaption></figure>'
            % (cls, e(spec), media({"video": case.get("video"), "image": case.get("image", "")}, lang, title), e(title)))


def comm_row(c, lang):
    tag = t(C.UI[c["type"]], lang)
    extra = ""
    if c.get("selected"):
        extra = ' · <strong class="hl">%s</strong>' % e(t(C.UI["selected"], lang))
    ref = ' · %s' % e(c["ref"]) if c.get("ref") else ""
    return ('<li class="row3"><span class="y">%s</span><span class="v">%s</span>'
            '<span class="ti"><span lang="%s">%s</span> <span class="muted">· %s%s</span>%s</span></li>'
            % (e(c["year"]), e(c["venue"]), c.get("tl", "es"), e(c["title"]), e(tag), ref, extra))


def pub_row(p, lang, thumb=False):
    links = "".join('<a class="btn" href="%s">%s</a>' % (e(u), e(t(C.UI["code"], lang) if n == "CODE" else n))
                    for n, u in p["links"])
    th = ""
    if thumb and p.get("image"):
        th = media({"image": p["image"]}, lang, p["title"], extra_class="thumb")
    elif thumb:
        th = '<span class="thumb thumb-none" aria-hidden="true"></span>'  # keeps the grid column
    return ('<li class="pub%s"><span class="pub-year accent-text">%s</span>%s'
            '<span class="pub-body"><span class="pub-title" lang="en">%s</span><span class="muted">%s</span>'
            '<span class="pub-venue">%s</span></span><span class="pub-links">%s</span></li>'
            % (" has-thumb" if thumb else "", e(p["year"]), th, e(p["title"]), e(p["authors"]), e(p["venue"]), links))


def stat(n, label, solid=False, href=""):
    tag = "a" if href else "div"
    h = ' href="%s"' % href if href else ""
    return '<%s class="stat%s"%s><span class="stat-n">%s</span><span class="stat-l">%s</span></%s>' % (
        tag, " solid" if solid else "", h, e(n), e(label), tag)


N_THESES = str(sum(int(n) for n, _ in C.TEACHING["stats"][:2]))


# ------------------------------------------------------------------ pages
def home(lang):
    ui = C.UI
    areas = C.AREAS
    cases = "".join(case_tile(c, lang, "m%d" % (i + 1)) for i, c in enumerate(C.CASES[:6]))
    rows = []
    for slug, _label, num in C.PAGES:
        if num and slug != "planning":
            rows.append("""<a class="area-row" href="%s/">
  <span class="area-num accent-text">%s</span>
  <span class="area-title">%s</span>
  <span class="area-sum">%s</span>
  <span class="area-arrow" aria-hidden="true">→</span>
</a>""" % (slug, num, e(t(areas[slug]["title"], lang)), e(t(areas[slug]["summary"], lang))))
    n_pubs = str(len(C.PUBLICATIONS))
    n_comms = str(len(C.COMMUNICATIONS))
    body = """<section class="wrap hero">
  <h1 class="hero-name">{name_lines}</h1>
  <div class="hero-card">
    <p class="kicker">{kicker}</p>
    <p class="hero-desc">{desc}</p>
  </div>
</section>
<section class="wrap block">
  <a class="area-head" href="planning/">
    <span class="area-num accent-text">01</span>
    <h2 class="area-title">{a1}</h2>
    <span class="muted area-note">{cases_note}</span>
  </a>
  <div class="mosaic">{cases}</div>
</section>
<section class="wrap block areas">{rows}</section>
<section class="wrap block output-band">
  <h2 class="label">{output}</h2>
  <div class="mini-stats">
    <div><span class="mini-n accent-text">{n_pubs}</span><span>{l_pubs}</span></div>
    <div><span class="mini-n accent-text">{n_comms}</span><span>{l_comms}</span></div>
    <div><span class="mini-n accent-text">{n_theses}</span><span>{l_theses}</span></div>
  </div>
  <a class="underline-link" href="publications/">{all_pubs} →</a>
</section>""".format(
        name_lines="<br>".join(e(w) for w in C.PERSON["name"].split()), kicker=e(t(C.HOME["kicker"], lang)), desc=e(t(C.HOME["desc"], lang)),
        a1=e(t(areas["planning"]["title"], lang)), cases_note=e(t(ui["cases_note"], lang)), cases=cases,
        rows="".join(rows), output=e(t(ui["output"], lang)),
        n_pubs=n_pubs, n_comms=n_comms, n_theses=N_THESES,
        l_pubs=e(t(ui["n_pubs"], lang)), l_comms=e(t(ui["n_comms"], lang)), l_theses=e(t(ui["n_theses"], lang)),
        all_pubs=e(t(ui["all_pubs"], lang)))
    return page(lang, "", "", body)


def planning(lang):
    P = C.PLANNING
    ui = C.UI
    steps = "".join('<li><span class="step-n accent-text">%d</span><strong>%s</strong><span class="muted">%s</span></li>'
                    % (i + 1, e(t(a, lang)), e(t(b, lang))) for i, (a, b) in enumerate(P["steps"]))
    twins = "".join('<figure class="twin">%s<figcaption><strong>%s</strong><span class="muted">%s</span></figcaption></figure>'
                    % (media({"video": v}, lang, t(a, lang)), e(t(a, lang)), e(t(b, lang))) for a, b, v in P["twin_uses"])
    used = []
    for c in C.CASES:
        if c["spec"] not in used:
            used.append(c["spec"])
    chips = ['<button type="button" class="chip" aria-pressed="true" data-filter="all">%s</button>' % e(t(ui["all"], lang))]
    chips += ['<button type="button" class="chip" aria-pressed="false" data-filter="%s">%s</button>'
              % (s, e(t(C.SPECIALTIES[s], lang))) for s in used]
    cases = "".join(case_tile(c, lang, "big" if i == 0 else ("wide" if c.get("wide") else ""))
                    for i, c in enumerate(C.CASES))
    pubs = [p for p in C.PUBLICATIONS if p["id"] == "fcvm2023"]
    comms = "".join(comm_row(c, lang) for c in C.COMMUNICATIONS if c.get("planning"))
    pub_rows = "".join('<li class="row3"><span class="y">%s</span><span class="v">%s</span><span class="ti"><span lang="en">%s</span> <span class="muted">· %s</span></span></li>'
                       % (e(p["year"]), e(p["venue"]), e(p["title"]), e(t(ui["case_report"], lang))) for p in pubs)
    body = page_head("01", t(C.AREAS["planning"]["title"], lang), t(P["desc"], lang)) + """
<section class="wrap block">
  <figure class="reel">{reel}<figcaption class="tag">{reel_label}</figcaption></figure>
</section>
<section class="wrap block"><ol class="steps steps-4">{steps}</ol></section>
<section class="wrap block">
  {twin_head}
  <div class="twins">{twins}</div>
</section>
<section class="wrap block">
  {cases_head}
  <div class="chips" role="group" aria-label="{filter}">{chips}</div>
  <div class="case-grid" data-filterable>{cases}</div>
</section>
<section class="wrap block split">
  <h2 class="split-title">{presented}</h2>
  <ol class="rows">{comms}{pub_rows}</ol>
</section>
""".format(reel=media({"video": P["reel"]}, lang, t(P["reel_label"], lang)), reel_label=e(t(P["reel_label"], lang)),
           steps=steps, twin_head=section_title(t(P["twin_title"], lang), t(P["twin_desc"], lang)), twins=twins,
           cases_head=section_title(t(ui["cases"], lang), t(ui["cases_note"], lang)),
           filter=e(t(ui["filter"], lang)), chips="".join(chips), cases=cases,
           presented=e(t(ui["presented"], lang)), comms=comms, pub_rows=pub_rows) + next_areas(lang, "planning")
    return page(lang, "planning", t(C.AREAS["planning"]["title"], lang), body, t(P["desc"], lang))


# Schematic cross-sections of the three printing processes. Colours come from CSS tokens
# (currentColor = ink, .acc = accent), so they follow the day / night theme.
def _layers(x, y0, w, n, step=10, h=8):
    return "".join('<rect class="line" x="%d" y="%d" width="%d" height="%d" rx="3"/>' % (x, y0 + i * step, w, h)
                   for i in range(n))


PRINTER_SVG = {
    # FDM: nozzle laying the current layer on a stack, filament feeding from above
    "FDM": ('<rect class="ink" x="30" y="150" width="180" height="8"/>'
            + _layers(70, 91, 100, 6)
            + '<rect class="acc" x="70" y="81" width="62" height="8" rx="3"/>'
            '<line class="line thick" x1="140" y1="6" x2="140" y2="44"/>'
            '<rect class="ink" x="122" y="44" width="36" height="22"/>'
            '<polygon class="ink" points="131,66 149,66 140,78"/>'
            '<line class="line" x1="166" y1="55" x2="206" y2="55"/><polygon class="ink" points="206,50 216,55 206,60"/>'),
    # SLA (inverted): platform lifts the part out of a resin tank; light cures from below
    "SLA": ('<rect class="ink" x="112" y="4" width="16" height="24"/>'
            '<rect class="ink" x="60" y="28" width="120" height="10"/>'
            + _layers(90, 40, 60, 9)
            + '<rect class="acc" x="90" y="130" width="60" height="8" rx="3"/>'
            '<rect class="acc-soft" x="32" y="112" width="176" height="28"/>'
            '<polyline class="line" points="30,100 30,141 210,141 210,100"/>'
            '<rect class="line" x="40" y="148" width="160" height="8"/>'
            '<rect class="acc" x="90" y="148" width="60" height="8"/>'),
    # SLS: laser sinters the top of a powder bed; roller spreads fresh powder from the feed bed
    "SLS": ('<defs><pattern id="pdots" width="6" height="6" patternUnits="userSpaceOnUse">'
            '<circle class="ink" cx="3" cy="3" r="1"/></pattern></defs>'
            '<rect fill="url(#pdots)" x="14" y="104" width="46" height="54"/>'
            '<rect class="line" x="14" y="104" width="46" height="54"/>'
            '<rect fill="url(#pdots)" x="74" y="96" width="132" height="62"/>'
            '<rect class="line" x="74" y="96" width="132" height="62"/>'
            '<path class="ink" d="M104 150 V116 H118 V134 H160 V116 H174 V150 Z"/>'
            '<rect class="acc" x="104" y="110" width="14" height="6"/><rect class="acc" x="160" y="110" width="14" height="6"/>'
            '<circle class="line" cx="68" cy="88" r="7"/>'
            '<line class="line" x1="80" y1="80" x2="100" y2="80"/><polygon class="ink" points="100,75 110,80 100,85"/>'
            '<rect class="ink" x="150" y="8" width="44" height="18"/>'
            '<line class="acc-line" x1="164" y1="26" x2="167" y2="108"/><circle class="acc" cx="167" cy="110" r="4"/>'),
}


def printer_card(key, machine, how, lang):
    return ('<li class="printer"><svg class="pdiag" viewBox="0 0 240 170" role="img" aria-label="%s">%s</svg>'
            '<span class="tech-k accent-text">%s</span><span class="tech-v">%s</span><span class="muted">%s</span></li>'
            % (e("%s · %s" % (key, t(how, lang))), PRINTER_SVG[key], e(key), e(machine), e(t(how, lang))))


def devices(lang):
    D = C.DEVICES
    ui = C.UI
    printers = "".join(printer_card(k, m, h, lang) for k, m, h in D["printers"])
    gallery = "".join('<figure class="gal">%s<figcaption><strong>%s</strong><span class="muted">%s</span></figcaption></figure>'
                      % (media(g[2] if len(g) > 2 else {"video": {}}, lang, t(g[0], lang)), e(t(g[0], lang)), e(t(g[1], lang)))
                      for g in D["gallery"])
    also = "".join("<li>%s</li>" % e(t(x, lang)) for x in D["also"])
    tech = "".join('<li class="tech"><span class="tech-k%s">%s</span><span class="tech-v">%s</span></li>'
                   % (" accent-text" if k != "CAD" else "", e(k), e(v)) for k, v in D["tech"])
    body = page_head("02", t(D["title"], lang), t(D["desc"], lang), t(D["kicker"], lang)) + """
<section class="wrap block">
  {gal_head}
  <div class="gallery">{gallery}</div>
</section>
<section class="wrap block split">
  <h2 class="split-title">{also_t}</h2>
  <ul class="rows plain">{also}</ul>
</section>
<section class="wrap block split">
  <h2 class="split-title">{tech_t}</h2>
  <div><ul class="printers">{printers}</ul><ul class="rows techs">{tech}</ul></div>
</section>
""".format(gal_head=section_title(t(ui["planned"], lang), t(ui["planned_note"], lang)), gallery=gallery,
           also_t=e(t(ui["also"], lang)), also=also, tech_t=e(t(ui["technology"], lang)), tech=tech,
           printers=printers) + next_areas(lang, "devices")
    return page(lang, "devices", t(D["title"], lang), body, t(D["desc"], lang))


# Schematic flags (shape only, in theme tokens): EU ring of 12 stars, Spain 1:2:1 bands, Catalonia 9 stripes.
def _eu_stars():
    import math
    return "".join('<circle class="acc" cx="%.2f" cy="%.2f" r="1.9"/>'
                   % (30 + 12 * math.cos(math.radians(30 * i)), 20 + 12 * math.sin(math.radians(30 * i)))
                   for i in range(12))


FLAG_SVG = {
    "eu": _eu_stars(),
    "es": '<rect class="acc" x="0" y="0" width="60" height="10"/><rect class="acc" x="0" y="30" width="60" height="10"/>',
    "cat": "".join('<rect class="acc" x="0" y="%.3f" width="60" height="%.3f"/>' % (40 / 9 * (2 * i + 1), 40 / 9)
                   for i in range(4)),
}
for _k in FLAG_SVG:
    FLAG_SVG[_k] += '<rect class="line" x="1" y="1" width="58" height="38"/>'


def regulatory(lang):
    R = C.REGULATORY
    blocks = []
    for i, (big, name, sub) in enumerate(R["blocks"]):
        blocks.append('<div class="reg-block%s"><span class="reg-big">%s</span><span class="reg-txt"><strong>%s</strong><span>%s</span></span></div>'
                      % (" solid" if i == 0 else "", e(t(big, lang)), e(t(name, lang)), e(t(sub, lang))))
    life = "".join('<li><span class="step-n accent-text">%d</span><strong>%s</strong><span class="muted">%s</span></li>'
                   % (i + 1, e(t(a, lang)), e(t(b, lang))) for i, (a, b) in enumerate(R["life"]))
    auth = "".join('<li class="lettered"><span class="letter accent-text">%s</span><span>%s</span></li>'
                   % ("ABC"[i], e(t(x, lang))) for i, x in enumerate(R["auth"]))
    fw, last = [], None
    for jur, k, v in R["framework"]:
        if jur != last:
            fw.append('<li class="fw-group"><svg class="flag" viewBox="0 0 60 40" aria-hidden="true">%s</svg>'
                      '<span>%s</span></li>' % (FLAG_SVG[jur], e(t(R["jurisdictions"][jur], lang))))
            last = jur
        fw.append('<li class="fw"><span class="fw-k">%s</span><span>%s</span></li>' % (e(t(k, lang)), e(t(v, lang))))
    fw = "".join(fw)
    title = t(C.AREAS["regulatory"]["title"], lang)
    body = page_head("03", title, t(R["desc"], lang)) + """
<section class="wrap block"><div class="reg-blocks">{blocks}</div></section>
<section class="wrap block">
  {life_head}
  <ol class="steps steps-6">{life}</ol>
</section>
<section class="wrap block split">
  <h2 class="split-title">{auth_t}</h2>
  <ul class="rows plain big-rows">{auth}</ul>
</section>
<section class="wrap block split">
  <h2 class="split-title">{fw_t}</h2>
  <ul class="rows">{fw}</ul>
</section>
""".format(blocks="".join(blocks), life_head=section_title(t(R["life_title"], lang)), life=life,
           auth_t=e(t(R["auth_title"], lang)), auth=auth, fw_t=e(t(R["fw_title"], lang)), fw=fw) + next_areas(lang, "regulatory")
    return page(lang, "regulatory", title, body, t(R["desc"], lang))


def ai(lang):
    A = C.AI
    ui = C.UI
    pubs = [p for pid in A["pubs"] for p in C.PUBLICATIONS if p["id"] == pid]
    rows = "".join(pub_row(p, lang, thumb=True) for p in pubs)
    title = t(C.AREAS["ai"]["title"], lang)
    body = page_head("04", title, t(A["desc"], lang)) + """
<section class="wrap block ai-hero">
  <figure class="ai-media">{media}<figcaption class="tag">{label}</figcaption></figure>
  <div class="focus-card"><p class="kicker">{focus_t}</p><p class="focus-txt">{focus}</p></div>
</section>
<section class="wrap block">
  {pubs_head}
  <ol class="pubs">{rows}</ol>
</section>
<section class="wrap block two-col">
  <div class="mini"><p class="label">{sup_t}</p><span class="mini-n accent-text">{n_theses}</span><span class="muted">{sup_l} · UPF · UB · UPC</span></div>
  <div class="mini"><p class="label">{code_t}</p><a class="mini-link" href="https://github.com/cesaracebes">github.com/cesaracebes →</a><span class="muted">{code_note}</span></div>
</section>
""".format(media=media(A["hero_media"], lang, t(A["hero_label"], lang)), label=e(t(A["hero_label"], lang)),
           focus_t=e(t(ui["focus"], lang)), focus=e(t(A["focus"], lang)),
           pubs_head=section_title(t(ui["publications"], lang)), rows=rows,
           sup_t=e(t(ui["supervision"], lang)), n_theses=N_THESES, sup_l=e(t(ui["n_theses"], lang)),
           code_t=e(t(ui["code"], lang)), code_note=e(A["code_note"])) + next_areas(lang, "ai")
    return page(lang, "ai", title, body, t(A["desc"], lang))


def publications(lang):
    ui = C.UI
    rows = "".join(pub_row(p, lang) for p in C.PUBLICATIONS)
    comms = "".join(comm_row(c, lang) for c in C.COMMUNICATIONS)
    title = t(ui["output"], lang)
    body = """<section class="wrap page-head simple"><h1>{title}</h1></section>
<section class="wrap block stats">{s1}{s2}{s3}</section>
<section class="wrap block split" id="publications">
  <div class="split-title"><h2>{pubs_t}</h2><a class="underline-link small" href="https://scholar.google.com/citations?user=a-DuhUUAAAAJ">Google Scholar →</a></div>
  <ol class="pubs">{rows}</ol>
</section>
<section class="wrap block split" id="communications">
  <h2 class="split-title">{comms_t}</h2>
  <ol class="rows">{comms}</ol>
</section>""".format(
        title=e(title),
        s1=stat(str(len(C.PUBLICATIONS)), t(ui["n_pubs"], lang), True, "#publications"),
        s2=stat(str(len(C.COMMUNICATIONS)), t(ui["n_comms"], lang), False, "#communications"),
        s3=stat(N_THESES, t(ui["n_theses"], lang), False, "../teaching/"),
        pubs_t=e(t(ui["publications"], lang)), rows=rows, comms_t=e(t(ui["communications"], lang)), comms=comms)
    return page(lang, "publications", title, body)


def teaching(lang):
    T = C.TEACHING
    stats = "".join(stat(n, t(l, lang), i == 0) for i, (n, l) in enumerate(T["stats"]))
    uni = "".join('<li class="row3"><span class="y">%s</span><span class="v">%s</span><span class="ti">%s</span></li>'
                  % (e(y), e(w), e(t(x, lang))) for y, w, x in T["uni"])
    courses = "".join('<li class="row3"><span class="y">%s</span><span class="v">%s</span><span class="ti">%s</span></li>'
                      % (e(y), e(w), e(t(x, lang))) for y, w, x in T["courses"])
    title = t(T["title"], lang)
    body = """<section class="wrap page-head simple"><h1>{title}</h1><p class="lead">{desc}</p></section>
<section class="wrap block stats stats-2">{stats}</section>
<section class="wrap block split"><h2 class="split-title">{uni_t}</h2><ol class="rows">{uni}</ol></section>
<section class="wrap block split"><h2 class="split-title">{courses_t}</h2><ol class="rows">{courses}</ol></section>
""".format(title=e(title), desc=e(t(T["desc"], lang)), stats=stats, uni_t=e(t(T["uni_title"], lang)), uni=uni,
           courses_t=e(t(T["courses_title"], lang)), courses=courses)
    return page(lang, "teaching", title, body, t(T["desc"], lang))


# ------------------------------------------------------------------ root files
ROOT_INDEX = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name}</title>
<link rel="canonical" href="{site}/en/">
<script>(function(){{var l=(navigator.languages&&navigator.languages[0]||navigator.language||"en").toLowerCase();
var t=l.indexOf("ca")===0?"ca":(l.indexOf("es")===0?"es":"en");location.replace(t+"/");}})();</script>
<style>body{{margin:0;padding:40px 20px;font:16px/1.5 Archivo,Helvetica,Arial,sans-serif;background:#0E0E0E;color:#F2F2EE}}a{{color:#D7FF3A}}</style>
</head>
<body>
<p><a href="en/">English</a> · <a href="es/">Español</a> · <a href="ca/">Català</a></p>
</body>
</html>
"""

NOT_FOUND = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 · {name}</title>
<style>body{{margin:0;padding:64px 20px;font:18px/1.5 Archivo,Helvetica,Arial,sans-serif;background:#0E0E0E;color:#F2F2EE}}
h1{{font-size:clamp(64px,14vw,160px);margin:0;line-height:.9;color:#D7FF3A}}a{{color:#F2F2EE}}</style>
</head>
<body>
<h1>404</h1>
<p>Page not found · Página no encontrada · Pàgina no trobada</p>
<p><a href="/en/">English</a> · <a href="/es/">Español</a> · <a href="/ca/">Català</a></p>
</body>
</html>
"""


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    builders = {"planning": planning, "devices": devices, "regulatory": regulatory, "ai": ai,
                "publications": publications, "teaching": teaching}
    urls = []
    for lang in C.LANGS:
        out = os.path.join(ROOT, lang)
        if os.path.isdir(out):
            shutil.rmtree(out)
        write("%s/index.html" % lang, home(lang))
        urls.append("%s/%s/" % (C.SITE_URL, lang))
        for slug, _l, _n in C.PAGES:
            write("%s/%s/index.html" % (lang, slug), builders[slug](lang))
            urls.append("%s/%s/%s/" % (C.SITE_URL, lang, slug))
    write("index.html", ROOT_INDEX.format(name=e(C.PERSON["name"]), site=C.SITE_URL))
    write("404.html", NOT_FOUND.format(name=e(C.PERSON["name"])))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join("  <url><loc>%s</loc></url>\n" % u for u in urls) + "</urlset>\n")
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % C.SITE_URL)
    print("Built %d pages." % len(urls))


if __name__ == "__main__":
    main()
