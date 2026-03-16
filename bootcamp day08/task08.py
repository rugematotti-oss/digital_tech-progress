from task01 import get_html
import pandas as pd
import matplotlib.pyplot as plt


def wiki_table_to_df(url: str):
    soup = get_html(url)
    
    table = soup.find('table', {'class': 'wikitable'})
    
    if not table:
        return pd.DataFrame()
    
    headers = []
    header_row = table.find('tr')
    if header_row:
        for th in header_row.find_all(['th', 'td']):
            headers.append(th.get_text().strip())
    rows = []
    for tr in table.find_all('tr')[1:]:  
        cells = []
        for td in tr.find_all(['td', 'th']):
            cells.append(td.get_text().strip())
        if cells:
            rows.append(cells)
    df = pd.DataFrame(rows, columns=headers if headers else None)
    if 'Rank' in df.columns:
        df = df.drop('Rank', axis=1)
    if 'rank' in df.columns:
        df = df.drop('rank', axis=1)
    
    return df


def wiki_chart(url: str, n: int = 5) -> None:

    if n <= 0:
        raise ValueError("n must be strictly positive")
    
    df = wiki_table_to_df(url)
    
    if df.empty:
        print("No data to plot")
        return None
    
    df_plot = df.head(n)
    
    if len(df_plot.columns) < 2:
        print("Not enough columns to plot")
        return None

    values_col = df_plot.iloc[:, 0] 
    labels_col = df_plot.iloc[:, 1]      
    values = pd.to_numeric(values_col.str.replace(',', ''), errors='coerce')
    labels = labels_col.tolist()
    
    plt.figure(figsize=(10, 6))
    plt.barh(labels, values)
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.title(f'Top {n} - {df.columns[1]} by {df.columns[0]}')
    plt.gca().invert_yaxis()  
    plt.tight_layout()
    filename = f"chart_{n}.png"
    plt.savefig(filename)
    print(f"Chart saved as {filename}")
    
    plt.show(block=True)
    return None