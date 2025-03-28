import pandas as pd
from pathlib import Path

def read_data():
    
    # Creates the path to data folder
    data_path = Path(__file__).parent / "data"
    # Create data folder if doesen't exist
    data_path.mkdir(exist_ok=True, parents=True)
    # Read CSV file
    df = pd.read_csv(data_path / "supahcoolsoft.csv")
        
    return df

# Runs only when the script is executed directly
if __name__ == '__main__':
    # Call the read_data function
    df = read_data()
    
    print(df.columns)
    
    print("\nFirst 5 rows")
    print(df.head())