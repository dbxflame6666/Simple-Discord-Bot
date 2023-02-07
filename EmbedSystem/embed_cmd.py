from discord.ext import commands
from discord.commands import slash_command
from EmbedSystem.Views.embuilder import dbxModal

class Sayembed(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command()
    async def embed(self, ctx):
        modal = dbxModal(title="Create an Embed")
        await ctx.send_modal(modal)


def setup(client):
    client.add_cog(Sayembed(client))
