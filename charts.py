from read_data import read_data
import streamlit as st
import pandas as pd
import plotly.express as px

# Create streamlit diagram

def employees_by_department_bar():
    
    df = read_data()
    
    dept_counts = df['Department'].value_counts().reset_index()
    dept_counts.columns = ['Department', 'Count']

    fig = px.bar(
        dept_counts,
        x='Department',
        y='Count',
        text='Count',
        title="Antal Anställda per avdelning",
        color='Department'
    )

    fig.update_layout(
        xaxis_title="Avdelning",
        yaxis_title="Antal anställd",
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

def salary_distribution_histogram():
    
    df = read_data()
    
    fig = px.histogram(
        df, 
        x='Salary_SEK',
        nbins=20,
        title="Lönefördelning",
        color_discrete_sequence=['#1E3A8A']
    )
    
    fig.update_layout(
        xaxis_title="Lön (kr)",
        yaxis_title="Antal anställda" 
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
def salary_by_department_boxplot():
    
    df = read_data()
        
    fig = px.box(
        df,
        x='Department',
        y='Salary_SEK',
        color='Department',
        title="Löner per avdelning"
        )
    
    fig.update_layout(
        xaxis_title="Avdelning",
        yaxis_title="Lön (kr)",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

def age_distribution_histogram():
    
    df = read_data()
    
    fig = px.histogram(
        df,
        x='Age',
        nbins=20,
        title="Åldersfördlning",
        color_discrete_sequence=['#1E3A8A']
    )
    
    fig.update_layout(
        xaxis_title="Ålder",
        yaxis_title="Antal anställd",
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
def age_by_department_boxplot():
    
    df = read_data()
    
    fig = px.box(
        df,
        x='Department',
        y='Age',
        color='Department',
        title="Ålder per avdelning",
    )
    
    fig.update_layout(
        xaxis_title="Avdelning",
        yaxis_title="Ålder",
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
if __name__ == '__main__':
    import streamlit as st
        
    st.title("Test av diagram")
    employees_by_department_bar()
    salary_distribution_histogram()
    salary_by_department_boxplot()
    age_distribution_histogram()
    age_by_department_boxplot()
    