import pandas as pd
from read_data import read_data

# Helper function to find columns based on name
def find_column(df, possible_names):
    for name in possible_names:
        matches = [col for col in df.columns if name.lower() in col.lower()]
        if matches:
            return matches[0]
    return None

# Read Dataframe from CSV file
df = read_data()

# Find relevant columns
age_column = find_column(df, ['Age', 'age'])
salary_column = find_column(df, ['Salary', 'salary', 'Salary_SEK'])
department_column = find_column(df, ['Department', 'department', 'Dept'])

# Check if required columns were found
if not (age_column and salary_column and department_column):
    missing = []
    if not age_column: missing.append("Age")
    if not salary_column: missing.append("Salary")
    if not department_column: missing.append("Department")
    print(f"Warning: Some required columns were not found: {', '.join(missing)}")

# Convert age and salary to numric values for calulations 
if age_column:
    df[age_column] = pd.to_numeric(df[age_column], errors='coerce')
if salary_column:
    df[salary_column] = pd.to_numeric(df[salary_column], errors='coerce')

# Calculate overall KPIs
total_employees = len(df)
average_age = round(df[age_column].mean(), 1) if age_column else 0
average_salary = round(df[salary_column].mean(), 2) if salary_column else 0
