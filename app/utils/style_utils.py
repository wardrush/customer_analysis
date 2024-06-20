import streamlit as st
from services import boilerplate

def highlight_cells(val):
    if val >= 90:
        color = 'green'
    elif 80 <= val < 90:
        color = 'yellow'
    else:
        color = 'red'
    return f'background-color: {color}'


def manage_info_blurb():
    with st.expander("**📖 How to Use This Tool**"):
        st.markdown(boilerplate.headers_how_to_use_this_tool)
        st.info(boilerplate.headers_how_to_use_this_tool_info)
    with st.expander("**🔧 Example Use Cases & Tips**"):
        st.markdown(boilerplate.headers_example_use_cases_and_tips)
        st.info(boilerplate.headers_example_use_cases_and_tips_info)