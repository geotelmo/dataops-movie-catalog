from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

required_env_vars = ['MONGODB_DB', 'MONGODB_URL']
for var in required_env_vars:
    if not os.getenv(var):
        raise Exception(f"Environment variable {var} is not set")

DB_URL = os.getenv('MONGODB_URL')
DB_NAME = os.getenv('MONGODB_DB')
MOVIES_COLLECTION_NAME = 'movies'

def get_mongo_connection():
    client = MongoClient(DB_URL)
    db = client[DB_NAME]
    return db[MOVIES_COLLECTION_NAME]

if __name__ == '__main__':
    collection = get_mongo_connection()
    print("Connection established successfully")