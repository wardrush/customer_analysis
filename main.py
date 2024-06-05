# main.py
import streamlit as st
import io
import pandas as pd
from app.analysis import read_csv, analyze_customer_table
from app.report import generate_report
from app.email import capture_user_email

def manage_file_uploader():
    # File uploader for CSV files
    uploaded_file = st.file_uploader("Choose a CSV file. Generally this is an export from your CRM.", type="csv")

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

def manage_info_blurb():
    with st.expander("**📖 How to Use This Tool**"):
        st.markdown("""
                    **Purpose:**

                    The Completeness Check Tool helps you evaluate the quality of your customer data by analyzing how many records meet specific completeness criteria. This can be invaluable during due diligence or data quality assessments.

                    **How It Works:**

                    Upload your customer CRM dataset and specify the columns that are required for a record to be considered complete (e.g., email and phone).
        """)
        st.info("""
                    **Expected Outputs:**

                    1. **Percentage of Complete Records:** The tool calculates the percentage of records that have non-null values for all specified criteria.
                    2. **Summary Table:** The table provides a detailed breakdown of:
                       - Percentage and number of records with non-null values for each individual criterion.
                       - Overall percentage and number of records that meet all the specified criteria.
                """)
    with st.expander("**🔧 Example Use Cases & Tips**"):
        st.markdown("""
                    **Example Use Case:**

                    Imagine you need to assess the quality of your contact data before merging databases. You want to ensure that each contact has both an email and a phone number. Here's how you would use this tool: Upload your dataset, define your criteria, and run the tool to get the results.

                    **Why Use This Tool?**

                    - **Quick Assessment:** Instantly see the quality of your data based on your defined criteria.
                    - **Informed Decisions:** Use the summary table to understand where your data might be lacking and make informed decisions on data cleaning or enhancement.
                    - **Flexible and Customizable:** Define any number of criteria to suit your specific needs.
                    """)
        st.info("""
                **Tips:**

                - **Regular Usage:** Keep this tool handy during data migration, integration projects, or regular data quality checks.
                - **Feedback Welcome:** If you have suggestions for improving this tool, please reach out directly or open an issue on our GitHub page. Your feedback helps keep this tool accurate and useful.
                """)


def manage_email_capture():
    # Capture email address from text field
    pass

def manage_report_send():
    pass

def main():

    # Set the title of the app
    st.image("./assets/CHC_logo.jpg", use_column_width=True)
    manage_info_blurb()
    #st.title("Customer Data Health Check")



    # Section 1: File Upload
    st.header('📂 1. Upload File', help='Upload a csv file with customer data here')
    uploaded_file = manage_file_uploader()

    # Section 2: 2a Criteria Selection
    st.header('🔭 2. Select Criteria', help='Choose what completeness consists of')
    criteria = st.text_input("Enter criteria for complete records (comma-separated)", "email,phone")
    criteria_list = process_criteria_selection(criteria)

    st.header('💡 3. See Results')
    # Section 2: 2b Results Display
    manage_analysis_button(uploaded_file=uploaded_file, criteria_list=criteria_list)

    # Section 3 Report Management
    #st.header('3. Create and Send Report')
    manage_email_capture()
    manage_report_send()

if __name__ == "__main__":
    main()