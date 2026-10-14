"""Generate cresceo.fr SEO landing pages (one URL per search intent).

Usage: python build_pages.py <site_dir>
Reuses nav + footer from <site_dir>/formations.html so the pages stay in sync with the site chrome.
Course @ids reference the Course entities emitted by seo_schema.py on formations.html.
"""
import html
import json
import sys
from pathlib import Path

SITE = "https://cresceo.fr"
ORG_ID = f"{SITE}/#organization"
WEBSITE_ID = f"{SITE}/#website"
UPDATED = "2026-10-12"
UPDATED_FR = "12 octobre 2026"
C_RS = f"{SITE}/formations.html#regard-securite"
C_PREV = f"{SITE}/formations.html#prevention"
C_LEAN = f"{SITE}/formations.html#lean"

GA4 = """  <!-- GA4 (chargé uniquement après consentement) -->
  <script>
    window.gaLoaded = false;
    function loadGA4() {
      if (window.gaLoaded) return;
      window.gaLoaded = true;
      var s = document.createElement('script');
      s.src = 'https://www.googletagmanager.com/gtag/js?id=G-7BZC8Y1G2Q';
      s.async = true;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-7BZC8Y1G2Q');
    }
    if (localStorage.getItem('cresceo_consent') === 'accepted') { loadGA4(); }
  </script>"""

QUALIOPI = ("Cresceo est certifié Qualiopi au titre des actions de formation (certificat n° 875611-1 délivré par "
            "Certifopac, valable jusqu'au 06/09/2029)")

# --------------------------------------------------------------------------- pages

