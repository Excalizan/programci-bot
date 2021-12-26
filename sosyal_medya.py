import discord
from discord.ext import commands

class Sosyal_Medya(commands.Cog):
    """Sosyal Medya Hesapları"""
      
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="youtube")
    async def youtube(self, ctx: commands.Context):
      """Kodla Bakalım Youtube Kanalı"""
      await ctx.send("İşte Kodla Bakalım Youtube Kanalının Linki:")
      await ctx.send("https://www.youtube.com/channel/UC_0vGVggvyIVAqvS0X0rd3w")


    @commands.command(name="github")
    async def github(self, ctx: commands.Context):
      """Kodla Bakalım GitHub Hesabı"""
      await ctx.send("İşte Kodla Bakalım Github Hesabının Linki:")
      await ctx.send("https://github.com/Ozan-Kement")

    
    @commands.command(name="discord")
    async def discord(self, ctx: commands.Context):
      """Programcının Yeri Discord Sunucusu"""
      await ctx.send("İşte Programcının Yeri Discord Sunucusunun Davet Linki:")
      await ctx.send("https://discord.gg/zWJDv2UQAu")

    
    @commands.command(name="oy")
    async def oy(self, ctx: commands.Context):
      """Programcının Yeri Oylama Sayfası"""
      await ctx.send("İşte Programının Yeri top.gg Oylama Sayfasının Linki:")
      await ctx.send("https://top.gg/servers/832241473370062848/vote")



def setup(bot: commands.Bot):
    bot.add_cog(Sosyal_Medya(bot))