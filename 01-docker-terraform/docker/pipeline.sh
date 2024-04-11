DATA_URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"
TIMES_URL="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"

docker run -it \
    --network pg-network \
    taxi_ingest:v1 \
        --port 5432 \
        --db postgres \
        --table green_taxi_data \
        --url ${DATA_URL} \
        --host pg-database

docker run -it \
    --network pg-network \
    taxi_ingest:v1 \
        --port 5432 \
        --db postgres \
        --table green_taxi_times \
        --url ${TIMES_URL} \
        --host pg-database
