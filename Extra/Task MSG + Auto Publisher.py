"""
Quick Note:
  This Code is written in a Cog, not main.py !!
  Also, please change your Channel ID in line 27
"""

import discord  ,  asyncio
from discord.ext  import commands  ,  tasks
from discord.commands import slash_command
from datetime import datetime


class task(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
        
    @commands.Cog.listener()
    async def on_ready(self): 
        if not self.TaskName.is_running():
            self.taskk.start() 
            
            
    @tasks.loop(hours=6)
    async def ad(self):
        CHANNELID = self.client.get_channel(123456789) # --------------- HERE YOUR CHANNEL ID!!!!!!!!!! ----------------
        em = discord.Embed(
            title=f'Official __**dbx**__ Code',
            description=
                    "This is a MSG using a Task + Auto Publisher",
            color=discord.Color.green(),
            timestamp=datetime.now()
        )
        msg = await CHANNELID.send( embed=em)
        await msg.publish()
        
        
        
        
def setup(client):
     client.add_cog(task(client))
