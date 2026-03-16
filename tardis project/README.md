# DASHBOARD_GUIDE 
python3 -m venv .venv
source .venv/bin/activate
## Installation
pip install -r requirements.txt

## Entraîner le modèle
python -m src.train

## Lancer le dashboard
streamlit run tardis_dashboard.py --server.headless true

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


# Model report : Tardis 
## 1) Objectif :
Notre objectif est de construire un modèle de regression capable de prédire la durée des retards, en minutes, à partir des données d'un dataset de la SNCF, puis l'intégrer dans l'interface Streamlit .

## 2) Données utilisées :
**Source**: './cleaned_dataset.csv' 
**Période**: années de 2018 à 2025 ( dans colonne `Year`)
- Variables principales : 
- `Service`, `Gare de départ`, `Gare d'arrivée`
- `Durée moyenne du trajet`
- `Year`, `Month`
Cible : `Retard moyen de tous les trains à l'arrivée`

## 3) Cible (y): 
**`Retard moyen de tous les trains à l'arrivée`**
Interprétation : retard moyen à l'arrivée, en minutes . 

## 4) Features (X) retenues 
Pour garantir une prédiction utilisable dans l'interface, nous avons choisi un sous-ensemble de variables facilement choisissables par un utilisateur :
`Service`
`Gare de départ`
`Gare d'arrivée`
`Durée moyenne du trajet`
`Year`
`Month`
- Justification : 
Ces features couvrent la dimension "type de service" , "géographie" , "longueur du trajet" , "saisonnalité" . Ainsi , la prédiction est cohérente dans streamlit . 

## 5) Pipeline de prétraitement :
Pipeline scikit-learn utilisé afin d'appliquer le même traitement en entrainement et en prédiction  
- Imputation médiane 
- Standardisation (`StandardScaler`)
- imputationd de la modalité la plus fréquente 
- encodage One-hot 

## 6) Modèle testés 
### Baseline
-Baseline : prédire la moyenne de `y_train` pour tout le testset . 
### Modèle principal 
`RandomForestRegressor`
 
## 7) Evaluation : 
- Split : train/test 80/20, `random_state=42`
- Métriques : MAE, RMSE, R²
**Résultats obtenus :**
- **Baseline** : MAE = **2.991** | RMSE = **4.392** | R² = **0.000**
- **RandomForest** : MAE = **2.067** | RMSE = **4.293** | R² = **0.045** 
**Lecture des résultats**: 
- *Par rapport à une baseline qui prédit simplement le retard moyen, notre RandomForest réduit l'erreur moyenne d'environ 31%, ce qui montre qu'il apprend des patterns liés au service, aux gares et au saisonnalité.*
- *Le R² reste faible : avec un formulaire volontairement léger pour streamlit , on privilégie l'utilisabilité, mais on perd une partie de l'information explicative contenue dans les variables opérationnelles (trafic, annulations ...)*

## 8) Export et intégration :
- Modèle exporté en `joblib`: `model.joblib`
- Streamlit charge le modèle et appelle `predict()` sur une ligne contenant les colonnes attendues 

## 9) Limites et améliorations :
- Ajouter des variables plus explicatives, commes les annulations ou les causes du retard, qui améliorerait probablement la performance mais qui nécessiterait un formulaire plus complexe 


============================================================
Shape: 11896 rows × 28 columns
============================================================

Column   : Date
Type     : str
Missing  : 380 (3.2%)
Unique   : 96

Column   : Service
Type     : str
Missing  : 240 (2.0%)
Unique   : 2

Column   : Gare de départ
Type     : str
Missing  : 59 (0.5%)
Unique   : 132

Column   : Gare d'arrivée
Type     : str
Missing  : 59 (0.5%)
Unique   : 116

Column   : Durée moyenne du trajet
Type     : float64
Missing  : 368 (3.1%)
Unique   : 495
Min      : 0.0
Max      : 786.0
Mean     : 170.98

Column   : Nombre de circulations prévues
Type     : float64
Missing  : 263 (2.2%)
Unique   : 881
Min      : 0.0
Max      : 1100.0
Mean     : 270.87

