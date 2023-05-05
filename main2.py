import argparse
from controller2 import MongoController
from model2 import MongoModel


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate fake documents from JSON schema and insert them into MongoDB')
    parser.add_argument('uri', nargs='?', type=str, help='MongoDB connection string', default="mongodb+srv://pbenjamin:dba%401qaz%40WSX@cluster0.ljwxo.mongodb.net")
    parser.add_argument('db_name', nargs='?', type=str, help='Database name', default="loadTester")
    parser.add_argument('collection_name', nargs='?', type=str, help='Collection name', default="testing")
    parser.add_argument('model_file', nargs='?', type=str, help='JSON schema file', default="model.json")
    parser.add_argument('num_docs', nargs='?', type=int, help='Number of fake documents to generate', default=1000)
    parser.add_argument('batch_size', nargs='?', type=int, help='Batch size for bulkWrite operation', default=100)
    args = parser.parse_args()
    
    if args.uri is None:
        args.uri = 'mongodb://localhost:27017'
    if args.db_name is None:
        args.db_name = 'test'
    if args.collection_name is None:
        args.collection_name = 'test'
    if args.model_file is None:
        args.model_file = 'model_file.json'
    if args.num_docs is None:
        args.num_docs = 1000
    if args.batch_size is None:
        args.batch_size = 100

    controller = MongoController(model=MongoModel(uri=args.uri, db_name=args.db_name, collection_name=args.collection_name))
    controller.generate_docs_from_file(args.model_file, args.num_docs, args.batch_size)
