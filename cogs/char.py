import discord
from discord.ext import commands
from direc import *
from base import *

icon1 = ['\\GS.png', '\\HS.png', '\\H.png', '\\L.png', '\\SS.png', '\\LB.png', '\\DS.png',
         '\\LS.png', '\\HH.png', '\\GL.png', '\\B.png', '\\T.png', '\\SAF.png', '\\MS.png']
icon = [ICON_PATH+icon1[i] for i in range(len(icon1))]


async def mcard(bot, ctx, arg):
    set_up()
    type(arg)
    char = character(arg)
    a = char.name
    if a == None:
        return None
    b = char.uid
    c = char.username
    d = char.guild
    e = char.gid
    f = char.gender
    g = char.hrp
    h = char.gr
    i = char.login
    embed = discord.Embed(title=a, color=discord.Color.blue())
    if char.discord != None:
        user = await bot.fetch_user(int(char.discord))
        embed.set_author(name=user.display_name, icon_url=user.avatar_url)
    else:
        None
    file = discord.File(icon[char.weapon], filename='wep.png')
    embed.set_thumbnail(url='attachment://wep.png')
    embed.add_field(
        name='Account', value=f'Username : {c}\nUser ID : {b}\nLast Login : <t:{i}:R>', inline=False)
    embed.add_field(
        name='Character', value=f'Gender : {f}\nHunter Rank : {g}\nGold Rank : {h}', inline=False)
    embed.add_field(
        name='Guild', value=f'Name : {d}\nGuild ID : {e}', inline=False)
    await ctx.channel.send(file=file, embed=embed)


async def mcur(bot, ctx, arg):
    set_up()
    char = character(arg)
    a = char.gcp
    b = char.prem
    c = char.trial
    d = char.netcafe
    e = char.frontier
    f = char.kouryou
    embed = discord.Embed(title=f"{char.name}\'s currencies",
                          description=f'GCPoint : {a}\nPremium coin : {b}\ntrial coin : {c}\nnetcafe point : {d}\nfrontier point : {e}\nkouryou point : {f}', color=discord.Color.red())
    if char.discord != None:
        user = await bot.fetch_user(int(char.discord))
        embed.set_author(name=user.display_name, icon_url=user.avatar_url)
    else:
        None
    await ctx.channel.send(content=None, embed=embed)


async def mboost(bot, ctx, arg):
    set_up()
    char = character(arg)
    a = char.boost()
    b = []
    e = char.name
    for i in range(len(a)):
        if a[i] == 1:
            b.append('cooldown')
        elif a[i] == 0:
            b.append('available')
        else:
            b.append('active')
    embed = discord.Embed(title=e+'''\'s'''+' Login Boost',
                          color=discord.Color.blue())
    if char.discord != None:
        user = await bot.fetch_user(int(char.discord))
        embed.set_author(name=user.display_name, icon_url=user.avatar_url)
    else:
        None
    for i in range(len(b)):
        embed.add_field(name='Week '+str(i+1), value=b[i], inline=False)
    await ctx.channel.send(content=None, embed=embed)


