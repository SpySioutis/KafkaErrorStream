#!/bin/bash

mkdir ~/db_backup
mkdir ~/db_backup/postgres
mkdir ~/db_backup/postgres/pg17
mkdir ~/db_backup/postgres/pg17/data

docker compose up -d

docker exec -it kafka kafka-topics --create --topic sensor-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
docker exec -it kafka kafka-topics --create --topic user-logs --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
docker exec -it kafka kafka-topics --create --topic error-logs --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092

docker exec -it postgres17 psql -U postgres -c "CREATE DATABASE kafka_test"

docker exec -it postgres17 psql -U postgres -d kafka_test -c "CREATE TABLE error_messages (id SERIAL PRIMARY KEY, process TEXT , message TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"

