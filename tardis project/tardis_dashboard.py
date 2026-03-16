from __future__ import annotations

#imports Streamlit 
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

#Imports standards
import joblib
import pandas as pd
import plotly.express as px
import streamlit as st

# Imports projet 
from src.config import DATA_PATH, MODEL_PATH, TARGET_COL
from src.preprocessing import load_clean_dataset


@st.cache_data
def load_data() -> pd.DataFrame:
    return load_clean_dataset(DATA_PATH)


@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        return None


st.set_page_config(page_title="TARDIS", layout="wide")
st.title("TARDIS — Retards SNCF (Analyse + Prédiction)")

df = load_data()
model = load_model()

tabs = st.tabs(["Vue d'ensemble", "Explorer", "Prédire"])

# TAB 1 : Overview
with tabs[0]:
    st.subheader("Vue d'ensemble")
    c1, c2, c3 = st.columns(3)

    if TARGET_COL in df.columns:
        c1.metric("Retard moyen (arrivée)", f"{df[TARGET_COL].mean():.2f} min")

    if "Nombre de trains annulés" in df.columns:
        c2.metric("Annulations moyennes", f"{df['Nombre de trains annulés'].mean():.2f}")

    c3.metric("Nombre de lignes", f"{len(df)}")

    if TARGET_COL in df.columns:
        fig = px.histogram(df, x=TARGET_COL, nbins=40, title="Distribution des retards (arrivée)")
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df.head(20), use_container_width=True)

# TAB 2 : Explore
with tabs[1]:
    st.subheader("Explorer")
    tmp = df.copy()

    #  colonnes (FR/EN)
    DEP_COL = "Gare de départ" if "Gare de départ" in tmp.columns else "Departure station"
    ARR_COL = "Gare d'arrivée" if "Gare d'arrivée" in tmp.columns else "Arrival station"

    # Filtres simples
    col1, col2, col3 = st.columns(3)

    if "Service" in tmp.columns:
        services = ["(Tous)"] + sorted(tmp["Service"].dropna().unique().tolist())
        service = col1.selectbox("Service", services)
        if service != "(Tous)":
            tmp = tmp[tmp["Service"] == service]

    if DEP_COL in tmp.columns:
        deps = ["(Toutes)"] + sorted(tmp[DEP_COL].dropna().unique().tolist())
        dep = col2.selectbox("Gare de départ", deps)
        if dep != "(Toutes)":
            tmp = tmp[tmp[DEP_COL] == dep]

    if ARR_COL in tmp.columns:
        arrs = ["(Toutes)"] + sorted(tmp[ARR_COL].dropna().unique().tolist())
        arr = col3.selectbox("Gare d'arrivée", arrs)
        if arr != "(Toutes)":
            tmp = tmp[tmp[ARR_COL] == arr]

    st.write(f"Lignes après filtre : **{len(tmp)}**")

    if TARGET_COL in tmp.columns and "Month" in tmp.columns:
        grp = tmp.groupby("Month", as_index=False)[TARGET_COL].mean()
        fig2 = px.line(grp, x="Month", y=TARGET_COL, markers=True, title="Retard moyen par mois")
        st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(tmp.head(100), use_container_width=True)

# TAB 3 : Predict
with tabs[2]:
    st.subheader("Prédire un retard")
    st.caption("Sélectionne des valeurs existantes dans le dataset pour prédire un retard")

    if model is None:
        st.warning("Modèle non trouvé, lance : `python -m src.train`")
    else:
        st.success("Modèle chargé avec succès ")

        #colonnes (FR/EN) 
        DEP_COL = "Gare de départ" if "Gare de départ" in df.columns else "Departure station"
        ARR_COL = "Gare d'arrivée" if "Gare d'arrivée" in df.columns else "Arrival station"

        #Listes de choix
        services = sorted(df["Service"].dropna().unique().tolist()) if "Service" in df.columns else []
        deps = sorted(df[DEP_COL].dropna().unique().tolist()) if DEP_COL in df.columns else []
        arrs = sorted(df[ARR_COL].dropna().unique().tolist()) if ARR_COL in df.columns else []

        years = sorted(df["Year"].dropna().astype(int).unique().tolist()) if "Year" in df.columns else []
        months = (
            sorted(df["Month"].dropna().astype(int).unique().tolist())
            if "Month" in df.columns
            else list(range(1, 13))
        )

        # Valeurs par défaut
        default_year_idx = len(years) - 1 if years else 0
        default_month_idx = months.index(6) if 6 in months else 0

        #Formulaire
        with st.form("predict_form"):
            service = st.selectbox("Service", services, index=0) if services else st.text_input("Service", value="National")
            dep = st.selectbox("Gare de départ", deps, index=0) if deps else st.text_input("Gare de départ", value="PARIS MONTPARNASSE")
            arr = st.selectbox("Gare d'arrivée", arrs, index=0) if arrs else st.text_input("Gare d'arrivée", value="BORDEAUX ST JEAN")

            duree = st.number_input("Durée prévue du trajet (en minutes)", min_value=0.0, value=120.0)

            year = st.selectbox("Year", years, index=default_year_idx) if years else st.number_input("Year", min_value=2000, value=2023)
            month = st.selectbox("Month", months, index=default_month_idx) if months else st.number_input("Month", min_value=1, max_value=12, value=6)

            submitted = st.form_submit_button("Prédire")

        if submitted:

            expected = list(getattr(model, "feature_names_in_", []))

            if "Departure station" in expected:
                # Modèle colonnes EN
                row = pd.DataFrame([{
                    "Service": service,
                    "Departure station": dep,
                    "Arrival station": arr,
                    "Durée moyenne du trajet": duree,
                    "Year": int(year),
                    "Month": int(month),
                }])
            else:
                # Modèle c colonnes FR 
                row = pd.DataFrame([{
                    "Service": service,
                    "Gare de départ": dep,
                    "Gare d'arrivée": arr,
                    "Durée moyenne du trajet": duree,
                    "Year": int(year),
                    "Month": int(month),
                }])

            pred = float(model.predict(row)[0])
            st.metric("Retard estimé (arrivée)", f"{pred:.2f} min")
                