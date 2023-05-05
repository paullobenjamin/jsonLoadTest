from model2 import MongoModel


class MongoController(object):
    def __init__(self, model=None):
        self._model = model or MongoModel()

    def generate_docs_from_file(self, model_file, num_docs, batch_size):
        self._model.generate_docs_from_model_file(model_file, num_docs, batch_size)
