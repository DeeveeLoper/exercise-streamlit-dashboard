import pandas as pd
from read_data import read_data

df = read_data()
# Calculate basic statistics about the dataset
total_records = len(df)
total_location = df['location'].nunique()
total_subjects = df['indicator'].nunique()
total_time_periods = df['time_period'].nunique()

# Define helper functions for specific analysis.
# Identify the top performing countries for a specific subject area, gender group, and year
def get_top_countries(n=5, indicator='PISAMATH', subject='TOT', year=2018):
    # Filter data based on the specified criteria
    filtered = df[(df['indicator'] == indicator) & 
                  (df['subject'] == subject) & 
                  (df['time_period'] == year)]
    
    return filtered.sort_values('value', ascending=False).head(n)

# Calculate which countries have shown the most improvement between two assessment years.
def get_most_improved(indicator='PISAMATH', subject='TOT', start_year=2003, end_year=2018):
    
    # Get data for the starting year with specified criteria
    start_df = df[(df['indicator'] == indicator) & 
                 (df['subject'] == subject) & 
                 (df['time_period'] == start_year)]
    
    # Get data for the ending year with specified criteria
    end_df = df[(df['indicator'] == indicator) & 
               (df['subject'] == subject) & 
               (df['time_period'] == end_year)]
    
    # Merge on location
    merged = pd.merge(start_df, end_df, on='location', suffixes=('_start', '_end'))
    
    # Calculate difference
    merged['improvement'] = merged['value_end'] - merged['value_start']
    
    return merged.sort_values('improvement', ascending=False)

def get_gender_gap(indicator='PISAMATH', year=2018):
    
    # Get data for boys in the specified subject and year
    boys = df[(df['indicator'] == indicator) & 
             (df['subject'] == 'BOY') & 
             (df['time_period'] == year)]
    
    # Get data for girls in the specified subject and year
    girls = df[(df['indicator'] == indicator) & 
              (df['subject'] == 'GIRL') & 
              (df['time_period'] == year)]
    
    # Merge on location
    merged = pd.merge(boys, girls, on='location', suffixes=('_boys', '_girls'))
    
    # Calculate gap (positive means boys score higher)
    merged['gap'] = merged['value_boys'] - merged['value_girls']
    
    return merged.sort_values('gap', ascending=False)

# Calculate global average PISA scores for each subject area by year.
def get_global_average_by_year():
    """Get global average scores by year across all indicators"""
    return df[df['subject'] == 'TOT'].groupby(['time_period', 'indicator'])['value'].mean().reset_index()

# Calculate overall average PISA scores for each subject area across all years.
def get_average_by_indicator():
    """Get average scores by indicator across all years"""
    return df[df['subject'] == 'TOT'].groupby('indicator')['value'].mean().reset_index()