class MHFZ_User_Interactive(commands.Cog):
    """ all the command needed to connect to your Mhfz game """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def id(self, ctx, arg):
        set_up()
        a = char_id(arg)
        await ctx.send(a)

    @commands.command()
    async def card(self, ctx, arg):
        try:
            int(arg)
        except:
            did = int(arg[2:-1])
            set_up()
            arg = check_disc(did)
        await mcard(self.bot, ctx, arg)

    @commands.command()
    async def mycard(self, ctx):
        a = ctx.message.author.id
        set_up()
        try:
            arg = check_disc(a)
        except:
            await ctx.send("you are not registered")
            return
        await mcard(self.bot, ctx, arg)

    @commands.command()
    async def currency(self, ctx, arg):
        try:
            int(arg)
        except:
            did = int(arg[2:-1])
            set_up()
            arg = check_disc(did)
        await mcur(self.bot, ctx, arg)

    @commands.command()
    async def mycurrency(self, ctx):
        a = ctx.message.author.id
        set_up()
        try:
            arg = check_disc(a)
        except:
            await ctx.send("you are not registered")
            return
        await mcur(self.bot, ctx, arg)

    @commands.command()
    async def myboost(self, ctx):
        a = ctx.message.author.id
        set_up()
        try:
            arg = check_disc(a)
        except:
            await ctx.send("you are not registered")
            return
        await mboost(self.bot, ctx, arg)

    @commands.command()
    async def transmog(self, ctx):
        a = ctx.message.author.id
        set_up()
        try:
            arg = check_disc(a)
        except:
            await ctx.send("you are not registered")
            return
        char = character(arg)
        char.mog()
        await ctx.send(f"{char.name} transmog is all unlocked")

    @commands.command()
    async def boost(self, ctx, arg):
        try:
            int(arg)
        except:
            did = int(arg[2:-1])
            set_up()
            arg = check_disc(did)
        await mboost(self.bot, ctx, arg)

    @commands.command()
    async def myboost_off(self, ctx):
        a = ctx.message.author.id
        set_up()
        arg = check_disc(a)
        char = character(arg)
        char.boost_off()
        await ctx.channel.send(f"turn off {char.name} boost")

    @commands.command()
    async def myboost_on(self, ctx):
        a = ctx.message.author.id
        set_up()
        arg = check_disc(a)
        char = character(arg)
        char.boost_on()
        await ctx.channel.send(f"turn on {char.name} boost")

    @commands.command()
    async def join_guild(self, ctx, arg1):
        a = ctx.message.author.id
        set_up()
        try:
            int(arg1)
        except:
            arg1 = guild_check(arg1)
        arg = check_disc(a)
        char = character(arg)
        mod = moderator()
        if mod.guild_mem(arg1) >= 60:
            await ctx.channel.send(f"Guild already overloaded")
            return
        char.join_guild(arg1)
        await ctx.channel.send(f"{char.name} joined a guild")

    @commands.command()
    async def transfer_guild(self, ctx, arg1):
        a = ctx.message.author.id
        set_up()
        arg = check_disc(a)
        char = character(arg)
        char.transfer_guild(arg1)
        await ctx.channel.send(f"{char.name} transfered")

    @commands.command()
    async def mysave(self, ctx):
        a = ctx.message.author.id
        set_up()
        arg = check_disc(a)
        char = character(arg)
        char.download_file()
        user = await self.bot.fetch_user(int(char.discord))
        await user.send(f"downloading {char.name} savedata")
        await user.send(file=discord.File(f'{SAVE_PATH}\\savedata_{char.cid}.bin'))
        await user.send(f"downloading {char.name} partner data")
        await user.send(file=discord.File(f'{SAVE_PATH}\\partner_{char.cid}.bin'))
        await ctx.channel.send("dm'd")

    @commands.command()
    async def register(self, ctx, arg, arg1):
        bot = self.bot
        a = ctx.message.author.id
        set_up()
        char = character(arg)
        if char.discord != None:
            await ctx.channel.send("character already owned")
            return
        try:
            b = check_disc(a)
            await ctx.channel.send(f"you have own {b}")
            return
        except:
            None
        if arg1 == 'm' or arg1 == 'f':
            None
        else:
            await ctx.channel.send("invalid gender")
            return
        await ctx.channel.send('is this your charachter?\nReply with (y/n)\nwait a minute if embeded did not shown yet')
        await mcard(self.bot, ctx, arg)

        def check(author):
            def inner_check(message):
                if message.author != author:
                    return False
                else:
                    if message.content == 'y' or message.content == 'Y' or message.content == 'n':
                        return True
            return inner_check
        msg = await bot.wait_for('message', check=check(ctx.author), timeout=120)
        if 'n' in msg.content.lower():
            return await ctx.send("aborted")
        role = await ctx.guild.create_role(name=f'ID:{arg}')
        await ctx.author.add_roles(role)
        char.add_data(a, arg1)
        await ctx.channel.send('now you are registered')


def setup(bot):
    bot.add_cog(MHFZ_User_Interactive(bot))
