# Error Logs
from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "error-logs"

error_messages = ["Out of memory", "Connection lost", "Timeout error", "Invalid input"]

for i in range(5):
    message = {"error_code": i, "message": random.choice(error_messages)}
    producer.send(topic, message)
    print(f"Producer 3 Sent: {message}")
    time.sleep(2)

producer.flush()
producer.close()