from discord.ext import commands
from discord.commands import slash_command
import discord

class Sayembed(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command()
    async def sayembed(self, ctx):
      if ctx.author.guild_permissions.manage_messages:
        modal = EmbedSetup(title="Create a Embed")
        await ctx.send_modal(modal)
        
      else:
        await ctx.respond("You dont got permissions to use that Command.")


def setup(client):
    client.add_cog(Sayembed(client))
    
    
    

class EmbedSetup(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Channel ID",
                placeholder="ID from the Channel where the Embed should go in",
                style=discord.InputTextStyle.short,
            ),
            discord.ui.InputText(
                label="Embed Title",
                placeholder="Title"
            ),
            discord.ui.InputText(
                label="Embed Description",
                placeholder="Description",
                style=discord.InputTextStyle.long
            ),
            discord.ui.InputText(
                label="Embed Field 1",
                placeholder="Field 1",
                style=discord.InputTextStyle.long,
                required=False,
            ),
            discord.ui.InputText(
                label="Embed Field 2",
                placeholder="Field 2",
                style=discord.InputTextStyle.long,
                required=False,
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        client = interaction.client
        channel = client.get_channel(self.children[0].value)

        embed = discord.Embed(
            title=self.children[1].value,
            description=f'{self.children[2].value}\n\n{self.children[3].value}\n\n{self.children[4].value}',
            color=0x3398ee
        )
        embed.set_footer(text='Made by dbxflame | Made with ❤️')
        await channel.send(embed=embed)
        await interaction.response.send_message('Send embed!', ephemeral=True)
