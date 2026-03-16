from task00 import make_dataframe

def get_towns(df, department: str | None = None) -> list[dict]:

    if department is not None:
        df_filtered = df[df['Code INSEE du département'].astype(str) == str(department)]
        if df_filtered.empty:
            return []
    else:
        df_filtered = df  
    towns = df_filtered[['Nom de la commune', 'Code INSEE de la commune']].drop_duplicates()
    
    result = [
        {"name": row['Nom de la commune'], "insee_code": str(row['Code INSEE de la commune'])}
        for _, row in towns.iterrows()
    ]
    
    return sorted(result, key=lambda x: x['insee_code'])
