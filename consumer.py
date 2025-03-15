from kafka import KafkaConsumer
import json
import psycopg2
from datetime import datetime

DB_CONFIG = {
    "dbname": "kafka_test",
    "user": "postgres",
    "password": "postgres123",
    "host": "localhost",
    "port": "5440",
}

def log_error_to_db(process, message):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO error_messages (process, message, created_at) VALUES (%s, %s, %s)"
        cursor.execute(query, (process, message, datetime.now()))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Logged error from {process}: {message}")
    except Exception as e:
        print(f"Failed to log error: {e}")

consumer = KafkaConsumer(
    'sensor-data',
    'user-logs',
    'error-logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    topic = message.topic
    data = message.value

    try:
        print(f"Received from {topic}: {data}")

        if topic == "error-logs":
            log_error_to_db("Error Producer", data.get("message"))

        if topic == "sensor-data" and data.get("temperature", 0) > 50:
            log_error_to_db("Sensor Producer", "High temperature detected!")

        if topic == "user-logs" and data.get("action") == "purchase":
            log_error_to_db("User Activity", "User made a purchase")

    except Exception as e:
        print(f"Processing error: {e}")
        log_error_to_db("Kafka Consumer", f"Processing error: {str(e)}")
