import pandas as pd
from app.models import db, InsuranceRecord
import os

def import_data():
    # Check if data already exists
    if InsuranceRecord.query.first() is None:
        # Get the absolute path to the CSV file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, '..', 'data', 'insurance.csv')
        
        # Check if the CSV file exists
        if not os.path.exists(csv_path):
            print(f"Error: CSV file not found at {csv_path}")
            return

        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Insert data into the database
        for _, row in df.iterrows():
            record = InsuranceRecord(
                age=row['age'],
                sex=row['sex'],
                bmi=row['bmi'],
                children=row['children'],
                smoker=row['smoker'],
                region=row['region'],
                charges=row['charges']
            )
            db.session.add(record)
        
        # Commit the changes
        db.session.commit()
        print(f"Data imported successfully. {len(df)} records added.")
    else:
        print("Data already exists in the database.")

def get_db_stats():
    record_count = InsuranceRecord.query.count()
    return f"Database contains {record_count} records."

