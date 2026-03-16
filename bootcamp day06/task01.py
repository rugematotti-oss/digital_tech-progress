import pandas as pd
from task00 import make_dataframe
def get_departments(df) -> list[str]:
    departments= df['Code INSEE du département'].astype(str).dropna().unique().tolist()
    return sorted(departments)

