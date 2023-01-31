from discord.ext import commands
from discord.ext.commands import MissingPermissions, CommandNotFound, BotMissingPermissions, MissingRequiredArgument
import discord

class errorCatch(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, CommandNotFound):
            return await ctx.send(f"{ctx.author.mention} this isnt a Command by me.")
            
        elif isinstance(error, BotMissingPermissions):
            missing = ", ".join(error.missing_perms)
            return await ctx.send(f"{ctx.author.mention} I need the `{missing}` permission(s) to run this command.")
        elif isinstance(error, MissingPermissions):
            missing = ", ".join(error.missing_perms)
            return await ctx.send(f"{ctx.author.mention} You need the `{missing}` permission(s) to run this command.")
        elif isinstance(error, MissingRequiredArgument):
            return await ctx.send(f"{ctx.author.mention} Required argument is missed!\nUse this model : `{self.client.command_prefix}{ctx.command.name} {ctx.command.usage}`")
        else:
            em = discord.Embed(title=f'Error', description='Bot got occured a Code Error. Please report it to the Developer on my official Support Server.\n\n[Support Server](https://discord.gg/9Bt7U6kGKP)', color=discord.Color.red())
            await ctx.send(embed=em)
            print(error)
            


def setup(client):
    client.add_cog(errorCatch(client))
