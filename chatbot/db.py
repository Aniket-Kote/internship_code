import pymongo
from pymongo.errors import PyMongoError
import os
def get_mongo_client(uri):
    """Initialize and return a MongoDB client."""
    try:
        client = pymongo.MongoClient(uri)
        print("MongoDB client connected successfully.")
        return client
    except PyMongoError as e:
        raise RuntimeError(f"Failed to connect to MongoDB: {e}")

# MongoDB connection setup
MONGO_URI = os.getenv("MONGO_URI")
db_name = "internshipData"
collection_name = "questions"

try:
    myclient = get_mongo_client(MONGO_URI)
    mydb = myclient[db_name]
    mycol = mydb[collection_name]
except Exception as e:
    print(f"Error during MongoDB setup: {e}")
    raise

def insert_data(data):
    # Insert a single document into the collection.
    # Args:
    #     data (dict): The data to be inserted.
    # Returns:
    #     bool: True if insertion is successful, False otherwise.
    
    if not isinstance(data, dict):
        return False

    try:
        mycol.insert_one(data)
        return True
    except PyMongoError as e:
        print(f"Error inserting data into MongoDB: {e}")
        return False
