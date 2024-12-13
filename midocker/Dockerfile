FROM python

WORKDIR /app
COPY script1_v2.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./script1_v2.py"]
