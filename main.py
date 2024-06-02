# main.py
import streamlit as st
from app.analysis import read_csv, analyze_customers
from app.report import generate_report

st.title("Customer Data Analysis")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
criteria = st.text_input("Enter criteria for complete records (comma-separated)", "email,phone_number")

if uploaded_file is not None:
    customers = read_csv(uploaded_file)
    criteria_list = criteria.split(',')
    complete_records, incomplete_records = analyze_customers(customers, criteria_list)
    
    email = st.text_input("Enter your email to receive the report")
    
    if st.button("Generate Report"):
        generate_report(complete_records, incomplete_records, email)
        st.success(f"Report generated and sent to {email}")
