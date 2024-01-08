FROM python:3.9.18-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python", "main.py"]
CMD []

