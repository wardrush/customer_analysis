#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:53:42 2024

@author: wardrushton
"""
from faker import Faker
from faker.providers import DynamicProvider
import pandas as pd
import numpy as np
from datetime import datetime


def remove_random_cells(df, num_removals):
    """
    Remove a specified number of random cells from the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to modify.
    num_removals (int): The number of cells to remove.

    Returns:
    pd.DataFrame: The modified DataFrame with random cells removed.
    """
    rows, cols = df.shape
    total_cells = rows * cols

    if num_removals > total_cells:
        raise ValueError("num_removals exceeds the number of available cells in the DataFrame")

    # Randomly select cells to remove
    flat_indices = np.random.choice(total_cells, num_removals, replace=False)

    # Convert flat indices to row, column indices
    row_indices, col_indices = np.unravel_index(flat_indices, (rows, cols))

    # Create a copy of the DataFrame to modify
    modified_df = df.copy()

    # Remove the selected cells
    for row, col in zip(row_indices, col_indices):
        modified_df.iat[row, col] = np.nan

    return modified_df

# Initialize Faker instance
fake = Faker()

# Define a function to create a transaction history
def create_transaction_history(num=3):
    """
    Creates a list of tuples with transaction ID and datetime of purchase.
    By default, generates 5 transactions per customer.
    """
    return [(fake.uuid4(), fake.date_this_decade()) for _ in range(num)]

project_type_provider = DynamicProvider(
    provider_name="project_type",
    elements=["Environmental Risk Assessment",
            "Remediation and Cleanup Services",
            "Water Resource Management",
            "Air Quality Monitoring",
            "Marine and Coastal Science",
            "Sustainability Consulting",
            "Regulatory Compliance",
            "Hazardous Materials Management",
            "Ecological Restoration",
            "Geotechnical Engineering",
            "Climate Change Adaptation",
            "Environmental Impact Assessments",
            "Waste Management Consulting",
            "Natural Resource Management",
            "Environmental Health and Safety",
            "Contaminant Hydrogeology"])

fake.add_provider(project_type_provider)

engineering_professions_provider = DynamicProvider(
    provider_name="engineering_profession",
    elements=["Environmental Toxicologist",
              "Senior Engineer",
              "Principal Geoscientist",
              "Marine Biologist",
              "Environmental Chemist",
              "Data Analyst",
              "Ecotoxicologist",
              "Project Engineer",
              "Senior Scientist",
              "Environmental Consultant",
              "Water Resource Engineer",
              "Air Quality Specialist",
              "Geotechnical Engineer",
              "Environmental Health Scientist",
              "Marine Ecologist",
              "Contaminant Hydrogeologist",
              "Environmental Risk Assessor",
              "Sustainability Consultant",
              "Remediation Engineer",
              "Senior Data Scientist",
              "Hazardous Materials Specialist",
              "Coastal Engineer",
              "Environmental Planner",
              "Environmental Project Manager",
              "Natural Resource Economist",
              "Climate Change Specialist",
              "Environmental Compliance Officer",
              "Ecological Risk Assessor",
              "Environmental Policy Analyst",
              "Environmental Scientist",
              "Hydrologist",
              "Soil Scientist",
              "Biostatistician",
              "Marine Engineer",
              "Environmental Auditor",
              "Ecosystem Modeler",
              "Environmental Technician",
              "Environmental Impact Assessor",
              "Fisheries Scientist",
              "Wildlife Biologist",
              "Conservation Scientist",
              "Environmental Epidemiologist",
              "Oceanographer",
              "Environmental Microbiologist",
              "Forestry Consultant",
              "Urban Planner",
              "Sustainability Manager",
              "Regulatory Affairs Specialist",
              "Environmental Educator",
              "GIS Specialist"])

fake.add_provider(engineering_professions_provider)

def generate_project_name():
    words = [fake.word().capitalize() for _ in range(2)]
    return ' '.join(words)



# then add new provider to faker instance
fake.add_provider(engineering_professions_provider)

# now you can use:
#fake.engineering_profession()

# Generate the database
rows_requested = 100
data = {
    'ClientID': [fake.uuid4()[0:9] for _ in range(rows_requested)],
    'FirstName': [fake.first_name() for _ in range(rows_requested)],
    'LastName': [fake.last_name() for _ in range(rows_requested)],
    'EmailAddress': [fake.email() for _ in range(rows_requested)],
    'Company': [fake.company() for _ in range(rows_requested)],
    'ProjectName': [generate_project_name() for _ in range(rows_requested)],
    'ProjectType': [fake.project_type() for _ in range(rows_requested)],
    'ShippingAddress': [fake.address() for _ in range(rows_requested)],
    'PhoneNumber': [fake.phone_number() for _ in range(rows_requested)],
    'BuyerTitle': [fake.engineering_profession() for _ in range(rows_requested)]
    #'TransactionHistory': [create_transaction_history() for _ in range(100)]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

modified_df = remove_random_cells(df, 200)


# Showing the first few rows of the dataframe to verify its structure and contents
modified_df.to_csv('test2.csv')
