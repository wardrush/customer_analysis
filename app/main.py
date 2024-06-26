import streamlit as st

from utils.file_utils import manage_file_uploader
from services.analysis_service import manage_analysis_button
from services.criteria_service import process_criteria_selection
from utils.style_utils import manage_info_blurb
from services.data_model_validation_service import display_mapping_ui
from shared_page_elements import render_header

def main():
    #initialize variables
    df = None
    transformed_df = None
    uploaded_file = None

    # Set the title of the frontend
    render_header()
    manage_info_blurb()

    # Section 1: File Upload
    st.header('📂 1. Upload File', help='Upload a csv file with customer data here')
    uploaded_file, df = manage_file_uploader()

    st.header('1b. Map Fields')
    if df is not None:
        transformed_df = display_mapping_ui(df)


    # Section 2: 2a Criteria Selection
    st.header('🔭 2. Select Criteria', help='Choose what completeness consists of')
    if transformed_df is not None:
        # Process criteria selection with checkboxes
        criteria_list = process_criteria_selection(transformed_df)

        st.header('💡 3. See Results')
        # Section 2: 2b Results Display
        manage_analysis_button(uploaded_file=uploaded_file, df=transformed_df, criteria_list=criteria_list)


if __name__ == "__main__":
    main()
