import discord
from datetime import datetime
from Views.TicketViews.TicketButtonsEm import TicketViewButtonEmMSG

class PartnerModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="How many members you got?",
                placeholder="How many members you got?",
                style=discord.InputTextStyle.short
            ),
            discord.ui.InputText(
                label="Why do you want to Partner with us?",
                placeholder="...",
                style=discord.InputTextStyle.long
            ),
            discord.ui.InputText(
                label="Is your Server active?",
                placeholder="yes/no",
                style=discord.InputTextStyle.long,
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        cat = client.get_channel(1234) # Add your Category ID here
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
            await ticket_channel.set_permissions(interaction.guild.get_role(1234), send_messages=True, read_messages=True, view_channel=True) # Add your Staffrole ID here
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
                        f'`┌›` Current Members: `{self.children[0].value}`\n'
                        f'`├›` Why do you want to Partner with us?: `{self.children[1].value}`\n'
                        f'`├›` Is your Server active?: `{self.children[2].value}`\n'
                        f'`└›` Please be patient and wait for a Staff Member.',
            color=discord.Color.blurple(),
            timestamp=datetime.now()
        )
        await ticket_channel.send(embed=embed3, view=TicketViewButtonEmMSG())
