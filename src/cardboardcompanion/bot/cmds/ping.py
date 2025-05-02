from discord import ApplicationCommand


async def ping(ctx):
    print("Pinging!")
    await ctx.respond("pong")


PingPong = ApplicationCommand(ping)
