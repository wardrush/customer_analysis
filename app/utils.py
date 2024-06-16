# app/utils.py
import pandas as pd

from app.analysis import analyze_customer_table
import os
from pathlib import Path
import io
import streamlit as st
from .data import boilerplate

def manage_info_blurb():
    with st.expander("**📖 How to Use This Tool**"):
        st.markdown(boilerplate.headers_how_to_use_this_tool)
        st.info(boilerplate.headers_how_to_use_this_tool_info)
    with st.expander("**🔧 Example Use Cases & Tips**"):
        st.markdown(boilerplate.headers_example_use_cases_and_tips)
        st.info(boilerplate.headers_example_use_cases_and_tips_info)

def manage_file_uploader():
    # Radio button to select between uploading a file and using test data
    data_source = st.radio(
        "Select data source:",
        ('Upload a CSV file', 'Use sample data')
    )

    if data_source == 'Upload a CSV file':
        # File uploader for CSV files
        uploaded_file = st.file_uploader("Choose a CSV file. Generally this is an export from your CRM.", type="csv")

        # Display a preview of the uploaded file
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                if df.empty:
                    st.error("The uploaded file is empty. Please upload a valid CSV file.")
                    return None, None
                else:
                    # Show a file preview
                    st.write("File Preview:")
                    st.dataframe(df.head())
                    return uploaded_file, df
            except pd.errors.EmptyDataError:
                st.error("No columns to parse from file. Please upload a valid CSV file.")
                return None, None
            except Exception as e:
                st.error(f"An error occurred: {e}")
                return None, None
        else:
            return None, None
    else:
        # Use test data
        try:
            st.write("Using test data:")
            test_data = pd.read_csv(os.path.join('app', 'data', 'sample_data.csv'), index_col=0)
            df = pd.DataFrame(test_data)
            st.dataframe(df)
            return None, df
        except Exception as e:
            st.error(f"An error occurred while loading test data: {e}")
            return None, None

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


def process_criteria_selection(df):
    # Create a list to store the selected criteria
    criteria_list = []

    # Divide columns into three lists for a three-column layout
    third = len(df.columns) // 3
    columns_left = df.columns[:third]
    columns_middle = df.columns[third:2 * third]
    columns_right = df.columns[2 * third:]

    # Display checkboxes for each column in a three-column layout
    st.write("Select the criteria for completeness:")
    col1, col2, col3 = st.columns(3)

    with col1:
        for column in columns_left:
            if st.checkbox(column, key=column):
                criteria_list.append(column)

    with col2:
        for column in columns_middle:
            if st.checkbox(column, key=column):
                criteria_list.append(column)

    with col3:
        for column in columns_right:
            if st.checkbox(column, key=column):
                criteria_list.append(column)

    return criteria_list


# Integrate this function in the main Streamlit app
def main():
    st.title("Customer Data Completeness Check Tool")

    # Manage file upload
    uploaded_file, df = manage_file_uploader()

    if df is not None:
        # Process criteria selection with checkboxes
        criteria_list = process_criteria_selection(df)

        # Manage the analysis button and perform analysis
        manage_analysis_button(uploaded_file, df, criteria_list)

    # Display information blurb
    manage_info_blurb()

# Define function to highlight cells based on the value ranges
def highlight_cells(val):
    if val >= 90:
        color = 'green'
    elif 80 <= val < 90:
        color = 'yellow'
    else:
        color = 'red'
    return f'background-color: {color}'



if __name__=="__main__":

    api_key = None
    user_input = pd.read_csv(os.path.join(Path(os.getcwd()).parent,"data/sample_data.csv")).columns.tolist()
    var = completion_to_dataframe(column_matcher_gpt(user_input, api_key), to_csv=True)
