import pandas as pd
from read_data import read_data

# Read Dataframe from CSV file
df = read_data()

# Convert age and salary to numeric values for calculations 
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Salary_SEK'] = pd.to_numeric(df['Salary_SEK'], errors='coerce')

# Calculate overall KPIs
total_employees = len(df)
average_age = round(df['Age'].mean(), 1)
average_salary = round(df['Salary_SEK'].mean(), 2)