PAGES = [
    # ------------------------------------------------------------------ pilier
    {
        "slug": "formation-ia-btp",
        "nav": "Formation IA BTP",
        "title": "Formation IA BTP certifiée Qualiopi, finançable OPCO | Cresceo",
        "description": "Formation intelligence artificielle pour le BTP, certifiée Qualiopi : détection des risques chantier, prévention, Lean Construction. Sur vos chantiers, dès 400 €, finançable OPCO Constructys.",
        "h1": "Formation IA pour le BTP, certifiée Qualiopi",
        "subtitle": "Former l'encadrement de chantier à utiliser l'intelligence artificielle pour la prévention et la productivité.",
        "lead": (f"{QUALIOPI}. Ses formations IA sont conçues pour le chantier, pas pour le bureau : vos conducteurs de travaux, "
                 "chefs de chantier et préventeurs filment une visite au smartphone, l'IA analyse la vidéo, et un formateur expert "
                 "du BTP les aide à transformer ces données en actions de prévention ou de productivité. 3 formations, à partir de "
                 "400 € par participant, finançables par l'OPCO Constructys."),
        "facts": [("Formations", "3 parcours + accompagnement"), ("Durée", "7 h ou 4 x 1 h"),
                  ("Tarif", "Dès 400 € / participant"), ("Financement", "OPCO Constructys, FAF")],
        "courses": [C_RS, C_PREV, C_LEAN],
        "body": """
<h2>Ce que l'IA change concrètement sur un chantier</h2>
<p>L'œil humain s'habitue : après quelques semaines sur un chantier, l'encadrement ne voit plus certaines situations à risque ni certains temps morts. C'est l'effet tunnel. L'intelligence artificielle apporte un regard objectif sur la réalité du terrain :</p>
<ul>
  <li><strong>Prévention</strong> : détection des situations à risque sur une vidéo de visite (coactivité engins-piétons, risques de chute, postures à l'origine de TMS), avec des rapports visuels et factuels.</li>
  <li><strong>Productivité</strong> : mesure des cycles de production (par exemple les cycles de grue), repérage des temps morts et des goulets d'étranglement, tableaux de bord de suivi.</li>
  <li><strong>Animation</strong> : quarts d'heure sécurité et réunions de coordination préparés à partir d'images réelles de vos chantiers.</li>
</ul>
<p>La solution d'analyse vidéo utilisée en formation est développée par notre partenaire technologique CAD.42. Les images sont traitées dans un cadre conforme au RGPD (floutage des personnes).</p>

<h2>Nos formations IA pour le BTP</h2>
<div class="table-wrap"><table class="cr-programme-table">
  <thead><tr><th>Formation</th><th>Objectif</th><th>Durée et format</th><th>Tarif</th></tr></thead>
  <tbody>
    <tr><td><a href="formation-prevention-risques-chantier-ia.html#regard-securite"><strong>Regard Sécurité</strong></a></td><td>Détecter les risques chantier grâce à l'analyse vidéo par IA</td><td>7 h, hybride (4 h distanciel + 3 h terrain)</td><td>400 € / participant</td></tr>
    <tr><td><a href="formation-prevention-risques-chantier-ia.html#piloter-la-prevention"><strong>Piloter la Prévention avec l'IA</strong></a></td><td>Piloter les indicateurs sécurité et animer la prévention</td><td>4 semaines (4 x 1 h), hybride</td><td>Dès 400 € HT / participant</td></tr>
    <tr><td><a href="formation-lean-construction-ia.html"><strong>Piloter la Productivité avec l'IA</strong></a></td><td>Lean Construction : chasser les gaspillages, piloter la production</td><td>4 semaines (4 x 1 h), distanciel</td><td>Dès 400 € HT / participant</td></tr>
  </tbody>
</table></div>
<p>Pour un déploiement sur plusieurs chantiers ou plusieurs équipes, voir notre <a href="formation-ia-btp-grandes-entreprises.html">offre intra-entreprise pour les grands comptes</a>.</p>

<h2>Pourquoi une formation IA spécifique au BTP</h2>
<p>La plupart des formations à l'IA apprennent à utiliser un assistant conversationnel pour rédiger des documents. Utile, mais cela ne change pas ce qui se passe sur le chantier. Les formations Cresceo partent du terrain :</p>
<ul>
  <li><strong>Sur vos chantiers</strong> : la mission pratique se fait sur vos propres situations de travail, pas sur des cas d'école.</li>
  <li><strong>Des formateurs issus du chantier</strong> : plus de 15 ans d'expérience en prévention HSE et en Lean Construction.</li>
  <li><strong>Des résultats mesurés</strong> : indicateurs avant et après la formation, avec une capacité de détection des risques multipliée par 3 et une identification des gaspillages multipliée par 2.</li>
  <li><strong>Simple</strong> : un smartphone suffit, aucune compétence informatique avancée n'est requise.</li>
</ul>

<h2>Comment choisir une formation IA pour le BTP</h2>
<p>Avant de vous engager, vérifiez 6 points :</p>
<ol>
  <li><strong>La certification Qualiopi</strong> de l'organisme, vérifiable dans la liste publique des organismes de formation sur data.gouv.fr. Elle conditionne le financement par votre OPCO.</li>
  <li><strong>Des cas d'usage chantier</strong> (sécurité, production, coordination) et pas seulement de la bureautique.</li>
  <li><strong>Une mise en pratique sur le terrain</strong>, idéalement sur vos propres chantiers.</li>
  <li><strong>Le profil des formateurs</strong> : expérience opérationnelle du BTP, pas uniquement de l'IA.</li>
  <li><strong>L'évaluation des acquis</strong> : positionnement initial, exercices, évaluation finale.</li>
  <li><strong>Le cadre RGPD</strong> dès qu'il y a captation d'images de personnes sur chantier.</li>
</ol>

<h2>Certification Qualiopi et financement</h2>
<p>Cresceo est certifié Qualiopi (certificat n° 875611-1, Certifopac) et enregistré sous le numéro de déclaration d'activité 11757694675. Nos formations peuvent être prises en charge par l'OPCO Constructys pour les entreprises du BTP, ou par un FAF pour les dirigeants non salariés, dans la limite des plafonds de votre financeur. Plafonds, démarches et délais : <a href="financement-formation-btp-constructys.html">financer une formation BTP avec Constructys</a>. Indicateurs de résultats : <a href="qualite.html">qualité et certification</a>.</p>
""",
        "faq": [
            ("Faut-il des compétences en informatique pour suivre une formation IA BTP ?",
             "Non. Une maîtrise basique d'un ordinateur (visioconférence, navigateur web) et un smartphone avec accès internet suffisent. Regard Sécurité ne demande aucun prérequis."),
            ("Où se déroulent les formations ?",
             "Partout en France : la partie théorique se fait en classe virtuelle et la mise en pratique sur vos propres chantiers."),
            ("Les formations IA de Cresceo sont-elles finançables ?",
             "Oui. Cresceo étant certifié Qualiopi, ses formations sont éligibles à une prise en charge par l'OPCO de l'entreprise (Constructys pour le BTP) ou par un FAF pour les dirigeants non salariés, dans la limite des plafonds de votre financeur (par exemple 24 € HT de l'heure pour les entreprises du Bâtiment de moins de 11 salariés chez Constructys)."),
            ("Quelle formation choisir pour commencer ?",
             "Regard Sécurité (7 h, sans prérequis) est la porte d'entrée : elle montre en une journée ce que l'IA voit sur un chantier. Les parcours Piloter la Prévention et Piloter la Productivité s'adressent ensuite aux encadrants responsables d'un chantier actif."),
        ],
        "related": ["formation-prevention-risques-chantier-ia", "formation-lean-construction-ia", "financement-formation-btp-constructys", "formation-ia-btp-grandes-entreprises"],
    },
    # ------------------------------------------------------------------ prévention
    {
        "slug": "formation-prevention-risques-chantier-ia",
        "nav": "Prévention des risques chantier",
        "title": "Formation prévention des risques chantier avec l'IA, Qualiopi | Cresceo",
        "description": "Formation détection et prévention des risques chantier grâce à l'IA : Regard Sécurité (7 h, 400 €) et Piloter la Prévention (4 x 1 h). Certifiée Qualiopi, finançable OPCO Constructys.",
        "h1": "Formation prévention des risques chantier avec l'IA",
        "subtitle": "Apprendre à voir les risques que l'habitude rend invisibles, puis piloter la prévention par la donnée.",
        "lead": ("2 formations certifiées Qualiopi pour l'encadrement de chantier. Regard Sécurité (7 h, 400 € par participant, sans prérequis) "
                 "apprend à détecter les situations à risque grâce à l'analyse vidéo par IA d'une visite de chantier. Piloter la Prévention "
                 "avec l'IA (4 semaines, 4 x 1 h, dès 400 € HT) apprend à piloter les indicateurs sécurité et à animer la prévention à partir "
                 "de preuves visuelles. Les 2 sont finançables par l'OPCO Constructys."),
        "facts": [("Public", "Conducteurs de travaux, chefs de chantier, préventeurs"), ("Durée", "7 h ou 4 x 1 h"),
                  ("Tarif", "Dès 400 € / participant"), ("Résultat", "Détection des risques x 3")],
        "courses": [C_RS, C_PREV],
        "body": """
<h2>Pourquoi l'encadrement ne voit plus certains risques</h2>
<p>Sur un chantier que l'on parcourt chaque jour, le cerveau filtre : c'est l'effet tunnel, un biais cognitif bien documenté. Des situations dangereuses deviennent « normales » (coactivité entre engins et piétons, protections collectives déplacées, postures pénibles répétées). L'analyse vidéo par IA ne s'habitue pas : elle objective ce que l'œil ne voit plus, et donne à l'encadrant un point de comparaison pour entraîner son propre regard.</p>

<h2 id="regard-securite">Regard Sécurité : détecter les risques chantier grâce à l'IA</h2>
<p><strong>7 heures (1 journée), hybride : 4 h en distanciel + 3 h sur le terrain. 400 € par participant. Aucun prérequis.</strong></p>
<p>À l'issue de la formation, le participant sait identifier les situations à risque « invisibles » (coactivité engins-piétons, chutes, TMS) grâce à l'outil d'IA, et interpréter les rapports générés pour prioriser ses actions de prévention.</p>
<div class="table-wrap"><table class="cr-programme-table">
  <thead><tr><th>Séquence</th><th>Durée</th><th>Contenu</th></tr></thead>
  <tbody>
    <tr><td><strong>1. Fondamentaux</strong></td><td>2 h</td><td>Biais cognitifs et effet tunnel, présentation de l'IA, cadre RGPD et floutage (classe virtuelle).</td></tr>
    <tr><td><strong>2. Mission terrain</strong></td><td>3 h</td><td>Captation vidéo d'une visite au smartphone et dépôt sur une plateforme sécurisée (ou analyse d'une vidéo fournie).</td></tr>
    <tr><td><strong>3. Analyse et action</strong></td><td>2 h</td><td>Débriefing avec un expert : « vision humaine contre vision IA », plan de progrès personnel.</td></tr>
  </tbody>
</table></div>
<p>Évaluation : questionnaire de positionnement, exercices d'identification de risques sur photos, quiz final (seuil de réussite 80 %). <a href="formations.html#regard-securite">Voir la fiche programme complète</a>.</p>

<h2 id="piloter-la-prevention">Piloter la Prévention avec l'IA : animer la sécurité par la donnée</h2>
<p><strong>4 semaines (4 x 1 h), hybride. À partir de 400 € HT par participant. Prérequis : être responsable d'un chantier actif.</strong></p>
<ul>
  <li><strong>Semaine 1</strong> : l'IA au service d'une prévention bienveillante, prise en main de l'interface.</li>
  <li><strong>Semaine 2</strong> : filtrer les risques, lire les indicateurs, extraire les rapports d'intervention.</li>
  <li><strong>Semaine 3</strong> : préparer un quart d'heure sécurité avec des images réelles captées par l'IA.</li>
  <li><strong>Semaine 4</strong> : suivre les actions correctives, construire son plan de progrès.</li>
</ul>
<p>Le parcours fait évoluer la posture managériale : passer de la sanction au coaching, en s'appuyant sur des faits visuels plutôt que sur des impressions. <a href="formations.html#prevention">Voir la fiche programme</a>.</p>

<h2>Ce que la formation apporte à l'entreprise</h2>
<ul>
  <li>Une capacité de détection des risques multipliée par 3 chez les encadrants formés.</li>
  <li>Des observations factuelles et visuelles pour alimenter l'évaluation des risques et le <a href="formation-duerp-btp.html">DUERP</a>.</li>
  <li>Des rituels sécurité (quarts d'heure, causeries) plus concrets, construits sur vos propres chantiers.</li>
  <li>Une réponse à l'obligation de formation à la sécurité des travailleurs (Code du travail, articles L4141-2 et suivants).</li>
</ul>
<p>Sur nos 8 premières sessions : 100 % de participants satisfaits et une recommandation moyenne de 9,6/10 (<a href="qualite.html">indicateurs détaillés</a>).</p>
""",
        "faq": [
            ("Combien de temps dure la formation Regard Sécurité ?",
             "7 heures sur 1 journée, en format hybride : 4 h en classe virtuelle et 3 h de mission terrain sur un chantier."),
            ("Faut-il être déjà équipé d'une solution IA ?",
             "Non pour Regard Sécurité : un smartphone suffit et l'analyse est réalisée pendant la formation. Le parcours Piloter la Prévention suppose en revanche un compte opérationnel sur la solution IA."),
            ("Les personnes filmées sur le chantier sont-elles protégées ?",
             "Oui. Le cadre RGPD est présenté dès la première séquence, les personnes sont floutées et les vidéos sont déposées sur une plateforme sécurisée."),
            ("La formation est-elle finançable ?",
             "Oui, par l'OPCO Constructys pour les entreprises du BTP ou par un FAF pour les dirigeants non salariés, Cresceo étant certifié Qualiopi."),
        ],
        "related": ["formation-ia-btp", "formation-duerp-btp", "accueil-securite-chantier", "financement-formation-btp-constructys"],
    },
    # ------------------------------------------------------------------ lean
    {
        "slug": "formation-lean-construction-ia",
        "nav": "Lean Construction",
        "title": "Formation Lean Construction avec l'IA, certifiée Qualiopi | Cresceo",
        "description": "Formation Lean Construction BTP : chasser les gaspillages et piloter la productivité chantier grâce à l'IA. 4 x 1 h en distanciel, dès 400 € HT, certifiée Qualiopi, finançable OPCO.",
        "h1": "Formation Lean Construction avec l'IA",
        "subtitle": "Mesurer la réalité du chantier pour réduire les gaspillages et piloter la production par la donnée.",
        "lead": ("Piloter la Productivité avec l'IA est une formation Lean Construction certifiée Qualiopi de 4 semaines (4 x 1 h en classe virtuelle), "
                 "à partir de 400 € HT par participant. Elle apprend aux conducteurs de travaux, chefs de chantier et responsables méthodes à "
                 "mesurer les cycles de production grâce à l'IA, repérer les temps morts et les gaspillages, et animer la coordination à partir "
                 "de données factuelles. Finançable par l'OPCO Constructys."),
        "facts": [("Public", "Conducteurs, chefs de chantier, méthodes"), ("Durée", "4 semaines (4 x 1 h)"),
                  ("Tarif", "Dès 400 € HT / participant"), ("Résultat", "Gaspillages identifiés x 2")],
        "courses": [C_LEAN],
        "image": ("assets/ia-prod/prod-chronoanalyse.jpg", "Chronoanalyse IA d'un cycle de grue avec détection automatique des séquences", 1200, 561),
        "body": """
<h2>Le Lean Construction appliqué au chantier</h2>
<p>Le Lean vise à supprimer tout ce qui n'apporte pas de valeur à l'ouvrage. Sur un chantier, les gaspillages classiques sont bien connus :</p>
<ul>
  <li><strong>Attentes</strong> : grue occupée, livraison en retard, plan manquant.</li>
  <li><strong>Transports et manutentions</strong> inutiles de matériaux.</li>
  <li><strong>Stocks</strong> qui encombrent les zones de travail.</li>
  <li><strong>Déplacements</strong> superflus des compagnons.</li>
  <li><strong>Reprises et non-qualité</strong>.</li>
  <li><strong>Surproduction</strong> (préparer trop tôt) et <strong>surtraitement</strong> (contrôles redondants).</li>
</ul>
<p>La difficulté n'est pas de les connaître, mais de les mesurer. C'est là que l'IA change la donne : l'analyse vidéo permet de chronométrer les cycles (par exemple ceux d'une grue), de détecter les temps morts et de comparer le prévu au réalisé, sans chronométreur sur place.</p>
{image}

<h2>Programme de la formation Piloter la Productivité avec l'IA</h2>
<ul>
  <li><strong>Semaine 1</strong> : l'IA au service de l'efficacité opérationnelle, capteurs et prise en main de l'interface productivité.</li>
  <li><strong>Semaine 2</strong> : la chasse aux gaspillages, tableaux de bord personnalisés, lecture des indicateurs, détection des temps morts.</li>
  <li><strong>Semaine 3</strong> : animer la performance et la coordination terrain, préparer une réunion de planification avec les données IA.</li>
  <li><strong>Semaine 4</strong> : amélioration continue, suivi des actions d'optimisation, mesure de l'impact, plan de progrès personnel.</li>
</ul>
<p>Méthodes : classes virtuelles interactives, exercices sur données réelles, analyse de rapports de production, simulation de réunion de coordination. Prérequis : être responsable d'un chantier actif et disposer d'un compte sur la solution IA. <a href="formations.html#lean">Voir la fiche programme</a>.</p>

<h2>Objectifs pédagogiques</h2>
<ul>
  <li>Concevoir des tableaux de bord et indicateurs de productivité pour identifier goulets d'étranglement et temps morts.</li>
  <li>Passer d'une gestion réactive à une planification proactive fondée sur des données terrain.</li>
  <li>Piloter les indicateurs de production pour optimiser les flux et réduire les gaspillages.</li>
  <li>Animer les réunions de coordination à partir de preuves factuelles et visuelles.</li>
</ul>

<h2>Aller plus loin : l'accompagnement productivité</h2>
<p>En complément, Cresceo propose un accompagnement Lean appliqué à votre contexte : optimisation des flux, chronoanalyse, plan d'actions opérationnel et suivi des indicateurs de performance. Le formateur référent est Julien Gardette, spécialiste de l'optimisation de production et du Lean Management appliqué à la construction.</p>
""",
        "faq": [
            ("Qu'est-ce que le Lean Construction ?",
             "C'est l'application au BTP des principes du Lean : identifier et supprimer ce qui n'apporte pas de valeur à l'ouvrage (attentes, manutentions, stocks, reprises), et organiser le flux de production pour livrer plus vite, avec moins d'aléas."),
            ("En quoi l'IA aide-t-elle une démarche Lean sur chantier ?",
             "Elle mesure automatiquement ce qui demandait un chronométreur : cycles de grue, temps morts, enchaînement des tâches. Les décisions se prennent sur des données factuelles plutôt que sur des impressions."),
            ("La formation se fait-elle sur le chantier ?",
             "Les 4 séances d'1 h se déroulent en classe virtuelle, sur les données réelles de votre chantier."),
            ("La formation Lean Construction est-elle finançable ?",
             "Oui, par l'OPCO Constructys pour les entreprises du BTP, Cresceo étant certifié Qualiopi."),
        ],
        "related": ["formation-ia-btp", "formation-prevention-risques-chantier-ia", "financement-formation-btp-constructys", "formation-ia-btp-grandes-entreprises"],
    },
    # ------------------------------------------------------------------ DUERP (guide)
    {
        "slug": "formation-duerp-btp",
        "nav": "DUERP BTP",
        "title": "DUERP BTP : obligations, mise à jour et formation | Cresceo",
        "description": "DUERP dans le BTP : qui doit le réaliser, quand le mettre à jour, quelles sanctions, et comment former l'encadrement de chantier à l'évaluation des risques. Guide Cresceo, organisme Qualiopi.",
        "h1": "DUERP dans le BTP : obligations et formation de l'encadrement",
        "subtitle": "Ce que dit le Code du travail, et comment des observations terrain fiables alimentent votre document unique.",
        "lead": ("Tout employeur, dès le premier salarié, doit évaluer les risques professionnels et transcrire les résultats dans un document unique "
                 "d'évaluation des risques professionnels (DUERP), à mettre à jour au moins chaque année dans les entreprises d'au moins 11 salariés "
                 "et à chaque changement important. Dans le BTP, où les situations de travail évoluent chaque jour, la qualité du DUERP dépend de la "
                 "capacité de l'encadrement à repérer les risques sur le terrain : c'est ce que développent les formations Cresceo."),
        "facts": [("Concerné", "Tout employeur dès 1 salarié"), ("Mise à jour", "Annuelle dès 11 salariés"),
                  ("Conservation", "40 ans"), ("Sanction", "Contravention de 5e classe")],
        "courses": [C_RS, C_PREV],
        "body": """
<h2>Ce que dit le Code du travail</h2>
<ul>
  <li><strong>Évaluer les risques</strong> : l'employeur évalue les risques pour la santé et la sécurité des travailleurs (article L4121-3).</li>
  <li><strong>Les transcrire</strong> dans un document unique, qui inventorie les risques identifiés dans chaque unité de travail (articles L4121-3-1 et R4121-1).</li>
  <li><strong>Le mettre à jour</strong> au moins chaque année dans les entreprises d'au moins 11 salariés, lors de toute décision d'aménagement important modifiant les conditions de travail, et lorsqu'une information supplémentaire sur un risque est connue (article R4121-2).</li>
  <li><strong>En tirer un plan d'actions</strong> : programme annuel de prévention (PAPRIPACT) dans les entreprises d'au moins 50 salariés, liste d'actions de prévention en dessous (article L4121-3-1).</li>
  <li><strong>Le conserver</strong> dans ses versions successives pendant au moins 40 ans et le tenir à disposition des travailleurs et des anciens travailleurs.</li>
</ul>
<p>L'absence de transcription ou de mise à jour de l'évaluation des risques est punie de l'amende prévue pour les contraventions de 5e classe (article R4741-1).</p>

<h2>Les spécificités du BTP</h2>
<p>Dans le BTP, le DUERP se heurte à une difficulté propre : le lieu de travail change sans cesse. Phases de gros œuvre et de second œuvre, coactivité entre entreprises, engins, travail en hauteur, conditions météorologiques : un document rédigé une fois par an au bureau décrit mal la réalité. Le DUERP d'une entreprise de BTP doit s'appuyer sur des observations régulières et précises des situations de travail, et s'articuler avec les documents propres au chantier (plan de prévention, PPSPS).</p>

<h2>Le rôle de l'encadrement de chantier</h2>
<p>Ce sont les conducteurs de travaux et les chefs de chantier qui voient les situations à risque, ou qui ne les voient plus. L'habitude crée un effet tunnel : des dangers deviennent invisibles à force d'être quotidiens. Former l'encadrement à « voir » les risques est donc la condition d'une évaluation des risques sincère, et d'un DUERP utile plutôt que formel.</p>

<h2>Comment nos formations alimentent votre DUERP</h2>
<p>Cresceo ne rédige pas votre document unique à votre place : nos formations outillent l'encadrement pour l'alimenter avec des observations factuelles.</p>
<ul>
  <li><a href="formation-prevention-risques-chantier-ia.html#regard-securite"><strong>Regard Sécurité</strong></a> (7 h, 400 €) : l'analyse vidéo par IA d'une visite de chantier fait apparaître les situations à risque, photos à l'appui. L'encadrant apprend à les repérer lui-même et à prioriser les actions.</li>
  <li><a href="formation-prevention-risques-chantier-ia.html#piloter-la-prevention"><strong>Piloter la Prévention avec l'IA</strong></a> (4 x 1 h) : suivi des indicateurs sécurité dans la durée et des actions correctives, une matière directement réutilisable pour la mise à jour du DUERP et le plan d'actions.</li>
</ul>
<p>Ces formations répondent aussi à l'obligation générale de formation à la sécurité des travailleurs (article L4141-2) et sont finançables par l'OPCO Constructys.</p>
<p class="source-note">Sources : Code du travail, articles L4121-3, L4121-3-1, R4121-1, R4121-2, R4741-1 et L4141-2 (<a href="https://www.legifrance.gouv.fr/" rel="noopener" target="_blank">Légifrance</a>). Page à valeur informative, qui ne constitue pas un conseil juridique.</p>
""",
        "faq": [
            ("Le DUERP est-il obligatoire pour une petite entreprise du BTP ?",
             "Oui. L'obligation s'applique à tout employeur dès le premier salarié, quelle que soit la taille de l'entreprise."),
            ("À quelle fréquence mettre à jour le DUERP ?",
             "Au moins chaque année dans les entreprises d'au moins 11 salariés, et dans tous les cas lors d'un aménagement important modifiant les conditions de travail ou lorsqu'une information nouvelle sur un risque est connue."),
            ("Que risque une entreprise sans DUERP à jour ?",
             "L'absence de transcription ou de mise à jour est punie de l'amende des contraventions de 5e classe. En cas d'accident, l'absence d'évaluation des risques pèse aussi lourdement dans l'appréciation de la responsabilité de l'employeur."),
            ("Existe-t-il une formation DUERP obligatoire ?",
             "Le Code du travail n'impose pas de formation spécifique au DUERP, mais il impose d'évaluer les risques et de former les travailleurs à la sécurité. Former l'encadrement à repérer les risques est le moyen le plus direct de fiabiliser l'évaluation."),
        ],
        "related": ["formation-prevention-risques-chantier-ia", "accueil-securite-chantier", "formation-ia-btp", "financement-formation-btp-constructys"],
        "article": True,
    },
    # ------------------------------------------------------------------ accueil sécurité
    {
        "slug": "accueil-securite-chantier",
        "nav": "Accueil sécurité chantier",
        "title": "Accueil sécurité chantier externalisé, dès 75 € HT | Cresceo",
        "description": "Externalisez l'accueil sécurité de vos nouveaux arrivants, intérimaires et CDD sur chantier : à partir de 75 € HT par accueil (minimum 20). Organisme certifié Qualiopi.",
        "h1": "Accueil sécurité chantier externalisé",
        "subtitle": "Former chaque nouvel arrivant à la sécurité dès le premier jour, sans mobiliser votre encadrement.",
        "lead": ("Cresceo prend en charge l'accueil sécurité de vos nouveaux arrivants, intérimaires et salariés en CDD, à partir de 75 € HT par accueil "
                 "(minimum 20 participants). Vous répondez à l'obligation de formation à la sécurité à l'embauche prévue par le Code du travail, "
                 "votre encadrement garde son temps pour le chantier, et vos équipes montent en compétence dès le premier jour."),
        "facts": [("Tarif", "Dès 75 € HT / accueil"), ("Volume", "Minimum 20 participants"),
                  ("Public", "Embauches, intérim, CDD"), ("Organisme", "Certifié Qualiopi")],
        "courses": [],
        "body": """
<h2>Une obligation à chaque arrivée</h2>
<ul>
  <li><strong>Formation à la sécurité à l'embauche</strong> : l'employeur organise une formation pratique et appropriée à la sécurité au bénéfice des travailleurs qu'il embauche, de ceux qui changent de poste ou de technique, et des travailleurs temporaires (article L4141-2 du Code du travail).</li>
  <li><strong>Son objet</strong> : instruire le travailleur des précautions à prendre pour sa propre sécurité et celle des autres personnes présentes (article R4141-3).</li>
  <li><strong>Formation renforcée</strong> pour les salariés en CDD et les intérimaires affectés à des postes présentant des risques particuliers (article L4154-2).</li>
</ul>
<p>Sur un chantier où les arrivées sont fréquentes (intérim, sous-traitance, renforts), l'accueil sécurité mobilise beaucoup de temps d'encadrement, et sa qualité varie d'un accueil à l'autre.</p>

<h2>Ce que vous gagnez à l'externaliser</h2>
<ul>
  <li><strong>Un accueil homogène</strong>, construit à partir de vos consignes et des risques propres à vos chantiers.</li>
  <li><strong>Du temps rendu à l'encadrement</strong>, qui reste concentré sur la production et la prévention au quotidien.</li>
  <li><strong>Un interlocuteur unique</strong>, organisme de formation certifié Qualiopi.</li>
</ul>

<h2>Tarif et organisation</h2>
<p>À partir de 75 € HT par accueil, pour un minimum de 20 participants. Le contenu et l'organisation sont définis avec vous selon vos chantiers et vos volumes d'arrivées. Un financement est possible selon votre situation : <a href="financement-formation-btp-constructys.html">voir les démarches de financement</a>.</p>
<p>Pour aller plus loin avec votre encadrement, découvrez notre <a href="formation-prevention-risques-chantier-ia.html">formation prévention des risques chantier avec l'IA</a>.</p>
""",
        "faq": [
            ("L'accueil sécurité est-il obligatoire pour les intérimaires ?",
             "Oui. La formation pratique et appropriée à la sécurité concerne aussi les travailleurs temporaires, et une formation renforcée est due aux intérimaires et salariés en CDD affectés à des postes à risques particuliers."),
            ("Combien coûte un accueil sécurité externalisé ?",
             "À partir de 75 € HT par accueil, avec un minimum de 20 participants."),
            ("Le contenu est-il adapté à nos chantiers ?",
             "Oui, il est défini avec vous à partir de vos consignes et des risques propres à vos chantiers."),
        ],
        "related": ["formation-prevention-risques-chantier-ia", "formation-duerp-btp", "financement-formation-btp-constructys", "formation-ia-btp"],
    },
    # ------------------------------------------------------------------ financement
    {
        "slug": "financement-formation-btp-constructys",
        "nav": "Financement Constructys",
        "title": "Financer une formation BTP avec Constructys (OPCO) | Cresceo",
        "description": "Comment faire financer une formation BTP par l'OPCO Constructys ou un FAF : plafonds 2026, délai de 15 jours, démarches eGestion, documents. Formations IA BTP certifiées Qualiopi.",
        "h1": "Financer une formation BTP avec l'OPCO Constructys",
        "subtitle": "Démarches, documents et bons réflexes pour faire prendre en charge vos formations.",
        "lead": ("Les entreprises du BTP peuvent faire financer leurs formations par Constructys, l'opérateur de compétences (OPCO) de la construction, "
                 "à condition que l'organisme soit certifié Qualiopi. Cresceo l'est (certificat n° 875611-1) : ses formations IA, prévention et "
                 "Lean Construction sont finançables dans la limite des plafonds de Constructys : dans le Bâtiment, 24 € HT par heure et par "
                 "stagiaire pour les entreprises de moins de 11 salariés, 19 € HT de 11 à 49 salariés. La demande complète doit parvenir à "
                 "Constructys sur eGestion au moins 15 jours avant le début de la formation."),
        "facts": [("OPCO du BTP", "Constructys"), ("Condition", "Organisme certifié Qualiopi"),
                  ("Plafond Bâtiment", "24 € HT/h (< 11 sal.), 19 € HT/h (11-49)"), ("Délai", "15 jours avant, via eGestion")],
        "courses": [],
        "body": """
<h2>Qui finance quoi ?</h2>
<div class="table-wrap"><table class="cr-programme-table">
  <thead><tr><th>Votre situation</th><th>Financeur</th></tr></thead>
  <tbody>
    <tr><td>Entreprise du BTP (salariés)</td><td><strong>Constructys</strong>, OPCO de la construction, au titre du plan de développement des compétences</td></tr>
    <tr><td>Entreprise de l'industrie</td><td>Son OPCO de branche, par exemple <strong>OPCO 2i</strong> pour l'interindustrie</td></tr>
    <tr><td>Artisan ou dirigeant non salarié</td><td>Le <strong>fonds d'assurance formation (FAF)</strong> dont il relève, par exemple le FAFCEA pour les artisans ou l'AGEFICE pour les dirigeants du commerce et des services</td></tr>
  </tbody>
</table></div>
<p>Les règles de prise en charge (plafonds, critères, taille d'entreprise) sont fixées par chaque financeur et évoluent régulièrement : vérifiez les conditions en vigueur sur le site de votre OPCO ou de votre FAF.</p>

<h2>Combien Constructys prend-il en charge en 2026 ?</h2>
<p>Barème du plan de développement des compétences de la branche Bâtiment, applicable aux demandes reçues à partir du 1er juin 2026 (actions non qualifiantes, dans la limite de 300 heures par stagiaire) :</p>
<div class="table-wrap"><table class="cr-programme-table">
  <thead><tr><th>Taille de l'entreprise</th><th>Plafond coût pédagogique</th><th>Plafond en intra-entreprise</th><th>Frais de salaire</th></tr></thead>
  <tbody>
    <tr><td>Moins de 11 salariés</td><td>24 € HT / heure / stagiaire</td><td>840 € HT / jour / groupe</td><td>15 € HT / heure / stagiaire</td></tr>
    <tr><td>11 à 49 salariés</td><td>19 € HT / heure / stagiaire</td><td>665 € HT / jour / groupe</td><td>Actions qualifiantes et cas particuliers uniquement</td></tr>
    <tr><td>50 à 299 salariés</td><td colspan="3">Participation sur le budget de l'entreprise : à voir avec votre délégation régionale</td></tr>
  </tbody>
</table></div>
<p><strong>Exemple</strong> : pour Regard Sécurité (7 h, 400 € par participant), le plafond Constructys représente 168 € par participant dans une entreprise du Bâtiment de moins de 11 salariés (7 h x 24 €), et 133 € de 11 à 49 salariés (7 h x 19 €). Le reste est à la charge de l'entreprise, ou finançable par d'autres dispositifs selon votre situation : demandez-nous une estimation.</p>
<p>Pour les entreprises de moins de 300 salariés, Constructys finance aussi des <strong>actions Lean Management</strong> dans la limite de 1 000 € HT par jour (2 jours de diagnostic et 6 jours d'accompagnement au maximum), un cadre adapté à notre <a href="formation-lean-construction-ia.html">accompagnement Lean Construction</a>. Les montants sont des plafonds, accordés dans la limite des fonds disponibles. Pour les Travaux publics, les modalités sont à vérifier auprès de votre délégation régionale.</p>
<p class="source-note">Source : Constructys, « Plan de développement des compétences, modalités de participation financière », juin 2026, et page <a href="https://www.constructys.fr/financer-vos-projets-de-formation/modalites-demandes-de-prise-charge/conditions-de-prise-en-charge-2/" rel="noopener" target="_blank">conditions de prise en charge</a>. Barème en vigueur au 14 octobre 2026.</p>

<h2>Les démarches, étape par étape</h2>
<ol>
  <li><strong>Demandez un devis et le programme</strong> de la formation à Cresceo.</li>
  <li><strong>Déposez la demande de prise en charge</strong> complète sur l'espace en ligne de votre OPCO ou FAF. Chez Constructys : plateforme <strong>eGestion</strong> obligatoire, <strong>au moins 15 jours calendaires avant le début</strong> de la formation. Une formation déjà commencée n'est pas finançable.</li>
  <li><strong>Recevez l'accord de financement</strong>, puis signez la convention de formation.</li>
  <li><strong>La formation a lieu</strong> ; nous émettons les attestations et les justificatifs de réalisation.</li>
  <li><strong>Règlement</strong> : selon l'accord, l'OPCO règle directement l'organisme de formation (subrogation) ou rembourse l'entreprise.</li>
</ol>

<h2>Les documents que Cresceo vous fournit</h2>
<ul>
  <li>Devis et programme détaillé (objectifs, durée, modalités, évaluation).</li>
  <li>Convention de formation.</li>
  <li>Attestations de fin de formation et justificatifs de réalisation.</li>
  <li>Certificat Qualiopi n° 875611-1 et numéro de déclaration d'activité 11757694675.</li>
</ul>

<h2>Les formations concernées</h2>
<ul>
  <li><a href="formation-prevention-risques-chantier-ia.html">Regard Sécurité et Piloter la Prévention avec l'IA</a> (prévention des risques chantier).</li>
  <li><a href="formation-lean-construction-ia.html">Piloter la Productivité avec l'IA</a> (Lean Construction).</li>
  <li><a href="accueil-securite-chantier.html">Accueil sécurité externalisé</a>, financement possible selon votre situation.</li>
</ul>
""",
        "faq": [
            ("Quel est l'OPCO des entreprises du BTP ?",
             "Constructys est l'opérateur de compétences (OPCO) de la construction. Il finance notamment les formations du plan de développement des compétences des entreprises du BTP."),
            ("Quand faut-il déposer la demande de prise en charge ?",
             "Chez Constructys, la demande complète doit parvenir sur la plateforme eGestion au moins 15 jours calendaires avant le début de la formation. Déposez-la le plus tôt possible : les financements dépendent des fonds disponibles."),
            ("Combien Constructys prend-il en charge sur une formation ?",
             "Dans la branche Bâtiment, pour les demandes reçues depuis le 1er juin 2026, Constructys finance le coût pédagogique dans la limite de 24 € HT par heure et par stagiaire pour les entreprises de moins de 11 salariés, et de 19 € HT de 11 à 49 salariés. Les entreprises de moins de 11 salariés peuvent aussi obtenir une participation aux frais de salaire (15 € HT par heure). Pour les Travaux publics, renseignez-vous auprès de votre délégation régionale."),
            ("Une formation déjà commencée peut-elle être financée ?",
             "Non. La demande doit parvenir complète à Constructys au moins 15 jours avant le début de la formation, et une formation qui a démarré avant la réception de la demande n'est pas éligible."),
            ("Pourquoi la certification Qualiopi est-elle importante pour le financement ?",
             "Depuis le 1er janvier 2022, seuls les organismes certifiés Qualiopi peuvent bénéficier des fonds publics et mutualisés de la formation, dont ceux des OPCO."),
        ],
        "related": ["formation-ia-btp", "formation-prevention-risques-chantier-ia", "formation-lean-construction-ia", "accueil-securite-chantier"],
        "article": True,
    },
    # ------------------------------------------------------------------ grands comptes
    {
        "slug": "formation-ia-btp-grandes-entreprises",
        "nav": "Grandes entreprises",
        "title": "Formation IA BTP intra-entreprise pour grands comptes | Cresceo",
        "description": "Déployez la formation IA prévention et Lean Construction sur vos chantiers et vos équipes : parcours intra-entreprise sur mesure, indicateurs avant/après, organisme certifié Qualiopi. Sur devis.",
        "h1": "Formation IA BTP pour les grandes entreprises",
        "subtitle": "Un déploiement intra-entreprise, chantier par chantier, avec des résultats mesurés.",
        "lead": ("Pour les entreprises générales, majors et ETI du BTP, Cresceo déploie ses formations IA en intra-entreprise : prévention des risques "
                 "chantier, pilotage de la sécurité et Lean Construction, adaptés à vos chantiers, vos process et vos indicateurs. Les sessions se "
                 "font en petits groupes, avec un suivi des indicateurs avant et après formation. Organisme certifié Qualiopi, tarification sur devis."),
        "facts": [("Format", "Intra-entreprise, petits groupes"), ("Périmètre", "Plusieurs chantiers et équipes"),
                  ("Pilotage", "Indicateurs avant / après"), ("Tarif", "Sur devis")],
        "courses": [C_RS, C_PREV, C_LEAN],
        "body": """
<h2>Ce que nous déployons</h2>
<ul>
  <li><strong>Prévention</strong> : <a href="formation-prevention-risques-chantier-ia.html">Regard Sécurité et Piloter la Prévention avec l'IA</a> pour l'encadrement de chantier et les préventeurs.</li>
  <li><strong>Productivité</strong> : <a href="formation-lean-construction-ia.html">Piloter la Productivité avec l'IA</a>, parcours Lean Construction pour conducteurs de travaux et méthodes.</li>
  <li><strong>Accueil sécurité</strong> : <a href="accueil-securite-chantier.html">externalisation des accueils</a> des nouveaux arrivants, intérimaires et CDD.</li>
  <li><strong>Accompagnement</strong> : coaching terrain post-formation, prévention ou productivité.</li>
</ul>

<h2>Un déploiement pensé pour les grands comptes</h2>
<ol>
  <li><strong>Cadrage</strong> : objectifs, chantiers pilotes, populations cibles, indicateurs de référence.</li>
  <li><strong>Ingénierie</strong> : adaptation des contenus à vos standards sécurité, vos modes opératoires et vos outils.</li>
  <li><strong>Déploiement par vagues</strong> : sessions en petits groupes, chantier par chantier, en classe virtuelle et sur le terrain.</li>
  <li><strong>Mesure</strong> : indicateurs avant et après (détection des risques, gaspillages identifiés), satisfaction et acquis.</li>
  <li><strong>Ancrage</strong> : accompagnement des encadrants et retours d'expérience pour les vagues suivantes.</li>
</ol>

<h2>Les garanties</h2>
<ul>
  <li>Organisme certifié Qualiopi (certificat n° 875611-1), formations éligibles au plan de développement des compétences.</li>
  <li>Formateurs experts du terrain, plus de 15 ans d'expérience en prévention HSE et Lean Construction.</li>
  <li>Solution d'analyse vidéo IA de notre partenaire technologique CAD.42, cadre RGPD (floutage des personnes).</li>
  <li>Finaliste des Trophées de l'Innovation du WinLab' CCCA-BTP (BATIMAT 2026).</li>
  <li>Premiers résultats : 100 % de satisfaction et 9,6/10 de recommandation sur 8 sessions (<a href="qualite.html">indicateurs</a>).</li>
</ul>
<p>Chaque déploiement fait l'objet d'une proposition sur mesure. <a href="/#contact">Demandez un échange</a> pour cadrer votre projet.</p>
""",
        "faq": [
            ("Les formations peuvent-elles être adaptées à nos standards internes ?",
             "Oui. En intra-entreprise, les contenus sont adaptés à vos standards sécurité, vos modes opératoires et vos outils lors d'une phase d'ingénierie préalable."),
            ("Combien coûte un déploiement intra-entreprise ?",
             "La tarification se fait sur devis, selon le nombre de participants, de chantiers et le niveau d'accompagnement souhaité."),
            ("Comment mesurez-vous l'impact de la formation ?",
             "Par des indicateurs avant et après formation (capacité de détection des risques, gaspillages identifiés), complétés par l'évaluation des acquis et la satisfaction des participants."),
        ],
        "related": ["formation-ia-btp", "formation-prevention-risques-chantier-ia", "formation-lean-construction-ia", "financement-formation-btp-constructys"],
    },
]

