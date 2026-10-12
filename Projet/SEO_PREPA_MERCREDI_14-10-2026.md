# SEO & GEO : dossier de travail du mercredi 14/10/2026

> Suite du plan SEO accéléré. Phases 1 (technique) et 2 (7 pages par intention) en ligne depuis le 12/10. Search Console : sitemap renvoyé et indexation demandée.
> Ce dossier prépare la Phase 3 (blog) et la Phase 4 (autorité externe). Suivi des mots-clés : [SEO_MOTS_CLES.md](SEO_MOTS_CLES.md).

## 1. À vérifier en premier (bloquants)

| # | Point | Pourquoi | Action |
|---|---|---|---|
| 1 | **Référencement Constructys** | La documentation Constructys conditionne le financement à un organisme **référencé** (historiquement : dossier Datadock avec l'attribut « référençable » et au moins 1 action financée sur les 2 dernières années). Qualiopi seul ne suffit peut-être pas. Si Cresceo n'est pas référencé, nos pages qui promettent un financement Constructys sont fragiles. | Appeler ou écrire à la direction régionale Constructys Île-de-France (contact Éloïse depuis BIM World) : « Cresceo est-il référencé ? sinon, quelle procédure en 2026 ? ». Si besoin, ouvrir le dossier Datadock. |
| 2 | **Délai de dépôt OPCO** | Un guide public indique un dépôt sur eGestion **au moins 15 jours avant** la formation, puis 15 jours ouvrés d'instruction. | Confirmer avec Constructys, puis je mets à jour la page financement (aujourd'hui : « avant le début, le plus tôt possible »). |
| 3 | **Fiche organisme MAF** | La liste publique des organismes de formation (data.gouv) est alimentée depuis Mon Activité Formation. Le code d'activation reçu avec le NDA expirait le 30/09/2026. | Vérifier que l'accès MAF est activé et que la fiche (nom, site web, spécialités) est complète. |
| 4 | **Relectures métier** | Pages publiées le 12/10 sur la base des programmes et du Code du travail. | Igor : [DUERP BTP](https://cresceo.fr/formation-duerp-btp.html) et [accueil sécurité](https://cresceo.fr/accueil-securite-chantier.html). Julien : [Lean Construction](https://cresceo.fr/formation-lean-construction-ia.html) (il y est cité comme formateur référent). |

## 2. Blog (Phase 3)

### Choix techniques (proposés, à valider)

- **Même approche que les pages par intention** : un script Python génère `/blog/` (index + 1 page par article) depuis des fichiers Markdown dans le repo, avec le gabarit du site, le schema `Article` (auteur nommé), le sitemap et le `llms.txt` mis à jour automatiquement. Pas de CMS.
- **Emplacement des sources** : `COM/blog/AAAA-MM-JJ-slug.md` (front matter : titre, description, auteur, requête cible, page à mailler, sources).
- **Format de chaque article** (citable par les moteurs IA) : réponse en 2-3 phrases en tête, H2 formulés comme des questions, 1 tableau ou liste chiffrée, sources primaires citées (OPPBTP, INRS, Légifrance, France Compétences...), encadré « Ce que propose Cresceo » avec lien vers la page formation, date de mise à jour. 800 à 1 500 mots.
- **Signature** : Igor pour la prévention, Julien pour le Lean et la productivité, Cresceo pour le financement. À valider avec eux (le signataire relit).

### Les 10 articles de lancement (ordre de publication proposé)

Matière déjà sourcée dans les posts LinkedIn hebdo (`COM/drafts/weekly/`). Chaque article = le post développé, pas recopié.

| # | Titre proposé | Requête visée | Source interne | Sources primaires | Page à mailler | Signataire |
|---|---|---|---|---|---|---|
| 1 | Budget formation : comment ne pas perdre votre enveloppe OPCO avant la fin d'année | budget formation OPCO fin d'année BTP | W42 | France Compétences (enveloppe PDC 2026), Constructys | Financement Constructys | Cresceo |
| 2 | IA sur chantier : ce qu'elle détecte vraiment, et ce qu'elle ne remplace pas | IA chantier sécurité | Msg clés Regard Sécurité, programme | Programme Regard Sécurité, cadre RGPD | Formation IA BTP | Igor |
| 3 | Chutes de hauteur dans le BTP : chiffres clés et leviers de prévention | chutes de hauteur BTP | W30 | OPPBTP (campagne nationale) | Prévention risques chantier | Igor |
| 4 | Accueil des nouveaux arrivants dans le BTP : les 6 étapes d'un accueil sécurité réussi | accueil sécurité nouveaux arrivants BTP | W29 | OPPBTP (6 étapes, vidéo juridique) | Accueil sécurité chantier | Igor |
| 5 | Coactivité sur chantier : prévenir les risques d'interférence | coactivité chantier risques | W37 | OPPBTP, INRS (coordination SPS) | Prévention risques chantier | Igor |
| 6 | Lean Construction : pourquoi performance et prévention vont ensemble | lean construction prévention | W28 v2 | OPPBTP, FFB, USH | Lean Construction | Julien |
| 7 | Travaux de reprise : 5 à 10 % du chiffre d'affaires du bâtiment | coût des reprises bâtiment | W31 | Le Moniteur (étude PlanRadar) | Lean Construction | Julien |
| 8 | Retards de chantier : pourquoi la productivité du BTP stagne | retard chantier productivité BTP | W34 | McKinsey | Lean Construction | Julien |
| 9 | TMS dans le BTP : repérer les postures à risque avant l'arrêt de travail | TMS BTP prévention | W33 | OPPBTP (boîte à outils TMS, campagne) | Prévention risques chantier | Igor |
| 10 | Chutes de plain-pied : le 2e risque d'accident du BTP | chutes de plain-pied chantier | W41 | OPPBTP | Prévention risques chantier | Igor |

**En réserve** : reprise de chantier après un arrêt (W35), recruter ou former face à la pénurie de compétences (W35 v2, France Travail BMO 2026), digitalisation du BTP en 2026 (W38, Batipôle), canicule sur chantier (W28, instruction DGT du 22/05/2026, à publier au printemps 2027).

**Cadence ensuite** : 1 à 2 articles par semaine, en recyclant le post LinkedIn de la semaine (le post renvoie vers l'article, l'article reprend et approfondit le post).

## 3. Autorité externe (Phase 4) : textes prêts à l'emploi

### Fiche Google Business Profile

- **Point d'attention** : l'adresse du siège (58 rue de Monceau) est une domiciliation. Google refuse souvent ce type d'adresse. Configurer la fiche en **établissement de services sans accueil du public** : zone desservie = France (ou régions principales), adresse masquée. La validation se fait par courrier, vidéo ou téléphone selon ce que Google propose.
- **Catégorie principale** : Centre de formation. **Secondaires** : Consultant en sécurité, Service de formation professionnelle (selon disponibilité).
- **Site web** : `https://cresceo.fr/formation-ia-btp.html` (la page principale, plutôt que la home).
- **Description** (642 caractères, sous la limite de 750) :

> Cresceo est un organisme de formation certifié Qualiopi (certificat n° 875611-1) spécialisé dans les formations IA pour le BTP et l'Industrie. Nos formations apprennent à l'encadrement de chantier à détecter les risques grâce à l'analyse vidéo par intelligence artificielle, à piloter la prévention par la donnée et à améliorer la productivité avec le Lean Construction. Formats hybrides : classes virtuelles et mise en pratique sur vos chantiers, partout en France. À partir de 400 € par participant, finançables par votre OPCO. Nous proposons aussi l'accueil sécurité externalisé et des déploiements sur mesure pour les grandes entreprises.

- **Services** (avec prix quand public) : Regard Sécurité (400 €), Piloter la Prévention avec l'IA (à partir de 400 € HT), Piloter la Productivité avec l'IA (à partir de 400 € HT), Accueil sécurité externalisé (à partir de 75 € HT), Formation intra-entreprise (sur devis).
- **Photos** : logo, Igor et Julien, captures IA (`assets/ia/`, `assets/ia-prod/`), visuel BATIMAT.
- **Avis** : dès la fiche validée, envoyer le lien d'avis aux participants des 8 premières sessions (c'est le signal local le plus fort).

