# 📡 Real-Time Sensor Data Pipeline with Kafka & Snowflake

A real-time data pipeline built using **Apache Kafka**, **Python**, and **Snowflake**, simulating IoT-like sensor data, validating it, and loading clean records into a cloud data warehouse.

---

## 🚀 Overview

This project showcases my hands-on skills in data engineering by building an end-to-end real-time data pipeline. It includes:

- Simulating live sensor data (temperature, humidity, status)
- Streaming through Apache Kafka
- Validating and saving clean records to CSV
- Running data quality checks
- Uploading clean data to a Snowflake table

---

## 🧱 Project Structure

| File                      | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `data_producer.py`        | Simulates and sends fake sensor data to Kafka topic (`sensor-data`)         |
| `data_consumer.py`        | Consumes from Kafka, validates data, saves clean records to CSV             |
| `upload_to_snowflake.py`  | Uploads clean CSV data into a Snowflake table named `SENSOR_DATA`           |
| `data_quality_check.py`   | Performs basic data quality checks on the CSV file                          |
| `docker-compose.yml`      | Sets up Kafka and Zookeeper using Docker                                    |
| `requirements.txt`        | Lists all required Python libraries                                         |
| `README.md`               | Project documentation                                                       |

---

## ⚙️ Technologies Used

- **Apache Kafka** (via Docker)
- **Python 3**
  - `kafka-python`
  - `faker`
  - `pandas`
  - `snowflake-connector-python`
- **Docker**
- **Snowflake**

---

## 🔄 How the Pipeline Works

1. **Data Simulation**  
   `data_producer.py` generates fake sensor readings and sends them to a Kafka topic.

2. **Data Consumption & Validation**  
   `data_consumer.py` consumes that stream, filters out invalid data, and saves clean records to a CSV file.

3. **Data Quality Checks**  
   `data_quality_check.py` checks for missing values and duplicates in the CSV.

4. **Upload to Snowflake**  
   `upload_to_snowflake.py` uploads the validated data into the `SENSOR_DATA` table in your Snowflake account.

---

## 📋 Sample Data Format

```json
{
  "sensor_id": "d4476c6d-b3ab-461c-b37f-df518d477455",
  "timestamp": 1754962255,
  "temperature": 30.97,
  "humidity": 86.04,
  "status": "FAIL"
}

