import discord
from datetime import datetime
from discord.ext import commands

class Yasa(commands.Cog):
    """Yasa Komutları"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @commands.command(name="yasa1")
    async def yasa1(self, ctx: commands.Context):
        """Yasaların Bir Listesini Gösterir"""
        embed = discord.Embed(title = "Yasalar - 1", description = "İlk 5 Yasanın Listesi", colour = 0xFF8C00)
        embed.add_field(name="1. Spam Yasak", value = "Tahmin edeceğiniz gibi spam ban sebebidir. Yani, spam yapmayın, botlarımız tetikte!", inline=False)
        embed.add_field(name="2. Gerekli Olmadıkça Yetkililerden Bahsetmeyin", value = "Eğer yardıma ihtiyacınız olursa @Yardımcı lardan bahsedebilirsiniz, ancak @Admin ve @Moderatör lerden gerekmedikçe bahsetmeyin.", inline=False)
        embed.add_field(name="3. Reklam Kanalı Hariç Reklam Yasak", value="Reklam kanalı dışında kendinizin veya başkasının reklamını yapmak yasaktır. Nasıl reklam paylaşılır için (bkz: #reklam )", inline=False)
        embed.add_field(name="4. Müzik Botlarını Boşuna Meşgul Etmeyin", value = "Biliyorsunuz sunucuda sayılı müzik botu var, bu yüzden herkes aynı anda müzik dinleyemez. Bunun için kullanmadığınız zamanlarda botu kapatmanız rica olunur.", inline=False)
        embed.add_field(name="5. Küfür Kullanmak Yasak", value = "Metin kanallarında insanlara küfür etmek hoş değil! Botlarımız sürekli kanalları tarıyor, yani küfür etmeyin.", inline=False)
        await ctx.send(embed=embed)


    @commands.command(name="yasa2")
    async def yasa2(self, ctx: commands.Context):
        """Yasaların Bir Listesini Gösterir"""
        embed = discord.Embed(title = "Yasalar - 2", description = "Son 5 Yasanın Listesi", colour = 0x9D70F9)
        embed.add_field(name="6. Birisi Sizi Rahatsız Ederse Bildirmekten Çekinmeyin", value = "Eğer birisi sizi rahatsız edecek davranışlarda bulunuyorsa online bir @Moderatör e veya @Admin e başvurabilirsiniz. Eğer online bir yetkili göremiyorsanız, @ModMail botuna mesaj atın ve sorununuzu bildirin, emin olun ki sorunu görürüz.", inline=False)
        embed.add_field(name="7. Fikirlere Saygı Duyun", value = "Herkes sizin sevdiğiniz animeyi sevmek zorunda değil, ya da desteklediğiniz futbol takımını desteklemek zorunda değil. Fikirlere saygı duymalısınız.", inline=False)
        embed.add_field(name="8. DM Reklamcılığı Yasaktır", value = "DM reklamcılarını kimse sevmez. Eğer bir reklam yapmak istiyorsanız, #reklam  kanalımız mevcut. Duyarlı olun.", inline=False)
        embed.add_field(name="9. Kimseden Kişisel Bilgi İstemeyin", value = "Bir kişiden kişisel bilgilerini istemek rahatsız edici bir davranıştır, kimse kimseye karışmasın.", inline=False)
        embed.add_field(name="10. Önerileriniz İçin DM Yolunu Kullanmayın", value = "Sunucmuz için bir öneriniz olduğunda, bunu #öneri kanalında yapın, yetkililere DM atmayın. Düzenli olarak #öneri kanalını kontrol ediyoruz. ", inline=False)
        await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(Yasa(bot))
