#import the discord library
import discord

#Created a class that inherits from discord.Client
class MyClient(discord.Client):
  #The on ready is used when the discord bot is ready to start working
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  #The on message is used when the bot receives a message
  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$hello'):
      await message.channel.send('Ssssss!(Hello World!)')

#setting for what the bot can access in the server. Assigned the default behavior for the bot 
# thus we have to make the bot message become true
intents = discord.Intents.default()
intents.message_content = True

#This calls it to run the server,
client = MyClient(intents=intents)
client.run('MTQxNTE3NzIzNDc4MzgwMTQwNw.G8g4xS.uHPdyGeIdAq9C2GqUSWad0yaF3PFvVSTqfgkmI') # Replace with your own token.

