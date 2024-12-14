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


### 3. Configura y ejecuta Docker

```bash
cd midocker
docker-compose up --build


