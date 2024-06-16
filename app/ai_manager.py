#app/ai_manager.py
#
from openai import OpenAI
from app.data.models import CustomerModel
import pandas as pd
import io
def column_matcher_gpt(user_input, api_key):
    system_context = """
                    This GPT is an assistant tool that imports a list of column names from a dataset and a customer data
                    model, compares them, and returns a CSV with three columns: the customer data model fields, guessed
                    matching column names from the dataset, and a confidence percentage for each match. The assistant
                    focuses on accurately matching fields and providing a clear, easy-to-understand CSV output. It should
                    use common variations in naming conventions and educated guesses to improve match accuracy and indicate
                    lower confidence for ambiguous matches.
                    
                    Please only return a python-readable csv as your response. Do not include newline characters.
    
                    The tone is professional and clear, providing precise and helpful information.
                    """

    user_input = user_input

    client = OpenAI(
       api_key=api_key,
    )

    completion = client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[
        {"role": "system", "content": system_context},
        {"role": "user", "content": f"Customer Data Model Fields:{CustomerModel.get_fields()}"},
        {"role": "user", "content": f"User Input Fields:{user_input}"}
      ]
    )
    return completion

def filter_by_confidence(dataframe, cutoff):
    filtered_df = dataframe[dataframe['confidence_percentage'] > cutoff]
    return filtered_df

def completion_to_dataframe(input_gpt_response, confidence_cutoff=80, to_csv=False):
    completion_message = input_gpt_response.choices[0].message.content
    resp_df = pd.read_csv(io.StringIO(completion_message), sep=",")
    resp_df = resp_df.sort_values(by=resp_df.columns[2], ascending=False)
    if to_csv: resp_df.to_csv("Response.csv")
    resp_df = filter_by_confidence(resp_df, confidence_cutoff)
    return resp_df