import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'your-prefix-goes-here')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

client.run('your-token-goes-here')