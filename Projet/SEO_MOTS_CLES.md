# SEO : mots-clés de référence et suivi

> Version 1 du 12/10/2026. Source unique de vérité pour le ciblage SEO/GEO de cresceo.fr. Les 15 mots-clés d'origine (mars 2026) n'étaient conservés nulle part, seuls 3 sont retrouvés : ils sont repris ci-dessous.
> Plan d'action associé : refonte SEO & GEO, octobre 2026.

## Mots-clés cibles

| # | Requête | Intention | Page cible (actuelle → Phase 2) | Priorité |
|---|---|---|---|---|
| 1 | formation IA BTP | achat | `/formation-ia-btp.html` | P1 |
| 2 | formation qualiopi IA BTP | achat | `/formation-ia-btp.html` | P1 |
| 3 | formation intelligence artificielle BTP | achat | `/formation-ia-btp.html` | P1 |
| 4 | formation détection risques chantier | achat | formations.html#regard-securite → `/formation-prevention-risques-chantier-ia` | P1 |
| 5 | formation prévention risques BTP | achat | formations.html#prevention → `/formation-prevention-risques-chantier-ia` | P1 |
| 6 | formation sécurité chantier | achat | formations.html → `/formation-prevention-risques-chantier-ia` | P2 |
| 7 | formation lean construction | achat | formations.html#lean → `/formation-lean-construction-ia` | P1 |
| 8 | formation lean management BTP | achat | formations.html#lean → `/formation-lean-construction-ia` | P2 |
| 9 | formation DUERP BTP | achat / info | home → `/formation-duerp-btp` | P2 |
| 10 | accueil sécurité chantier externalisé | achat | home → `/accueil-securite-chantier` | P2 |
| 11 | financement formation BTP Constructys | info / achat | formations.html → `/financement-formation-btp-constructys` | P1 |
| 12 | formation conducteur de travaux IA | achat | à créer (page persona) | P3 |
| 13 | IA chantier sécurité | info | blog (cluster IA x BTP) | P2 |
| 14 | productivité chantier IA | info | blog (cluster Lean) | P3 |
| 15 | organisme formation HSE BTP Qualiopi | achat | home / qualite.html | P2 |

## Protocole de mesure (mensuel, 1er lundi du mois)

1. **Search Console** : impressions, clics, position moyenne par requête et par page (export Performances, 28 derniers jours).
2. **Test manuel** des 15 requêtes, navigation privée, géolocalisation France : position Google classique (top 30 sinon "non classé").
3. **GEO** : mêmes requêtes en mode IA Google, Perplexity et ChatGPT. Noter si Cresceo est cité (oui / non / source citée). Captures datées dans `COM/seo/AAAA-MM/`.
4. Reporter dans le tableau ci-dessous.

## Suivi

| Date | Requêtes top 10 | Requêtes top 30 | Citations IA | Domaines référents | Commentaire |
|---|---|---|---|---|---|
| 12/10/2026 | 0 | à mesurer | 0 | à mesurer (GSC > Liens) | Baseline. Non visible sur "formation qualiopi IA BTP" (Google classique et mode IA). |

## Journal des actions

- **12/10/2026, Phase 1** : schema.org unifié (Organization, Person, Course, FAQPage, BreadcrumbList), FAQ visible sur la home, titres et H2 orientés intentions, correction "Igor Canonne" sur la home, `llms.txt`, robots.txt ouvert aux bots IA, sitemap à jour, og:image, CSS de la home externalisé. Générateur du JSON-LD : `COM/scripts/seo_schema.py`.
- **12/10/2026, Phase 2** : 7 pages par intention en ligne (formation-ia-btp, prévention risques chantier, Lean Construction, DUERP BTP en guide, accueil sécurité, financement Constructys, grandes entreprises sur devis). Maillage depuis home, formations.html et pied de page. Générateur : `COM/scripts/build_pages.py` (modifier le contenu dans le script puis relancer `python COM/scripts/build_pages.py site`).
