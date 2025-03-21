import pandas as pd
from pathlib import Path

def read_data():
    
    data_path = Path(__file__).parent
    df = pd.read_csv(data_path / "data" / "supahcoolsoft.csv", skiprows=5)
    
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Salary_SEK'] = pd.to_numeric(df['Salary_SEK'], errors='coerce')
    
    return df

if __name__ == '__main__':
    df = read_data()
    print(df.columns)
    print("\nFirst 5 rows")
    print(df.head())