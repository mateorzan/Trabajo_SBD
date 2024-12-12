import pymongo
import pandas as pd

# Configuración da conexión á base de datos MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["bicicoruña"]
collection = db["Estaciones"]

# Función para ler os datos de MongoDB
def ler_datos_mongodb():
    documentos = collection.find()
    return documentos

# Función para exportar os datos a CSV e Parquet
def exportar_datos(datos):
    # Crear un DataFrame de pandas cos datos
    df = pd.DataFrame(datos)
    
    # Filtrar os campos que se desexan exportar
    campos_desejados = ["_id", "name", "timestamp", "free_bikes", "empty_slots", "uid", "last_updated", "slots", "normal_bikes", "ebikes"]
    df_filtrado = df[campos_desejados]
    
    # Exportar a CSV
    df_filtrado.to_csv("datos_exportados.csv", index=False)
    print("Datos exportados a CSV.")
    
    # Exportar a Parquet
    df_filtrado.to_parquet("datos_exportados.parquet", index=False)
    print("Datos exportados a Parquet.")

# Función principal para executar o script
def ejecutar_script():
    # Ler os datos de MongoDB
    documentos = ler_datos_mongodb()
    
    # Convertir os documentos a lista de diccionarios
    datos = list(documentos)
    
    # Exportar os datos
    exportar_datos(datos)

# Executar o script
if __name__ == "__main__":
    ejecutar_script()  # Executa cando se chame o script
