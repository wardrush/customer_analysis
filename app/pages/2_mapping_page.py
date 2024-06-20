import streamlit as st
from shared_elements import render_sidebar, render_header
from ..services.data_model_validation_service import map_columns

# Render shared elements
render_sidebar()
render_header()

st.title("Page 2")
st.header('1b. Map Fields')
if df is not None: map_columns(df)

# Add your content for Page 2 here
st.write("This is Page 2. Complete this task to proceed.")

if st.session_state.get('task2_completed', False):
    if st.button("Proceed to Page 3"):
        st.experimental_set_page_config(page_title="Page 3")
        st.experimental_rerun()
