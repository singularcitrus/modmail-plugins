from discord.ext import commands
from discord import utils

from core import checks
from core.models import PermissionLevel


class Transfer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def transfer(self, ctx, *, message):
        """
        Transfer a thread to a different category
        """
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Transfer(bot))
