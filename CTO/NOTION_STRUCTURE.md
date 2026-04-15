# Structure Notion - Cresceo

**Objectif** : Workspace collaboratif complet — pilotage projet, machine à contenus, CRM, pédagogie.
**Statut** : Vague 1 déployée (29/03, Éloïse) ; Vague 2 en cours (avril — bases opérationnelles + DAF)
**Dernière revue** : 15/04/2026 — ajout section DAF, bases Devis + Factures émises + Dépenses + Plan Qualiopi

---

## Architecture Workspace

```
Cresceo (Workspace)
│
├── 🏠 Dashboard
│   └── Vue d'ensemble (liens rapides, KPIs, prochaines étapes, calendrier)
│
├── 📐 Stratégie
│   ├── Contexte Projet
│   ├── Business Plan
│   ├── Analyse Marché
│   └── Juridique (pacte, statuts — liens vers docs avocat)
│
├── ⚙️ Opérationnel
│   ├── Plan de Lancement
│   ├── Actions / TODO (database)
│   ├── Réunions & CRs (database)
│   └── Automations (database) ← ajout Éloïse
│
├── 💼 Commercial
│   ├── Pipe Commercial (database)
│   ├── Contacts (database)
│   ├── Propositions commerciales
│   └── Offres commerciales (database) ← ajout Éloïse
│
├── 🎓 Pédagogie
│   ├── Catalogue Formations (database)
│   ├── Modules & Contenus (database)
│   ├── Supports de formation (PPT, PDF, parcours)
│   └── Qualiopi (process, indicateurs, audit)
│
├── 📢 Machine à Contenus
│   ├── Calendrier Éditorial (database — vue calendrier)
│   ├── Idées & Brouillons (database — kanban)
│   ├── Assets Visuels (database)
│   ├── Messages Clés & Angles (page)
│   ├── Guidelines Com (page)
│   ├── Funnel Marketing (database) ← ajout Éloïse
│   └── Sources d'acquisition (database) ← ajout Éloïse
│
├── 🎨 Marque & Design
│   ├── Charte Graphique (embed PDF ou page)
│   ├── Logos & Déclinaisons
│   ├── Templates (signatures, PPT, posts RS)
│   └── Univers graphiques (Vert HSE / Orange Lean)
│
├── 🗄️ Admin
│   ├── Ressources (liens Drive, docs externes)
│   ├── Archive Docsify
│   └── Paramètres & Permissions
│
└── ⚙️ Opérationnel / 💰 DAF / Finances  ← ajouté 15/04 (à remonter top-level par drag)
    ├── 📤 Factures émises (database — liée à Devis + Contacts)
    ├── 📥 Dépenses (database — factures fournisseurs + notes de frais)
    └── Suivi budget & tréso (à créer)
```

### Bases créées le 15/04/2026
| Base | Emplacement | ID | Rôle |
|------|-------------|----|------|
| Devis | 💼 Commercial | `343d62ae-ccba-819a-9ff2-c7761789e747` | Documents commerciaux individuels, liés à Offres, Formation, Deal |
| Plan Qualiopi | 🎓 Pédagogie / Qualiopi | `343d62ae-ccba-8182-a9f2-ed278c50ff51` | 7 critères × indicateurs × preuves × échéances |
| Factures émises | ⚙️ Opérationnel / 💰 DAF | `343d62ae-ccba-8172-bcec-e886ba9e58b9` | Factures clients, liées à Devis + Contacts |
| Dépenses | ⚙️ Opérationnel / 💰 DAF | `343d62ae-ccba-813a-a0f4-d9eb8de4ffa8` | Factures fournisseurs + notes de frais associés |
| Page DAF / Finances | ⚙️ Opérationnel | `343d62ae-ccba-810b-be4a-c99bf071c109` | Section finances (à remonter top-level workspace) |

---

## Déploiement en 2 vagues

### Vague 1 — Semaine du 24/03 (pré-BIM World)

Objectif : socle opérationnel pour produire du contenu et piloter.

