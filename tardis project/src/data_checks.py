import re
from pathlib import Path
import pandas as pd

"""
Vérifications simples sur le dataset nettoyé
But :
- Charger cleaned_dataset.csv
- Vérifier des règles "logiques" (Date propre, types numériques, pas de négatifs, Year/Month)
- Si une règle est cassée : on affiche l'erreur et on stop (exit code 1)
- Sinon : on affiche un résumé et on sort (exit code 0)
"""

CLEAN_PATH = Path("cleaned_dataset.csv")

DATE_COL = "Date"
YEAR_COL = "Year"
MONTH_COL = "Month"

ROUTE_COLS = ["Date", "Service", "Departure station", "Gare d'arrivée"]

COUNT_COLS = [
    "Nombre de circulations prévues",
    "Nombre de trains annulés",
    "Nombre de trains en retard au départ",
    "Nombre de trains en retard à l'arrivée",
    "Nombre trains en retard > 15min",
    "Nombre trains en retard > 30min",
    "Nombre trains en retard > 60min",
]

DELAY_COLS = [
    "Durée moyenne du trajet",
    "Retard moyen des trains en retard au départ",
    "Retard moyen de tous les trains au départ",
    "Retard moyen des trains en retard à l'arrivée",
    "Retard moyen de tous les trains à l'arrivée",
    "Retard moyen trains en retard > 15 (si liaison concurrencée par vol)",
]

TEXT_COLS = [
    "Commentaire annulations",
    "Commentaire retards au départ",
    "Commentaire retards à l'arrivée",
]

def fail(msg: str):
    print(f"ERROR: {msg}")
    raise SystemExit(1)

def warn(msg: str):
    print(f"WARNING: {msg}")

def load_data() -> pd.DataFrame:
    """Charge le CSV nettoyé"""
    if not CLEAN_PATH.exists():
        fail(f"File not found: {CLEAN_PATH}")

    df = pd.read_csv(CLEAN_PATH)
    print(f"Loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def require_columns(df: pd.DataFrame, cols: list[str], context: str):
    """Vérifie que des colonnes existent"""
    missing = [c for c in cols if c not in df.columns]
    if missing:
        fail(f"{context} - missing column(s): {missing}")

def check_date_not_missing(df: pd.DataFrame):
    """Date ne doit pas contenir de valeurs manquantes"""
    require_columns(df, [DATE_COL], "Date check")
    missing = int(df[DATE_COL].isna().sum())
    if missing != 0:
        fail(f"Missing values in '{DATE_COL}': {missing}")
    print("Date column: no missing values")

def check_date_format(df: pd.DataFrame):
    """Date doit être au format YYYY-MM-DD"""
    require_columns(df, [DATE_COL], "Date format check")

    s = df[DATE_COL].astype(str)
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    bad = int((~s.str.match(pattern)).sum())

    if bad != 0:
        sample = s[~s.str.match(pattern)].head(5).tolist()
        fail(f"Invalid date format (expected YYYY-MM-DD). Bad rows: {bad}. Examples: {sample}")

    print("Date format: YYYY-MM-DD")


def check_year_month(df: pd.DataFrame):
    """Year et Month doivent correspondre à Date"""
    require_columns(df, [DATE_COL, YEAR_COL, MONTH_COL], "Feature engineering check")

    dt = pd.to_datetime(df[DATE_COL], errors="coerce")
    bad_dt = int(dt.isna().sum())
    if bad_dt != 0:
        fail(f"Some Date values are not parseable as datetime: {bad_dt}")

    year = pd.to_numeric(df[YEAR_COL], errors="coerce")
    month = pd.to_numeric(df[MONTH_COL], errors="coerce")

    if year.isna().sum() != 0 or month.isna().sum() != 0:
        fail("Year/Month contains non-numeric values")

    if not (year == dt.dt.year).all():
        fail("Year values do not match Date year")
    if not (month == dt.dt.month).all():
        fail("Month values do not match Date month")

    print("Year/Month: consistent with Date")


def check_numeric_convertible(df: pd.DataFrame):
    """Les colonnes numériques doivent être convertibles en nombres"""
    problems = []
    for col in COUNT_COLS + DELAY_COLS:
        if col not in df.columns:
            continue

        original_non_null = int(df[col].notna().sum())
        coerced = pd.to_numeric(df[col], errors="coerce")
        coerced_non_null = int(coerced.notna().sum())

        if original_non_null > 0 and coerced_non_null == 0:
            problems.append(col)

    if problems:
        fail(f"Some columns are not numeric-convertible: {problems}")

    print("Numeric columns: convertible")

def check_no_negative_counts(df: pd.DataFrame):
    """Les colonnes de compteurs ne doivent pas être négatives."""
    bad = {}
    for col in COUNT_COLS:
        if col not in df.columns:
            continue
        s = pd.to_numeric(df[col], errors="coerce")
        neg = int((s.dropna() < 0).sum())
        if neg > 0:
            bad[col] = neg

    if bad:
        fail(f"Negative values found in count columns: {bad}")

    print("Count columns: no negative values")


def check_no_negative_delays(df: pd.DataFrame):
    """Les colonnes de durée/retards ne doivent pas être négatives"""
    bad = {}
    for col in DELAY_COLS:
        if col not in df.columns:
            continue
        s = pd.to_numeric(df[col], errors="coerce")
        neg = int((s.dropna() < 0).sum())
        if neg > 0:
            bad[col] = neg

    if bad:
        fail(f"Negative values found in delay columns: {bad}")

    print("Delay columns: no negative values")


def check_textual_fake_na(df: pd.DataFrame):
    """Les colonnes texte ne doivent pas contenir 'nan', 'null', 'none' comme texte"""
    pattern = re.compile(r"^\s*(nan|null|none|na|n/a)\s*$", re.IGNORECASE)
    bad = {}

    for col in TEXT_COLS:
        if col not in df.columns:
            continue
        s = df[col].dropna().astype(str)
        cnt = int(s.str.match(pattern).sum())
        if cnt > 0:
            bad[col] = cnt

    if bad:
        fail(f"Text columns contain textual missing markers (nan/null/none...): {bad}")

    print("Text columns: no textual fake NA")


def check_route_duplicates(df: pd.DataFrame):
    """Pas de doublons sur (Date, Service, Gare départ, Gare arrivée)"""
    require_columns(df, ROUTE_COLS, "Route duplicate check")
    dup = int(df.duplicated(subset=ROUTE_COLS).sum())
    if dup != 0:
        fail(f"Duplicate routes found based on {ROUTE_COLS}: {dup}")
    print("Routes: no duplicates")

def check_text_column_handling() -> str:
    """
    Check demandé par la mouli
    Objectif : vérifier que les colonnes texte ne contiennent pas des faux NA ("nan", "null", "none"...)
    et renvoyer "OK" si c'est bon.
    """
    df = load_data()
    check_textual_fake_na(df)
    return "OK"

def main():
    """Point d'entrée."""
    df = load_data()

    check_date_not_missing(df)
    check_date_format(df)
    check_year_month(df)
    check_numeric_convertible(df)
    check_no_negative_counts(df)
    check_no_negative_delays(df)
    check_textual_fake_na(df)
    check_route_duplicates(df)

    print("All checks passed.")
    return 0


if __name__ == "__main__":
    import sys

    if "--check-text" in sys.argv:
        try:
            print(check_text_column_handling())
            raise SystemExit(0)
        except SystemExit as e:
            raise
        except Exception:
            print("KO")
            raise SystemExit(1)

    raise SystemExit(main())