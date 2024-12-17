# Trabajo_SBD
# Proyecto Trabajo_SBD

Bienvenido al repositorio **Trabajo_SBD**. Este proyecto contiene scripts, configuraciones Docker, archivos de datos y notebooks enfocados en la manipulación y análisis de datos.

---

## 📁 Estructura del Proyecto

```plaintext
.
├── midocker/                   # Carpeta principal para Docker y procesamiento
│   ├── Dockerfile              # Configuración base para la imagen Docker
│   ├── datos_exportados.csv    # Datos exportados en formato CSV
│   ├── datos_exportados.parquet# Datos exportados en formato Parquet
│   ├── docker-compose.yml      # Orquestación de servicios Docker
│   ├── requirements.txt        # Dependencias de Python
│   ├── script1_v3.py           # Script principal versión 3
│   └── script2.py              # Script secundario
│
├── LICENSE                     # Licencia del proyecto
├── README.md                   # Documentación principal del proyecto
├── notebook1.ipynb             # Notebook 1 de análisis o procesamiento
└── notebook2.ipynb             # Notebook 2 de análisis adicional
```

## 🚀 Instalación y Configuración

### 1. Requisitos previos

Asegúrate de tener instalados los siguientes elementos en tu sistema:

- **Python 3.8+**
- **Docker y Docker Compose**
- **Jupyter Notebook / Jupyter Lab**
- **Git**

### 2. Clona este repositorio

Clona el repositorio localmente con:

```bash
git clone https://github.com/tu_usuario/mateorzan.git
cd mateorzan
```

### 3. Configura y ejecuta Docker a nivel local.

Configuracion
```bash
cd midocker
docker build -t mateorzan/midocker_mateo .
```
Crear una network
```bash
docker network create Trabajo_SBD
```
Ejecucion Mongo
```bash
docker run -d --name mongo --network Trabajo_SBD -p 27017:27017 mongo:latest
```

```bash
docker run -d --name mi_script --network Trabajo_SBD -p 5000:5000 --env MONGO_URI=mongodb://mongo:27017 mateorzan/midocker_mateo
```

## Pasos que se siguieron 

### 1.Creamos y clonamos el repositorio de GitHub

### 2.Creamos entorno de ejecucion Trabajo_SBD

### 3.Creamos notebooks previos para probar el funcionamiento del codigo

### 4.Creamos Scripts

### 5.Dockerizamos el script1 
A traves del archivo Dockerfile

### 6.Probamos funcionamiento a nivel local
Ejecucion de dockers,mongo y script

### 7.Subimos imagen a DockerHub
Comandos

### 8.Creamos instancia en Openstack

Creamos la instancia y nos conectamos a la maquina a traves de ssh, 
obtenemos la imagen y ejecutamos a nivel local como hicimos anteriormente a ver si funciona

