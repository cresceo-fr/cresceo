# Visuels LinkedIn Cresceo (HTML → PNG)

Système de cartes LinkedIn 1080x1080 piloté par la charte Cresceo (système « Ascension & précision » : fond bleu profond, diagonales ascendantes vert/orange, coins nets, Montserrat/Roboto, logo). Rendu local en PNG via navigateur headless (Edge/Chrome). Remplace les gabarits Canva génériques.

## Fichiers
- `card.html` : template unique, 3 modèles (stat / tips / news), piloté par query-string.
- `render.ps1` : rend une carte en PNG (URL-encode les valeurs tout seul).
- `cresceo-logo.png` : logo wordmark recadré (fond transparent).

## Rendu
```powershell
cd "COM/templates/linkedin"
.\render.ps1 -Out "..\..\drafts\weekly\2026-Wxx-<slug>.png" -Params "type=...&kicker=...&title=..."
```
Sortie : PNG 2160x2160 (haute résolution, LinkedIn downscale sans perte).

## Paramètres
Communs : `type` (stat|tips|news|formation), `kicker` (accroche, ex. "Prévention · HSE"), `title` (mettre `*mot*` pour surligner), `hl` (vert|orange, couleur du surlignage, défaut vert).

- **stat** : `num` (ex. 87), `unit` (défaut %), `ring` (0-100, défaut = num), `sub` (ligne orange), `source`.
- **tips** : `intro` (ligne grise sous le titre), `t1`, `t2`, `t3`.
- **news** : `m1`, `m2`, `m3` (lignes meta), `sub` (ligne orange).
- **formation** : `sub` (accroche orange), `s1`, `s2`, `s3` (specs à puces), `cta` (ligne verte, ex. "Programme complet sur cresceo.fr").

## Exemples
Stat :
```
type=stat&kicker=Prévention · HSE&title=Les *TMS*, 1ʳᵉ cause de maladies professionnelles du BTP.&num=87&sub=Et ça se prévient.&source=Source : Cnam
```
Tips :
```
type=tips&kicker=Prévention · HSE&title=Chutes de *plain-pied* : les éviter&intro=Environ 15% des accidents du BTP, la 2ᵉ cause.&t1=...&t2=...&t3=...
```
News :
```
type=news&kicker=BATIMAT 2026&title=Rendez-vous à *BATIMAT*&m1=Stand WinLab' · Hall H1, Stand H32&m2=28/09 au 01/10 · Porte de Versailles
```
Formation :
```
type=formation&kicker=Catalogue formation&title=Regard Sécurité *augmenté par l'IA*&sub=Triplez votre capacité à détecter les risques en 3 visites.&s1=2h, en présentiel sur site&s2=Certifié Qualiopi, éligible OPCO et CPF&s3=Dirigeants, préventeurs, conducteurs de travaux&cta=Programme complet sur cresceo.fr
```

## Notes
- **Polices embarquées** : `fonts.css` contient Montserrat (500/600/700/800) et Roboto (400) en base64. Rendu 100% hors-ligne, aucun appel réseau. Pour régénérer `fonts.css`, re-télécharger les woff2 depuis Google Fonts (CSS2) et les encoder en base64.
- Les 3 chips Tips sont vert / orange / vert (le 2e en orange pour le rythme) ; les puces Formation sont des carrés orange (angles nets).
- Charte de référence : `COM/Charte-Graphique_CRESCEO.pdf`.
