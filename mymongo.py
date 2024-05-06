
import pymongo
import json
from bson import json_util

class MongoOperations:
    def __init__(self, domain):
        self.mongodb_uri = "mongodb://localhost:27017"
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client["mydatabase"]
        self.collection = self.db[domain]
        self.collection2 = self.db["domains"]

    def print_document(self, document, only_sub=False):
        if only_sub:
            print(document.get("sub", "No subdomain found"))
        else:
            formatted_document = json.dumps(document, indent=2, default=json_util.default)
            print(formatted_document)

    def get_status_changed(self, only_sub):
        results = self.collection.find({"status_changed": {"$ne": False}})
        for document in results:
            self.print_document(document, only_sub)

    def get_tech_changed(self, only_sub):
        results = self.collection.find({"tech_changed": {"$ne": False}})
        for document in results:
            self.print_document(document, only_sub)

    def get_fresh(self, only_sub):
        results = self.collection.find({"fresh": {"$ne": False}})
        for document in results:
            self.print_document(document, only_sub)

    def get_all_sub(self):
        results = self.collection.find()
        for document in results:
            print(document.get("sub", "No subdomain found"))

    def add_domain(self):
        mydoc = {"domain": self.collection.name}
        self.collection2.insert_one(mydoc)

    def remove_domain(self):
        mydoc = {"domain": self.collection.name}
        self.collection2.delete_one(mydoc)

    def get_full(self):
        documents = self.collection.find()
        for document in documents:
            self.print_document(document)

    def filter_status(self, status, only_sub):
        query = {"status": int(status)} if status and status is not True else {"status": {"$ne": None}}
        documents = self.collection.find(query)
        for document in documents:
            self.print_document(document, only_sub)

    def filter_tech(self, tech, only_sub):
        regex_pattern = f"(?i){tech}" if tech and tech is not True else {"tech": {"$ne": None}}
        query = {"tech": {"$regex": regex_pattern}} if tech and tech is not True else {"tech": {"$ne": None}}
        documents = self.collection.find(query)
        for document in documents:
            self.print_document(document, only_sub)
