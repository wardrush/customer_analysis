import streamlit as st
import pandas as pd
import io
#from .boilerplate import analyze_customer_table
from .utils.file_utils import highlight_cells

def manage_analysis_button(uploaded_file=None, df=None, criteria_list=None):
    # Run analysis button
    if st.button("Run Analysis"):
        if df is None:
                df, customers = pd.read_csv(io.StringIO(uploaded_file.getvalue().decode('utf-8')))
        if df is not None:
            try:
                # Analyze the customer data based on criteria
                result = analyze_customer_table(df, criteria_list)
                result_df = pd.DataFrame(result['summary'])

                # Print the results
                st.subheader("Preliminary Results")
                st.write(f"Percentage of complete records: {result['percent_complete']:.2f}%")
                st.subheader("Summary Table")
                # Apply the color highlighting function to the relevant columns
                st.dataframe(result_df.style.applymap(highlight_cells, subset=['Percent Non-null']))

                # st.subheader("AI-Matched Columns & Confidences")
                # st.dataframe(fuzzy_ai_match_columns(uploaded_file))

            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
        else:
            st.error("Please upload a CSV file or select test data to run the analysis.")

def analyze_customer_table(customer_table: pd.DataFrame, criteria_list: list):
    """
    Check the completeness of records in a dataset based on user-defined criteria.

    Parameters:
    customer_table (pd.DataFrame): The customer CRM dataset.
    criteria_list (list): A list of column names to check for completeness.

    Returns:
    dict: A dictionary containing the percentage of complete records and a summary table.
    """
    #customer_table = pd.DataFrame(customer_table)
    # Check if all criteria columns are in the dataframe
    missing_columns = [col for col in criteria_list if col not in customer_table.columns]
    if missing_columns:
        raise ValueError(f"The following columns are missing from the uploaded dataframe: {missing_columns}")

    # Create a boolean mask for complete records based on the criteria
    complete_mask = customer_table[criteria_list].notnull().all(axis=1)

    # Calculate the percentage of complete records
    percent_complete = complete_mask.mean() * 100

    # Initialize the summary dictionary
    summary = {
        'Criterion': [],
        'Percent Non-null': [],
        'Number Non-null': []
    }

    # Calculate the summary statistics for each criterion
    for criterion in criteria_list:
        non_null_mask = customer_table[criterion].notnull()
        percent_non_null = non_null_mask.mean() * 100
        number_non_null = non_null_mask.sum()

        summary['Criterion'].append(criterion)
        summary['Percent Non-null'].append(percent_non_null)
        summary['Number Non-null'].append(number_non_null)

    # Add the summary for complete records
    summary['Criterion'].append('All Criteria')
    summary['Percent Non-null'].append(percent_complete)
    summary['Number Non-null'].append(complete_mask.sum())

    # Convert summary dictionary to a DataFrame
    summary_df = pd.DataFrame(summary)

    result = {'percent_complete': percent_complete, 'summary': summary_df}
    # Return the percentage of complete records and the summary DataFrame
    return result