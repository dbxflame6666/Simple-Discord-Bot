import discord  ,  aiosqlite
from discord.ext import commands  ,  bridge
from datetime import datetime

class Balance(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.DB = "fun.db"


    async def check_user(self, user_id):
        async with aiosqlite.connect(self.DB) as db:
            await db.execute("INSERT OR IGNORE INTO economy (user_id) VALUES (?)", (user_id,))
            await db.commit()

    async def get_cash(self, user_id):
        await self.check_user( user_id)
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute("SELECT cash FROM economy WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()

        return result[0]

    async def get_bank(self, user_id):
        await self.check_user( user_id)
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute("SELECT bank FROM economy WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()

        return result[0]


    @bridge.bridge_command(
        name='balance',
        description='Shows your Current Balance',
        aliases=['bal']
        )
    async def balance(self, ctx):
        eco = discord.utils.get(self.client.emojis, name='economye')

        cash = await self.get_cash(ctx.author.id)
        bank = await self.get_bank(ctx.author.id)
        total = await self.get_bank(ctx.author.id) + await self.get_cash(ctx.author.id)

        em = discord.Embed(
            color=discord.Color.green(),
            timestamp=datetime.now()
        )
        em.add_field(
            name='Cash:',
            value=f' {eco} {cash:,}'
        )
        em.add_field(
            name='Bank:',
            value=f' {eco} {bank:,}'
        )
        em.add_field(
            name='Total:',
            value=f'{eco} {total:,}'
        )
        em.set_author(name=f"{ctx.author.name}'s Balance", icon_url=f'{ctx.author.avatar}')

        await ctx.respond(embed=em)


def setup(client):
    client.add_cog(Balance(client))
