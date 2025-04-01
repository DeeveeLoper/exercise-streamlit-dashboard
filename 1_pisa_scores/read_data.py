import pandas as pd
from pathlib import Path

def read_data():
    
    data_path = Path(__file__).parent / "data"
    
    data_path.mkdir(exist_ok=True, parents=True)
    
    df = pd.read_csv(data_path / "OECD PISA data.csv")
    
    # Rename columns to match my dashboard
    column_mapping = {
        'LOCATION': 'location',
        'SUBJECT': 'subject',
        'TIME': 'time_period',
        'VALUE': 'value',
        'INDICATOR': 'indicator'
    }
    df = df.rename(columns=column_mapping)
    
    expected_columns = ['location','subject', 'time_period', 'value', 'indicator']
    missing_columns = [col for col in expected_columns if col not in df.columns]
    
    if missing_columns:
        print(f"Warning: Missing expected columns: {', '.join(missing_columns)}")
        
    if 'value' in df.columns:
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        
    return df

if __name__ == '__main__':
    df = read_data()
    
    print(df.columns)
    
    print("\nFirst 5 rows")
    print(df.head())
    
    print("\nStatistics")
    print(f"Total records: {len(df)}")
    print(f"Unique locations: {df['location'].nunique()}")
    print(f"Unique subjects: {df['subject'].nunique()}")
    print(f"Time periods: {df['time_period'].nunique()}")