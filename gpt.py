"""A module to interact with the OpenAI GPT-4 API."""
import os

import openai
import tiktoken


class Message:
    """A GPT-4 message."""
    def __init__(self, role: str, content: str) -> None:
        """Initialize a Message."""
        self.role = role
        self.content = content

    def __repr__(self) -> str:
        """Return a string representation of a Message."""
        return f'Message({self.role}, {self.content})'

    @property
    def message(self) -> dict:
        """Return a dictionary representation of a Message."""
        return {'role': self.role, 'content': self.content}


class Prompt:
    """A GPT-4 prompt."""
    def __init__(self, *messages: Message) -> None:
        """Initialize a Prompt."""
        self._messages = [message.message for message in messages]

    def __repr__(self) -> str:
        """Return a string representation of a Prompt."""
        return f'Prompt({self.messages})'

    @property
    def messages(self) -> list[dict]:
        """Return the messages of a Prompt."""
        return list(self._messages)

    @property
    def num_tokens(self) -> int:
        """Return the number of tokens in a Prompt."""
        encoding = tiktoken.encoding_for_model('gpt-4')
        num_tokens = 2
        for message in self.messages:
            num_tokens += 4
            for role, content in message.items():
                num_tokens += len(encoding.encode(content))
                if role == "name":
                    num_tokens -= 1
        return num_tokens


class Completion:
    """A GPT-4 completion."""
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def __init__(self, prompt: Prompt) -> None:
        """Initialize a Completion."""
        self.prompt = prompt
        self.completion = openai.ChatCompletion.create(
            model='gpt-4',
            messages=prompt.messages,
            max_tokens=8096 - prompt.num_tokens,
            temperature=1.0
        )

    def __repr__(self) -> str:
        """Return a string representation of a Completion."""
        return f'Completion({self.prompt}, {self.completion})'

    @property
    def content(self) -> str:
        """Return the content of a Completion."""
        return self.completion['choices'][0]['message']['content']
