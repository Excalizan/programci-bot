import time
import discord
from discord.ext import commands


class Komutlar(commands.Cog):
    """Birkaç Basit Komut."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None


    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

    
    @commands.command(name="snipe")
    async def snipe(self, ctx: commands.Context):
        """Silinen Mesajları Görüntüleyin."""
        if not self.last_msg:
            await ctx.send("Görüntülenecek mesaj yok!")
            return

        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title=f"{author} kişisinden mesaj", description=content)
        await ctx.send(embed=embed)



    @commands.command(name="durum")
    @commands.has_any_role(832242250351116329, 832241680706830398)
    async def durum(self, ctx: commands.Context, *, text: str):
        """Botun Durumunu Ayarlar (Sadece Yetkililer Kullanabilir)."""
        await self.bot.change_presence(activity=discord.Game(name=text))
        await ctx.send(f"Botun durumu '{text}' olarak ayarlandı")


    @commands.command(name="durum_sıfırla")
    @commands.has_any_role(832242250351116329, 832241680706830398)
    async def durum_sıfırla(self, ctx: commands.Context):
        """Botun Durumunu Sıfırlar (Sadece Yetkililer Kullanabilir)."""
        await self.bot.change_presence(activity=discord.Game('Programcının Botu | Excalizan#7330'))
        await ctx.send("Botun durumu sıfırlandı")


    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Botun Anlık Websoket ve API Gecikmesi."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")


    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(840118941611327508)

        if not channel:
            return

        await channel.send(f"Programcının Yeri'ne Hoşgeldin, @{member}!")

def setup(bot: commands.Bot):
    bot.add_cog(Komutlar(bot))
