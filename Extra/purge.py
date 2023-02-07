from discord.ext import commands
from discord.commands import slash_command  ,  Option
import discord



class purge(commands.Cog):

    def __init__(self, client):
        self.client = client

    @slash_command(description='Deletes an amount of Messages')
    @discord.default_permissions(manage_messages=True)
    async def purge(self, ctx, amount: Option(int)):

        deleted = await ctx.channel.purge(limit=amount)
        await ctx.respond('`Succesfully Cleared {} Message(s)`'.format(len(deleted)), delete_after=3)



def setup(client):
     client.add_cog(purge(client))
