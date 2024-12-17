import pymongo
import time
from datetime import datetime, timezone
from nba_api.live.nba.endpoints import scoreboard
import json

print("Iniciando o script1_v3")
print("Esperando 10 segundos para que MongoDB arrinque...")
time.sleep(10)  # Tempo de espera para MongoDB

print("Intentando conectar á base de datos...")
try:
    client = pymongo.MongoClient("mongodb://mongo:27017/", serverSelectionTimeoutMS=5000)
    client.server_info()  # Forzar conexión para validar
    print("Conexión á base de datos exitosa!")
except Exception as e:
    print(f"Erro conectando á base de datos: {e}")
    exit(1)

# Funcións principais
def obtener_datos_api():
    print("Obteñendo datos da API...")
    # Today's Score Board
    games = scoreboard.ScoreBoard()
    # json
    print("Datos da API obtidos correctamente.")
    juegos = games.get_json()
    data = json.loads(juegos)
    return data['scoreboard']['games']

def almacenar_datos_mongodb(datos):
    print("Almacenando datos en MongoDB...")
    db = client["NBA"]
    collection = db["partidos"]
    if datos:
        for dato in datos:
            collection.insert_one(dato)
        print("Datos almacenados correctamente.")
    else:
        print("Non hai datos para almacenar.")

# Loop principal
while True:
    datos = obtener_datos_api()
    print(datos)
    almacenar_datos_mongodb(datos)
    print("Durmindo por 5 minutos...")
    time.sleep(300) # 12 horas 43200s
