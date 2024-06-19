import streamlit as st
import pandas as pd
from models import CustomerModel

def map_columns(df: pd.DataFrame):
    # Get list of columns in the input DataFrame
    input_columns = df.columns.tolist()

    # Get list of fields in CustomerModel
    customer_fields = ["*Use Original Field*"] + CustomerModel.get_fields()

    # Create a dictionary to store the mapping
    column_mapping = {}

    # Display the field name from the uploaded file on the left and the field name mapping box on the right
    for col in input_columns:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.write(f"**{col}**")
        with col2:
            column_mapping[col] = st.selectbox(
                f"Map '{col}' to field:",
                options=customer_fields,
                index=0  # Default to "None" if no field is selected
            )

    if st.button("Submit Mapping"):
        st.write("Column Mapping:")
        st.json(column_mapping)

        # Apply the mapping to transform the DataFrame (if needed)
        # Rename columns only if the selected field is not "None"
        transformed_df = df.rename(columns={col: column_mapping[col] for col in input_columns if column_mapping[col] != "*Use Original Field*"})

        st.write("Transformed DataFrame:")
        st.dataframe(transformed_df)

        # Further processing can be done with transformed_df

# Example usage with a dummy DataFrame
if __name__ == "__main__":
    # Example CRM extract DataFrame
    data = {
        'Customer ID': ['1', '2', '3'],
        'First Name': ['Alice', 'Bob', 'Charlie'],
        'Last Name': ['Smith', 'Jones', 'Brown'],
        'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
        'Phone Number': ['123-456-7890', '234-567-8901', '345-678-9012']
    }
    df = pd.DataFrame(data)
    map_columns(df)
