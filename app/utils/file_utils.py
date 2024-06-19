import streamlit as st
import pandas as pd

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
            test_data = pd.read_csv(os.path.join('frontend', 'data', 'sample_data.csv'), index_col=0)
            df = pd.DataFrame(test_data)
            st.dataframe(df)
            return None, df
        except Exception as e:
            st.error(f"An error occurred while loading test data: {e}")
            return None, None