| Database | Priorité | Pourquoi |
|----------|----------|---------|
| Dashboard | Haute | Point d'entrée équipe |
| Catalogue Formations | Haute | Base de tout (site, contenus, pipe) |
| Calendrier Éditorial | Haute | Machine à contenus = priorité 1 |
| Idées & Brouillons | Haute | Alimenter le calendrier |
| Assets Visuels | Haute | Support des contenus |
| Actions / TODO | Haute | Pilotage opérationnel |
| Réunions & CRs | Haute | Historique décisions |
| Contacts | Moyenne | CRM light pour démarrer |
| Guidelines Com + Messages Clés | Haute | Cadrage ton + arguments de vente |

### Vague 2 — Post-BIM World (avril)

Objectif : structurer le pipe commercial et mesurer le ROI des actions.

| Database | Priorité | Pourquoi |
|----------|----------|---------|
| Pipe Commercial | Haute | Suivre les leads post-BIM |
| Offres commerciales | Moyenne | Packager les formations en offres |
| Funnel Marketing | Moyenne | Mesurer campagnes → leads → ventes |
| Sources d'acquisition | Moyenne | ROI par canal |
| Automations | Basse | Documenter les workflows Make.com |

---

## Databases

### 1. Pipe Commercial

| Propriété | Type | Options |
|-----------|------|---------|
| Nom client | Title | — |
| Statut | Select | Prospect, Qualifié, Devis envoyé, Gagné, Perdu |
| Canal | Select | CAD42, Réseau Igor, Réseau Julien, Réseau Baptiste, Direct, Autre |
| Valeur | Number | € |
| Date contact | Date | — |
| Prochaine action | Text | — |
| Responsable | Person | — |
| Formation liée | Relation | → Catalogue Formations |

### 2. Contacts

| Propriété | Type | Options |
|-----------|------|---------|
| Nom | Title | — |
| Entreprise | Text | — |
| Rôle | Text | — |
| Email | Email | — |
| Téléphone | Phone | — |
| LinkedIn | URL | — |
| Type | Select | Client, Prospect, Partenaire, Formateur, Institutionnel, OPCO |
| Notes | Text | — |

### 3. Actions / TODO

| Propriété | Type | Options |
|-----------|------|---------|
| Action | Title | — |
| Statut | Select | À faire, En cours, Fait, Bloqué |
| Responsable | Person | — |
| Échéance | Date | — |
| Priorité | Select | Haute, Moyenne, Basse |
| Catégorie | Select | Juridique, Commercial, Pédagogie, Com, Tech, Admin |
| Lié à | Relation | → Réunions & CRs |

### 4. Réunions & CRs

| Propriété | Type | Options |
|-----------|------|---------|
| Titre | Title | — |
| Date | Date | — |
| Type | Select | Point hebdo, Comité stratégique, Atelier, Point ad hoc |
| Participants | Multi-select | Igor, Baptiste, Julien, Éloïse |
| CR | Text (page) | Contenu du CR |
| Actions | Relation | → Actions / TODO |

### 5. Catalogue Formations

| Propriété | Type | Options |
|-----------|------|---------|
| Nom formation | Title | — |
| Référence | Text | Ex: 1.2, 1.3 |
| Univers | Select | 🟢 HSE/Prévention, 🟠 Production/Lean |
| Type | Select | Formation Qualiopi, Coaching non Qualiopi |
| Durée | Text | Ex: 0,5 jour, 1 jour |
| Modalité | Select | Présentiel chantier, Présentiel salle, Distanciel, Mixte |
| Sous-traitance | Select | Cresceo direct, Sous-traitée CAD42, Réalisée CAD42 |
| Expert | Person | Igor / Julien |
| Prix HT | Number | € |
| Objectifs pédagogiques | Text | — |
| Indicateurs de réussite | Text | — |
| Statut | Select | Brouillon, Prêt, En ligne, Archivé |
| Fiche site web | Checkbox | Publiée sur cresceo.fr ? |
| Nombre de ventes | Relation | → Pipe Commercial |
| CA généré | Relation | → Pipe Commercial |
| Feedback client | File ou URL | Google Sheet ou Google Form |
| Score de satisfaction | URL | Google Form |

