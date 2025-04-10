from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = pymongo.MongoClient(mongo_uri)

# Replace with your actual database and collection names
db = client["request_tracker"]
requests_collection = db["request"]
