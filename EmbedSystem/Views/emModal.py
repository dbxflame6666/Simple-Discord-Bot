import discord

class dbxModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Channel ID",
                placeholder="ID of channel wheret he Embed should be send to",
                style=discord.InputTextStyle.short
            ),
            discord.ui.InputText(
                label="Title",
                placeholder="title",
                style=discord.InputTextStyle.long
            ),
            discord.ui.InputText(
                label="Description",
                placeholder="Description",
                style=discord.InputTextStyle.long
            ),
            discord.ui.InputText(
                label="Field 1",
                placeholder="Add a Field",
                style=discord.InputTextStyle.long,
                required=None
            ),
            discord.ui.InputText(
                label="Field 2",
                placeholder="Add a 2nd Field",
                style=discord.InputTextStyle.long,
                required=None
            ),
            discord.ui.InputText(
                label="Field 3",
                placeholder="Add a 3rd Field",
                style=discord.InputTextStyle.long,
                required=None
            ),
            *args,
             **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client
        channel = client.get_channel(self.children[0].value)
        embed = discord.Embed(
            title=self.children[1].value,
            description=f'{self.children[2].value}\n\n{self.children[3].value}\n\n{self.children[4].value}\n\n{self.children[5].value}',
            color=0x4eb1a9
        )


        await channel.send(embed=embed)
        await interaction.response.send_message(f'Embed was sent to <#{self.children[0].value}>', ephemeral=True)