**Formations initiales à saisir :**

| Réf. | Formation | Univers | Type | Sous-traitance |
|------|-----------|---------|------|----------------|
| — | Regard Sécurité (visite NelIA) | 🟢 HSE | Qualiopi | Réalisée CAD42 (Igor) |
| 1.2 | Piloter la Prévention | 🟢 HSE | Qualiopi | Sous-traitée CAD42 |
| 1.3 | Piloter la Production | 🟠 Lean | Qualiopi | Sous-traitée CAD42 |
| 1.4 | Accompagnement personnalisé Prévention | 🟢 HSE | Coaching non Qualiopi | Cresceo direct |
| 1.5 | Accompagnement personnalisé Productivité | 🟠 Lean | Coaching non Qualiopi | Cresceo direct |

### 6. Calendrier Éditorial (Machine à Contenus)

| Propriété | Type | Options |
|-----------|------|---------|
| Titre | Title | — |
| Date publication | Date | — |
| Canal | Multi-select | LinkedIn, Blog, Newsletter, YouTube |
| Format | Select | Post texte, Carrousel, Vidéo courte, Article long, Infographie |
| Statut | Select | Idée, Brouillon, En revue, Prêt, Publié |
| Auteur | Person | Igor, Éloïse, Julien, Baptiste |
| Univers | Select | 🟢 HSE/Prévention, 🟠 Production/Lean, 🔵 Général |
| Formation liée | Relation | → Catalogue Formations |
| Assets | Relation | → Assets Visuels |
| Lien publication | URL | — |
| Engagement | Number | Likes + commentaires (suivi post-publi) |
| Leads générés | Relation | → Pipe Commercial |
| RDV générés | Relation | → Pipe Commercial |
| CA générés | Relation | → Pipe Commercial |

**Vues recommandées :**
- **Calendrier** : vue par date de publication (vue principale)
- **Kanban** : par statut (Idée → Brouillon → En revue → Prêt → Publié)
- **Par canal** : filtre LinkedIn / Blog / etc.
- **Par auteur** : qui doit produire quoi

### 7. Idées & Brouillons

| Propriété | Type | Options |
|-----------|------|---------|
| Titre / Accroche | Title | — |
| Angle | Select | Expertise terrain, Chiffre clé, Témoignage, Actualité secteur, Tuto/How-to, Coulisses |
| Univers | Select | 🟢 HSE, 🟠 Lean, 🔵 Général |
| Source | Text | Idée WhatsApp, retour client, actu… |
| Brouillon | Text (page) | Contenu rédigé |
| Promu en | Relation | → Calendrier Éditorial (quand validé) |
| Priorité | Select | À publier vite, Stock, Saisonnier |

### 8. Assets Visuels

| Propriété | Type | Options |
|-----------|------|---------|
| Nom | Title | — |
| Fichier | Files & media | Upload Notion ou lien Drive |
| Type | Select | Photo chantier, Illustration, Infographie, Vidéo, Template Canva |
| Univers | Select | 🟢 HSE, 🟠 Lean, 🔵 Général |
| Utilisé dans | Relation | → Calendrier Éditorial |
| Source | Text | Canva, Éloïse, Stock, Terrain… |

### 9. Offres Commerciales ← ajout Éloïse

Packages à partir du catalogue formations (ex: Pack IA Chantier, Formation Lean + Coaching, Audit HSE).

| Propriété | Type | Options |
|-----------|------|---------|
| Nom offre | Title | — |
| Type d'offre | Select | Formation, Coaching, Audit, Pack |
| Cible | Select | DRH, Dirigeant BTP, OPCO |
| Promesse | Text | — |
| Problème résolu | Text | — |
| Formations incluses | Relation | → Catalogue Formations |
| Prix HT | Number | € |
| Durée | Text | Ex: 2 jours, 15 jours… |
| Modalité | Select | Présentiel, Distanciel, Mixte |
| Taux de transformation | Formule | Devis → signé (%) |
| CA généré | Relation | → Pipe Commercial |

