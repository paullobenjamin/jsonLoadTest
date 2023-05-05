from pymongo import InsertOne, errors
import threading
import queue

def _bulk_insert_worker(bulk, insert_queue):
    while True:
        try:
            requests = insert_queue.get(timeout=1)
        except:
            if insert_queue.empty():
                break
        bulk_request = [InsertOne(doc) for doc in requests]
        try:
            bulk.execute(bulk_request, ordered=False)
        except errors.BulkWriteError as bwe:
            pass


def insert_docs_multi_threaded(docs, batch_size, mongo_connector):
    bulk = mongo_connector.collection.initialize_ordered_bulk_op()
    insert_queue = queue.Queue(maxsize=10)
    workers = [threading.Thread(target=_bulk_insert_worker, args=(bulk, insert_queue)) for _ in range(4)]
    for w in workers:
        w.start()
    count = 0
    for doc in docs:
        count += 1
        insert_queue.put(doc)
        if count == batch_size:
            count = 0
            insert_queue.join()
    insert_queue.join()
    bulk.execute()
    for w in workers:
        w.join()
