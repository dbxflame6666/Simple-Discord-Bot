"""
Change your Staff Role Name in Line 42 !
"""

import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from Views.CloseDropdownMenu import CloseDropdown
import os


class TicketViewButtonEmMSG(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(
        label='Close',
        style=discord.ButtonStyle.red,
        custom_id='close'
    )
    async def callback1(self, button, interaction):

        emClose = discord.Embed(
            title='Close Ticket',
            description=f'`┌›` Please select in the following Dropdown menu, why you exactly closing this Ticket.\n'
                        f'`└›` Note: Your @ will be in the Logs.',
            color=0x2F3136
        )
        await interaction.response.send_message(embed=emClose, view=CloseDropdown(), ephemeral=True)


    @discord.ui.button(
        label='Claim',
        style=discord.ButtonStyle.green,
        custom_id="ClaimTicket"
    )
    async def callback(self, button, interaction):
        member = interaction.user
        guild = interaction.guild
        staffRole = discord.utils.get(guild.roles, name='StafRole_Name') # Add your StaffRole Name here
        
        if staffRole in member.roles:
            ClaimEm = discord.Embed(
                title='Ticket was claimed!',
                description=f'`┌›` Hello, i am {member.mention} and __**claimed your Ticket**__\n'
                            f'`├›` I will help you, and answer your __**questions**__\n'
                            f'`└›` Claimers ID: {member.id}',
                color=0x2F3136,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=ClaimEm)
            button.disabled = True
            await interaction.message.edit(view=self)

        else:
            Err = discord.Embed(
                title=f'Error!',
                description=f'`›` You cannot Claim your own Ticket!',
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=Err, ephemeral=True)
