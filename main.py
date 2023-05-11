import json

import quart
import quart_cors

from quart import request
from datetime import timezone
from dateutil import parser
from nba_api.live.nba.endpoints import scoreboard

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.get("/scoreboard")
async def get_scoreboard():
    f = "{gameId}: {awayTeam} vs. {homeTeam} @ {gameTimeLTZ}" 
    board = scoreboard.ScoreBoard()
    print("ScoreBoardDate: " + board.score_board_date)
    games = board.games.get_dict()
    data = []
    for game in games:
        gameTimeLTZ = parser.parse(game["gameTimeUTC"]).replace(tzinfo=timezone.utc).astimezone(tz=None)
        data.append(f.format(gameId=game["gameId"], awayTeam=game["awayTeam"]["teamName"], homeTeam=game["homeTeam"]["teamName"], gameTimeLTZ=gameTimeLTZ))
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/player/<string:player_name>")
async def get_player(player_name):
    from nba_api.stats.static import players
    nba_players = players.get_players()
    player = [player for player in nba_players if player['full_name'] == player_name][0]
    return quart.Response(response=json.dumps(player), status=200)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
