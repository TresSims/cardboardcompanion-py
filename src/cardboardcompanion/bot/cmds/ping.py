import discord
from cardboardcompanion import cfg
from cardboardcompanion.bot import bot


@bot.slash_commands()
async def ping_pong(ctx):
    await ctx.sent("pong")
