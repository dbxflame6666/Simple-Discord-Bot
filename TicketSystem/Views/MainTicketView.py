
"""
Please Check the Code twice and check if you changed ALL ID's you have to Change
e.g.: Role IDs (e.g. Line 59) || Category IDs, where do you want to create the Tickets (e.g. Line 42)

Also, dont forget to Change the Role IDs, Category IDs in the Other Files !


All Codes were made by dbxFlame.
"""

import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from TicketSystem.Views.Ticket2 import Ticket2View
from TicketSystem.Views.Ticket3 import PartnerModal
from TicketSystem.Views.TicketButtonsEm import TicketViewButtonEmMSG


TicketOptionss = [
    discord.SelectOption(label="Ticket 1", description="Ticket 1-Ticket: ...", emoji="<:DBX:1047486135930200084>", value="Ticket1"),
    discord.SelectOption(label="Ticket 2", description="Ticket 2-Ticket: ...", emoji="<:DBX:1047486135930200084>", value="Ticket2"),
    discord.SelectOption(label="Ticket 3", description="Ticket 3-Ticket: ...", emoji="<:DBX:1047486135930200084>", value="Ticket3"),
]

class TicketViewCreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Select a Topic",
        options=TicketOptionss,
        custom_id="CreateTicket"
    )
    async def select_callback(self, select, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        if 'Ticket1' in select.values:
            cat = client.get_channel(1234) # Change your CATEGORY ID here
            ticket_channel = await interaction.guild.create_text_channel(
                f'ticket-{interaction.user}',
                topic=f'Ticket by {interaction.user}\nClient-ID: {interaction.user.id}',
                category=cat
            )

            try:
                embed1 = discord.Embed(
                    description=f'Ticket is getting created...',
                    color=discord.Color.green()
                )
                t = await interaction.response.send_message(embed=embed1, ephemeral=True)

                msg = await t.original_response()

                await ticket_channel.set_permissions(interaction.user, send_messages=True, read_messages=True, view_channel=True)
                await ticket_channel.set_permissions(interaction.guild.get_role(1234), send_messages=True, read_messages=True, view_channel=True) # Change your Staff Role ID here
                await ticket_channel.set_permissions(interaction.guild.default_role, view_channel=False)

                embed2 = discord.Embed(
                    title='📬 Ticket was created!',
                    description=f'`┌›` Your Ticket: {ticket_channel.mention}\n'
                                f'`└›` Ticket Owner: {member.mention}',
                    color=0xcd03e0,
                    timestamp=datetime.now()
                )
                await interaction.followup.edit_message(embed=embed2, message_id=msg.id)

            except:
                em1E = discord.Embed(
                    title='📬 Error!',
                    description=f'{member.mention}, I had a issues while creating your Ticket, report this to the Owner/Founder asap !',
                    color=discord.Color.red(),
                    timestamp=datetime.now()
                )
                await interaction.response.send_message(embed=em1E, ephemeral=True)
                return

            embed3 = discord.Embed(
                title=f'Ticket-{member.name}',
                description=f'Here is your Ticket, {member.mention}\n'
                            f'To Begin, please fill out the following questions:\n'
                            f'`┌›` Why did you create this Ticket?\n'
                            f'`├›` Is there (if needed) proof for that?\n'
                            f'`└›` Please be patient and wait for a Staff Member.',
                color=discord.Color.blurple(),
                timestamp=datetime.now()
            )
            await ticket_channel.send(embed=embed3, view=TicketViewButtonEmMSG())



        if 'Ticket2' in select.values:
            em2 = discord.Embed(
                title='Ticket 2',
                description=f'This is a Ticket Selection with a extra Dropdown.',
                color=0x2F3136,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=em2, view=Ticket2View(), ephemeral=True)



        if 'Ticket3' in select.values:

            em = discord.Embed(
                title='Ticket 3',
                description=f'This is a example of a Partner Request/Modal.'
            )

            await interaction.response.send_modal(PartnerModal(title='e.g. Partner Modal'))

