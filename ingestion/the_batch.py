import pandas as pd
import requests

def leer_datos_batch(subject='cooking'):
    url = f"https://openlibrary.org/subjects/{subject}.json?limit=50"
    response = requests.get(url)
    data = response.json()
    df_libreria = pd.json_normalize(data['works'])
    df_libreria = df_libreria[['title', 'key', 'first_publish_year']]
    print(f"Batch pulled {len(df_libreria)} book records.")
    
    

    return df_libreria

