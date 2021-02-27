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
    @checks.thread_only()
    async def transfer(self, ctx, *, message):
        """
        Transfer a thread to a different category
        """
        message_split = message.split(" ")
        if message[0].isnumeric():
            category_id = int(message_split[0])
            category = discord.utils.get(ctx.message.guild.categories, id=category_id)
            await ctx.thread.channel.edit(category=category)
            if "silent" not in message_split:
                new_message = await ctx.send("Transferring you to the `" + category.name + "` Department")
                await ctx.thread.reply(new_message, anonymous=True)


def setup(bot):
    bot.add_cog(Transfer(bot))
