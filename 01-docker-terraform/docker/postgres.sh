docker run -it \
    --network pg-network \
    --name pg-database \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 1111:5432 \
    postgres:13


