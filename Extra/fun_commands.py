import discord  ,  requests  ,  random  ,  asyncio
from discord.ext import commands  ,  bridge


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client


    @bridge.bridge_command() 
    async def ball(self, ctx, *, question):
        ballresponse = [
    "Yes", "No", "Take a wild guess...", "Very doubtful",
    "Sure", "Without a doubt", "Most likely", "Might be possible",
    "You'll be judged", "no... (╯°□°）╯︵ ┻━┻", "no... baka",
    "Please, Please no ;-;", "Who know?", "I don't care", "This tbh", "You too", 
    "Bruh", "(☞ﾟヮﾟ)☞", "ㄟ( ▔, ▔ )ㄏ", "¯\_(ツ)_/¯", "LOL", "lmao", "f*ck you",
    "Uhm, idk?", 'Why you asking me this?', 'im not sure.', 'poggers'
    ]
        answer = random.choice(ballresponse)
        async with ctx.typing():
            await asyncio.sleep(1)
        await ctx.reply(f'Your question was **{question}**\nMy answer is **{answer}**')



    @bridge.bridge_command() 
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def meme(self, ctx):
        response1 = requests.get('https://some-random-api.ml/meme')
        data1 = response1.json()
        embed = discord.Embed(
            title = 'Meme 🤣',
            description = 'Here is a random meme I found',
            color = random.randint(0, 0xFFFFFF)
        )
        embed.set_image(url=data1['image'])
        embed.set_footer(text="")
        async with ctx.typing():
            await asyncio.sleep(1)
            
        await ctx.send(embed=embed)


    @bridge.bridge_command() 
    async def roll(self, message):
        dice = ["1","2","3","4","5","6"]
        number = random.choice(dice)
        async with message.typing():
            await asyncio.sleep(1)

        message0 = await message.reply("I am rolling the dice now")
        await asyncio.sleep(2)
        await message0.edit(content=f"The number is {number}")

    @bridge.bridge_command() 
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def joke(self, ctx):
        response = requests.get('https://some-random-api.ml/joke') 
        data = response.json()
        joke = data['joke']
        embed = discord.Embed(
        title = 'Here is a joke',
        description = joke,
        color = random.randint(0, 0xFFFFFF))
        async with ctx.typing():
            await asyncio.sleep(1)
        await ctx.send(embed=embed)


def setup(client):
     client.add_cog(fun(client))
