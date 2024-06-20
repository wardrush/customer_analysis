import streamlit as st
from ..utils.file_utils import manage_file_uploader

def main():
    st.header('📂 1. Upload File', help='Upload a csv file with customer data here')
    uploaded_file, df = manage_file_uploader()
    if df is not None:
        if st.button("Continue with Chosen File", type="primary"):
            st.switch_page("Match Columns")

main()