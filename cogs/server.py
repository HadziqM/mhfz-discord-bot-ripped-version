import discord
from discord.ext import commands
from direc import *
from base import *


admin = 937306936939020309


class Server_Exclusive_Command(commands.Cog):
    """ mostly only decoration command """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guild(self, ctx):
        set_up()
        mod = moderator()
        a = mod.guild_id()
        b = mod.guild_name()
        c = len(a)
        d = [mod.guild_mem(a[i]) for i in range(c)]
        e = [mod.leader_id(a[i]) for i in range(c)]
        embed = discord.Embed(title='Guilds On Server',
                              color=discord.Color.green())
        for i in range(c):
            embed.add_field(
                name=b[i], value=f'Guild ID : {a[i]}\n Member : {d[i]}/60\nLead ID : {e[i]}')
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Server_Exclusive_Command(bot))
