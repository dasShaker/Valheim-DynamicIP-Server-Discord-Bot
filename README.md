# Valheim-DynamicIP-Server-Discord-Bot
A discord bot that can provide Dynamic IP address information to authorized users in order to Direct Connect to your Valheim locally hosted dedicated server.  This is not meant for paid dedicated servers hosted in the cloud.  I made this for my small group and thought I'd share.


**I'm not great with batch files, so this may not perfect or completely correct.  Use at your own discretion.**
I edited my Server Startup batch file to allow the bot to launch when the server starts.

1: Save a backup copy of your Server Startup batch file.
2: Just after the "set SteamAppID" line add the following:

    echo "Starting Valheim Discord Bot"
    @echo off
    START "Valheim Discord Bot" /Min "LOCATION OF PYTHON.EXE ON YOUR COMPUTER" "LOCATION OF THIS SCRIPT ON YOUR COMPUTER"

You need the full path to the locations listed.  Copy the path and replace the text between the quotes.  The quotes are important.  The bot script should go in your dedicated server folder to make it easy to find.

Running this edited Server Startup batch file will cause the Discord bot script to run.  When you shut down the server, you will need to also shut down the command prompt window that is running the bot script.  If you are just restarting the server it may call a second instance of the bot if the script isn't closed first.  Again, not good with batch files so not sure how to check if the file is already running.

In discord, if the bot is online this is an indicator to the users whether the server is up.

Be sure to set up your Discord permissions so that only users who play on your locally hosted dedicated server have access to the channel that provides your public IP address.  I chose to restrict this bot to a single text channel.  This channel is view-restricted only to those who have the proper role assigned.
