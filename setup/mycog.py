import discord
from redbot.core import commands

class MyCog(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def setup(self,ctx) : 
      embed=discord.Embed(title="Setup", description="How to setup MagicBot exclusively for your server", color=0xFF5733)
      await ctx.send(embed=embed)
