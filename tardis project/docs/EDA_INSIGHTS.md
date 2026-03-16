# EDA Report : Tardis

## 1) Objectif :
L’objectif de l’analyse exploratoire est de comprendre la structure du dataset SNCF et d’identifier les variables importantes pour prédire les retards 

## 2) Données utilisées :
Source : `cleaned_dataset.csv`  
Période : 2018–2025  
11 230 lignes – 28 colonnes  

Chaque ligne correspond à une liaison ferroviaire pour un mois donné

## 3) Analyse des retards :
Le retard moyen au départ est plus élevé pour le service **National (~12.57 min)** que pour l’**International (~10.53 min)**
Cela montre que le type de service influence le niveau de retard
L’analyse graphique par année montre également une évolution des retards dans le temps

*Ces résultats ont été observés à l’aide de visualisations (histogrammes et graphiques en barres), ce qui a permis d’identifier des différences claires entre les types de service*

## 4) Causes principales :
Les retards sont principalement liés à :
- L’infrastructure
- Les causes externes
- La gestion du trafic

Ces facteurs ont un impact important sur la ponctualité

## 5) Variables importantes pour le modèle :
Les variables les plus pertinentes sont :
- `Service`
- `Gare de départ`
- `Gare d'arrivée`
- `Durée moyenne du trajet`
- `Year`
- `Month`

Elles couvrent la dimension géographique, la saisonnalité et le type de service