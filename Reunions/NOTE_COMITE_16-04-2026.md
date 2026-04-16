# Note pour le comité — 16 avril 2026

> Synthèse des avancées opérationnelles (Baptiste, sessions 14-16/04)

---

## 1. Notion — Workspace opérationnel déployé

Le workspace Notion Cresceo est passé de "socle vague 1" (pages vides + 3 DBs basiques) à un **outil de pilotage opérationnel complet** :

**Bases créées et actives :**
- 🧾 **Devis** (dans Commercial) — lié à Contacts, Offres, Catalogue Formations, Pipe
- 📤 **Factures émises** (dans DAF) — liée à Devis + Contacts
- 📥 **Dépenses** (dans DAF) — factures fournisseurs + notes de frais associés (catégorisation par poste, workflow remboursement)
- ☑️ **Plan Qualiopi** (dans Pédagogie) — 7 critères × indicateurs × preuves × statut × échéance. À peupler avec le Google Doc d'Igor
- 💰 **Page DAF / Finances** — avec process notes de frais documenté

**Usine à contenu :**
- 5 idées SEO seedées dans Idées & brouillons (3 HSE, 1 Lean, 1 Général) — prêtes à passer en rédaction
- Architecture validée : palier Standard (~25€/mois com) — Make.com + Claude API + Canva Pro

**Pipeline veille AO :**
- En production depuis le 14/04 (3 sources, scoring IA Claude, alimentation automatique Notion)

**Intégration Notion API :**
- Connexion MCP opérationnelle → Claude Code peut créer/modifier directement dans Notion

## 2. DAF — Finances structurées

- Section 💰 DAF créée avec Factures émises + Dépenses
- **Spec Qonto ↔ Notion** documentée → reco Make.com (plan gratuit, ~2h de build)
- En attendant l'automation : export CSV mensuel Qonto (10 min/mois)
- Prochaine étape : créer API key Qonto + builder le scénario Make (S17-S18)

## 3. RC Pro — Devis reçus, décision à prendre

Deux devis obtenus :

| | Hiscox (direct) | Orus/AXA (via Qonto) |
|---|---|---|
| Prix annuel | 223€ HT | 231€ HT |
| RC Pro / sinistre | 100 000 € | **1 200 000 €** |
| RC Exploitation | 8 000 000 € | 9 000 000 € |
| Franchise | 0 € | 380 € (matériels) |

**Reco** : Orus/Qonto — plafond RC Pro 12× supérieur pour +8€/an, plus adapté au risque BTP chantier.

**Timing impératif** : souscrire avant le **10/05** (session physique Lyon 21/05 + attestation pour dossier Qualiopi).

Note complète : `DAF/NOTE_RC_PRO.md`

## 4. Qualiopi — Bascule CertifOPAC confirmée

- **Certificateur** : CertifOPAC (plus ICPF)
- **Entité client** : Cresceo SAS (résolu — pas Elfe Conseil)
- Facture F-2026-04-2725 reçue : 388€ HT (audit blanc Sérénité)
- **Pré-audit** : fait (13/04)
- **Audit initial** : date à confirmer avec CertifOPAC — objectif mai

## 5. CGV — V2 rédigée (13 articles)

La v1 (8 articles, 2 pages) avait des **lacunes de conformité significatives**. La v2 corrige :

| Lacune v1 | Correction v2 |
|-----------|---------------|
| Adresse siège erronée (Rueil vs 58 Monceau 75008) | ✅ Corrigée |
| Aucun droit de rétractation BtoC | ✅ Art. 3.2 — 10/14 jours (R.6353-1) |
| RGPD succinct (3 lignes) | ✅ Art. 8 — base légale, durée, droits, sous-traitants, CNIL |
| Pas d'indemnité 40€ recouvrement | ✅ Art. 4.3 (L.441-10) |
| Pas de clause OPCO | ✅ Art. 4.4 — subrogation + responsabilité Client si refus |
| Pas de référent handicap | ✅ Art. 9 — Igor, accessibilite@cresceo.fr |
| Pas de médiateur consommation | ✅ Art. 12.2 — placeholder, à désigner |
| PI floue sur données IA | ✅ Art. 7.3 — propriété stagiaire, usage anonymisé algo |

**Prochaines étapes** : relecture Me Frachon (05/05) → PDF brandé → déploiement avant audit Qualiopi.

Checklist détaillée (70+ items) : `Juridique/CHECKLIST_CGV_OF.md`

## 6. LinkedIn — Checklist prête

Page LinkedIn Cresceo : **pas encore créée**. Checklist complète livrée (`COM/LINKEDIN_CHECKLIST.md`) — pré-requis, About, admins, 5 posts de lancement J0→J21.

**Décision** : si Éloïse n'a pas créé la page d'ici le **22/04**, Baptiste prend le lead.

---

## Décisions à prendre demain

1. **RC Pro** : valider Orus/Qonto (1,2M€/sinistre, 231€/an) → souscrire cette semaine ?
2. **Naming formations CAD42** : "CRESCEO designed for CAD42" ou "Formations CAD42 by Cresceo" ?
3. **Qualiopi** : date exacte audit initial avec CertifOPAC ? Igor appelle ?
4. **Référent handicap = Igor** : confirmation officielle ?
5. **LinkedIn** : Éloïse s'en charge d'ici le 22 ou Baptiste prend ?
