# Test streamlit connectivity with databricks delta table/sql end point
# Streamlit can be used to connect to Databricks Delta tables and SQL endpoints through the use of the Databricks SQL Endpoint JDBC/ODBC driver.
# Here's a sample code snippet to connect Streamlit with Databricks Delta:

import streamlit as st
import pandas as pd
import sqlalchemy
 
# Set up a connection to the Databricks SQL Endpoint using SQLAlchemy
# Replace with your own values for the JDBC/ODBC driver and endpoint URL
engine = sqlalchemy.create_engine("databricks+odbc://<Driver Name>:<Host Name>:<Port Number>?Authentication=<Auth Type>")
 
# Define a function to execute SQL queries and return the results as a Pandas dataframe
def run_query(query):
    with engine.connect() as con:
        rs = con.execute(query)
        df = pd.DataFrame(rs.fetchall(), columns=rs.keys())
    return df
 
# Example query to retrieve data from a Delta table
query = "SELECT * FROM my_delta_table"
 
# Call the function to execute the query and display the results in Streamlit
result_df = run_query(query)
st.dataframe(result_df)

# Make sure to replace the values in the engine variable with your own JDBC/ODBC driver name, host name, port number, and authentication type.
# Also, note that Databricks Delta tables can be accessed through the Databricks Delta JDBC driver, while Databricks SQL endpoints can be accessed through the Databricks SQL Endpoint JDBC/ODBC driver.

# Ref: https://community.databricks.com/t5/data-engineering/can-anyone-provide-support-on-streamlit-connectivity-with/td-p/5111
