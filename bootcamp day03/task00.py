from pymongo import MongoClient
from pymongo.database import Database

def get_db(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host=host, port=port)
    db = client[db_name]
    return db


db = get_db("localhost", 27017, "noble_database")
print(db.list_collection_names())