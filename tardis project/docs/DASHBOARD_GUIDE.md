# DASHBOARD_GUIDE 
python3 -m venv .venv
source .venv/bin/activate
## Installation
pip install -r requirements.txt

## Entraîner le modèle
python -m src.train

## Lancer le dashboard
streamlit run tardis_dashboard.py --server.headless true