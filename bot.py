"""
bot.py
Made By Daniel Huang
Last update: 6/1/24
"""

import os
import asyncio
import discord
from discord.ext import commands
import config


# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "!", intents = intents)

# 當機器人完成啟動
@bot.event
async def on_ready():
    print(f"成功啟動,目前登入身份 --> {bot.user}")

# 載入指令程式檔
@bot.command()
async def load(ctx, extension):
    print(f"load called")
    try:
        await bot.load_extension(f"cogs.{extension}")
    except:
        await ctx.send(f"Load {extension} failed.")
    else:
        await ctx.send(f"Load {extension} done.")

# 卸載指令程式檔
@bot.command()
async def unload(ctx, extension):
    print(f"unload called")
    try:
        await bot.unload_extension(f"cogs.{extension}")
    except:
        await ctx.send(f"Unload {extension} failed.")
    else:
        await ctx.send(f"Unload {extension} done.")

# 更新指令程式檔
@bot.command()
async def reload(ctx, extension):
    print(f"reload called")
    try:
        await bot.reload_extension(f"cogs.{extension}")
    except:
        await ctx.send(f"Reload {extension} failed.")
    else:
        await ctx.send(f"Reload {extension} done.")

# initial load
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

# main
async def main():
    await load_extensions()
    await bot.start(config.TOKEN)

if __name__ == "__main__":
    asyncio.run(main())