### 10. Funnel Marketing ← ajout Éloïse

Suivi des campagnes de l'idée au CA.

| Propriété | Type | Options |
|-----------|------|---------|
| Nom campagne | Title | — |
| Objectif | Select | Lead, RDV, Vente |
| Cible | Select | DRH, Dirigeant, OPCO, Apprenant |
| Offre liée | Relation | → Offres Commerciales |
| Contenus liés | Relation | → Calendrier Éditorial |
| Leads générés | Relation | → Pipe Commercial |
| Taux de conversion | Formule | Leads → Vente (%) |

### 11. Sources d'acquisition ← ajout Éloïse

Mesurer le ROI par canal d'acquisition.

| Propriété | Type | Options |
|-----------|------|---------|
| Nom source | Title | — |
| Type | Select | Organique, Ads, Réseau, Partenariat |
| Canal | Select | LinkedIn, Email, Webinaire, Site |
| Campagnes liées | Relation | → Funnel Marketing |
| Leads générés | Relation | → Pipe Commercial |
| CA généré | Relation | → Pipe Commercial |
| Coût | Number | € |
| ROI | Formule | CA / Coût |
| Statut | Select | Actif, Test, Abandonné |

### 12. Automations ← ajout Éloïse

Documentation des scénarios d'automatisation.

| Propriété | Type | Options |
|-----------|------|---------|
| Nom automation | Title | — |
| Outil | Select | Notion, Make, Canva, Metricool, LinkedIn… |
| Déclencheur | Text | Ex: Nouveau lead |
| Action automation | Text | Ex: créer tâche |
| Database concernée | Select | CRM, Contenu, Offres, Funnel |
| Statut | Select | Actif, En test, Inactif |
| Lien scénario | URL | Make.com |

---

## Machine à Contenus — Process

### Architecture d'automatisation

**Objectif** : minimiser les étapes manuelles entre l'idée et la publication.

#### Socle commun (transverse — pas uniquement com/mkg)

Notion Plus sert l'ensemble du projet (CRM, pilotage, pédagogie, réunions…). Son coût n'est pas à imputer au seul budget com.

| Outil | Rôle | Coût/mois | Imputation |
|-------|------|-----------|------------|
| **Notion Plus** (4 users) | Workspace collaboratif complet : CRM, pilotage, pédagogie, calendrier éditorial, webhooks | ~40€ | **Transverse** |
| **Google Drive** | Stockage assets lourds (vidéos, PPT, PDF) | 0€ | Transverse |

#### 3 paliers pour la machine à contenus (budget com/mkg net)

**Palier Alpha — 0€/mois com** (semi-manuel, assisté par IA)

| Outil | Plan | Coût/mois |
|-------|------|-----------|
| Canva Free | Templates manuels (pas de brand kit) | 0€ |
| Metricool Free | Planification LinkedIn (1 marque, 50 posts/mois) | 0€ |
| Claude (interface web) | Rédaction assistée — copier/coller brief → texte | 0€ (inclus abonnement perso) |

- Workflow : saisie idée dans Notion → copier brief dans Claude web → coller le texte dans Notion → visuel Canva manuel → copier dans Metricool → publier
- **~25 min par contenu**
- Suffisant pour démarrer (2-3 posts/semaine)
- Limite : pas d'automatisation, couleurs à appliquer manuellement, copier-coller à chaque étape

**Palier Standard — ~25€/mois com** (semi-automatisé)

| Outil | Plan | Coût/mois |
|-------|------|-----------|
| Make.com Free | 100 opérations/mois (~25 posts) — workflow Notion → Claude API → Notion | 0€ |
| Claude API (via Make) | Génération auto des textes sur changement de statut | ~10-20€ |
| Canva Pro (1 licence) | Brand kit verrouillé (vert HSE / orange Lean), templates pro | 13€ |
| Metricool Free | Planification LinkedIn | 0€ |

