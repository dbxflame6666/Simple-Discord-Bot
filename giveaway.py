import discord
from discord.ext import commands
from discord.commands import slash_command
from Views.giveawayModal import GiveawayModal
from Views.giveawayModal import GiveawayEnter

class giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.add_view(GiveawayEnter())


    @slash_command(description='Create a simple Giveaway')
    async def giveaway(self, channel: discord.channel):
        await channel.send_modal(GiveawayModal(title='Giveaway'))


def setup(client):
    client.add_cog(giveaway(client))
