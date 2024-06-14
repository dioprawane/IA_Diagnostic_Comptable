import json

data = [
    {"messages": [{"role": "user", "content": "Définition du bilan financier :"}, {"role": "assistant", "content": "Le bilan financier est un bilan comptable après la répartition du résultat et présenté en valeurs nettes."}]},
    {"messages": [{"role": "user", "content": "Objectifs du bilan financier :"}, {"role": "assistant", "content": "Le bilan financier permet d’apprécier la structure financière de l’entreprise dans une optique de liquidation, d’évaluer la patrimoine réel, de déterminer l’équilibre financier, en comparant les différentes masses du bilan classées selon leur degré de liquidité ou d’exigibilité et en observant le degré de couverture du passif exigible par les actifs liquides, d’étudier la solvabilité et la liquidité de l’entreprise, de calculer la marge de sécurité financière de l’entreprise, et d’estimer les risques courus par les créanciers et les associés."}]},
    {"messages": [{"role": "user", "content": "Structure du bilan financier :"}, {"role": "assistant", "content": "Tableau en deux parties (actif et passif) regroupant des postes par ordre croissant de liquidité pour les actifs et par ordre croissant d’exigibilité pour les passifs."}]},
    {"messages": [{"role": "user", "content": "Qu'est-ce qu'un actif fictif ?"}, {"role": "assistant", "content": "Un actif fictif comprend des postes qui n'ont aucune valeur actuelle, comme les frais d'établissements, les frais de développement, les charges à répartir sur plusieurs exercices, et les primes de remboursement des obligations."}]},
    {"messages": [{"role": "user", "content": "Comment évaluer le patrimoine réel ?"}, {"role": "assistant", "content": "Pour évaluer le patrimoine réel, il faut éliminer les actifs fictifs du bilan comptable et intégrer les plus-values latentes."}]},
    {"messages": [{"role": "user", "content": "Comment déterminer l'équilibre financier ?"}, {"role": "assistant", "content": "L'équilibre financier est déterminé en comparant les différentes masses du bilan classées selon leur degré de liquidité ou d'exigibilité, et en observant le degré de couverture du passif exigible par les actifs liquides."}]},
    {"messages": [{"role": "user", "content": "Quels sont les objectifs de l'analyse financière ?"}, {"role": "assistant", "content": "Les objectifs de l'analyse financière sont d'étudier la solvabilité et la liquidité de l'entreprise, de calculer la marge de sécurité financière, et d'estimer les risques courus par les créanciers et les associés."}]},
    {"messages": [{"role": "user", "content": "Quels postes doivent être éliminés du bilan comptable ?"}, {"role": "assistant", "content": "Certains postes de l'actif, comme les frais d'établissements, les frais de développement, les charges à répartir sur plusieurs exercices, et les primes de remboursement des obligations, doivent être éliminés car ils constituent l'actif fictif."}]},
    {"messages": [{"role": "user", "content": "Pourquoi intégrer des éléments hors bilan ?"}, {"role": "assistant", "content": "L'intégration d'éléments hors bilan permet de refléter une image plus précise de la situation financière réelle de l'entreprise en tenant compte de toutes les obligations et ressources disponibles."}]},
    {"messages": [{"role": "user", "content": "Comment reclasse-t-on les postes du bilan comptable ?"}, {"role": "assistant", "content": "Le reclassement des postes du bilan comptable se fait en fonction de leur degré de liquidité pour les actifs et de leur degré d'exigibilité pour les passifs."}]}
]

with open('training2.jsonl', 'w', encoding='utf-8') as f:
    for entry in data:
        json.dump(entry, f)
        f.write('\n')
