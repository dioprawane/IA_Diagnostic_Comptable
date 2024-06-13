import json

data = [
    {"prompt": "Définition du bilan financier :", "completion": "Le bilan financier est un bilan comptable après la répartition du résultat et présenté en valeurs nettes."},
    {"prompt": "Objectifs du bilan financier :", "completion": "Le bilan financier permet d’apprécier la structure financière de l’entreprise dans une optique de liquidation, d’évaluer la patrimoine réel, de déterminer l’équilibre financier, en comparant les différentes masses du bilan classées selon leur degré de liquidité ou d’exigibilité et en observant le degré de couverture du passif exigible par les actifs liquides, d’étudier la solvabilité et la liquidité de l’entreprise, de calculer la marge de sécurité financière de l’entreprise, et d’estimer les risques courus par les créanciers et les associés."},
    {"prompt": "Structure du bilan financier :", "completion": "Tableau en deux parties (actif et passif) regroupant des postes par ordre croissant de liquidité pour les actifs et par ordre croissant d’exigibilité pour les passifs."}
]

with open('training2.jsonl', 'w', encoding='utf-8') as f:
    for entry in data:
        json.dump(entry, f)
        f.write('\n')
