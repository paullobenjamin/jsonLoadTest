# model.py
import json
from pymongo import MongoClient
from faker import Faker
from faker_schema import SchemaGenerator
from .insert import insert_docs_multi_threaded

class MongoConnector:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        
    def generate_docs_from_model_file(self, model_file, num_docs, batch_size):
        with open(model_file, 'r') as f:
            model = json.load(f)
        generator = SchemaGenerator(model)
        fake = Faker()
        docs = generator.generate(num_docs, fake=fake)
        insert_docs_multi_threaded(docs, batch_size, self.mongo_connector)
        self.view.show_message(f"{num_docs} documents generated and inserted successfully!")
