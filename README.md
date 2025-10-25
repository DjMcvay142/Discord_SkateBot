# skateBot V1

A Discord bot that generates random skateboard tricks with difficulty levels. Built with Python and py-cord as a learning project.

## Features

- Random trick generation from a library of 44 tricks
- Three difficulty levels: Easy, Medium, and Hard
- Smart trick selection that avoids consecutive repeats
- Slash command interface with difficulty selection dropdown

## Commands

- `/trick` - Get a random trick from all difficulty levels
- `/trick difficulty:easy` - Get an easy trick only
- `/trick difficulty:medium` - Get a medium difficulty trick
- `/trick difficulty:hard` - Get a hard difficulty trick
- `/hello` - Greet the bot

## Trick Library

**Easy (20 tricks)**: Ollies, 180s, Pop Shuvs and their stance variations (Nollie, Fakie, Switch)

**Medium (16 tricks)**: Kickflips, Heelflips, Varial Flips, Varial Heelflips and variations

**Hard (8 tricks)**: Tre-Flips, Laser-Flips and their stance variations

## Installation

### Prerequisites
- Python 3.8 or higher
- A Discord bot token

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/skateboard-trick-bot.git
   cd skateboard-trick-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```
   TOKEN=your_discord_bot_token_here
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Getting a Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Navigate to the "Bot" section and create a bot
4. Copy the bot token and add it to your `.env` file
5. Invite the bot to your server using the OAuth2 URL Generator

## Tech Stack

- **Python 3.8+**
- **py-cord** - Modern Discord API wrapper
- **python-dotenv** - Environment variable management

## Roadmap

- [ ] Interactive embeds with button controls
- [ ] S.K.A.T.E game mode (player vs player)
- [ ] Trick statistics and user history
- [ ] Custom trick lists per server
- [ ] Combo generator (multiple tricks in sequence)

## Development

This project was created as a learning exercise for Python programming and Discord bot development as part of my Computing and Information Technology Foundation Year at Northumbria University.

### Project Structure
```
skateboard-trick-bot/
├── main.py              # Main bot code
├── requirements.txt     # Python dependencies
├── .env                 # Bot token (not tracked in git)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Contributing

This is a personal learning project, but suggestions and feedback are welcome! Feel free to open an issue if you have ideas for improvements.

## License

This project is open source and available for educational purposes.

