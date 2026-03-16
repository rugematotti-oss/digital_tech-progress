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