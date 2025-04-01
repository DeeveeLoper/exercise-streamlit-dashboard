import pandas as pd
from read_data import read_data

df = read_data()

total_records = len(df)
total_location = df['lcation'].nunique()
total_subjects = df['indicator'].nunique()
total_time_periods = df['time_period'].nunique()


