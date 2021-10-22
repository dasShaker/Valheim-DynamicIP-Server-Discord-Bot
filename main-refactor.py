"""
A simple Discord Bot that allows you to provide your locally hosted server's direct connect information for your players.
The Direct Connect Information is pulled from a Dynamic IP Address provider such as www.noip.com.  If you pay for a dedicated
server hosted in the cloud, you don't need this script.

This bot should be limited to a single text channel, and locked behind role access given only to players on your server.

You must create a .env file to hold your Discord Bot Token and place it in the same folder where you save this script.

I may do another version later where this can be turned into a cog and incorporated into an overlord bot.

REF
https://discordpy.readthedocs.io/en/stable/api.html

I have no affiliation with www.noip.com.  It's just the only one I'm familiar with.
Created using python3.7
dasShaker Oct 21, 2021
"""

import socket
import os
from discord.ext import commands
from dotenv import load_dotenv

# Create the Bot and load the token from your .env file.
"""
Paste your bot token into a .env file as follows:
                   TOKEN = 'your_token_here'
"""
bot = commands.Bot(command_prefix="!")
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Dynamic IP Server Information
"""
Sign up for a free dynamic IP host name from a website like www.noip.com or similar.
"""
my_host_name = "YOUR_HOSTNAME_HERE"  # Place the host name between quotes
my_server_port = 2456  # Should match your server_start .bat file.
my_server_password = "YOUR_PASSWORD"  # Place the password between quotes. Should match your server_start .bat file. Case sensitive.

# Discord Text Channel Options
"""
Right-click the channel the bot will work in, Copy ID, and paste the number here <without quotes>.
Set the bot's channel connect message.
"""                  
bot_text_channelID = 123456789012345678
bot_text_channel_info_message = "Odin's messenger is online.\n -- '!info' for server information.\n -- " \
                                   "'!clear' to clean up the channel. "


@bot.event
async def on_ready():
    print("Valheim Discord Server Bot Running")
    channel = bot.get_channel(bot_text_channelID)
    print("Connected to channel " + str(channel))
    await channel.send(bot_text_channel_info_message)


@bot.command()
async def info(ctx):
    ip = socket.gethostbyname(my_host_name)
    await ctx.send(str(ip) + ":" + str(my_server_port) + "\n" + "PW: " + my_server_password, delete_after=10.0)


@bot.command()
async def clear(ctx):
    await ctx.channel.purge()
    await ctx.channel.send(bot_text_channel_info_message)


if __name__ == "__main__":
  bot.run(TOKEN)
