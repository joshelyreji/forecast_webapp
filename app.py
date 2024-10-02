import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the Streamlit app
st.title('Forecasted Sales Dashboard')

# Description for the app
st.write('This dashboard visualizes the forecasted sales over 90 days starting from 2024-03-01.')

# Load the CSV file with predicted sales data
# Ensure that the forecasted_sales.csv is in the same directory as this app.py file
data = pd.read_csv('forecasted_sales.csv')

# Generate a date range for 90 days starting from 2024-03-01
date_range = pd.date_range(start='2024-03-01', periods=len(data), freq='D')

# Create a DataFrame with dates and predicted sales
predictions_df = pd.DataFrame({
    'Date': date_range,
    'Predicted Sales': data.iloc[:, 0]  # Assuming the predicted sales are in the first column
})

# Display the data as a table in Streamlit (optional)
st.write("Here is the data used for the forecast:")
st.dataframe(predictions_df)

# Create an interactive line plot using Plotly
fig = px.line(
    predictions_df, 
    x='Date', 
    y='Predicted Sales', 
    title='Forecasted Sales Over Time',
    labels={'Date': 'Date', 'Predicted Sales': 'Sales'},
    markers=True  # Adds markers to the line for better visibility
)

# Update layout for better appearance
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales',
    template='plotly_white',
    width=900,
    height=600,
    xaxis=dict(
        tickformat='%Y-%m-%d',  # Format for date display
        dtick='5D',  # Tick every 5 days
        tickmode='linear',  # Ensures we get ticks every 5 days
        ticks='outside',  # Place ticks outside the plot
    )
)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)
