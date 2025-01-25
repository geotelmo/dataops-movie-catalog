from flask import Flask, jsonify, request
from mongo_client import get_mongo_connection

FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

app = Flask(__name__)
movies_collection = get_mongo_connection()

@app.route("/movies", methods=["GET"])
def get_movies():
    print("GET /movies")
    print("Trying to fetch movies from the database")
    movies = list(movies_collection.find({}, {"_id": 0}))
    return jsonify(movies)

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)