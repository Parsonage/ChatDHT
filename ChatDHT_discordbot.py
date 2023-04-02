"""A non-dual AI to replace... er... supplement D.H. Thorne"""
import os
import discord
from discord.ext import commands, tasks

# Variables
discord_token = ''
chatdht_trigger = '$askdh '
SYSTEM_PROMPT = 'You are a non-dual mystic. Your answers should be ' + \
                'verbose and from the perspective of an argumentative ' + \
                'asshole. You tend to use metaphors and analogies. You ' + \
                'are a wannabe Alan Watts.'
channel_id = '1091502020541816832'
question_pending = False
question_completed = False
dht_answer = ''


class MyClient(discord.Client):

    async def on_ready(self):
        print(self.user, 'is online.')

    async def on_message(self, message):

        # Failsafe to ensure bot doesn't respond to itself
        if message.author == self.user:
            return

        if message.content.startswith(chatdht_trigger):
            if question_pending:
                await message.reply("I'm busy with another question. Wait some more then ask again egregore.")

            else:
                question_pending == True
                await message.reply("Wait one minute while I stare into my orb & ponder your words.")

        @tasks.loop(seconds=10)
        async def send_message():
            global dht_answer

            async def generate_response():
                response = "this is my response"
                return response

            dht_answer = generate_response()
            print(f'this is the output: {dht_answer}')

        send_message.start()


# End of commands, runs bot
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(discord_token)