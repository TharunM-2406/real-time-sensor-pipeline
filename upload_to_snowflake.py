import snowflake.connector
import pandas as pd

# add your snowflake details
SNOWFLAKE_ACCOUNT = ''
USER = ''
PASSWORD = ''
WAREHOUSE = 'Project1_warehouse'
DATABASE = 'Real_time_data_pipeline'
SCHEMA = 'Project1_Data_Engineer'
TABLE = 'sensor_data '

def upload_csv_to_snowflake(file_path):
    ctx = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA
    )
    cs = ctx.cursor()
    try:
        df = pd.read_csv(file_path)

        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {TABLE} (
            sensor_id STRING,
            timestamp INTEGER,
            temperature FLOAT,
            humidity FLOAT,
            status STRING
        );
        """
        cs.execute(create_table_sql)

        for _, row in df.iterrows():
            insert_sql = f"""
            INSERT INTO {TABLE} (sensor_id, timestamp, temperature, humidity, status)
            VALUES (%s, %s, %s, %s, %s);
            """
            cs.execute(insert_sql, (row['sensor_id'], int(row['timestamp']), float(row['temperature']),
                                    float(row['humidity']), row['status']))
        print(f"Uploaded {len(df)} records to Snowflake.")
    finally:
        cs.close()
        ctx.close()

if __name__ == "__main__":
    upload_csv_to_snowflake('clean_sensor_data.csv')