### Page LinkedIn Cresceo (section « À propos »)

> Cresceo, organisme de formation certifié Qualiopi, forme l'encadrement de chantier du BTP et de l'Industrie à utiliser l'intelligence artificielle pour la prévention et la productivité. Détection des risques chantier par analyse vidéo IA, pilotage de la sécurité par la donnée, Lean Construction : des formations ancrées sur vos propres chantiers, animées par des experts du terrain, finançables par votre OPCO. Finaliste des Trophées de l'Innovation du WinLab' CCCA-BTP (BATIMAT 2026). La croissance par le savoir.

Site web de la page : `https://cresceo.fr/formation-ia-btp.html`. Spécialités : Formation IA BTP, Prévention des risques, Sécurité chantier, Lean Construction, DUERP, Qualiopi.

### Liens entrants à obtenir (par ordre de rapport effort/impact)

| Source | État supposé | Demande |
|---|---|---|
| CAD.42 (site partenaire) | À vérifier | Lien vers cresceo.fr depuis une page partenaires ou formation (positionnement : partenaire technologique). Via JP. |
| CCCA-BTP / WinLab' | Page finalistes à vérifier | Vérifier que la fiche finaliste renvoie vers cresceo.fr, sinon demander l'ajout. |
| Batinfo (communiqué) | Publié | Vérifier la présence d'un lien vers cresceo.fr, sinon demander l'ajout. |
| Carif-Oref Île-de-France (Défi métiers) | Non fait | Déclarer l'offre de formation (gratuit, alimente aussi d'autres portails). |
| Constructys | Voir bloquant n° 1 | Une fois référencé, vérifier la présence dans la liste des organismes. |
| Profils LinkedIn des associés | Partiel | Lien cresceo.fr en section « Coordonnées » et en « Sélection ». |

