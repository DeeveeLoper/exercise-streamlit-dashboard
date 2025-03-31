import streamlit as st
import pandas as pd
from pathlib import Path
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

# CSS loading function
def load_css():
    css_path = Path(__file__).parent / "style" / "style.css"
    st.write(f"Looking for CSS at: {css_path}")
    if css_path.exists():
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("style.css not found. Please check the path.")

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
