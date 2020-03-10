# 패치노트.
# rev 1.0 - 봇생성 / 기타 잡다한 기능 추가
# rev 1.1 - timestamp추가 / 


import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import time
#import youtube_dl
#from urllib.request import urlopen, Request
#import urllib
#import urllib.request

client = commands.Bot(command_prefix = '.')
client.remove_command("help")
token = 'token here :)'

@client.event
async def on_ready():
    print("Aria public version.")
    print("Bot_ready.")
    print(client.user.id)
    print("----------------")
    game = discord.Game("저는 Aria 에요! | .help")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command(pass_context=True) #후스의 와티스 배끼기(킹작권 ㅌㅌ)
async def help(ctx):
    embed = discord.Embed(
            title="Aria / rev1.1(Host with Heroku(after.)) / **도움말!**",
            description="> .help\n```Aria의 도움말을 볼수 있어요```\n> .ping\n```서버와 Discord 클라이언트 지연 시간을 확인할수 있어요```\n> .invite\n```저를 다른 서버에 초대할수 있어요```\n> .update\n```패치노트를 확인할수 있어요.```",
            timestamp=datetime.datetime.utcnow(),
            color=0xff5733
    )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(
            title=":ping_pong: L a t e n c y",
            description="현재 당신의 핑은 **" + str(int(client.latency * 1000)) + "ms** 예요.",
            timestamp=datetime.datetime.utcnow(),
            color=0x9feddb
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(
            title=":mailbox_with_mail: 저를 초대하고 싶으신가요?!",
            description="[여기](https://discordapp.com/oauth2/authorize?client_id=봇ID를 입력하세요&permissions=8&scope=bot)를 눌러 저를 초대할수 있어요!",
            timestamp=datetime.datetime.utcnow(),
            color=0x9fc2ed
        )
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def update(ctx):
    embed = discord.Embed(
            title=":notebook_with_decorative_cover: **패 치 노 트** :",
            description="# **__Aria의 패치노트에요. 아래를 참고하세요!__**\n# **개발자 연락처** : `! 𝘿𝙀𝙁𝙀𝘼𝙏 𝙄𝙉𝙎𝘼𝙉𝙀#7308`\n\n> rev 1.0(Date : ?)\n```봇 생성, 기능 추가```\n> rev 1.1(Date : 20200226)\n```TimpeStamp추가```",
            timestamp=datetime.datetime.utcnow(),
            color=0xffffff
        )
    await ctx.send(embed=embed)

# <!-- MUSIC / DISABLE / Bug--!>
#@client.command(pass_context=True)
#async def join(ctx):
#    channel = discord.voice.voice_channel
#    server = message.server
#    voice_client = client_voice_client_in(server)
#    print("아래 채널에 접속했어요 :")
#    print(voice_client)
#    if voice_client== None:
#        embed = discord.Embed(
#                title=":wave: 안녕!",
#                description="제가 등장했어요! ヾ(•ω•`)o",
#                color=0xdaeaff
#            )
#        await ctx.send(embed=embed)
#        await client.join.voice_channel(channel)
#    else:
#        await ctx.send("제가 이미 들어가 있는데.. 또 부르고 싶으신가요?")

@client.command(pass_context=True)
async def shutdown(ctx): #셧다운
    if str(ctx.message.author.id) == "개발자 Discord user id (개발자모드 키고 ID복사 ㄱㄱ)":
        embed = discord.Embed(
                title=":wave: `Shutdown..`",
                description="잘있어요!",
                color=0xffffff
        )
        await ctx.send(embed=embed)
        await client.close()
    else:
        embed = discord.Embed( 
                title=":warning: **이런!**",
                description="**현재 이 명령어를 사용 할 수 있는 권한은 <@개발자디코 유저id> (소유자) 밖에 없어요!\n소유자에게 연락을 해주세요!**",
                color=0xfd0101
        )
        await ctx.send(embed=embed)

client.run(token)