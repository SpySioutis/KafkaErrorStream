# User Logs
from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "user-logs"

actions = ["login", "logout", "purchase", "view"]

for i in range(10):
    message = {"user_id": i, "action": random.choice(actions)}
    producer.send(topic, message)
    print(f"Producer 2 Sent: {message}")
    time.sleep(1)

producer.flush()
producer.close()