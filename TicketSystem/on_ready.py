from discord.ext  import commands
from TicketSystem.Views.CloseDropdownMenu import CloseDropdown
from TicketSystem.Views.TicketButtonsEm import TicketViewButtonEmMSG
from TicketSystem.Views.MainTicketView import TicketViewCreateTicket


class on_ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener(
        'on_ready'
    )
    async def listener(
        self
    ):
        self.client.add_view(
            TicketViewCreateTicket()
        )

        self.client.add_view(
            TicketViewButtonEmMSG()
        )

        self.client.add_view(
            CloseDropdown()
        )



def setup(client):
     client.add_cog(on_ready(client))
