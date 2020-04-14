import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='.')
client.remove_command('help')
token = "Njk3NzYzMDk2NjE3Mjg3ODAw.XpU5zg.MCR3zx-7jwaMxGIAunG38NyqffE"

ball8 = ['As I see it, yes', 'Ask again later', ' Better not tell you now', 'Cannot predict now.',
         'Concentrate and ask again.', ' Don’t count on it.', 'It is certain.', "It is decidedly so.",
         'Most likely.', 'My reply is no.']

bedwars_tips = ['`Bedwars is not just a game its a feel, feel it.`',
               '**Teamwork** `is very important if u play teams, dont be a resource hog`',
               '**YOU CANT BECOME ANY BETTER**,`im sorry if that hurts`',
               '`subscribe to Rebox you will become legend instantly`',
               ]

welcome_message = f""":partying_face:   Thanks for joining us We are so grateful to have u  :partying_face:"""


@client.event
async def on_ready():
    print('ready')


@client.event
async def on_message(message):
    if (message.content.find('hello') != -1) or (message.content.find('Hello') != -1):
        await message.channel.send('Hi!')

    await client.process_commands(message)


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, args):
    await ctx.send(f'Your question was {args} and my answer is `{random.choice(ball8)}`')


@client.command()
async def bedwarstips(ctx):
    await ctx.send(random.choice(bedwars_tips))


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! `{round(client.latency * 1000)}ms`')


@client.event
async def on_member_join(member):
    await member.send(welcome_message)


@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        colour=discord.Colour.orange()
    )
    embed.set_author(name="Help")
    embed.add_field(name='.ping', value='to check your ping', inline=False)
    embed.add_field(name='.bedwars_tips', value='type it to get bedwars tips', inline=False)
    embed.add_field(name='.8ball <your question>', value='ask a question and know ur luck', inline=False)
    await ctx.send(embed=embed)


client.run(token)