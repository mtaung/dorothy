import discord
import core
from discord.ext import commands
from utils import config

# Configs
token = config.load('bot').get('token')
bot = commands.Bot(command_prefix='!')

# Cogs
startup_extensions = ["core.fun", "core.xkcd"]
for extension in startup_extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load extension {}\n{}'.format(extension, exc))

# Run
bot.run(token)
