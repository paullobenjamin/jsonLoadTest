from pymongo import MongoClient
from controller import Controller
from model import Model
from view import View

mongo_uri = "mongodb://localhost:27017/"
mongo_db = "test"
mongo_coll = "coll"

model_file = "/path/to/model.json"
num_docs = 1000
batch_size = 100

model = Model(mongo_uri, mongo_db, mongo_coll)
view = View()
controller = Controller(model, view)

controller.generate_docs_from_file(model_file, num_docs, batch_size)