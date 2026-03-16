from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

def get_today_games():

    today = datetime.date.today()

    url = f"https://api.balldontlie.io/v1/games?start_date={today}&end_date={today}"

    response = requests.get(url)

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
