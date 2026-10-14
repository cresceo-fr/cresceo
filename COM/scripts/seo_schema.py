"""Inject unified schema.org JSON-LD + home FAQ into cresceo.fr static pages.

Usage: python seo_schema.py <site_dir>
Idempotent: replaces the first ld+json block of each page and the FAQ section between markers.
"""
import html
import json
import re
import sys
from pathlib import Path

SITE = "https://cresceo.fr"
ORG_ID = f"{SITE}/#organization"
WEBSITE_ID = f"{SITE}/#website"
IGOR_ID = f"{SITE}/#igor-canonne"
JULIEN_ID = f"{SITE}/#julien-gardette"

ORG_REF = {"@type": "EducationalOrganization", "@id": ORG_ID, "name": "Cresceo", "url": f"{SITE}/"}

ORGANIZATION = {
    "@type": "EducationalOrganization",
    "@id": ORG_ID,
    "name": "Cresceo",
    "legalName": "Cresceo SAS",
    "url": f"{SITE}/",
    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo.png"},
    "image": f"{SITE}/assets/logo.png",
    "email": "contact@cresceo.fr",
    "slogan": "La croissance par le savoir",
    "description": (
        "Organisme de formation certifié Qualiopi spécialisé dans les formations IA pour le BTP "
        "et l'Industrie : détection des risques chantier, prévention HSE et Lean Construction."
    ),
    "foundingDate": "2026-04-07",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Les Tricolores, 58 rue de Monceau",
        "postalCode": "75008",
        "addressLocality": "Paris",
        "addressCountry": "FR",
    },
    "identifier": [
        {"@type": "PropertyValue", "propertyID": "SIREN", "value": "103298188"},
        {"@type": "PropertyValue", "propertyID": "Numéro de déclaration d'activité (NDA)", "value": "11757694675"},
    ],
    "areaServed": {"@type": "Country", "name": "France"},
    "knowsAbout": [
        "Formation IA BTP", "Intelligence artificielle appliquée au chantier", "Prévention des risques BTP",
        "HSE", "Sécurité chantier", "DUERP", "Lean Construction", "Productivité chantier",
    ],
    "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "certification",
        "name": "Certification Qualiopi, catégorie actions de formation",
        "identifier": "875611-1",
        "validFrom": "2026-09-07",
        "expires": "2029-09-06",
        "recognizedBy": {"@type": "Organization", "name": "Certifopac"},
    },
    "award": "Finaliste des Trophées de l'Innovation du WinLab' CCCA-BTP (BATIMAT 2026)",
    "member": [{"@id": IGOR_ID}, {"@id": JULIEN_ID}],
    "sameAs": ["https://www.linkedin.com/company/cresceo/"],
}

PERSONS = [
    {
        "@type": "Person",
        "@id": IGOR_ID,
        "name": "Igor Canonne",
        "jobTitle": "Président, expert HSE et Intelligence Artificielle",
        "description": "Plus de 15 ans d'expérience en prévention et sécurité dans le BTP, pionnier de l'IA appliquée à la détection des risques sur chantier.",
        "image": f"{SITE}/assets/igor.jpg",
        "worksFor": {"@id": ORG_ID},
        "sameAs": ["https://www.linkedin.com/in/igor-canonne"],
        "knowsAbout": ["Prévention des risques BTP", "HSE", "Intelligence artificielle"],
    },
    {
        "@type": "Person",
        "@id": JULIEN_ID,
        "name": "Julien Gardette",
        "jobTitle": "Expert Lean Construction et BTP",
        "description": "Spécialiste de l'optimisation de production et du Lean Management appliqué à la construction.",
        "image": f"{SITE}/assets/julien.jpg",
        "worksFor": {"@id": ORG_ID},
        "sameAs": ["https://www.linkedin.com/in/jgardette"],
        "knowsAbout": ["Lean Construction", "Productivité chantier", "Lean Management"],
    },
]

WEBSITE = {
    "@type": "WebSite",
    "@id": WEBSITE_ID,
    "url": f"{SITE}/",
    "name": "Cresceo",
    "inLanguage": "fr-FR",
    "publisher": {"@id": ORG_ID},
}


def weekly(hours):
    return {"@type": "Schedule", "duration": "PT1H", "repeatFrequency": "P1W", "repeatCount": hours}


