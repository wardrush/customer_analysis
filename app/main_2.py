import streamlit as st
from utils.style_utils import manage_info_blurb

def main():
    # Set the title of the frontend
    st.image("app/static/assets/CHC_logo.jpg", use_column_width=True)
    manage_info_blurb()
    setup_routes()

if __name__ == "__main__":
    main()