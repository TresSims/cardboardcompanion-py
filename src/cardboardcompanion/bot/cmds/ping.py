import discord


async def ping_pong(ctx):
    await ctx.sent("pong")


PingCommand = discord.SlashCommand(ping_pong)
