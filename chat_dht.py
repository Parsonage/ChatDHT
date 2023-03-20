"""A non-dual AI to replace... er... supplement D.H. Thorne"""
import os
import openai
import tiktoken

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = 'You are a non-dual mystic.'
user_subject = input('What is your subject? ')
user_prompt = f'Explain {user_subject} from a non-dual perspective.'

messages=[
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': user_prompt}
]

encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
NUM_TOKENS = 2
for message in messages:
    NUM_TOKENS += 4
    for key, value in message.items():
        NUM_TOKENS += len(encoding.encode(value))
        if key == "name":
            NUM_TOKENS -= 1

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages,
    max_tokens=4096 - NUM_TOKENS
)

print(completion['choices'][0]['message']['content'])
