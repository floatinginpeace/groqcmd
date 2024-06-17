
import os
from groq import Groq
from dotenv import load_dotenv
import sys

load_dotenv()

def llm_convo():

    MODEL= "llama3-70b-8192"
    system_prompt = "Make the answer as consise as possible."
    client = Groq( api_key = os.environ.get("GROQ_API_KEY") )
    user_input = input("Ask Groq: ")
    message_prompt =  [
            {
                'role' : 'user',
                'content': f"{system_prompt}{user_input}"
            }
        ]

    chat_completion = client.chat.completions.create(
        messages = message_prompt, 
        model = MODEL,
        tool_choice = "auto"
    )

    #initial response from model
    response_message = chat_completion.choices[0].message

    print (response_message.content)

    while True:
        additional_input = input("Next prompt (type 'q' to stop): ")
        
        if additional_input.lower() == 'q':
            break
        message_prompt.append({"role": "user",
                          "content": f"{system_prompt}{additional_input}"})
        response = client.chat.completions.create(
            messages = message_prompt, 
            model = MODEL,
            tool_choice = "auto"
        )
    
        other_response_message = response.choices[0].message
        print(other_response_message.content)

llm_convo()

