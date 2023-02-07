from discord.ext import commands
from discord.commands import slash_command  ,  Option
import discord  ,  asyncio
from datetime import datetime, timedelta
import asyncio


class unmute(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command()
    async def unmute(self, interaction: discord.Interaction,
        member: Option(discord.User, "Unmutes a specific User", required=True),
    ):
      if interaction.user.guild_permissions.manage_messages:


        await interaction.response.defer()
        await asyncio.sleep(1)

        try:

            em = discord.Embed(
                title=f'unmuted {member.name}!',
                description=f'┌› 〢 Moderator: {interaction.user.mention}'
                            f'├› 〢 Moderator ID: `{interaction.user.id}`'
                            f'├› 〢 In Guild: `{interaction.guild.name}`'
                            f'├› 〢 User: {member.mention}'
                            f'├› 〢 ID: `{member.id}`'
                            f'└› 〢 Action: **Unmute**',
                color=0xdcf1fc,
                timestamp=datetime.now()
            )
            em.set_footer(text="Bot Created by Ƒʉͫcͧкͭιͪηͣ dbxflame#4141")
            await interaction.followup.send(embed=em)
            await member.remove_timeout()

        except:

            em1 = discord.Embed(
                title=f'<:DBXcross:1047486128653078568> Error',
                description=f'I wasnt able to mute {member.mention}. \n`MISSING_PERMISSION`',
                color=discord.Color.red(),
                timestamp=datetime.now()
            )

            await interaction.followup.send(embed=em1, ephemeral=True)
            return

        try:
            em3 = discord.Embed(
                title=f"You've been unmuted!",
                description=f'┌› 〢 Moderator: {interaction.user.mention}'
                            f'├› 〢 Moderator ID: `{interaction.user.id}`'
                            f'├› 〢 In Guild: `{interaction.guild.name}`'
                            f'├› 〢 User: {member.mention}'
                            f'├› 〢 ID: `{member.id}`'
                            f'└› 〢 Action: **Unmute**',
                color=0xdcf1fc
            )
            em3.set_footer(text="Bot Created by Ƒʉͫcͧкͭιͪηͣ dbxflame#4141")
            await member.send(embed=em3)
            return

        except:
            dmE = discord.Embed(
                title=f'<:cross:1055560123709411488> Error',
                description=f'{member.mention} got __unmuted__ but I wasnt able to sent a DM Notification.',
                color=discord.Color.red(),
                timestamp=datetime.now()
            )
            await interaction.followup.send(embed=dmE, ephemeral=True)



def setup(client):
    client.add_cog(unmute(client))
