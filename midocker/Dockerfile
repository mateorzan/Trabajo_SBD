FROM python

WORKDIR /app

COPY script1_v3.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /app/script1_v3.py

# Ejecutar el script cuando el contenedor se inicie
ENTRYPOINT ["python", "script1_v3.py"]

