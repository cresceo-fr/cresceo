# Config LinkedIn Cresceo

> Fichier de configuration lu par le skill générique `/veille-linkedin cresceo` (et à terme `/linkedin-weekly cresceo`).
> Démocratise l'usine à contenus de Marketime Hub vers Cresceo. Voir `_PILOTAGE/roadmap-mutualisation-2026.md`.

## brand_voice_path
`C:\Users\bapti\OneDrive\Documents\SLASH\Cresceo\COM\Charte-Graphique_CRESCEO.pdf` (charte visuelle)
À défaut de brand voice markdown dédiée, se référer aux sections "ton" ci-dessous (source de vérité éditoriale) + `Cresceo/CLAUDE.md`.

## secteur
Organisme de formation IA & HSE pour le BTP. Cible LinkedIn : conducteurs de travaux, préventeurs / responsables HSE, dirigeants TPE-PME du BTP, chargés de formation, coordonnateurs SPS, acteurs de l'intérim BTP (PASI). Positionnement : prévention des risques chantier et performance terrain augmentées par l'IA.

### 2 piliers offre (= `offre`)
1. **Regard Sécurité augmenté par l'IA** : prévention HSE, détection des risques chantier en temps réel. Preuves chiffrées : capacité de détection ×3 en 3 visites, 1 risque identifié par minute par l'IA.
2. **Lean Construction** : amélioration continue, pilotage de la productivité terrain, "mesurer pour progresser".
Atouts transverses : experts métiers 15+ ans de chantier, déployable sur site, certifié Qualiopi, éligible OPCO / CPF.

## requetes
- FR : "sécurité chantier BTP accident travail prévention HSE [mois] [année]"
- FR thématique : "Lean construction productivité chantier OR IA prévention risques BTP [année]"
- EN : "construction safety AI site risk prevention OR lean construction [mois] [année]"
- Variantes selon actu : réglementation (Code du travail, INRS, OPPBTP, CARSAT), accidentologie BTP, intérim sécurité (PASI), financement formation (OPCO Constructys, France Travail).

## hashtag_signature
`#Cresceo` (systématique) + 2-4 parmi : `#FormationBTP` `#IAChantier` `#Prévention` `#HSE` `#LeanConstruction` `#SécuritéChantier` `#BTP`

## sources_privilegiees
OPPBTP (preventionbtp.fr), INRS, CARSAT / Assurance Maladie risques pro, Ministère du Travail, Le Moniteur, Batiactu, Construction Cayola, Chantiers de France, AFP/presse régionale (accidentologie), publications IA appliquée au BTP. Sources institutionnelles HSE à privilégier pour la crédibilité.

## sources_evitees
Blogs SEO low-content, sites de génération de leads formation sans valeur éditoriale, communiqués pure promo, X/Reddit en source primaire (acceptés seulement si confirmés par un média établi).

**Domaines bloqués (ne jamais mettre dans `allowed_domains`)** : aucun identifié à ce jour sur le périmètre BTP/HSE. Les 8 domaines de `sources_privilegiees` ont été testés accessibles le 2026-09-11. Rappel du piège : un seul domaine bloqué dans la liste fait échouer tout l'appel WebSearch (erreur 400, zéro résultat). Si ça arrive, retirer le domaine fautif et relancer, puis l'ajouter ici.

## dossier_sortie
`C:\Users\bapti\OneDrive\Documents\SLASH\Cresceo\COM\drafts\veille`

## cadence
**1 post original/semaine + 1-2 reshares** (décision COPIL 07/09/2026). On garde des créneaux libres pour diffuser des news ponctuelles (BATIMAT, distinctions, actus des associés). Rythme volontairement resserré tant que l'activité et l'audience ne justifient pas plus ; arbitrage fin 2026 selon business/followers. Qualité > quantité, anti-spam.
Le skill `/linkedin-weekly` peut produire 2 posts (1 prévention + 1 performance) d'avance : n'en programmer qu'un par semaine et décaler l'autre à la semaine suivante.

