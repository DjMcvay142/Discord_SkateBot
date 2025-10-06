import random

import discord
print(discord.__version__)
import os
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

tricks = {
    "easy": [
        "Ollie",
        "Nollie",
        "Fakie Ollie",
        "Switch Ollie",
        "Frontside-180",
        "Nollie Frontside-180",
        "Fakie Frontside-180",
        "Switch Frontside-180",
        "Backside-180",
        "Nollie Backside-180",
        "Fakie Backside-180",
        "Switch Backside-180",
        "Pop Shuv",
        "Nollie Pop Shuv",
        "Fakie Pop Shuv",
        "Switch Pop Shuv",
        "FS Pop Shuv",
        "Nollie FS Pop Shuv",
        "Fakie FS Pop Shuv",
        "Switch FS Pop Shuv"
    ],
    "medium": [
        "Kickflip",
        "Nollie Flip",
        "Fakie Flip",
        "Switch Flip",
        "Heelflip",
        "Nollie Heel",
        "Fakie Heel",
        "Switch Heel",
        "Varial Flip",
        "Nollie Varial Flip",
        "Fakie Varial Flip",
        "Switch Varial Flip",
        "Varial Heel",
        "Nollie Varial Heel",
        "Fakie Varial Heel",
        "Switch Varial Heel",

    ],
    "hard": [
        "Tre-Flip",
        "Nollie Tre-Flip",
        "Fakie Tre-Flip",
        "Switch Tre-Flip",
        "Laser-Flip",
        "Nollie Laser-Flip",
        "Fakie Laser-Flip",
        "Switch Laser-Flip",
    ]


}

previous_trick = ""

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond(f"Hey, {ctx.author.mention}! This bot is currently a work in progress. Soon there will be more features, stay tuned!")

@bot.slash_command(name="trick", description="Let the bot set a trick")
async def trick(
        ctx: discord.ApplicationContext,
        difficulty: discord.Option(str, description="Choose difficulty", required=False,
                                   choices=["easy", "medium", "hard"])
):
    global previous_trick

    # NEW: Check if difficulty was selected
    if difficulty is None:
        # No difficulty selected - use all tricks
        all_tricks = tricks["easy"] + tricks["medium"] + tricks["hard"]
    else:
        # Difficulty was selected - use only that difficulty
        all_tricks = tricks[difficulty]  # This uses the difficulty value as the key!

    # The rest stays the same
    selected_trick = random.choice(all_tricks)

    while selected_trick == previous_trick:
        selected_trick = random.choice(all_tricks)

    previous_trick = selected_trick

    await ctx.respond(f"🛹 Your trick: **{selected_trick}**")




bot.run(os.getenv('TOKEN')) # run the bot with the token
