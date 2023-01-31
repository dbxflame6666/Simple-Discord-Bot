import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from datetime import datetime

class ui(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(description='Shows Informations about a User')
    async def userinfo(self, ctx, user: Option(discord.User, 'The User you wanna get Informations', required=False) = None):
        if user == None:
            user == ctx.author

        userinfo = discord.Embed(
            title=f'Userinfo about {user.name}',
            color=0x813ecc,
            timestamp=datetime.now()
        )

        userinfo.add_field(
            name='General',
            value=f"""
                    > **Member:** {user.name}#{user.discriminator}
                    > **ID:** `{user.id}`
                    > **Mention:** {user.mention}
                    > **Nickname:** `{(user.nick if user.nick else "No Nickname")}`
                    > **Color:** `{user.color}`
                    > **Highest Role:** {user.top_role.mention}
                    """
                    )
        
        userinfo.add_field(
            name='Discord',
            value=f"""
                    > **Account Created at:** {discord.utils.format_dt(user.created_at)}
                    > **Joined Server at:** {discord.utils.format_dt(user.joined_at)}
                    """,
            inline=False
        )

        userinfo.set_thumbnail(url=user.avatar)

        await ctx.respond(embed=userinfo, ephemeral=True)


def setup(client):
    client.add_cog(ui(client))
