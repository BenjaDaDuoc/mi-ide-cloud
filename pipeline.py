import pandas as pd
import time

from ingestion.lectura_csv import leer_datos_csv

def run_orchestator():
    almacen_datos = {}
    print("-- Lectura de csv")
    almacen_datos['Titanic']=leer_datos_csv()
    
    return almacen_datos