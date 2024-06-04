# main.py
import streamlit as st
import io
import pandas as pd
from app.analysis import read_csv, analyze_customer_table
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
                return uploaded_file
        except pd.errors.EmptyDataError:
            st.error("No columns to parse from file. Please upload a valid CSV file.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

def process_criteria_selection(criteria_input=None):
    criteria_list = [c.strip() for c in criteria_input.split(',')]
    return criteria_list


def manage_analysis_button(uploaded_file=None, criteria_list=None):
    # Run analysis button
    if st.button("Run Analysis"):
        if uploaded_file is not None:
            try:
                # Read the CSV file and convert to customer data instances
                # TODO Figure out if we want to use the customer data model at this stage
                uploaded_df, customers = read_csv(io.StringIO(uploaded_file.getvalue().decode('utf-8')))

                # Analyze the customer data based on criteria
                result = analyze_customer_table(uploaded_df, criteria_list)

                # Print the results
                st.subheader("Preliminary Results")
                st.write(f"Percentage of complete records: {result['percent_complete']:.2f}%")
                st.subheader("Summary Table")
                st.dataframe(result['summary'])

            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
        else:
            st.error("Please upload a CSV file to run the analysis.")

def manage_email_capture():
    # Capture email address from text field
    pass

def manage_report_send():
    pass

def main():

    # Set the title of the app
    st.title("Customer Data Analysis")

    # Section 1: File Upload
    st.header('1. Upload File', help='Upload a csv file with customer data here')
    uploaded_file = manage_file_uploader()

    # Section 2: 2a Criteria Selection
    st.header('2. Select Criteria', help='Choose what completeness consists of')
    criteria = st.text_input("Enter criteria for complete records (comma-separated)",
                                                    "email,phone_number")
    criteria_list = process_criteria_selection(criteria)

    # Section 2: 2b Results Display
    manage_analysis_button(uploaded_file=uploaded_file, criteria_list=criteria_list)

    # Section 3 Report Management
    st.header('3. Create and Send Report')
    manage_email_capture()
    manage_report_send()

if __name__ == "__main__":
    main()