import json
from pymongo import MongoClient
from faker import Faker


class MongoModel(object):
    def __init__(self, uri=None, db_name=None, collection_name=None, faker=None):
        self._client = MongoClient(uri)
        self._db = self._client[db_name]
        self._collection = self._db[collection_name]
        self._faker = faker or Faker()

    def insert_one_doc(self, doc):
        self._collection.insert_one(doc)

    def insert_many_docs(self, docs):
        self._collection.insert_many(docs)

    def generate_fake_doc(self, schema):
        return {k: getattr(self._faker, v)() for k, v in schema.items()}

    def generate_fake_docs(self, schema, num_docs):
        return [self.generate_fake_doc(schema) for _ in range(num_docs)]

    def generate_docs_from_model_file(self, model_file, num_docs, batch_size):
        with open(model_file, "r") as f:
            model = json.load(f)
        docs = self.generate_fake_docs(schema=model, num_docs=num_docs)
        for i in range(0, len(docs), batch_size):
            self.insert_many_docs(docs[i:i + batch_size])
