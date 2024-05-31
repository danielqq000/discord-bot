import discord
from discord.ext import commands
import config

# 初始化機器人
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 加載Cogs
initial_extensions = ['cogs.character', 'cogs.adventure']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# 啟動機器人
bot.run(config.TOKEN)
