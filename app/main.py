import streamlit as st

from utils.file_utils import manage_file_uploader
from services.analysis_service import manage_analysis_button, process_criteria_selection
from utils.style_utils import manage_info_blurb

def main():
    # Set the title of the frontend
    st.image("app/static/assets/CHC_logo.jpg", use_column_width=True)
    manage_info_blurb()

    # Section 1: File Upload
    st.header('📂 1. Upload File', help='Upload a csv file with customer data here')
    uploaded_file, df = manage_file_uploader()

    # Section 2: 2a Criteria Selection
    st.header('🔭 2. Select Criteria', help='Choose what completeness consists of')
    if df is not None:
        # Process criteria selection with checkboxes
        criteria_list = process_criteria_selection(df)

        st.header('💡 3. See Results')
        # Section 2: 2b Results Display
        manage_analysis_button(uploaded_file=uploaded_file, df=df, criteria_list=criteria_list)

if __name__ == "__main__":
    main()
