"""
A simple Discord Bot that allows you to provide your locally hosted server's direct connect information for your players.
This script is for a locally hosted dedicated Valheim server only.

This does not set bot permissions in Discord!  Discord admins should create a text channel for authorized players
to be able to see if they have the specific role for it only.  You are responsible for your own security.

Discord bot permissions should include read and manage messages for this script to work.  I recommend limiting this bot 
to a single 'secure' channel in your Discord.

REF
https://discordpy.readthedocs.io/en/stable/api.html

10/18/21
"""


import discord
import socket

# Dynamic IP server Information for Direct Connect option in the Valheim Game Client
my_hostname = "YOUR_HOST_NAME"  # Dynamic IP address hostname, get from sites such as www.noip.com (Not affiliated)
my_port = 2457  # Valheim ports use 2456 to 2458, pick one.
my_server_password = "YOUR_SERVER_PASSWORD"

# Discord Bot Token *** KEEP THIS SECRET! ***
TOKEN = "YOUR_DISCORD_BOT_TOKEN_GOES_HERE"

client = discord.Client()


@client.event
async def on_ready():
    print("Valheim Discord Server Bot Ready!")


# "delete_after" is a float to delete the bot's message after a set amount of seconds.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!help":
        await message.channel.send("Commands:\n!help - (Brings up this list)\n!ip - (Show current server IP "
                                   "address)\n!pw - (Show current server Password)\n!clear - (Clears the channel of "
                                   "all messages)", delete_after=6.0)

    if message.content == "!ip":
        ip = socket.gethostbyname(my_hostname)
        await message.channel.send(str(ip) + ":" + str(my_port), delete_after=6.0)

    if message.content == "!pw":
        await message.channel.send(my_server_password, delete_after=6.0)

    if message.content == "!clear":
        await message.channel.purge()

if __name__ == "__main__":
    client.run(TOKEN)
