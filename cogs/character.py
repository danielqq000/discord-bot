import discord
from discord.ext import commands
from utils.db import create_character, get_character

class Character(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx, character_name: str):
        """創建一個新角色"""
        success = create_character(ctx.author.id, character_name)
        if success:
            await ctx.send(f'{ctx.author.mention} 創建了一個新角色: {character_name}！')
        else:
            await ctx.send(f'{ctx.author.mention}, 你已經有一個角色了！')

    @commands.command()
    async def profile(self, ctx):
        """顯示玩家角色的資料"""
        try:
            await ctx.send("profile called")
        except:
            await ctx.send("profile failed")

        character = get_character(ctx.author.id)
        if character:
            profile = (f'角色名: {character["name"]}\n'
                       f'等級: {character["level"]}\n'
                       f'經驗值: {character["experience"]}\n'
                       f'生命值: {character["health"]}\n'
                       f'法力值: {character["mana"]}\n'
                       f'攻擊力: {character["attack"]}\n'
                       f'防禦力: {character["defense"]}\n')
            await ctx.send(profile)
        else:
            await ctx.send(f'{ctx.author.mention}, 你還沒有角色！使用 !start [角色名字] 創建一個角色。')

async def setup(bot):
    await bot.add_cog(Character(bot))
