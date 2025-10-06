import random  # For selecting random tricks from lists
import discord  # The py-cord library for Discord bot functionality

print(discord.__version__)  # Print the version for debugging purposes
import os  # For accessing environment variables
from dotenv import load_dotenv  # For loading .env file

# Load environment variables from .env file (like bot token)
load_dotenv()

# Create the bot instance
bot = discord.Bot()

# Dictionary storing all tricks organized by difficulty level
# Keys are difficulty levels, values are lists of trick names
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

# Global variable to track the last trick given
# This prevents the same trick from appearing twice in a row
previous_trick = ""


# Event that fires when the bot successfully connects to Discord
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


# Simple greeting command to test bot functionality
@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond(
        f"Hey, {ctx.author.mention}! This bot is currently a work in progress. Soon there will be more features, stay tuned!")


# Main trick command - displays an embed with interactive menu
@bot.slash_command(name="trick", description="Let the bot set a trick")
async def trick(ctx: discord.ApplicationContext):
    # Create the initial embed (the visual message box)
    embed = discord.Embed(
        title="🛹 Skateboard Trick Generator",  # Title at the top
        description="Select difficulty from the menu below to get a random trick!",  # Main text
        color=0x43B581  # Green color (hex format: 0xRRGGBB)
    )

    # View class for the "Try Again" button
    # This appears after a trick is shown to reset the menu
    class TryAgainView(discord.ui.View):
        def __init__(self):
            super().__init__()  # Initialize the parent View class

        # Decorator that creates a button in the view
        @discord.ui.button(label="Try Again", style=discord.ButtonStyle.green, emoji="🔄")
        async def try_again_button(self, button: discord.ui.Button, interaction: discord.Interaction):
            # When clicked, recreate the original menu embed
            original_embed = discord.Embed(
                title="🛹 Skateboard Trick Generator",
                description="Select difficulty from the menu below to get a random trick!",
                color=0x43B581
            )

            # Create a new instance of TrickView (the select menu)
            new_view = TrickView()

            # Edit the message to show the original menu again
            await interaction.response.edit_message(embed=original_embed, view=new_view)

    # View class for the main difficulty selection menu
    class TrickView(discord.ui.View):
        def __init__(self):
            super().__init__()  # Initialize the parent View class

        # Decorator that creates a select menu (dropdown) in the view
        @discord.ui.select(
            placeholder="Choose difficulty...",  # Text shown before selection
            min_values=1,  # User must select at least 1 option
            max_values=1,  # User can select at most 1 option
            options=[  # List of options in the dropdown
                discord.SelectOption(label="Easy", description="Basic tricks", emoji="🟢"),
                discord.SelectOption(label="Medium", description="Intermediate tricks", emoji="🟡"),
                discord.SelectOption(label="Hard", description="Advanced tricks", emoji="🔴"),
                discord.SelectOption(label="Random", description="Surprise me!", emoji="🎲"),
            ]
        )
        # Callback function that runs when user selects an option
        async def select_callback(self, select: discord.ui.Select, interaction: discord.Interaction):
            global previous_trick  # Access the global variable to track last trick

            # Get what the user selected (returns a list, we take the first item)
            selected = select.values[0]  # Will be "Easy", "Medium", "Hard", or "Random"

            # STEP 1: Determine which tricks to choose from based on selection
            if selected == "Random":
                # For Random, combine all difficulty levels into one list
                trick_list = tricks["easy"] + tricks["medium"] + tricks["hard"]
            else:
                # For specific difficulty, access that key in the tricks dictionary
                # selected.lower() converts "Easy" to "easy" to match dictionary keys
                trick_list = tricks[selected.lower()]

            # STEP 2: Select a random trick, avoiding consecutive repeats
            selected_trick = random.choice(trick_list)  # Pick random trick from list

            # If the trick matches the previous one, keep picking until we get a different one
            while selected_trick == previous_trick:
                selected_trick = random.choice(trick_list)

            # Update the global variable to remember this trick for next time
            previous_trick = selected_trick

            # STEP 3: Determine the embed color based on difficulty selected
            colors = {
                "Easy": 0x43B581,  # Green
                "Medium": 0xF1C40F,  # Yellow/Gold
                "Hard": 0xE74C3C,  # Red
                "Random": 0x9B59B6  # Purple
            }
            embed_color = colors[selected]  # Get the color for this difficulty

            # STEP 4: Create a new embed to display the selected trick
            new_embed = discord.Embed(
                title="🛹 Your Trick",  # New title
                description=f"**{selected_trick}**",  # Trick name in bold
                color=embed_color  # Color based on difficulty
            )
            # Add a field showing which difficulty was selected
            new_embed.add_field(name="Difficulty", value=f"{selected}", inline=True)
            # Add a footer message
            new_embed.set_footer(text="Good luck! 🤙")

            # STEP 5: Update the message with the new embed and Try Again button
            try_again_view = TryAgainView()  # Create instance of the Try Again view
            # Edit the original message to show the trick and new button
            await interaction.response.edit_message(embed=new_embed, view=try_again_view)

    # Create an instance of the TrickView (the initial select menu)
    view = TrickView()

    # Send the initial embed with the select menu to Discord
    await ctx.respond(embed=embed, view=view)


# Run the bot using the token from the .env file
bot.run(os.getenv('TOKEN'))
