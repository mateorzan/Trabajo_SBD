import pymongo
import pandas as pd

# Configuración de la conexión a MongoDB Atlas
uri = "mongodb+srv://admin:admin@cluster0.j3yin.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri)
db = client["bicicoruña"]
collection = db["Estaciones"]

# Función para leer los datos de MongoDB
def leer_datos_mongodb():
    documentos = collection.find()
    return documentos

# Función para limpiar y transformar los datos
def procesar_datos(datos):
    # Crear un DataFrame con los datos
    df = pd.DataFrame(datos)

    # Extraer los campos de "extra" para cada fila
    if "extra" in df.columns:
        extra_df = df["extra"].apply(pd.Series)  # Esto crea un DataFrame de los campos de "extra"
        df = pd.concat([df, extra_df], axis=1)  # Concatenar los campos de "extra" al DataFrame principal

    # Campos deseados
    campos_deseados = [
        "id", "name", "timestamp", 
        "free_bikes", "empty_slots", "uid", "last_updated", "slots", "normal_bikes", 
        "ebikes"
    ]

    # Filtrar el DataFrame para mantener solo los campos deseados
    df = df[campos_deseados]

    # Convertir el campo "timestamp" a un formato compatible
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

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

    # Convertir los documentos a una lista de diccionarios
    datos = list(documentos)

    # Procesar y limpiar los datos
    df = procesar_datos(datos)

    # Exportar los datos
    exportar_datos(df)

# Ejecutar el script
ejecutar_script()

