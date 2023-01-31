"""
Please dont forget to add your regular Member Role in line 31 !!
"""

import discord
from datetime import datetime
import asyncio
import random


class verifyModal(discord.ui.Modal):

    def __init__(self, *args, **kwargs):
        self.captcha_text = random.randint(100000, 999999)
        super().__init__(
            discord.ui.InputText(
                label=f"Code: {self.captcha_text}",
                placeholder=f"Write the code here: | {self.captcha_text} |",
                style=discord.InputTextStyle.short
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client
        member = interaction.user
        guild = interaction.guild

        if int(self.children[0].value) == self.captcha_text:
            role = discord.utils.get(guild.roles, name='ADD_YOUR_MEMBER_ROLE_HERE_!!')
            await interaction.response.send_message('You succesfully made the Verification!', ephemeral=True)
            await member.add_roles(role)

        else:
            emW = discord.Embed(
                title='This is wrong!',
                description=f'Please retry it and put in the correct Code!',
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=emW, ephemeral=True)
            return
