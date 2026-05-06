import pandas as pd
import pipeline.py

df_titanic = pd.read_csv('Titanic.csv')
df_titanic.info()


resumen = (df_titanic.groupby("2urvived").size())

almacen_datos['resumen_titanic'] = resumen
print(almacen_datos['resumen_titanic'])