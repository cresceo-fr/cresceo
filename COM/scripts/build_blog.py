"""Generate the cresceo.fr blog (/blog/) from Markdown sources in COM/blog/.

Usage:
  python build_blog.py <site_dir>            # publish articles with status: published
  python build_blog.py <site_dir> --drafts   # also render drafts (local preview only, do not commit)

Source file format (COM/blog/AAAA-MM-JJ-slug.md):
  ---
  title: ...            # H1 + <title>
  seo_title: ...        # optional, <title> override
  description: ...      # meta description (150-160 chars)
  slug: ...             # URL: /blog/<slug>.html
  date: 2026-10-14      # publication date
  updated: 2026-10-14   # optional
  author: igor | julien | cresceo
  keyword: ...          # target query (documentation only)
  lead: ...             # 2-3 sentence answer shown first (GEO)
  cta: formation-ia-btp # slug of the intent page promoted in the "Ce que propose Cresceo" box
  cta_text: ...         # box text
  related: [slug, ...]  # intent pages (build_pages.py) linked at the bottom
  sources: [{title, url}, ...]
  status: draft | published
  ---
  Markdown body (H2 = questions)

Also refreshes the /blog/ entries of sitemap.xml and the "## Blog" section of llms.txt.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

import markdown
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_pages import BY_SLUG, GA4, ORG_ID, SITE, WEBSITE_ID, esc  # noqa: E402

BLOG_SRC = Path(__file__).resolve().parents[1] / "blog"
MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

AUTHORS = {
    "igor": {"name": "Igor Canonne", "role": "Président, expert HSE et Intelligence Artificielle", "ref": {"@type": "Person", "@id": f"{SITE}/#igor-canonne", "name": "Igor Canonne"}},
    "julien": {"name": "Julien Gardette", "role": "Expert Lean Construction et BTP", "ref": {"@type": "Person", "@id": f"{SITE}/#julien-gardette", "name": "Julien Gardette"}},
    "cresceo": {"name": "L'équipe Cresceo", "role": "Organisme de formation certifié Qualiopi", "ref": {"@type": "EducationalOrganization", "@id": ORG_ID, "name": "Cresceo"}},
}

URL_ATTR = re.compile(r'(href|src|srcset)="(?!https?:|/|#|mailto:|tel:|data:)([^"]+)"')


def fr_date(d):
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def absolutize(fragment):
    """Make site-relative URLs root-absolute so the chrome works from /blog/."""
    return URL_ATTR.sub(lambda m: f'{m.group(1)}="/{m.group(2)}"', fragment)


def load_posts(include_drafts):
    posts = []
    for f in sorted(BLOG_SRC.glob("*.md")):
        raw = f.read_text(encoding="utf-8")
        _, fm, body = raw.split("---", 2)
        meta = yaml.safe_load(fm)
        if meta.get("status") != "published" and not include_drafts:
            continue
        meta.setdefault("updated", meta["date"])
        for k in ("date", "updated"):
            if isinstance(meta[k], str):
                meta[k] = date.fromisoformat(meta[k])
        meta["body_html"] = md_to_html(body)
        meta["url"] = f"{SITE}/blog/{meta['slug']}.html"
        posts.append(meta)
    return sorted(posts, key=lambda p: p["date"], reverse=True)


def md_to_html(text):
    out = markdown.markdown(text, extensions=["tables", "sane_lists"])
    out = out.replace("<table>", '<div class="table-wrap"><table class="cr-programme-table">').replace("</table>", "</table></div>")
    return out


def head(title, description, url, og_type, ld):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">

  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/logo.png">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="Cresceo">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{SITE}/assets/logo.png">

  <link rel="icon" type="image/png" href="/assets/icon.png">
  <link rel="alternate" type="application/rss+xml" title="Blog Cresceo" href="{SITE}/blog/feed.xml">

{GA4}

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/cresceo.css">
  <link rel="stylesheet" href="/assets/css/formations.css">
  <link rel="stylesheet" href="/assets/css/pages.css">

  <script type="application/ld+json">
{ld}
  </script>
</head>
<body>
"""


