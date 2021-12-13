import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!', description = "你好，我是千遇工作室的客服小姐姐")
client = discord.Client()
channel = bot.get_channel(896622684291620866)


@client.event
async def on_message(message):
    if message.author == client.user:
        return


@client.event
async def on_ready():
    print('目前登入身份：', client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '你好':
        await message.channel.send('你好，请问需要什么服务')
    if message.content == '欢迎':
        await message.channel.send('欢迎加入千遇工作室服务器，请问是老板还是陪陪呢？')
    if message.content == '陪陪':
        await message.channel.send('https://imgtu.com/i/oXYKFP')
    if message.content == '老板':
        await message.channel.send('https://discord.gg/ZRVSJ4rdz4')

client.run('OTE5ODUwNzgwNzMzODg2NDY0.YbbzzA.k49JECp50FUHkT_kKvqpH5CZqyM')