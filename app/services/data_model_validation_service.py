import streamlit as st
import pandas as pd
from models import CustomerModel

def display_mapping_ui(input_df: pd.DataFrame):
    # Get list of columns in the input DataFrame
    input_columns = input_df.columns.tolist()

    # Get list of fields in CustomerModel
    customer_fields = ["{Keep Original Field}"] + CustomerModel.get_fields()

    # Create a dictionary to store the mapping
    column_mapping = {}

    st.title("Map CRM Extract Columns to Customer Data Model")

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
        st.write("Column Mapping (for your data dictionary):")

        # Ensure we keep original field names where {Keep Original Field} is selected
        mapping_to_display = {
            col: (column_mapping[col] if column_mapping[col] != "{Keep Original Field}" else col)
            for col in input_columns
        }

        st.json(mapping_to_display)

        # Apply the mapping to transform the DataFrame (if needed)
        # Rename columns only if the selected field is not "{Keep Original Field}"
        transformed_df = input_df.rename(
            columns={col: column_mapping[col] for col in input_columns if column_mapping[col] != "{Keep Original Field}"}
        )

        # Check for duplicate column names after renaming
        if transformed_df.columns.duplicated().any():
            st.error("Duplicate column names found after renaming. Please ensure all mappings are unique.")
        else:
            st.write("Transformed DataFrame:")
            st.dataframe(transformed_df)

            # Store the transformed DataFrame in session state for later use
            st.session_state.transformed_df = transformed_df

            # Display checkboxes for criteria selection if transformation is successful
            st.write("Select Criteria for Analysis:")
            criteria_columns = st.session_state.transformed_df.columns.tolist()
            selected_criteria = []
            for col in criteria_columns:
                if st.checkbox(f"Use {col} for analysis"):
                    selected_criteria.append(col)

            # Store selected criteria in session state for later use
            st.session_state.selected_criteria = selected_criteria

            if st.button("Submit for Analysis"):
                st.write("Selected Criteria for Analysis:")
                st.json(st.session_state.selected_criteria)
                # Proceed with the analysis using the selected criteria

    return st.session_state.get('transformed_df', input_df)

# Example usage with a dummy DataFrame
if __name__ == "__main__":
    # Example CRM extract DataFrame
    data = {
        'contact_id': ['1', '2', '3'],
        'FirstName': ['Alice', 'Bob', 'Charlie'],
        'phone': ['123-456-7890', '234-567-8901', '345-678-9012'],
        'Company': ['Company A', 'Company B', 'Company C'],
        'ProjectName': ['Project X', 'Project Y', 'Project Z'],
        'ProjectType': ['Type 1', 'Type 2', 'Type 3'],
        'InvoiceAddress': ['Address 1', 'Address 2', 'Address 3'],
        'PhoneNumber': ['111-222-3333', '444-555-6666', '777-888-9999'],
        'BuyerTitle': ['Buyer 1', 'Buyer 2', 'Buyer 3']
    }
    df = pd.DataFrame(data)
    display_mapping_ui(df)
