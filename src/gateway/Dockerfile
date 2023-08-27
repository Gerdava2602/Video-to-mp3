FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y --no-install-suggests \
    gcc \
    libpq-dev \
    && pip install --no-cache-dir --upgrade pip 

ENV JWT_SECRET=secret

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 8080
CMD ["python", "server.py"]