import pandas as pd
def make_dataframe(path: str):
 df= pd.read_csv(path, sep=';')
 df_DataFrame= df.dropna(subset=['Latitude','Longitude'])
 return df_DataFrame