BY_SLUG = {p["slug"]: p for p in PAGES}

# --------------------------------------------------------------------------- rendering


def esc(s):
    return html.escape(s, quote=True)


def jsonld(page):
    url = f"{SITE}/{page['slug']}.html"
    webpage = {
        "@type": "Article" if page.get("article") else "WebPage",
        "@id": f"{url}#webpage",
        "url": url,
        ("headline" if page.get("article") else "name"): page["h1"],
        "description": page["description"],
        "inLanguage": "fr-FR",
        "isPartOf": {"@id": WEBSITE_ID},
        "publisher": {"@id": ORG_ID},
        "dateModified": UPDATED,
    }
    if page.get("article"):
        webpage["author"] = {"@id": ORG_ID}
        webpage["datePublished"] = UPDATED
        webpage["mainEntityOfPage"] = url
    if page["courses"]:
        webpage["about"] = [{"@id": c} for c in page["courses"]]
    graph = [
        webpage,
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "Formations", "item": f"{SITE}/formations.html"},
                {"@type": "ListItem", "position": 3, "name": page["nav"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page["faq"]
            ],
        },
    ]
    body = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return "\n".join("  " + l for l in body.split("\n"))


def published_posts_by_page():
    """Map intent-page slug -> published blog posts linking to it (cta or related), newest first."""
    import yaml

    by_page = {}
    for f in sorted((Path(__file__).resolve().parents[1] / "blog").glob("*.md"), reverse=True):
        meta = yaml.safe_load(f.read_text(encoding="utf-8").split("---", 2)[1])
        if meta.get("status") != "published":
            continue
        for slug in {meta["cta"], *meta.get("related", [])}:
            by_page.setdefault(slug, []).append(meta)
    return by_page


