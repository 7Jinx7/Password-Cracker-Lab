# Author: Sanjana Suresh
# Web app using Flask

from flask import Flask, render_template, request
from crackerlib.analyzer import BruteForceAnalyzer

app = Flask(__name__)
DATA_FILE = "data/common_passwords.csv"

analyzer = BruteForceAnalyzer(DATA_FILE) # calk the class
analyzer.load_passwords()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form.get("password")
        seconds = analyzer.estimate_crack_time(password)
        label = analyzer.strength_label(seconds)
        suggestion = analyzer.improvement_suggestions(password)
        result = (password, seconds, label, suggestion)


    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
