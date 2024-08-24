# main.py

import discord
from discord.ext import commands, tasks
import requests
import os

# Enable necessary intents
intents = discord.Intents.default()
intents.members = True  # Enable the Server Members Intent
intents.message_content = True  # Enable Message Content Intent if needed

# Initialize the bot with the command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Replace with your Discord bot token
DISCORD_TOKEN = 'your-bot-token-here'  # Replace with your actual token

# Define the Minecraft server IP
MINECRAFT_SERVER_IP = "Your-servers-IP"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    update_status.start()  # Start the task to update status

@tasks.loop(seconds=60)
async def update_status():
    """Periodically updates the bot's status with the number of players online."""
    url = f"https://api.mcsrvstat.us/2/{MINECRAFT_SERVER_IP}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["online"]:
            current_players = data["players"]["online"]
            max_players = data["players"]["max"]
            status_message = f'{current_players}/{max_players} on Minecraft'
        else:
            status_message = "Server Offline"
            
        # Set the bot's status
        await bot.change_presence(activity=discord.Game(name=status_message))
    except Exception as e:
        print(f"An error occurred: {e}")

# Start the bot
bot.run(DISCORD_TOKEN)
