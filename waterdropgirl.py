import discord
import random
from random import choice
import bank
from bank import deposit, transfer
import asyncio

@commands.command()
async def hello(self, ctx):
	await ctx.send("Hi I'm beemo, how are you doing?")

@commands.command()
async def goodbye(self, ctx, user: discord.Member):
	await ctx.send(f"Talk to you later {user.mention}(:")

@commands.command()
async def randomtest(self, ctx, user: discord.Member):
	base_msg = ["Hello,", "Hi,", "Hey there,"]
	mid_msg = ["is currently not available right now.", "is out and about and will not be able to reply.", "cannot respond to you at the moment."]
	end_msg = ["Please try again later!", "Try again in a bit"]
	msg = random.choice(base_msg) + " " + user.mention + " Sara " + random.choice(mid_msg) + " " + random.choice(end_msg)
	await ctx.send(msg)


@commands.command()
async def diceroll(self, ctx, sides: int):
	num = random.randint(1, sides)
	await ctx.send("Rolling dice...")
	asyncio.sleep(5)
	await ctx.send(":game_die:" + num)



@commands.command()
async def embedtest(self, ctx):
	string = "This is a field title"
	embed = discord.Embed(title="Test Title", description="This is a test description", color=0x5d43dd)
	embed.add_field(name=string, value="This is a description of the field")
	embed.set_image(url="https://i.imgur.com/DjxXPqg.jpg")
	embed.set_footer(text="This is the footer")
	await ctx.send(embed=embed)