- Workflow : saisie idée dans Notion → statut "À rédiger" → **texte généré automatiquement** → revue humaine → visuel Canva (template brand kit) → copier dans Metricool → publier
- **~15 min par contenu**
- Le saut qualitatif : la rédaction IA est automatique (webhook Notion → Make → Claude → Notion), le brand kit garantit la cohérence visuelle
- Limite : publication LinkedIn encore manuelle (copier/coller vers Metricool)

**Palier Full — ~75€/mois com** (automatisé bout en bout)

| Outil | Plan | Coût/mois |
|-------|------|-----------|
| Make.com Teams | Workflows illimités, scénarios complexes | 29€ |
| Claude API (via Make) | Génération auto des textes | ~10-20€ |
| Canva Pro (1 licence) | Brand kit + templates | 13€ |
| Metricool Starter | Publication auto via Make.com + analytics avancés | 18€ |

- Workflow : saisie idée dans Notion → statut "À rédiger" → texte généré auto → revue humaine → visuel Canva → statut "Prêt" → **publication LinkedIn automatique** → lien remonté dans Notion
- **~10-15 min par contenu** (seule la revue et le visuel restent manuels)

**Évolutions ultérieures** (quand le volume le justifie) :

| Outil | Rôle | Coût/mois |
|-------|------|-----------|
| **Templated.io** | Visuels générés automatiquement depuis templates Canva via API | 29$ |
| **Ghost** (self-hosted) | Blog SEO natif + newsletter intégrée | ~7€ |
| **Typefully** | Éditeur LinkedIn spécialisé (hooks, carrousels) | 12,50$ |

#### Récapitulatif des coûts

| Palier | Budget com/mois | + Notion (transverse) | Total réel | Temps/contenu |
|--------|----------------|----------------------|------------|---------------|
| **Alpha** | 0€ | 40€ | 40€ | ~25 min |
| **Standard** | ~25€ | 40€ | ~65€ | ~15 min |
| **Full** | ~75€ | 40€ | ~115€ | ~10-15 min |

**Recommandation** : démarrer **Standard** (25€/mois com) — le meilleur rapport automatisation/prix. La rédaction IA auto est le vrai gain de temps. Monter en Full quand le rythme dépasse 3 posts/semaine.

#### Pourquoi ces choix

- **Make.com >> Zapier** : 3x moins cher, workflow visuel plus puissant, connecteurs Notion + Canva + LinkedIn natifs, interface en français
- **Notion webhooks natifs** (plan Plus) : déclenchement automatique quand un statut change — c'est ce qui rend l'automatisation possible
- **Canva API (autofill)** réservé aux comptes Enterprise (30+ users) → inaccessible, d'où Templated.io en évolution
- **LinkedIn API directe** interdit sans Partner Program → obligation de passer par Metricool/Buffer

### Pipeline automatisé

```
1. CAPTURE              2. RÉDACTION IA           3. REVUE               4. PUBLICATION
   (tous, dans Notion)     (automatique)             (humain, dans Notion)   (automatique)

   Igor/Éloïse/Julien      Make.com déclenché        Éloïse valide le ton    Make.com déclenché
   saisit une idée          quand statut →            Igor valide si           quand statut →
   dans la base "Idées"     "À rédiger"               expertise technique     "Prêt"

   Brief :                  Claude API génère          Visuel Canva créé       → Metricool planifie
   - angle                   le post/article            depuis template          et publie LinkedIn
   - univers (vert/orange)   selon guidelines           (manuel Phase 1,       → Ghost publie blog
   - format (post/article)   + brief                    auto Phase 2)            (Phase 2)
   - formation liée
                            Résultat injecté           Statut → "Prêt"        Lien publication
                            dans Notion                                        remonté dans Notion
                            Statut → "En revue"
```

**Concrètement, le workflow d'un post LinkedIn :**

