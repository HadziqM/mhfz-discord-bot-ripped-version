import discord
from discord.ext import commands
from data import *
from pretty_help import PrettyHelp, DefaultMenu

db = database()


intents = discord.Intents.default()
intents.members = True

menu = DefaultMenu(page_left="◀️", page_right="▶️", remove="❌")
bot = commands.Bot(command_prefix=db.command,
                   intents=intents, help_command=PrettyHelp(color=discord.Colour.teal(), menu=menu))
# ,help_command=None
print('start')

extension = ['cogs.char', 'cogs.server', 'cogs.mod', 'cogs.general']
if __name__ == '__main__':
    for i in extension:
        bot.load_extension(i)

print('confirming token')
bot.run(db.token)
