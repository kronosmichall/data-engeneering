URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

docker run -it \
    --network pg-network \
    taxi_ingest:v1 \
        --port 5432 \
        --db postgres \
        --table green_taxi_data \
        --url ${URL} \
        --host pg-database
