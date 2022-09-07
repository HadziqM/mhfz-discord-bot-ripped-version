import random
from discord.ext import commands
from discord.utils import get
from direc import *
from base import *

main = database()
mod_id = int(main.mod)


class Mod_Only_Command(commands.Cog):
    """ only specified role can use this command """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(mod_id)
    async def upload(self, ctx, arg):
        try:
            int(arg)
        except:
            did = int(arg[2:-1])
            set_up()
            arg = check_disc(did)
        char = character(arg)
        char.upload_save()
        char.upload_part()
        await ctx.channel.send(f'uploaded ID:{arg} file to server')

    @commands.command()
    @commands.has_role(mod_id)
    async def add_gcp(self, ctx, arg, arg2):
        try:
            int(arg)
        except:
            did = int(arg[2:-1])
            set_up()
            arg = check_disc(did)
        char = character(arg)
        char.add_gcp(int(arg2))
        await ctx.channel.send(f'{char.name} added gcp by {arg2}')

    @commands.command()
    @commands.has_role(mod_id)
    async def add_gcp_all(self, ctx, arg):
        set_up()
        mod = moderator()
        mod.gcp_add(int(arg))
        await ctx.channel.send(f'sended {arg} gcp to all player')

    @commands.command()
    @commands.has_role(mod_id)
    async def transmog_all(self, ctx):
        set_up()
        mod = moderator()
        mod.mog_all()
        await ctx.channel.send('sended all transmog to all player')

    @commands.command()
    @commands.has_role(mod_id)
    async def unreg(self, ctx, arg):
        set_up()
        try:
            a = int(arg[2:-1])
        except:
            char = character(arg)
            a = char.discord
        try:
            arg = check_disc(a)
        except:
            await ctx.send("you are not registered")
            return
        char = character(arg)
        user = await ctx.guild.fetch_member(char.discord)
        role = get(user.guild.roles, name=f'ID:{arg}')
        await user.remove_roles(role)
        char.unreg()
        await role.delete()
        await ctx.channel.send('success')

    @commands.command()
    @commands.has_role(mod_id)
    async def f_reg(self, ctx, arg, arg2, arg1):
        arg2 = int(arg2)
        did = int(arg[2:-1])
        set_up()
        char = character(arg2)
        user = await ctx.guild.fetch_member(did)
        role = await ctx.guild.create_role(name=f'ID:{arg2}')
        await user.add_roles(role)
        char.add_data(did, arg1)
        await ctx.channel.send(f'now {user} are registered to {char.name}')

    @commands.command()
    @commands.has_role(mod_id)
    async def ravi_restart(self, ctx):
        set_up()
        mod = moderator()
        mod.rav_trunc()
        await ctx.channel.send('cleared ravi table')

    @commands.command()
    @commands.has_role(mod_id)
    async def random_move(self, ctx, arg, arg1, arg2):
        set_up()
        try:
            int(arg1)
            int(arg2)
        except:
            arg1 = guild_check(arg1)
            arg2 = guild_check(arg2)
        mod = moderator()
        a = mod.guild_mem_id(arg1)
        try:
            a.remove(mod.leader_id(arg1))
        except:
            await ctx.send("leader is invalid on guild")
            return
        random.shuffle(a)
        b = []
        for i in range(int(arg)):
            char = character(a[i])
            char.transfer_guild(arg2)
            b.append(char.name)
        await ctx.send(f" {b} in Guild ID {arg1} randomly selected to be transferred to Guild ID {arg2}")

    @commands.command()
    @commands.has_role(mod_id)
    async def purge(self, ctx, arg):
        a = int(arg)
        async for message in ctx.channel.history(limit=a):
            await message.delete()


def setup(bot):
    bot.add_cog(Mod_Only_Command(bot))
