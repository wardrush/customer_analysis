# app/utils.py
from app.models import CustomerData

def get_customer_data_fields():
    return CustomerData.get_fields()

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

def match_columns(column_names):
    customer_data_columns = get_customer_data_fields()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Match the following columns to the closest columns in this list: {', '.join(customer_data_columns)}.\n\nColumns: {', '.join(column_names)}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
