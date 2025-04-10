from read_data import read_data
import streamlit as st
import pandas as pd
import plotly.express as px

def employees_by_department_bar():
    
    # Load data from CSV file
    df = read_data()
    # Count employees in each department and prepare data for chart
    dept_counts = df['Department'].value_counts().reset_index()
    dept_counts.columns = ['Department', 'Count']
    # Create bar chart using Plotly Express
    fig = px.bar(
        dept_counts,
        x='Department',
        y='Count',
        text='Count',
        title="Number of employees per department",
        color='Department'
    )
    # Customize chart appearance
    fig.update_layout(
        xaxis_title="Department",
        yaxis_title="Number of employees",
        showlegend=False # Hide redundant legend
    )
    # Display the chart in Streamlit with responsive width
    st.plotly_chart(fig, use_container_width=True)

def salary_distribution_histogram():
    
    df = read_data()
    # Create histogram of salary distribution
    fig = px.histogram(
        df, 
        x='Salary_SEK',
        nbins=20,
        title="Salary distribution",
        color_discrete_sequence=['#1E3A8A']
    )
    # Customize chart appearance
    fig.update_layout(
        xaxis_title="Salary (SEK)",
        yaxis_title="Number of employees" 
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
def salary_by_department_boxplot():
    
    df = read_data()
    # Create box plot comparing salaries across departments
    fig = px.box(
        df,
        x='Department',
        y='Salary_SEK',
        color='Department',
        title="Salaries per department"
        )
    
    fig.update_layout(
        xaxis_title="Department",
        yaxis_title="Salary (SEK)",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

def age_distribution_histogram():
    
    df = read_data()
    
    fig = px.histogram(
        df,
        x='Age',
        nbins=20,
        title="Age distribution",
        color_discrete_sequence=['#1E3A8A']
    )
    
    fig.update_layout(
        xaxis_title="Age",
        yaxis_title="Number of employees",
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
def age_by_department_boxplot():
    
    df = read_data()
    
    fig = px.box(
        df,
        x='Department',
        y='Age',
        color='Department',
        title="Age per department",
    )
    
    fig.update_layout(
        xaxis_title="Department",
        yaxis_title="Age",
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Code to test charts independently. Use: streamlit run charts.py
if __name__ == '__main__':
    import streamlit as st
        
    st.title("Test of diagram")
    employees_by_department_bar()
    salary_distribution_histogram()
    salary_by_department_boxplot()
    age_distribution_histogram()
    age_by_department_boxplot()
    