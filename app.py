from flask import Flask, jsonify, request
from mongo_client import get_mongo_connection
from omdb_client import fetch_movie

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

app = Flask(__name__)
movies_collection = get_mongo_connection()

@app.route("/movies", methods=["GET"])
def get_movies():
    """
    Returns all the movies stored in the database.
    """
    movies = list(movies_collection.find({}, {"_id": 0}))
    return jsonify(movies)

@app.route("/movies", methods=["POST"])
def add_movie():
    """
    Adds a new movie to the database using information from the OMDB API.
    """
    try:
        data = request.get_json()
        title = data.get("title")
        if not title:
            return jsonify({"error": "The field 'title' is required"}), 400
        
        if movies_collection.find_one({"title": {"$regex": title}}):
            return jsonify({"error": "The movie already exists"}), 400

        movie = fetch_movie(title)
        if not movie:
            return jsonify({"error": "Movie not found"}), 404
        movies_collection.insert_one(movie)
        movie.pop("_id", None)

        return jsonify({"message": "Movie added successfully", "movie": movie}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)