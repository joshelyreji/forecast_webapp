import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the Streamlit app
st.title('Forecasted Sales Dashboard')

# Description for the app
st.write('This dashboard visualizes the forecasted sales over time based on data from the CSV file.')

# Load the CSV file
# Ensure that the forecasted_sales.csv is in the same directory as this app.py file
data = pd.read_csv('forecasted_sales.csv')

# Extract the second column for 'Predicted Sales'
# Assuming the second column (index 1) contains the predicted sales data
predictions_df = pd.DataFrame({
    'Predicted Sales': data.iloc[:, 1]
})

# Display the data as a table in Streamlit (optional)
st.write("Here is the data used for the forecast:")
st.dataframe(predictions_df)

# Create an interactive line plot using Plotly
fig = px.line(
    predictions_df, 
    y='Predicted Sales', 
    title='Forecasted Sales Over Time',
    labels={'index': 'Index', 'Predicted Sales': 'Sales'}
)

# Update layout for better appearance
fig.update_layout(
    xaxis_title='Index',
    yaxis_title='Sales',
    template='plotly_white',
    width=900,
    height=600
)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)
