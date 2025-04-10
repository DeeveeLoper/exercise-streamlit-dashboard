import streamlit as st
import pandas as pd
from read_data import read_data
from charts import (
    scores_by_location_bar,
    score_trends_by_location,
    score_distribution_histogram
)
from pathlib import Path

# --- Page configuration ---
st.set_page_config(
    page_title="PISA Scores Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS from style file
def load_css(css_file):
    with open(css_file, 'r') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Load the CSS
try:
    load_css(Path(__file__).parent / "style" / "style.css")
except Exception as e:
    st.warning(f"Could not load style.css file. Error: {e}")

# --- Sidebar for filters (Bonus feature) ---
st.sidebar.title("Filters")

# Load data
try:
    df = read_data()
    
    if df.empty:
        st.error("No data found. Please check the CSV file.")
        st.stop()
        
except Exception as e:
    st.error(f"An error occurred when loading data: {e}")
    st.info("Please check that the file 'OECD PISA data.csv' exists in the 'data' folder.")
    st.stop()

# Define mappings for country codes to names (for better readability)
country_codes = {
    'AUS': 'Australia', 'AUT': 'Austria', 'BEL': 'Belgium', 'CAN': 'Canada', 
    'CHL': 'Chile', 'COL': 'Colombia', 'CZE': 'Czech Republic', 'DNK': 'Denmark', 
    'EST': 'Estonia', 'FIN': 'Finland', 'FRA': 'France', 'DEU': 'Germany', 
    'GRC': 'Greece', 'HUN': 'Hungary', 'ISL': 'Iceland', 'IRL': 'Ireland', 
    'ISR': 'Israel', 'ITA': 'Italy', 'JPN': 'Japan', 'KOR': 'Korea', 
    'LVA': 'Latvia', 'LTU': 'Lithuania', 'LUX': 'Luxembourg', 'MEX': 'Mexico', 
    'NLD': 'Netherlands', 'NZL': 'New Zealand', 'NOR': 'Norway', 'POL': 'Poland', 
    'PRT': 'Portugal', 'SVK': 'Slovak Republic', 'SVN': 'Slovenia', 'ESP': 'Spain', 
    'SWE': 'Sweden', 'CHE': 'Switzerland', 'TUR': 'Turkey', 'GBR': 'United Kingdom', 
    'USA': 'United States', 'BRA': 'Brazil', 'RUS': 'Russia',
    'SGP': 'Singapore', 'CHN': 'China', 'HKG': 'Hong Kong', 'MAC': 'Macao',
    'QAT': 'Qatar', 'ARE': 'United Arab Emirates', 'CRI': 'Costa Rica', 'BGR': 'Bulgaria'
}

# Create a display version of the dataframe with country names for display
display_df = df.copy()
display_df['location_name'] = display_df['location'].map(lambda x: country_codes.get(x, x))

# Sidebar filters (Bonus feature)
locations = sorted(df['location'].unique())
indicators = sorted(df['indicator'].unique())
subjects = sorted(df['subject'].unique())
years = sorted(df['time_period'].unique())

# Map indicators to more readable names
indicator_names = {
    'PISAMATH': 'Mathematics',
    'PISAREAD': 'Reading',
    'PISASCIENCE': 'Science'
}

# Map subjects to more readable names
subject_names = {
    'BOY': 'Boys',
    'GIRL': 'Girls',
    'TOT': 'All Students'
}

selected_locations = st.sidebar.multiselect(
    "Select Countries",
    options=locations,
    default=locations[:5],  # Default to first 5 countries
    format_func=lambda x: country_codes.get(x, x)
)

selected_indicators = st.sidebar.multiselect(
    "Select Subjects",
    options=indicators,
    default=indicators,  # Default to all indicators
    format_func=lambda x: indicator_names.get(x, x)
)

selected_subjects = st.sidebar.multiselect(
    "Select Gender",
    options=subjects,
    default=['TOT'],  # Default to total (all students)
    format_func=lambda x: subject_names.get(x, x)
)

selected_years = st.sidebar.multiselect(
    "Select Years",
    options=years,
    default=years,  # Default to all years
)

# Filter data based on selections (Bonus feature)
filtered_df = df.copy()
display_filtered_df = display_df.copy()

if selected_locations:
    filtered_df = filtered_df[filtered_df['location'].isin(selected_locations)]
    display_filtered_df = display_filtered_df[display_filtered_df['location'].isin(selected_locations)]
if selected_indicators:
    filtered_df = filtered_df[filtered_df['indicator'].isin(selected_indicators)]
    display_filtered_df = display_filtered_df[display_filtered_df['indicator'].isin(selected_indicators)]
if selected_subjects:
    filtered_df = filtered_df[filtered_df['subject'].isin(selected_subjects)]
    display_filtered_df = display_filtered_df[display_filtered_df['subject'].isin(selected_subjects)]
if selected_years:
    filtered_df = filtered_df[filtered_df['time_period'].isin(selected_years)]
    display_filtered_df = display_filtered_df[display_filtered_df['time_period'].isin(selected_years)]

# --- Dashboard components ---
# Title
st.title("PISA Scores Dashboard")
st.markdown("### Programme for International Student Assessment")
st.markdown("---")

# Basic statistics of the data (Required feature #1)
st.markdown("## Basic Statistics")
cols = st.columns(4)

with cols[0]:
    st.metric(label="Total Records", value=len(df))
with cols[1]:
    st.metric(label="Locations", value=df['location'].nunique())
with cols[2]:
    st.metric(label="Subjects", value=df['indicator'].nunique())
with cols[3]:
    st.metric(label="Time Periods", value=df['time_period'].nunique())

# Show a table with sample data (Required feature #2)
with st.expander("Show Sample Data", expanded=False):
    # Create a more readable version of the data for display
    display_data = display_filtered_df.copy()
    display_data['indicator'] = display_data['indicator'].map(lambda x: indicator_names.get(x, x))
    display_data['subject'] = display_data['subject'].map(lambda x: subject_names.get(x, x))
    display_cols = ['location_name', 'indicator', 'subject', 'time_period', 'value']
    st.dataframe(display_data[display_cols], hide_index=True, 
                column_config={
                    "location_name": "Country",
                    "indicator": "Subject Area",
                    "subject": "Gender",
                    "time_period": "Year",
                    "value": "PISA Score"
                })

# Bar chart showing average PISA scores by location (Required feature #3)
st.markdown("## Average PISA Scores by Country")
scores_by_location_bar(filtered_df, country_codes)

# Plot trends that can be filtered for each country (Required feature #4)
st.markdown("## PISA Score Trends Over Time")
score_trends_by_location(filtered_df, selected_locations, country_codes)

# Additional visualizations
if len(selected_indicators) > 1:
    indicator_for_dist = st.selectbox(
        "Select subject for score distribution:",
        options=selected_indicators,
        format_func=lambda x: indicator_names.get(x, x)
    )
    dist_df = filtered_df[filtered_df['indicator'] == indicator_for_dist]
else:
    dist_df = filtered_df

st.markdown("## Score Distribution")
score_distribution_histogram(dist_df)

