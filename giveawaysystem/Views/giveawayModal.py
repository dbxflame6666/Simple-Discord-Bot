import discord
import datetime
from datetime import datetime, timedelta
import random
import json
import os
import asyncio

custom_id = random.randint(1, 1000000)



class GiveawayModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Duration",
                placeholder="e.g.: 10m"
            ),
            discord.ui.InputText(
                label="Price",
                placeholder="The price the winner should get",
                style=discord.InputTextStyle.long
            ),
            discord.ui.InputText(
                label="Winner amount",
                placeholder="How many wwinners should be there?",
                style=discord.InputTextStyle.short
            ),
            discord.ui.InputText(
                label="Description",
                placeholder="Descripe your giveaway !",
                style=discord.InputTextStyle.long,
                required=False,
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client

        if 's' in self.children[0].value:
            MDelta = self.children[0].value.replace('s', '')
            DeltaM = datetime.now() + timedelta(seconds=int(MDelta))
            time = discord.utils.format_dt(DeltaM, 'R')
            time2 = discord.utils.format_dt(DeltaM)
            timestamp = datetime.now() + timedelta(seconds=int(MDelta))
            asy = int(MDelta)

        elif 'm' in self.children[0].value:
            MDelta = self.children[0].value.replace('m', '')
            DeltaM = datetime.now() + timedelta(minutes=int(MDelta))
            time = discord.utils.format_dt(DeltaM, 'R')
            time2 = discord.utils.format_dt(DeltaM)
            timestamp = datetime.now() + timedelta(minutes=int(MDelta))
            asy = int(MDelta)*60

        elif 'h' in self.children[0].value:
            MDelta = self.children[0].value.replace('h', '')
            DeltaM = datetime.now() + timedelta(hours=int(MDelta))
            time = discord.utils.format_dt(DeltaM, 'R')
            time2 = discord.utils.format_dt(DeltaM)
            timestamp = datetime.now() + timedelta(hours=int(MDelta))
            asy = int(MDelta)*3600

        elif 'd' in self.children[0].value:
            MDelta = self.children[0].value.replace('d', '')
            DeltaM = datetime.now() + timedelta(days=int(MDelta))
            time = discord.utils.format_dt(DeltaM, 'R')
            time2 = discord.utils.format_dt(DeltaM)
            timestamp = datetime.now() + timedelta(days=int(MDelta))
            asy = int(MDelta)*3600*24


        embed = discord.Embed(
            title=f'🎉 `{self.children[1].value}` 🎉',
            description=f"""
{self.children[3].value}

× **{self.children[2].value}** Winner
× **Ends:** {time}  |  {time2}
× **Created by:** {interaction.user.mention}
                        """,
            color=0xf7a1ff,
            timestamp=timestamp
        )
        embed.set_footer(text="Bot created by dbxFlame")

        my_msg = await interaction.response.send_message(embed=embed, view=GiveawayEnter())

        giveaway = await my_msg.original_response()
        new_msg = client.get_message(giveaway.id)

        await asyncio.sleep(int(asy))

        winners_number = int(self.children[2].value)
        users = []


        with open(f"giveaway_users/{custom_id}.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                users.append(stripped_line)

        winners = random.sample(users, int(winners_number))
        
        Winner = ''

        for w in winners:

            Winner += f'<@{w}>  '


        embed2 = discord.Embed(
            title=f'<a:DBXTada:1050422319392243722> **|** Giveaway ended!',
            description=f"""
`You to late.`

**Price:** 🎉 `{self.children[1].value}` 🎉

× **Winner:** {Winner}
× **Ended:** {time}  |  {time2}
× **Created by:** {interaction.user.mention}
                        """,
            color=0xf7a1ff,
            timestamp=timestamp
        )
        embed2.set_footer(text="Code made by dbxFlame")


        await new_msg.edit(f'<a:DBXTada:1050422319392243722> **|** {Winner}won the giveaway', embed=embed2, view=None)
        await interaction.followup.send(f'<a:DBXTada:1050422319392243722> **|** {Winner}won the giveaway!\n\nCreate a `Support` Ticket to claim your reward !', embed=embed2, view=None)
        os.remove(f"giveaway_users/{custom_id}.txt")
        


giveaway_users = []

class GiveawayEnter(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(
        label='Enter', custom_id=str(custom_id), style=discord.ButtonStyle.gray, emoji="<:FU_TaDa:1048674955736391690>"
    )
    async def callback(self, button: discord.Button, interaction: discord.Interaction):
        member = interaction.user
        giveaway_users = []

        if os.path.exists(f"giveaway_users/{custom_id}.txt"):
            pass

        else:
            open(f"giveaway_users/{custom_id}.txt", "x")
            pass
        

        with open(f"giveaway_users/{custom_id}.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                giveaway_users.append(stripped_line)


        if str(member.id) not in giveaway_users:
            await interaction.response.send_message("You **succesfully** joined the giveaway!", ephemeral=True)
            a = member.id
            with open(f'giveaway_users/{custom_id}.txt', 'a') as file:
                file.write(f'{str(a)}\n')


        else:
            await interaction.response.send_message("You **already** joined the giveaway!", ephemeral=True)
