import pandas as pd

def leer_datos_csv():
    source = 'Titanic.csv'
    df = pd.read_csv(source)
    print(f"Total lineas importadas: {len(df)}")
    return df

    
