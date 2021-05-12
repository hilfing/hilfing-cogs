
import discord
from redbot.core import commands

class newhelp(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def help(self,ctx) :
      def check(reaction, user):
        return reaction.message.id == msg.id and user == ctx.author #msg.id is the id of the embed sent by the bot.

      page = 0

      while True: #can be changed to a variable to let it work a certain amount of times.
        try:
          reaction, _ = await bot.wait_for('reaction_add', timeout= 20.0, check=check)
          if reaction.emoji == 'emote of choice here' and page > 0:
           page -= 1
           embed = discord.Embed(title='Title Here', description=pages[page]
          await msg.edit(embed=embed)
          if reaction.emoji == 'emote of choice here' and page < len(pages) -1:
           page += 1
           embed = discord.Embed(title='Title Here', description= pages[page]
          await msg.edit(embed=embed)
         except asyncio.TimeoutError:
          pass
