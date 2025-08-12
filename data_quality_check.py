import pandas as pd

def run_quality_checks(file_path):
    df = pd.read_csv(file_path)

    print(f"Total records: {len(df)}")
    print("Missing values per column:")
    print(df.isnull().sum())
    print(f"Duplicate records: {df.duplicated().sum()}")

if __name__ == "__main__":
    run_quality_checks('clean_sensor_data.csv')

