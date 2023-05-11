# ChatGPT NBA Stats API Plugin

This plugin is an experiment using the NBA's APIs to make their data & statistics easily accessible in ChatGPT.  This plugin is currently only available for local install & use, but I am open to the option of hosting the API for public availability. Open to feedback, issues, and pull requests (create an issue first for discussion). 

Built with the [nba_api](https://github.com/swar/nba_api) client to access NBA APIs.  


![Scoreboard Screenshot](/examples/screenshots/scoreboard.png)

![Player Screenshot](/examples/screenshots/player.png)

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

Start asking a question relevant to the plugin, like "Is Raymond Felton still active in the NBA?", or "Get me today's games."

## Endpoints
- `/scoreboard`: Get today's scheduled NBA games.  Returns results in the format below: 
  - `{gameId}: {awayTeam} vs. {homeTeam} @ {gameTimeLTZ}`
  - Example: `Celtics vs. 76ers at 7:30 PM Eastern Time`
- `/player/:player_name`: Returns basic information about the requested player, notably if they are active or not.
