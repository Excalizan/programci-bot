import discord
from discord.ext import commands

class Yardım(commands.Cog):
    """Yardım Komutları"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name="yardım")
    async def yardım(self, ctx: commands.Context):
        """Yardım Penceresini Açar."""
        await ctx.send("Merhaba, tüm komutların bir listesini istiyorsan p/komutlar yazabilirsin")

    
    @commands.command(name="komutlar")
    async def komutlar(self, ctx: commands.Context):
        """Komutların Bir Listesini Gösterir"""
        embed = discord.Embed(title = "Yardım Komutları", description = "Bazı yardım Komutlarının listesi", colour = 0x00FF00)
        embed.add_field(name="p/help", value = "Yardım penceresini açar", inline=False)
        embed.add_field(name="p/yardım", value = "Neden bu komutu ekledim bilmiyorum :)", inline=False)
        embed.add_field(name="p/komutlar", value="Bu pencereyi açar", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="komutlar2")
    async def komutlar2(self, ctx: commands.Context):
        """Komutların İkinci Bir Listesini Gösterir"""
        embed = discord.Embed(title = "Genel Komutlar", description = "BGenel komut listesi listesi", colour = 0x59FFCA)
        embed.add_field(name="p/ping", value = "Botun Websocket ve API gecikmesini gösterir", inline=False)
        embed.add_field(name="p/durum", value = "Botun Durumunu Ayarlar (Sadece Yetkililer Kullanabilir)", inline=False)
        embed.add_field(name="p/durum_sıfırla", value="Botun Durumunu Sıfırlar (Sadece Yetkililer Kullanabilir)", inline=False)
        embed.add_field(name="p/snipe", value="Silinen Mesajları Görüntüleyin", inline=False)
        await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(Yardım(bot))