def offer(desc):
    return {"@type": "Offer", "category": "Paid", "price": "400", "priceCurrency": "EUR", "description": desc}


COURSES = [
    {
        "@type": "Course",
        "@id": f"{SITE}/formations.html#regard-securite",
        "url": f"{SITE}/formations.html#regard-securite",
        "name": "Regard Sécurité",
        "alternateName": "Formation détection des risques chantier avec l'IA",
        "description": (
            "Formation de 7 heures pour identifier les situations à risque sur chantier (coactivité engins-piétons, "
            "chutes, TMS) grâce à l'analyse vidéo par IA, puis prioriser les actions de prévention."
        ),
        "provider": ORG_REF,
        "inLanguage": "fr",
        "educationalLevel": "Professionnel",
        "audience": {"@type": "Audience", "audienceType": "Conducteurs de travaux, chefs de chantier, préventeurs HSE"},
        "coursePrerequisites": "Aucun",
        "teaches": ["Détection des risques chantier", "Lecture de rapports d'analyse IA", "Priorisation des actions de prévention"],
        "timeRequired": "PT7H",
        "offers": offer("Par participant, financement OPCO possible"),
        "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Blended", "courseWorkload": "PT7H"},
    },
    {
        "@type": "Course",
        "@id": f"{SITE}/formations.html#prevention",
        "url": f"{SITE}/formations.html#prevention",
        "name": "Piloter la Prévention avec l'IA",
        "alternateName": "Formation prévention des risques BTP avec l'IA",
        "description": (
            "Parcours de 4 semaines (4 x 1 h) pour utiliser l'IA afin d'identifier les risques invisibles, "
            "piloter les indicateurs sécurité et animer la prévention sur chantier."
        ),
        "provider": ORG_REF,
        "inLanguage": "fr",
        "educationalLevel": "Professionnel",
        "audience": {"@type": "Audience", "audienceType": "Conducteurs de travaux, chefs de chantier, préventeurs, directeurs de travaux"},
        "coursePrerequisites": "Être responsable d'un chantier actif",
        "teaches": ["Pilotage des indicateurs sécurité", "Animation de quarts d'heure sécurité", "Prévention des risques BTP"],
        "timeRequired": "PT4H",
        "offers": offer("À partir de, HT par participant, financement OPCO possible"),
        "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Blended", "courseWorkload": "PT4H", "courseSchedule": weekly(4)},
    },
    {
        "@type": "Course",
        "@id": f"{SITE}/formations.html#lean",
        "url": f"{SITE}/formations.html#lean",
        "name": "Piloter la Productivité avec l'IA",
        "alternateName": "Formation Lean Construction avec l'IA",
        "description": (
            "Parcours Lean Construction de 4 semaines (4 x 1 h) : identifier les gaspillages et temps morts, "
            "piloter les indicateurs de production et animer la performance chantier grâce à l'IA."
        ),
        "provider": ORG_REF,
        "inLanguage": "fr",
        "educationalLevel": "Professionnel",
        "audience": {"@type": "Audience", "audienceType": "Conducteurs de travaux, directeurs de travaux, chefs de chantier, responsables méthodes"},
        "coursePrerequisites": "Être responsable d'un chantier actif",
        "teaches": ["Lean Construction", "Productivité chantier", "Tableaux de bord de production"],
        "timeRequired": "PT4H",
        "offers": offer("À partir de, HT par participant, financement OPCO possible"),
        "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Online", "courseWorkload": "PT4H", "courseSchedule": weekly(4)},
    },
]

