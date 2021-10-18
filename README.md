# Valheim-DynamicIP-Server-Discord-Bot
A discord bot that can provide Dynamic IP address information to authorized users in order to Direct Connect to your Valheim locally hosted dedicated server.


**I'm not great with batch files, so this may not perfect or completely correct.  Use at your own discretion.**
I edited my Server Startup batch file to allow the bot to launch when the server starts.

1: Save a backup copy of your Server Startup batch file.
2: Just after the "set SteamAppID" line add the following:

    echo "Starting Valheim Discord Bot"
    @echo off
    START "Valheim Discord Bot" /Min "LOCATION OF PYTHON.EXE ON YOUR COMPUTER" "LOCATION OF THIS SCRIPT ON YOUR COMPUTER"

You need the full path to the locations listed.  Copy the path to in between the quotes.

Running this edited Server Startup batch file will cause the Discord bot script to run.  When you shut down the server, you will need to also shut down the command prompt window that is running the bot script.

In discord, if the bot is online this is an indicator to the users whether the server is up and running.

Be sure to set up your Discord permissions so that only users who play on your locally hosted dedicated server have access to the channel that provides your public IP address.  I chose to restrict this bot to a single text channel.  This channel is view-restricted only to those who have the proper role assigned.
