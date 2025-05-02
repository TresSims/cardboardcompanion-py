from discord.ext import commands


class SlashCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print("Pinging!")
        await ctx.respond("pong")
