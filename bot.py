##More stuff I want the bot to do:
#1. If someone were to say $slither to @user the snake will respond with a slithering gif
#2. If someone needs help with the commands, they can use $help. The bot will responds with a list of commands
#4. If someone says $bite @user, the bot will respond with either a snake biting gif or a nuzzel gif

#import the discord library
import discord
import json
import requests

def get_meme():
  response = requests.get('https://meme-api.com/gimme/snakememes') #You can change the subreddit to any subreddit you want
  json_data = json.loads(response.text)
  return json_data['url']

#Created a class that inherits from discord.Client
class MyClient(discord.Client):
  #The on ready is used when the discord bot is ready to start working
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  #The on message is used when the bot receives a message
  async def on_message(self, message):
    if message.author == self.user:
      return
    
    #Check if the message starts with $meme, thus it prints out a "funny" snake meme
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())
    #When the user says $hello the bot responds with its own little hello message
    elif message.content.startswith('$hello'):
      await message.channel.send('Ssss!(Hello!)')
    #If you tell the bot I love you it will respond back with a response and a cute snake image
    elif message.content.startswith('$Love you!'):
      await message.channel.send('Sss!(I love you too!)')
      await message.channel.send("https://i.pinimg.com/736x/8f/5a/0b/8f5a0b9787f745cfe0fe8974d860435c.jpg")
    
    elif message.content.startswith('$slither to {user}'.format(user=message.author.mention)):
      await message.channel.send('Sss!(Slithering...) to : {user}'.format(user=message.author.mention))
      await message.channel.send("https://tenor.com/view/snake-purple-snkae-cute-snake-gif-26014503")
    
    elif message.content.startswith('$bite {user}'.format(user=message.author.mention)):
      await message.channel.send('Sss!(Biting...) : {user}'.format(user=message.author.mention))
      await message.channel.send("https://tenor.com/view/snake-strike-rattle-gif-12291395")

    elif message.content.startswith('$goodnight'):
      await message.channel.send('Sss..(Goodnight!) : {user}'.format(user=message.author.mention))
      await message.channel.send("https://tenor.com/view/點點-睡99-gif-17616746108318256175")

    elif message.content.startswith('$goodmorning'):
      await message.channel.send('Sss!(Goodmorning!) : {user}'.format(user=message.author.mention))
      await message.channel.send("https://tenor.com/view/cute-snake-jawn-good-morning-wake-up-gif-17002140")

    elif message.content.startswith('$fancy snake'):
      await message.channel.send('Sss~(Tis I, a cute fancy snake~)')
      await message.channel.send("https://tenor.com/view/snake-gif-1306923234310821986")

    elif message.content.startswith('$help'):
      await message.channel.send("Ssssss!(Here are the commands you can use: $meme, $hello, $Love you!, $slither, $bite, $goodnight, $goodmorning, $fancy snake)")

#setting for what the bot can access in the server. Assigned the default behavior for the bot 
# thus we have to make the bot message become true
intents = discord.Intents.default()
intents.message_content = True

#This calls it to run the server,
client = MyClient(intents=intents)
client.run('MTQxNTE3NzIzNDc4MzgwMTQwNw.G8g4xS.uHPdyGeIdAq9C2GqUSWad0yaF3PFvVSTqfgkmI') # Replace with your own token.
#Make sure to keep your token private and safe!
