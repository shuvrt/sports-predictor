from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    
    score_local = None
    score_visit = None
    
    if request.method == "POST":
        
        last3_local = float(request.form["last3_local"])
        home_local = float(request.form["home_local"])
        year_local = float(request.form["year_local"])
        off_local = float(request.form["off_local"])
        
        last3_visit = float(request.form["last3_visit"])
        away_visit = float(request.form["away_visit"])
        year_visit = float(request.form["year_visit"])
        off_visit = float(request.form["off_visit"])
        
        score_local = (last3_local + home_local + year_local + off_local) / 4
        score_visit = (last3_visit + away_visit + year_visit + off_visit) / 4
    
    return render_template("index.html",score_local=score_local,score_visit=score_visit)

if __name__ == "__main__":
    app.run()
