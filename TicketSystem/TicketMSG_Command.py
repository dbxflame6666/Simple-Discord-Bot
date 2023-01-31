import discord
from discord.ext  import commands
from discord.commands import slash_command
from datetime import datetime
import asyncio
from Views.MainTicketView import TicketViewCreateTicket

class TicketMSG(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(description='Sends the Ticket Menu')
    async def ticketmsg(self, interaction):
      if interaction.user.has_permissions.administrator:
        em = discord.Embed(
            title='dbx Code',
            description=f'Ticket Rules\n'
                        '> Useless creating of Tickets will be fined\n'
                        '> Be patient'
                        '> Do not ping Staff Members\n\n'

                        'Ticket Categories\n'
                        '**Test Ticket**\n'
                        '> ➥ ...\n'
,
            color=discord.Color.blurple()
        )

        ticketmsg = self.client.get_channel(1234) # Add your Channel ID here

        await ticketmsg.send(embed=em, view=TicketViewCreateTicket())
        await interaction.response.send_message('posted', ephemeral=True)
      else:
        await interaction.response.send_message('You dont got permissions for that.')

def setup(client):
     client.add_cog(TicketMSG(client))
