# Trabajo_SBD

# Proyecto Trabajo_SBD

Bienvenido al repositorio **Trabajo_SBD**. Este proyecto contiene scripts, configuraciones Docker, archivos de datos y notebooks enfocados en la manipulación y análisis de datos.

---

## 📁 Estructura del Proyecto

```plaintext
.
├── midocker/                   # Carpeta principal para Docker y procesamiento.
│   ├── Dockerfile              # Configuración base para la imagen Docker.
│   ├── datos_exportados.csv    # Datos exportados en formato CSV.
│   ├── datos_exportados.parquet# Datos exportados en formato Parquet.
│   ├── requirements.txt        # Dependencias de Python.
│   ├── script1_v3.py           # Script principal que se ejecuta en bucle.
│   └── script2.py              # Script secundario que carga los datos.
│
├── LICENSE                     # Licencia del proyecto.
├── notebook1.ipynb             # Notebook 1 
└── notebook2.ipynb             # Notebook 2 
```

## 🚀 Instalación y Configuración

### ✅ 1. Requisitos previos

Asegúrate de tener instalados los siguientes elementos en tu sistema:

- **Python 3.8+**
- **Docker **
- **Jupyter Notebook / Jupyter Lab**
- **Git**

### 🪞 2. Clona este repositorio

Clona el repositorio localmente con:

```bash
git clone https://github.com/tu_usuario/mateorzan.git
cd mateorzan
```

### ⚙️ 3. Configura y ejecuta Docker a nivel local.

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

## 👣 Pasos que se siguieron

### 1.Creamos y clonamos el repositorio de GitHub

### 2.Creamos entorno de ejecucion Trabajo_SBD

Cree una carpeta para organizar el trabajo ahi.

```bash
mkdir Trabajo_SBD
cd Trabajo_SBD
```

Cree un enviroment.

```bash
conda create -n Trabajo_SBD
conda activate Trabajo_SBD
```

### 3.Creamos notebooks previos para probar el funcionamiento del codigo

Para esto utilice Visual Studio code conectado a mi entorno WSL para crear los archivos

### 4.Creamos Scripts

Una vez probado los archivos con los notebooks traslade estos codigos a dos archivos

    1.script1_v3.py
    2.script2.py

### 5.Dockerizamos el script1

A traves del archivo Dockerfile, ejecutamos el siguiente comando para crear la imagen.

```bash
docker build -t mateorzan/midocker_mateo .
```

### 6.Probamos funcionamiento a nivel local

Ejecucion de dockers,mongo y script. Comandos:

```bash
docker run -d --name mongo --network Trabajo_SBD -p 27017:27017 mongo:latest
```

```bash
docker run -d --name mi_script --network Trabajo_SBD -p 5000:5000 --env MONGO_URI=mongodb://mongo:27017 mateorzan/midocker_mateo
```

### 7.Subimos imagen a DockerHub

Creamos un tag para subir la imagen

```bash
docker tag mi_proyecto_app:latest tu_usuario/mi_repositorio_app:latest
```

Iniciamos sesion con nuestra cuenta y subimos la imagen

```bash
docker login
docker push miusuario/mi-imagen:latest
```

### 8.Creamos instancia en Openstack

Creamos la instancia en Openstack y nos conectamos a la maquina a traves de ssh

```bash
ssh -J usuario_hadoop@hadoop.cesga.es cesgaxuser@ip_máquina_virtual 
```

Obtenemos la imagen y ejecutamos a nivel local como hicimos anteriormente a ver si funciona

```
docker pull mateorzan/midocker_mateo
docker run -d --name mongo --network Trabajo_SBD -p 27017:27017 mongo:latest
docker run -d --name mi_script --network Trabajo_SBD -p 5000:5000 --env MONGO_URI=mongodb://mongo:27017 mateorzan/midocker_mateo

```

## ➕EXTRA
