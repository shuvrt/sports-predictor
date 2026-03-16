from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

def get_today_games():

    url = "https://api.balldontlie.io/v1/games?per_page=10"

    headers = {
        "Authorization": "Bearer 8ae9a654-874d-4d4b-8b79-396d21bc0759"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    games = []

    for game in data["data"]:

        games.append({
            "home": game["home_team"]["full_name"],
            "away": game["visitor_team"]["full_name"],
            "home_score": game["home_team_score"],
            "away_score": game["visitor_team_score"]
        })

    return games


@app.route("/")
def index():

    games = get_today_games()

    return render_template("index.html", games=games)


if __name__ == "__main__":
    app.run()
