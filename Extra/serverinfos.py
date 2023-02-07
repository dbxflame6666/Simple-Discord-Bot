import discord
from datetime import datetime
from discord.ext import commands, tasks
from colorama import Fore
from discord.commands import slash_command, Option


class serverInfos(commands.Cog):

    def __init__(self, client):
        self.client = client

    @slash_command(description='Check Server Infos')
    async def serverinfos(self,ctx):
        serverinfo = discord.Embed(
            title=f'Serverinfo about {ctx.guild.name}',
            color=0xdcf1fc,
            timestamp=datetime.now()
        )
        serverinfo.add_field(
            name='General',
            value=f"""
> **Member:** {ctx.guild.member_count}
> **ID:** `{ctx.guild.id}`
> **Guild-Name:** {ctx.guild.name}
                    """
                    )
        
        serverinfo.add_field(
            name='Discord',
            value=f"""
> **Server Created at:** {discord.utils.format_dt(ctx.guild.created_at)}
                    """,
            inline=False
        )

        serverinfo.set_thumbnail(url=ctx.guild.icon)

        await ctx.respond(embed=serverinfo, ephemeral=True)




def setup(client):
    client.add_cog(serverInfos(client))
