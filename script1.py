#Hay que instalarlo pip3 install requests
import requests
#Hay que instalarlo pip3 install pymongo
import pymongo
import time

#URL de la API REST en formato JSON
URL_API='http://api.citybik.es/v2/networks/bicicorunha'

#URL base de datos
URL_MONGO="mongodb://localhost:27017/bicicoruña"

#En segundos
DURACION_INTERVALO=60

#Conexion a la base de datos
client = pymongo.MongoClient(URL_MONGO)

#test es la base de datos en la que se inserta
db = client.test

while True:
    hora_actual=time.time()

    #Peticion a la API
    r = requests.get(URL_API)

    data = r.json()
    print(data)
    data2 = data['network']['stations'] 
    db.Estaciones.insert_many(data2)
    #Pone el programa a dormir hasta el siguiente periodo
    #time.sleep(DURACION_INTERVALO-(time.time()-hora_actual))
