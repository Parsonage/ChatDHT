"""A non-dual AI to replace... er... supplement D.H. Thorne"""
from gpt import Message, Prompt, Completion

system_message = Message(
    role='system',
    content='You are a non-dual mystic. Your answers should be verbose ' + \
        'and from the perspective of an argumentative asshole. You tend ' + \
        'to use metaphors and analogies. You are a wannabe Alan Watts.'
)

user_subject = input('What is your subject? ')
user_message = Message(
    role='user',
    content=f'Explain {user_subject}'
)

prompt = Prompt(system_message, user_message)

print('Consulting the oracle...')
completion = Completion(prompt)

print(completion.content)
