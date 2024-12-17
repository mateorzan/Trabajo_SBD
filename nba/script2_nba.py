import pymongo
import pandas as pd

# Configuración de la conexión a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["NBA"]
collection = db["partidos"]

# Función para leer los datos de MongoDB
def leer_datos_mongodb():
    documentos = collection.find()
    return documentos

# Función para limpiar y transformar los datos
def procesar_datos(datos):
    # Crear un DataFrame con los datos
    df = pd.DataFrame(datos)
    print("Dataframe")

    # Lista de columnas que no deseas
    columnas_a_excluir = ["_id"]

    # Filtrar el DataFrame excluyendo las columnas no deseadas
    df = df.drop(columns=columnas_a_excluir, errors='ignore')  # 'errors="ignore"' evita errores si la columna no existe


    return df

# Función para exportar los datos a CSV y Parquet
def exportar_datos(df):
    # Exportar a CSV
    df.to_csv("datos_exportados.csv", index=False)
    print("Datos exportados a CSV.")

    # Exportar a Parquet
    df.to_parquet("datos_exportados.parquet", index=False)
    print("Datos exportados a Parquet.")

# Función principal
def ejecutar_script():
    # Leer los datos de MongoDB
    documentos = leer_datos_mongodb()
    print("Se leyeron los datos")
    # Convertir los documentos a una lista de diccionarios
    datos = list(documentos)
    print("Se covertieron los datos a una lista")
    # Procesar y limpiar los datos
    df = procesar_datos(datos)

    # Exportar los datos
    exportar_datos(df)

# Ejecutar el script
ejecutar_script()

