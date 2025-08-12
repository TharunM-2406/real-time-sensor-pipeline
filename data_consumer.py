from kafka import KafkaConsumer
import json
import pandas as pd

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def validate(data):
    required_fields = ['sensor_id', 'timestamp', 'temperature', 'humidity', 'status']
    for field in required_fields:
        if field not in data:
            return False
    return True

def main():
    clean_data = []
    print("Starting consumer...")

    for message in consumer:
        data = message.value
        if validate(data):
            clean_data.append(data)
            print(f"Valid data received: {data}")
        else:
            print(f"Invalid data skipped: {data}")

        if len(clean_data) >= 10:
            df = pd.DataFrame(clean_data)
            df.to_csv('clean_sensor_data.csv', index=False)
            print("Saved 10 records to clean_sensor_data.csv")
            clean_data = []

if __name__ == "__main__":
    main()

