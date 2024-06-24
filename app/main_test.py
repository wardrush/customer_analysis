import streamlit as st

# Setting the page configuration to use the wide layout
st.set_page_config(layout="wide")

# Main content
st.title("Test App Runs!")

# Ensure the sidebar is empty
with st.sidebar:
    st.empty()