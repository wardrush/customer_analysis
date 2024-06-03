# app/utils.py
from app.models import CustomerData

def get_customer_data_fields():
    return CustomerData.get_fields()
