FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2 requests tqdm

WORKDIR /app

COPY main.py main.py

ENTRYPOINT [ "python3", "main.py" ]