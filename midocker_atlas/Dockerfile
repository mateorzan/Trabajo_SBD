FROM python

WORKDIR /app

COPY script_atlas.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /app/script_atlas.py

# Ejecutar el script cuando el contenedor se inicie
ENTRYPOINT ["python", "script_atlas.py"]

