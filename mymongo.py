import pymongo
import json
from bson import json_util

def initialize_mongo_collection(domain, mongodb_uri):
    client = pymongo.MongoClient(mongodb_uri)
    db = client["mydatabase"]
    collection = db[domain]
    return collection

def print_document(document):
    formatted_document = json.dumps(document, indent=2, default=json_util.default)
    print(formatted_document)

def get_status_changed(collection):
    results = collection.find({"status_changed": {"$ne": False}})
    for document in results:
        print_document(document)

def get_tech_changed(collection):
    results = collection.find({"tech_changed": {"$ne": False}})
    for document in results:
        print_document(document)

def get_fresh(collection):
    query = {"fresh": {"$ne": False}}
    results = collection.find(query)
    for document in results:
        print_document(document)

def get_all(collection):
    results = collection.find()
    for document in results:
        print_document(document)

def add_domain(collection, domain):
    mydoc = {"domain": domain}
    collection.insert_one(mydoc)

def delete_domain(collection, domain):
    mydoc = {"domain": domain}
    collection.delete_one(mydoc)

def get_full(collection):
    documents = collection.find()
    for document in documents:
        print_document(document)