def ld_json(graph):
    body = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return "\n".join("  " + l for l in body.split("\n"))


def breadcrumb(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)],
    }


def render_post(p, nav_html, footer_html):
    a = AUTHORS[p["author"]]
    graph = [
        {
            "@type": "BlogPosting",
            "@id": f"{p['url']}#article",
            "url": p["url"],
            "mainEntityOfPage": p["url"],
            "headline": p["title"],
            "description": p["description"],
            "inLanguage": "fr-FR",
            "datePublished": p["date"].isoformat(),
            "dateModified": p["updated"].isoformat(),
            "author": a["ref"],
            "publisher": {"@id": ORG_ID},
            "isPartOf": {"@id": f"{SITE}/blog/#blog"},
            "image": f"{SITE}/assets/logo.png",
            "keywords": p.get("keyword", ""),
            "citation": [s["url"] for s in p.get("sources", [])],
        },
        breadcrumb([("Accueil", f"{SITE}/"), ("Blog", f"{SITE}/blog/"), (p["title"], p["url"])]),
    ]
    sources = "\n".join(
        f'        <li><a href="{esc(s["url"])}" rel="noopener" target="_blank">{esc(s["title"])}</a></li>' for s in p.get("sources", [])
    )
    cta_page = BY_SLUG[p["cta"]]
    related = "\n".join(
        f'      <a class="related-card" href="/{r}.html"><span>{esc(BY_SLUG[r]["nav"])}</span><small>{esc(BY_SLUG[r]["subtitle"])}</small></a>'
        for r in p.get("related", [])
    )
    updated = "" if p["updated"] == p["date"] else f" &middot; mis à jour le {fr_date(p['updated'])}"
    return head(p.get("seo_title", f"{p['title']} | Cresceo"), p["description"], p["url"], "article", ld_json(graph)) + f"""{nav_html}
  <header class="page-header">
    <div class="breadcrumb">
      <a href="/">Accueil</a> <span>/</span> <a href="/blog/">Blog</a> <span>/</span> <span style="color: rgba(255,255,255,0.7);">Article</span>
    </div>
    <h1>{esc(p['title'])}</h1>
    <p class="post-meta">Par <strong>{esc(a['name'])}</strong>, {esc(a['role'])} &middot; publié le {fr_date(p['date'])}{updated}</p>
  </header>

  <main class="page-content">
    <section class="answer-box" aria-label="En bref">
      <p class="answer-lead">{esc(p['lead'])}</p>
    </section>

    <article class="content-body">
{p['body_html']}

      <aside class="cresceo-box">
        <p class="cresceo-box__title">Ce que propose Cresceo</p>
        <p>{esc(p['cta_text'])}</p>
        <a href="/{p['cta']}.html" class="btn btn-primary">{esc(cta_page['nav'])}</a>
      </aside>

      <section class="post-sources">
        <h2>Sources</h2>
        <ul>
{sources}
        </ul>
      </section>
    </article>

    <nav class="related" aria-label="Pages liées">
      <h2>À lire aussi</h2>
      <div class="related-grid">
{related}
      </div>
    </nav>
  </main>

{footer_html}"""


