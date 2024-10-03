from discord import Intents, Client
from langchain import OpenAI
import os

environ["OPENAI_API_KEY"] = '<Insert Your Key Here>'

DisGPT_llm = OpenAI()


class MyClient(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        if message.content.startswith("!DisGPT"):
          print(message.content[8:])
          channel = message.channel
          await channel.send(DisGPT_llm.predict(message.content[8:]))

intents = Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE1Mjk3MzcxMTI4NTE2NjExMg.GJsQL6.1ZeqFFx5FLUmM1fRFVCtMRQTI6VQNpuDgFZUsw')
