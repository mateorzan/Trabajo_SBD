import pymongo
import requests
import time
from datetime import datetime, timezone

print("Iniciando o script1_v3")
print("Esperando 10 segundos para que MongoDB arrinque...")
time.sleep(10)  # Tempo de espera para MongoDB

print("Intentando conectar á base de datos...")
try:
    client = pymongo.MongoClient("mongodb://mongodb:27017/", serverSelectionTimeoutMS=5000)
    client.server_info()  # Forzar conexión para validar
    print("Conexión á base de datos exitosa!")
except Exception as e:
    print(f"Erro conectando á base de datos: {e}")
    exit(1)

# Funcións principais
def obtener_datos_api():
    print("Obteñendo datos da API...")
    url = "http://api.citybik.es/v2/networks/bicicorunha"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Datos da API obtidos correctamente.")
            return response.json()['network']['stations']
        else:
            print(f"Erro ao obter datos da API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Erro ao conectar coa API: {e}")
        return None

def almacenar_datos_mongodb(datos):
    print("Almacenando datos en MongoDB...")
    db = client["bicicoruña"]
    collection = db["Estaciones"]
    if datos:
        for dato in datos:
            dato['timestamp'] = datetime.now(timezone.utc)
            collection.insert_one(dato)
        print("Datos almacenados correctamente.")
    else:
        print("Non hai datos para almacenar.")

# Loop principal
while True:
    datos = obtener_datos_api()
    almacenar_datos_mongodb(datos)
    print("Durmindo por 5 minutos...")
    time.sleep(300)
