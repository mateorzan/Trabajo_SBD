import pymongo
import requests
import time
from datetime import datetime, timezone

print("Iniciando o script1_v3")
print("Esperando 10 segundos para iniciar conexión a MongoDB Atlas...")
time.sleep(10)  # Tiempo de espera inicial

print("Intentando conectar a la base de datos en MongoDB Atlas...")
try:
    # URI de conexión a MongoDB Atlas
    uri =  "mongodb+srv://admin:admin@cluster0.j3yin.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.server_info()  # Forzar conexión para validar
    print("¡Conexión a MongoDB Atlas exitosa!")
except Exception as e:
    print(f"Error conectando a la base de datos: {e}")
    exit(1)

# Funciones principales
def obtener_datos_api():
    print("Obteniendo datos de la API...")
    url = "http://api.citybik.es/v2/networks/bicicorunha"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Datos de la API obtenidos correctamente.")
            return response.json()['network']['stations']
        else:
            print(f"Error al obtener datos de la API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al conectar con la API: {e}")
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
        print("No hay datos para almacenar.")

# Bucle principal
while True:
    datos = obtener_datos_api()
    almacenar_datos_mongodb(datos)
    print("Durmiendo por 5 minutos...")
    time.sleep(300)
