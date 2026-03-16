def get_prices(
df,
department_code: str,
town_code: str,
r_min: int = 1,
r_max: int = 10,
s_min: float = 20.0,
s_max: float = 200.0
):
    required_col= [
        'Code INSEE du département',
        'Code INSEE de la commune',
        'Nombre de pièces principales',
        'Surface réelle du bâti',
        'Valeur foncière'
    ]

    df_clean= df.dropna(subset=required_col).copy()

    df_clean['Code INSEE du département'] = df_clean['Code INSEE du département'].astype(str)
    df_clean['Code INSEE de la commune'] = df_clean['Code INSEE de la commune'].astype(str)
    df_clean['Nombre de pièces principales'] = df_clean['Nombre de pièces principales'].astype(int)
    df_clean['Surface réelle du bâti'] = df_clean['Surface réelle du bâti'].astype(float)
    df_clean['Valeur foncière'] = df_clean['Valeur foncière'].astype(float)

    if town_code not in df_clean['Code INSEE de la commune'].values:
        pass
    else:
         df_clean = df_clean[df_clean['Code INSEE de la commune'] == town_code]
    df_clean = df_clean[
        (df_clean['Nombre de pièces principales'] >= r_min) &
        (df_clean['Nombre de pièces principales'] <= r_max)
    ]
    
    df_clean = df_clean[
        (df_clean['Surface réelle du bâti'] >= s_min) &
        (df_clean['Surface réelle du bâti'] <= s_max)
    ]
    prices = []
    for _, row in df_clean.iterrows():
        prices.append({
            "department_code": str(row['Code INSEE du département']),
            "town_code": str(row['Code INSEE de la commune']),
            "rooms": int(row['Nombre de pièces principales']),
            "surface": float(row['Surface réelle du bâti']),
            "price": float(row['Valeur foncière'])
        })
    
    return {"prices": prices}
