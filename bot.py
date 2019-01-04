import discord
from discord.ext import commands
import requests
import time
import json


bot = commands.Bot(command_prefix='%', description="Is [Insert game here] dead yet?!?!", pm_help=True)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')


@bot.command(help='You need to enter the exact name of the game.\nAnd if the name contains more than one word you need to contain them in "".\n\nFor example: "Grand Theft Auto 5"')
async def g(ctx, game: str):
    if game is None:
        await ctx.send("No game passed")

    try:

        data_path = 'data/data.json'

        with open(data_path) as f:
            data = json.load(f)

        gameid = data[game]

        playercounturl = (f'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={gameid}')
        presp = requests.get(playercounturl)
        pcountdata = json.loads(presp.text)

        try:
            playercount = pcountdata['response']['player_count']
            

        except KeyError:
            playercount = pcountdata['response']['result']

        await ctx.send(f"{game} has {playercount} players online.")
    
    except KeyError:
        await ctx.send('You need to enter the exact name of the game.\nAnd if the name contains more than one word you need to contain them in "".\n\nFor example: ```"Grand Theft Auto 5"```')
        
        
        

    




# Get the token from the "token.txt" file
token_path = "token.txt"
with open(token_path, 'r') as token_file:
    token = token_file.readline()
    
bot.run(token)
