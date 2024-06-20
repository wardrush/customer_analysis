import streamlit as st
def process_criteria_selection(df):
    # Create a list to store the selected criteria
    criteria_list = []

    # Divide columns into three lists for a three-column layout
    third = len(df.columns) // 3
    columns_left = df.columns[:third]
    columns_middle = df.columns[third:2 * third]
    columns_right = df.columns[2 * third:]

    # Display checkboxes for each column in a three-column layout
    st.write("Select the criteria for completeness:")
    col1, col2, col3 = st.columns(3)

    with col1:
        for column in columns_left:
            if st.checkbox(column, key=column):
                criteria_list.append(column)

    with col2:
        for column in columns_middle:
            if st.checkbox(column, key=column):
                criteria_list.append(column)

    with col3:
        for column in columns_right:
            if st.checkbox(column, key=column):
                criteria_list.append(column)

    return criteria_list