import os
import openai

openai.api_key ='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' 
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content":"This is the year 2099.I am a cyberpunk AI. Ask me anything."},{'role': 'user', 'content': prompt}],
        max_tokens=1024,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    response_text = response['choices'][0]['message']['content']
    return response_text


print("Welcome to a conversation with a cyberpunk AI in the year 2099!")
while True:
    # Prompt the user for input
    prompt = input("You: ")

    # Generate a response to the user input
    response = generate_response(prompt)
    print('\n')
    # Print the response
    print('output:-',response)