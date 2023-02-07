import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from colorama import Fore

class nick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description="Change a Nickname from a Person")
    @commands.bot_has_permissions(manage_nicknames=True)
    @discord.default_permissions(manage_nicknames=True)
    async def changenick(self, ctx, user: Option(discord.Member, required=True), nickname: Option(str)):
        await user.edit(nick=nickname)
        
        embed = discord.Embed(
            title="Changed Nickname!",
            description=f"{user} will be called {nickname} on {ctx.guild.name}!",
            color=0x4eb1a9
        )

        dm = discord.Embed(
            title=f"Nickname {ctx.guild.name}!",
            description=f"Hey {user} your Nickname on {ctx.guild.name} got changed to {nickname}!",
            color=0x4eb1a9
        )

        await user.send(embed=dm)
        await ctx.respond(embed=embed)

def setup(client):
    client.add_cog(nick(client))
