"""
This is just a simple Poll Command and nothing special.
"""


import discord
from datetime import datetime
from discord.ext import commands, tasks
from colorama import Fore
from discord.commands import slash_command, Option


class poll(commands.Cog):

    def __init__(self, client):
        self.client = client


    @slash_command()
    async def poll(self, ctx, *, message: Option(str), choice1: Option(str), choice2: Option(str)):
      if ctx.author.has_permissions.manage_messages:
        await ctx.respond('Poll was created succesfully!', ephemeral=True)

        embed = discord.Embed(
            title=" Abstimmung ",
            description=f"__**{message}**__\n\n\n1️⃣ - {choice1}\n\n2️⃣ - {choice2}",
            color=0x813ecc
        )

        msg = await ctx.channel.send(embed=embed)

        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        
      else:
        await ctx.respond('You dont got permissions for that.')



def setup(client):
    client.add_cog(poll(client))
