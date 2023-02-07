import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from VerifySystem.Views.ButtonintoView import Buttonintomodal

Verification = [
    discord.SelectOption(label="Wrong", description="This is wrong", emoji="<:DBXcross:1047486128653078568>", value="wrong"),
    discord.SelectOption(label="Correct", description="Click here to verify", emoji="<:DBXtick:1047486130066567188>", value="right"),
    discord.SelectOption(label="Wrong", description="This is wrong", emoji="<:DBXcross:1047486128653078568>", value="wrong1"),
    discord.SelectOption(label="Wrong", description="This is wrong", emoji="<:DBXcross:1047486128653078568>", value="wrong2"),
    discord.SelectOption(label="Wrong", description="This is wrong", emoji="<:DBXcross:1047486128653078568>", value="wrong3"),
    discord.SelectOption(label="Wrong", description="This is wrong", emoji="<:DBXcross:1047486128653078568>", value="wrong4")
]

class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Click on Correct",
        options=Verification,
        custom_id="Verification"
    )
    async def select_callback(self, select, interaction):

        if 'wrong' in select.values or 'wrong1' in select.values or 'wrong2' in select.values or 'wrong3' in select.values or 'wrong4' in select.values:
            emW = discord.Embed(
                title='This is wrong!',
                description=f'Please retry it and select the Correct Option!',
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=emW, ephemeral=True)
            return


        elif 'right' in select.values:
            emR = discord.Embed(
                title='This is Correct!',
                description=f'Now next step. Write in the Correct numbers.',
                color=discord.Color.green()
            )
            await interaction.response.send_message(embed=emR, view=Buttonintomodal(), ephemeral=True)
