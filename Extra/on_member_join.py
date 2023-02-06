"""
Change the Channel names in line 23/24 and the channel ID in line 25
"""

import discord
import json
import asyncio
from datetime import datetime
import time
import random
from discord.ext import commands, tasks


class onMemberJoin(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        for channel in member.guild.channels:
            if channel.name.startswith('Channel Name -'):  # Change this !
                await channel.edit(name=f'Channel Name - {member.guild.member_count}')   # Change this !
        Welcome = self.client.get_channel(1234) # Change this Channel ID to the Welcome Channel where you want to send a message !
        WelcomeEmbed = discord.Embed(
            title=f"Welcome and Hello",
            description=f"`>` {member.mention}\n**Thanks for joining !**\n**Verify yourself and read our Rules**\n**You got Questions? Ask Us!**\n\n**Good Luck and Have fun!**",
            color=0x3398ee,
            timestamp=datetime.now()
        )
        WelcomeEmbed.set_thumbnail(url="url") # Add a URL here for a Banner
        WelcomeEmbed.set_footer(text="Created by dbxflame")
        await Welcome.send(embed=WelcomeEmbed)



def setup(client):
     client.add_cog(onMemberJoin(client))