| Étape | Action | Qui | Temps |
|-------|--------|-----|-------|
| 1 | Saisir l'idée + brief dans Notion | Humain (Igor/Éloïse) | 2 min |
| 2 | Passer le statut à "À rédiger" | Humain | 1 clic |
| 3 | Make.com envoie le brief à Claude API → texte généré → injecté dans Notion | Automatique | ~30 sec |
| 4 | Relire, ajuster, valider | Humain (Éloïse/Igor) | 5 min |
| 5 | Créer le visuel dans Canva (template) | Humain (Éloïse) | 5-10 min |
| 6 | Passer le statut à "Prêt" + date de publication | Humain | 1 clic |
| 7 | Make.com envoie vers Metricool → planifié → publié | Automatique | — |
| 8 | Lien du post remonté dans Notion | Automatique | — |

**Temps humain par contenu : ~15 min** (vs ~45 min en full manuel)

### Guidelines Com (page dédiée)

**Tonalité :**
- Sobre (cibles grands groupes BTP)
- Positive (pas anxiogène — on montre les solutions, pas les problèmes)
- Centrée solutions/formations, pas sur la marque Cresceo

**Ce qu'on met en avant :**
- Les différenciants : formation sur chantier, avec IA, détection de risques en temps réel
- Les experts métiers : Igor (HSE, +15 ans) & Julien (Lean BTP)
- Les résultats concrets : "73% de risques détectés en 3 visites", "l'IA détecte 1 risque/min"

**Ce qu'on évite :**
- Ton corporate/institutionnel creux
- Messages anxiogènes sur les accidents
- Sur-promotion de la marque
- Jargon IA sans valeur ajoutée terrain

### Messages Clés — Formation Regard Sécurité (page dédiée)

> Source : Google Doc "Msg clés Formation Regard sécurité"

**Accroches / Arguments de vente :**
- Seule formation chasse aux risques sur chantier avec IA
- L'utilisateur acquiert directement une compétence
- Formation simple et gamifiée
- Flexible (possible de changer le créneau)
- Il faut juste un téléphone pour chasser les risques sur le chantier
- En 3 visites, l'encadrant double sa capacité à détecter des risques
- Pas besoin de savoir lire : rapports factuels et visuels (photos)
- Conforme RGPD (personnes floutées)
- Accompagnement par des experts HSE de plus de 15 ans d'expérience
- **73% de risques détectés** au bout de 3 visites
- **L'IA détecte un risque par minute**

**Vidéo démo :** https://www.youtube.com/watch?v=1GioarVCvu0

**Angles de contenu possibles :**

| # | Angle | Format suggéré | Canal |
|---|-------|----------------|-------|
| 1 | "73% de risques détectés en 3 visites" — chiffre choc + explication | Post LinkedIn (image + texte) | LinkedIn |
| 2 | Vidéo démo NelIA sur chantier (extrait YouTube) | Vidéo courte / carrousel | LinkedIn |
| 3 | "Pas besoin de savoir lire" — accessibilité et inclusion sur chantier | Post texte (storytelling) | LinkedIn |
| 4 | Avant/après : capacité de détection d'un encadrant en 3 visites | Infographie | LinkedIn, Blog |
| 5 | "1 risque détecté par minute par l'IA" — comment ça marche concrètement | Article blog | Blog, LinkedIn |
| 6 | RGPD et IA sur chantier — comment on protège les données | Article blog | Blog |
| 7 | Témoignage encadrant post-formation (quand dispo) | Post LinkedIn | LinkedIn |

---

## Templates

### Template CR Réunion

```
# CR [Titre] — [Date]

**Participants** : ...
**Durée** : ...

---

## Décisions prises
1. ...

## Actions

| Action | Responsable | Échéance |
|--------|-------------|----------|
| ... | ... | ... |

## Points en suspens
- ...

## Prochaine réunion
- Date :
- Objet :
```

### Template Fiche Formation (pour le catalogue)

