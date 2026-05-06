import pandas as pd
import time
from ingestion.lectura_csv import leer_datos_csv
from ingestion.fuente_realtime import leer_clima_tiempo_real
from ingestion.the_batch import leer_datos_batch

def run_orchestator():
    almacen_datos = {}
    print("-- Lectura de csv")
    almacen_datos['Titanic']=leer_datos_csv()
    almacen_datos['Libros']=leer_datos_batch()
    almacen_datos['Clima']=leer_clima_tiempo_real()
    return almacen_datos
    