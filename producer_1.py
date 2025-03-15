# Temperature Sensor
from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "sensor-data"

for i in range(100):
    message = {"sensor_id": i, "temperature": round(random.uniform(20, 70), 2)}
    producer.send(topic, message)
    print(f"Producer 1 Sent: {message}")
    # time.sleep(1)

producer.flush()
producer.close()

