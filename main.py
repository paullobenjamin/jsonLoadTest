import argparse
from pymongo import MongoClient
from controller import Controller
from model import MongoConnector
from view import View

# Configuração do argparse para receber os parâmetros da linha de comando
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--uri", help="URI do MongoDB")
parser.add_argument("-d", "--database", help="Nome do banco de dados")
parser.add_argument("-c", "--collection", help="Nome da coleção")
parser.add_argument("-n", "--num_docs", type=int, help="Número de documentos a gerar e inserir")
parser.add_argument("-b", "--batch_size", type=int, help="Tamanho do lote de inserção")
parser.add_argument("-f", "--model_file", help="Caminho para o arquivo de modelo JSON")

args = parser.parse_args()

# Leitura dos parâmetros da linha de comando
mongo_uri = args.uri or "mongodb+srv://pbenjamin:dba%401qaz%40WSX@sandbox.ljwxo.mongodb.net/"
mongo_db = args.database or "test"
mongo_coll = args.collection or "coll"
num_docs = args.num_docs or 1000
batch_size = args.batch_size or 100
model_file = args.model_file or "./user_basic_interior_tag.json"

model = MongoConnector(mongo_uri, mongo_db, mongo_coll)
view = View()
controller = Controller(model, view)

controller.generate_docs_from_file(model_file, num_docs, batch_size)