Modèle de demande (ton à ajuster selon le contact) :

> Bonjour [Prénom],
> Merci encore pour [la mise en avant / le partenariat / l'article]. Une petite demande : serait-il possible d'ajouter un lien vers notre site (https://cresceo.fr/formation-ia-btp.html) sur [la page concernée] ? Cela aide les entreprises qui découvrent Cresceo par votre biais à retrouver nos formations.
> Bonne journée,
> Baptiste

## 4. Proposition de déroulé pour mercredi

| Créneau | Tâche | Qui |
|---|---|---|
| 30 min | Bloquants 1 à 3 (Constructys, délai OPCO, MAF) | Baptiste (+ Éloïse pour Constructys) |
| 30 min | Fiche Google Business Profile + « À propos » LinkedIn | Baptiste |
| 15 min | Envoi des demandes de liens (CAD.42, CCCA-BTP, Batinfo) | Baptiste |
| 1 h | Générateur de blog + articles 1 et 2 rédigés, puis publiés après ta relecture | Claude, puis Baptiste |
| 30 min | Lancement de la rédaction des articles 3 à 10 en brouillon, envoi aux signataires pour relecture | Claude, puis Igor et Julien |
| 15 min | Déclaration Carif-Oref (Défi métiers) | Baptiste |

## 5. Mesure

1er relevé complet prévu le **lundi 02/11/2026** (protocole dans [SEO_MOTS_CLES.md](SEO_MOTS_CLES.md)) : premières impressions sur les 7 nouvelles pages attendues d'ici là. Le classement sur « formation qualiopi IA BTP » dépend surtout des liens entrants et prendra 2 à 4 mois.
