import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
from Views.TicketButtonsEm import TicketViewButtonEmMSG

options = [
    discord.SelectOption(label="1", description="1!", emoji="<:DBXdiscord:1047271041623392317>", value="1"),
    discord.SelectOption(label="2", description="1!", emoji="<:DBXdiscord:1047271041623392317>", value="2")
]


class Ticket2View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Select a Topic of what you would like to Order",
        options=options,
        custom_id="Ticket2"
    )
    async def select_callback(self, select, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        if "1" in select.values:

            cat = client.get_channel(1234) # Change your Category ID here
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
                            f'`┌›` Type: `1`\n'
                            f'`├›` Requirements: `Please list us a few Requirements so our Staff can do the exact thing you would like to have.`\n'
                            f'`└›` Please be patient and wait for a Staff Member.',
                color=0xcd03e0,
                timestamp=datetime.now()
            )
            await ticket_channel.send(embed=embed3, view=TicketViewButtonEmMSG())



        if "2" in select.values:

            cat = client.get_channel(1234) # Change your Category ID here
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
                            f'`┌›` Type: `2`\n'
                            f'`├›` Requirements: `Please list us a few Requirements so our Staff can do the exact thing you would like to have.`\n'
                            f'`└›` Please be patient and wait for a Staff Member.',
                color=0xcd03e0,
                timestamp=datetime.now()
            )
            await ticket_channel.send(embed=embed3, view=TicketViewButtonEmMSG())

