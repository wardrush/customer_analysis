# main.py
import streamlit as st
import pandas as pd
from app.analysis import read_csv, analyze_customers
from app.report import generate_report

# Set the title of the app
st.title("Customer Data Analysis")

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Display a preview of the uploaded file
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if df.empty:
            st.error("The uploaded file is empty. Please upload a valid CSV file.")
        else:
            st.write("File Preview:")
            st.dataframe(df.head())
    except pd.errors.EmptyDataError:
        st.error("No columns to parse from file. Please upload a valid CSV file.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Text input for criteria
criteria = st.text_input("Enter criteria for complete records (comma-separated)", "email,phone_number")

# Initial estimate title line
initial_estimate = st.empty()
initial_estimate.text("Initial Estimate of Complete Records: 0%")

# Run analysis button
if st.button("Run Analysis"):
    if uploaded_file is not None:
        try:
            # Read the CSV file and convert to customer data instances
            customers = read_csv(uploaded_file)
            
            # Split the criteria input into a list
            criteria_list = [c.strip() for c in criteria.split(',')]
            
            # Analyze the customer data based on criteria
            complete_records, incomplete_records = analyze_customers(customers, criteria_list)
            
            # Calculate the percentage of complete records
            total_records = len(customers)
            complete_percentage = (len(complete_records) / total_records) * 100 if total_records > 0 else 0
            
            # Update the initial estimate title line
            initial_estimate.text(f"Initial Estimate of Complete Records: {complete_percentage:.2f}%")
            
            # Display the analysis results
            st.write(f"Complete Records: {len(complete_records)}")
            st.write(f"Incomplete Records: {len(incomplete_records)}")
            
            # Email input for sending the report
            email = st.text_input("Enter your email to receive the report")
            
            # Generate the report and send it to the provided email
            if st.button("Generate Report"):
                generate_report(complete_records, incomplete_records, email)
                st.success(f"Report generated and saved as {email}_report.pdf")
        except Exception as e:
            st.error(f"An error occurred during analysis: {e}")
    else:
        st.error("Please upload a CSV file to run the analysis.")
