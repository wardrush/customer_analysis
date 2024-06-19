import streamlit as st
import app.utils.utils as utils
from app.utils.file_utils import manage_file_uploader




def manage_email_capture():
    # Capture email address from text field
    pass


def manage_report_send():
    pass

def main():

    # Set the title of the frontend
    st.image("./assets/CHC_logo.jpg", use_column_width=True)
    utils.manage_info_blurb()
    #st.title("Customer Data Health Check")

    # Section 1: File Upload
    st.header('📂 1. Upload File', help='Upload a csv file with customer data here')
    uploaded_file, df = manage_file_uploader()


    # Section 2: 2a Criteria Selection
    st.header('🔭 2. Select Criteria', help='Choose what completeness consists of')
    if df is not None:
        # Process criteria selection with checkboxes
        criteria_list = utils.process_criteria_selection(df)
    #criteria = st.text_input("Enter criteria for complete records (comma-separated)", "email,phone")
    #criteria_list = utils.process_criteria_selection(criteria)

        st.header('💡 3. See Results')
        # Section 2: 2b Results Display
        utils.manage_analysis_button(uploaded_file=uploaded_file, df=df, criteria_list=criteria_list)

    # Section 3 Report Management
    #st.header('3. Create and Send Report')
    manage_email_capture()
    manage_report_send()

if __name__ == "__main__":
    main()
