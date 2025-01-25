# Movie Catalog Recommendation System

This project is a comprehensive movie recommendation system that leverages the [OMDb API](http://www.omdbapi.com/) and MongoDB. The system allows users to query movie information, store it in a MongoDB database, and expose the data through a Flask API.

This project is part of the exercises implemented during the DataOps bootcamp at Edit Academy.


## Getting Started

### Prerequisites

- Python 3.9
- Docker
- Docker Compose
- Valid OMDb API key (available through the [OMDb API website](http://www.omdbapi.com/))

### Setting Up the Environment

1. **Clone the repository:**

    ```bash
    git clone https://github.com/BMSihlas/dataops-movie-catalog.git <REPOSITORY_DESTINATION>
    cd <REPOSITORY_DESTINATION>
    ```

### **Running the Project**

1. **Start the movie-catalogue container:**

    This project uses environment variables to store the API key for the OMDb API. To set the environment variables, create a new copy of the `.env.example` file and name it `.env`. Then, replace the placeholders with your own values.

    ```bash
    docker-compose --env-file .env up --build  [ -d ]   # -d flag to run in detached mode
    ```

2. **Terminate the movie-catalog container:**

- To stop the container use the following command:
    ```bash
    docker-compose stop
    ```
- To fully stop and remove the container, use the following command:
    ```bash
    docker-compose down
    ```
- To remove the container and its volumes, use the following command:
    ```bash
    docker-compose down -v
    ```