```
# [Réf.] [Nom Formation]

**Univers** : 🟢 HSE / 🟠 Lean
**Durée** : ...
**Modalité** : Présentiel chantier / salle / distanciel
**Expert** : Igor Cannone / Julien Gardette
**Prix** : ... € HT

## Objectifs pédagogiques
- À l'issue de la formation, le stagiaire sera capable de :
  1. ...
  2. ...

## Public cible
- ...

## Prérequis
- ...

## Programme
1. ...
2. ...

## Moyens pédagogiques
- ...

## Modalités d'évaluation
- ...

## Indicateurs de réussite
- Taux de satisfaction : ...
- Taux de réussite : ...

## Accessibilité
- Référent handicap : [Nom] — [Contact]
- Adaptation possible sur demande
```

### Template Post LinkedIn

```
# [Accroche — 1 ligne max]

[Corps du post — 3-5 paragraphes courts]

[CTA ou question ouverte]

#FormationBTP #IAChantier #Prévention #Cresceo
```

---

## Migration depuis Docsify

### Documents à importer

| Document Docsify | Destination Notion |
|------------------|-------------------|
| CONTEXTE_PROJET.md | Stratégie / Contexte Projet |
| Business Plan.md | Stratégie / Business Plan |
| ANALYSE_MARCHE.md | Stratégie / Analyse Marché |
| PLAN_LANCEMENT_CRESCEO.md | Opérationnel / Plan de Lancement |
| CRs ateliers / réunions | Réunions & CRs (database) |

### Process de migration

1. Créer le workspace Notion "Cresceo"
2. Inviter les membres (Igor, Julien, Baptiste, Éloïse)
3. Créer la structure (pages + databases)
4. Importer les contenus MD (Notion parse le Markdown)
5. Configurer les templates
6. Saisir les formations dans le catalogue
7. Configurer la machine à contenus (calendrier + idées)
8. Archiver Docsify (garder GitHub Pages en backup)

---

## Qonto ↔ Notion — Synchronisation

**Objectif** : voir dans Notion (DB Dépenses) les transactions Qonto, sans re-saisir manuellement.

**Source de vérité** : Qonto reste la source comptable. Pennylane est la référence fiscale. Notion est une vue opérationnelle enrichie (catégorisation métier, rattachement à des chantiers/clients, suivi notes de frais).

### 3 options évaluées

| Option | Mécanisme | Coût mensuel | Setup | Avantage | Limite |
|--------|-----------|--------------|-------|----------|--------|
| **A. Make.com** (reco) | Webhook Qonto API → Make scénario → création ligne Notion Dépenses | 0€ (plan gratuit, 1000 ops/mois suffisent) | 1-2h | DIY, contrôle total, déjà prévu pour Machine à Contenus | Doit être maintenu |
| **B. Pennylane natif** | Pennylane agrège Qonto + comptabilité, export manuel vers Notion | Pennylane déjà prévu | 0 | Pas de dev | Pas de sync auto Notion, ressaisie ou export CSV |
| **C. Zapier Qonto** | Trigger Qonto → action Notion | ~20€/mois Zapier Starter | 30 min | Plus simple que Make | Payant, moins puissant que Make |

### Recommandation : Option A (Make.com)