def blog_section(posts):
    if not posts:
        return ""
    cards = "\n".join(
        f'      <a class="related-card" href="/blog/{p["slug"]}.html"><span>{esc(p["title"])}</span>'
        f'<small>{esc(p["description"])}</small></a>'
        for p in posts[:4]
    )
    return f"""
    <nav class="related" aria-label="Articles du blog">
      <h2>Sur le blog</h2>
      <div class="related-grid">
{cards}
      </div>
    </nav>
"""


def render(page, nav_html, footer_html, posts=()):
    url = f"{SITE}/{page['slug']}.html"
    facts = "\n".join(
        f'        <div class="fiche-meta-item"><span class="fiche-meta-label">{esc(k)}</span>'
        f'<span class="fiche-meta-value">{esc(v)}</span></div>'
        for k, v in page["facts"]
    )
    faq = "\n".join(
        f'      <details class="faq-item">\n        <summary>{esc(q)}</summary>\n        <p>{esc(a)}</p>\n      </details>'
        for q, a in page["faq"]
    )
    related = "\n".join(
        f'      <a class="related-card" href="{r}.html"><span>{esc(BY_SLUG[r]["nav"])}</span>'
        f'<small>{esc(BY_SLUG[r]["subtitle"])}</small></a>'
        for r in page["related"]
    )
    image = ""
    if page.get("image"):
        src, alt, w, h = page["image"]
        image = f'<figure class="content-figure"><img src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy"><figcaption>{esc(alt)}</figcaption></figure>'
    body = page["body"].replace("{image}", image)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(page['title'])}</title>
  <meta name="description" content="{esc(page['description'])}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">

  <meta property="og:title" content="{esc(page['title'])}">
  <meta property="og:description" content="{esc(page['description'])}">
  <meta property="og:type" content="{'article' if page.get('article') else 'website'}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/logo.png">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="Cresceo">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(page['title'])}">
  <meta name="twitter:description" content="{esc(page['description'])}">
  <meta name="twitter:image" content="{SITE}/assets/logo.png">

  <link rel="icon" type="image/png" href="assets/icon.png">

