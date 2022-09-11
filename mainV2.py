import discord
import asyncio
from discord.ext import commands
from data import *
from pretty_help import PrettyHelp, DefaultMenu

db = database()


intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

menu = DefaultMenu(page_left="◀️", page_right="▶️", remove="❌")
bot = commands.Bot(command_prefix=db.command,
                   intents=intents, help_command=PrettyHelp(color=discord.Colour.teal(), menu=menu))
# ,help_command=None
print('start')

extension = ['cogs.char', 'cogs.server', 'cogs.mod', 'cogs.general']


async def start(bot, extension):
    for i in extension:
        await bot.load_extension(i)
        print('confirming token')
        await bot.start(db.token)
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start(bot, extension))
