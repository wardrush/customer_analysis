# app/analysis.py
import pandas as pd
from .models import CustomerData


def read_csv(uploaded_file=None):
    df = pd.read_csv(uploaded_file)
    customers = []
    for index, row in df.iterrows():
        customer = CustomerData(**row.to_dict())
        customers.append(customer)
    return df, customers

def calculate_filter_results_table(df: pd.DataFrame, criteria: list):
    """
    Check the completeness of records in a dataset based on user-defined criteria.

    Parameters:
    df (pd.DataFrame): The customer CRM dataset.
    criteria (list): A list of column names to check for completeness.

    Returns:
    dict: A dictionary containing the percentage of complete records and a summary table.
    """
    #print(df)
    df = pd.DataFrame(df)
    # Check if all criteria columns are in the dataframe
    missing_columns = [col for col in criteria if col not in df.columns]
    if missing_columns:
        raise ValueError(f"The following columns are missing from the uploaded dataframe: {missing_columns}")

    # Create a boolean mask for complete records based on the criteria
    complete_mask = df[criteria].notnull().all(axis=1)

    # Calculate the percentage of complete records
    percent_complete = complete_mask.mean() * 100

    # Initialize the summary dictionary
    summary = {
        'Criterion': [],
        'Percent Non-null': [],
        'Number Non-null': []
    }

    # Calculate the summary statistics for each criterion
    for criterion in criteria:
        non_null_mask = df[criterion].notnull()
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

    # Return the percentage of complete records and the summary DataFrame
    return {
        'percent_complete': percent_complete,
        'summary': summary_df
    }

def analyze_customers(customers, criteria):
    # Calculate a final percent score @ output a table of record # and % per criterion
    filter_results_table = calculate_filter_results_table(customers, criteria)

    # Define the criteria
    #criteria = ['email', 'phone', 'name', 'address']

    # Get the completeness check result
    result = calculate_filter_results_table(customers, criteria)

    return result

