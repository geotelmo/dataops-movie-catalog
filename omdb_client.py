from dotenv import load_dotenv
import os
import requests

load_dotenv()

required_env_vars = ['OMDB_API_URL', 'OMDB_BASE_KEY']
for var in required_env_vars:
    if not os.getenv(var):
        raise Exception(f"Environment variable {var} is not set")

OMDB_API_URL = os.getenv('OMDB_API_URL')
OMDB_BASE_KEY = os.getenv('OMDB_BASE_KEY')

def fetch_movie(title):
    """
    Searches information about a movie by its title using the OMDB API.
    Returns a dictionary with the data about the moview or `None` if the movie was not found.
    """
    params = {
        "apikey": OMDB_BASE_KEY,
        "t": title,
    }
    response = requests.get(OMDB_API_URL, params=params)
    if response.status_code == 200 and response.json().get("Response") == "True":
        return {
            "title": response.json().get("Title"),
            "year": response.json().get("Year"),
            "genre": response.json().get("Genre"),
            "director": response.json().get("Director"),
            "imdb_rating": response.json().get("imdbRating"),
        }
    return None

if __name__ == "__main__":
    movie_title = "Inception"
    movie = fetch_movie(movie_title)
    print(movie)