FAQ = [
    ("Cresceo est-il un organisme de formation certifié Qualiopi ?",
     "Oui. Cresceo est certifié Qualiopi au titre des actions de formation (certificat n° 875611-1 délivré par Certifopac, "
     "valable du 07/09/2026 au 06/09/2029). L'organisme est enregistré sous le numéro de déclaration d'activité 11757694675."),
    ("Quelles formations IA proposez-vous pour le BTP ?",
     "3 formations : Regard Sécurité (7 h, détection des risques chantier par analyse vidéo IA), Piloter la Prévention avec l'IA "
     "(4 semaines, 4 x 1 h) et Piloter la Productivité avec l'IA, un parcours Lean Construction (4 semaines, 4 x 1 h). "
     "Un accompagnement personnalisé est aussi proposé après la formation."),
    ("Combien coûte une formation et peut-elle être financée ?",
     "Les formations démarrent à 400 € par participant. Elles sont éligibles à une prise en charge par votre OPCO "
     "(Constructys pour le BTP) ou par le FAF pour les indépendants, dans la limite de leurs plafonds horaires. Demandez-nous une estimation de votre reste à charge."),
    ("À qui s'adressent les formations ?",
     "À l'encadrement de chantier du BTP et de l'Industrie : conducteurs et directeurs de travaux, chefs de chantier, "
     "préventeurs HSE, responsables méthodes. Regard Sécurité ne demande aucun prérequis."),
    ("Comment se déroule une formation ?",
     "En format hybride : classes virtuelles et mission sur vos propres chantiers. Un smartphone suffit pour filmer une visite, "
     "la vidéo est analysée par l'IA puis débriefée avec un formateur expert."),
    ("L'utilisation de l'IA sur chantier respecte-t-elle le RGPD ?",
     "Oui. Le cadre RGPD et le floutage des images sont traités dès la première séquence de formation, "
     "et les vidéos sont déposées sur une plateforme sécurisée."),
    ("Quel est le délai d'accès ?",
     "Inscription 10 jours avant la session pour Regard Sécurité, 2 à 4 semaines pour les parcours Piloter la Prévention "
     "et Piloter la Productivité."),
]

FAQPAGE = {
    "@type": "FAQPage",
    "@id": f"{SITE}/#faq",
    "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ
    ],
}


def breadcrumb(name, path):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": f"{SITE}/{path}"},
        ],
    }


PAGES = {
    "index.html": [ORGANIZATION, WEBSITE, *PERSONS, *COURSES, FAQPAGE],
    "formations.html": [*COURSES, breadcrumb("Formations", "formations.html")],
    "qualite.html": [breadcrumb("Qualité et certification Qualiopi", "qualite.html")],
}

LD_RE = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)

FAQ_START, FAQ_END = "<!-- ==================== FAQ ==================== -->", "<!-- /FAQ -->"
FAQ_ANCHOR = "  <!-- ==================== CTA FINAL / DEVIS ==================== -->"


def ld_block(graph):
    body = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return "\n" + "\n".join("  " + l for l in body.split("\n")) + "\n  "


def faq_html():
    items = "\n".join(
        f"        <details class=\"faq-item\">\n"
        f"          <summary>{html.escape(q, quote=False)}</summary>\n"
        f"          <p>{html.escape(a, quote=False)}</p>\n"
        f"        </details>"
        for q, a in FAQ
    )
    return (
        f"  {FAQ_START}\n"
        f"  <section class=\"section\" id=\"faq\">\n"
        f"    <div class=\"section-inner\">\n"
        f"      <div class=\"section-header\">\n"
        f"        <span class=\"section-tag\">Questions fréquentes</span>\n"
        f"        <h2 class=\"section-title\">Formation IA BTP certifiée Qualiopi : vos questions</h2>\n"
        f"      </div>\n"
        f"      <div class=\"faq-list\">\n{items}\n      </div>\n"
        f"    </div>\n"
        f"  </section>\n"
        f"  {FAQ_END}\n\n"
    )


def main(site_dir):
    site = Path(site_dir)
    for name, graph in PAGES.items():
        p = site / name
        src = p.read_text(encoding="utf-8")
        block = ld_block(graph)
        if LD_RE.search(src):
            src = LD_RE.sub(lambda m: m.group(1) + block + m.group(3), src, count=1)
        else:
            src = src.replace("</head>", f'  <script type="application/ld+json">{block}</script>\n</head>', 1)
        if name == "index.html":
            src = re.sub(re.escape("  " + FAQ_START) + r".*?" + re.escape(FAQ_END) + r"\n\n", "", src, flags=re.S)
            assert FAQ_ANCHOR in src, "FAQ anchor not found"
            src = src.replace(FAQ_ANCHOR, faq_html() + FAQ_ANCHOR, 1)
        p.write_text(src, encoding="utf-8")
        print(f"{name}: {len(graph)} entities")


if __name__ == "__main__":
    main(sys.argv[1])
