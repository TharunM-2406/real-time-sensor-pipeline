from kafka import KafkaProducer
import json
import time
import random
from faker import Faker

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data():
    return {
        "sensor_id": fake.uuid4(),
        "timestamp": int(time.time()),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 90.0), 2),
        "status": random.choice(["OK", "FAIL"]),
    }

def main():
    while True:
        data = generate_sensor_data()
        producer.send('sensor-data', value=data)
        print(f"Sent: {data}")
        time.sleep(1)

if __name__ == "__main__":
    main()