## tutoiement
`false` : **vouvoiement** sur la com large LinkedIn. Décision Igor + Julien (08/2026) : le persona cible (Direction, DRH, directeurs d'agences) attend le vouvoiement, même si le tutoiement est courant sur chantier. Garder le ton partenaire et le langage métier, mais vouvoyer. Exemple de CTA validé : « Sur vos chantiers, avez-vous déjà regardé ce que le Fipu pourrait financer ? ».

## Ton (6 repères)
1. **Factuel, jamais anxiogène** : la sécurité se prépare, ce n'est pas une fatalité. Pas d'alarmisme, pas de "🚨".
2. **Partenaire, pas vendeur** : on ouvre une conversation métier, on ne pitche pas la formation.
3. **Pédagogue** : analogies simples, chiffres concrets (les preuves chiffrées ci-dessus sont des actifs forts).
4. **Crédibilité terrain** : on parle le langage chantier, on cite des situations réelles.
5. **IA démystifiée** : l'IA est un outil au service du préventeur, pas un gadget. Concret, pas hype.
6. **Sobre** : vouvoiement (persona Direction/DRH/directeurs d'agences), emojis 0-2 max, CTA doux ("Comment gérez-vous cela aujourd'hui ?", "Parlons-en ?").

## Règles typo (rappel global)
- Pas de tirets cadratins (—) ni demi-cadratins (–). Utiliser virgules, parenthèses, deux-points, phrases séparées.
- Accents français corrects.
- Hashtag `#Cresceo` toujours présent.

## render_html
**Méthode visuelle par défaut (depuis 10/2026).** Cartes LinkedIn sur-mesure pilotées par la charte Cresceo (système « Ascension & précision » : bleu profond #112331, diagonales ascendantes vert/orange #079b85 / #f9a937, coins nets, Montserrat/Roboto, logo), rendues en PNG en local. Remplace les gabarits Canva génériques, jugés fades (décision Baptiste 10/2026). Doc complète : `COM/templates/linkedin/README.md`.

- **Template** : `COM/templates/linkedin/card.html` (1 fichier, 3 modèles).
- **Modèles** : `stat` (donut + grand chiffre, pour Performance/preuves), `tips` (3 réflexes numérotés, pour Prévention), `news` (annonce/actu, type BATIMAT/partenariat), `formation` (mise en avant d'une formation du catalogue : accroche + specs à puces + CTA).
- **Rendu** : `pwsh COM/templates/linkedin/render.ps1 -Out "<dossier weekly>/YYYY-Wxx-<slug>.png" -Params '<query string>'` (via Edge/Chrome headless, sortie 2160x2160). Le script URL-encode les valeurs. Polices Montserrat/Roboto **embarquées** (`fonts.css`, base64) : rendu 100% hors-ligne.
- **Paramètres** : communs `type`, `kicker`, `title` (`*mot*` = surligné), `hl` (vert|orange) ; stat `num`/`unit`/`ring`/`sub`/`source` ; tips `intro`/`t1`/`t2`/`t3` ; news `m1`/`m2`/`m3`/`sub` ; formation `sub`/`s1`/`s2`/`s3`/`cta`. Détails + exemples dans le README.
- **Vérifier** le PNG produit (lisibilité, débordement, accents) ; si un titre déborde, raccourcir ou retirer un `*`.

## canva (fallback)
> Déprécié au profit de `render_html` (gabarits génériques, rendu fade). Garder uniquement comme repli si le rendu HTML est indisponible. Production des visuels via le MCP `canva-cresceo`. Workflow historique dans `COM/usine-a-contenus-cresceo.md`.

### Contrainte plan (IMPORTANT)
Compte Canva Cresceo sur **plan gratuit** : les *brand kits* et la fonction *brand templates / autofill* sont **verrouillés** (payant). Donc **ne pas** utiliser `create-design-from-brand-template` / autofill : ça renvoie une erreur "requires a Canva paid plan".
Mécanisme viable sur plan gratuit : **`copy-design`** (dupliquer le template) → **`perform-editing-operations`** (remplacer les textes) → **`export-design`** (PNG). Toujours dupliquer d'abord, ne jamais éditer le template source.

### Dossier & templates
- Dossier de travail : `POST LINKEDIN` (`folder_id` = `FAHG2yKPRFs`). Ranger les copies produites ici (`move-item-to-folder`).
- Design couverture : `COUVERTURE` (`DAHG26uUVAQ`).

| Type de post | Quand l'utiliser | `design_id` template |
|---|---|---|
| POST - Chiffres & Stats | Post à preuve chiffrée (×3 détection en 3 visites, 1 risque/min, accidentologie, KPI) | `DAHG2yI8W-E` |
| POST - Conseil / Tips formation | Post pédagogique, astuce métier prévention / Lean | `DAHG22MggZc` |
| POST - Actualité BTP / Industrie | Reshare ou rebond sur une actu HSE / BTP | `DAHG2ja8j2E` |
| POST - Présentation de formation | Mise en avant d'une formation du catalogue | `DAHG2rA8pSI` |

### Export
- Format : PNG, qualité haute. Fichier nommé `YYYY-Wxx-<type>.png`.
- Livrer le visuel exporté à côté du draft texte, dans le dossier weekly (`.../COM/drafts/weekly/`).
- Toujours proposer le lien `edit_url` de la copie Canva pour retouche manuelle par Éloïse avant programmation.

## Gouvernance
- Owner com : Éloïse Bouveret (valide le ton, planifie dans Metricool).
- Validation expertise : Igor Canonne (HSE), Julien Gardette (Lean) avant publication des posts métier.
- Backup : Baptiste Casnedi.
- Le skill produit un **draft** (texte + visuel Canva en copie éditable) : aucune publication automatique.
