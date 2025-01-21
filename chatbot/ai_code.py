from ai21 import AI21Client
from ai21.models.chat import UserMessage
import json

# One way of passing your key to the client.
client = AI21Client(api_key="ca6HOzLp2g017w7e7FKOi52Ba00SpMRg")

# Another way to set your key is by setting the AI21_API_KEY
# environment variable to your key value. The default value
# of api_key in the constructor is os.environ["AI21_API_KEY"]. So:
# import os
# os.environ["AI21_API_KEY"] =  <YOUR_API_KEY>
# client = AI21Client();

def single_message_instruct(question):
    messages = [
        UserMessage(
            content=question
        )
    ]

    response = client.chat.completions.create(
        model="jamba-1.5-large",
        messages=messages,
        top_p=1.0 ,# Setting to 1 encourages different responses each call.
        temperature=0 #How much variation to provide in each answer. Setting this value to 0 guarantees the same response to the same question every time. 
    )
    # print(response.to_json())
    return json.dumps(response.model_dump(),indent=4)

# print(type(single_message_instruct("What is the sum of 2 and 3?")))