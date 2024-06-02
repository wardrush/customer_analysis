# app/analysis.py
import pandas as pd
from .models import CustomerData

def read_csv(uploaded_file=None):
    df = pd.read_csv(uploaded_file)
    customers = []
    for index, row in df.iterrows():
        customer = CustomerData(**row.to_dict())
        customers.append(customer)
    return customers

def analyze_customers(customers, criteria):
    complete_records = []
    incomplete_records = []
    for customer in customers:
        if all(getattr(customer, field) for field in criteria):
            complete_records.append(customer)
        else:
            incomplete_records.append(customer)
    return complete_records, incomplete_records
