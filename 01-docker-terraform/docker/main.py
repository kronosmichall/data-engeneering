import pandas as pd
import argparse
import requests
import gzip
import shutil
import os

from sqlalchemy import create_engine
from tqdm import tqdm

def download_file(url, file_name = ""):
    CHUNK_SIZE = 8192
    local_filename = file_name or url.split('/')[-1]

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc='CSV file downloading progress')

        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
                progress_bar.update(CHUNK_SIZE)
    return local_filename


def download_csv_gz(url, csv_name = ""):
    file_name = download_file(url)

    if file_name.endswith('.csv'): return file_name

    csv_name = file_name.split('.gz')[0]
    with gzip.open(file_name, 'rb') as f_in:
        with open(csv_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # unsafe
    os.remove(file_name)

    return csv_name

def main(params):
    CHUNK_SIZE = 100_000
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table = params.table
    url = params.url

    csv = download_csv_gz(url)
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    progress_bar = tqdm(desc="CSV chunks", unit='')

    for chunk in pd.read_csv(csv, header = 0, chunksize = CHUNK_SIZE):
        chunk.to_sql(name=table, con=engine, if_exists='append')
        progress_bar.update(1)

    count = f"""
    select count(*) from {table}
    """
    print(f"now {table} has {pd.read_sql(count, con=engine)} records")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV into postgres")

    parser.add_argument('--user', help='Postgres username', default='root')
    parser.add_argument('--password', help='Postgres password', default='root')
    parser.add_argument('--host', help='Postgres host', default='localhost')
    parser.add_argument('--port', help='Postgres port')
    parser.add_argument('--db', help='Postgres database name')
    parser.add_argument('--table', help='Postgres table name to create')
    parser.add_argument('--url', help="Url of CSV to ingest")

    args = parser.parse_args()

    main(args)
