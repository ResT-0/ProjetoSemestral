# api/db.py
from pymongo import MongoClient

def get_db_collections(mongo_uri):
    client = MongoClient(mongo_uri)
    db = client['ListasDeCompras']
    tasks_collection = db['items']
    users_collection = db['users']
    return tasks_collection, users_collection
