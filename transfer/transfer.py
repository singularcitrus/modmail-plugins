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
        content = message.replace(self.bot.prefix, "")
        names = content.split(" ")
        category = utils.get(ctx.guild.categories, id=names[0])
        await ctx.send(category.name)


def setup(bot):
    bot.add_cog(Transfer(bot))
