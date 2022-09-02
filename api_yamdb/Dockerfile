FROM python:3.7-slim

WORKDIR /app

COPY api_yamdb/ .

RUN pip3 install -r requirements.txt --no-cache-dir

ENTRYPOINT ["bash", "docker-entrypoint.sh"]
