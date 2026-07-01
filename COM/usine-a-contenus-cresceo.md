# Usine à contenus Cresceo, workflow hebdomadaire

> Workflow dédié LinkedIn de Cresceo, dérivé de l'usine à contenus Marketime Hub.
> Déclencheur : event Google Calendar récurrent **"Routine Usine à Contenus Cresceo, semaine complète"**, chaque **lundi 9h**.
> Config pilote : `COM/linkedin-config.md`. Moteur texte : skill `/linkedin-weekly cresceo`. Voir `_PILOTAGE/roadmap-mutualisation-2026.md`.

## Objectif
Produire chaque semaine, en un seul run, le contenu LinkedIn Cresceo prêt à valider :
1 post original (2 variantes texte) + son visuel Canva, plus 3-4 reshares à programmer.
Cadence cible : 2 posts/semaine (1 post original Cresceo + reshares). Les posts d'Igor et Julien (2/mois chacun) restent hors de ce run automatique.

## Rôles
- **Baptiste** (CTO) : lance le run, produit le draft texte + visuels, livre à Éloïse.
- **Éloïse** (Com) : valide le ton, retouche le visuel Canva si besoin, programme dans Metricool.
- **Igor / Julien** : valident l'expertise (HSE / Lean) avant publication des posts métier.
- Le workflow produit un **draft** : aucune publication automatique.

## Déclenchement
- **Automatique** : event calendar lundi 9h (rappel humain, pas d'exécution headless).
- **À la demande** : `/linkedin-weekly cresceo` à tout moment.

## Pipeline

### 1. Texte, via `/linkedin-weekly cresceo`
Le skill générique lit `linkedin-config.md`, recherche l'actu HSE/BTP de la semaine, et produit le draft dans `COM/drafts/weekly/YYYY-Wxx-linkedin.md` :
- Contexte semaine (angle actu + lien offre)
- Post original : variante A (court) + variante B (storytelling) + brief visuel
- 3-4 reshares (source, angle, hashtags, priorité, jour suggéré)

### 2. Visuel, via MCP `canva-cresceo`
Pour le post original retenu (souvent la variante recommandée) :
1. **Choisir le template** selon le type de post (cf. tableau `canva` de `linkedin-config.md`) :
   - Preuve chiffrée → `POST - Chiffres & Stats` (`DAHG2yI8W-E`)
   - Astuce / pédagogie → `POST - Conseil / Tips formation` (`DAHG22MggZc`)
   - Rebond actu → `POST - Actualité BTP / Industrie` (`DAHG2ja8j2E`)
   - Formation du catalogue → `POST - Présentation de formation` (`DAHG2rA8pSI`)
2. **Dupliquer** le template (`copy-design`), jamais éditer la source.
3. **Éditer les textes** de la copie (`perform-editing-operations`) : titre / accroche + éventuel chiffre clé, cohérents avec le post.
4. **Exporter** en PNG (`export-design`) vers `COM/drafts/weekly/YYYY-Wxx-<type>.png`.
5. **Ranger** la copie dans le dossier `POST LINKEDIN` (`FAHG2yKPRFs`) et noter son `edit_url` dans le draft pour retouche Éloïse.

> Rappel plan gratuit : pas de brand template / autofill (verrouillé, payant). Uniquement copie → édition → export.

### 3. Handoff Éloïse
Le run se termine par un récap conversationnel (8-12 lignes) : chemin du draft, variante recommandée, top reshare + jour, lien `edit_url` du visuel, flags. Éloïse valide, retouche si besoin, programme.

## Garde-fous
- Jamais inventer une actu : sinon angle evergreen assumé.
- Jamais publier directement : draft uniquement (texte + visuel en copie éditable).
- Respecter le ton config (tutoiement, factuel non anxiogène, pas de cadratin —, accents corrects).
- Pas de mention Qualiopi tant que la certification n'est pas obtenue (décision 18/05).
- Pas d'écrasement : suffixer `-v2` si un draft de la semaine existe.

## Évolutions prévues
- Alimentation auto de la DB Notion "Idées & Brouillons" depuis le pipeline signaux-faibles (cf. [[stack-automation-principles]]).
- Calendrier éditorial Cresceo dédié (aujourd'hui absent, l'angle est piloté par l'actu). À créer sur le modèle HTML MH si le besoin se confirme.
- Reconsidérer un plan Canva payant seulement si le besoin de templates répétables / carrousels / livre blanc se confirme (blog prévu août-sept).
