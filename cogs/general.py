import discord
from discord.ext import commands
from base import *
from direc import *


db = database()


class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ready')
        a = 0
        for i in self.bot.guilds:
            print(f'run on {i.id} (name: {i.name})')
            a += 1
        print(f'elzelion in {a} guilds')
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Hunter's Despair"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        # cek dm
        elif message.guild is None:
            c = message.author.id
            if str(message.attachments) == '[]':
                return None
            else:
                set_up()
                ck = check_disc(c)
                char = character(ck)
                sp = str(message.attachments).split("filename='")[1]
                filename = str(sp).split("' ")[0]
                ch2 = self.bot.get_channel(int(db.log))
                b = message.author
                oke = []
                space = str(message.attachments).split("url=\'")
                trump = len(space)-1
                proc = [space[i+1] for i in range(trump)]
                for i in range(trump):
                    mer = proc[i]
                    res = str(mer).split("'>")[0]
                    oke.append(res)
                if filename == db.savefile:
                    await message.attachments[0].save(fp=f'{UPLOAD_PATH}\\savedata_{ck}.bin')
                    char.upload_save()
                    await b.send(f'uploaded {char.name} savedata to server')
                    await ch2.send(f'{b} save downloaded')
                elif filename == db.partner:
                    await message.attachments[0].save(fp=f'{UPLOAD_PATH}\\partner_{ck}.bin')
                    await b.send(f'uploaded {char.name} partner data to server')
                    char.upload_part()
                    await ch2.send(f'{b} partner downloaded')


def setup(bot):
    bot.add_cog(GeneralCog(bot))
