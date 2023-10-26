import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a king {bot.user}!')


@bot.command()
async def panduan_praktik_ramah_lingkungan(ctx):
    await ctx.send('''
- Kurangi Penggunaan Plastik Sekali Pakai:
- Pilih Transportasi Ramah Lingkungan
- Gunakan Botol Air dan Tas Belanja Sendiri
- Daur Ulang Sampah Anda
- Gunakan Transportasi Umum
- Hindari Penggunaan Sedotan Plastik 
                   ''')
    

@bot.command()
async def cara_mengurangi_limbah(ctx):
    await ctx.send('''
- Manfaatkan Sampah Organik Sebagai Pupuk Kompos
- Hindari Barang Sekali Pakai
- Perbanyak Recycle, Reuse, Reduce
                   ''')
    

@bot.command()
async def apa_itu_limbah(ctx):
    await ctx.send('Material tak diinginkan, perlunya pengelolaan hati-hati untuk hindari pencemaran')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def coy(ctx, count_coy = 5):
    await ctx.send("coy" * count_coy)

bot.run("")
