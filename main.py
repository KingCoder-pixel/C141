from flask import Flask, jsonify, request
import csv
all_movies = []

#fetching data
with open('movies.csv','r', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

#creating empty list
like_movies = []
notLike_movies = []
didNot_watch = []

#creating object of flask
app = Flask(__name__)

#first api to get all movies detail
@app.route("/getMovie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })
    

#api to like movies
@app.route("/like_movie", methods = ["POST"])
def liked_Movie():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    liked_Movie.append(movies)
    return jsonify({
        "status": "success"
    }),201

@app.route("/Unliked_Movie", methods = ["POST"])
def notLiked_Movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    notLiked_Movies.append(movies)
    return jsonify({
        "status": "success"
    }),201

@app.route("/NotWatched_Movie", methods = ["POST"])
def notWatched_Movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    didNot_watch.append(movies)
    return jsonify({
        "status": "success"
    }), 201
#to execute api

if __name__ == "__main__":
  app.run()
