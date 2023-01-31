"""
Here is a simple and easy Verification System.
Please dont forget to add your Channel IDs below in the Code
AND
Dont forget to add your regular Member role in the File 'verifyModalView', line 30
"""

import discord
from discord.ext  import commands
from discord.commands import slash_command
from datetime import datetime
import asyncio
from Views.VerifyView import VerifyView

class verifymsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description='Owner Command only!')
    async def verifymsg(self, interaction):
      if interaction.user.has_permissions.administrator:
        em = discord.Embed(
            title='dbx Code',
            description=f'Verification\n'
                        '**How to verify?**\n'
                        '> ➥ Click on the Select Menu on the buttom of the Message and\n'
                        '> ➥ click/fill out the right stuff.\n\n'

                        'What to do if this wont work?\n'
                        '> ➥ DM the Owner and ask him for help.\n'
                        '> ➥ He will respond as soon as possible so stay patient!',
            color=discord.Color.blurple()
        )

        verifymsg = self.client.get_channel(1234) # Add your Channel ID here

        await verifymsg.send(embed=em, view=VerifyView())
        await interaction.response.send_message('posted', ephemeral=True)
      else:
        await interaction.response.send_message("You dont got permissions for that Command")

def setup(client):
     client.add_cog(verifymsg(client))
