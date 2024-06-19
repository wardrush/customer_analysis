import streamlit as st
from app.services.api_service import match_columns
from app.services.data_model_validation_service import validate_and_transform_data

def setup_routes():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Upload", "Match Columns", "Validate & Transform", "Enrich Data", "Download"])

    if page == "Upload":
        # Code for file upload
        pass
    elif page == "Match Columns":
        # Code for column matching
        pass
    elif page == "Validate & Transform":
        # Code for data model validation and transformation
        pass
    elif page == "Enrich Data":
        # Code for data enrichment
        pass
    elif page == "Download":
        # Code for file download
        pass
