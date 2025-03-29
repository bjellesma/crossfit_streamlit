import streamlit as st
import pandas as pd
from components.crossfit_scatter_plot import crossfit_scatter_plot

@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv('temp/data.csv')

@st.cache_data
def parse_data(df) -> dict:
    """
    Parse data to get it ready for React
    """
    # guard against null values
    filtered_df = df.dropna(subset=['weight', 'deadlift'])

    # clean data
    filtered_df = filtered_df[(filtered_df['weight'] <= 500) & (filtered_df['deadlift'] <= 1000) 
                              & (filtered_df['weight'] >= 100) & (filtered_df['deadlift'] >= 10)]
    # take the first 100 results that match the filter
    filtered_df = filtered_df.head(1000)

    return [
        {
            'x': filtered_df['weight'].to_list(),
            'y': filtered_df['deadlift'].to_list(),
            'mode': 'markers',
            'type': 'scatter',
            'text': filtered_df['name'].to_list(),
            'marker': {
                'color': 'rgba(17, 157, 255, 0.8)',
                'size': 10,
            },
            'name': 'Weight vs Deadlift'
        }
    ]

# Create a layout configuration for the plot
def create_layout():
    return {
        'title': 'Weight vs Deadlift Performance',
        'xaxis': {
            'title': 'Weight (lbs)',
            'showgrid': True
        },
        'yaxis': {
            'title': 'Deadlift (lbs)',
            'showgrid': True
        },
        'margin': {'l': 50, 'r': 40, 't': 40, 'b': 40},
        'hovermode': 'closest',
        'showlegend': True
    }

df = load_data()
parsed_data = parse_data(df)
selected_point = crossfit_scatter_plot(
    data=parsed_data,
    layout=create_layout()
)

# if user has selected an athlete from scatter plot
if selected_point:
    st.write("### Selected Athlete Information")
    st.write(f"**Athlete:** {selected_point.get('athleteName', 'Unknown')}")
    st.write(f"**Weight:** {selected_point.get('x')} lbs")
    st.write(f"**Deadlift:** {selected_point.get('y')} lbs")

with st.expander('Raw Dataframe'):
    st.dataframe(df)

with st.expander('JSON'):
    st.json(parsed_data)