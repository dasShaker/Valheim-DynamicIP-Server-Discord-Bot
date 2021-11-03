# Valheim-DynamicIP-Server-Discord-Bot
A discord bot that can provide Dynamic IP address information to authorized users in order to Direct Connect to your Valheim locally hosted dedicated server.  This is **not** meant for paid dedicated servers hosted in the cloud.  I wrote this for my small private server and thought I'd share.

To use this script, go create a Discord Bot through the Discord Developer Portal and give it Admin permissions.  Or go through the script and decide which permissions you want it to have.  I'm pretty sure it just needs ones pertaining to messages.  There is a comment in the script telling you to create a .env file and how to format the token variable.  Save the file in the same folder where you saved this script.


**I'm not great with batch files, so this may not perfect or completely correct.  Use at your own discretion.**

You will need to edit your Valheim Server Startup batch file to allow the bot to launch when the server starts.

    **Make sure to have a saved backup copy of your working Server Startup batch file.**

Just after the "set SteamAppID" line add the following:

    echo "Starting Valheim Discord Bot"
    @echo off
    START "Valheim Discord Bot" /Min "LOCATION OF PYTHON.EXE ON YOUR COMPUTER" "LOCATION OF THIS SCRIPT ON YOUR COMPUTER"

You need the full path to the locations listed.  Copy the path and replace the text between the quotes.  The quotes are important.

Now when you run your server_startup .bat file, it will cause the Discord bot script to run in another terminal window.  When you shut down the server, you will need to manually  shut down this terminal as well, otherwise you will open multiple instances of the bot whenever you restart the server.  Again, not good with batch files, so not sure how to check if the file is already running and close it when the server closes.  I'll have a look into that later.

In discord, if the bot is online this is an indicator to the users whether the server is up.

Be sure to set up your Discord permissions so that only users who play on your locally hosted dedicated server have access to the channel that provides your public IP address.  I chose to restrict this bot to a single text channel.  This channel is view-restricted only to those who have the proper role assigned.  There is a comment in the script that tells you how to get the channel ID and where to put that info.
