import pandas as pd

def get_price_per_sqm_stats(
    df,
    department: str | None = None,
    property_type: str | None = None,
    min_surface: float | None = None,
    max_surface: float | None = None,
):
    df_clean = df.copy()

    df_clean['Code INSEE du département'] = df_clean['Code INSEE du département'].astype(str)

    df_clean['Valeur foncière'] = pd.to_numeric(df_clean['Valeur foncière'], errors='coerce')
    df_clean['Surface réelle du bâti'] = pd.to_numeric(df_clean['Surface réelle du bâti'], errors='coerce')
    
    df_clean = df_clean[df_clean['Valeur foncière'].notna() & (df_clean['Valeur foncière'] > 0)]
    df_clean = df_clean[df_clean['Surface réelle du bâti'].notna() & (df_clean['Surface réelle du bâti'] > 0)]

    df_clean['price_per_sqm'] = df_clean['Valeur foncière'] / df_clean['Surface réelle du bâti']
    if department is not None:
        df_clean = df_clean[df_clean['Code INSEE du département'] == str(department)]

    if property_type is not None:
        df_clean = df_clean[df_clean['Type de local'] == property_type]

    if min_surface is not None:
        df_clean = df_clean[df_clean['Surface réelle du bâti'] >= min_surface]
    if max_surface is not None:
        df_clean = df_clean[df_clean['Surface réelle du bâti'] <= max_surface]
    grouped = df_clean.groupby('Code INSEE du département')['price_per_sqm'].agg(
        count='count',
        avg_price_per_sqm='mean',
        median_price_per_sqm='median',
        min_price_per_sqm='min',
        max_price_per_sqm='max'
    ).reset_index()

    grouped = grouped.sort_values('Code INSEE du département', key=lambda x: x.astype(str))

    result = []
    for _, row in grouped.iterrows():
        result.append({
            "department": str(row['Code INSEE du département']),
            "count": int(row['count']),
            "avg_price_per_sqm": round(float(row['avg_price_per_sqm']), 2),
            "median_price_per_sqm": round(float(row['median_price_per_sqm']), 2),
            "min_price_per_sqm": round(float(row['min_price_per_sqm']), 2),
            "max_price_per_sqm": round(float(row['max_price_per_sqm']), 2)
        })
    
    return result
