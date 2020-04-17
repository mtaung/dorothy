import asyncio, aiohttp, random, re, requests, json
import discord
from discord.ext import commands
from discord.ext.commands import BadArgument
from lxml import html 

class Fun(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def inspire(self, ctx):
        """Grab random inspirobot image from inspirobot.me"""
        async with aiohttp.ClientSession() as session:
            async with session.get('http://inspirobot.me/api?generate=true') as response:
                if(response.status == 200):
                    imgurl = await response.text()
                    embed = discord.Embed(colour=discord.Colour.dark_blue())
                    embed.set_image(url=imgurl)
                    embed.set_footer(text='http://inspirobot.me/')
                    await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def flipcoin(self, ctx):
        """Flip a two sided coin"""
        flip = random.choice([True, False])
        if flip == True:
            msg = 'It\'s heads!'
            await ctx.send(msg)
        elif flip == False:
            msg = 'It\'s tails!'
            await ctx.send(msg)
            
    @commands.command(pass_context=True)
    async def choose(self, ctx, *args):
        """Ask Dorothy to randomly pick from a specified list of options."""
        choicelist = []
        for choice in args:
            choicelist.append(choice)
        result = random.choice(choicelist)
        await ctx.send("Like it or not, I choose {}!".format(result))
            
    @commands.command(pass_context=True)
    async def deal(self, ctx):
        """A dank meme originally written by Dariusz."""
        frames = ['( •_•)', '( •_•)>⌐■-■', '(⌐■_■)', '(⌐■_■) Deal', '(⌐■_■) Deal with', '(⌐■_■) Deal with it.']
        msg = await ctx.send(frames[0])
        for frame in frames[1:]:
            await asyncio.sleep(0.3)
            await msg.edit(content = frame)

    @commands.command(pass_context=True)
    async def bother(self, ctx, user: discord.Member):
        """An abusive command to grab the attention of a user. Please deploy sparingly."""
        for i in range(5):
            msg =  await ctx.send(user.mention)
            await msg.delete()

    @commands.command(pass_context=True)
    async def mal(self,ctx):
        """Quickly search something on MyAnimeList with Zakie's command."""
        anime = ctx.message.content[4:]
        response = requests.get("https://api.jikan.moe/v3/search/anime?q={}".format(anime))
        if response.status_code != 200:
            await ctx.send("Anime not found.")
            return
        response = json.loads(response.content)
        url = response['results'][0]['url']
        await ctx.send(url)
        return

def setup(bot):
    bot.add_cog(Fun(bot))