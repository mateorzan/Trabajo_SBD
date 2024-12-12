import requests
import pymongo
import time
from datetime import datetime, timezone

# Configuración da conexión á base de datos MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bicicoruña"]
collection = db["Estaciones"]

# Función para obter datos da API
def obtener_datos_api():
    url = "http://api.citybik.es/v2/networks/bicicorunha"  # Substitúe por a URL real da API
    response = requests.get(url)
    if response.status_code == 200:
        try:
            datos = response.json()
            return datos['network']['stations'] # Retorna os datos en formato JSON
        except ValueError:
            print("Erro ao parsear os datos JSON.")
            return None
    else:
        print("Error ao obter datos da API")
        return None

# Función para almacenar datos na base de datos
def almacenar_datos_mongodb(datos):
    if datos:
        if isinstance(datos, list):  # Comproba se os datos son unha lista
            for dato in datos:
                if isinstance(dato, dict):  # Comproba se cada item é un diccionario
                    dato['timestamp'] = datetime.now(timezone.utc) # Asigna o timestamp
                    collection.insert_one(dato)
            print("Datos almacenados correctamente.")
        else:
            print("Os datos non están no formato esperado.")
    else:
        print("Non se almacenaron datos.")

# Función principal para executar o script a intervalos regulares

while True:
    datos = obtener_datos_api()
    almacenar_datos_mongodb(datos)
    time.sleep(1 * 60)  # Dorme durante o intervalo (en segundos)

# Comezar a execución do script