Column   : Nombre de trains annulés
Type     : float64
Missing  : 264 (2.2%)
Unique   : 191
Min      : 0.0
Max      : 288.0
Mean     : 8.63

Column   : Commentaire annulations
Type     : str
Missing  : 11324 (95.2%)
Unique   : 3

Column   : Nombre de trains en retard au départ
Type     : float64
Missing  : 258 (2.2%)
Unique   : 465
Min      : 0.0
Max      : 1066.0
Mean     : 86.97

Column   : Retard moyen des trains en retard au départ
Type     : float64
Missing  : 357 (3.0%)
Unique   : 11047
Min      : 0.0
Max      : 316.188
Mean     : 12.31

Column   : Retard moyen de tous les trains au départ
Type     : float64
Missing  : 354 (3.0%)
Unique   : 11296
Min      : -229.2694444
Max      : 115.04738956
Mean     : 3.14

Column   : Commentaire retards au départ
Type     : str
Missing  : 11299 (95.0%)
Unique   : 3

Column   : Nombre de trains en retard à l'arrivée
Type     : float64
Missing  : 264 (2.2%)
Unique   : 201
Min      : 0.0
Max      : 376.0
Mean     : 37.34

Column   : Retard moyen des trains en retard à l'arrivée
Type     : float64
Missing  : 350 (2.9%)
Unique   : 11034
Min      : -40.10925926
Max      : 299.6
Mean     : 35.19

Column   : Retard moyen de tous les trains à l'arrivée
Type     : float64
Missing  : 363 (3.1%)
Unique   : 11279
Min      : -472.6388889
Max      : 92.0
Mean     : 6.05

Column   : Commentaire retards à l'arrivée
Type     : str
Missing  : 10778 (90.6%)
Unique   : 276

Column   : Nombre trains en retard > 15min
Type     : float64
Missing  : 264 (2.2%)
Unique   : 158
Min      : 0.0
Max      : 312.0
Mean     : 26.84

Column   : Retard moyen trains en retard > 15 (si liaison concurrencée par vol)
Type     : float64
Missing  : 335 (2.8%)
Unique   : 10974
Min      : -2.714285714
Max      : 299.6
Mean     : 36.18

Column   : Nombre trains en retard > 30min
Type     : float64
Missing  : 259 (2.2%)
Unique   : 103
Min      : -44.0
Max      : 202.0
Mean     : 12.49

Column   : Nombre trains en retard > 60min
Type     : float64
Missing  : 264 (2.2%)
Unique   : 53
Min      : 0.0
Max      : 71.0
Mean     : 5.14

Column   : Prct retard pour causes externes
Type     : float64
Missing  : 351 (3.0%)
Unique   : 2629
Min      : 0.0
Max      : 100.0
Mean     : 21.52

Column   : Prct retard pour cause infrastructure
Type     : float64
Missing  : 343 (2.9%)
Unique   : 2495
Min      : 0.0
Max      : 100.0
Mean     : 21.88

Column   : Prct retard pour cause gestion trafic
Type     : float64
Missing  : 347 (2.9%)
Unique   : 2575
Min      : 0.0
Max      : 100.0
Mean     : 20.34

Column   : Prct retard pour cause matériel roulant
Type     : float64
Missing  : 344 (2.9%)
Unique   : 2448
Min      : 0.0
Max      : 100.0
Mean     : 18.91

Column   : Prct retard pour cause gestion en gare et réutilisation de matériel
Type     : float64
Missing  : 367 (3.1%)
Unique   : 2038
Min      : 0.0
Max      : 100.0
Mean     : 7.39

Column   : Prct retard pour cause prise en compte voyageurs (affluence, gestions PSH, correspondances)
Type     : float64
Missing  : 350 (2.9%)
Unique   : 2089
Min      : 0.0
Max      : 100.0
Mean     : 7.61

Column   : Year
Type     : float64
Missing  : 380 (3.2%)
Unique   : 8
Min      : 2018.0
Max      : 2025.0
Mean     : 2021.48

Column   : Month
Type     : float64
Missing  : 380 (3.2%)
Unique   : 12
Min      : 1.0
Max      : 12.0
Mean     : 6.51