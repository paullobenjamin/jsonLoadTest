from model import MongoConnector
from view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def generate_docs_from_file(self, model_file, num_docs, batch_size):
        self.model.generate_docs_from_model_file(model_file, num_docs, batch_size)