**Justification** :
- Make.com est **déjà prévu** pour la Machine à Contenus (Notion ↔ Claude API ↔ Metricool) → on mutualise l'abonnement
- **Plan gratuit** (1 000 opérations / mois) suffit pour Cresceo Y1 (50-100 transactions/mois prévues)
- **Qonto a une API officielle** bien documentée (https://api-doc.qonto.com) avec auth IBAN + API key
- Plus fin que Pennylane sur les règles de catégorisation custom (ex: distinguer sous-traitance CAD42 vs prestation juridique)

### Scénario Make à construire (V1)

```
Trigger: Qonto new transaction (polling 1×/h)
  ↓
Filter: amount ≠ 0 AND status = "completed"
  ↓
Router:
  ├── IF operation_type = "card" → Notion: create Dépense (type = Prestation ponctuelle)
  ├── IF operation_type = "transfer" (sortant) → Notion: create Dépense
  ├── IF operation_type = "transfer" (entrant, client) → Notion: mark Facture as Payée (match sur Numéro dans label)
  └── ELSE → notification Slack/mail pour classement manuel
  ↓
Enrichissement IA (optionnel, Claude API) : extraction fournisseur + catégorie suggérée depuis le libellé Qonto
  ↓
Notion: create row in Dépenses avec pré-remplissage
```

**Champs pré-remplis automatiquement** : Date, Montant HT/TTC, Fournisseur (libellé Qonto), Payée par = "Qonto Cresceo", Statut = "Payée".
**Champs à compléter manuellement** : Catégorie, Type (si pas déduit), Notes, Justificatif (lien Drive).

### Setup requis (hors scope du 15/04)

1. Créer une API key Qonto (dans paramètres Qonto → Intégrations → API)
2. Stocker la clé dans Make.com (pas dans settings repo)
3. Builder le scénario Make (~1h)
4. Tester sur 1 semaine de transactions historiques
5. Activer le cron

**Estimation effort** : 2h de build + 1 semaine observation avant production.

### Alternative (si Make trop lourd au démarrage)

En Y1 démarrage : **export mensuel CSV depuis Qonto** (1 clic) → import manuel dans la DB Dépenses Notion (10 min/mois). À utiliser les 1-2 premiers mois pendant qu'on construit le scénario Make.

---

## Permissions

| Membre | Niveau | Périmètre |
|--------|--------|-----------|
| Igor, Baptiste, Julien, Éloïse | Full access | Tout |

## Intégrations

| Intégration | Usage | Via |
|-------------|-------|----|
| Google Drive | Stockage assets lourds (vidéos, PPT, PDF) | Liens dans Notion |
| Canva Pro | Templates visuels (vert HSE / orange Lean) | Manuel (Phase 1), Templated.io (Phase 2) |
| Make.com | Orchestration : Notion → Claude API → Metricool | Webhooks Notion |
| Claude API | Génération/enrichissement textes selon guidelines | Make.com |
| Metricool | Planification + publication LinkedIn | Make.com |
| Google Calendar | Sync dates réunions et deadlines | Notion natif |
| Ghost (Phase 2) | Blog SEO + newsletter | Make.com → Ghost API |

---

## Prochaines étapes

### Vague 1 — Workspace Notion (semaine du 24/03)
- [ ] Baptiste : créer le workspace Notion Plus + inviter l'équipe
- [ ] Éloïse : valider la structure (retour intégré ci-dessus)
- [ ] Baptiste/Éloïse : déployer la structure Vague 1 (pages + databases)
- [ ] Baptiste : saisir les 5 formations dans le catalogue
- [ ] Baptiste : importer les docs Docsify dans Stratégie/Opérationnel
- [ ] Igor : alimenter les messages clés pour chaque formation

### Vague 2 — Machine à contenus (palier Standard recommandé, post-BIM)
- [ ] Baptiste : configurer Make.com (scénario Notion → Claude API → Notion)
- [ ] Éloïse : créer les templates Canva Pro verrouillés (1 vert HSE, 1 orange Lean — post + carrousel)
- [ ] Baptiste : configurer Metricool (connexion page LinkedIn)
- [ ] Éloïse + Igor : saisir 10 idées de contenu dans la base "Idées"
- [ ] Tous : tester le workflow complet (idée → rédaction IA → revue → visuel → publication)
- [ ] Baptiste : déployer les databases Vague 2 (Pipe, Offres, Funnel, Sources, Automations)

### Vague 3 — Montée en puissance (quand volume le justifie)
- [ ] Passer Make.com en Teams + Metricool Starter (palier Full — publication auto)
- [ ] Déployer Ghost (blog SEO + newsletter)
- [ ] Intégrer Templated.io (visuels automatiques)
- [ ] Évaluer Typefully pour les power users LinkedIn (Igor)

---

*Document créé le 4 février 2026 — Mis à jour le 24 mars 2026 (intégration retours Éloïse)*
