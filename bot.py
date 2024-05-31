import discord
from discord.ext import commands
import config

# 初始化機器人
intents = discord.Intents.all()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

# 加載Cogs
initial_extensions = ['cogs.character', 'cogs.adventure']

@bot.event
# 當機器人成功啟動
async def on_ready():
    print(f'成功啟動並登入 --> {bot.user}\n')

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello, {ctx.author.mention}")


# 啟動機器人
bot.run(config.TOKEN)
