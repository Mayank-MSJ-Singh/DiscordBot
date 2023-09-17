import discord
from langchain import *
from openai import *
import os

os.environ["OPENAI_API_KEY"] = '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'

DisGPT_llm = OpenAI()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        if message.content.startswith("!DisGPT"):
          print(message.content[8:])
          channel = message.channel
          await channel.send(DisGPT_llm.predict(message.content[8:]))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE1Mjk3MzcxMTI4NTE2NjExMg.Gi6Fxe.IA9YKut3qpbYhOs-hW2tDQhrTQU-hi0wOghbHU')