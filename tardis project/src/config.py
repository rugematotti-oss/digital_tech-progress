from __future__ import annotations

# Chemins
DATA_PATH = "./cleaned_dataset.csv"
MODEL_PATH = "./model.joblib"

# Cible
TARGET_COL = "Retard moyen de tous les trains à l'arrivée"

# Features utilisées pour la prédiction
FEATURE_COLS = [
    "Service",
    "Gare de départ",
    "Gare d'arrivée",
    "Durée moyenne du trajet",
    "Year",
    "Month",
]

# Colonnes “texte long” à exclure des features
TEXT_COMMENT_COLS = [
    "Commentaire annulations",
    "Commentaire retards au départ",
    "Commentaire retards à l'arrivée",
]
