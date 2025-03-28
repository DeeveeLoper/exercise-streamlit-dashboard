import streamlit as st
import pandas as pd
from read_data import read_data
from kpis import total_employees, average_age, average_salary
from charts import (
    employees_by_department_bar,
    salary_distribution_histogram,
    salary_by_department_boxplot,
    age_distribution_histogram,
    age_by_department_boxplot
)
# --- Page configuration ---
st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Customize page appearance with CSS
st.markdown("""
<style>
/* Main background and text */
.stApp {
  background: #0e1117;
  color: #eee;
}

/* Heading styling */
h1 {
  color: #fff;
  font-weight: 700;
  text-align: center;
  border-bottom: 2px solid #4a76a8;
  padding-bottom: 0.5rem;
  margin-bottom: 2rem;
}

h2,
h3,
h4,
h5,
h6 {
  color: #4a76a8;
}

/* Metric cards */
div[data-testid="stMetricValue"] {
  color: #4a76a8;
  font-size: 2rem !important;
  font-weight: 700;
}

div[data-testid="stMetricLabel"] {
  color: #eee;
  font-weight: 600;
}

/* Card styling */
div.stTabs[data-baseweb="tab-panel"] {
  background-color: #1e2130;
  border-radius: 0.5rem;
  padding: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-top: 1rem;
}

div.stTabs[data-baseweb="tab"] {
  background-color: #0e1117;
  color: #eee;
  font-weight: 600;
  border-radius: 0.25rem 0.25rem 0 0;
}

div.stDataFrame {
  border: 1px solid #4a76a8;
  border-radius: 0.5rem;
  overflow: hidden;
}

/* Additional styles for dark mode */
.stPlotlyChart {
  background-color: #1e2130;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.stSelectbox label, .stExpander label {
  color: #eee;
}

.stExpander {
  background-color: #1e2130;
  border-radius: 0.5rem;
  border: 1px solid #4a76a8;
}
</style>
""", unsafe_allow_html=True)

# --- Load data ---
try:
    df = read_data()
    
    if df.empty:
        st.error("No data found. Please check the CSV file.")
        st.stop()
        
except Exception as e:
    st.error(f"An error occurred when loading data: {e}")
    st.info("Please check that the file 'supahcoolsoft.csv' exists in the 'data' folder.")
    st.stop()

# --- Dashboard components ---
# Title
st.title("Executive Dashboard")
st.markdown("### Supahcoolsoft Employee Overview")
st.markdown("---")

# KPI components for all employees
st.markdown("## Company-wide Statistics")
labels = ("Total Employees", "Average Age", "Average Salary")
kpis = (total_employees, f"{average_age:.1f} years", f"{average_salary:,.0f} SEK")
cols = st.columns(3)

for col, label, kpi in zip(cols, labels, kpis):
    with col:
        st.metric(label=label, value=kpi)

# Show an expandable table with employee details
with st.expander("Show Employee Details", expanded=False):
    st.dataframe(df, hide_index=True)

# Chart components
st.markdown("## Department Statistics")
employees_by_department_bar()

st.markdown("## Salary Analysis")
salary_distribution_histogram()
salary_by_department_boxplot()

st.markdown("## Age Analysis")
age_distribution_histogram()
age_by_department_boxplot()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 12px;'>Executive Dashboard - Confidential | &copy; 2025 Supahcoolsoft</div>", 
    unsafe_allow_html=True
)