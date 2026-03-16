from __future__ import annotations

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import FEATURE_COLS, TARGET_COL


def load_clean_dataset(path: str) -> pd.DataFrame:
    """
    Charge le dataset nettoyé, conversion de la date en datetime et création d'une route départ/arrivée

    """
    df = pd.read_csv(path)

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    return df


def make_X_y(
    df: pd.DataFrame, target_col: str = TARGET_COL
) -> tuple[pd.DataFrame, pd.Series]:
    """
        Séparer les features (X) de la cible (y), retirer la colonne cible et les colonnes commentaires, et retirer les lignes
    )
    """
    if target_col not in df.columns:
        raise ValueError(f"Colonne cible introuvable: {target_col}")

    df = df.dropna(subset=[target_col]).copy()

    # Vérifie que toutes les colonnes nécessaires sont présentes
    missing = [c for c in FEATURE_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Colonnes features manquantes dans le dataset : {missing}")

    X = df[FEATURE_COLS].copy()
    y = df[target_col].astype(float)

    return X, y


def build_pipeline(X: pd.DataFrame, model) -> Pipeline:
    """
    Construire un pipeline scikit-learn propre, avec :
    des colonnes numériques qu'on remplit si valeurs manquaantes et on standardise
    des colonnes catégorielles qu'on remplit et OneHotEncode
    """
    num_cols = X.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = [c for c in X.columns if c not in num_cols]

    numeric = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    pre = ColumnTransformer(
        transformers=[
            ("num", numeric, num_cols),
            ("cat", categorical, cat_cols),
        ]
    )

    return Pipeline(steps=[("preprocess", pre), ("model", model)])
