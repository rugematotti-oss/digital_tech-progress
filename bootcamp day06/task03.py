import pandas as pd
from task00 import make_dataframe 
def get_department_prices(df):
    avg_prices = df.groupby('Code INSEE du département')['Valeur foncière'].mean()
    result= {str(k): float(v)for k, v in avg_prices.items()}
    return dict(sorted(result.items()))
    