"""
Please dont forget to add your Channel ID in line 17 AND Line 25 !!!
"""

from datetime import datetime
import discord
from discord.ext import commands, tasks


class suggest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @slash_command(aliases=['Suggest'])
    async def suggest(self, ctx, suggestion: Option(str)):
        channel = self.client.get_channel(1234) # Add your Channel ID here

        suggestEmbed = discord.Embed(color=discord.Color.green())
        suggestEmbed.set_author(name=f"Suggested by {ctx.author.name}", icon_url=f'{ctx.author.avatar.url}')
        suggestEmbed.add_field(name='New Suggestion!', value=f"{suggestion}", inline=True)

        message = await channel.send(embed=suggestEmbed)

        await ctx.respond('Suggestion got send succesfully in <#1234>', ephemeral=True) # Add your Channel ID here !

        await message.add_reaction('✔️')
        await message.add_reaction('❌')
        
        SuggestEmbed = discord.Embed(description=f"Hey, {ctx.author.mention}. Your suggestion has been send to {channel.mention} to be voted on!", color=discord.Color.random())
        SuggestEmbed.add_field(name="Note:", value="Suggestions will be checked out every Sunday.", inline=False)
        SuggestEmbed.set_author(name='Guild Name | Suggestions')
        SuggestEmbed.set_footer(text='Code made by dbxFlame')
        await ctx.author.send(embed=SuggestEmbed)


def setup(client):
    client.add_cog(suggest(client))
