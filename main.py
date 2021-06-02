import discord
import os
import random

def rollFateDie(times) :
  returnValue = 0;
  for x in range(times):
    returnValue +=  random.randint(-1,1) 
  return returnValue

def rollDie(times,size) :
  returnValue = 0;
  for x in range(times):
    returnValue +=  random.randint(1,size) 
  return returnValue

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    return("Hello, " + str(rollFateDie(4)) + ". Good morning!")


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/fate'):
        await message.channel.send(greet(message.content))

client.run(os.getenv('TOKEN'))