import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the Streamlit app
st.title('Forecasted Sales Dashboard')

# Description for the app
st.write('This dashboard visualizes the forecasted sales over time based on data from the CSV file.')

# Load the CSV file
# Ensure that the predicted_sales_with_dates.csv is in the same directory as this app.py file
data = pd.read_csv('predicted_sales_with_dates.csv')

# Extract the dates and predicted sales from the DataFrame
# Assuming the first column contains dates and the second column contains predicted sales
data['Date'] = pd.to_datetime(data.iloc[:, 0])  # Convert the first column to datetime
data['Predicted Sales'] = data.iloc[:, 1]       # Extract the second column for predicted sales

# Create a new DataFrame with the extracted data
predictions_df = data[['Date', 'Predicted Sales']]

# Display the data as a table in Streamlit (optional)
st.write("Here is the data used for the forecast:")
st.dataframe(predictions_df)

# Create an interactive line plot using Plotly
fig = px.line(
    predictions_df, 
    x='Date', 
    y='Predicted Sales', 
    title='Forecasted Sales Over Time',
    labels={'Date': 'Date', 'Predicted Sales': 'Sales'}
)

# Update layout for better appearance
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales',
    template='plotly_white',
    width=900,
    height=600
)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)
