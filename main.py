import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.reactions = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Replace 'TARGET_USER_ID' with the actual ID of the user you want to upvote
    # xd vision
    target_user_id = 180939123706691585

    if message.author.id == target_user_id:
        # Replace '👎' with the emoji or reaction you want to use for upvoting
        await message.add_reaction('👎')

    await bot.process_commands(message)

if __name__ == '__main__':
    bot.run('DISCORD_TOKEN')
