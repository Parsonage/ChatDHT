"""A non-dual AI to replace... er... supplement D.H. Thorne"""
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = 'Explain art from a non-dual perspective.'
completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a non-dual mystic.'},
        {'role': 'user', 'content': prompt}
    ]
)

print(completion['choices'][0]['message']['content'])
