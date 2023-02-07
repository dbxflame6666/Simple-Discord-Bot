import discord  ,  asyncio
from discord.ext  import commands  ,  tasks
from discord.commands import slash_command
from datetime import datetime


class tasks(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self): 
        if not self.taskk.is_running():
            self.taskk.start() 



    @tasks.loop(seconds=60)
    async def taskk(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'over {len(self.client.users)} users'))
        await asyncio.sleep(30)
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'Made by dbx'))



def setup(client):
     client.add_cog(tasks(client))
