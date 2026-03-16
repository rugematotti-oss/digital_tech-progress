from __future__ import annotations

import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from src.config import DATA_PATH, MODEL_PATH, TARGET_COL
from src.preprocessing import build_pipeline, load_clean_dataset, make_X_y


def _baseline_predict(y_train: np.ndarray, n: int) -> np.ndarray:
    """Baseline simple : prédire la moyenne du train pour toutes les lignes du test."""
    return np.full(shape=n, fill_value=float(np.mean(y_train)))


def main() -> None:
    # DATA_PATH est un pathlib.Path -> on le convertit en str pour être compatible partout
    df = load_clean_dataset(str(DATA_PATH))
    X, y = make_X_y(df, TARGET_COL)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y.values, test_size=0.2, random_state=42
    )

    # Baseline
    y_base = _baseline_predict(y_train, len(y_test))

    # Modèle
    model = RandomForestRegressor(
        n_estimators=400,
        random_state=42,
        n_jobs=-1,
    )

    pipe = build_pipeline(X_train, model)
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    def report(name: str, y_true, y_hat) -> None:
        mae = mean_absolute_error(y_true, y_hat)
        rmse = mean_squared_error(y_true, y_hat) ** 0.5
        r2 = r2_score(y_true, y_hat)
        print(f"{name} | MAE={mae:.3f} | RMSE={rmse:.3f} | R2={r2:.3f}")

    report("BASELINE", y_test, y_base)
    report("RANDOM_FOREST", y_test, y_pred)

    # on convertit MODEL_PATH en str pour joblib
    joblib.dump(pipe, str(MODEL_PATH), compress=("xz", 3))
    print(f"Modèle exporté -> {MODEL_PATH}")


if __name__ == "__main__":
    main()
