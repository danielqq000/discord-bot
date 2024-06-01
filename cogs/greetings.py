###greetings.py
###Made By Daniel Huang
###Last update: 6/1/24


import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        content = message.content.lower()

        if '早安' in content:
            await message.channel.send(f'早安, {message.author.mention}! 祝你有美好的一天!')
        elif '午安' in content:
            await message.channel.send(f'午安, {message.author.mention}! 祝你下午愉快!')
        elif '晚安' in content:
            await message.channel.send(f'晚安, {message.author.mention}! 祝你有個美好的夜晚!')

async def setup(bot: commands.Bot):
    await bot.add_cog(Greetings(bot))