{GA4}

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/cresceo.css">
  <link rel="stylesheet" href="assets/css/formations.css">
  <link rel="stylesheet" href="assets/css/pages.css">

  <script type="application/ld+json">
{jsonld(page)}
  </script>
</head>
<body>
{nav_html}
  <!-- PAGE HEADER -->
  <header class="page-header">
    <div class="breadcrumb">
      <a href="/">Accueil</a> <span>/</span> <a href="formations.html">Formations</a> <span>/</span> <span style="color: rgba(255,255,255,0.7);">{esc(page['nav'])}</span>
    </div>
    <h1>{esc(page['h1'])}</h1>
    <p>{esc(page['subtitle'])}</p>
    <p style="font-size:0.8rem;color:rgba(255,255,255,0.5);margin-top:1rem;">Dernière mise à jour : {UPDATED_FR}</p>
  </header>

  <main class="page-content">
    <section class="answer-box" aria-label="En bref">
      <p class="answer-lead">{esc(page['lead'])}</p>
      <div class="fiche-meta">
{facts}
      </div>
      <div class="answer-cta"><a href="/#contact" class="btn btn-primary">Obtenir un devis</a></div>
    </section>

    <article class="content-body">
{body}
    </article>

    <section class="content-faq" id="faq">
      <h2>Questions fréquentes</h2>
{faq}
    </section>

    <nav class="related" aria-label="Pages liées">
      <h2>À lire aussi</h2>
      <div class="related-grid">
{related}
      </div>
    </nav>
{blog_section(posts)}  </main>

  <section class="cta-section">
    <h2>Un projet de formation ?</h2>
    <p>Recevez un devis et un programme détaillé, et faites le point sur votre financement.</p>
    <a href="/#contact" class="btn btn-primary">Obtenir un devis</a>
    <p class="cta-email">ou directement : <a href="mailto:contact@cresceo.fr">contact@cresceo.fr</a></p>
  </section>

{footer_html}"""


def footer_links_html():
    links = " &middot; ".join(f'<a href="{p["slug"]}.html">{esc(p["nav"])}</a>' for p in PAGES)
    return f'    <p class="footer-seo-links">{links}</p>\n'


def main(site_dir):
    site = Path(site_dir)
    tpl = (site / "formations.html").read_text(encoding="utf-8")
    nav_html = tpl[tpl.index("  <!-- NAV -->"):tpl.index("  <!-- PAGE HEADER -->")]
    footer_html = tpl[tpl.index("  <!-- FOOTER -->"):]
    # Inject the SEO link row into the footer (idempotent: only if not already present in template)
    if "footer-seo-links" not in footer_html:
        footer_html = footer_html.replace("  </footer>", footer_links_html() + "  </footer>", 1)
    posts = published_posts_by_page()
    for page in PAGES:
        out = site / f"{page['slug']}.html"
        out.write_text(render(page, nav_html, footer_html, posts.get(page["slug"], [])), encoding="utf-8")
        print("wrote", out.name)


if __name__ == "__main__":
    main(sys.argv[1])
