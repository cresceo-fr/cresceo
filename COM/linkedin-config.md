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

## dossier_sortie
`C:\Users\bapti\OneDrive\Documents\SLASH\Cresceo\COM\drafts\veille`

## cadence
2 posts/semaine cible (palier Standard "Machine à Contenus"). Veille quotidienne possible, mais sélectionner ce qui mérite vraiment un reshare. Qualité > quantité, anti-spam.

## tutoiement
`true` : ton partenaire, on s'adresse aux gens du métier de pair à pair.

## Ton (6 repères)
1. **Factuel, jamais anxiogène** : la sécurité se prépare, ce n'est pas une fatalité. Pas d'alarmisme, pas de "🚨".
2. **Partenaire, pas vendeur** : on ouvre une conversation métier, on ne pitche pas la formation.
3. **Pédagogue** : analogies simples, chiffres concrets (les preuves chiffrées ci-dessus sont des actifs forts).
4. **Crédibilité terrain** : on parle le langage chantier, on cite des situations réelles.
5. **IA démystifiée** : l'IA est un outil au service du préventeur, pas un gadget. Concret, pas hype.
6. **Sobre** : tutoiement, emojis 0-2 max, CTA doux ("Comment tu fais aujourd'hui ?", "Parlons-en ?").

## Règles typo (rappel global)
- Pas de tirets cadratins (—) ni demi-cadratins (–). Utiliser virgules, parenthèses, deux-points, phrases séparées.
- Accents français corrects.
- Hashtag `#Cresceo` toujours présent.

## canva
Production des visuels LinkedIn via le MCP `canva-cresceo` (pivot acté 01/07/2026, cf. [[stack-automation-principles]] mise à jour). Le workflow dédié complet est décrit dans `COM/usine-a-contenus-cresceo.md`.

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
- Validation expertise : Igor Cannone (HSE), Julien Gardette (Lean) avant publication des posts métier.
- Backup : Baptiste Casnedi.
- Le skill produit un **draft** (texte + visuel Canva en copie éditable) : aucune publication automatique.
