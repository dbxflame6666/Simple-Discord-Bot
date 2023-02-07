import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from VerifySystem.Views.verifyModalView import verifyModal


class Buttonintomodal(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(
        label='Next Step',
        style=discord.ButtonStyle.red,
        custom_id='nS'
    )
    async def callback1(self, button, interaction):
        await interaction.response.send_modal(verifyModal(title='Put in the correct code!'))