def render_index(posts, nav_html, footer_html):
    url = f"{SITE}/blog/"
    graph = [
        {
            "@type": "Blog",
            "@id": f"{url}#blog",
            "url": url,
            "name": "Blog Cresceo : prévention, productivité et IA sur chantier",
            "inLanguage": "fr-FR",
            "publisher": {"@id": ORG_ID},
            "isPartOf": {"@id": WEBSITE_ID},
            "blogPost": [{"@id": f"{p['url']}#article"} for p in posts],
        },
        breadcrumb([("Accueil", f"{SITE}/"), ("Blog", url)]),
    ]
    cards = "\n".join(
        f"""      <a class="post-card" href="/blog/{p['slug']}.html">
        <span class="post-card__meta">{fr_date(p['date'])} &middot; {esc(AUTHORS[p['author']]['name'])}</span>
        <span class="post-card__title">{esc(p['title'])}</span>
        <span class="post-card__desc">{esc(p['description'])}</span>
      </a>"""
        for p in posts
    ) or '      <p class="post-empty">Premiers articles en cours de publication.</p>'
    title = "Blog : prévention des risques, Lean et IA sur chantier | Cresceo"
    desc = "Articles pratiques pour l'encadrement du BTP : prévention des risques chantier, Lean Construction, IA appliquée au terrain et financement de la formation."
    return head(title, desc, url, "website", ld_json(graph)) + f"""{nav_html}
  <header class="page-header">
    <div class="breadcrumb">
      <a href="/">Accueil</a> <span>/</span> <span style="color: rgba(255,255,255,0.7);">Blog</span>
    </div>
    <h1>Le blog Cresceo</h1>
    <p>Prévention des risques, productivité et IA sur chantier : des repères concrets pour l'encadrement du BTP.</p>
  </header>

  <main class="page-content">
    <div class="post-list">
{cards}
    </div>
  </main>

{footer_html}"""


def render_feed(posts):
    items = "\n".join(
        f"""    <item>
      <title>{esc(p['title'])}</title>
      <link>{p['url']}</link>
      <guid>{p['url']}</guid>
      <pubDate>{p['date'].strftime('%a, %d %b %Y')} 08:00:00 +0200</pubDate>
      <description>{esc(p['description'])}</description>
    </item>"""
        for p in posts
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Blog Cresceo</title>
    <link>{SITE}/blog/</link>
    <description>Prévention des risques, Lean Construction et IA sur chantier.</description>
    <language>fr-FR</language>
{items}
  </channel>
</rss>
"""


def update_sitemap(site, posts):
    p = site / "sitemap.xml"
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"  <url>\n    <loc>https://cresceo\.fr/blog/[^<]*</loc>.*?</url>\n", "", s, flags=re.S)
    newest = max((x["updated"] for x in posts), default=date.today())
    entries = [f"  <url>\n    <loc>{SITE}/blog/</loc>\n    <lastmod>{newest.isoformat()}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"]
    entries += [
        f"  <url>\n    <loc>{x['url']}</loc>\n    <lastmod>{x['updated'].isoformat()}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n"
        for x in posts
    ]
    p.write_text(s.replace("</urlset>", "".join(entries) + "</urlset>"), encoding="utf-8")


def update_llms(site, posts):
    p = site / "llms.txt"
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"## Blog\n.*?(?=\n## )", "", s, flags=re.S)
    lines = "\n".join(f"- [{x['title']}]({x['url']}): {x['description']}" for x in posts)
    block = f"## Blog\n\n- [Tous les articles]({SITE}/blog/)\n{lines}\n\n" if posts else ""
    s = s.replace("## Équipe", block + "## Équipe", 1)
    p.write_text(re.sub(r"\n{3,}", "\n\n", s), encoding="utf-8")


def main(site_dir, include_drafts=False):
    site = Path(site_dir)
    tpl = (site / "formations.html").read_text(encoding="utf-8")
    nav_html = absolutize(tpl[tpl.index("  <!-- NAV -->"):tpl.index("  <!-- PAGE HEADER -->")])
    footer_html = absolutize(tpl[tpl.index("  <!-- FOOTER -->"):])
    posts = load_posts(include_drafts)
    out = site / "blog"
    out.mkdir(exist_ok=True)
    for p in posts:
        (out / f"{p['slug']}.html").write_text(render_post(p, nav_html, footer_html), encoding="utf-8")
        print("wrote blog/" + p["slug"] + ".html", "(draft)" if p.get("status") != "published" else "")
    (out / "index.html").write_text(render_index(posts, nav_html, footer_html), encoding="utf-8")
    (out / "feed.xml").write_text(render_feed(posts), encoding="utf-8")
    if not include_drafts:
        update_sitemap(site, posts)
        update_llms(site, posts)
    print(f"{len(posts)} article(s), index + feed written")


if __name__ == "__main__":
    main(sys.argv[1], "--drafts" in sys.argv[2:])
