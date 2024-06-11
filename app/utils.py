# app/utils.py
import pandas as pd

from app.models import CustomerModel # Can future import other options
import os
from openai import OpenAI
from pathlib import Path
import io



# Define function to highlight cells based on the value ranges
def highlight_cells(val):
    if val >= 90:
        color = 'green'
    elif 80 <= val < 90:
        color = 'yellow'
    else:
        color = 'red'
    return f'background-color: {color}'



if __name__=="__main__":

    api_key = None
    user_input = pd.read_csv(os.path.join(Path(os.getcwd()).parent,"data/Integer_test_data.csv")).columns.tolist()
    var = completion_to_dataframe(column_matcher_gpt(user_input, api_key), to_csv=True)
