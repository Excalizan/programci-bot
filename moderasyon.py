import discord
from discord.ext import commands

class Moderasyon(commands.Cog):

  def __init__(self, bot: commands.Bot):
      self.bot = bot

  @commands.command(name="kick")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason="Sebep Belirtilmemiş"):
    """Kullanıcıları Sunucudan Atın"""
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention}, {ctx.author.mention} tarafından atıldı. Sebep: [{reason}]")


  @commands.command(name="ban")
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason="Sebep Belirtilmemiş"):
    """Kullanıcıları Banlayın"""
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention}, {ctx.author.mention} tarafından banlandı. Sebep: [{reason}]")


  @commands.command(name="sil")
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, amount:int):
    """Mesajları Silin"""
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} adet mesaj silindi!")





def setup(bot):
  bot.add_cog(Moderasyon(bot))