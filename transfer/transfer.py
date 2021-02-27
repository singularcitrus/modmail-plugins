from discord.ext import commands
import discord

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
        if message.isnumeric():
            category_id = int(message)
            category = discord.utils.get(ctx.message.guild.categories, id=category_id)
            await ctx.send("Transferring you to the `" + category.name + "` Department")


def setup(bot):
    bot.add_cog(Transfer(bot))
