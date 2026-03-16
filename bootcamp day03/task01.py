from task00 import get_db
from pymongo import MongoClient
from pymongo.database import Database
import os
import json

def import_data(db: Database, data_path: str) -> None:

    for filename in os.listdir(data_path):
        if filename.endswith(".json"):
            collection_name = filename.replace(".json", "")
            collection = db[collection_name]

            with open(os.path.join(data_path, filename), "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                collection.insert_many(data)
            else:
                collection.insert_one(data)

if __name__ == "__main__":
    db = get_db("localhost", 27017, "noble_database")
    import_data(db, "./data")
    print(db.list_collection_names())



