import streamlit as st
from app.routes import setup_routes

def main():
    st.title("CRM Data Analyzer")
    setup_routes()

if __name__ == "__main__":
    main()