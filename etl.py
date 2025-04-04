import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Database configuration
DATABASE_URL = "postgresql://myuser:mypassword@db:5432/mydatabase"

def extract():
    """Extract data from a CSV file."""
    print("Extracting data...")
    df = pd.read_csv("data.csv")
    return df

def transform(df):
    """Transform the data (e.g., clean or modify)."""
    print("Transforming data...")
    # Example transformation: Convert all strings to uppercase
    df['name'] = df['name'].str.upper()
    return df

def load(df):
    """Load data into the PostgreSQL database."""
    print("Loading data into the database...")
    engine = create_engine(DATABASE_URL)
    df.to_sql("users", engine, if_exists="append", index=False)

def main():
    try:
        # Extract data
        df = extract()

        # Transform data
        df = transform(df)

        # Load data
        load(df)
        print("ETL process completed successfully.")
    except Exception as e:
        print(f"Error during ETL process: {e}")

if __name__ == "__main__":
    main()