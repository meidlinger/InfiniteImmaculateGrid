from flask import Flask, request, jsonify
from flask_cors import CORS
from GameCategories import GameCategories
from BaseballData import BaseballData

app = Flask(__name__)

CORS(app, resources={r"/get_new_grid": {"origins": "http://localhost:3000"}})

@app.route("/get_new_grid", methods=["GET"])
def get_new_grid():
    categories = GameCategories()
    return jsonify(categories.get_grid())

@app.route("/search_players", methods=["GET"])
def search_players():
    query = request.args.get("name")
    players = BaseballData.search_players(query)
    data = players
    if len(data) > 0:
        if len(data) > 5:
            data = data[:5]
        players = []
        for x in range(len(data)):
            players.append(data[x]["fullName"])
        return jsonify(players)
    return jsonify([])

@app.route("/validate_player", methods=["GET"])
def validate_player():
    query = request.args.get("name")
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")
    player = BaseballData.get_player_teams(query)
    if player:
        if team1 in player and team2 in player:
            # get player info to return
            return
    # return nothing
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)