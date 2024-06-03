# main.py
import streamlit as st
import io
import pandas as pd
from app.analysis import read_csv, analyze_customers
from app.report import generate_report
from app.email import capture_user_email

def manage_file_uploader():
    # File uploader for CSV files
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Display a preview of the uploaded file
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if df.empty:
                st.error("The uploaded file is empty. Please upload a valid CSV file.")
            else:
                # Show a file preview
                st.write("File Preview:")
                st.dataframe(df.head())
        except pd.errors.EmptyDataError:
            st.error("No columns to parse from file. Please upload a valid CSV file.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

def manage_criteria_selection():
    # Text input for criteria
    criteria = st.text_input("Enter criteria for complete records (comma-separated)", "email,phone_number")

def manage_initial_estimate_display():
    # Initial estimate title line
    initial_estimate = st.empty()
    initial_estimate.header("Initial Completeness Estimate: 0%")

def manage_analysis_button():
    # Run analysis button
    if st.button("Run Analysis"):
        if uploaded_file is not None:
            try:
                # Read the CSV file and convert to customer data instances
                st.dataframe(uploaded_file)
                customers = read_csv(io.StringIO(uploaded_file.getvalue().decode('utf-8')))

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

                # Offer Email Generation
                # user_email = st.text_input("Enter your email to receive the report")
                # capture_user_email_and_generate_report(user_email)
                # report = generate_report(complete_records, incomplete_records, user_email)
                # st.success(f"Report generated and saved as {user_email}_report.pdf")
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
        else:
            st.error("Please upload a CSV file to run the analysis.")

def manage_email_capture():
    pass

def manage_report_send():
    pass

def main():
    # Set the title of the app
    st.title("Customer Data Analysis")
    manage_initial_estimate_display()
    st.header('1. Upload File', divider='blue', help='Upload a csv file with customer data here')
    manage_file_uploader()
    st.header('2. Select Criteria', divider='blue', help='Choose what completeness consists of')
    manage_criteria_selection()
    manage_analysis_button()
    manage_initial_estimate_display()

    st.header('3. Create and Send Report', divider='blue')
    manage_email_capture()
    manage_report_send()

if __name__ == "__main__":
    main()