from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

genres = [
    "Action",
    "Adventure",
    "Animation",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Family",
    "Fantasy",
    "History",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Sport",
    "Thriller",
    "War",
    "Western"
    ]

@app.route("/")
def home():

    years = []
    for year in range(1920, 2021):
        years.append(year)

    ratings = []
    for rating in range(1, 11):
        ratings.append(rating)

    return render_template('filterbar.html', years=years, ratings=ratings, genres=genres)


app.run(debug=True)

app.run(host="0.0.0.0", port=5001)