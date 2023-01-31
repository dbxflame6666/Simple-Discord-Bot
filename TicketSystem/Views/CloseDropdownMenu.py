"""
Dont Forget to Change the CHANNEL IDs for the LOGS (Line 72 and 84 and 113)
"""


import discord
from discord.ext  import commands
from datetime import datetime
import asyncio
import os


class Logger:
    def __init__(
        self,
        channel: discord.TextChannel
    ):
        self.channel = channel

    async def create_log_file(
        self
    ):
        with open(f"Log {self.channel.name}.txt", "w", encoding="utf-8") as f:
            f.write(f'Log of the Ticket "{self.channel.name}"\n')
            f.write("########## START OF THE LOG ##########\n")
            messages = await self.channel.history(limit=69420).flatten()
            for i in reversed(messages):
                f.write(f"{i.created_at}: {i.author}: {i.content}\n")
            f.write("########## END OF THE LOG ##########\n\n")
            if len(messages) >= 69420:
                f.write(
                    f"More than 69420 messages got sent into that channel. Because of Save reasons,"
                    f"only the last 69420 messages got logged.")
            else:
                f.write(f"Message count: {len(messages)}")

    async def send_log_file(
        self,
        channel: discord.TextChannel
    ):
        await channel.send(
            files=[discord.File(f"Log {self.channel.name}.txt", filename=f"{self.channel.name}.txt")]
        )
        os.remove(
            f"Log {self.channel.name}.txt"
        )


options = [
    discord.SelectOption(label="finished", description="Ticket is finished", emoji="<:DBXtick:1047486130066567188>", value="finished"),
    discord.SelectOption(label="User left the Discord", description="If the user left the discord before ticket was finished, choose this", emoji="<:DBX:1047486142544617572>", value="left"),
]


class CloseDropdown(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Select a reason for closing this Ticket",
        options=options,
        custom_id="ReasonDropDown"
    )
    async def select_callback(self, select, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild
        log = client.get_channel(1234)
        if "finished" in select.values:

            em2 = discord.Embed(
                title='Ticket get closed...',
                description=f'3 Seconds until this Ticket will be deleted.',
                color=0x2F3136,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=em2)
            await asyncio.sleep(3)

            modchannel = client.get_channel(1234)
            logger = Logger(interaction.channel)
            await logger.create_log_file()
            await logger.send_log_file(modchannel)

            await interaction.channel.delete()

            logg = discord.Embed(
                title='Ticket was closed!',
                description=f'`┌›` Ticket: `{interaction.channel.name}`\n'
                            f'`├›` Closed by: {member.mention}\n'
                            f'`└›` Reason: `Finished`',
                color=discord.Color.red(),
                timestamp=datetime.now()
            )
            await log.send(embed=logg)


        if "left" in select.values:

            em2 = discord.Embed(
                title='Ticket get closed...',
                description=f'3 Seconds until this Ticket will be deleted.',
                color=0x2F3136,
                timestamp=datetime.now()
            )
            await interaction.response.send_message(embed=em2)
            await asyncio.sleep(3)

            modchannel = client.get_channel(1234)
            logger = Logger(interaction.channel)
            await logger.create_log_file()
            await logger.send_log_file(modchannel)

            await interaction.channel.delete()

            logg = discord.Embed(
                title='Ticket was closed!',
                description=f'`┌›` Ticket: `{interaction.channel.name}`\n'
                            f'`├›` Closed by: {member.mention}\n'
                            f'`└›` Reason: `User left the Discord`',
                color=discord.Color.red(),
                timestamp=datetime.now()
            )
            await log.send(embed=logg)
