import pandas as pd


def load_raw(path: str = "data/project_dataset.csv") -> pd.DataFrame:
    """Load the raw dataset."""
    return pd.read_csv(path, sep=";")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates and convert columns to appropriate types."""

    # Remove duplicates
    df = df.drop_duplicates().copy()

    # Date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Categorical
    categorical_cols = [
        "Service",
        "Gare de départ",
        "Gare d'arrivée",
        "Commentaire annulations",
        "Commentaire retards au départ",
        "Commentaire retards à l'arrivée",
    ]
    for col in categorical_cols:
        df[col] = df[col].astype("category")

    # Integer
    int_cols = [
        "Nombre de circulations prévues",
        "Nombre de trains annulés",
        "Nombre de trains en retard au départ",
        "Nombre de trains en retard à l'arrivée",
        "Nombre trains en retard > 15min",
        "Nombre trains en retard > 30min",
        "Nombre trains en retard > 60min",
    ]
    for col in int_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    # Float
    float_cols = [
        "Durée moyenne du trajet",
        "Retard moyen des trains en retard au départ",
        "Retard moyen de tous les trains au départ",
        "Retard moyen des trains en retard à l'arrivée",
        "Retard moyen de tous les trains à l'arrivée",
        "Retard moyen trains en retard > 15 (si liaison concurrencée par vol)",
        "Prct retard pour causes externes",
        "Prct retard pour cause infrastructure",
        "Prct retard pour cause gestion trafic",
        "Prct retard pour cause matériel roulant",
        "Prct retard pour cause gestion en gare et réutilisation de matériel",
        "Prct retard pour cause prise en compte voyageurs (affluence, gestions PSH, correspondances)",
    ]
    for col in float_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create new features from existing columns."""

    # Extract date parts
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month

    return df


def save_clean(df: pd.DataFrame, path: str = "cleaned_dataset.csv"):
    """Save the cleaned dataset."""
    df.to_csv(path, index=False)
    print(f"save the cleaned dataset: {path}")


if __name__ == "__main__":
    df = load_raw()
    df = clean(df)
    df = engineer_features(df)
    save_clean(df)
