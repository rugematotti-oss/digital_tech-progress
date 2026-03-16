import pandas as pd

def get_monthly_activity(
    df,
    department: str | None = None,
    mutation_type: str | None = None,
):
    df_clean = df.copy()
    df_clean['Date de la mutation'] = pd.to_datetime(
        df_clean['Date de la mutation'], 
        errors='coerce'
    )
    df_clean = df_clean.dropna(subset=['Date de la mutation', 'Valeur foncière'])
    df_clean['Valeur foncière'] = df_clean['Valeur foncière'].astype(float)
    df_clean['year'] = df_clean['Date de la mutation'].dt.year
    df_clean['month'] = df_clean['Date de la mutation'].dt.month

    if department is not None:
        df_clean = df_clean[df_clean['Code INSEE du département'].astype(str) == str(department)]
    if mutation_type is not None:
        df_clean = df_clean[df_clean['Nature de la mutation'] == mutation_type]

    grouped = df_clean.groupby(['year', 'month'])['Valeur foncière'].agg(
        transactions='count',
        average_price='mean',
        total_value='sum'
    ).reset_index()

    grouped = grouped.sort_values(['year', 'month'])

    result = []
    for _, row in grouped.iterrows():
        result.append({
            "year": int(row['year']),
            "month": int(row['month']),
            "transactions": int(row['transactions']),
            "average_price": round(float(row['average_price']), 2),
            "total_value": round(float(row['total_value']), 2)
        })
    
    return result