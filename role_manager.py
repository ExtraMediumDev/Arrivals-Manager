import sys
import discord
from discord.ext import commands



#something that i apparently have to set to True idk?
intents = discord.Intents.default()
intents.members = True

#bot object thingy idk how objects and classes work shut up
bot = commands.Bot(command_prefix='no prefix',intents=intents)

rulesID = []

#tells me the bot is ready when it is ready
@bot.event
async def on_ready():
    print("Bot is online!")


@bot.event
async def on_member_join(member):
    await member.edit(nick="Stranger " + member.name)


#when a reaction is added to a message
@bot.event
async def on_raw_reaction_add(payload):
    role = discord.utils.get(payload.member.guild.roles, name="Outer Party⭐")
    user = payload.member
    if payload.channel_id == 782030542320828426: await user.add_roles(role)
    channel = bot.get_channel(782030542320828426)
    msg = await channel.fetch_message(payload.message_id)
    await msg.clear_reactions()
    await user.edit(nick="Comrade " + user.name)


#when a message is sent, runs the code below
@bot.event
async def on_message(message):
    pass


#runs the bot
bot.run('YOUR TOKEN HERE')
