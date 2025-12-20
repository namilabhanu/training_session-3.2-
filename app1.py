from flask import Flask, render_template, request
import random

app = Flask(__name__)

quotes = {
    "Motivation": [
        "The best way to get started is to quit talking and begin doing. - Walt Disney",
        "Don't let yesterday take up too much of today. - Will Rogers",
        "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
        "If you are working on something exciting, it will keep you motivated. - Unknown",
        "Success is not in what you have, but who you are. - Bo Bennett"
    ],
    "Life": [
        "Life is what happens when you're busy making other plans. - John Lennon",
    ],
    "Success": [
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "Don't be afraid to give up the good to go for the great. - John D. Rockefeller"
    ]   

}

@app.route("/", methods=["GET", "POST"])
def Home():
    quote = ""
    if request.method == "POST":
        topic = request.form.get("topic")
        quote = random.choice(quotes.get(topic, ["No quotes available for this topic."]))
        return render_template("index.html", quote=quote)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)