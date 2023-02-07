from discord.ext import commands
from discord.commands import slash_command  ,  Option
import discord  ,  asyncio
from datetime import datetime, timedelta
import asyncio


class mute(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command()
    async def mute(self, interaction: discord.Interaction,
        member: Option(discord.User, "Mutes a specific User", required=True),
        minutes: int,
        reason: Option(str, "Adds a Mute Reason", required=True)
    ):
      if interaction.user.guild_permissions.manage_messages:
    
        duration = timedelta(minutes=minutes)

        await interaction.response.defer()
        await asyncio.sleep(1)

        try:
            await member.timeout_for(duration)

            em = discord.Embed(
                title=f'Muted {member.name}!',
                description=f'┌› 〢 Moderator: {interaction.user.mention}\n'
                            f'├› 〢 Moderator ID: `{interaction.user.id}`\n'
                            f'├› 〢 In Guild: `{interaction.guild.name}`\n'
                            f'├› 〢 User: {member.mention}\n'
                            f'├› 〢 ID: `{member.id}`\n'
                            f'├› 〢 Action: **Mute**\n'
                            f'└› 〢 Reason: **{reason}**',
                color=discord.Color.blurple(),
                timestamp=datetime.now()
            )
            em.set_footer(text="Bot Created by Ƒʉͫcͧкͭιͪηͣ dbxflame#4141")
            await interaction.followup.send(embed=em)

        except:

            em1 = discord.Embed(
                title=f'<:DBXcross:1047486128653078568> Error',
                description=f'I wasnt able to mute {member.mention}. \n`MISSING_PERMISSION`',
                color=discord.Color.blurple(),
                timestamp=datetime.now()
            )

            await interaction.followup.send(embed=em1, ephemeral=True)
            return

        try:
            em3 = discord.Embed(
                title=f"You've been Muted!",
                description=f'┌› 〢 Moderator: {interaction.user.mention}\n'
                            f'├› 〢 Moderator ID: `{interaction.user.id}`\n'
                            f'├› 〢 In Guild: `{interaction.guild.name}`\n'
                            f'├› 〢 User: {member.mention}\n'
                            f'├› 〢 ID: `{member.id}`\n'
                            f'├› 〢 Reason: **{reason}**\n'
                            f'└› 〢 Action: **Mute**',
                color=discord.Color.blurple()
            )
            em3.set_footer(text="Bot Created by Ƒʉͫcͧкͭιͪηͣ dbxflame#4141")
            await member.send(embed=em3)
            return

        except:
            dmE = discord.Embed(
                title=f'<:DBXcross:1047486128653078568> Error',
                description=f'{member.mention} got __muted__ but I wasnt able to sent a DM Notification.',
                color=0xee00e3,
                timestamp=datetime.now()
            )
            await interaction.followup.send(embed=dmE, ephemeral=True)



def setup(client):
    client.add_cog(mute(client))
