# Develop by NK Development Team
import discord
from discord.ext import commands
import requests
import sys

config = {
    "RemoveServerIcon": True,
    "ChangeServerName": True,
    "DeleteAllChannels": True,
    "DeleteAllRoles": True,
    "DeleteAllEmojis": True,
    "DeleteAllWebhooks": True,
    "DeleteAllInvites": True,
    "RemoveAllBans": True,
    "BanAllMembers": True
}

bot = commands.Bot(command_prefix=".", intents=discord.Intents.All())

def validateToken(token):
    url = "https://discord.com/api/v10/users/@me"
    headers = { "Authorization", f"Bot {token}" }
    response = requests.get(url, headers=headers)
    return response.status_code == 200:

def main():
    bot_token = input("Enter Bot Token >> ")
    if validateToken(bot_token):
        print("[+] Token Validated")
    else:
        print("[!] Cannot login to token.)
        sys.exit(0)
    
