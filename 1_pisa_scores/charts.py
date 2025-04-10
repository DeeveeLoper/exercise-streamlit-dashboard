import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def validate_selection(locations, min_count=1, max_count=None):
    if locations is None or len(locations) < min_count:
        st.warning(f"Please select at least {min_count} country/countries.")
        return False
    if max_count and len(locations) > max_count:
        st.warning(f"Please select at most {max_count} countries.")
        return False
    return True

def scores_by_location_bar(df, country_codes):

    location_avg = df.groupby('location')['value'].mean().reset_index()
    location_avg = location_avg.sort_values('value', ascending=False)
    location_avg['country_name'] = location_avg['location'].map(lambda x: country_codes.get(x, x))
    
    fig = px.bar(
        location_avg,
        x='location', y='value',
        text=location_avg['value'].round(1),
        title="Average PISA Scores by Country",
        color='location',
        hover_data=['country_name']
    )
    fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    fig.update_layout(
        xaxis_title="Country Code", yaxis_title="Average Score",
        showlegend=False, height=500
    )
    fig.update_xaxes(ticktext=location_avg['country_name'], tickvals=location_avg['location'])
    
    st.plotly_chart(fig, use_container_width=True)

def score_trends_by_location(df, selected_locations, country_codes):

    if not validate_selection(selected_locations):
        return
    
    filtered_df = df[df['location'].isin(selected_locations)]
    trends_df = filtered_df.groupby(['location', 'time_period', 'indicator'])['value'].mean().reset_index()
    trends_df['country_name'] = trends_df['location'].map(lambda x: country_codes.get(x, x))
    
    indicators = sorted(trends_df['indicator'].unique())
    if len(indicators) == 0:
        st.warning("No data available for the selected filters.")
        return
        
    indicator_tabs = st.tabs([indicator for indicator in indicators])
    
    for i, indicator in enumerate(indicators):
        with indicator_tabs[i]:
            indicator_df = trends_df[trends_df['indicator'] == indicator]
            
            fig = px.line(
                indicator_df,
                x='time_period', y='value', color='country_name',
                title=f"PISA Score Trends Over Time - {indicator}",
                markers=True,
                labels={'country_name': 'Country', 'time_period': 'Year', 'value': 'Score'}
            )
            fig.update_layout(
                xaxis_title="Year", yaxis_title="Average Score",
                legend_title="Country", height=500
            )
            fig.update_xaxes(
                tickmode='array',
                tickvals=sorted(trends_df['time_period'].unique())
            )
            
            st.plotly_chart(fig, use_container_width=True)

def score_distribution_histogram(df):

    fig = px.histogram(
        df, 
        x='value', nbins=20,
        title="PISA Score Distribution",
        color_discrete_sequence=['#1E3A8A'],
        labels={'value': 'Score'}
    )
    fig.update_layout(
        xaxis_title="Score", yaxis_title="Frequency", height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
